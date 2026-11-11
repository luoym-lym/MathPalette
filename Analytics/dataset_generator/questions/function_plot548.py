"""Frozen Author Designed original. Importing writes no artifacts."""
from pathlib import Path
import json
import sys
import numpy as np
_HELPERS = Path(__file__).resolve().parents[1]
if str(_HELPERS) not in sys.path:
    sys.path.insert(0, str(_HELPERS))
from common_renderer import open_canvas, plot_curve, scatter_points, label, finalize
_SCENE_PATH = _HELPERS / "scenes" / "Ana548.json"

class Ana548:
    def __init__(self):
        self.id = 'Ana548'
        self.source_dataset = "Author Designed"
        self.question = 'The graph shows a one-to-one function f on its displayed closed domain. Find f^(-1)(3).'
        self.query = self.question
        self.answer = '2'
        self.answer_type = 'number'
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
            coords = np.asarray(obj["points"], dtype=float)
            if obj["type"] == "curve":
                plot_curve(ax, coords[:, 0], coords[:, 1])
            else:
                scatter_points(ax, coords[:, 0], coords[:, 1], open_marker=obj["open"])
        for entry in scene["labels"]:
            label(ax, **entry)
        target = Path(output_path) if output_path else _HELPERS.parents[1] / ".runtime" / "reproduced" / "Analytics" / (self.id + ".png")
        return finalize(fig, target)

def draw(num=0, output_path=None):
    return Ana548().draw(num=num, output_path=output_path)

if __name__ == "__main__":
    print(draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
