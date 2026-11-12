"""Frozen question Ana01; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana01:

    def __init__(self):
        self.id = 'Ana01'
        self.source_dataset = 'DynaMath'
        self.question = 'What is the limit of the function as x approaches 1 from the left side?'
        self.answer = 0
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
        with Canvas(ANALYTICS) as c:
            x = np.linspace(-8, 1, 200)
            c.line(np.column_stack((x, x * x + x - 2)), id='curve_001', solid_capstyle='butt')
            x = np.linspace(1, 8, 200)
            c.line(np.column_stack((x, -4 * x + 2)), id='curve_002', solid_capstyle='butt')
            c.point([[1, 0]], filled=False, id='point_001')
            c.point([[1, -2]], id='point_002')
            return c if _canvas else c.save(output_path)

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana01().draw(sys.argv[1] if len(sys.argv) > 1 else None))
