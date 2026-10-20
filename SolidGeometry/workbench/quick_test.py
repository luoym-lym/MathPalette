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
MIMO_API_BASE = "https://token-plan-cn.xiaomimimo.com/v1"
PROVIDERS = {
    "minimax": {"label": "MiniMax", "api_key_env": "MINIMAX_API_KEY", "api_bases": API_BASES},
    "mimo": {"label": "小米 MiMo", "api_key_env": "MIMO_API_KEY", "api_bases": {MIMO_API_BASE}},
}
MAX_RESPONSE_BYTES = 8 * 1024 * 1024
TEST_PROFILES = {
    "quicktest1": {"label": "Quick Test 1", "provider": "minimax", "model": "MiniMax-M3",
                   "thinking": {"type": "disabled"}},
    "quicktest2": {"label": "Quick Test 2", "provider": "minimax", "model": "MiniMax-M3.1-Flash-Preview",
                   "thinking": {"type": "adaptive"}, "reasoning_effort": "low"},
    "quicktest3": {"label": "Quick Test 3", "provider": "mimo", "model": "mimo-v2.6-flash",
                   "thinking": {"type": "disabled"}},
    "quicktest4": {"label": "Quick Test 4", "provider": "mimo", "model": "mimo-v2.6-flash",
                   "thinking": {"type": "enabled"}},
}
DEFAULT_PROFILE = "quicktest1"


def load_api_key(project, variable="MINIMAX_API_KEY"):
    key = os.environ.get(variable, "").strip()
    path = Path(project) / ".env"
    if not key and path.is_file():
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            match = re.match(rf"\s*(?:export\s+)?{re.escape(variable)}\s*=\s*(.*?)\s*$", line)
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
    return re.sub(r"(?:sk|tp|ttp)-[A-Za-z0-9_-]+", "[REDACTED]", message)[:1000]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward the subscription credential to a redirected address.
        return None


def parse_response(data, provider="MiniMax"):
    if not isinstance(data, dict):
        raise WorkbenchError(f"{provider} 返回了无效响应。", 502, "model_response_invalid")
    base = data.get("base_resp") or {}
    if data.get("error") or base.get("status_code", 0) != 0:
        error = data.get("error") or base
        message = error.get("message") or error.get("status_msg") if isinstance(error, dict) else str(error)
        raise WorkbenchError(provider + "：" + str(message), 502, "model_request_failed")
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
        raise WorkbenchError(f"{provider} 没有返回回答。", 502, "model_response_invalid")
    choice = choices[0]
    message = choice.get("message") or {}
    answer, thinking = message.get("content") or "", message.get("reasoning_content") or ""
    if not isinstance(answer, str) or not isinstance(thinking, str):
        raise WorkbenchError(f"{provider} 返回了无法识别的回答格式。", 502, "model_response_invalid")
    # Some compatible responses still place thinking inside content.
    embedded = re.findall(r"<think>(.*?)</think>", answer, flags=re.DOTALL)
    if embedded:
        if not thinking:
            thinking = "\n\n".join(embedded)
        answer = re.sub(r"<think>.*?</think>", "", answer, flags=re.DOTALL)
    if not answer.strip() and not thinking.strip():
        raise WorkbenchError(f"{provider} 返回了空回答。", 502, "model_response_invalid")
    return {"answer": answer.strip(), "thinking": thinking.strip(),
            "finish_reason": choice.get("finish_reason"), "usage": data.get("usage") or {},
            "response_model": data.get("model"), "truncated": choice.get("finish_reason") == "length"}


def call_model(settings, key, question, image):
    provider = PROVIDERS[settings.get("provider", "minimax")]
    label = provider["label"]
    if settings["api_base"] not in provider["api_bases"]:
        raise WorkbenchError(f"{label} 接口地址无效。")
    payload = {"model": settings["model"], "stream": False,
               "thinking": copy.deepcopy(settings.get("thinking", {"type": "disabled"})),
               "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": [
                                {"type": "text", "text": question},
                                {"type": "image_url", "image_url": {
                                    "url": "data:image/png;base64," + base64.b64encode(image).decode("ascii")}}]}]}
    if "reasoning_effort" in settings:
        payload["reasoning_effort"] = settings["reasoning_effort"]
    request = Request(settings["api_base"] + "/chat/completions",
                      data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                      headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        # Let the provider finish; do not impose a local generation or waiting limit.
        with build_opener(NoRedirect()).open(request, timeout=None) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise WorkbenchError(f"{label} 响应过大，已停止读取。", 502, "model_response_invalid")
        return parse_response(json.loads(raw), label)
    except HTTPError as error:
        hints = {401: "Key 无效或与国内/国际区不匹配", 403: "当前 Key 没有此模型的调用权限",
                 429: "达到套餐额度或速率限制，请稍后手动重试"}
        detail = hints.get(error.code, "模型请求失败")
        try:
            body = json.loads(error.read(16384))
            provider_error = body.get("error") or body.get("base_resp") or {}
            if isinstance(provider_error, dict):
                detail += "：" + str(provider_error.get("message") or provider_error.get("status_msg") or "")
        except (ValueError, OSError, AttributeError):
            pass
        raise WorkbenchError(f"{label} HTTP {error.code} — {safe_error(detail, key)}",
                             502, "model_request_failed") from None
    except (TimeoutError, URLError) as error:
        timed_out = isinstance(error, TimeoutError) or isinstance(getattr(error, "reason", None), TimeoutError)
        detail = "模型请求超时，可手动重试。" if timed_out else f"无法连接 {label}，请检查网络后重试。"
        raise WorkbenchError(detail, 502, "model_request_failed") from None
    except (ValueError, UnicodeError):
        raise WorkbenchError(f"{label} 返回的响应不是有效 JSON。", 502, "model_response_invalid") from None


def call_minimax(settings, key, question, image):
    return call_model({**settings, "provider": "minimax"}, key, question, image)


class QuickTests:
    def __init__(self, workbench, caller=call_model):
        self.workbench, self.caller = workbench, caller
        self.project = Path(workbench.config["config_path"]).resolve().parents[2]
        self.root = contained_path(workbench.root, "quick_tests")
        self.settings = {"model": "MiniMax-M3", "api_base": "https://api.minimaxi.com/v1",
                         **workbench.config.get("quick_test", {})}
        if self.settings["api_base"] not in API_BASES or self.settings["model"] != "MiniMax-M3":
            raise WorkbenchError("Quick Test 须使用 MiniMax 官方接口；默认模型为 MiniMax-M3。")
        self.mimo_api_base = self.settings.pop("mimo_api_base", MIMO_API_BASE)
        if self.mimo_api_base not in PROVIDERS["mimo"]["api_bases"]:
            raise WorkbenchError("Quick Test 3、4 须使用小米 Token Plan 官方接口。")
        self.lock, self.active, self.closed = threading.RLock(), None, False

    def _path(self, cid, profile=DEFAULT_PROFILE):
        if not isinstance(cid, str) or not re.fullmatch(r"[0-9a-f]{32}", cid):
            raise WorkbenchError("候选 ID 无效。")
        if not isinstance(profile, str) or profile not in TEST_PROFILES:
            raise WorkbenchError("Quick Test 模式无效。", 400, "invalid_quick_test_profile")
        # Keep the original filename for existing M3 results.
        suffix = "" if profile == DEFAULT_PROFILE else "." + profile
        return contained_path(self.root, cid + suffix + ".json")

    def snapshot(self, state):
        with self.lock:
            candidate = state.get("candidate")
            jobs = {profile: None for profile in TEST_PROFILES}
            if candidate:
                cid = candidate["candidate_id"]
                for profile, settings in TEST_PROFILES.items():
                    path = self._path(cid, profile)
                    job = None
                    if self.active and self.active["candidate_id"] == cid and self.active["profile"] == profile:
                        job = copy.deepcopy(self.active)
                    elif path.is_file():
                        job = read_json(path)
                        if job.get("status") == "running":
                            job.update(status="interrupted", error="上次测试随服务停止而中断；需要时可手动重试。")
                            atomic_json(path, job)
                    if job and (job.get("profile", DEFAULT_PROFILE) != profile or
                                job.get("model") != settings["model"] or
                                any(job.get(key) != value for key, value in {
                        "branch": "SolidGeometry", "question_id": state["question_id"],
                        "png_sha256": candidate["png_sha256"],
                        "candidate_id": cid, "pixel_sha256": candidate["pixel_sha256"],
                        "parameter_key": candidate["parameter_key"], "input_revision": state["input_revision"]}.items())):
                        job = None
                    jobs[profile] = job
            configured = {name: bool(load_api_key(self.project, provider["api_key_env"]))
                          for name, provider in PROVIDERS.items()}
            return {"model": self.settings["model"], "profiles": copy.deepcopy(TEST_PROFILES),
                    "configured": configured["minimax"],
                    "configured_profiles": {profile: configured[settings["provider"]]
                                            for profile, settings in TEST_PROFILES.items()},
                    "running_candidate_id": self.active["candidate_id"] if self.active else None,
                    "running_profile": self.active["profile"] if self.active else None,
                    "jobs": jobs, "job": jobs[DEFAULT_PROFILE]}

    def start(self, body):
        profile = body.get("profile", DEFAULT_PROFILE)
        if not isinstance(profile, str) or profile not in TEST_PROFILES:
            raise WorkbenchError("Quick Test 模式无效。", 400, "invalid_quick_test_profile")
        settings = {**self.settings, **copy.deepcopy(TEST_PROFILES[profile])}
        provider = PROVIDERS[settings["provider"]]
        if settings["provider"] == "mimo":
            settings["api_base"] = self.mimo_api_base
            settings.pop("reasoning_effort", None)
        packet, image = self.workbench.quick_test_input(
            body["question_id"], body["candidate_id"], body["context_token"],
            body["pixel_sha256"], body["parameter_key"])
        key = load_api_key(self.project, provider["api_key_env"])
        if not key:
            raise WorkbenchError(f"请在项目 .env 中配置 {provider['api_key_env']} 后重试。", 400, "missing_api_key")
        with self.lock:
            if self.closed:
                raise WorkbenchError("工作台正在停止，请重启后再试。", 409, "server_stopping")
            if self.active:
                if self.active["candidate_id"] == packet["candidate_id"] and self.active["profile"] == profile:
                    return copy.deepcopy(self.active)
                raise WorkbenchError("已有一个 Quick Test 正在运行，请等待完成。", 409, "quick_test_running")
            job = {**packet, "run_id": uuid.uuid4().hex, "status": "running", "started_at": timestamp(),
                   "profile": profile, "provider": settings["provider"], "model": settings["model"], "thinking_mode": settings["thinking"]["type"],
                   "reasoning_effort": settings.get("reasoning_effort"), "answer": "", "thinking": "", "error": None}
            atomic_json(self._path(job["candidate_id"], job["profile"]), job)
            self.active = job
            threading.Thread(target=self._run, args=(copy.deepcopy(job), image, key, settings), daemon=True).start()
            return copy.deepcopy(job)

    def _run(self, job, image, key, settings):
        start = time.monotonic()
        try:
            result = self.caller(settings, key, job["question"], image)
            job.update(result, status="completed")
        except Exception as error:
            message = str(error) if isinstance(error, WorkbenchError) else "Quick Test 调用失败，请重试或检查模型接口。"
            job.update(status="error", error=safe_error(message, key))
        job.update(finished_at=timestamp(), elapsed_seconds=round(time.monotonic() - start, 2))
        with self.lock:
            if self.closed:
                return
            try:
                atomic_json(self._path(job["candidate_id"], job["profile"]), job)
            finally:
                self.active = None

    def close(self):
        with self.lock:
            self.closed = True
            if self.active:
                job = {**self.active, "status": "interrupted", "error": "服务停止，测试已中断；需要时可手动重试。"}
                atomic_json(self._path(job["candidate_id"], job["profile"]), job)
                self.active = None
