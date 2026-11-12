"""Frozen question Plane413; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane413:

    def __init__(self):
        self.id = 'Plane413'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1776'
        self.question = 'Each square in the grid shown is $1 \\mathrm{~cm}$ by $1 \\mathrm{~cm}$. What is the area of the shaded figure, in $\\mathrm{cm}^{2}$?'
        self.answer = '17'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane413.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2230502095313236, 9.238034935319352], ylim=[-3.238029551592005, 6.223055593258671], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 3.0], [9.0, 3.0], [7.0, 0.0], [6.0, 2.0], [4.0, 0.0], [3.0, 1.0], [2.0, 0.0], [0.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='grey', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [9.0, 3.0], [7.0, 0.0], [6.0, 2.0], [4.0, 0.0], [3.0, 1.0], [2.0, 0.0], [0.0, 3.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='grey', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('v0', [[0.0, 0.0], [0.0, 3.0]]), ('v1', [[1.0, 0.0], [1.0, 3.0]]), ('v2', [[2.0, 0.0], [2.0, 3.0]]), ('v3', [[3.0, 0.0], [3.0, 3.0]]), ('v4', [[4.0, 0.0], [4.0, 3.0]]), ('v5', [[5.0, 0.0], [5.0, 3.0]]), ('v6', [[6.0, 0.0], [6.0, 3.0]]), ('v7', [[7.0, 0.0], [7.0, 3.0]]), ('v8', [[8.0, 0.0], [8.0, 3.0]]), ('v9', [[9.0, 0.0], [9.0, 3.0]]), ('h0', [[0.0, 0.0], [9.0, 0.0]]), ('h1', [[0.0, 1.0], [9.0, 1.0]]), ('h2', [[0.0, 2.0], [9.0, 2.0]]), ('h3', [[0.0, 3.0], [9.0, 3.0]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane413().draw(sys.argv[1] if len(sys.argv) > 1 else None))
