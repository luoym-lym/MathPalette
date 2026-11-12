"""Frozen question Plane70; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane70:

    def __init__(self):
        self.id = 'Plane70'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/951'
        self.question = 'Find $x$.\nChoices:\nA: 10.25\nB: 12.75\nC: 18.75\nD: 25.5'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '10.25', 'B': '12.75', 'C': '18.75', 'D': '25.5'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0], 'C': [-0.785316930880745, -0.619093949309834], 'E': [0.785316930880745, 0.619093949309834], 'D': [-0.785316930880745, 0.619093949309834]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane70.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0505995639534884, 1.0505995639534884], ylim=[-1.0505995639534884, 1.0505995639534884]) as c:
            c.point([self.points['O']], filled=True, id='point1')
            c.circle(self.points['O'], 1, id='circle5')
            for object_id, points in [('segment9', [self.points['C'], self.points['D']]), ('segment10', [self.points['D'], self.points['E']]), ('segment11', [self.points['E'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['D'], self.points['E'], self.points['C'], reflex=False)
            c.arc(center, 23, start, end, radius_pt=True, id='angle_arc12')
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['E'], reflex=False)
            c.arc(center, 30, start, end, radius_pt=True, id='angle_arc14')
            c.text('C', self.points['C'], offset_pt=[-13, -10], vertex=True, id='label2')
            c.text('E', self.points['E'], offset_pt=[14, 10], vertex=True, id='label3')
            c.text('D', self.points['D'], offset_pt=[-13, 10], vertex=True, id='label4')
            center, direction, start, end = self._angle(self.points['D'], self.points['E'], self.points['C'], reflex=False)
            offset = direction * 54 + np.array([0, 0])
            c.text('3x°', center, offset_pt=offset, id='anglelabel13')
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['E'], reflex=False)
            offset = direction * 125 + np.array([0, 0])
            c.text('(5x − 12)°', center, offset_pt=offset, id='anglelabel15')
            return c if _canvas else c.save(output_path)

    @staticmethod
    def _angle(a, vertex, b, reflex=False):
        center = np.asarray(vertex, dtype=float)
        u, v = (np.asarray(a) - center, np.asarray(b) - center)
        u, v = (u / np.linalg.norm(u), v / np.linalg.norm(v))
        start, end = (np.degrees(np.arctan2(u[1], u[0])), np.degrees(np.arctan2(v[1], v[0])))
        sweep = (end - start) % 360
        if sweep > 180:
            start, sweep = (end, 360 - sweep)
        if reflex:
            start, sweep = (start + sweep, 360 - sweep)
        middle = np.radians(start + sweep / 2)
        return (center, np.array([np.cos(middle), np.sin(middle)]), start, start + sweep)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane70().draw(sys.argv[1] if len(sys.argv) > 1 else None))
