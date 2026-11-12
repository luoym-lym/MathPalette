"""Frozen question Plane477; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane477:

    def __init__(self):
        self.id = 'Plane477'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2711'
        self.question = 'Each of the following four large congruent squares is subdivided into combinations of congruent triangles or rectangles and is partially shaded. What percent of the total area is shaded?\n\n\nChoices:\nA:$12\\frac{1}{2}$\nB:$20$\nC:$25$\nD:$33 \\frac{1}{3}$\nE:$37\\frac{1}{2}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$12\\frac{1}{2}$', 'B': '$20$', 'C': '$25$', 'D': '$33 \\frac{1}{3}$', 'E': '$37\\frac{1}{2}$'}
        self.query = self.question
        self._geometry_01 = [('outer00', [[0.0, 3.0], [2.0, 3.0]]),
         ('outer01', [[2.0, 3.0], [2.0, 5.0]]),
         ('outer02', [[2.0, 5.0], [0.0, 5.0]]),
         ('outer03', [[0.0, 5.0], [0.0, 3.0]]),
         ('vertical1', [[0.5, 3.0], [0.5, 5.0]]),
         ('vertical2', [[1.0, 3.0], [1.0, 5.0]]),
         ('vertical3', [[1.5, 3.0], [1.5, 5.0]]),
         ('outer10', [[3.0, 3.0], [5.0, 3.0]]),
         ('outer11', [[5.0, 3.0], [5.0, 5.0]]),
         ('outer12', [[5.0, 5.0], [3.0, 5.0]]),
         ('outer13', [[3.0, 5.0], [3.0, 3.0]]),
         ('v1', [[4.0, 3.0], [4.0, 5.0]]),
         ('h1', [[3.0, 4.0], [5.0, 4.0]]),
         ('outer20', [[0.0, 0.0], [2.0, 0.0]]),
         ('outer21', [[2.0, 0.0], [2.0, 2.0]]),
         ('outer22', [[2.0, 2.0], [0.0, 2.0]]),
         ('outer23', [[0.0, 2.0], [0.0, 0.0]]),
         ('v2', [[1.0, 0.0], [1.0, 2.0]]),
         ('h2', [[0.0, 1.0], [2.0, 1.0]]),
         ('outer30', [[3.0, 0.0], [5.0, 0.0]]),
         ('outer31', [[5.0, 0.0], [5.0, 2.0]]),
         ('outer32', [[5.0, 2.0], [3.0, 2.0]]),
         ('outer33', [[3.0, 2.0], [3.0, 0.0]]),
         ('v3', [[4.0, 0.0], [4.0, 2.0]]),
         ('h3', [[3.0, 1.0], [5.0, 1.0]]),
         ('bold00', [[0.0, 3.0], [0.5, 3.0]]),
         ('bold01', [[0.5, 3.0], [0.5, 5.0]]),
         ('bold02', [[0.5, 5.0], [0.0, 5.0]]),
         ('bold03', [[0.0, 5.0], [0.0, 3.0]]),
         ('bold10', [[4.0, 5.0], [5.0, 5.0]]),
         ('bold11', [[5.0, 5.0], [5.0, 4.0]]),
         ('bold12', [[5.0, 4.0], [4.0, 5.0]]),
         ('bold20', [[0.0, 0.0], [1.0, 0.0]]),
         ('bold21', [[1.0, 0.0], [1.0, 2.0]]),
         ('bold22', [[1.0, 2.0], [0.0, 1.0]]),
         ('bold23', [[0.0, 1.0], [0.0, 0.0]]),
         ('bold30', [[3.0, 0.0], [4.0, 0.0]]),
         ('bold31', [[4.0, 0.0], [4.0, 1.0]]),
         ('bold32', [[4.0, 1.0], [3.0, 1.0]]),
         ('bold33', [[3.0, 1.0], [3.0, 0.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane477.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12462905402063695, 5.132936789950156], ylim=[-0.13293678995015545, 5.124629054020637], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='identified_region_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='identified_region_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 2.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='identified_region_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 2.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='identified_region_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 4.0], [4.0, 5.0]], [1, 2, 2, 79], id='identified_region_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 4.0], [4.0, 5.0]], [1, 2, 2, 79], id='identified_region_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 3.0], [0.5, 3.0], [0.5, 5.0], [0.0, 5.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='identified_region_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [0.5, 3.0], [0.5, 5.0], [0.0, 5.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='identified_region_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane477().draw(sys.argv[1] if len(sys.argv) > 1 else None))
