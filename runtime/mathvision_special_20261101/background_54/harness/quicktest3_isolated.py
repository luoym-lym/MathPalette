"""User-authorized isolated Quick Test 3. No library/workbench writes or approvals.

Run with python -B. Each invocation preserves immutable request bytes and both
independent responses in a fresh evidence directory below the root runtime/.
"""
from __future__ import annotations

import argparse
import base64
import copy
import hashlib
from http.client import IncompleteRead
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import env54
PROJECT = env54.PROJECT
RUNTIME = (PROJECT / "runtime").resolve()
HARNESS = Path(__file__).resolve().parent
for variable, directory in {"MPLCONFIGDIR": "mpl_cache", "XDG_CACHE_HOME": "cache",
                            "TEMP": "tmp", "TMP": "tmp"}.items():
    target = HARNESS / directory
    target.mkdir(parents=True, exist_ok=True)
    os.environ[variable] = str(target)


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def runtime_path(path, *, exists=False):
    target = Path(path).resolve()
    if not target.is_relative_to(RUNTIME) or target == RUNTIME:
        raise ValueError("All inputs/outputs produced by this task must be below root runtime/.")
    if exists and not target.is_file():
        raise ValueError("Runtime input file is missing: " + str(target))
    return target


def write_new_json(path, value):
    path = runtime_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def reference_module(branch):
    directory = PROJECT / branch / "workbench"
    sys.path.insert(0, str(directory))
    spec = importlib.util.spec_from_file_location("_isolated_reference_quick_test", directory / "quick_test.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_key(branch="PlaneGeometry"):
    module = reference_module(branch)
    key = module.load_api_key(PROJECT, "MIMO_API_KEY")
    return {"configured": bool(key), "token_plan_format": key.startswith(("tp-", "ttp-")),
            "profile": "quicktest3", "model": module.TEST_PROFILES["quicktest3"]["model"],
            "thinking": module.TEST_PROFILES["quicktest3"]["thinking"]}


def run_tests(branch, question_id, image_path, design_path, output_dir, runs=2):
    if branch not in {"PlaneGeometry", "SolidGeometry"}:
        raise ValueError("Unsupported branch.")
    if runs not in (1, 2):
        raise ValueError("This task permits one or two independent calls per invocation.")
    image_path = runtime_path(image_path, exists=True)
    design_path = runtime_path(design_path, exists=True)
    output_dir = runtime_path(output_dir)
    module = reference_module(branch)
    dataset_path = PROJECT / branch / "dataset.jsonl"
    dataset_bytes = dataset_path.read_bytes()
    record = next((json.loads(line) for line in dataset_bytes.decode("utf-8-sig").splitlines()
                   if line.strip() and json.loads(line).get("id") == question_id), None)
    if not record or record.get("source_dataset") != "MathVision":
        raise ValueError("Question is not a formal MathVision record.")
    design_bytes = design_path.read_bytes()
    design = json.loads(design_bytes.decode("utf-8-sig"))
    if design.get("question_id", question_id) != question_id:
        raise ValueError("Design question_id differs.")
    expected = design.get("expected_wrong_answer", design.get("predicted_wrong_answer"))
    if expected is None or expected == "":
        raise ValueError("Write expected_wrong_answer in the design JSON before testing.")
    if str(expected).strip() == str(record["answer"]).strip():
        raise ValueError("Expected wrong answer equals the formal correct answer.")
    image_bytes = image_path.read_bytes()
    if image_bytes[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Candidate must be a PNG image.")
    from PIL import Image
    with Image.open(io.BytesIO(image_bytes)) as image:
        image.load()
        if image.size != (768, 768):
            raise ValueError("Candidate must retain the standard 768 x 768 canvas.")
        rgba = image.convert("RGBA")
        if rgba.getextrema()[3] != (255, 255):
            raise ValueError("Candidate must retain opaque background.")
        pixel_hash = sha256(b"768x768:RGBA:" + rgba.tobytes())
    settings = copy.deepcopy(module.TEST_PROFILES["quicktest3"])
    config = json.loads((PROJECT / branch / "workbench/config.json").read_text(encoding="utf-8-sig"))
    api_base = config.get("quick_test", {}).get("mimo_api_base", module.MIMO_API_BASE)
    if api_base not in module.PROVIDERS["mimo"]["api_bases"]:
        raise ValueError("MiMo Token Plan endpoint is not the official configured endpoint.")
    key = module.load_api_key(PROJECT, "MIMO_API_KEY")
    if not key:
        raise ValueError("MIMO_API_KEY is not configured.")
    settings["api_base"] = api_base
    payload = {"model": settings["model"], "stream": False,
               "thinking": copy.deepcopy(settings["thinking"]),
               "messages": [{"role": "system", "content": module.SYSTEM_PROMPT},
                            {"role": "user", "content": [
                                {"type": "text", "text": record["question"]},
                                {"type": "image_url", "image_url": {
                                    "url": "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")}}]}]}
    request_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    invocation = output_dir / ("quicktest3_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
                               + "_" + uuid.uuid4().hex[:12])
    invocation.mkdir(parents=True, exist_ok=False)
    frozen = {"branch": branch, "question_id": question_id, "profile": "quicktest3",
              "settings": settings, "system_prompt": module.SYSTEM_PROMPT,
              "question": record["question"], "image_path": str(image_path),
              "image_sha256": sha256(image_bytes), "pixel_sha256": pixel_hash,
              "design_path": str(design_path), "design_sha256": sha256(design_bytes),
              "expected_wrong_answer": expected,
              "question_record_sha256": sha256(json.dumps(record, ensure_ascii=False, sort_keys=True,
                                                           separators=(",", ":")).encode("utf-8")),
              "dataset_sha256": sha256(dataset_bytes), "request_body_sha256": sha256(request_bytes),
              "reference_quick_test_sha256": sha256(Path(module.__file__).read_bytes()),
              "created_at": timestamp(), "requested_runs": runs,
              "authorization": "User explicitly requested automatic exploration and two quicktest3 calls.",
              "approval_status": "UNREVIEWED; no Pass or Collect action performed"}
    write_new_json(invocation / "binding.json", frozen)
    # Exact request body has no credential and binds bytes sent to the model.
    (invocation / "request.json").write_bytes(request_bytes)
    (invocation / "design_snapshot.json").write_bytes(design_bytes)
    results = []
    for run_index in range(1, runs + 1):
        if image_path.read_bytes() != image_bytes or design_path.read_bytes() != design_bytes:
            raise ValueError("Candidate/design changed between independent calls; stop.")
        job = {"run_index": run_index, "run_id": uuid.uuid4().hex,
               "started_at": timestamp(), "request_body_sha256": sha256(request_bytes),
               "image_sha256": frozen["image_sha256"], "design_sha256": frozen["design_sha256"]}
        write_new_json(invocation / f"run_{run_index:02d}_started.json", job)
        began = time.monotonic()
        request = Request(api_base + "/chat/completions", data=request_bytes,
                          headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        try:
            with build_opener(module.NoRedirect()).open(request, timeout=None) as response:
                raw = response.read(module.MAX_RESPONSE_BYTES + 1)
                job["http_status"] = response.status
            if len(raw) > module.MAX_RESPONSE_BYTES:
                raise ValueError("Response exceeded the reference workbench response limit.")
            response_data = json.loads(raw)
            # The provider response is preserved verbatim; credentials never enter it.
            (invocation / f"run_{run_index:02d}_response.json").write_bytes(raw)
            job.update(module.parse_response(response_data, module.PROVIDERS["mimo"]["label"]), status="completed")
            job["response_sha256"] = sha256(raw)
        except IncompleteRead as error:
            partial = error.partial[:module.MAX_RESPONSE_BYTES]
            (invocation / f"run_{run_index:02d}_incomplete_response.bin").write_bytes(partial)
            job.update(status="error", error_code="incomplete_http_response",
                       error=module.safe_error(str(error), key),
                       partial_response_sha256=sha256(partial))
        except HTTPError as error:
            body = error.read(16384).decode("utf-8", errors="replace")
            job.update(status="error", http_status=error.code,
                       error=module.safe_error(body, key))
        except (OSError, URLError, ValueError, module.WorkbenchError) as error:
            job.update(status="error", error=module.safe_error(str(error), key))
        job.update(finished_at=timestamp(), elapsed_seconds=round(time.monotonic() - began, 3))
        write_new_json(invocation / f"run_{run_index:02d}.json", job)
        results.append(job)
        print(json.dumps({"question_id": question_id, "run": run_index, "status": job["status"],
                          "elapsed_seconds": job["elapsed_seconds"],
                          "evidence_dir": str(invocation), "error": job.get("error")},
                         ensure_ascii=False), flush=True)
        if job["status"] != "completed":
            break  # API errors are never automatically retried.
    summary = {**frozen, "evidence_dir": str(invocation), "results": results,
               "two_completed": len(results) == 2 and all(r["status"] == "completed" for r in results),
               "note": "Human/agent review must compare each final answer with the predeclared wrong answer; no approval recorded."}
    write_new_json(invocation / "summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", choices=("PlaneGeometry", "SolidGeometry"), default="PlaneGeometry")
    parser.add_argument("--question")
    parser.add_argument("--image")
    parser.add_argument("--design")
    parser.add_argument("--output")
    parser.add_argument("--runs", choices=(1, 2), type=int, default=2)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        print(json.dumps(check_key(args.branch), ensure_ascii=False))
        return
    if not all((args.question, args.image, args.design, args.output)):
        parser.error("--question, --image, --design, --output are required unless --check.")
    result = run_tests(args.branch, args.question, args.image, args.design, args.output, args.runs)
    print(json.dumps({"evidence_dir": result["evidence_dir"], "two_completed": result["two_completed"]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
