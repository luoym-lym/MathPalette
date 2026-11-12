"""Frozen question Plane33; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane33:

    def __init__(self):
        self.id = 'Plane33'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/283'
        self.question = '$\\overline{WTY} \\cong \\overline{TWY}$. Find $x$.\nChoices:\nA: 2\nB: 4\nC: 5\nD: 10'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '2', 'B': '4', 'C': '5', 'D': '10'}
        self.query = self.question
        self.points = {'T': [-7.653668647301795, 7.653668647301796],
         'W': [7.653668647301796, 7.653668647301795],
         'Y': [-1.9883222152652114e-15, -10.82392200292394],
         'X': [0.0, 0.0],
         '_t12': [-3.8268343236508984, -1.585126677811072],
         '_t14': [3.826834323650897, -1.5851266778110724]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane33.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-11.82983770014381, 11.82983770014381], ylim=[-12.27794607173334, 11.381729328554282]) as c:
            c.circle(self.points['X'], 10.82392200292394, id='o1')
            for object_id, points in [('o2', [self.points['T'], self.points['Y']]), ('o3', [self.points['W'], self.points['Y']]), ('o4', [self.points['T'], self.points['X']]), ('o5', [self.points['W'], self.points['X']]), ('o6', [self.points['X'], self.points['Y']])]:
                c.line(points, id=object_id)
            c.point([self.points['X']], filled=True, id='o7')
            c.text('T', self.points['T'], offset_pt=[-12, 8], vertex=True, id='v8')
            c.text('W', self.points['W'], offset_pt=[12, 8], vertex=True, id='v9')
            c.text('Y', self.points['Y'], offset_pt=[0, -14], vertex=True, id='v10')
            c.text('X', self.points['X'], offset_pt=[0, 15], vertex=True, id='v11')
            c.text('4x', self.points['_t12'], offset_pt=[-18, 2], vertex=False, id='t13')
            c.text('2x + 10', self.points['_t14'], offset_pt=[50, 0], vertex=False, id='t15')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane33().draw(sys.argv[1] if len(sys.argv) > 1 else None))
