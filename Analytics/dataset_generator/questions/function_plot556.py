"""Deterministic frozen-scene Author Designed redraw. Importing does not write files."""
from pathlib import Path
import json
import sys
import numpy as np
import platform
import matplotlib
from matplotlib import ft2font
import PIL

_HELPERS = Path(__file__).resolve().parents[1]
if str(_HELPERS) not in sys.path:
    sys.path.insert(0, str(_HELPERS))
from common_renderer import (
    open_canvas,
    plot_curve,
    scatter_points,
    fill_region,
    label,
    figure_label,
    finalize,
)

_SCENE_PATH = _HELPERS / "scenes" / "Ana556.json"


class Ana556:
    def __init__(self):
        self.id = 'Ana556'
        self.source_dataset = "Author Designed"
        self.source_key = 'author_special20_20261111/Ana556'
        self.question = 'Read the unit grid. A linear map T fixes O. The marked points give E1=(1,0), E2=(0,1), T(E1)=E1, and T(E2)=V. Find the Cartesian coordinates of T(P).'
        self.query = self.question
        self.answer = '(1, 2)'
        self.answer_type = 'expression'
        self.subject = "Analytics"
        self.level = None
        self.scene_path = str(_SCENE_PATH)

    def get_scene(self):
        return json.loads(_SCENE_PATH.read_text(encoding="utf-8"))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        actual = (platform.python_version(), np.__version__, matplotlib.__version__, PIL.__version__, ft2font.__freetype_version__)
        if actual != ("3.13.9", "2.5.3", "3.11.2", "12.3.0", "2.14.3"):
            raise RuntimeError(f"Frozen rendering environment required; got {actual}")
        scene = self.get_scene()
        fig, ax = open_canvas(**scene["axes"])
        for obj in scene["objects"]:
            kind = obj["type"]
            if kind == "curve":
                points = np.asarray(obj["points"])
                if len(points):
                    plot_curve(ax, points[:, 0], points[:, 1])
            elif kind == "points":
                points = np.asarray(obj["points"])
                if len(points):
                    scatter_points(ax, points[:, 0], points[:, 1], open_marker=obj["open"])
                    ax.collections[-1].set_clip_on(obj["clip_on"])
            elif kind == "region":
                fill_region(ax, obj["x"], obj["y1"], obj["y2"])
            else:
                raise ValueError(f"Unsupported frozen analytic object: {kind}")
        for entry in scene["labels"]:
            label(ax, entry["x"], entry["y"], entry["text"], ha=entry["ha"], va=entry["va"])
        for text in scene["figure_labels"]:
            figure_label(fig, text)
        target = (
            Path(output_path)
            if output_path
            else _HELPERS.parents[1] / ".runtime" / "reproduced" / "Analytics" / f"{self.id}.png"
        )
        return finalize(fig, target)


def draw(num=0, output_path=None):
    return Ana556().draw(num=num, output_path=output_path)


if __name__ == "__main__":
    print(draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
