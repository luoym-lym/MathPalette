"""Start the workbench with the Python environment frozen in its saved recipes.

Keep this launcher standard-library-only: desktop CMD may initially select a
different Python, including one without the rendering dependencies installed.
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[1]
PACKAGES = ("matplotlib", "numpy", "pillow")
PROBE = """
import json, platform
from importlib.metadata import PackageNotFoundError, version
environment = {"python": platform.python_version()}
for name in ("matplotlib", "numpy", "pillow"):
    try:
        environment[name] = version(name)
    except PackageNotFoundError:
        environment[name] = None
print(json.dumps(environment))
"""


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def launch_config(arguments):
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    parser.add_argument("--config", type=Path, default=ROOT / "config.json")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args, _ = parser.parse_known_args(arguments)
    if bool(args.data_dir) != bool(args.output_dir):
        raise ValueError("隔离测试须同时指定 --data-dir 与 --output-dir。")
    path = args.config.resolve()
    config = read_json(path)
    for key in ("runtime_dir", "output_dir"):
        config[key] = (path.parent / config[key]).resolve()
    if args.data_dir:
        config.update(runtime_dir=args.data_dir.resolve(), output_dir=args.output_dir.resolve())
    return config


def absolute_path_arguments(arguments):
    """The child runs in workbench/, but CLI paths belong to the invoking cwd."""
    result = list(arguments)
    for index, argument in enumerate(result):
        for flag in ("--config", "--data-dir", "--output-dir"):
            if argument == flag and index + 1 < len(result):
                result[index + 1] = str(Path(result[index + 1]).resolve())
            elif argument.startswith(flag + "="):
                result[index] = flag + "=" + str(Path(argument.split("=", 1)[1]).resolve())
    return result


def required_environment(config):
    required = {}
    for line in (PROJECT / "requirements.txt").read_text(encoding="utf-8-sig").splitlines():
        name, separator, version = line.split("#", 1)[0].strip().partition("==")
        if separator and name.strip().lower() in PACKAGES:
            required[name.strip().lower()] = version.strip()
    if set(required) != set(PACKAGES):
        raise ValueError("requirements.txt 必须固定 matplotlib、numpy、pillow 的版本。")
    # Passed recipes survive removal of runtime caches and include the Python
    # version as well. Never rewrite them to fit the Python chosen by PATH.
    for path in sorted(config["output_dir"].glob("*/recipes.json")):
        for recipe in read_json(path):
            environment = recipe["environment"]
            if any(environment.get(key) != value for key, value in required.items()):
                raise ValueError(f"{path} 的冻结环境与依赖要求不一致；请恢复匹配的版本。")
            required["python"] = environment["python"]
    return required


def python_candidates():
    override = os.environ.get("MATHPALETTE_PYTHON")
    if override:
        return [Path(override).expanduser()]
    candidates = [Path(sys.executable)]
    prefixes = [Path.home() / "Desktop" / "PythonEnvs" / "mathpalette-analytics",
                PROJECT / ".venv", PROJECT / "venv"]
    if os.environ.get("CONDA_PREFIX"):
        prefixes.append(Path(os.environ["CONDA_PREFIX"]))
    prefixes.extend(Path.home() / name for name in ("miniconda3", "anaconda3"))
    conda_environments = Path.home() / ".conda" / "environments.txt"
    if conda_environments.is_file():
        prefixes.extend(Path(line.strip()) for line in conda_environments.read_text(
            encoding="utf-8-sig").splitlines() if line.strip())
    for prefix in prefixes:
        candidates.extend(prefix / name for name in ("python.exe", "Scripts/python.exe", "bin/python"))
    for directory in os.get_exec_path():
        if directory:
            candidates.extend(Path(directory) / name for name in ("python.exe", "python3", "python"))
    return list(dict.fromkeys(path.resolve() for path in candidates if path.is_file()))


def select_python(required):
    checked = []
    for path in python_candidates():
        try:
            result = subprocess.run([str(path), "-X", "utf8", "-B", "-c", PROBE],
                                    capture_output=True, text=True, encoding="utf-8", timeout=10)
            environment = json.loads(result.stdout) if result.returncode == 0 else {}
        except (OSError, ValueError, subprocess.TimeoutExpired):
            environment = {}
        checked.append(f"  {path}: {json.dumps(environment, ensure_ascii=False)}")
        if all(environment.get(key) == value for key, value in required.items()):
            return path, environment
    raise ValueError("未找到与正式数据匹配的 Python 环境。\n需要：" +
                     json.dumps(required, ensure_ascii=False) + "\n已检查：\n" + "\n".join(checked) +
                     "\n可将 MATHPALETTE_PYTHON 设置为匹配环境的 python.exe 完整路径。")


def main():
    arguments = absolute_path_arguments(sys.argv[1:])
    config = launch_config(arguments)
    python, environment = select_python(required_environment(config))
    print(f"MathPalette Python: {python}", flush=True)
    print("Render environment: " + json.dumps(environment), flush=True)
    service_path = Path(config["runtime_dir"]) / "state" / "service.json"
    if service_path.is_file() and not any(flag in arguments for flag in ("--check", "--help", "-h")):
        service = read_json(service_path)
        url = service["url"]
        if urlparse(url).hostname not in ("localhost", "127.0.0.1"):
            raise SystemExit("Unexpected workbench address.")
        try:
            with build_opener(ProxyHandler({})).open(url + "/api/health", timeout=2) as response:
                health = json.load(response)
        except (URLError, TimeoutError):
            health = None
        if health:
            if health.get("session_id") != service["session_id"]:
                raise SystemExit("Another service uses this address; close it before starting.")
            with build_opener(ProxyHandler({})).open(url + "/api/state", timeout=2) as response:
                state = json.load(response)
            request = Request(url + "/api/shutdown", data=b"{}", method="POST",
                              headers={"Content-Type": "application/json", "X-Review-Token": state["review_token"]})
            with build_opener(ProxyHandler({})).open(request, timeout=3) as response:
                json.load(response)
            deadline = time.monotonic() + 10
            while service_path.exists() and time.monotonic() < deadline:
                time.sleep(.1)
            if service_path.exists():
                raise SystemExit("The previous server is still saving. Wait and try again.")
    raise SystemExit(subprocess.call([str(python), "-X", "utf8", "-B", str(ROOT / "server.py"),
                                     "--open-browser", *arguments], cwd=ROOT))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
