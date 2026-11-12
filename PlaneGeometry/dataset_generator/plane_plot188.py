"""Frozen question Plane188; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane188:

    def __init__(self):
        self.id = 'Plane188'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:401'
        self.question = 'If the length of the side of a little square is 1, what is the area of the letter N?'
        self.answer = '18'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('v0_0', [[0.0, 0.0], [0.0, 6.0]]),
         ('v1_0', [[1.0, 0.0], [1.0, 6.0]]),
         ('v2_0', [[2.0, 0.0], [2.0, 6.0]]),
         ('v3_0', [[3.0, 0.0], [3.0, 3.0]]),
         ('v4_0', [[4.0, 3.0], [4.0, 6.0]]),
         ('v5_0', [[5.0, 0.0], [5.0, 6.0]]),
         ('v6_0', [[6.0, 0.0], [6.0, 6.0]]),
         ('v7_0', [[7.0, 0.0], [7.0, 6.0]]),
         ('h0_0', [[0.0, 0.0], [1.0, 0.0]]),
         ('h0_1', [[2.0, 0.0], [4.0, 0.0]]),
         ('h0_3', [[6.0, 0.0], [7.0, 0.0]]),
         ('h1_0', [[0.0, 1.0], [1.0, 1.0]]),
         ('h1_1', [[2.0, 1.0], [3.6666666666666665, 1.0]]),
         ('h1_2', [[4.666666666666667, 1.0], [5.0, 1.0]]),
         ('h1_3', [[6.0, 1.0], [7.0, 1.0]]),
         ('h2_0', [[0.0, 2.0], [1.0, 2.0]]),
         ('h2_1', [[2.0, 2.0], [3.3333333333333335, 2.0]]),
         ('h2_2', [[4.333333333333333, 2.0], [5.0, 2.0]]),
         ('h2_3', [[6.0, 2.0], [7.0, 2.0]]),
         ('h3_0', [[0.0, 3.0], [1.0, 3.0]]),
         ('h3_1', [[2.0, 3.0], [3.0, 3.0]]),
         ('h3_2', [[4.0, 3.0], [5.0, 3.0]]),
         ('h3_3', [[6.0, 3.0], [7.0, 3.0]]),
         ('h4_0', [[0.0, 4.0], [1.0, 4.0]]),
         ('h4_1', [[2.0, 4.0], [2.666666666666667, 4.0]]),
         ('h4_2', [[3.666666666666667, 4.0], [5.0, 4.0]]),
         ('h4_3', [[6.0, 4.0], [7.0, 4.0]]),
         ('h5_0', [[0.0, 5.0], [1.0, 5.0]]),
         ('h5_1', [[2.0, 5.0], [2.333333333333333, 5.0]]),
         ('h5_2', [[3.333333333333333, 5.0], [5.0, 5.0]]),
         ('h5_3', [[6.0, 5.0], [7.0, 5.0]]),
         ('h6_0', [[0.0, 6.0], [1.0, 6.0]]),
         ('h6_2', [[3.0, 6.0], [5.0, 6.0]]),
         ('h6_3', [[6.0, 6.0], [7.0, 6.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane188.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.17816062571270042, 7.1831447805536905], ylim=[-0.6797831820162257, 6.681522224250165], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 6.0], [1.0, 6.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='Npart0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 6.0], [1.0, 6.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='Npart0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 6.0], [5.0, 6.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='Npart1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 6.0], [5.0, 6.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='Npart1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 6.0], [3.0, 6.0], [5.0, 0.0], [4.0, 0.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='Npart2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 6.0], [3.0, 6.0], [5.0, 0.0], [4.0, 0.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='Npart2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane188().draw(sys.argv[1] if len(sys.argv) > 1 else None))
