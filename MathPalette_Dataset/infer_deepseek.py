"""Run the frozen MathPalette snapshot through DeepSeek V4.1 Flash.

Python 3.9+, standard library only. See INFERENCE.md. No grading is performed.
"""
from __future__ import annotations

import argparse
import base64
import collections
import copy
import hashlib
import json
import os
import re
import signal
import struct
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

DATASET = Path(__file__).resolve().parent
MODEL = "deepseek-flash"
DOCUMENTED_VERSION = "DeepSeek-V4.1-Flash-1017"
BASE_URL = "https://api.deepseek.com"
SYSTEM_PROMPT = (
    "Solve the mathematics question using the provided image. "
    "Give a clear final answer at the end. For a multiple-choice question, "
    "include the option letter in your final answer."
)
MAX_RESPONSE_BYTES = 16 * 1024 * 1024


def now():
    return datetime.now(timezone.utc).isoformat()


def encode(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(",", ":")).encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def atomic_write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = value if isinstance(value, bytes) else encode(value) + b"\n"
    fd, name = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def redact(value, secret):
    if isinstance(value, str):
        return value.replace(secret, "[REDACTED]") if secret else value
    if isinstance(value, dict):
        return {k: redact(v, secret) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v, secret) for v in value]
    return value


def load_key(env_file):
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key and env_file.is_file():
        for line in env_file.read_text(encoding="utf-8-sig").splitlines():
            match = re.match(r"\s*(?:export\s+)?DEEPSEEK_API_KEY\s*=\s*(.*?)\s*$", line)
            if match:
                key = match.group(1).strip()
                if len(key) >= 2 and key[0] == key[-1] and key[0] in "\"'":
                    key = key[1:-1]
                else:
                    key = key.split(" #", 1)[0].strip()
                break
    if not key:
        raise ValueError("Set DEEPSEEK_API_KEY in the environment or the project .env file.")
    return key


def contained(root, relative):
    root = root.resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or path == root:
        raise ValueError("A dataset path escapes its directory")
    return path


def load_dataset(root):
    """Validate the release and its normal Collect records, not the source workbench."""
    root = root.resolve()
    metadata = read_json(root / "metadata.json")
    for relative, expected in metadata["artifact_sha256"].items():
        if sha(contained(root, relative).read_bytes()) != expected:
            raise ValueError("Frozen data file changed: " + relative)
    questions = read_rows(root / "dataset.jsonl")
    samples = read_rows(root / "samples.jsonl")
    image_rows = read_rows(root / "image_manifest.jsonl")
    by_question = {row["id"]: row for row in questions}
    by_image = {row["image"]: row for row in image_rows}
    if (len(by_question) != len(questions) or len(by_image) != len(image_rows)
            or len({s["id"] for s in samples}) != len(samples)):
        raise ValueError("Duplicate question, sample, or image identity")
    expected_ids = set()
    for question in questions:
        qid = question["id"]
        collection = read_json(root / "provenance/collections" / (qid + ".json"))
        current = collection.get("current", {})
        if (collection.get("question_id") != qid or current.get("question_id") != qid
                or collection.get("status") != "collected" or current.get("status") != "collected"
                or current.get("special_case", False) or current.get("review_status") == "pending"
                or question.get("collection", {}).get("special_case") is not False):
            raise ValueError("Not a current normal Collect: " + qid)
        slots = [row["slot_id"] for row in question["special_variants"]]
        if (len(slots) != len(set(slots)) or set(slots) != set(current.get("slots", []))
                or len(slots) != current.get("accepted_count")):
            raise ValueError("Special slots differ from Collect: " + qid)
        expected_ids.add(qid + "_original")
        expected_ids.update(row["id"] for row in question["special_variants"])
    if expected_ids != {s["id"] for s in samples}:
        raise ValueError("Question and flattened sample sets differ")
    for row in image_rows:
        data = contained(root, row["image"]).read_bytes()
        if (len(data) != row["bytes"] or sha(data) != row["sha256"]
                or not data.startswith(b"\x89PNG\r\n\x1a\n") or struct.unpack(">II", data[16:24]) != (768, 768)):
            raise ValueError("Frozen PNG changed: " + row["image"])
    for sample in samples:
        if not re.fullmatch(r"(?:Ana|Plane|Solid)\d+_(?:original|C\d+)", sample["id"]):
            raise ValueError("Invalid sample identity")
        question = by_question[sample["question_id"]]
        for key in ("question", "answer", "answer_type", "branch", "source_dataset"):
            if sample[key] != question[key]:
                raise ValueError("Sample and question disagree: " + sample["id"])
        if sample.get("choices") != question.get("choices"):
            raise ValueError("Sample choices differ: " + sample["id"])
        if sample["variant_type"] == "original" and sample["variant_id"] is None:
            expected = question
            expected_id = question["id"] + "_original"
        elif sample["variant_type"] == "special":
            candidates = [s for s in question["special_variants"] if s["slot_id"] == sample["variant_id"]]
            if len(candidates) != 1:
                raise ValueError("Unknown Special sample")
            expected = candidates[0]
            expected_id = expected["id"]
        else:
            raise ValueError("Invalid variant type")
        if (sample["id"] != expected_id or sample["image"] != expected["image"]
                or sample["image_sha256"] != expected["image_sha256"]
                or by_image[sample["image"]]["sha256"] != sample["image_sha256"]):
            raise ValueError("Sample image mapping differs: " + sample["id"])
    counts = metadata["counts"]
    if (counts["questions"] != len(questions) or counts["samples"] != len(samples)
            or counts["unique_image_files"] != len(image_rows)):
        raise ValueError("Release counts differ from its metadata")
    return samples, metadata


def build_request(sample, root, args):
    data = contained(root, sample["image"]).read_bytes()
    if sha(data) != sample["image_sha256"]:
        raise ValueError("Image changed since preflight: " + sample["id"])
    body = {
        "model": MODEL, "thinking": {"type": "enabled"}, "reasoning_effort": args.reasoning_effort,
        "top_p": 1.0, "stream": True,
        "stream_options": {"include_usage": True},
        "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                     {"role": "user", "content": [
                         {"type": "text", "text": sample["question"]},
                         {"type": "image_url", "image_url": {
                             "url": "data:image/png;base64," + base64.b64encode(data).decode("ascii"),
                             "detail": "original"}}]}],
    }
    saved = copy.deepcopy(body)
    saved["messages"][1]["content"][1]["image_url"]["url"] = sample["image"]
    return encode(body), saved


def parse_stream(data):
    """Extract both output channels without discarding partial SSE responses."""
    result = {"reasoning_content": "", "content": "", "usage": None, "finish_reason": None,
              "response_id": None, "returned_model": None, "system_fingerprint": None,
              "done_received": False, "parse_errors": [], "api_error": None}
    text = data.decode("utf-8", errors="replace").replace("\r\n", "\n")
    for event in text.split("\n\n"):
        lines = [line[5:].lstrip(" ") for line in event.splitlines() if line.startswith("data:")]
        if not lines:
            continue  # SSE comments / keep-alive packets.
        payload = "\n".join(lines)
        if payload.strip() == "[DONE]":
            result["done_received"] = True
            continue
        try:
            chunk = json.loads(payload)
            if chunk.get("error"):
                result["api_error"] = chunk["error"]
            for key, target in (("id", "response_id"), ("model", "returned_model"),
                                ("system_fingerprint", "system_fingerprint")):
                if chunk.get(key) is not None:
                    result[target] = chunk[key]
            if chunk.get("usage") is not None:
                result["usage"] = chunk["usage"]
            for choice in chunk.get("choices", []):
                if choice.get("index", 0) != 0:
                    raise ValueError("Unexpected multiple choices in a one-sample request")
                delta = choice.get("delta", {})
                for key in ("reasoning_content", "content"):
                    value = delta.get(key)
                    if value is not None:
                        if not isinstance(value, str):
                            raise ValueError("Non-text " + key)
                        result[key] += value
                if choice.get("finish_reason") is not None:
                    result["finish_reason"] = choice["finish_reason"]
        except (ValueError, TypeError, AttributeError) as error:
            result["parse_errors"].append(str(error))
    return result


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def http_worker():
    """Isolated HTTP process: the parent can close a stalled streaming request."""
    settings = json.load(sys.stdin)
    directory = Path(settings["attempt_dir"])
    key = os.environ["MATHPALETTE_INFERENCE_API_KEY"]
    raw_path = directory / "response.sse"
    transport = {"status": "transport_error", "http_status": None, "request_id": None, "retry_after": 0}

    def watch_parent():
        while True:
            time.sleep(0.25)
            if os.getppid() != settings["parent_pid"]:
                os._exit(75)  # Close an orphaned local connection after a parent crash.

    threading.Thread(target=watch_parent, daemon=True).start()
    request = Request(settings["url"], data=base64.b64decode(settings["body"]), method="POST",
                      headers={"Authorization": "Bearer " + key, "Content-Type": "application/json",
                               "Accept": "text/event-stream", "User-Agent": "MathPalette-DeepSeek/1.0"})

    def save_response(response):
        transport["http_status"] = response.code
        transport["request_id"] = (response.headers.get("x-request-id")
                                   or response.headers.get("x-ds-request-id")
                                   or response.headers.get("request-id"))
        try:
            transport["retry_after"] = min(60.0, max(0.0, float(response.headers.get("Retry-After", "0"))))
        except ValueError:
            pass
        atomic_write(directory / "http_headers.json", redact(transport, key))
        total = 0
        with raw_path.open("wb") as handle:
            while True:
                chunk = response.read1(min(65536, MAX_RESPONSE_BYTES + 1 - total))
                if not chunk:
                    break
                handle.write(chunk)
                handle.flush()
                total += len(chunk)
                if total > MAX_RESPONSE_BYTES:
                    transport["status"] = "response_too_large"
                    return
        transport["status"] = "ok" if 200 <= response.code < 300 else "http_error"

    try:
        handlers = [NoRedirect()]
        if urlsplit(settings["url"]).hostname in ("127.0.0.1", "localhost", "::1"):
            handlers.insert(0, ProxyHandler({}))  # Local tests never use external/system proxies.
        opener = build_opener(*handlers)
        # This timestamp is immediately before the actual HTTP call, not queue entry.
        atomic_write(directory / "request_started.json", {"at_utc": now(), "monotonic": time.monotonic()})
        try:
            with opener.open(request, timeout=None) as response:
                save_response(response)
        except HTTPError as error:
            with error:
                save_response(error)
    except Exception as error:
        transport.update(status="transport_error", error_type=type(error).__name__, error=str(error))
    transport.update(finished_at_utc=now(), finished_monotonic=time.monotonic())
    atomic_write(directory / "transport.json", redact(transport, key))


def request_once(endpoint, body, key, directory, timeout, stop):
    """Enforce an elapsed-time deadline even while SSE keep-alives keep arriving."""
    environment = dict(os.environ)
    environment["MATHPALETTE_INFERENCE_API_KEY"] = key
    settings = {"url": endpoint, "body": base64.b64encode(body).decode("ascii"),
                "attempt_dir": str(directory), "parent_pid": os.getpid()}
    spawned = time.monotonic()
    # Credentials are in the child's environment, never argv or a persisted request.
    with tempfile.TemporaryFile(dir=directory) as source:
        source.write(encode(settings))
        source.seek(0)
        process = subprocess.Popen([sys.executable, "-X", "utf8", "-u", "-B", str(Path(__file__).resolve()),
                                    "--_http-worker"], stdin=source, stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, env=environment)
    started = None
    local_status = None
    try:
        while process.poll() is None:
            if started is None and (directory / "request_started.json").exists():
                started = read_json(directory / "request_started.json")
            if stop.is_set():
                local_status = "interrupted"
                break
            if started and time.monotonic() >= started["monotonic"] + timeout:
                local_status = "timeout"
                break
            if started is None and time.monotonic() - spawned > 15:
                local_status = "worker_startup_error"
                break
            stop.wait(0.02)
    finally:
        if process.poll() is None:
            process.kill()
        process.wait()
    if started is None and (directory / "request_started.json").exists():
        started = read_json(directory / "request_started.json")
    if local_status is None and started and (directory / "transport.json").exists():
        ended = read_json(directory / "transport.json").get("finished_monotonic")
        if ended is not None and ended > started["monotonic"] + timeout:
            local_status = "timeout"
    return capture_response(directory, key, local_status, started)


def capture_response(directory, key, local_status=None, started=None, recovered=False):
    if started is None and (directory / "request_started.json").exists():
        started = read_json(directory / "request_started.json")
    if local_status:
        headers = read_json(directory / "http_headers.json") if (directory / "http_headers.json").exists() else {}
        transport = {"http_status": None, "retry_after": 0, **headers, "status": local_status,
                     "local_request_closed": True, "server_cancellation_confirmed": False}
    elif (directory / "transport.json").exists():
        transport = read_json(directory / "transport.json")
    else:
        transport = {"status": "worker_error", "http_status": None, "retry_after": 0}
    raw_path = directory / "response.sse"
    raw = raw_path.read_bytes() if raw_path.exists() else b""
    # Sanitize a provider error that might echo a credential, including on timeout.
    clean = raw.replace(key.encode("utf-8"), b"[REDACTED]")
    if raw != clean:
        atomic_write(raw_path, clean)
    parsed = redact(parse_stream(clean), key)
    transport = redact(transport, key)
    status = transport["status"]
    http_status = transport.get("http_status")
    retryable = False
    fatal = False
    if status == "ok":
        if not parsed["done_received"]:
            status, retryable = "incomplete_stream", True
        elif parsed["parse_errors"] or parsed["api_error"]:
            status, fatal = "invalid_response", True
        elif parsed["finish_reason"] == "length":
            status = "truncated"
        elif parsed["finish_reason"] != "stop":
            status = "unexpected_finish_reason"
        elif not parsed["content"].strip():
            status, fatal = "missing_content", True
        elif not parsed["reasoning_content"].strip():
            status, fatal = "missing_reasoning", True
        else:
            status = "completed"
    elif status == "http_error":
        retryable = http_status in (408, 409, 425, 429) or (http_status is not None and http_status >= 500)
        fatal = not retryable
        transport["error_body"] = clean.decode("utf-8", errors="replace")
    elif status in ("timeout", "transport_error", "worker_startup_error", "worker_error", "interrupted"):
        retryable = True
    if status == "response_too_large":
        fatal = True
    ended = transport.get("finished_monotonic")
    finished_at = transport.get("finished_at_utc")
    if not recovered and ended is None:
        ended, finished_at = time.monotonic(), now()
    return {**parsed, "transport": transport, "status": status, "retryable": retryable, "fatal": fatal,
            "request_started_at_utc": started["at_utc"] if started else None,
            "elapsed_seconds": round(ended - started["monotonic"], 3) if started and ended is not None else None,
            "finished_at_utc": finished_at, "response_complete": status == "completed",
            "usage_missing": parsed["usage"] is None}


class RunLock:
    def __init__(self, directory):
        directory.mkdir(parents=True, exist_ok=True)
        self.handle = (directory / "run.lock").open("a+b")
        if self.handle.seek(0, os.SEEK_END) == 0:
            self.handle.write(b"0")
            self.handle.flush()
        self.handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self.handle.close()
            raise ValueError("Another inference process is using this output directory") from None

    def close(self):
        self.handle.close()


class RateLimiter:
    def __init__(self, rpm, stop):
        self.rpm, self.stop = rpm, stop
        self.lock = threading.Lock()
        self.sent = collections.deque()

    def acquire(self):
        while not self.stop.is_set():
            with self.lock:
                clock = time.monotonic()
                while self.sent and self.sent[0] <= clock - 60:
                    self.sent.popleft()
                if len(self.sent) < self.rpm:
                    self.sent.append(clock)
                    return True
                delay = self.sent[0] + 60 - clock
            self.stop.wait(max(0.01, delay))
        return False


def job_directory(output, sample, trial):
    return output / "samples" / sample["id"] / ("trial_%02d" % trial)


def infer_sample(sample, trial, root, output, args, key, limiter, stop, signature):
    directory = job_directory(output, sample, trial)
    if stop.is_set() and not directory.exists():
        return {"id": sample["id"], "trial": trial, "status": "pending"}
    result_path = directory / "result.json"
    body, saved_request = build_request(sample, root, args)
    request_hash = sha(body)
    previous = read_json(result_path) if result_path.exists() else None
    if previous and previous["request_sha256"] != request_hash:
        raise ValueError("Saved result has a different frozen request")
    attempt_dirs = sorted((directory / "attempts").glob("attempt_*"))
    attempts = []
    for path in attempt_dirs:
        record_path = path / "attempt.json"
        if record_path.exists():
            record = read_json(record_path)
            if record["request_sha256"] != request_hash:
                raise ValueError("Previous attempt uses a different request")
        else:
            record = {"attempt_id": path.name, "attempt_number": len(attempts) + 1,
                      "request_sha256": request_hash, "status": "started"}
        if record["status"] == "started":
            # Recover already downloaded output before considering another paid call.
            if (path / "transport.json").exists():
                response = capture_response(path, key, recovered=True)
            else:
                response = capture_response(path, key, "interrupted", recovered=True)
            record.update(response, recovered_after_interruption=True)
            atomic_write(record_path, record)
        attempts.append((path, record))
    if previous and previous["status"] == "completed":
        return previous
    latest = attempts[-1][1] if attempts else None

    def save_result():
        if not attempts:
            return {"id": sample["id"], "trial": trial, "status": "pending"}
        latest = attempts[-1][1] if attempts else {}
        result = {"id": sample["id"], "question_id": sample["question_id"], "trial": trial,
                  "branch": sample["branch"], "variant_type": sample["variant_type"],
                  "variant_id": sample["variant_id"], "question": sample["question"],
                  "reference_answer": sample["answer"], "answer_type": sample["answer_type"],
                  "image": sample["image"], "image_sha256": sample["image_sha256"],
                  "run_signature": signature, "request_sha256": request_hash, "requested_model": MODEL,
                  "reasoning_kind": "provider_reasoning_text", "status": latest.get("status", "pending"),
                  "reasoning_content": latest.get("reasoning_content", ""), "content": latest.get("content", ""),
                  "usage": latest.get("usage"), "finish_reason": latest.get("finish_reason"),
                  "response_id": latest.get("response_id"), "returned_model": latest.get("returned_model"),
                  "system_fingerprint": latest.get("system_fingerprint"),
                  "api_request_id": latest.get("transport", {}).get("request_id"),
                  "response_complete": latest.get("response_complete", False),
                  "retryable": latest.get("retryable", True), "fatal": latest.get("fatal", False),
                  "attempt_count": len(attempts),
                  "attempt_budget_exhausted": len(attempts) >= args.max_attempts and latest.get("status") != "completed",
                  "attempts": [{"attempt_id": r["attempt_id"], "status": r["status"],
                                "record": (p / "attempt.json").relative_to(output).as_posix()}
                               for p, r in attempts], "updated_at_utc": now()}
        atomic_write(result_path, result)
        return result

    if latest and (latest["status"] == "completed" or not latest.get("retryable", False)):
        if latest.get("fatal"):
            stop.set()
        return save_result()
    while len(attempts) < args.max_attempts and not stop.is_set():
        if not limiter.acquire():
            break
        if stop.is_set():
            break
        number = len(attempts) + 1
        attempt_id = "%03d_%s" % (number, uuid.uuid4().hex)
        path = directory / "attempts" / ("attempt_" + attempt_id)
        path.mkdir(parents=True, exist_ok=False)
        record = {"attempt_id": attempt_id, "attempt_number": number, "created_at_utc": now(),
                  "status": "started", "request_sha256": request_hash,
                  "request": saved_request, "image_sha256": sample["image_sha256"],
                  "endpoint": args.endpoint, "request_timeout_seconds": args.timeout,
                  "raw_response_file": "response.sse"}
        atomic_write(path / "attempt.json", record)
        attempts.append((path, record))
        try:
            record.update(request_once(args.endpoint, body, key, path, args.timeout, stop))
        except Exception as error:
            record.update(status="runner_error", fatal=True, retryable=False,
                          error=redact(str(error), key), finished_at_utc=now())
        atomic_write(path / "attempt.json", record)
        result = save_result()
        if record.get("fatal"):
            stop.set()
        if record["status"] == "completed" or not record.get("retryable") or stop.is_set():
            return result
        if len(attempts) < args.max_attempts:
            delay = max(record.get("transport", {}).get("retry_after", 0), min(2 ** (number - 1), 8))
            if stop.wait(delay):
                break
    return save_result()


def export_results(output, samples, trials, selected_ids, execution_status):
    records = []
    for sample in samples:
        for trial in range(1, trials + 1):
            path = job_directory(output, sample, trial) / "result.json"
            if path.exists():
                records.append(read_json(path))
    atomic_write(output / "results.jsonl", b"".join(encode(row) + b"\n" for row in records))
    states = collections.Counter(row["status"] for row in records)
    summary = {"updated_at_utc": now(), "execution_status": execution_status,
               "total_samples": len(samples), "trials_per_sample": trials, "total_jobs": len(samples) * trials,
               "selected_samples_this_invocation": len(selected_ids), "saved_jobs": len(records),
               "completed_jobs": states.get("completed", 0),
               "unstarted_jobs": len(samples) * trials - len(records),
               "status_counts": dict(states), "attempts_used": sum(row["attempt_count"] for row in records),
               "grading_performed": False}
    atomic_write(output / "summary.json", summary)
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-dir", type=Path, default=DATASET)
    parser.add_argument("--output-dir", type=Path, default=DATASET.parent / ".runtime/inference/deepseek_v4_1_flash")
    parser.add_argument("--env-file", type=Path, default=DATASET.parent / ".env")
    parser.add_argument("--base-url", default=os.environ.get("DEEPSEEK_BASE_URL", BASE_URL))
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--rpm", type=int, default=60, help="Request attempts per minute, including retries.")
    parser.add_argument("--timeout", type=float, default=240, help="Total HTTP deadline, at most 240 seconds.")
    parser.add_argument("--max-attempts", type=int, default=3, help="Total attempts per sample/trial, including saved attempts.")
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--reasoning-effort", choices=("low", "high", "max"), default="max")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--sample-id", action="append", help="Select an exact sample ID; may be repeated.")
    parser.add_argument("--smoke", action="store_true", help="Select one original/Special pair from each branch (6 requests).")
    parser.add_argument("--dry-run", action="store_true", help="Validate all frozen data without a key or HTTP requests.")
    args = parser.parse_args(argv)
    if not (1 <= args.concurrency <= 32 and args.rpm > 0 and 0 < args.timeout <= 240
            and 1 <= args.max_attempts <= 10 and 1 <= args.trials <= 20):
        parser.error("Invalid concurrency, rate, deadline, attempt budget, or trial count")
    if args.limit is not None and args.limit <= 0:
        parser.error("--limit must be positive")
    if args.smoke and (args.limit is not None or args.sample_id):
        parser.error("Use --smoke separately from --limit and --sample-id")
    args.dataset_dir = args.dataset_dir.resolve()
    args.output_dir = args.output_dir.resolve()
    if args.output_dir.is_relative_to(args.dataset_dir):
        parser.error("Runtime output must be outside the formal dataset directory")
    base = args.base_url.rstrip("/")
    url = urlsplit(base)
    if (not url.hostname or url.username or url.password or url.query or url.fragment
            or not (url.scheme == "https" or (url.scheme == "http" and url.hostname in ("127.0.0.1", "localhost", "::1")))):
        parser.error("Use an HTTPS API base URL; plain HTTP is allowed only for local software tests")
    args.endpoint = base + "/chat/completions"
    samples, metadata = load_dataset(args.dataset_dir)
    selected = samples
    if args.sample_id:
        ids = set(args.sample_id)
        if not ids.issubset({row["id"] for row in samples}):
            parser.error("An unknown sample ID was selected")
        selected = [row for row in samples if row["id"] in ids]
    if args.smoke:
        ids = set()
        for branch in ("Analytics", "PlaneGeometry", "SolidGeometry"):
            special = next((row for row in samples if row["branch"] == branch and row["variant_type"] == "special"), None)
            if special is None:
                parser.error("This snapshot does not have an original/Special pair in every branch")
            ids.update((special["id"], special["question_id"] + "_original"))
        selected = [row for row in samples if row["id"] in ids]
    if args.limit is not None:
        selected = selected[:args.limit]
    config = {
        "schema_version": 1, "runner_sha256": sha(Path(__file__).read_bytes()),
        "provider": "DeepSeek official API", "requested_model": MODEL,
        "documented_version": DOCUMENTED_VERSION, "api_model_is_alias": True,
        "endpoint": args.endpoint, "system_prompt": SYSTEM_PROMPT,
        "thinking": {"type": "enabled"}, "reasoning_effort": args.reasoning_effort,
        "output_token_limit_policy": "provider_default; no token-limit parameter sent",
        "top_p": 1.0, "stream": True,
        "image_mode": "local PNG bytes as base64; detail=original",
        "request_timeout_seconds": args.timeout, "max_attempts": args.max_attempts,
        "trials_per_sample": args.trials, "require_reasoning_content": True,
        "data_sha256": metadata["artifact_sha256"],
    }
    signature = sha(encode(config))
    if args.dry_run:
        print(json.dumps({"status": "validated", "model": MODEL, "documented_version": DOCUMENTED_VERSION,
                          "dataset_questions": metadata["counts"]["questions"], "dataset_samples": len(samples),
                          "unique_pngs": metadata["counts"]["unique_image_files"],
                          "selected_samples": len(selected), "planned_jobs": len(selected) * args.trials,
                          "output_dir": str(args.output_dir), "config": config,
                          "model_requests_submitted": 0}, ensure_ascii=False, indent=2))
        return 0
    key = load_key(args.env_file.resolve())
    run_lock = RunLock(args.output_dir)
    stop = threading.Event()
    interrupted = threading.Event()
    old_handlers = {}

    def on_signal(signum, frame):
        interrupted.set()
        stop.set()

    try:
        path = args.output_dir / "run.json"
        if path.exists():
            run = read_json(path)
            if run.get("signature") != signature:
                raise ValueError("Output directory belongs to different data/code/settings; use a separate --output-dir.")
        else:
            run = {"signature": signature, "config": config, "created_at_utc": now(), "invocations": []}
        run["invocations"].append({"started_at_utc": now(), "concurrency": args.concurrency,
                                    "rpm": args.rpm, "selected_ids": [row["id"] for row in selected]})
        atomic_write(path, run)
        if threading.current_thread() is threading.main_thread():
            for sig in (signal.SIGINT, signal.SIGTERM):
                old_handlers[sig] = signal.signal(sig, on_signal)
        limiter = RateLimiter(args.rpm, stop)
        futures = {}
        errors = []
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            for sample in selected:
                for trial in range(1, args.trials + 1):
                    futures[executor.submit(infer_sample, sample, trial, args.dataset_dir,
                                            args.output_dir, args, key, limiter, stop, signature)] = (sample["id"], trial)
            finished = 0
            for future in as_completed(futures):
                sample_id, trial = futures[future]
                try:
                    result = future.result()
                    state = result["status"]
                    if result.get("fatal"):
                        stop.set()
                    if state not in ("completed", "pending", "interrupted"):
                        errors.append("%s trial %d: %s" % (sample_id, trial, state))
                except Exception as error:
                    stop.set()
                    state = "runner_error"
                    errors.append(redact(str(error), key))
                finished += 1
                if state != "pending" and (finished <= 6 or finished % 10 == 0 or state != "completed"):
                    print("%s trial %d: %s (%d/%d selected jobs)" %
                          (sample_id, trial, state, finished, len(futures)), file=sys.stderr, flush=True)
        summary = export_results(args.output_dir, samples, args.trials,
                                 {row["id"] for row in selected}, "interrupted" if interrupted.is_set() else "finished")
        run["invocations"][-1].update(finished_at_utc=now(), interrupted=interrupted.is_set(), errors=errors)
        atomic_write(path, run)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if interrupted.is_set():
            return 130
        return 1 if errors or stop.is_set() else 0
    finally:
        stop.set()
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
        run_lock.close()


if __name__ == "__main__":
    if sys.argv[1:] == ["--_http-worker"]:
        http_worker()
    else:
        try:
            raise SystemExit(main())
        except (ValueError, OSError, KeyError) as error:
            print("Error: " + str(error), file=sys.stderr)
            raise SystemExit(2)
