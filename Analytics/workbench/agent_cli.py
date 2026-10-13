"""Machine-readable agent commands. Human Pass/No Pass are intentionally absent."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import ProxyHandler, Request, build_opener

from workbench_io import ROOT, WorkbenchError, load_config, parse_json, read_json


def call_api(url, path, body=None):
    parsed = urlparse(url)
    if parsed.scheme != "http" or parsed.hostname not in ("127.0.0.1", "localhost"):
        raise WorkbenchError("CLI 只连接本机 HTTP 工作台。")
    data = json.dumps(body, ensure_ascii=False, allow_nan=False).encode("utf-8") if body is not None else None
    request = Request(url.rstrip("/") + path, data=data, headers={"Content-Type": "application/json"})
    try:
        with build_opener(ProxyHandler({})).open(request, timeout=300) as response:
            return parse_json(response.read().decode("utf-8"))
    except HTTPError as error:
        try:
            detail = parse_json(error.read().decode("utf-8"))
        except WorkbenchError:
            detail = {"error": str(error), "code": "http_error"}
        raise WorkbenchError(detail.get("error", str(error)), error.code, detail.get("code", "http_error")) from error
    except (URLError, TimeoutError) as error:
        raise WorkbenchError(f"无法连接 C 工作台；先运行 start_workbench.cmd。{error}", 503, "service_unavailable") from error


def main():
    parser = argparse.ArgumentParser(description="向网页提交 C 插件候选；不提供人工审核命令")
    parser.add_argument("--config", type=Path, default=ROOT / "config.json")
    parser.add_argument("--url", help="测试或自定义端口的本机工作台 URL")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("context", "validate", "submit", "status", "highlight"):
        sub = commands.add_parser(name)
        sub.add_argument("--config", type=Path, default=argparse.SUPPRESS)
        sub.add_argument("--url", default=argparse.SUPPRESS)
        if name in ("validate", "submit"):
            sub.add_argument("--plugin", type=Path, required=True)
        if name == "submit":
            sub.add_argument("--context-token", required=True)
            sub.add_argument("--replace", help="仅在用户要求修改当前待审候选时使用")
        if name == "status":
            sub.add_argument("--candidate", required=True)
        if name == "highlight":
            sub.add_argument("--object", required=True)
            sub.add_argument("--question", help="默认使用网页当前题目")
    args = parser.parse_args()
    config = load_config(args.config)
    registry = Path(config["runtime_dir"]) / "state" / "service.json"
    url = args.url or (read_json(registry)["url"] if registry.exists() else f"http://127.0.0.1:{config['port']}")
    if args.command == "context":
        result = call_api(url, "/api/context")
    elif args.command == "status":
        result = call_api(url, "/api/status/" + quote(args.candidate, safe=""))
    elif args.command == "highlight":
        qid = args.question or call_api(url, "/api/context")["question_id"]
        result = call_api(url, "/api/highlight", {"question_id": qid, "object_id": args.object})
    else:
        body = {"plugin_path": str(args.plugin.resolve())}
        if args.command == "submit":
            body.update(context_token=args.context_token, replace=args.replace)
        result = call_api(url, "/api/" + args.command, body)
    print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        main()
    except (WorkbenchError, OSError) as error:
        print(json.dumps({"ok": False, "error": str(error), "code": getattr(error, "code", "file_error")}, ensure_ascii=False))
        raise SystemExit(1)
