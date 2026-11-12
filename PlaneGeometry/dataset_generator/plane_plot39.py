"""Frozen question Plane39; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane39:

    def __init__(self):
        self.id = 'Plane39'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/342'
        self.question = 'In the figure above, which of the following is the greatest?\nChoices:\nA: a\nB: b\nC: c\nD: d\nE: e'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0],
         'B': [6.0, 0.0],
         'C': [3.680044790717034, 6.374024551651077],
         'L': [-2.5, 0.0],
         'R': [8.5, 0.0],
         'D': [-1.0000000000000002, -1.7320508075688772],
         'U': [4.580044790717034, 7.932870278463067]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane39.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.771358204134367, 8.795229731912144], ylim=[-2.6828842325761606, 8.883703703470351]) as c:
            for object_id, points in [('o1', [self.points['L'], self.points['R']]), ('o2', [self.points['D'], self.points['U']]), ('o3', [self.points['B'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['D'], reflex=False)
            c.arc(center, 22, start, end, radius_pt=True, id='o4')
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='o6')
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['B'], reflex=False)
            c.arc(center, 22, start, end, radius_pt=True, id='o8')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 21, start, end, radius_pt=True, id='o10')
            center, direction, start, end = self._angle(self.points['C'], self.points['B'], self.points['R'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='o12')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 25, start, end, radius_pt=True, id='o14')
            center, direction, start, end = self._angle(self.points['U'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='o16')
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['D'], reflex=False)
            offset = direction * 41 + np.array([0, 0])
            c.text('a°', center, offset_pt=offset, id='a5')
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 38 + np.array([0, 0])
            c.text('b°', center, offset_pt=offset, id='a7')
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['B'], reflex=False)
            offset = direction * 43 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='a9')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 41 + np.array([0, 0])
            c.text('70°', center, offset_pt=offset, id='a11')
            center, direction, start, end = self._angle(self.points['C'], self.points['B'], self.points['R'], reflex=False)
            offset = direction * 40 + np.array([0, 0])
            c.text('e°', center, offset_pt=offset, id='a13')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 47 + np.array([0, 0])
            c.text('c°', center, offset_pt=offset, id='a15')
            center, direction, start, end = self._angle(self.points['U'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 38 + np.array([0, 0])
            c.text('d°', center, offset_pt=offset, id='a17')
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
    print(Plane39().draw(sys.argv[1] if len(sys.argv) > 1 else None))
