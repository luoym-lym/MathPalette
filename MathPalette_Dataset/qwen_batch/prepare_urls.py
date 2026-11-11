"""Replace image URL placeholders in Batch templates. No inference or upload."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

PLACEHOLDER = "https://replace-image-host.invalid/mathpalette"
PACKAGE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image-base-url", required=True,
                        help="HTTPS prefix above images/, e.g. https://bucket.example.com/mathpalette")
    parser.add_argument("--output-dir", type=Path, default=PACKAGE / "ready")
    args = parser.parse_args()
    base = args.image_base_url.rstrip("/")
    parsed = urlsplit(base)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password
            or parsed.query or parsed.fragment or parsed.hostname == "localhost"
            or parsed.hostname.endswith(".invalid") or any(c.isspace() for c in base)
            or ".." in parsed.path.split("/")):
        parser.error("Use a real public HTTPS prefix without query, fragment, credentials, or placeholders.")
    output = args.output_dir.resolve()
    if output.exists() and any(output.iterdir()):
        parser.error("Output directory is not empty; choose another --output-dir to preserve previous requests.")

    # Validate every template before writing any output.
    prepared, counts = {}, {}
    for path in sorted((PACKAGE / "templates").glob("*.template.jsonl")):
        lines, seen = [], set()
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            request = json.loads(line)
            custom_id = request["custom_id"]
            if custom_id in seen or len(custom_id) > 256:
                raise ValueError(f"Invalid/duplicate custom_id: {path.name}:{number}")
            seen.add(custom_id)
            if request["method"] != "POST" or request["url"] != "/v1/chat/completions":
                raise ValueError(f"Invalid Batch endpoint: {path.name}:{number}")
            body = request["body"]
            if body["model"] != "qwen3.8-max" or body.get("enable_thinking") is not True:
                raise ValueError(f"Unexpected model or thinking mode: {path.name}:{number}")
            if "extra_body" in body:
                raise ValueError("Batch parameters must be at the body top level")
            images = [part for message in body["messages"]
                      if isinstance(message.get("content"), list) for part in message["content"]
                      if part.get("type") == "image_url"]
            if len(images) != 1:
                raise ValueError("Each MathPalette sample must reference exactly one image")
            old = images[0]["image_url"]["url"]
            if not old.startswith(PLACEHOLDER + "/images/"):
                raise ValueError("Expected the original image URL placeholder")
            relative = old[len(PLACEHOLDER) + 1:]
            if not (PACKAGE.parent / relative).is_file():
                raise ValueError(f"Missing packaged image: {relative}")
            images[0]["image_url"]["url"] = base + "/" + relative
            rendered = json.dumps(request, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
            if ".invalid/" in rendered or len(rendered.encode("utf-8")) > 1_000_000:
                raise ValueError("Unresolved placeholder or request exceeds the conservative 1 MB limit")
            lines.append(rendered + "\n")
        data = "".join(lines).encode("utf-8")
        if not lines or len(lines) > 50_000 or len(data) > 500_000_000:
            raise ValueError("Batch file is empty or exceeds the file/request limit")
        name = path.name.replace(".template.jsonl", ".jsonl")
        prepared[name] = data
        counts[name] = len(lines)
    if not prepared:
        raise ValueError("No Batch templates found")
    output.mkdir(parents=True, exist_ok=True)
    for name, data in prepared.items():
        (output / name).write_bytes(data)
    print(json.dumps({"output_dir": str(output), "requests": counts,
                      "url_reachability_checked": False,
                      "note": "URLs replaced locally. Confirm remote PNG bytes are accessible before submission."},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
