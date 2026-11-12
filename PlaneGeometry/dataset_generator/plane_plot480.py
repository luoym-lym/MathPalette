"""Frozen question Plane480; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane480:

    def __init__(self):
        self.id = 'Plane480'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2747'
        self.question = 'The twelve-sided figure shown has been drawn on $1 \\text{ cm}\\times 1 \\text{ cm}$ graph paper. What is the area of the figure in $\\text{cm}^2$?'
        self.answer = '13'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane480.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1708095785044188, 7.182464365228442], ylim=[-0.18246436522844167, 7.170809578504419], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('v0', [[0.0, 0.0], [0.0, 7.0]]), ('v1', [[1.0, 0.0], [1.0, 7.0]]), ('v2', [[2.0, 0.0], [2.0, 7.0]]), ('v3', [[3.0, 0.0], [3.0, 7.0]]), ('v4', [[4.0, 0.0], [4.0, 7.0]]), ('v5', [[5.0, 0.0], [5.0, 7.0]]), ('v6', [[6.0, 0.0], [6.0, 7.0]]), ('h1', [[0.0, 1.0], [7.0, 1.0]]), ('h2', [[0.0, 2.0], [7.0, 2.0]]), ('h3', [[0.0, 3.0], [7.0, 3.0]]), ('h4', [[0.0, 4.0], [7.0, 4.0]]), ('h5', [[0.0, 5.0], [7.0, 5.0]]), ('h6', [[0.0, 6.0], [7.0, 6.0]]), ('h7', [[0.0, 7.0], [7.0, 7.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#AAAAAA')
            c.path([[1.0, 3.0], [2.0, 4.0], [2.0, 5.0], [3.0, 6.0], [4.0, 5.0], [5.0, 5.0], [6.0, 4.0], [5.0, 3.0], [5.0, 2.0], [4.0, 1.0], [3.0, 2.0], [2.0, 2.0], [1.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='boundary', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane480().draw(sys.argv[1] if len(sys.argv) > 1 else None))
