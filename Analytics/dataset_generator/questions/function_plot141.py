"""Frozen We-Math original; user batch admission is recorded in provenance. Importing writes no artifacts."""
from pathlib import Path
import json
import importlib.util
import platform
import sys
import numpy as np
import matplotlib
from matplotlib import ft2font
import PIL

_HELPERS = Path(__file__).resolve().parents[1]
_RENDERER = _HELPERS / "wemath_renderers" / '39d623eb465b9f92ec7f6e38382de08883a6f995e44990c0e9026c665bce00b2' / "common_renderer.py"
_SPEC = importlib.util.spec_from_file_location("_wemath_frozen_renderer_Ana141", _RENDERER)
_RENDER = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_RENDER)
open_canvas = _RENDER.open_canvas
plot_curve = _RENDER.plot_curve
scatter_points = _RENDER.scatter_points
fill_region = _RENDER.fill_region
fill_polygon = _RENDER.fill_polygon
label = _RENDER.label
figure_label = _RENDER.figure_label
finalize = _RENDER.finalize
_SCENE_PATH = _HELPERS / "scenes" / 'Ana141.json'

class Ana141:
    def __init__(self):
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5462'
        self.question = 'Find the equation of the curve symmetric to the equilateral hyperbola in the figure with respect to $y = x$.'
        self.answer = '$\\frac{y^2}{4} - \\frac{x^2}{4} = 1$'
        self.answer_type = 'expression'
        self.id = 'Ana141'
        self.query = 'Find the equation of the curve symmetric to the equilateral hyperbola in the figure with respect to $y = x$.'
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = str(_SCENE_PATH)

    def get_scene(self):
        return json.loads(_SCENE_PATH.read_text(encoding="utf-8"))

    def draw(self, num=0, output_path=None):
        actual = (platform.python_version(), np.__version__, matplotlib.__version__, PIL.__version__, ft2font.__freetype_version__)
        if actual != ("3.13.9", "2.5.3", "3.11.2", "12.3.0", "2.14.3"):
            raise RuntimeError(f"Frozen rendering environment required; got {actual}")
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        scene = self.get_scene()
        fig, ax = open_canvas(**scene.get("axes", {}))
        for obj in scene["objects"]:
            kind = obj["type"]
            if kind in ("curve", "points"):
                points = np.asarray(obj["points"], dtype=float)
                if kind == "curve":
                    plot_curve(ax, points[:, 0], points[:, 1])
                else:
                    scatter_points(ax, points[:, 0], points[:, 1], open_marker=obj.get("open", False))
                    ax.collections[-1].set_clip_on(obj.get("clip_on", True))
            elif kind == "region":
                fill_region(ax, obj["x"], obj["y1"], obj.get("y2", 0))
            elif kind == "polygon_region":
                fill_polygon(ax, obj["x"], obj["y"])
            else:
                raise ValueError(f"Unsupported frozen object: {kind}")
        for entry in scene.get("labels", []):
            label(ax, entry["x"], entry["y"], entry["text"], ha=entry.get("ha", "center"), va=entry.get("va", "center"))
        for text in scene.get("figure_labels", []):
            figure_label(fig, text)
        target = Path(output_path) if output_path else _HELPERS.parents[1] / ".runtime" / "reproduced" / "Analytics" / f"{self.id}.png"
        return finalize(fig, target)


def draw(num=0, output_path=None):
    return Ana141().draw(num=num, output_path=output_path)


if __name__ == "__main__":
    print(draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
