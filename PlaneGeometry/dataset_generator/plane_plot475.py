"""Frozen question Plane475; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane475:

    def __init__(self):
        self.id = 'Plane475'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2703'
        self.question = 'How many non-congruent triangles have vertices at three of the eight points in the array shown below?'
        self.answer = '8'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p00': [0, 0], 'p01': [0, 1], 'p10': [1, 0], 'p11': [1, 1], 'p20': [2, 0], 'p21': [2, 1], 'p30': [3, 0], 'p31': [3, 1]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane475.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.09518809249925542, 3.100186679394703], ylim=[-1.1001830456692014, 2.0951917262247566]) as c:
            for object_id, points in [('p00', [self.points['p00']]), ('p01', [self.points['p01']]), ('p10', [self.points['p10']]), ('p11', [self.points['p11']]), ('p20', [self.points['p20']]), ('p21', [self.points['p21']]), ('p30', [self.points['p30']]), ('p31', [self.points['p31']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane475().draw(sys.argv[1] if len(sys.argv) > 1 else None))
