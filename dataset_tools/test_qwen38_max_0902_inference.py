"""Real local HTTP/SSE integration tests; no external API or paid requests."""
import contextlib
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "MathPalette_Dataset/infer_qwen38_max_0902.py"
spec = importlib.util.spec_from_file_location("qwen38_max_0902_inference", SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
TEST_KEY = "local-test-secret-0123456789"


def emit(handler, reasoning="观察图像，计算左极限。", content="0", finish="stop", done=True):
    handler.send_response(200)
    handler.send_header("Content-Type", "text/event-stream")
    handler.send_header("x-request-id", "local-request")
    handler.end_headers()
    chunks = [
        {"id": "local-response", "model": "qwen3.8-max-0902", "choices": [
            {"index": 0, "delta": {"reasoning_content": reasoning, "content": ""}, "finish_reason": None}]},
        {"choices": [{"index": 0, "delta": {"content": content}, "finish_reason": None}]},
        {"choices": [{"index": 0, "delta": {}, "finish_reason": finish}]},
        {"choices": [], "usage": {"prompt_tokens": 123, "completion_tokens": 45, "total_tokens": 168,
                   "completion_tokens_details": {"reasoning_tokens": 40}}},
    ]
    handler.wfile.write(b": keep-alive\n\n")
    for chunk in chunks:
        data = ("data: " + json.dumps(chunk, ensure_ascii=False) + "\n\n").encode("utf-8")
        # Exercise UTF-8 boundaries in network reads.
        handler.wfile.write(data[:17])
        handler.wfile.flush()
        handler.wfile.write(data[17:])
        handler.wfile.flush()
    if done:
        handler.wfile.write(b"data: [DONE]\n\n")
        handler.wfile.flush()


def slow_stream(handler):
    handler.send_response(200)
    handler.send_header("Content-Type", "text/event-stream")
    handler.end_headers()
    event = {"id": "slow-response", "choices": [{"index": 0, "delta": {"reasoning_content": "正在观察图像。"}}]}
    try:
        handler.wfile.write(("data: " + json.dumps(event, ensure_ascii=False) + "\n\n").encode())
        handler.wfile.flush()
        for _ in range(160):
            time.sleep(0.025)
            handler.wfile.write(b": keep-alive\n\n")
            handler.wfile.flush()
    except (BrokenPipeError, ConnectionResetError):
        pass


@contextlib.contextmanager
def fake_server(callback):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            with self.server.lock:
                self.server.requests.append(body)
                self.server.paths.append(self.path)
                number = len(self.server.requests)
            try:
                callback(self, number, body)
            except (BrokenPipeError, ConnectionResetError):
                pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    server.requests = []
    server.paths = []
    server.lock = threading.Lock()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server, "http://127.0.0.1:%d" % server.server_port
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


class Qwen38Max0902InferenceTests(unittest.TestCase):
    def setUp(self):
        runtime = ROOT / ".runtime"
        runtime.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="qwen38_max_0902_inference_tests_", dir=runtime)
        self.base = Path(self.temporary.name)
        self.data = self.base / "fixture_dataset"
        self.data.mkdir()
        source = ROOT / "MathPalette_Dataset"
        question = runner.read_rows(source / "dataset.jsonl")[0]
        samples = [s for s in runner.read_rows(source / "samples.jsonl") if s["question_id"] == question["id"]]
        images = [r for r in runner.read_rows(source / "image_manifest.jsonl") if r["image"] in {s["image"] for s in samples}]
        for row in images:
            destination = self.data / row["image"]
            destination.parent.mkdir(exist_ok=True)
            shutil.copyfile(source / row["image"], destination)
        for name, rows in (("dataset.jsonl", [question]), ("samples.jsonl", samples), ("image_manifest.jsonl", images)):
            (self.data / name).write_bytes(b"".join(runner.encode(r) + b"\n" for r in rows))
        collection = self.data / "provenance/collections" / (question["id"] + ".json")
        collection.parent.mkdir(parents=True)
        shutil.copyfile(source / "provenance/collections" / collection.name, collection)
        metadata = {"counts": {"questions": 1, "samples": len(samples), "unique_image_files": len(images)},
                    "artifact_sha256": {name: runner.sha((self.data / name).read_bytes())
                                        for name in ("dataset.jsonl", "samples.jsonl", "image_manifest.jsonl")}}
        runner.atomic_write(self.data / "metadata.json", metadata)
        self.output = self.base / "output"

    def tearDown(self):
        self.temporary.cleanup()

    def command(self, url, *extra):
        return [sys.executable, "-B", str(SCRIPT), "--dataset-dir", str(self.data),
                "--output-dir", str(self.output), "--base-url", url, "--concurrency", "1",
                "--rpm", "10000", "--env-file", str(self.base / "absent.env"), *extra]

    def run_cli(self, url, *extra):
        environment = dict(os.environ, QWEN_38_MAX_0902_API_KEY=TEST_KEY)
        return subprocess.run(self.command(url, *extra), env=environment, capture_output=True, text=True, timeout=15)

    def result(self):
        return runner.read_rows(self.output / "results.jsonl")[0]

    def test_parent_clock_epoch_does_not_make_a_completed_request_time_out(self):
        directory = self.base / "clock_epoch_attempt"
        directory.mkdir()
        clock = time.monotonic
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            with mock.patch.object(runner.time, "monotonic", side_effect=lambda: clock() + 1000000):
                response = runner.request_once(
                    url + "/chat/completions", b"{}", TEST_KEY, directory, 2, threading.Event(),
                )
            self.assertEqual(response["status"], "completed")
            self.assertEqual(len(server.requests), 1)
            self.assertGreaterEqual(response["elapsed_seconds"], 0)
            self.assertLess(response["elapsed_seconds"], 2)

    def test_gateway_prefix_and_fixed_model_are_used(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            result = self.run_cli(url + "/compatible-mode/v1", "--limit", "1")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(server.paths, ["/compatible-mode/v1/chat/completions"])
            self.assertEqual(server.requests[0]["model"], "qwen3.8-max-0902")
        self.assertEqual(runner.BASE_URL, "https://maas.qianwenaiapi.com/compatible-mode/v1")
        self.assertEqual(self.result()["returned_model"], "qwen3.8-max-0902")

    def test_model_key_is_independent_and_environment_has_priority(self):
        path = self.base / "project.env"
        path.write_text('DEEPSEEK_API_KEY=other-provider-test-key\nQWEN_38_MAX_0902_API_KEY="qwen-file-test-key"\n')
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(runner.load_key(path), "qwen-file-test-key")
        with mock.patch.dict(os.environ, {"QWEN_38_MAX_0902_API_KEY": "qwen-env-test-key"}, clear=True):
            self.assertEqual(runner.load_key(path), "qwen-env-test-key")

    def test_capture_reasoning_answer_usage_and_frozen_image_without_ground_truth(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            result = self.run_cli(url, "--limit", "1")
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = server.requests[0]
            self.assertEqual(payload["model"], "qwen3.8-max-0902")
            self.assertTrue(payload["enable_thinking"])
            self.assertNotIn("thinking", payload)
            self.assertNotIn("extra_body", payload)
            self.assertNotIn("top_p", payload)
            self.assertEqual(payload["reasoning_effort"], "xhigh")
            for parameter in ("max_tokens", "max_completion_tokens", "max_output_tokens", "thinking_budget"):
                self.assertNotIn(parameter, payload)
            self.assertNotIn("temperature", payload)
            self.assertNotIn("answer", payload)
            self.assertNotIn("reference_answer", payload)
            self.assertNotIn("tools", payload)
            self.assertEqual([message["role"] for message in payload["messages"]], ["user"])
            image = payload["messages"][0]["content"][1]["image_url"]
            sample = runner.read_rows(self.data / "samples.jsonl")[0]
            expected_text = (
                r'Please solve the problem step by step and put your answer in one "\boxed{}".'
                + "\n" + sample["question"]
            )
            self.assertEqual(payload["messages"][0]["content"][0]["text"], expected_text)
            from types import SimpleNamespace
            for answer_type in ("choice", "number", "expression", "text"):
                body, saved = runner.build_request(
                    {**sample, "answer_type": answer_type}, self.data,
                    SimpleNamespace(reasoning_effort="xhigh"),
                )
                self.assertEqual(json.loads(body)["messages"][0]["content"][0]["text"], expected_text)
                self.assertEqual(saved["messages"][0]["content"][1]["image_url"]["url"], sample["image"])
            self.assertNotIn("detail", image)
            import base64
            self.assertEqual(base64.b64decode(image["url"].split(",", 1)[1]), (self.data / sample["image"]).read_bytes())
        record = self.result()
        self.assertEqual(record["reasoning_content"], "观察图像，计算左极限。")
        self.assertEqual(record["content"], "0")
        self.assertEqual(record["usage"]["completion_tokens_details"]["reasoning_tokens"], 40)
        self.assertEqual(record["api_request_id"], "local-request")
        self.assertTrue(record["response_complete"])
        config = runner.read_json(self.output / "run.json")["config"]
        self.assertEqual(config["request_timeout_seconds"], 240)
        self.assertEqual(config["reasoning_effort"], "xhigh")
        self.assertNotIn("max_tokens", config)

    def test_deadline_accepts_240_and_rejects_longer_requests(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            result = self.run_cli(url, "--limit", "1", "--timeout", "240")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.run_cli(url, "--timeout", "241").returncode, 2)
            self.assertEqual(len(server.requests), 1)

    def test_resume_skips_completed_and_allows_expanding_selection(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            self.assertEqual(self.run_cli(url, "--limit", "1").returncode, 0)
            result = self.run_cli(url, "--limit", "2")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(server.requests), 2)
            self.assertEqual(len(runner.read_rows(self.output / "results.jsonl")), 2)
            changed = self.run_cli(url, "--limit", "2", "--reasoning-effort", "low")
            self.assertEqual(changed.returncode, 2)
            self.assertEqual(len(server.requests), 2)

    def test_missing_reasoning_is_terminal_and_stops_further_calls(self):
        with fake_server(lambda h, n, b: emit(h, reasoning="")) as (server, url):
            result = self.run_cli(url)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(self.result()["status"], "missing_reasoning")
            self.assertEqual(len(server.requests), 1)
            self.assertEqual(self.run_cli(url).returncode, 1)
            self.assertEqual(len(server.requests), 1)

    def test_truncation_does_not_change_parameters_or_retry(self):
        with fake_server(lambda h, n, b: emit(h, content="partial", finish="length")) as (server, url):
            result = self.run_cli(url, "--limit", "1")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(len(server.requests), 1)
            self.assertEqual(self.result()["status"], "truncated")
            self.assertFalse(self.result()["response_complete"])

    def test_wrong_math_answer_is_kept_without_retesting(self):
        with fake_server(lambda h, n, b: emit(h, content="999")) as (server, url):
            self.assertEqual(self.run_cli(url, "--limit", "1").returncode, 0)
            self.assertEqual(len(server.requests), 1)
            self.assertEqual(self.result()["content"], "999")
            self.assertEqual(self.result()["status"], "completed")

    def test_only_timed_out_trial_is_retried_and_completed_trial_is_preserved(self):
        with fake_server(lambda h, n, b: slow_stream(h) if n == 2 else emit(h)) as (server, url):
            options = ("--limit", "1", "--trials", "2", "--timeout", "1", "--max-attempts", "2")
            result = self.run_cli(url, *options)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(server.requests), 3)
            rows = runner.read_rows(self.output / "results.jsonl")
            self.assertEqual([row["attempt_count"] for row in rows], [1, 2])
            self.assertTrue(all(row["status"] == "completed" for row in rows))
            self.assertEqual(self.run_cli(url, *options).returncode, 0)
            self.assertEqual(len(server.requests), 3)

    def test_timeout_is_total_despite_keepalives_and_budget_survives_resume(self):
        with fake_server(lambda h, n, b: slow_stream(h)) as (server, url):
            before = time.monotonic()
            result = self.run_cli(url, "--limit", "1", "--timeout", "1", "--max-attempts", "2")
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertLess(time.monotonic() - before, 7)
            self.assertEqual(len(server.requests), 2)
            self.assertEqual(server.requests[0], server.requests[1])
            record = self.result()
            self.assertEqual(record["status"], "timeout")
            self.assertEqual(record["attempt_count"], 2)
            self.assertTrue(record["attempt_budget_exhausted"])
            self.assertIn("正在观察图像", record["reasoning_content"])
            self.assertEqual(self.run_cli(url, "--limit", "1", "--timeout", "1", "--max-attempts", "2").returncode, 1)
            self.assertEqual(len(server.requests), 2)

    def test_transient_retry_preserves_attempts_and_redacts_error(self):
        def respond(handler, number, body):
            if number == 1:
                handler.send_response(429)
                handler.send_header("Retry-After", "0")
                handler.send_header("x-request-id", TEST_KEY)
                handler.end_headers()
                handler.wfile.write(json.dumps({"error": {"message": "busy " + TEST_KEY}}).encode())
            else:
                emit(handler)
        with fake_server(respond) as (server, url):
            result = self.run_cli(url, "--limit", "1")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(server.requests), 2)
            self.assertEqual(server.requests[0], server.requests[1])
        self.assertEqual(self.result()["attempt_count"], 2)
        self.assertEqual([a["status"] for a in self.result()["attempts"]], ["http_error", "completed"])
        for path in self.output.rglob("*"):
            if path.is_file():
                self.assertNotIn(TEST_KEY.encode(), path.read_bytes(), str(path))

    def test_recover_finished_download_after_parent_state_was_not_saved(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            self.assertEqual(self.run_cli(url, "--limit", "1").returncode, 0)
            path = next(self.output.rglob("attempt.json"))
            attempt = runner.read_json(path)
            previous_elapsed = attempt["elapsed_seconds"]
            attempt["status"] = "started"
            runner.atomic_write(path, attempt)
            next(self.output.rglob("result.json")).unlink()
            result = self.run_cli(url, "--limit", "1")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(server.requests), 1)
            recovered = runner.read_json(path)
            self.assertEqual(recovered["elapsed_seconds"], previous_elapsed)
            self.assertTrue(recovered["recovered_after_interruption"])

    def test_invalid_key_error_is_not_retried(self):
        def respond(handler, number, body):
            handler.send_response(401)
            handler.end_headers()
            handler.wfile.write(b'{"error":{"message":"unauthorized"}}')
        with fake_server(respond) as (server, url):
            self.assertEqual(self.run_cli(url).returncode, 1)
            self.assertEqual(len(server.requests), 1)

    def test_dataset_tampering_and_special_flag_are_rejected_without_network(self):
        with fake_server(lambda h, n, b: emit(h)) as (server, url):
            path = next((self.data / "provenance/collections").glob("*.json"))
            collection = runner.read_json(path)
            collection["current"]["special_case"] = True
            runner.atomic_write(path, collection)
            result = self.run_cli(url, "--dry-run")
            self.assertEqual(result.returncode, 2)
            self.assertFalse(self.output.exists())
            self.assertEqual(len(server.requests), 0)
            collection["current"]["special_case"] = False
            runner.atomic_write(path, collection)
            image = next((self.data / "images").glob("*.png"))
            image.write_bytes(image.read_bytes() + b"tampered")
            self.assertEqual(self.run_cli(url, "--dry-run").returncode, 2)
            self.assertEqual(len(server.requests), 0)

    @unittest.skipIf(os.name == "nt", "POSIX interrupt integration test")
    def test_keyboard_interrupt_preserves_partial_and_resume_uses_remaining_budget(self):
        with fake_server(lambda h, n, b: slow_stream(h) if n == 1 else emit(h)) as (server, url):
            command = self.command(url, "--limit", "1", "--timeout", "2", "--max-attempts", "2")
            process = subprocess.Popen(command, env=dict(os.environ, QWEN_38_MAX_0902_API_KEY=TEST_KEY),
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline:
                partial = list(self.output.rglob("response.sse")) if self.output.exists() else []
                if partial and partial[0].stat().st_size > 0:
                    break
                time.sleep(0.02)
            else:
                process.kill()
                process.communicate()
                self.fail("No partial stream was recorded")
            overlapping = self.run_cli(url, "--limit", "1", "--timeout", "2", "--max-attempts", "2")
            self.assertEqual(overlapping.returncode, 2)
            self.assertIn("Another inference process", overlapping.stderr)
            self.assertEqual(len(server.requests), 1)
            process.send_signal(signal.SIGINT)
            stdout, stderr = process.communicate(timeout=5)
            self.assertEqual(process.returncode, 130, stderr)
            self.assertEqual(self.result()["status"], "interrupted")
            self.assertIn("正在观察图像", self.result()["reasoning_content"])
            resumed = self.run_cli(url, "--limit", "1", "--timeout", "2", "--max-attempts", "2")
            self.assertEqual(resumed.returncode, 0, resumed.stderr)
            self.assertEqual(len(server.requests), 2)
            self.assertEqual(self.result()["attempt_count"], 2)


if __name__ == "__main__":
    unittest.main()
