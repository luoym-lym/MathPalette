"""Frozen question Plane255; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane255:

    def __init__(self):
        self.id = 'Plane255'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:749'
        self.question = 'A parallelogram is divided in two parts $P_{1}$ and $P_{2}$, as shown in the picture. Which sentence is always true?\nChoices:\nA:$P_{2}$ has a longer perimeter than $P_{1}$\nB:$P_{2}$ has a smaller perimeter than $P_{1}$\nC:$P_{2}$ has a smaller area than $P_{1}$\nD:$P_{1}$ and $P_{2}$ have the same perimeter\nE:$P_{1}$ and $P_{2}$ have the same area'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$P_{2}$ has a longer perimeter than $P_{1}$',
         'B': '$P_{2}$ has a smaller perimeter than $P_{1}$',
         'C': '$P_{2}$ has a smaller area than $P_{1}$',
         'D': '$P_{1}$ and $P_{2}$ have the same perimeter',
         'E': '$P_{1}$ and $P_{2}$ have the same area'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane255.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3090991525872955, 12.309099152587295], ylim=[-3.815876804671571, 8.80232150050302]) as c:
            c.path([[0, 5], [8, 5], [12, 0], [4, 0], [0, 5]], [1, 2, 2, 2, 79], id='o0')
            for object_id, points in [('o1', [[0, 5], [1.5, 3.9]]), ('o2', [[1.5, 3.9], [2.6, 4.5]]), ('o3', [[2.6, 4.5], [2.7, 3.2]]), ('o4', [[2.7, 3.2], [5.5, 2.95]]), ('o5', [[5.5, 2.95], [5.5, 1.2]]), ('o6', [[5.5, 1.2], [7, 1.95]]), ('o7', [[7, 1.95], [8.4, 0.85]]), ('o8', [[8.4, 0.85], [9.25, 1.45]]), ('o9', [[9.25, 1.45], [9.35, 0.7]]), ('o10', [[9.35, 0.7], [12, 0]])]:
                c.line(points, id=object_id)
            c.text('$P_1$', [4.5, 1.4], offset_pt=[0, 0], vertex=False, id='t0')
            c.text('$P_2$', [7.3, 3.5], offset_pt=[0, 0], vertex=False, id='t1')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane255().draw(sys.argv[1] if len(sys.argv) > 1 else None))
