"""Prepare frozen geometry questions and provenance; registration is a root task.

Run from the project directory, e.g.
python -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01 Plane02
After actually inspecting the PNG, use --reviewed to record agent visual review.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import platform
import re
import shutil
import sys

from PIL import Image
import matplotlib
import numpy as np
import PIL

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
IMPORT_ROOT = ROOT / "imports" / "mathverse_vision_dominant"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pixel_digest(data):
    with Image.open(io.BytesIO(data)) as image:
        rgba = image.convert("RGBA")
        return digest(f"{rgba.width}x{rgba.height}:RGBA:".encode() + rgba.tobytes())


@lru_cache(maxsize=4)
def renderer_for(branch):
    if branch not in ("PlaneGeometry", "SolidGeometry"):
        raise ValueError(f"Unknown geometry branch: {branch}")
    path = ROOT / branch / "dataset_generator" / "common_renderer.py"
    spec = importlib.util.spec_from_file_location("_dataset_" + branch, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def draw_question(branch, scene_path, output_path=None):
    renderer = renderer_for(branch)
    scene_path = Path(scene_path)
    scene = renderer.read_json(scene_path)
    target = output_path or ROOT / branch / "reproduced" / f"{scene['id']}.png"
    return renderer.draw(scene_path, target)


def wrapper_text(branch, scene):
    qid = scene["id"]
    return '\n'.join([
        f'"""Frozen MathVerse question {qid}; source key {scene["provenance"]["source_key"]}."""',
        'from pathlib import Path', 'import sys',
        '_PROJECT_ROOT = Path(__file__).resolve().parents[2]',
        'if str(_PROJECT_ROOT) not in sys.path:', '    sys.path.insert(0, str(_PROJECT_ROOT))',
        'from dataset_tools.geometry_dataset import draw_question, read_json', '',
        f'class {qid}:', '    def __init__(self):',
        f'        self.id = {qid!r}', "        self.source_dataset = 'MathVerse'",
        f'        self.query = {scene["query"]!r}', f'        self.answer = {scene["answer"]!r}',
        f'        self.answer_type = {scene["answer_type"]!r}', f'        self.subject = {branch!r}',
        f'        self.level = {scene["level"]!r}',
        f'        self.scene_path = Path(__file__).with_name("scenes") / "{qid}.json"',
        '', '    def get_scene(self):', '        return read_json(self.scene_path)',
        '', '    def draw(self, output_path=None):',
        f'        return draw_question({branch!r}, self.scene_path, output_path)', '',
        'if __name__ == "__main__":', f'    result = {qid}().draw()',
        '    print(result["image_path"])', ''])


def prepare(branch, qids, reviewed=False):
    renderer = renderer_for(branch)
    assignments = {r["id"]: r for r in read_json(IMPORT_ROOT / "assignments.json") if r["branch"] == branch}
    source_records = {r["source_key"]: r for r in read_json(IMPORT_ROOT / "source_manifest.json")}
    branch_root = ROOT / branch
    results = []
    for qid in qids:
        if qid not in assignments:
            raise ValueError(f"Question is not assigned to this branch: {qid}")
        assignment = assignments[qid]
        source = source_records[assignment["source_key"]]
        scene_path = branch_root / "dataset_generator" / "scenes" / f"{qid}.json"
        scene = renderer.read_json(scene_path)
        if scene["id"] != qid or scene.get("source_dataset") != "MathVerse":
            raise ValueError(f"Wrong scene identity/source: {qid}")
        for field in ("query", "answer", "answer_type", "level", "answer_verification"):
            if field not in scene:
                raise ValueError(f"Missing question metadata {field}: {qid}")
        if scene["query"] != source["question"] or scene["answer"] != source["source_answer"]:
            raise ValueError(f"Preserve source question and GT verbatim; keep verification candidates separately: {qid}")
        if not scene["answer_verification"].get("reasoning"):
            raise ValueError(f"Mathematical verification is missing: {qid}")
        if scene.get("provenance", {}).get("source_key") != source["source_key"]:
            raise ValueError(f"Scene-to-source assignment mismatch: {qid}")
        source_copy = (scene_path.parent / scene["source_image"]).resolve()
        if not source_copy.is_relative_to(branch_root / "originals"):
            raise ValueError(f"Source copy must live in this branch's originals/: {qid}")
        source_bytes = (IMPORT_ROOT / source["source_image"]).read_bytes()
        if digest(source_bytes) != source["source_image_sha256"]:
            raise ValueError(f"Extracted source fingerprint changed: {qid}")
        source_copy.parent.mkdir(parents=True, exist_ok=True)
        if source_copy.exists() and source_copy.read_bytes() != source_bytes:
            raise ValueError(f"Existing source copy differs: {qid}")
        source_copy.write_bytes(source_bytes)
        prefix = "plane" if branch == "PlaneGeometry" else "solid"
        number = re.search(r"\d+$", qid).group()
        script_path = branch_root / "dataset_generator" / f"{prefix}_plot{number}.py"
        script_path.write_text(wrapper_text(branch, scene), encoding="utf-8")
        png, checks = renderer.image_bytes(scene)
        repeated_png, _ = renderer.image_bytes(scene)
        svg, _ = renderer.image_bytes(scene, vector=True)
        repeated_svg, _ = renderer.image_bytes(scene, vector=True)
        if pixel_digest(png) != pixel_digest(repeated_png) or svg != repeated_svg:
            raise ValueError(f"Frozen rendering is not deterministic: {qid}")
        png_path, svg_path = [branch_root / "image" / f"{qid}.{ext}" for ext in ("png", "svg")]
        png_path.parent.mkdir(parents=True, exist_ok=True)
        png_path.write_bytes(png)
        svg_path.write_bytes(svg)
        input_paths = {"source_image": source_copy, "scene": scene_path, "protocol": renderer.PROTOCOL_PATH,
                       "renderer": Path(renderer.__file__), "question_script": script_path,
                       "preparation_entrypoint": Path(__file__), "written_protocol": branch_root / "REDRAW_PROTOCOL.md"}
        inputs = {key: {"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path.read_bytes())}
                  for key, path in input_paths.items()}
        if "target_long_side_fraction" in renderer.read_json(renderer.PROTOCOL_PATH)["view"]:
            layout_path = ROOT / "dataset_tools" / "geometry_layout.py"
            inputs["layout_helper"] = {"path": layout_path.relative_to(ROOT).as_posix(),
                                       "sha256": digest(layout_path.read_bytes())}
        output_hash = digest(png)
        report_path = branch_root / "dataset_generator" / "reports" / f"{qid}_redraw_report.json"
        visual = {"status": "pending", "reviewer": None, "user_pass": False}
        if report_path.exists():
            old = read_json(report_path)
            if old.get("inputs") == inputs and old.get("output_png_sha256") == output_hash:
                visual = old.get("visual_review", visual)
        if reviewed:
            visual = {"status": "inspected", "reviewer": "agent", "user_pass": False,
                      "reviewed_at_utc": datetime.now(timezone.utc).isoformat(), "image_sha256": output_hash,
                      "scope": "Source/redraw labels, connectivity, dimensions, visibility and overall layout."}
        report = {"id": qid, "status": scene["status"], "source_dataset": "MathVerse",
                  "source_provenance": {k: source[k] for k in source if k != "previous_model_response"},
                  "question": scene["query"], "answer": scene["answer"], "answer_type": scene["answer_type"],
                  "answer_verification": scene["answer_verification"], "inputs": inputs,
                  "output_png": png_path.relative_to(ROOT).as_posix(), "output_png_sha256": output_hash,
                  "output_svg": svg_path.relative_to(ROOT).as_posix(), "output_svg_sha256": digest(svg),
                  "rgba_pixel_sha256": pixel_digest(png), "determinism_verified": True,
                  "all_constraints_passed": all(c["passed"] for c in checks), "checks": checks,
                  "protocol_version": scene["protocol_version"], "visual_review": visual,
                  "dependencies": {"python": platform.python_version(), "matplotlib": matplotlib.__version__,
                                   "numpy": np.__version__, "Pillow": PIL.__version__}}
        if "layout_helper" in inputs:
            from dataset_tools.geometry_layout import layout_metrics
            report["layout"] = layout_metrics(Image.open(io.BytesIO(png)))
        write_json(report_path, report)
        status = "verified" if scene["answer_verification"]["status"] == "verified" else "needs_review"
        result = {"source_key": source["source_key"], "id": qid, "branch": branch, "source_dataset": "MathVerse",
                  "question": scene["query"], "answer": scene["answer"], "source_answer": source["source_answer"],
                  "image": png_path.relative_to(ROOT).as_posix(), "scene": scene_path.relative_to(ROOT).as_posix(),
                  "script": script_path.relative_to(ROOT).as_posix(), "report": report_path.relative_to(ROOT).as_posix(),
                  "status": status, "answer_verification": scene["answer_verification"], "visual_review": visual}
        write_json(IMPORT_ROOT / "results" / ("plane" if branch == "PlaneGeometry" else "solid") / f"{source['source_key']}.json", result)
        results.append(result)
        print(f"{qid} ({source['source_key']}): rendered PNG/SVG, {len(checks)} checks, {status}, visual={visual['status']}", flush=True)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("branch", choices=["PlaneGeometry", "SolidGeometry"])
    parser.add_argument("questions", nargs="+")
    parser.add_argument("--reviewed", action="store_true", help="Record an agent review ONLY after actually viewing these PNGs.")
    args = parser.parse_args()
    prepare(args.branch, args.questions, args.reviewed)
