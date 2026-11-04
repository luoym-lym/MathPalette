"""Render the frozen grid scene; no output occurs on import."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().with_name("scene.json")
    output = Path(args.output).resolve()
    if output == source or output.suffix.lower() not in (".png", ".svg"):
        raise ValueError("Output must be a new PNG or SVG, not the scene")
    scene = json.loads(source.read_text(encoding="utf-8"))
    with matplotlib.rc_context({"path.simplify": False, "svg.fonttype": "path", "svg.hashsalt": "MathPalette.Plane307", "savefig.bbox": None}):
        fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor="white")
        ax = fig.add_axes(scene["view"]["layout"]["axes_position"])
        ax.set_xlim(*scene["view"]["xlim"]); ax.set_ylim(*scene["view"]["ylim"])
        ax.set_aspect("equal"); ax.set_autoscale_on(False); ax.set_axis_off()
        for obj in scene["objects"]:
            pts = [scene["points"][p] for p in obj["points"]]
            if obj["type"] == "polygon" and obj.get("semantic_fill"):
                ax.add_patch(Polygon(pts, closed=True, facecolor=obj["semantic_color"], edgecolor="none", zorder=1))
            elif obj["type"] == "segment":
                ax.plot([pts[0][0], pts[1][0]], [pts[0][1], pts[1][1]], color="#000000", linewidth=1, solid_capstyle="round", antialiased=True, zorder=2)
            else:
                raise ValueError("Unknown scene object")
        fig.savefig(output, dpi=100, facecolor="white", transparent=False, bbox_inches=None, pad_inches=0, metadata={"Date": None} if output.suffix.lower() == ".svg" else {"Software":"MathPalette stage-one grid renderer"})
        plt.close(fig)

if __name__ == "__main__":
    main()
