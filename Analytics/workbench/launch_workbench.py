"""Start or gracefully restart this workbench from its desktop shortcut."""
import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from workbench_io import ROOT, load_config, read_json


def main():
    config = load_config()
    service_path = Path(config["runtime_dir"]) / "state" / "service.json"
    if service_path.is_file():
        service = read_json(service_path)
        url = service["url"]
        if urlparse(url).hostname not in ("localhost", "127.0.0.1"):
            raise SystemExit("Unexpected workbench address.")
        try:
            with urlopen(url + "/api/health", timeout=2) as response:
                health = json.load(response)
        except URLError:
            health = None
        if health:
            if health.get("session_id") != service["session_id"]:
                raise SystemExit("Another service uses this address; close it before starting.")
            with urlopen(url + "/api/state", timeout=2) as response:
                state = json.load(response)
            request = Request(url + "/api/shutdown", data=b"{}", method="POST",
                              headers={"Content-Type": "application/json", "X-Review-Token": state["review_token"]})
            with urlopen(request, timeout=3) as response:
                json.load(response)
            deadline = time.monotonic() + 10
            while service_path.exists() and time.monotonic() < deadline:
                time.sleep(.1)
            if service_path.exists():
                raise SystemExit("The previous server is still saving. Wait and try again.")
    raise SystemExit(subprocess.call([sys.executable, "-B", str(ROOT / "server.py"),
                                     "--open-browser", *sys.argv[1:]], cwd=ROOT))


if __name__ == "__main__":
    main()
