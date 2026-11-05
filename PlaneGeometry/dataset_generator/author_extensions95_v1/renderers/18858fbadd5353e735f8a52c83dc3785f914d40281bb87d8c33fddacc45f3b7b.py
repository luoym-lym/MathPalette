"""Frozen, data-driven original renderer; importing this module writes nothing."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

def draw(output, record=None, svg=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    from matplotlib import ft2font
    import numpy as np
    from PIL import Image, ImageChops, __version__ as pillow_version
    scene_path = HERE / "scene.json"
    scene = json.loads(scene_path.read_text(encoding="utf-8"))
    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 16,
        "svg.fonttype": "path", "svg.hashsalt": scene["id"],
        "path.simplify": False, "lines.antialiased": True,
        "text.antialiased": True, "figure.facecolor": "white",
        "savefig.facecolor": "white", "savefig.transparent": False,
    })
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor="white")
    view = scene["view"]
    ax = fig.add_axes(view["layout"]["axes_position"])
    ax.set_xlim(view["xlim"])
    ax.set_ylim(view["ylim"])
    ax.set_aspect("equal", adjustable="box")
    ax.set_autoscale_on(False)
    ax.set_axis_off()
    points = scene["points"]
    def xy(value):
        return points[value] if isinstance(value, str) else value
    for obj in scene["objects"]:
        if obj["type"] == "segment":
            a, b = map(xy, obj["points"])
            artist, = ax.plot([a[0], b[0]], [a[1], b[1]],
                color=obj["stroke_color"], linewidth=obj["linewidth_pt"],
                solid_capstyle="round", antialiased=True,
                zorder=1 if obj["role"] == "grid" else 3)
        elif obj["type"] == "point_marker":
            radius = obj["radius_pt"] / 72 * fig.dpi / (
                768 * view["layout"]["axes_position"][2] /
                (view["xlim"][1] - view["xlim"][0]))
            artist = Circle(xy(obj["point"]), radius=radius,
                fill=False, edgecolor="black", linewidth=1.0,
                antialiased=True, zorder=4)
            ax.add_patch(artist)
        else:
            raise ValueError(f"Unknown frozen object: {obj['type']}")
        artist.set_gid(obj["id"])
    for label in scene["labels"]:
        artist = ax.annotate(label["text"], xy=points[label["point"]],
            xytext=label["offset_pt"], textcoords="offset points",
            fontsize=18, fontfamily="DejaVu Sans", fontstyle="italic",
            ha="center", va="center", color="black", zorder=5,
            annotation_clip=False)
        artist.set_gid(label["id"])
    output = Path(output)
    if not output.is_absolute():
        output = HERE / output
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=100, facecolor="white", transparent=False,
        metadata={"Software": "MathPalette staged original renderer"})
    if svg:
        svg = Path(svg)
        if not svg.is_absolute():
            svg = HERE / svg
        svg.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(svg, format="svg", facecolor="white", transparent=False,
            metadata={"Date": None, "Creator": "MathPalette staged original renderer"})
    plt.close(fig)
    if record:
        image = Image.open(output).convert("RGBA")
        rgb = image.convert("RGB")
        bbox = ImageChops.difference(rgb, Image.new("RGB", rgb.size, "white")).getbbox()
        width, height = image.size
        cx, cy = (bbox[0] + bbox[2])/2, (bbox[1] + bbox[3])/2
        longest = max(bbox[2] - bbox[0], bbox[3] - bbox[1]) / width
        margin = min(bbox[0], bbox[1], width-bbox[2], height-bbox[3]) / width
        assert image.size == (768, 768)
        assert image.getchannel("A").getextrema() == (255, 255)
        assert margin >= .05 and abs(cx - 384) <= 2 and abs(cy - 384) <= 2
        assert .85 <= longest <= .87
        info = {
            "pid": os.getpid(), "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
            "output": str(output.relative_to(HERE)).replace("\\", "/"),
            "file_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "decoded_rgba_sha256": hashlib.sha256(image.tobytes()).hexdigest(),
            "size": list(image.size), "alpha_extrema": [255, 255],
            "content_bbox_px": bbox, "center_px": [cx, cy],
            "long_side_fraction": longest, "minimum_margin_fraction": margin,
            "dependencies": {"python": platform.python_version(),
                "numpy": np.__version__, "matplotlib": matplotlib.__version__,
                "pillow": pillow_version, "freetype": ft2font.__freetype_version__},
            "scene_sha256": hashlib.sha256(scene_path.read_bytes()).hexdigest(),
            "renderer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "isolation": {key: os.environ.get(key) for key in
                ["PYTHONDONTWRITEBYTECODE", "MPLCONFIGDIR", "TEMP", "TMP"]},
        }
        record_path = Path(record)
        if not record_path.is_absolute():
            record_path = HERE / record_path
        record_path.write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {output.name}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="baseline.png")
    parser.add_argument("--record")
    parser.add_argument("--svg")
    args = parser.parse_args()
    draw(args.output, args.record, args.svg)

if __name__ == "__main__":
    main()
