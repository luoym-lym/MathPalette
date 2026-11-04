"""Render the adjacent frozen scene only; importing this module writes nothing."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Destination PNG or SVG")
    args = parser.parse_args()
    scene = json.loads((HERE / "scene.json").read_text(encoding="utf-8"))
    output = Path(args.output)
    if output.suffix.lower() not in (".png", ".svg"):
        parser.error("output must end in .png or .svg")
    with matplotlib.rc_context({"font.family": "DejaVu Sans", "savefig.facecolor": "white", "svg.fonttype": "path", "path.simplify": False}):
        fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor="white")
        ax = fig.add_axes(scene["view"]["layout"]["axes_position"])
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(*scene["view"]["xlim"]); ax.set_ylim(*scene["view"]["ylim"])
        ax.set_axis_off(); ax.set_autoscale_on(False)
        for obj in scene["objects"]:
            if obj["type"] != "point": raise ValueError("unsupported object")
            x, y = scene["points"][obj["point"]]
            ax.scatter([x], [y], s=36, marker="o", c="#000000", edgecolors="#000000", linewidths=1, zorder=4)
        fig.savefig(output, dpi=100, facecolor="white", transparent=False)
        plt.close(fig)
if __name__ == "__main__": main()
