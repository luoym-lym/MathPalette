"""Loopback HTTP server for the C workbench and the terminal agent CLI."""
from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

from review_store import Workbench
from quick_test import QuickTests
from workbench_io import (ROOT, WorkbenchError, atomic_json, contained_path, load_config,
                          parse_json, read_json)


def make_handler(workbench, quick_tests=None):
    quick_tests = quick_tests or QuickTests(workbench)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            if self.path not in ("/api/state", "/api/context"):
                super().log_message(format, *args)

        def _send(self, data, content_type="application/json; charset=utf-8", status=200):
            if isinstance(data, dict) and "review_token" in data and "questions" in data:
                data = {**data, "quick_test": quick_tests.snapshot(data)}
            if not isinstance(data, bytes):
                data = json.dumps(data, ensure_ascii=False, allow_nan=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def _error(self, error):
            status = error.status if isinstance(error, WorkbenchError) else 500
            code = error.code if isinstance(error, WorkbenchError) else "internal_error"
            self._send({"ok": False, "error": str(error), "code": code}, status=status)

        def _guard_host(self):
            host = self.headers.get("Host", "")
            allowed = (f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}")
            if host not in allowed:
                raise WorkbenchError("仅允许本机工作台地址。", 403, "invalid_host")
            origin = self.headers.get("Origin")
            if origin and origin != "http://" + host:
                raise WorkbenchError("不接受其他网页来源的请求。", 403, "invalid_origin")

        def do_GET(self):
            try:
                self._guard_host()
                path = unquote(urlparse(self.path).path)
                if path == "/api/state":
                    return self._send(workbench.snapshot())
                if path == "/api/context":
                    return self._send(workbench.context())
                if path.startswith("/api/drawing-scene/"):
                    return self._send(workbench.drawing_scene(path.removeprefix("/api/drawing-scene/")))
                if path == "/api/health":
                    return self._send({"ready": True, "session_id": workbench.session_id, "question_count": len(workbench.adapter.records)})
                if path == "/api/prompt":
                    return self._send((ROOT / "agent_prompt.md").read_bytes(), "text/plain; charset=utf-8")
                if path.startswith("/api/status/"):
                    return self._send(workbench.status(path.removeprefix("/api/status/")))
                if path.startswith("/api/original-image/"):
                    qid = path.removeprefix("/api/original-image/")
                    if qid not in workbench.adapter.records:
                        raise WorkbenchError("题号不存在。", 404)
                    return self._send(workbench.adapter.original_paths[qid].read_bytes(), "image/png")
                if path.startswith("/api/candidate-image/"):
                    cid = path.removeprefix("/api/candidate-image/")
                    with workbench.lock:
                        candidate = workbench.progress["candidates"].get(cid)
                        if not candidate or candidate["status"] != "pending":
                            raise WorkbenchError("此候选已不在待审状态。", 404, "stale_candidate")
                        workbench._verify_package(candidate)
                        return self._send(workbench._package_file(candidate, "image.png").read_bytes(), "image/png")
                if path.startswith("/api/accepted-image/"):
                    parts = path.removeprefix("/api/accepted-image/").split("/")
                    if len(parts) != 2 or parts[0] not in workbench.progress["questions"]:
                        raise WorkbenchError("正式图片路径无效。", 404)
                    recipe = next((r for r in workbench.progress["questions"][parts[0]]["accepted"]
                                   if r["slot_id"] == parts[1]), None)
                    if not recipe:
                        raise WorkbenchError("正式槽位不存在。", 404)
                    return self._send(workbench._accepted_path(recipe["image_path"]).read_bytes(), "image/png")
                if path.startswith("/api/reference-image/"):
                    name = path.removeprefix("/api/reference-image/")
                    if not name.startswith("reference-") or "/" in name or "\\" in name or not name.endswith(".png"):
                        raise WorkbenchError("参考图路径无效。", 404)
                    return self._send(contained_path(workbench.root / "reproduced", name).read_bytes(), "image/png")
                static = {"/": ("index.html", "text/html; charset=utf-8"),
                          "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                          "/quick-test.js": ("quick-test.js", "text/javascript; charset=utf-8"),
                          "/drawing-board.js": ("drawing-board.js", "text/javascript; charset=utf-8"),
                          "/partial-selection.js": ("partial-selection.js", "text/javascript; charset=utf-8"),
                          "/geometry-input.js": ("geometry-input.js", "text/javascript; charset=utf-8"),
                          "/style.css": ("style.css", "text/css; charset=utf-8")}
                if path in static:
                    name, mime = static[path]
                    return self._send((ROOT / "web" / name).read_bytes(), mime)
                raise WorkbenchError("路径不存在。", 404, "not_found")
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                pass
            except Exception as error:
                self._error(error)

        def do_POST(self):
            try:
                self._guard_host()
                if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
                    raise WorkbenchError("请求须使用 application/json。", 415)
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 1024 * 1024:
                    raise WorkbenchError("请求大小无效。", 413)
                body = parse_json(self.rfile.read(length).decode("utf-8"))
                if not isinstance(body, dict):
                    raise WorkbenchError("请求必须为 JSON 对象。")
                path = urlparse(self.path).path
                if path == "/api/validate":
                    return self._send(workbench.validate(body["plugin_path"]))
                if path == "/api/submit":
                    return self._send(workbench.submit(body["plugin_path"], body["context_token"], body.get("replace")))
                if path == "/api/highlight":
                    return self._send(workbench.highlight(body["question_id"], body["object_id"]))
                if path in ("/api/navigate", "/api/review", "/api/drawing-preview", "/api/drawing-submit", "/api/collect", "/api/mark-special", "/api/reopen", "/api/delete-accepted", "/api/shutdown", "/api/quick-test"):
                    token = self.headers.get("X-Review-Token", "")
                    if not hmac.compare_digest(token, workbench.review_token):
                        raise WorkbenchError("页面会话已过期；请刷新工作台。", 403, "invalid_session")
                    if path == "/api/quick-test":
                        return self._send(quick_tests.start(body), status=202)
                    if path == "/api/shutdown":
                        self._send({"stopping": True})
                        threading.Thread(target=self.server.shutdown, daemon=True).start()
                        return
                    if path == "/api/navigate":
                        return self._send(workbench.navigate(body["question_id"]))
                    if path == "/api/mark-special":
                        return self._send(workbench.mark_special(body["question_id"], body["context_token"]))
                    if path == "/api/collect":
                        return self._send(workbench.collect(body["question_id"], body["context_token"]))
                    if path == "/api/reopen":
                        return self._send(workbench.reopen(body["question_id"], body["context_token"]))
                    if path == "/api/delete-accepted":
                        return self._send(workbench.delete_accepted(body["question_id"], body["candidate_id"],
                            body["slot_id"], body["context_token"], body["pixel_sha256"], body["parameter_key"]))
                    if path == "/api/drawing-preview":
                        return self._send(workbench.drawing_preview(body["plugin"], body["context_token"], body.get("replace")))
                    if path == "/api/drawing-submit":
                        return self._send(workbench.drawing_submit(body["plugin"], body["context_token"], body.get("replace"),
                            body["pixel_sha256"], body["parameter_key"]))
                    return self._send(workbench.review(body["question_id"], body["candidate_id"], body["decision"],
                        body["context_token"], body["pixel_sha256"], body["parameter_key"], body.get("note", "")))
                raise WorkbenchError("路径不存在。", 404)
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                pass
            except (KeyError, TypeError, ValueError, UnicodeError) as error:
                self._error(WorkbenchError(f"请求字段无效：{error}"))
            except Exception as error:
                self._error(error)
    return Handler


def main():
    parser = argparse.ArgumentParser(description="MathPalette C 特殊标记协作工作台")
    parser.add_argument("--config", type=Path, default=ROOT / "config.json")
    parser.add_argument("--port", type=int)
    parser.add_argument("--data-dir", type=Path, help="独立运行状态目录；测试时与 --output-dir 一起指定")
    parser.add_argument("--output-dir", type=Path, help="独立正式输出目录；测试不能使用默认正式目录")
    parser.add_argument("--check", action="store_true", help="校验本批全部原题并退出，不生成候选")
    parser.add_argument("--open-browser", action="store_true")
    args = parser.parse_args()
    config = load_config(args.config)
    if bool(args.data_dir) != bool(args.output_dir):
        raise WorkbenchError("隔离测试须同时指定 --data-dir 与 --output-dir。")
    if args.data_dir:
        config["runtime_dir"] = str(args.data_dir.resolve())
        config["output_dir"] = str(args.output_dir.resolve())
        config["dataset_root"] = str(args.output_dir.resolve().parent)
    workbench = Workbench(config, lambda line: print(line, flush=True))
    registry = workbench.state_dir / "service.json"
    quick_tests = None
    try:
        if args.check:
            print(json.dumps({"questions_checked": len(workbench.active_questions()), "noop_pixels_match": True,
                              "baseline_fingerprint": workbench.adapter.manifest["fingerprint"],
                              "collected_questions": workbench.snapshot()["collected_total"],
                              "accepted_count": workbench.snapshot()["accepted_total"], "candidates_generated": 0},
                             ensure_ascii=False, indent=2))
            return
        port = args.port if args.port is not None else config["port"]
        quick_tests = QuickTests(workbench)
        server = ThreadingHTTPServer((config["host"], port), make_handler(workbench, quick_tests))
        server.daemon_threads = False
        url = f"http://127.0.0.1:{server.server_port}"
        atomic_json(registry, {"url": url, "pid": os.getpid(), "session_id": workbench.session_id})
        print(f"C 工作台已启动：{url} ；Ctrl+C 停止。Pass 由用户在网页执行。", flush=True)
        if args.open_browser:
            threading.Timer(.3, lambda: webbrowser.open(url)).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("C 工作台已停止；待审候选与收集结果已保存。", flush=True)
        finally:
            server.server_close()
    finally:
        if quick_tests:
            quick_tests.close()
        workbench.close()
        if registry.exists() and read_json(registry).get("session_id") == workbench.session_id:
            registry.unlink()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        main()
    except (WorkbenchError, OSError) as error:
        raise SystemExit(str(error))
