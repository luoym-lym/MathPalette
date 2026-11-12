"""Frozen question Plane25; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane25:

    def __init__(self):
        self.id = 'Plane25'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/102'
        self.question = 'The shape is made of unit squares. What is the area of the shape?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p00': [0.0, 0.0],
         'p01': [0.0, 1.0],
         'p02': [0.0, 2.0],
         'p03': [0.0, 3.0],
         'p10': [1.0, 0.0],
         'p11': [1.0, 1.0],
         'p12': [1.0, 2.0],
         'p13': [1.0, 3.0],
         'p20': [2.0, 0.0],
         'p21': [2.0, 1.0],
         'p22': [2.0, 2.0],
         'p23': [2.0, 3.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane25.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5734572248750054, 2.5776993434716937], ylim=[-0.0776993434716935, 3.073457224875005]) as c:
            for object_id, points in [('o1', [self.points['p00'], self.points['p03']]), ('o2', [self.points['p10'], self.points['p13']]), ('o3', [self.points['p20'], self.points['p23']]), ('o4', [self.points['p00'], self.points['p20']]), ('o5', [self.points['p01'], self.points['p21']]), ('o6', [self.points['p02'], self.points['p22']]), ('o7', [self.points['p03'], self.points['p23']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane25().draw(sys.argv[1] if len(sys.argv) > 1 else None))
