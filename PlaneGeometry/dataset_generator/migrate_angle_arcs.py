"""Migrate existing plane scenes to one arc per annotated geometric angle.

Source questions, answers, coordinates, constraints and answer QA stay frozen.
Run from MathPalette; visual review is recorded separately after inspection.
"""
from __future__ import annotations

import hashlib
import math
from pathlib import Path
import sys

from common_renderer import read_json, same_angle, validate_scene, render_scene, angle_geometry, PROTOCOL_PATH
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from dataset_tools.geometry_dataset import prepare, write_json

SCENES = Path(__file__).with_name("scenes")
ARCHIVE = ROOT / "PlaneGeometry" / "archive" / "angle_arcs_1_1_0"

# These are angle symbols/numbers, rather than similarly named side lengths.
SYMBOLS = {
    "Plane18": {"num1": (["C", "X", "B"], 27), "num2": (["A", "X", "B"], 27)},
    "Plane22": {"adeg": (["Q", "R", "P"], 32)},
    "Plane30": {"theta": (["V", "A", "C"], 29)},
    "Plane35": {"unknown_b": (["T", "S", "C"], 54), "unknown_a": (["N2", "C", "S"], 44)},
}
CALLOUTS = {
    "Plane20": {"given134": ["C", "O", "D"]},
    "Plane40": {"xmark": ["O", "A", "B"], "zmark": ["O", "B", "A"],
                "given80": ["O", "A", "B"]},
}


def refine_angle_labels(scene):
    """Freeze clear label positions once; redraw itself never searches layouts."""
    fig, _ = render_scene(scene)
    moved = []
    try:
        ax = fig.axes[0]
        renderer = fig.canvas.get_renderer()
        artists = {a.get_gid(): a for a in ax.texts}
        paths = [a.get_path().transformed(a.get_transform()) for a in [*ax.lines, *ax.patches]]
        for label in scene["labels"]:
            if label["type"] != "angle" or label["id"] == "start14":
                continue  # 14 is an explicit external annotation in the source.
            artist = artists[label["id"]]
            def clear():
                box = artist.get_window_extent(renderer).padded(2)
                if not (fig.bbox.contains(box.x0, box.y0) and fig.bbox.contains(box.x1, box.y1)):
                    return False
                if any(path.intersects_bbox(box, filled=False) for path in paths):
                    return False
                return not any(box.overlaps(other.get_window_extent(renderer).padded(2))
                               for key, other in artists.items() if key != label["id"])
            if clear():
                continue
            _, bisector, _, start, end = angle_geometry(scene, label["points"], label.get("reflex", False))
            base = label.get("radius_pt", 27)
            original = artist.get_position()
            found = False
            for radius in np.arange(max(base, 30), 126, 6):
                for fraction in (0.5, 0.35, 0.65, 0.2, 0.8):
                    direction = np.array([math.cos(math.radians(start+(end-start)*fraction)),
                                          math.sin(math.radians(start+(end-start)*fraction))])
                    offset = radius * direction
                    artist.set_position(offset.tolist())
                    if clear():
                        label["radius_pt"] = float(radius)
                        label["offset_pt"] = (offset - radius * bisector).tolist()
                        moved.append(label["id"])
                        found = True
                        break
                if found:
                    break
            if not found:
                artist.set_position(original)
                raise ValueError(f"No clear angle-label placement: {scene['id']}/{label['id']}")
        return moved
    finally:
        plt.close(fig)


def audit_record(scene, before, path):
    arcs = [item for item in scene["objects"] if item["type"] == "angle_arc"]
    old_ids = {item["id"] for item in before["objects"]}
    return {"id": scene["id"], "added_arc_ids": [a["id"] for a in arcs if a["id"] not in old_ids],
            "bindings": [{"label_id": l["id"], "arc_id": l["arc_id"]}
                         for l in scene["labels"] if "arc_id" in l],
            "angle_arc_count": len(arcs), "geometry_question_answer_unchanged": True,
            "scene_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def migrate():
    protocol = read_json(PROTOCOL_PATH)
    audit = []
    for path in sorted(SCENES.glob("Plane*.json")):
        scene = read_json(path)
        before = read_json(ARCHIVE / path.relative_to(ROOT))
        if scene["protocol_version"] == "1.1.0":
            validate_scene(scene, protocol)
            moved = refine_angle_labels(scene)
            write_json(path, scene)
            print(f"{scene['id']}: adjusted angle labels {moved}")
            assert all(scene[key] == before[key] for key in set(before) - {"protocol_version", "objects", "labels"})
            assert [o for o in scene["objects"] if o["type"] != "angle_arc"] == [o for o in before["objects"] if o["type"] != "angle_arc"]
            audit.append(audit_record(scene, before, path))
            continue
        if scene["protocol_version"] != "1.0.0":
            raise ValueError(f"Unexpected starting version: {path}")
        qid = scene["id"]
        scene["protocol_version"] = "1.1.0"
        for label in scene["labels"]:
            symbolic = SYMBOLS.get(qid, {}).get(label["id"])
            if symbolic:
                names, radius = symbolic
                label_id, text = label["id"], label["text"]
                label.clear()
                label.update(id=label_id,
                             type="angle", points=names, text=text, radius_pt=radius)
            callout = CALLOUTS.get(qid, {}).get(label["id"])
            if callout:
                label["angle_points"] = callout
            if qid == "Plane05" and label["id"] == "given_AOC":
                label.clear()
                label.update(id="given_AOC", type="angle", points=["A", "O", "C"],
                             degrees=70, radius_pt=52, offset_pt=[-8, -12])
            if qid == "Plane18" and label["id"] in ("arcBC30", "arcAD20"):
                label.update(role="arc_measure", center="O",
                             arc_points=["B", "C"] if label["id"] == "arcBC30" else ["A", "D"])
                label["text"] += "\N{DEGREE SIGN}"
        arcs = [item for item in scene["objects"] if item["type"] == "angle_arc"]
        for label in scene["labels"]:
            if label["type"] != "angle" and "angle_points" not in label:
                continue
            matches = [arc for arc in arcs if same_angle(scene, label, arc, protocol)]
            if len(matches) > 1:
                raise ValueError(f"Existing duplicate angle arcs: {qid}/{label['id']}")
            if not matches:
                names = label["points"] if label["type"] == "angle" else label["angle_points"]
                arc = {"id": "angle_arc_" + label["id"], "type": "angle_arc",
                       "points": names, "radius_pt": 16}
                if label.get("reflex"):
                    arc["reflex"] = True
                scene["objects"].append(arc)
                arcs.append(arc)
            else:
                arc = matches[0]
            label["arc_id"] = arc["id"]
            # Keep the source's large enclosing/bisecting arcs and nested layout.
            if qid == "Plane03":
                arc["radius_pt"] = 12 if label["id"] == "given_AOD" else 24
                label["radius_pt"] = 28 if label["id"] == "given_AOD" else 40
            elif qid == "Plane27":
                arc["radius_pt"] = 16 if label["id"] == "angle37" else 33
            elif qid == "Plane35":
                arc["radius_pt"] = {"start14": 16, "turn49": 16, "unknown_b": 37,
                                    "unknown_a": 27}[label["id"]]
                if label["id"] == "start14":
                    label.update(radius_pt=30, offset_pt=[-18, -5])
                elif label["id"] == "turn49":
                    label["radius_pt"] = 32
            elif qid not in ("Plane05", "Plane40"):
                arc["radius_pt"] = 16
                if label["type"] == "angle":
                    label["radius_pt"] = max(label.get("radius_pt", 27), 30)
        # The requested annotation change must not alter mathematical inputs.
        protected = set(before) - {"protocol_version", "objects", "labels"}
        assert all(scene[key] == before[key] for key in protected), qid
        old_geometry = [o for o in before["objects"] if o["type"] != "angle_arc"]
        new_geometry = [o for o in scene["objects"] if o["type"] != "angle_arc"]
        assert old_geometry == new_geometry, qid
        validate_scene(scene, protocol)
        refine_angle_labels(scene)
        write_json(path, scene)
        audit.append(audit_record(scene, before, path))
    if audit:
        write_json(ARCHIVE / "migration.json", {"protocol_version": "1.1.0", "questions": audit})
    return [path.stem for path in sorted(SCENES.glob("Plane*.json"))]


if __name__ == "__main__":
    questions = migrate()
    prepare("PlaneGeometry", questions)
    print(f"Migrated and redrawn {len(questions)} scenes; inspect the PNGs before --reviewed.")
