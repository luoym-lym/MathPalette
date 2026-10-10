"""One manual model call against an immutable candidate; no judging or collection."""
from __future__ import annotations

import base64
import copy
import json
import os
import re
import threading
import time
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

from workbench_io import WorkbenchError, atomic_json, contained_path, read_json, timestamp

SYSTEM_PROMPT = (
    "Solve the mathematics question using the provided image. "
    "Give a clear final answer at the end. For a multiple-choice question, "
    "include the option letter in your final answer."
)
API_BASES = {"https://api.minimaxi.com/v1", "https://api.minimax.io/v1"}
MAX_RESPONSE_BYTES = 8 * 1024 * 1024


def load_api_key(project):
    key = os.environ.get("MINIMAX_API_KEY", "").strip()
    path = Path(project) / ".env"
    if not key and path.is_file():
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            match = re.match(r"\s*(?:export\s+)?MINIMAX_API_KEY\s*=\s*(.*?)\s*$", line)
            if match:
                key = match.group(1).strip()
                if len(key) >= 2 and key[0] == key[-1] and key[0] in "\"'":
                    key = key[1:-1]
                else:
                    key = key.split(" #", 1)[0].strip()
                break
    return key


def safe_error(message, key):
    message = str(message).replace(key, "[REDACTED]") if key else str(message)
    return re.sub(r"sk-[A-Za-z0-9_-]+", "[REDACTED]", message)[:1000]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward the subscription credential to a redirected address.
        return None


def parse_response(data):
    if not isinstance(data, dict):
        raise WorkbenchError("MiniMax 返回了无效响应。", 502, "model_response_invalid")
    base = data.get("base_resp") or {}
    if data.get("error") or base.get("status_code", 0) != 0:
        error = data.get("error") or base
        message = error.get("message") or error.get("status_msg") if isinstance(error, dict) else str(error)
        raise WorkbenchError("MiniMax：" + str(message), 502, "model_request_failed")
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
        raise WorkbenchError("MiniMax 没有返回回答。", 502, "model_response_invalid")
    choice = choices[0]
    message = choice.get("message") or {}
    answer, thinking = message.get("content") or "", message.get("reasoning_content") or ""
    if not isinstance(answer, str) or not isinstance(thinking, str):
        raise WorkbenchError("MiniMax 返回了无法识别的回答格式。", 502, "model_response_invalid")
    # Some compatible responses still place thinking inside content.
    embedded = re.findall(r"<think>(.*?)</think>", answer, flags=re.DOTALL)
    if embedded:
        if not thinking:
            thinking = "\n\n".join(embedded)
        answer = re.sub(r"<think>.*?</think>", "", answer, flags=re.DOTALL)
    if not answer.strip() and not thinking.strip():
        raise WorkbenchError("MiniMax 返回了空回答。", 502, "model_response_invalid")
    return {"answer": answer.strip(), "thinking": thinking.strip(),
            "finish_reason": choice.get("finish_reason"), "usage": data.get("usage") or {},
            "response_model": data.get("model"), "truncated": choice.get("finish_reason") == "length"}


def call_minimax(settings, key, question, image):
    payload = {"model": settings["model"], "stream": False, "thinking": {"type": "disabled"},
               "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": [
                                {"type": "text", "text": question},
                                {"type": "image_url", "image_url": {
                                    "url": "data:image/png;base64," + base64.b64encode(image).decode("ascii")}}]}]}
    request = Request(settings["api_base"] + "/chat/completions",
                      data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                      headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        # Let the provider finish; do not impose a local generation or waiting limit.
        with build_opener(NoRedirect()).open(request, timeout=None) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise WorkbenchError("MiniMax 响应过大，已停止读取。", 502, "model_response_invalid")
        return parse_response(json.loads(raw))
    except HTTPError as error:
        hints = {401: "Key 无效或与国内/国际区不匹配", 403: "当前 Key 没有此模型的调用权限",
                 429: "达到套餐额度或速率限制，请稍后手动重试"}
        detail = hints.get(error.code, "模型请求失败")
        try:
            body = json.loads(error.read(16384))
            provider = body.get("error") or body.get("base_resp") or {}
            if isinstance(provider, dict):
                detail += "：" + str(provider.get("message") or provider.get("status_msg") or "")
        except (ValueError, OSError, AttributeError):
            pass
        raise WorkbenchError(f"MiniMax HTTP {error.code} — {safe_error(detail, key)}",
                             502, "model_request_failed") from None
    except (TimeoutError, URLError) as error:
        timed_out = isinstance(error, TimeoutError) or isinstance(getattr(error, "reason", None), TimeoutError)
        detail = "模型请求超时，可手动重试。" if timed_out else "无法连接 MiniMax，请检查网络后重试。"
        raise WorkbenchError(detail, 502, "model_request_failed") from None
    except (ValueError, UnicodeError):
        raise WorkbenchError("MiniMax 返回的响应不是有效 JSON。", 502, "model_response_invalid") from None


class QuickTests:
    def __init__(self, workbench, caller=call_minimax):
        self.workbench, self.caller = workbench, caller
        self.project = Path(workbench.config["config_path"]).resolve().parents[2]
        self.root = contained_path(workbench.root, "quick_tests")
        self.settings = {"model": "MiniMax-M3", "api_base": "https://api.minimaxi.com/v1",
                         **workbench.config.get("quick_test", {})}
        if self.settings["api_base"] not in API_BASES or self.settings["model"] != "MiniMax-M3":
            raise WorkbenchError("Quick Test 须使用 MiniMax 官方接口与 MiniMax-M3。")
        self.lock, self.active, self.closed = threading.RLock(), None, False

    def _path(self, cid):
        if not isinstance(cid, str) or not re.fullmatch(r"[0-9a-f]{32}", cid):
            raise WorkbenchError("候选 ID 无效。")
        return contained_path(self.root, cid + ".json")

    def snapshot(self, state):
        with self.lock:
            candidate = state.get("candidate")
            job = None
            if candidate:
                cid = candidate["candidate_id"]
                path = self._path(cid)
                if self.active and self.active["candidate_id"] == cid:
                    job = copy.deepcopy(self.active)
                elif path.is_file():
                    job = read_json(path)
                    if job.get("status") == "running":
                        job.update(status="interrupted", error="上次测试随服务停止而中断；需要时可手动重试。")
                        atomic_json(path, job)
                if job and any(job.get(key) != value for key, value in {
                        "candidate_id": cid, "pixel_sha256": candidate["pixel_sha256"],
                        "parameter_key": candidate["parameter_key"], "input_revision": state["input_revision"]}.items()):
                    job = None
            return {"model": self.settings["model"], "configured": bool(load_api_key(self.project)),
                    "running_candidate_id": self.active["candidate_id"] if self.active else None, "job": job}

    def start(self, body):
        packet, image = self.workbench.quick_test_input(
            body["question_id"], body["candidate_id"], body["context_token"],
            body["pixel_sha256"], body["parameter_key"])
        key = load_api_key(self.project)
        if not key:
            raise WorkbenchError("请在项目 .env 中配置 MINIMAX_API_KEY 后重试。", 400, "missing_api_key")
        with self.lock:
            if self.closed:
                raise WorkbenchError("工作台正在停止，请重启后再试。", 409, "server_stopping")
            if self.active:
                if self.active["candidate_id"] == packet["candidate_id"]:
                    return copy.deepcopy(self.active)
                raise WorkbenchError("已有一个 Quick Test 正在运行，请等待完成。", 409, "quick_test_running")
            job = {**packet, "run_id": uuid.uuid4().hex, "status": "running", "started_at": timestamp(),
                   "model": self.settings["model"], "answer": "", "thinking": "", "error": None}
            atomic_json(self._path(job["candidate_id"]), job)
            self.active = job
            threading.Thread(target=self._run, args=(copy.deepcopy(job), image, key), daemon=True).start()
            return copy.deepcopy(job)

    def _run(self, job, image, key):
        start = time.monotonic()
        try:
            result = self.caller(self.settings, key, job["question"], image)
            job.update(result, status="completed")
        except Exception as error:
            message = str(error) if isinstance(error, WorkbenchError) else "Quick Test 调用失败，请重试或检查模型接口。"
            job.update(status="error", error=safe_error(message, key))
        job.update(finished_at=timestamp(), elapsed_seconds=round(time.monotonic() - start, 2))
        with self.lock:
            if self.closed:
                return
            try:
                atomic_json(self._path(job["candidate_id"]), job)
            finally:
                self.active = None

    def close(self):
        with self.lock:
            self.closed = True
            if self.active:
                job = {**self.active, "status": "interrupted", "error": "服务停止，测试已中断；需要时可手动重试。"}
                atomic_json(self._path(job["candidate_id"]), job)
                self.active = None
