"""Deterministic frozen-scene MathVista redraw. Importing does not write files."""
from pathlib import Path
import json
import sys
import numpy as np

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

_SCENE_PATH = _HELPERS / "scenes" / "Ana94.json"


class Ana94:
    def __init__(self):
        self.id = 'Ana94'
        self.source_dataset = "MathVista"
        self.source_key = 'testmini/308'
        self.question = 'What is this function most likely be?\nChoices:\nA: a polynomial\nB: a trigonometric function\nC: an exponential function\nD: a logarithmic function'
        self.query = self.question
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'a polynomial', 'B': 'a trigonometric function', 'C': 'an exponential function', 'D': 'a logarithmic function'}
        self.subject = "Analytics"
        self.level = None
        self.scene_path = str(_SCENE_PATH)

    def get_scene(self):
        return json.loads(_SCENE_PATH.read_text(encoding="utf-8"))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
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
    return Ana94().draw(num=num, output_path=output_path)


if __name__ == "__main__":
    print(draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
