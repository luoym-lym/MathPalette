"""Frozen question Plane64; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane64:

    def __init__(self):
        self.id = 'Plane64'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/815'
        self.question = 'Find $m \\angle N C L$\nChoices:\nA: 60\nB: 120\nC: 240\nD: 360'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '60', 'B': '120', 'C': '240', 'D': '360'}
        self.query = self.question
        self.points = {'C': [0.0, 0.0],
         'R': [-0.5591929034707467, 0.8290375725550417],
         'M': [0.17364817766693041, 0.984807753012208],
         'N': [0.9396926207859084, 0.3420201433256687],
         'L': [-0.17364817766693033, -0.984807753012208]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane64.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1159946241528362, 1.1495270551121384], ylim=[-1.1266161607625744, 1.1389055185024002]) as c:
            c.point([self.points['C']], filled=True, id='point2')
            for object_id, points in [('segment4', [self.points['C'], self.points['R']]), ('segment6', [self.points['C'], self.points['M']]), ('segment8', [self.points['C'], self.points['N']]), ('segment10', [self.points['C'], self.points['L']])]:
                c.line(points, id=object_id)
            c.circle(self.points['C'], 1, id='circle11')
            center, direction, start, end = self._angle(self.points['M'], self.points['C'], self.points['N'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='angle_arc16')
            center, direction, start, end = self._angle(self.points['R'], self.points['C'], self.points['M'], reflex=False)
            c.arc(center, 32, start, end, radius_pt=True, id='angle_arc18')
            center, direction, start, end = self._angle(self.points['R'], self.points['C'], self.points['L'], reflex=False)
            c.arc(center, 45, start, end, radius_pt=True, id='angle_arc20')
            c.text('C', self.points['C'], offset_pt=[10, -10], vertex=True, id='label1')
            c.text('R', self.points['R'], offset_pt=[-8.3878935520612, 12.435563588325627], vertex=True, id='label3')
            c.text('M', self.points['M'], offset_pt=[2.604722665003956, 14.772116295183121], vertex=True, id='label5')
            c.text('N', self.points['N'], offset_pt=[14.095389311788626, 5.130302149885031], vertex=True, id='label7')
            c.text('L', self.points['L'], offset_pt=[-2.6047226650039548, -14.772116295183121], vertex=True, id='label9')
            center, direction, start, end = self._angle(self.points['M'], self.points['C'], self.points['N'], reflex=False)
            offset = direction * 43 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='anglelabel17')
            center, direction, start, end = self._angle(self.points['R'], self.points['C'], self.points['M'], reflex=False)
            offset = direction * 105 + np.array([0, 0])
            c.text('(x − 1)°', center, offset_pt=offset, id='anglelabel19')
            center, direction, start, end = self._angle(self.points['R'], self.points['C'], self.points['L'], reflex=False)
            offset = direction * 96 + np.array([0, 0])
            c.text('(3x + 5)°', center, offset_pt=offset, id='anglelabel21')
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
    print(Plane64().draw(sys.argv[1] if len(sys.argv) > 1 else None))
