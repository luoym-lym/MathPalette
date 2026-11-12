"""Frozen question Plane24; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane24:

    def __init__(self):
        self.id = 'Plane24'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/84'
        self.question = 'ABCD is a square. Inscribed Circle center is O. Find the the angle of ∠AMK. Return the numeric value.'
        self.answer = '130.9'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-1.0, -1.0],
         'B': [-1.0, 1.0],
         'C': [1.0, 1.0],
         'D': [1.0, -1.0],
         'E': [-1.0, 0.0],
         'F': [0.0, 1.0],
         'G': [1.0, 0.0],
         'H': [0.0, -1.0],
         'O': [0.0, 0.0],
         'K': [-0.7071067811865476, 0.7071067811865476],
         'M': [-0.4530818393219729, 0.09383632135605424],
         'U': [-0.33333333333333337, 0.33333333333333326]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane24.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.150730183282768, 1.153491292487297], ylim=[-1.1447862037078684, 1.1594352720621968]) as c:
            for object_id, points in [('o1', [self.points['A']]), ('o2', [self.points['B']]), ('o3', [self.points['C']]), ('o4', [self.points['D']]), ('o5', [self.points['E']]), ('o6', [self.points['F']]), ('o7', [self.points['G']]), ('o8', [self.points['H']]), ('o9', [self.points['O']]), ('o10', [self.points['K']]), ('o11', [self.points['M']]), ('o12', [self.points['U']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['D'], self.points['A']], [1, 2, 2, 2, 79], id='o13')
            c.circle(self.points['O'], 1, id='o14')
            for object_id, points in [('o15', [self.points['B'], self.points['D']]), ('o16', [self.points['A'], self.points['F']]), ('o17', [self.points['K'], self.points['H']])]:
                c.line(points, id=object_id)
            c.text('A', self.points['A'], offset_pt=[-12, -12], vertex=True, id='l1')
            c.text('B', self.points['B'], offset_pt=[-12, 12], vertex=True, id='l2')
            c.text('C', self.points['C'], offset_pt=[12, 12], vertex=True, id='l3')
            c.text('D', self.points['D'], offset_pt=[12, -12], vertex=True, id='l4')
            c.text('E', self.points['E'], offset_pt=[-14, 0], vertex=True, id='l5')
            c.text('F', self.points['F'], offset_pt=[0, 15], vertex=True, id='l6')
            c.text('G', self.points['G'], offset_pt=[14, 0], vertex=True, id='l7')
            c.text('H', self.points['H'], offset_pt=[0, -15], vertex=True, id='l8')
            c.text('O', self.points['O'], offset_pt=[18, 0], vertex=True, id='l9')
            c.text('K', self.points['K'], offset_pt=[0, 25], vertex=True, id='l10')
            c.text('M', self.points['M'], offset_pt=[19, -1], vertex=True, id='l11')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane24().draw(sys.argv[1] if len(sys.argv) > 1 else None))
