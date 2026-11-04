"""Render frozen scene, without side effects on import."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    scene = json.loads((Path(__file__).parent / "scene.json").read_text(encoding="utf-8"))
    output = Path(args.output)
    if output.resolve() in {(Path(__file__).parent / "scene.json").resolve(), Path(__file__).resolve()}:
        raise ValueError("output may not overwrite frozen inputs")
    if output.suffix.lower() not in (".png", ".svg"):
        raise ValueError("output must be PNG or SVG")
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor="#FFFFFF")
    ax = fig.add_axes(scene["view"]["layout"]["axes_position"])
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(*scene["view"]["xlim"]); ax.set_ylim(*scene["view"]["ylim"])
    ax.set_axis_off(); ax.set_autoscale_on(False)
    for obj in scene["objects"]:
        if obj["type"] != "point":
            raise ValueError("unsupported object")
        x,y = scene["points"][obj["point"]]
        ax.scatter([x], [y], s=obj["area_pt2"], c="#000000", edgecolors="#000000", linewidths=1, zorder=4)
    fig.savefig(output, dpi=100, facecolor="#FFFFFF", transparent=False, bbox_inches=None, pad_inches=0, metadata={"Software":"MathPalette staged original"} if output.suffix.lower()==".png" else None)
    plt.close(fig)

if __name__ == "__main__":
    main()
