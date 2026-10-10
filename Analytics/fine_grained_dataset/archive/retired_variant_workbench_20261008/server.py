"""Loopback-only, dependency-free HTTP service for the human review workbench."""

from __future__ import annotations

import argparse
import json
import secrets
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from review_store import Workbench
from workbench_io import ROOT, WorkbenchError, contained_path, load_config


def make_handler(workbench):
    api_token = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        server_version = "MathPalette/1.0"

        def log_message(self, format, *args):
            if args and str(args[1] if len(args) > 1 else "").startswith("5"):
                super().log_message(format, *args)

        def send_data(self, data, content_type, status=200):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("Content-Security-Policy", "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def send_json(self, value, status=200):
            self.send_data(json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8"), "application/json; charset=utf-8", status)

        def state(self):
            return {**workbench.snapshot(), "api_token": api_token}

        def do_GET(self):
            path = urlparse(self.path).path
            try:
                if path == "/api/state":
                    self.send_json(self.state())
                    return
                static = {"/": ("index.html", "text/html; charset=utf-8"),
                          "/app.js": ("app.js", "application/javascript; charset=utf-8"),
                          "/style.css": ("style.css", "text/css; charset=utf-8")}
                if path in static:
                    filename, mime = static[path]
                    self.send_data((ROOT / "web" / filename).read_bytes(), mime)
                    return
                parts = path.strip("/").split("/")
                with workbench.lock:
                    if len(parts) == 3 and parts[:2] == ["media", "original"]:
                        qid = parts[2]
                        if qid not in workbench.adapter.records:
                            raise WorkbenchError("原图不存在。", 404)
                        image = contained_path(workbench.adapter.source, workbench.adapter.records[qid]["image"])
                    elif len(parts) == 3 and parts[:2] == ["media", "candidate"]:
                        candidate = next((q["candidate"] for q in workbench.progress["questions"].values()
                                          if q["candidate"] and q["candidate"]["candidate_id"] == parts[2]), None)
                        if candidate is None or (workbench.root / "state" / "pending_transaction.json").exists():
                            raise WorkbenchError("此候选已删除、已审核或正在恢复。", 404)
                        image = workbench._candidate_path(candidate)
                    elif len(parts) == 4 and parts[:2] == ["media", "accepted"]:
                        qid, slot = parts[2:]
                        question = workbench.progress["questions"].get(qid)
                        recipe = next((r for r in question["accepted"] if r["slot_id"] == slot), None) if question else None
                        if recipe is None:
                            raise WorkbenchError("此槽位尚未通过。", 404)
                        image = contained_path(workbench.root / "accepted", Path(recipe["image_path"]).relative_to("accepted"))
                    else:
                        raise WorkbenchError("页面不存在。", 404)
                    if not image.is_file():
                        raise WorkbenchError("图片文件不存在，请重试或检查本地文件。", 404)
                    self.send_data(image.read_bytes(), "image/png")
            except WorkbenchError as error:
                self.send_json({"error": str(error)}, error.status)
            except (OSError, ValueError) as error:
                self.send_json({"error": f"读取失败：{error}"}, 500)

        def do_POST(self):
            try:
                if self.headers.get("X-Workbench-Token") != api_token:
                    raise WorkbenchError("会话已更新，请刷新页面后重试。", 403)
                origin = self.headers.get("Origin")
                if origin and urlparse(origin).netloc != self.headers.get("Host"):
                    raise WorkbenchError("仅允许当前本地工作台提交审核。", 403)
                if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                    raise WorkbenchError("请求必须是 JSON。", 415)
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 65536:
                    raise WorkbenchError("请求大小无效。", 413)
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise WorkbenchError("请求格式无效。")
                path = urlparse(self.path).path
                if path == "/api/review":
                    workbench.review(data.get("candidate_id"), data.get("decision"))
                elif path == "/api/navigate":
                    workbench.navigate(data.get("question_id"))
                elif path == "/api/skip":
                    workbench.skip(data.get("candidate_id"), data.get("reason") or "用户选择暂不继续尝试此类型。", data.get("operation"))
                elif path == "/api/retry":
                    workbench.retry(data.get("operation"))
                else:
                    raise WorkbenchError("接口不存在。", 404)
                self.send_json(self.state())
            except WorkbenchError as error:
                self.send_json({"error": str(error)}, error.status)
            except (ValueError, TypeError, KeyError) as error:
                self.send_json({"error": f"请求无效：{error}"}, 400)
            except Exception as error:
                self.send_json({"error": f"保存或生成失败：{error}。请重试恢复；保留已有文件。"}, 500)

    return Handler


def main():
    parser = argparse.ArgumentParser(description="MathPalette 本地人工审核工作台")
    parser.add_argument("--port", type=int)
    parser.add_argument("--data-dir", type=Path, help="独立状态/输出目录，可用于隔离测试")
    parser.add_argument("--check", action="store_true", help="校验基线和 80 题可用性后退出，不生成候选")
    parser.add_argument("--open-browser", action="store_true")
    args = parser.parse_args()
    config = load_config()
    if config["host"] not in ("127.0.0.1", "localhost"):
        raise WorkbenchError("本服务仅绑定本机 127.0.0.1/localhost。")
    workbench = Workbench(args.data_dir, config, print)
    try:
        if args.check:
            snapshot = workbench.snapshot()
            availability = {op: sum(meta["operations"][op]["status"] == "available" for meta in workbench.metadata.values())
                            for op in snapshot["operation_names"]}
            print(json.dumps({"baseline_unchanged": True, "questions_checked": 80,
                              "available_questions_by_operation": availability,
                              "accepted": snapshot["global"]["accepted"], "target": 800}, ensure_ascii=False, indent=2))
            return
        workbench._generate_safely()
        port = args.port or config["port"]
        server = ThreadingHTTPServer((config["host"], port), make_handler(workbench))
        url = f"http://127.0.0.1:{server.server_port}"
        print(f"工作台已启动：{url} ；Ctrl+C 停止。正式通过仅由页面人工审核产生。", flush=True)
        if args.open_browser:
            threading.Timer(0.3, lambda: webbrowser.open(url)).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("审核进度已持久保存。")
        finally:
            server.server_close()
    finally:
        workbench.close()


if __name__ == "__main__":
    try:
        main()
    except (WorkbenchError, OSError) as error:
        raise SystemExit(str(error))
