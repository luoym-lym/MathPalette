"""Offline regression checks; all review operations use an isolated dataset copy."""
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

from quick_test import QuickTests, TEST_PROFILES, MIMO_API_BASE, call_model, call_minimax, load_api_key, parse_response
from review_store import Workbench
from server import make_handler
from workbench_io import WorkbenchError, load_config

PROJECT = Path(__file__).resolve().parents[2]
KEY = "sk-cp-quick-test-fixture"
MIMO_KEY = "tp-quick-test-fixture"
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

    def test_mimo_modes_use_token_plan_with_separate_reasoning(self):
        for profile, thinking in (("quicktest3", "disabled"), ("quicktest4", "enabled")):
            with self.subTest(profile=profile):
                response = {"model": "mimo-v2.6-flash", "choices": [{"message": {
                    "content": "final", "reasoning_content": "reasoning" if thinking == "enabled" else ""},
                    "finish_reason": "stop"}], "usage": {"total_tokens": 123}}
                settings = {**TEST_PROFILES[profile], "api_base": MIMO_API_BASE}
                with patch("quick_test.build_opener") as opener:
                    opener.return_value.open.return_value = io.BytesIO(json.dumps(response).encode())
                    result = call_model(settings, MIMO_KEY, "QUESTION ONLY", b"exact candidate PNG")
                    request = opener.return_value.open.call_args.args[0]
                    self.assertIsNone(opener.return_value.open.call_args.kwargs["timeout"])
                    self.assertEqual(opener.return_value.open.call_count, 1)
                payload = json.loads(request.data)
                self.assertEqual(set(payload), {"model", "stream", "thinking", "messages"})
                self.assertEqual(payload["model"], "mimo-v2.6-flash")
                self.assertEqual(payload["thinking"], {"type": thinking})
                self.assertFalse(payload["stream"])
                self.assertEqual(payload["messages"][1]["content"][0]["text"], "QUESTION ONLY")
                url = payload["messages"][1]["content"][1]["image_url"]["url"]
                self.assertEqual(base64.b64decode(url.split(",", 1)[1]), b"exact candidate PNG")
                self.assertEqual(request.full_url, MIMO_API_BASE + "/chat/completions")
                self.assertEqual(request.get_header("Authorization"), "Bearer " + MIMO_KEY)
                self.assertNotIn(MIMO_KEY, request.data.decode())
                self.assertEqual(result["answer"], "final")
                self.assertEqual(result["thinking"], "reasoning" if thinking == "enabled" else "")
                self.assertEqual(result["usage"]["total_tokens"], 123)

    def test_mimo_errors_redact_token_plan_keys_and_do_not_retry(self):
        settings = {**TEST_PROFILES["quicktest4"], "api_base": MIMO_API_BASE}
        error = HTTPError(MIMO_API_BASE, 401, "Unauthorized", {}, io.BytesIO(json.dumps({
            "error": {"message": "bad " + MIMO_KEY + " tp-other-secret ttp-team-secret"}}).encode()))
        with patch("quick_test.build_opener") as opener:
            opener.return_value.open.side_effect = error
            with self.assertRaises(WorkbenchError) as raised:
                call_model(settings, MIMO_KEY, "question", b"image")
            self.assertEqual(opener.return_value.open.call_count, 1)
        self.assertIn("MiMo HTTP 401", str(raised.exception))
        for key in (MIMO_KEY, "tp-other-secret", "ttp-team-secret"):
            self.assertNotIn(key, str(raised.exception))
        with patch("quick_test.build_opener") as opener:
            with self.assertRaises(WorkbenchError):
                call_model({**settings, "api_base": SETTINGS["api_base"]}, MIMO_KEY, "question", b"image")
            opener.assert_not_called()

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
        fixture_parent = PROJECT / ".runtime/plane_workbench_tests"
        fixture_parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="dotenv-fixture-", dir=fixture_parent) as directory, patch.dict(os.environ, {"MINIMAX_API_KEY": ""}):
            self.assertTrue(Path(directory).resolve().is_relative_to(fixture_parent.resolve()))
            Path(directory, ".env").write_text('export MINIMAX_API_KEY="' + KEY + '"\n', encoding="utf-8")
            self.assertEqual(load_api_key(directory), KEY)
            Path(directory, ".env").write_text("MINIMAX_API_KEY=" + KEY + "\nexport MIMO_API_KEY='" + MIMO_KEY + "'\n", encoding="utf-8")
            with patch.dict(os.environ, {"MIMO_API_KEY": ""}):
                self.assertEqual(load_api_key(directory, "MIMO_API_KEY"), MIMO_KEY)
            with patch.dict(os.environ, {"MIMO_API_KEY": "tp-env-fixture"}):
                self.assertEqual(load_api_key(directory, "MIMO_API_KEY"), "tp-env-fixture")


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture_parent = PROJECT / ".runtime/plane_workbench_tests"
        fixture_parent.mkdir(parents=True, exist_ok=True)
        cls.temporary = tempfile.TemporaryDirectory(prefix="quick-test-fixture-", dir=fixture_parent)
        cls.root = Path(cls.temporary.name).resolve()
        assert cls.root.is_relative_to(fixture_parent.resolve())
        config = load_config()
        config.update(runtime_dir=str(cls.root / "state"), output_dir=str(cls.root / "output"), dataset_root=str(cls.root))
        cls.bench = Workbench(config)
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.addClassCleanup(cls.bench.close)
        cls.qid = cls.bench.active_questions()[0]
        cls.bench.navigate(cls.qid)
        scene = cls.bench.drawing_scene(cls.qid)
        plugin = {"plugin_schema_version": "1.0.0", "question_id": cls.qid, "category": "C", "operation": "C_manual",
                  "description": "fixture annotation hint must never reach model", "intent": "SECRET VARIANT INTENT",
                  "params": {"actions": [{**scene["presets"]["point"], "id": "test_point",
                    "xy": [sum(scene["xlim"])/2, sum(scene["ylim"])/2]}]}}
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
        self.environment = patch.dict(os.environ, {"MINIMAX_API_KEY": KEY, "MIMO_API_KEY": MIMO_KEY})
        self.environment.start()

    def tearDown(self):
        self.environment.stop()

    def wait_done(self, manager, profile="quicktest1"):
        deadline = time.monotonic() + 5
        while manager.active and time.monotonic() < deadline:
            time.sleep(.01)
        self.assertIsNone(manager.active)
        return manager.snapshot(self.bench.snapshot())["jobs"][profile]

    def test_four_modes_keep_independent_results_and_restore_legacy_m3(self):
        calls = []
        def provider(settings, key, question, image):
            calls.append((copy.deepcopy(settings), key))
            return {**RESULT, "answer": settings["model"], "response_model": settings["model"]}
        manager = QuickTests(self.bench, provider)
        before = copy.deepcopy(self.bench.progress)
        saved = {}
        for profile in TEST_PROFILES:
            manager.start({**self.body, "profile": profile})
            saved[profile] = self.wait_done(manager, profile)
            self.assertEqual(saved[profile]["model"], TEST_PROFILES[profile]["model"])
        self.assertEqual([key for _, key in calls], [KEY, KEY, MIMO_KEY, MIMO_KEY])
        first, second, third, fourth = [settings for settings, _ in calls]
        self.assertEqual(third["api_base"], MIMO_API_BASE)
        self.assertEqual(fourth["api_base"], MIMO_API_BASE)
        self.assertEqual(third["thinking"], {"type": "disabled"})
        self.assertEqual(fourth["thinking"], {"type": "enabled"})
        self.assertNotIn("reasoning_effort", third)
        self.assertNotIn("reasoning_effort", fourth)
        self.assertEqual(first["thinking"], {"type": "disabled"})
        self.assertNotIn("reasoning_effort", first)
        self.assertEqual(second["thinking"], {"type": "adaptive"})
        self.assertEqual(second["reasoning_effort"], "low")
        snapshot = manager.snapshot(self.bench.snapshot())
        self.assertEqual(snapshot["jobs"], saved)
        self.assertEqual(snapshot["job"], saved["quicktest1"])
        self.assertEqual(self.bench.progress, before)
        self.assertNotIn(KEY, json.dumps(snapshot))
        self.assertNotIn(MIMO_KEY, json.dumps(snapshot))
        # Existing M3 cache filenames and records without a profile remain readable.
        legacy = dict(saved["quicktest1"])
        for name in ("profile", "thinking_mode", "reasoning_effort"):
            legacy.pop(name, None)
        manager._path(self.candidate["candidate_id"]).write_text(json.dumps(legacy), encoding="utf-8")
        manager.close()
        restored = QuickTests(self.bench, lambda *args: self.fail("Restoring must not call the model"))
        jobs = restored.snapshot(self.bench.snapshot())["jobs"]
        self.assertEqual(jobs["quicktest1"]["run_id"], saved["quicktest1"]["run_id"])
        for profile in ("quicktest2", "quicktest3", "quicktest4"):
            self.assertEqual(jobs[profile], saved[profile])
        stale = self.bench.snapshot()
        stale["candidate"] = {**stale["candidate"], "pixel_sha256": "changed"}
        self.assertEqual(restored.snapshot(stale)["jobs"], {profile: None for profile in TEST_PROFILES})
        restored.close()

    def test_provider_credentials_enable_profiles_independently(self):
        calls = []
        manager = QuickTests(self.bench, lambda *args: calls.append(args) or copy.deepcopy(RESULT))
        try:
            for available, enabled in (("MIMO_API_KEY", {"quicktest3", "quicktest4"}),
                                       ("MINIMAX_API_KEY", {"quicktest1", "quicktest2"})):
                with self.subTest(available=available), patch("quick_test.load_api_key", side_effect=
                        lambda project, variable="MINIMAX_API_KEY": "fixture-key" if variable == available else ""):
                    snapshot = manager.snapshot(self.bench.snapshot())
                    self.assertEqual(snapshot["configured"], available == "MINIMAX_API_KEY")
                    self.assertEqual(snapshot["configured_profiles"], {p: p in enabled for p in TEST_PROFILES})
                    for profile in set(TEST_PROFILES) - enabled:
                        with self.assertRaises(WorkbenchError) as raised:
                            manager.start({**self.body, "profile": profile})
                        self.assertEqual(raised.exception.code, "missing_api_key")
                        missing = "MINIMAX_API_KEY" if profile in ("quicktest1", "quicktest2") else "MIMO_API_KEY"
                        self.assertIn(missing, str(raised.exception))
            self.assertFalse(calls)
        finally:
            manager.close()

    def test_mimo_inflight_prevents_cross_provider_calls(self):
        entered, release, finished = threading.Event(), threading.Event(), threading.Event()
        calls = []
        def provider(settings, *args):
            calls.append(settings["provider"])
            entered.set(); release.wait(5); finished.set()
            return copy.deepcopy(RESULT)
        manager = QuickTests(self.bench, provider)
        body = {**self.body, "profile": "quicktest4"}
        try:
            job = manager.start(body)
            self.assertTrue(entered.wait(2))
            self.assertEqual(manager.start(body)["run_id"], job["run_id"])
            for profile in ("quicktest1", "quicktest2", "quicktest3"):
                with self.assertRaises(WorkbenchError) as raised:
                    manager.start({**self.body, "profile": profile})
                self.assertEqual(raised.exception.code, "quick_test_running")
            self.assertEqual(calls, ["mimo"])
        finally:
            manager.close(); release.set()
        self.assertTrue(finished.wait(2))
        restored = QuickTests(self.bench, lambda *args: self.fail("Do not retry automatically"))
        self.assertEqual(restored.snapshot(self.bench.snapshot())["jobs"]["quicktest4"]["status"], "interrupted")
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
        self.assertEqual(saved["branch"], "PlaneGeometry")
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
            for profile in ("quicktest2", "quicktest3", "quicktest4"):
                request = Request(base + "/api/quick-test", data=json.dumps({**self.body, "profile": profile}).encode(),
                                  headers={"Content-Type": "application/json", "X-Review-Token": self.bench.review_token})
                with urlopen(request) as response:
                    self.assertEqual(response.status, 202)
                self.wait_done(manager, profile)
                with urlopen(base + "/api/state") as response:
                    state = json.load(response)
                saved = state["quick_test"]["jobs"][profile]
                self.assertEqual(saved["status"], "completed")
                self.assertEqual(saved["thinking_mode"], TEST_PROFILES[profile]["thinking"]["type"])
                self.assertEqual(saved["provider"], TEST_PROFILES[profile]["provider"])
                self.assertEqual(calls[-1][1], MIMO_KEY if saved["provider"] == "mimo" else KEY)
                self.assertNotIn(KEY, json.dumps(state))
                self.assertNotIn(MIMO_KEY, json.dumps(state))
            self.assertEqual(len(calls), 3)
        finally:
            server.shutdown(); server.server_close(); thread.join(); manager.close()


if __name__ == "__main__":
    unittest.main()
