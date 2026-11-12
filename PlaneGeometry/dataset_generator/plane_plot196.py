"""Frozen question Plane196; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane196:

    def __init__(self):
        self.id = 'Plane196'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:458'
        self.question = 'Where is the Kangaroo?\nChoices:\nA:In the circle and in the triangle but not in the square.\nB:In the circle and in the square but not in the triangle.\nC:In the triangle and in the square but not in the circle.\nD:In the circle but in neither the square or the triangle.\nE:In the square but in neither the circle or the triangle.'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'In the circle and in the triangle but not in the square.',
         'B': 'In the circle and in the square but not in the triangle.',
         'C': 'In the triangle and in the square but not in the circle.',
         'D': 'In the circle but in neither the square or the triangle.',
         'E': 'In the square but in neither the circle or the triangle.'}
        self.query = self.question
        self._geometry_01 = [[0.9750000000000001, -0.05799999999999998],
         [0.8370000000000001, 0.022500000000000006],
         [0.9405000000000001, 0.11449999999999999],
         [0.9980000000000001, 0.034],
         [0.9635000000000001, -0.05799999999999998],
         [1.1015000000000001, -0.09249999999999999],
         [1.205, 0.10300000000000001],
         [1.2855, 0.31],
         [1.343, 0.3675],
         [1.5845, 0.32149999999999995],
         [1.78, 0.31],
         [1.8605, 0.3675],
         [1.8145, 0.5399999999999999],
         [1.7685, 0.6319999999999999],
         [1.7455, 0.7814999999999999],
         [1.826, 0.6894999999999999],
         [1.8835, 0.5514999999999999],
         [1.872, 0.6894999999999999],
         [1.9295, 0.5744999999999999],
         [2.01, 0.5055],
         [2.102, 0.4595],
         [1.964, 0.4135],
         [1.9065, 0.21799999999999997],
         [1.8605, 0.057],
         [1.803, -0.023499999999999993],
         [1.734, -0.011999999999999997],
         [1.665, 0.057],
         [1.688, 0.1375],
         [1.596, 0.034],
         [1.573, -0.081],
         [1.734, -0.14999999999999997],
         [1.8375, -0.104],
         [1.8835, -0.21899999999999997],
         [1.4925000000000002, -0.1845],
         [1.3775, -0.14999999999999997],
         [1.458, 0.0915],
         [1.481, 0.1835],
         [1.3315000000000001, 0.045500000000000006],
         [1.1360000000000001, -0.20749999999999996],
         [0.9750000000000001, -0.05799999999999998],
         [0.9750000000000001, -0.05799999999999998]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane196.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.2197140046864834, 6.1270582406177425], ylim=[-3.474457301787358, 5.8723149435168684], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 3.0, id='circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.path([[0.5, -0.5], [4.7, -0.5], [4.7, 3.7], [0.5, 3.7], [0.5, -0.5]], [1, 2, 2, 2, 79], id='square', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.95, 1.15], [3.0, 5.4], [5.9, -0.25], [0.95, 1.15]], [1, 2, 2, 79], id='triangle', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path(self._geometry_01, self._geometry_02, id='kangaroo', facecolor=[0.0, 0.0, 0.0, 1.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane196().draw(sys.argv[1] if len(sys.argv) > 1 else None))
