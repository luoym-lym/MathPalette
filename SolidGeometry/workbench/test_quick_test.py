"""Offline API mocks; all runtime and review files use an isolated fixture."""
import base64
import copy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

from quick_test import QuickTests, TEST_PROFILES, call_minimax, load_api_key, parse_response
from review_store import Workbench
from server import make_handler
from workbench_io import WorkbenchError, load_config

PROJECT = Path(__file__).resolve().parents[2]
KEY = "sk-cp-quick-test-fixture"
RESULT = {"answer": "(2, 2)", "thinking": "Fixture reasoning <script>never execute</script>",
          "usage": {"total_tokens": 30}, "finish_reason": "stop", "response_model": "MiniMax-M3", "truncated": False}
SETTINGS = {"model": "MiniMax-M3", "api_base": "https://api.minimaxi.com/v1"}


class ClientTests(unittest.TestCase):
    def test_payload_disables_thinking_without_output_or_waiting_limit(self):
        response = {"model": "MiniMax-M3", "choices": [{"message": {
            "content": "final"}, "finish_reason": "stop"}]}
        with patch("quick_test.build_opener") as opener:
            opener.return_value.open.return_value = io.BytesIO(json.dumps(response).encode())
            result = call_minimax(SETTINGS, KEY, "QUESTION ONLY", b"exact candidate PNG")
            request = opener.return_value.open.call_args.args[0]
            self.assertIsNone(opener.return_value.open.call_args.kwargs["timeout"])
        payload = json.loads(request.data)
        self.assertEqual(result["answer"], "final")
        self.assertEqual(result["thinking"], "")
        self.assertEqual(payload["model"], "MiniMax-M3")
        self.assertEqual(payload["thinking"], {"type": "disabled"})
        self.assertNotIn("reasoning_effort", payload)
        self.assertNotIn("max_tokens", payload)
        self.assertNotIn("max_completion_tokens", payload)
        self.assertEqual(payload["messages"][1]["content"][0]["text"], "QUESTION ONLY")
        url = payload["messages"][1]["content"][1]["image_url"]["url"]
        self.assertEqual(base64.b64decode(url.split(",", 1)[1]), b"exact candidate PNG")
        self.assertNotIn(KEY, request.data.decode())
        self.assertEqual(request.full_url, "https://api.minimaxi.com/v1/chat/completions")

    def test_flash_preview_uses_adaptive_thinking_and_low_effort(self):
        response = {"model": "MiniMax-M3.1-Flash-Preview", "choices": [{"message": {
            "content": "final", "reasoning_content": "brief reasoning"}, "finish_reason": "stop"}]}
        settings = {**SETTINGS, **TEST_PROFILES["quicktest2"]}
        with patch("quick_test.build_opener") as opener:
            opener.return_value.open.return_value = io.BytesIO(json.dumps(response).encode())
            result = call_minimax(settings, KEY, "QUESTION ONLY", b"exact candidate PNG")
            request = opener.return_value.open.call_args.args[0]
            self.assertIsNone(opener.return_value.open.call_args.kwargs["timeout"])
        payload = json.loads(request.data)
        self.assertEqual(payload["model"], "MiniMax-M3.1-Flash-Preview")
        self.assertEqual(payload["thinking"], {"type": "adaptive"})
        self.assertEqual(payload["reasoning_effort"], "low")
        self.assertNotIn("max_tokens", payload)
        self.assertNotIn("max_completion_tokens", payload)
        self.assertEqual(payload["messages"][1]["content"][0]["text"], "QUESTION ONLY")
        url = payload["messages"][1]["content"][1]["image_url"]["url"]
        self.assertEqual(base64.b64decode(url.split(",", 1)[1]), b"exact candidate PNG")
        self.assertEqual((result["answer"], result["thinking"]), ("final", "brief reasoning"))
        self.assertNotIn(KEY, request.data.decode())

    def test_truncation_and_missing_thinking(self):
        result = parse_response({"choices": [{"message": {"reasoning_content": "partial"}, "finish_reason": "length"}]})
        self.assertTrue(result["truncated"])
        self.assertEqual(result["thinking"], "partial")
        self.assertEqual(result["answer"], "")
        result = parse_response({"choices": [{"message": {"content": "plain answer"}, "finish_reason": "stop"}]})
        self.assertEqual(result["thinking"], "")
        result = parse_response({"choices": [{"message": {"content": "<think>reason</think>answer"}}]})
        self.assertEqual((result["thinking"], result["answer"]), ("reason", "answer"))

    def test_provider_errors_and_credentials(self):
        error = HTTPError(SETTINGS["api_base"], 401, "Unauthorized", {},
                          io.BytesIO(json.dumps({"error": {"message": "bad " + KEY}}).encode()))
        with patch("quick_test.build_opener") as opener:
            opener.return_value.open.side_effect = error
            with self.assertRaises(WorkbenchError) as raised:
                call_minimax(SETTINGS, KEY, "question", b"image")
        self.assertNotIn(KEY, str(raised.exception))
        self.assertIn("401", str(raised.exception))
        with self.assertRaises(WorkbenchError):
            parse_response({"base_resp": {"status_code": 1008, "status_msg": "quota exceeded"}})
        with self.assertRaises(WorkbenchError):
            parse_response({"choices": []})

    def test_timeout_does_not_retry(self):
        with patch("quick_test.build_opener") as opener:
            opener.return_value.open.side_effect = URLError(TimeoutError())
            with self.assertRaises(WorkbenchError):
                call_minimax(SETTINGS, KEY, "question", b"image")
            self.assertEqual(opener.return_value.open.call_count, 1)

    def test_dotenv_stays_on_server(self):
        fixture_root = PROJECT / ".runtime/solid_workbench_tests"
        fixture_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=fixture_root) as directory, patch.dict(os.environ, {"MINIMAX_API_KEY": ""}):
            Path(directory, ".env").write_text('export MINIMAX_API_KEY="' + KEY + '"\n', encoding="utf-8")
            self.assertEqual(load_api_key(directory), KEY)


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture_root = PROJECT / ".runtime/solid_workbench_tests"
        fixture_root.mkdir(parents=True, exist_ok=True)
        cls.temporary = tempfile.TemporaryDirectory(prefix="quick-test-fixture-", dir=fixture_root)
        cls.root = Path(cls.temporary.name)
        config = load_config()
        config.update(runtime_dir=str(cls.root / "runtime"), output_dir=str(cls.root / "dataset/special_variant"),
                      dataset_root=str(cls.root / "dataset"))
        cls.bench = Workbench(config)
        cls.qid = cls.bench.active_questions()[0]
        cls.bench.navigate(cls.qid)
        scene = cls.bench.drawing_scene(cls.qid)
        plugin = {"plugin_schema_version": "1.0.0", "question_id": cls.qid, "category": "C", "operation": "C_manual",
                  "description": "fixture annotation hint must never reach model", "intent": "SECRET VARIANT INTENT",
                  "params": {"actions": [{**scene["presets"]["point"], "id": "test_point", "xy": [-6.4317, -5.2711]}]}}
        preview = cls.bench.drawing_preview(plugin, cls.bench.context_token())
        cls.candidate = cls.bench.drawing_submit(plugin, cls.bench.context_token(), None,
            preview["pixel_sha256"], preview["parameter_key"])["candidate"]
        cls.body = {"question_id": cls.qid, "candidate_id": cls.candidate["candidate_id"],
                    "context_token": cls.bench.context_token(), "pixel_sha256": cls.candidate["pixel_sha256"],
                    "parameter_key": cls.candidate["parameter_key"]}

    @classmethod
    def tearDownClass(cls):
        cls.bench.close()
        cls.temporary.cleanup()

    def setUp(self):
        self.environment = patch.dict(os.environ, {"MINIMAX_API_KEY": KEY})
        self.environment.start()

    def tearDown(self):
        self.environment.stop()

    def wait_done(self, manager, profile="quicktest1"):
        deadline = time.monotonic() + 5
        while manager.active and time.monotonic() < deadline:
            time.sleep(.01)
        self.assertIsNone(manager.active)
        return manager.snapshot(self.bench.snapshot())["jobs"][profile]

    def test_two_modes_keep_independent_results_and_restore_legacy_m3(self):
        calls = []
        def provider(settings, key, question, image):
            calls.append(copy.deepcopy(settings))
            return {**RESULT, "answer": settings["model"], "response_model": settings["model"]}
        manager = QuickTests(self.bench, provider)
        before = copy.deepcopy(self.bench.progress)
        saved = {}
        for profile in TEST_PROFILES:
            manager.start({**self.body, "profile": profile})
            saved[profile] = self.wait_done(manager, profile)
            self.assertEqual(saved[profile]["model"], TEST_PROFILES[profile]["model"])
        first, second = calls
        self.assertEqual(first["thinking"], {"type": "disabled"})
        self.assertNotIn("reasoning_effort", first)
        self.assertEqual(second["thinking"], {"type": "adaptive"})
        self.assertEqual(second["reasoning_effort"], "low")
        snapshot = manager.snapshot(self.bench.snapshot())
        self.assertEqual(snapshot["jobs"], saved)
        self.assertEqual(snapshot["job"], saved["quicktest1"])
        self.assertEqual(self.bench.progress, before)
        self.assertNotIn(KEY, json.dumps(snapshot))
        # Existing M3 cache filenames and records without a profile remain readable.
        legacy = dict(saved["quicktest1"])
        for name in ("profile", "thinking_mode", "reasoning_effort"):
            legacy.pop(name, None)
        manager._path(self.candidate["candidate_id"]).write_text(json.dumps(legacy), encoding="utf-8")
        manager.close()
        restored = QuickTests(self.bench, lambda *args: self.fail("Restoring must not call the model"))
        jobs = restored.snapshot(self.bench.snapshot())["jobs"]
        self.assertEqual(jobs["quicktest1"]["run_id"], saved["quicktest1"]["run_id"])
        self.assertEqual(jobs["quicktest2"], saved["quicktest2"])
        stale = self.bench.snapshot()
        stale["candidate"] = {**stale["candidate"], "pixel_sha256": "changed"}
        self.assertEqual(restored.snapshot(stale)["jobs"], {"quicktest1": None, "quicktest2": None})
        restored.close()

    def test_invalid_mode_never_calls_provider(self):
        manager = QuickTests(self.bench, lambda *args: self.fail("Invalid mode must not call the model"))
        for profile in ("unknown", "../quicktest2", "", None, [], {}):
            with self.assertRaises(WorkbenchError) as raised:
                manager.start({**self.body, "profile": profile})
            self.assertEqual(raised.exception.code, "invalid_quick_test_profile")
        manager.close()

    def test_flash_inflight_dedup_conflict_and_restart(self):
        entered, release, finished = threading.Event(), threading.Event(), threading.Event()
        def provider(settings, *args):
            entered.set(); release.wait(5); finished.set()
            return {**RESULT, "response_model": settings["model"]}
        manager = QuickTests(self.bench, provider)
        body = {**self.body, "profile": "quicktest2"}
        try:
            job = manager.start(body)
            self.assertTrue(entered.wait(2))
            self.assertEqual(manager.start(body)["run_id"], job["run_id"])
            with self.assertRaises(WorkbenchError) as raised:
                manager.start({**self.body, "profile": "quicktest1"})
            self.assertEqual(raised.exception.code, "quick_test_running")
            self.assertEqual(manager.snapshot(self.bench.snapshot())["running_profile"], "quicktest2")
        finally:
            manager.close(); release.set()
        self.assertTrue(finished.wait(2))
        restored = QuickTests(self.bench, lambda *args: self.fail("Do not automatically retry"))
        self.assertEqual(restored.snapshot(self.bench.snapshot())["jobs"]["quicktest2"]["status"], "interrupted")
        restored.close()

    def test_stale_candidate_never_calls_provider(self):
        calls = []
        manager = QuickTests(self.bench, lambda *args: calls.append(args))
        for body in ({**self.body, "pixel_sha256": "wrong"}, {**self.body, "parameter_key": "wrong"},
                     {**self.body, "context_token": "stale"}, {**self.body, "candidate_id": "0" * 32}):
            with self.assertRaises(WorkbenchError):
                manager.start(body)
        self.assertEqual(calls, [])
        manager.close()

    def test_exact_input_dedup_recovery_and_review_independence(self):
        entered, release = threading.Event(), threading.Event()
        calls = []
        def provider(settings, key, question, image):
            calls.append((question, image)); entered.set(); release.wait(5)
            return copy.deepcopy(RESULT)
        before = copy.deepcopy(self.bench.progress)
        index_before = (PROJECT / "question_bank.jsonl").read_bytes()
        manager = QuickTests(self.bench, provider)
        job = manager.start(self.body)
        self.assertTrue(entered.wait(2))
        self.assertEqual(manager.start(self.body)["run_id"], job["run_id"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][0], self.bench.adapter.records[self.qid]["question"])
        self.assertEqual(calls[0][1], self.bench._package_file(self.candidate, "image.png").read_bytes())
        self.assertNotIn("intent", job)
        self.assertNotIn("params", job)
        self.assertNotIn("SECRET VARIANT INTENT", json.dumps(job))
        state = self.bench.snapshot()
        replaced = {**state, "candidate": {**state["candidate"], "candidate_id": "1" * 32}}
        self.assertIsNone(manager.snapshot(replaced)["job"])
        release.set()
        saved = self.wait_done(manager)
        self.assertEqual(saved["status"], "completed")
        self.assertEqual(saved["thinking"], RESULT["thinking"])
        self.assertEqual(self.bench.progress, before)
        self.assertEqual((PROJECT / "question_bank.jsonl").read_bytes(), index_before)
        self.assertEqual(saved["branch"], "SolidGeometry")
        self.assertEqual(saved["question_id"], self.qid)
        self.assertEqual(saved["png_sha256"], self.candidate["png_sha256"])
        self.assertNotIn(KEY, json.dumps(saved))
        manager.close()
        restored = QuickTests(self.bench, lambda *args: self.fail("Reading results must not call the model"))
        self.assertEqual(restored.snapshot(state)["job"]["run_id"], job["run_id"])
        restored.close()

    def test_missing_key_does_not_start(self):
        manager = QuickTests(self.bench, lambda *args: self.fail("Missing key"))
        with patch("quick_test.load_api_key", return_value=""):
            with self.assertRaises(WorkbenchError) as raised:
                manager.start(self.body)
            self.assertEqual(raised.exception.code, "missing_api_key")
        manager.close()

    def test_changed_image_is_rejected_before_call(self):
        manager = QuickTests(self.bench, lambda *args: self.fail("Changed image must not be sent"))
        path = self.bench._package_file(self.candidate, "image.png")
        original = path.read_bytes()
        try:
            path.write_bytes(original + b"tampered fixture")
            with self.assertRaises(WorkbenchError):
                manager.start(self.body)
        finally:
            path.write_bytes(original)
            manager.close()

    def test_interrupted_request_is_not_retried_on_restart(self):
        release, entered, finished = threading.Event(), threading.Event(), threading.Event()
        def provider(*args):
            entered.set(); release.wait(5); finished.set()
            return copy.deepcopy(RESULT)
        manager = QuickTests(self.bench, provider)
        manager.start(self.body)
        self.assertTrue(entered.wait(2))
        manager.close()
        release.set()
        self.assertTrue(finished.wait(2))
        restored = QuickTests(self.bench, lambda *args: self.fail("Do not retry automatically"))
        self.assertEqual(restored.snapshot(self.bench.snapshot())["job"]["status"], "interrupted")
        restored.close()

    def test_error_is_saved_without_credential(self):
        def fail(*args):
            raise WorkbenchError("provider echoed " + KEY)
        manager = QuickTests(self.bench, fail)
        manager.start(self.body)
        saved = self.wait_done(manager)
        self.assertEqual(saved["status"], "error")
        self.assertNotIn(KEY, saved["error"])
        manager.close()

    def test_http_requires_review_session(self):
        calls = []
        manager = QuickTests(self.bench, lambda *args: calls.append(args) or copy.deepcopy(RESULT))
        server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.bench, manager))
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        try:
            request = Request(base + "/api/quick-test", data=json.dumps({**self.body, "profile": "quicktest2"}).encode(),
                              headers={"Content-Type": "application/json"})
            with self.assertRaises(HTTPError) as raised:
                urlopen(request)
            self.assertEqual(raised.exception.code, 403)
            self.assertFalse(calls)
            request.add_header("X-Review-Token", self.bench.review_token)
            with urlopen(request) as response:
                self.assertEqual(response.status, 202)
            self.wait_done(manager, "quicktest2")
            with urlopen(base + "/api/state") as response:
                state = json.load(response)
            self.assertEqual(state["quick_test"]["jobs"]["quicktest2"]["status"], "completed")
            self.assertEqual(state["quick_test"]["jobs"]["quicktest2"]["reasoning_effort"], "low")
            self.assertNotIn(KEY, json.dumps(state))
        finally:
            server.shutdown(); server.server_close(); thread.join(); manager.close()


if __name__ == "__main__":
    unittest.main()
