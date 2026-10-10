"""Offline redraw of imported, frozen A/B recipes using this dataset only."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import platform
import sys
import threading
from importlib.metadata import version
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
GENERATOR_VERSION = "fine-grained-AB-1.0.0"
RENDER_LOCK = threading.RLock()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pixel_hash(image_or_path):
    if isinstance(image_or_path, bytes):
        image_or_path = io.BytesIO(image_or_path)
    with Image.open(image_or_path) as source:
        image = source.convert("RGBA")
        prefix = f"{image.width}x{image.height}:RGBA:".encode("ascii")
        return hashlib.sha256(prefix + image.tobytes()).hexdigest()


def environment_versions():
    return {"python": platform.python_version(), **{name: version(name)
            for name in ("matplotlib", "numpy", "pillow")}}


def assert_baseline():
    manifest = json.loads((ROOT / "dataset_generator/baseline_manifest.json").read_text(encoding="utf-8"))
    if canonical_hash(manifest["files"]) != manifest["fingerprint"]:
        raise ValueError("Baseline manifest fingerprint is invalid.")
    for relative, digest in manifest["files"].items():
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or file_hash(path) != digest:
            raise ValueError(f"Frozen baseline changed: {relative}")
    return manifest


def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_question(question_id):
    """Bind the local common renderer even if another dataset was imported."""
    records = {row["id"]: row for row in map(json.loads, (ROOT / "dataset.jsonl").read_text(encoding="utf-8").splitlines()) if row}
    if question_id not in records:
        raise ValueError(f"Unknown question: {question_id}")
    matches = []
    common = _load_module("_fine_grained_common_renderer", ROOT / "dataset_generator/common_renderer.py")
    previous = sys.modules.get("common_renderer")
    sys.modules["common_renderer"] = common
    try:
        for path in sorted((ROOT / "dataset_generator/dataset_generator").glob("function_plot*.py")):
            module = _load_module("_fine_grained_" + path.stem, path)
            cls = getattr(module, question_id, None)
            if cls is not None:
                matches.append((module, cls()))
    finally:
        if previous is None:
            sys.modules.pop("common_renderer", None)
        else:
            sys.modules["common_renderer"] = previous
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one frozen class: {question_id}")
    module, question = matches[0]
    record = records[question_id]
    if question.id != question_id or question.query != record["question"] or (
            type(question.answer) is not type(record["answer"]) or question.answer != record["answer"]):
        raise ValueError("Frozen class and dataset record disagree.")
    return module, question, common


def _scene(question_id):
    module, question, common = load_question(question_id)
    captured = []
    previous = module.finalize
    before = set(plt.get_fignums())
    def capture(fig, destination):
        common.lock_view(fig.axes[0])
        captured.append(fig)
        return {}
    module.finalize = capture
    try:
        question.draw(0)
        if len(captured) != 1:
            raise ValueError("A frozen question must produce exactly one figure.")
        return captured[0]
    except Exception:
        for number in set(plt.get_fignums()) - before:
            plt.close(number)
        raise
    finally:
        module.finalize = previous


def _apply(fig, operation, params):
    """Preserve the original A/B executor's Matplotlib drawing semantics."""
    ax, background = fig.axes[0], "#FFFFFF"
    if operation == "A1":
        for axis in (ax.xaxis, ax.yaxis):
            for tick, location in zip(axis.get_major_ticks(), axis.get_majorticklocs()):
                tick.gridline.set_visible(location in params["grid_positions"])
    elif operation == "A2":
        ax.tick_params(axis="both", labelbottom=False, labeltop=False, labelleft=False, labelright=False)
        ax._mp_origin_zero.set_visible(False)
    elif operation == "A3":
        kwargs = {"fill": False, "edgecolor": params["color"], "linewidth": params["linewidth_pt"],
                  "linestyle": "-", "zorder": 3, "gid": "variant_addition"}
        if params["shape"] == "ellipse":
            patch = Ellipse(params["center"], params["width"], params["height"], angle=params["angle_deg"], **kwargs)
        else:
            patch = Polygon(params["vertices"], closed=True, **kwargs)
        ax.add_patch(patch)
    elif operation == "A4":
        background = params["background_color"]
        fig.patch.set_facecolor(background)
        ax.set_facecolor(background)
        for text in [*ax.get_xticklabels(), *ax.get_yticklabels(), ax._mp_origin_zero]:
            if text.get_bbox_patch() is not None:
                text.get_bbox_patch().set_facecolor(background)
    elif operation in ("B1", "B5"):
        for point in params["points"]:
            x, y = point["xy"]
            ax.scatter([x], [y], s=point["size_pt2"], marker="o",
                       facecolors=point["color"] if point["filled"] else background,
                       edgecolors=point["color"], linewidths=params["linewidth_pt"],
                       zorder=4, gid="variant_addition")
    elif operation in ("B2", "B3", "B4"):
        endpoints = np.asarray(params["endpoints"])
        style = "-" if params["linestyle"] == "solid" else (0, tuple(params["dash_pattern_pt"]))
        ax.plot(endpoints[:, 0], endpoints[:, 1], color=params["color"], linewidth=params["linewidth_pt"],
                linestyle=style, zorder=3, solid_capstyle="butt", gid="variant_addition")
    else:
        raise ValueError(f"Unsupported A/B operation: {operation}")
    return background


def render_recipe(recipe, output_path=None):
    """Verify an accepted snapshot, redraw, compare pixels, then save outside inputs."""
    with RENDER_LOCK:
        manifest = assert_baseline()
        if recipe["status"] != "passed" or recipe["generator_version"] != GENERATOR_VERSION:
            raise ValueError("Only accepted recipes for this executor can be redrawn.")
        if recipe["environment"] != environment_versions() or recipe["baseline_fingerprint"] != manifest["fingerprint"]:
            raise ValueError("Recipe environment or baseline does not match.")
        if recipe["parameter_key"] != canonical_hash({"operation": recipe["operation"], "params": recipe["params"]}):
            raise ValueError("Frozen A/B parameters changed.")
        qid, slot = recipe["question_id"], recipe["slot_id"]
        if slot not in [f"{group}{n:02d}" for group in "AB" for n in range(1, 6)] or slot[0] != recipe["category"]:
            raise ValueError("Invalid A/B slot.")
        if not recipe["operation"].startswith(recipe["category"]):
            raise ValueError("Operation and category disagree.")
        expected = f"base_variant/{qid}/images/{slot}.png"
        if recipe["image_path"] != expected or pixel_hash(ROOT / expected) != recipe["pixel_sha256"]:
            raise ValueError("Accepted image is missing or changed.")
        destination = Path(output_path).resolve() if output_path is not None else ROOT / "reproduced" / qid / f"{slot}.png"
        if destination.suffix.lower() != ".png":
            raise ValueError("Redraw output must be a PNG.")
        # Generated outputs are distinct from every input and formally accepted file.
        if destination.is_relative_to(ROOT) and not destination.is_relative_to(ROOT / "reproduced"):
            raise ValueError("Redraw output cannot overwrite this dataset's inputs or accepted data.")
        if destination.is_relative_to(ROOT.parent / "construct_dataset"):
            raise ValueError("Redraw output cannot overwrite the source dataset.")
        fig = _scene(qid)
        try:
            background = _apply(fig, recipe["operation"], recipe["params"])
            buffer = io.BytesIO()
            fig.savefig(buffer, dpi=100, facecolor=background, transparent=False)
            data = buffer.getvalue()
            with Image.open(io.BytesIO(data)) as image:
                if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
                    raise ValueError("Expected an opaque 768×768 image.")
            if pixel_hash(data) != recipe["pixel_sha256"]:
                raise ValueError(f"Redraw differs from reviewed image: {qid}/{slot}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            return destination
        finally:
            plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Redraw one frozen A/B variant; never sample or approve new data.")
    parser.add_argument("question_id")
    parser.add_argument("slot_id")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    recipes = json.loads((ROOT / "base_variant" / args.question_id / "recipes.json").read_text(encoding="utf-8"))
    recipe = next(r for r in recipes if r["slot_id"] == args.slot_id)
    print(render_recipe(recipe, args.output))
