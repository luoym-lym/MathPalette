"""Frozen question Ana19; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana19:

    def __init__(self):
        self.id = 'Ana19'
        self.source_dataset = 'DynaMath'
        self.question = 'A circle is shown. What is its radius?'
        self.answer = 3
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.circle([1, -2], 3.0, id='curve_001', alpha=1.0, facecolor=[0.0, 0.0, 0.0, 0.0], fill=False)
            return c if _canvas else c.save(output_path)

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana19().draw(sys.argv[1] if len(sys.argv) > 1 else None))
