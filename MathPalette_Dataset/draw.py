"""Draw, rebuild, or verify the collected MathPalette dataset."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import importlib
import json
import multiprocessing
from pathlib import Path
import platform
import re
import shutil
import sys
import tempfile

DATASET = Path(__file__).resolve().parent
if str(DATASET.parent) not in sys.path:
    sys.path.insert(0, str(DATASET.parent))


def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_rows(path, rows):
    Path(path).write_text("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n" for r in rows), encoding="utf-8")


def load_question(qid):
    if not re.fullmatch(r"(?:Ana|Plane|Solid)\d+", qid):
        raise ValueError("Invalid question ID")
    if qid not in {r["id"] for r in read_rows(DATASET / "dataset.jsonl")}:
        raise ValueError("Unknown collected question: " + qid)
    module = importlib.import_module("MathPalette_Dataset.questions." + qid)
    return getattr(module, qid)()


def _render(item):
    row, directory = item
    from PIL import Image
    question = load_question(row["id"])
    for key in ("id", "question", "answer", "answer_type", "source_dataset", "source_key", "choices"):
        if getattr(question, key, None) != row.get(key):
            raise ValueError(row["id"] + ": class metadata differs: " + key)
    slots = [v["slot_id"] for v in row["special_variants"]]
    if list(question.variants) != slots:
        raise ValueError("Class Special slots differ: " + row["id"])
    outputs = []
    for variant in [None, *slots]:
        sid = row["id"] + "_" + (variant or "original")
        path = Path(directory) / (sid + ".png")
        question.draw(path, variant=variant)
        with Image.open(path) as image:
            rgba = image.convert("RGBA")
            if image.size != (768, 768) or rgba.getextrema()[3] != (255, 255):
                raise ValueError("Expected opaque 768x768 PNG: " + sid)
            pixel_hash = hashlib.sha256(b"768x768:RGBA:" + rgba.tobytes()).hexdigest()
        outputs.append({"id": sid, "variant": variant, "path": str(path),
                        "sha256": file_hash(path), "pixel_sha256": pixel_hash})
    return outputs


def render_all(rows, directory, jobs):
    context = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers=jobs, mp_context=context) as pool:
        for result in pool.map(_render, ((row, str(directory)) for row in rows)):
            yield from result


def write_checksums():
    paths = sorted(p for p in DATASET.rglob("*") if p.is_file() and p.name != "SHA256SUMS"
                   and "__pycache__" not in p.parts and p.name != ".DS_Store")
    (DATASET / "SHA256SUMS").write_text("".join(
        file_hash(p) + "  " + p.relative_to(DATASET).as_posix() + "\n" for p in paths), encoding="utf-8")


def check(jobs=4, redraw=False):
    from MathPalette_Dataset.infer_deepseek import load_dataset
    samples, metadata = load_dataset(DATASET)
    listed = set()
    for line in (DATASET / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        path = (DATASET / relative).resolve()
        if not path.is_relative_to(DATASET) or file_hash(path) != digest:
            raise ValueError("Checksum mismatch: " + relative)
        listed.add(relative)
    actual = {p.relative_to(DATASET).as_posix() for p in DATASET.rglob("*") if p.is_file()
              and p.name != "SHA256SUMS" and "__pycache__" not in p.parts and p.name != ".DS_Store"}
    if actual != listed:
        raise ValueError("Checksum manifest and dataset file set differ")
    image_rows = read_rows(DATASET / "image_manifest.jsonl")
    by_image = defaultdict(list)
    for sample in samples:
        by_image[sample["image"]].append(sample["id"])
    if any(sorted(row["sample_ids"]) != sorted(by_image[row["image"]]) for row in image_rows):
        raise ValueError("Image and sample manifest identities differ")
    if {p.name for p in (DATASET / "images").glob("*.png")} != {Path(r["image"]).name for r in image_rows}:
        raise ValueError("Unused or missing PNG files")
    rows = read_rows(DATASET / "dataset.jsonl")
    if {p.stem for p in (DATASET / "questions").glob("*.py") if p.name != "__init__.py"} != {r["id"] for r in rows}:
        raise ValueError("Unused or missing question classes")
    if redraw:
        expected = {s["id"]: s["image_sha256"] for s in samples}
        with tempfile.TemporaryDirectory(prefix="mathpalette-redraw-") as temporary:
            generated = list(render_all(rows, temporary, jobs))
            if len(generated) != len(samples) or any(r["sha256"] != expected[r["id"]] for r in generated):
                raise ValueError("Class redraw differs from frozen PNGs; use the pinned drawing environment")
    return {"questions": len(rows), "samples": len(samples),
            "specials": sum(len(r["special_variants"]) for r in rows),
            "unique_pngs": len(image_rows), "redraw_verified": redraw}


def rebuild(jobs=4):
    """Regenerate formal images and manifests from the retained question classes."""
    rows = read_rows(DATASET / "dataset.jsonl")
    for row in rows:
        c = row["collection"]
        slots = [s["slot_id"] for s in row["special_variants"]]
        if (c.get("status") != "collected" or c.get("special_case") is not False
                or c.get("review_status") in ("pending", "pending_review")
                or c.get("slots") != slots or c.get("accepted_count") != len(slots)):
            raise ValueError("Not a complete normal Collect: " + row["id"])
    with tempfile.TemporaryDirectory(prefix="mathpalette-build-") as temporary:
        outputs = {r["id"]: r for r in render_all(rows, temporary, jobs)}
        images = DATASET / "images"
        images.mkdir(exist_ok=True)
        manifest = {}
        samples = []
        for row in rows:
            sid = row["id"] + "_original"
            for target, sample_id, variant in [(row, sid, None), *(
                    (s, s["id"], s["slot_id"]) for s in row["special_variants"])]:
                rendered = outputs[sample_id]
                relative = "images/" + rendered["sha256"] + ".png"
                destination = DATASET / relative
                if not destination.exists() or file_hash(destination) != rendered["sha256"]:
                    shutil.copyfile(rendered["path"], destination)
                target.update(image=relative, image_sha256=rendered["sha256"])
                manifest.setdefault(relative, {"image": relative, "sha256": rendered["sha256"],
                    "pixel_sha256": rendered["pixel_sha256"], "bytes": destination.stat().st_size,
                    "width": 768, "height": 768, "sample_ids": []})["sample_ids"].append(sample_id)
                sample = {k: row[k] for k in ("branch", "source_dataset", "source_key", "question", "answer", "answer_type", "choices") if k in row}
                sample.update(id=sample_id, question_id=row["id"], variant_type="original" if variant is None else "special",
                              variant_id=variant, image=relative, image_sha256=rendered["sha256"])
                samples.append(sample)
        for path in images.glob("*.png"):
            if "images/" + path.name not in manifest:
                path.unlink()
        write_rows(DATASET / "dataset.jsonl", rows)
        write_rows(DATASET / "samples.jsonl", samples)
        write_rows(DATASET / "image_manifest.jsonl", [manifest[k] for k in sorted(manifest)])
    import matplotlib
    import numpy
    import PIL
    from MathPalette_Dataset.drawing import PROTOCOL_VERSION
    metadata = {"schema_version": "2.0.0", "name": "MathPalette collected dataset",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "selection": "collected, special_case=false, not pending review; exactly the passed Collect slots",
        "image_authority": "PNG generated by the retained Python question classes and shared drawing protocol",
        "drawing_protocol_version": PROTOCOL_VERSION,
        "counts": {"questions": len(rows), "original_images": len(rows), "special_images": len(samples)-len(rows),
                   "samples": len(samples), "unique_image_files": len(manifest),
                   "image_bytes": sum(r["bytes"] for r in manifest.values())},
        "branches": {b: {"questions": sum(r["branch"] == b for r in rows),
                         "samples": sum(s["branch"] == b for s in samples)} for b in sorted({r["branch"] for r in rows})},
        "sources": dict(Counter(r["source_dataset"] for r in rows)),
        "rendering_environment": {"python": platform.python_version(), "numpy": numpy.__version__,
            "matplotlib": matplotlib.__version__, "pillow": PIL.__version__, "freetype": matplotlib.ft2font.__freetype_version__},
        "artifact_sha256": {name: file_hash(DATASET / name) for name in (
            "dataset.jsonl", "samples.jsonl", "image_manifest.jsonl", "drawing.py", "draw.py",
            *[r["script"] for r in rows])}}
    (DATASET / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_checksums()
    return metadata["counts"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    draw = sub.add_parser("draw", help="Draw a collected question or its Special")
    draw.add_argument("question_id"); draw.add_argument("--variant"); draw.add_argument("--output", type=Path)
    for command in ("check", "rebuild"):
        p = sub.add_parser(command)
        p.add_argument("--jobs", type=int, default=4)
        if command == "check": p.add_argument("--redraw", action="store_true")
    args = parser.parse_args()
    if args.command == "draw":
        result = load_question(args.question_id).draw(args.output, variant=args.variant)
    elif not 1 <= args.jobs <= 16:
        parser.error("--jobs must be between 1 and 16")
    elif args.command == "check": result = check(args.jobs, args.redraw)
    else: result = rebuild(args.jobs)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
