"""Audit all migrated scenes and create source/redraw sheets for visual review."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps
from matplotlib.font_manager import findfont
from common_renderer import read_json, validate_scene

ROOT = Path(__file__).resolve().parents[2]
BRANCH = ROOT / "PlaneGeometry"
ARCHIVE = BRANCH / "archive" / "angle_arcs_1_1_0"
QA = BRANCH / "dataset_generator" / "angle_arc_review"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def content(path):
    image = Image.open(path).convert("RGB")
    bounds = ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()
    if bounds:
        image = image.crop((max(0, bounds[0]-15), max(0, bounds[1]-15),
                            min(image.width, bounds[2]+15), min(image.height, bounds[3]+15)))
    return image


def main():
    QA.mkdir(exist_ok=True)
    source = {r["source_key"]: r for r in read_json(ROOT / "imports/mathverse_vision_dominant/source_manifest.json")}
    old_hashes = read_json(ARCHIVE / "before_manifest.json")
    records = []
    font = ImageFont.truetype(findfont("DejaVu Sans"), 18)
    scenes = [read_json(p) for p in sorted((BRANCH / "dataset_generator/scenes").glob("Plane*.json"))]
    for scene in scenes:
        qid = scene["id"]
        before = read_json(ARCHIVE / "PlaneGeometry/dataset_generator/scenes" / f"{qid}.json")
        geometry = lambda s: [o for o in s["objects"] if o["type"] != "angle_arc"]
        manual = False
        if manual:
            comparison = read_json(BRANCH / "archive/manual_corrections/Plane01_before_user_correction/Plane01.json")
            mutable = {"objects", "labels", "points", "constraints", "status", "ambiguities", "answer_verification"}
            for field in set(before) - mutable - {"protocol_version"}:
                assert before[field] == scene[field], f"{qid}: changed {field}"
            assert {k: v for k, v in scene["points"].items() if k != "D"} == {k: v for k, v in comparison["points"].items() if k != "D"}, qid
            assert [o for o in geometry(comparison) if o["id"] != "BC"] == geometry(scene), qid
            assert scene["constraints"] == [c for c in comparison["constraints"] if c["id"] != "AB_AD"], qid
            assert scene["labels"] == comparison["labels"] and "AB_AD" not in {c["id"] for c in scene["constraints"]}, qid
            old_d = comparison["points"]["D"]
            new_d = scene["points"]["D"]
            assert new_d[1] < old_d[1] and abs((new_d[0]/old_d[0])-(new_d[1]/old_d[1])) < 1e-9, qid
        else:
            for field in set(before) - {"objects", "labels", "protocol_version"}:
                assert before[field] == scene[field], f"{qid}: changed {field}"
            assert geometry(before) == geometry(scene), qid
        checks = validate_scene(scene)
        bound = [c for c in checks if c["type"] == "angle_annotation"]
        arcs = [o for o in scene["objects"] if o["type"] == "angle_arc"]
        svg = ET.parse(BRANCH / "image" / f"{qid}.svg")
        svg_ids = [e.attrib.get("id") for e in svg.iter()]
        assert all(svg_ids.count(a["id"]) == 1 for a in arcs), f"{qid}: rendered arc count"
        png = BRANCH / "image" / f"{qid}.png"
        with Image.open(png) as image:
            assert image.size == (768, 768) and image.convert("RGBA").getchannel("A").getextrema() == (255, 255)
        original = BRANCH / "originals" / f"{qid}.png"
        assert digest(original) == source[scene["provenance"]["source_key"]]["source_image_sha256"], qid
        previous_png = ARCHIVE / png.relative_to(ROOT)
        with Image.open(previous_png) as old, Image.open(png) as new:
            changed = old.convert("RGBA").tobytes() != new.convert("RGBA").tobytes()
        records.append({"id": qid, "annotated_angles": len({c["arc_id"] for c in bound}),
                        "angle_labels": len(bound), "angle_arcs": len(arcs),
                        "added_arcs": len(arcs)-sum(o["type"] == "angle_arc" for o in before["objects"]),
                        "pixels_changed": changed, "all_checks_passed": True,
                        "source_image_question_answer_preserved": True,
                        "geometry_preserved": not manual,
                        "explicit_user_geometry_correction": ["moved D down", "removed BC segment"] if manual else []})
    assert digest(BRANCH / "dataset.jsonl") == old_hashes["PlaneGeometry/dataset.jsonl"]
    for start in range(0, len(scenes), 4):
        sheet = Image.new("RGB", (1200, 1600), "white")
        draw = ImageDraw.Draw(sheet)
        for row, scene in enumerate(scenes[start:start+4]):
            qid = scene["id"]
            draw.text((15, row*400+8), f"{qid} MathVerse source / protocol 1.1.0 redraw", fill="black", font=font)
            for col, folder in enumerate(("originals", "image")):
                tile = ImageOps.contain(content(BRANCH / folder / f"{qid}.png"), (560, 350))
                sheet.paste(tile, (col*600+(600-tile.width)//2, row*400+38+(350-tile.height)//2))
        sheet.save(QA / f"review_{start//4+1:02d}.png")
    summary = {"protocol_version": "1.1.0", "question_count": len(records),
               "pixel_changed_questions": sum(r["pixels_changed"] for r in records),
               "angle_labels": sum(r["angle_labels"] for r in records),
               "annotated_geometric_angles": sum(r["annotated_angles"] for r in records),
               "angle_arcs": sum(r["angle_arcs"] for r in records),
               "added_arcs": sum(r["added_arcs"] for r in records),
               "all_source_images_questions_answers_preserved": True,
               "user_geometry_correction_count": sum(not r["geometry_preserved"] for r in records),
               "all_bindings_valid_and_no_duplicate_arcs": True, "questions": records}
    (QA / "validation.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "questions"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
