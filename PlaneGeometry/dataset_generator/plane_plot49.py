"""Frozen question Plane49; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane49:

    def __init__(self):
        self.id = 'Plane49'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/610'
        self.question = 'In the figure above, P, Q, and R lie on the same line. P is the center of the larger circle, and Q is the center of the smaller circle. If the radius of the larger circle is 4, what is the radius of the smaller circle?\nChoices:\nA: 1\nB: 2\nC: 4\nD: 8\nE: 16'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1', 'B': '2', 'C': '4', 'D': '8', 'E': '16'}
        self.query = self.question
        self.points = {'P': [0.0, 0.0], 'Q': [2.0, 0.0], 'R': [4.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane49.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.205403190623847, 4.530622615778168], ylim=[-4.3680129032010075, 4.3680129032010075]) as c:
            c.circle(self.points['P'], 4, id='circle_1')
            c.circle(self.points['Q'], 2, id='circle_2')
            for object_id, points in [('point_3', [self.points['P']]), ('point_4', [self.points['Q']]), ('point_5', [self.points['R']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[-15, 0], vertex=True, id='name_P')
            c.text('Q', self.points['Q'], offset_pt=[0, -16], vertex=True, id='name_Q')
            c.text('R', self.points['R'], offset_pt=[14, 0], vertex=True, id='name_R')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane49().draw(sys.argv[1] if len(sys.argv) > 1 else None))
