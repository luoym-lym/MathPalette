"""Fit and freeze geometry page layout without changing mathematical geometry.

Run after a protocol update: python -B dataset_tools/geometry_layout.py BRANCH IDS...
Only the protocol version, square view and label spacing are migrated.
Rendering continues to use those frozen values, with autoscale disabled.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from dataset_tools.geometry_dataset import read_json, renderer_for, write_json, prepare


def content_bbox(image):
    """Include strokes, labels, dimensions and semantic fills, not the white page."""
    image = image.convert("RGB")
    return ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()


def layout_metrics(image):
    bounds = content_bbox(image)
    if bounds is None:
        raise ValueError("Empty geometry drawing")
    width, height = image.size
    x0, y0, x1, y1 = bounds
    return {"content_bbox_px": list(bounds),
            "long_side_fraction": max((x1-x0)/width, (y1-y0)/height),
            "center_offset_px": [(x0+x1-width)/2, (y0+y1-height)/2],
            "minimum_outer_margin_fraction": min(x0/width, y0/height,
                                                  (width-x1)/width, (height-y1)/height)}


def fit_scene(scene, renderer, protocol=None):
    """Measure a preview repeatedly, then freeze only its equal-scale square view."""
    protocol = protocol or read_json(renderer.PROTOCOL_PATH)
    fitted = deepcopy(scene)
    target = protocol["view"]["target_long_side_fraction"]
    width, height = protocol["output"]["width_px"], protocol["output"]["height_px"]
    axes_width = width * protocol["figure"]["axes_position"][2]
    for iteration in range(24):
        fig, _ = renderer.render_scene(fitted, protocol, check_layout=False)
        try:
            fig.canvas.draw()
            metrics = layout_metrics(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())))
        finally:
            plt.close(fig)
        dx, dy = metrics["center_offset_px"]
        occupancy = metrics["long_side_fraction"]
        if abs(occupancy-target) <= 1.5/width and max(abs(dx), abs(dy)) <= 1:
            break
        span = fitted["view"]["xlim"][1]-fitted["view"]["xlim"][0]
        cx = sum(fitted["view"]["xlim"])/2 + dx * span/axes_width
        cy = sum(fitted["view"]["ylim"])/2 - dy * span/axes_width
        new_span = span * occupancy/target
        fitted["view"]["xlim"] = [cx-new_span/2, cx+new_span/2]
        fitted["view"]["ylim"] = [cy-new_span/2, cy+new_span/2]
    else:
        raise ValueError(f"Content fitting did not converge: {scene['id']}")
    if metrics["minimum_outer_margin_fraction"] < protocol["view"]["minimum_outer_margin_fraction"]:
        raise ValueError(f"Insufficient outer margin: {scene['id']}")
    fitted["view"]["layout"] = {"method": "frozen_content_fit", "target_long_side_fraction": target,
                                  "include": ["geometry", "labels", "dimensions", "markers"],
                                  "equal_scale": True, "center": "content_bbox"}
    return fitted, metrics


def migrate(branch, qids):
    renderer = renderer_for(branch)
    protocol = read_json(renderer.PROTOCOL_PATH)
    for qid in qids:
        path = ROOT/branch/"dataset_generator/scenes"/f"{qid}.json"
        scene = read_json(path)
        if scene["protocol_version"] != protocol["protocol_version"]:
            # Keep label direction/ownership, including explicit user corrections.
            for label in scene["labels"]:
                scale = 1.5 if label["type"] == "vertex" else 4/3
                if "offset_pt" in label:
                    label["offset_pt"] = [value*scale for value in label["offset_pt"]]
                if label["type"] == "angle" and "radius_pt" in label:
                    label["radius_pt"] *= scale
            for dimension in scene.get("dimensions", []):
                for field in ("offset_pt", "label_offset_pt"):
                    dimension[field] = [value*4/3 for value in dimension[field]]
            scene["protocol_version"] = protocol["protocol_version"]
        fitted, metrics = fit_scene(scene, renderer, protocol)
        write_json(path, fitted)
        prepare(branch, [qid])
        print(f"{qid}: longest side {metrics['long_side_fraction']:.3f}, center {metrics['center_offset_px']}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("branch", choices=["PlaneGeometry", "SolidGeometry"])
    parser.add_argument("questions", nargs="+")
    args = parser.parse_args()
    migrate(args.branch, args.questions)
