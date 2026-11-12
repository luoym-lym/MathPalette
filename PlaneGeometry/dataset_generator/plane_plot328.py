"""Frozen question Plane328; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane328:

    def __init__(self):
        self.id = 'Plane328'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1051'
        self.question = 'What is the minimum number of dots that must be taken away from the picture so that no three of the remaining dots lie on a straight line?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P00': [0, 0], 'P01': [0, 1], 'P02': [0, 2], 'P10': [1, 0], 'P11': [1, 1], 'P12': [1, 2], 'P20': [2, 0], 'P21': [2, 1], 'P22': [2, 2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane328.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.06151447582090652, 2.0646394758209063], ylim=[-0.06463947582090623, 2.0615144758209065]) as c:
            for object_id, points in [('dotP00', [self.points['P00']]), ('dotP01', [self.points['P01']]), ('dotP02', [self.points['P02']]), ('dotP10', [self.points['P10']]), ('dotP11', [self.points['P11']]), ('dotP12', [self.points['P12']]), ('dotP20', [self.points['P20']]), ('dotP21', [self.points['P21']]), ('dotP22', [self.points['P22']])]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane328().draw(sys.argv[1] if len(sys.argv) > 1 else None))
