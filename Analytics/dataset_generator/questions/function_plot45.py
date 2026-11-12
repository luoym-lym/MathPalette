"""Frozen question Ana45; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana45:

    def __init__(self):
        self.id = 'Ana45'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3009'
        self.question = 'Let $f$ be the function given by the following graph. What is the domain of $f$?'
        self.answer = '$[-5,-3) \\cup(-3,5]$'
        self.answer_type = 'expression'
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
            for object_id, points in [('curve_001', [[-5.0, 1.0], [-3.0, 2.0]]), ('curve_002', [[-3.0, 2.0], [-1.0, 4.0]]), ('curve_003', [[-1.0, 5.0], [3.0, 3.0], [5.0, 1.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.point([[-5.0, 1.0]], id='point_001')
            c.point([[-3.0, 2.0]], id='point_002', facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-1.0, 4.0]], id='point_003', facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-1.0, 5.0]], id='point_004')
            c.point([[5.0, 1.0]], id='point_005')
            return c if _canvas else c.save(output_path)

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana45().draw(sys.argv[1] if len(sys.argv) > 1 else None))
