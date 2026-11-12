"""Frozen question Plane53; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane53:

    def __init__(self):
        self.id = 'Plane53'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/690'
        self.question = 'In the diagram above, lines M and N are parallel. All of the following are true except\nChoices:\nA: a + b = j + l\nB: g = h\nC: c + f = f + b\nD: g + e + f + h = 360\nE: d + e = f + j'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'a + b = j + l', 'B': 'g = h', 'C': 'c + f = f + b', 'D': 'g + e + f + h = 360', 'E': 'd + e = f + j'}
        self.query = self.question
        self.points = {'L': [0.0, 1.3],
         'O': [2.0, 0.0],
         'R': [4.0, 1.3],
         'Lu': [0.0, 2.3],
         'Ld': [0.0, 0.30000000000000004],
         'Ll': [-1.0, 1.9500000000000002],
         'Lr': [1.0, 0.65],
         'Ru': [4.0, 2.3],
         'Rd': [4.0, 0.30000000000000004],
         'Rl': [3.0, 0.65],
         'Rr': [5.0, 1.9500000000000002],
         'Oul': [1.0, 0.65],
         'Our': [3.0, 0.65],
         'Odl': [1.0, -0.65],
         'Odr': [3.0, -0.65]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane53.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.6700114343413626, 6.670011434341363], ylim=[-4.234500880138569, 5.105521988544156]) as c:
            for object_id, points in [('segment_1', [[-2, 2.6], [6, -2.6]]), ('segment_2', [[-1.5, -2.275], [6, 2.6]]), ('segment_3', [[0, -4], [0, 4]]), ('segment_4', [[4, -3.5], [4, 4.5]])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['Lu'], self.points['L'], self.points['Ll'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_7')
            center, direction, start, end = self._angle(self.points['Lu'], self.points['L'], self.points['Lr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_9')
            center, direction, start, end = self._angle(self.points['Ld'], self.points['L'], self.points['Ll'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_11')
            center, direction, start, end = self._angle(self.points['Ld'], self.points['L'], self.points['Lr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_13')
            center, direction, start, end = self._angle(self.points['Ru'], self.points['R'], self.points['Rl'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_15')
            center, direction, start, end = self._angle(self.points['Ru'], self.points['R'], self.points['Rr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_17')
            center, direction, start, end = self._angle(self.points['Rd'], self.points['R'], self.points['Rl'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_19')
            center, direction, start, end = self._angle(self.points['Rd'], self.points['R'], self.points['Rr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_21')
            center, direction, start, end = self._angle(self.points['Oul'], self.points['O'], self.points['Odl'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_23')
            center, direction, start, end = self._angle(self.points['Our'], self.points['O'], self.points['Odr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_25')
            center, direction, start, end = self._angle(self.points['Oul'], self.points['O'], self.points['Our'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_27')
            center, direction, start, end = self._angle(self.points['Odl'], self.points['O'], self.points['Odr'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc_29')
            c.text('M', [0, 4], offset_pt=[0, 14], vertex=False, id='label_5')
            c.text('N', [4, 4.5], offset_pt=[0, 14], vertex=False, id='label_6')
            center, direction, start, end = self._angle(self.points['Lu'], self.points['L'], self.points['Ll'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('a', center, offset_pt=offset, id='angle_label_8')
            center, direction, start, end = self._angle(self.points['Lu'], self.points['L'], self.points['Lr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('b', center, offset_pt=offset, id='angle_label_10')
            center, direction, start, end = self._angle(self.points['Ld'], self.points['L'], self.points['Ll'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('c', center, offset_pt=offset, id='angle_label_12')
            center, direction, start, end = self._angle(self.points['Ld'], self.points['L'], self.points['Lr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('d', center, offset_pt=offset, id='angle_label_14')
            center, direction, start, end = self._angle(self.points['Ru'], self.points['R'], self.points['Rl'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('i', center, offset_pt=offset, id='angle_label_16')
            center, direction, start, end = self._angle(self.points['Ru'], self.points['R'], self.points['Rr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('k', center, offset_pt=offset, id='angle_label_18')
            center, direction, start, end = self._angle(self.points['Rd'], self.points['R'], self.points['Rl'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('j', center, offset_pt=offset, id='angle_label_20')
            center, direction, start, end = self._angle(self.points['Rd'], self.points['R'], self.points['Rr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('l', center, offset_pt=offset, id='angle_label_22')
            center, direction, start, end = self._angle(self.points['Oul'], self.points['O'], self.points['Odl'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('e', center, offset_pt=offset, id='angle_label_24')
            center, direction, start, end = self._angle(self.points['Our'], self.points['O'], self.points['Odr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('f', center, offset_pt=offset, id='angle_label_26')
            center, direction, start, end = self._angle(self.points['Oul'], self.points['O'], self.points['Our'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('g', center, offset_pt=offset, id='angle_label_28')
            center, direction, start, end = self._angle(self.points['Odl'], self.points['O'], self.points['Odr'], reflex=False)
            offset = direction * 29 + np.array([0, 0])
            c.text('h', center, offset_pt=offset, id='angle_label_30')
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
    print(Plane53().draw(sys.argv[1] if len(sys.argv) > 1 else None))
