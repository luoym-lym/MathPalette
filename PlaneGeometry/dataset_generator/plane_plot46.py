"""Frozen question Plane46; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane46:

    def __init__(self):
        self.id = 'Plane46'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/434'
        self.question = 'In the figure above, side AC of triangle ABC is on line l. What is x in terms of k?\nChoices:\nA: 60-k\nB: k\nC: 60+k\nD: 120-k\nE: 120-2*k'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '60-k', 'B': 'k', 'C': '60+k', 'D': '120-k', 'E': '120-2*k'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0], 'B': [1.4037333412861324, 7.960967378027261], 'C': [6.0, 0.0], 'L': [-4.0, 0.0], 'R': [9.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane46.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.323362372585031, 9.687655512927408], ylim=[-2.978853025464166, 11.032164860048272]) as c:
            for object_id, points in [('o1', [self.points['L'], self.points['R']]), ('o2', [self.points['A'], self.points['B']]), ('o3', [self.points['B'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 29, start, end, radius_pt=True, id='o8')
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['B'], reflex=False)
            c.arc(center, 26, start, end, radius_pt=True, id='o10')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['R'], reflex=False)
            c.arc(center, 24, start, end, radius_pt=True, id='o12')
            c.text('A', self.points['A'], offset_pt=[0, -14], vertex=True, id='v4')
            c.text('B', self.points['B'], offset_pt=[0, 14], vertex=True, id='v5')
            c.text('C', self.points['C'], offset_pt=[0, -14], vertex=True, id='v6')
            c.text('l', self.points['R'], offset_pt=[12, 0], vertex=False, id='t7')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 57 + np.array([0, 0])
            c.text('x°', center, offset_pt=offset, id='a9')
            center, direction, start, end = self._angle(self.points['L'], self.points['A'], self.points['B'], reflex=False)
            offset = direction * 80 + np.array([0, 0])
            c.text('(120 − k)°', center, offset_pt=offset, id='a11')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['R'], reflex=False)
            offset = direction * 55 + np.array([0, 0])
            c.text('120°', center, offset_pt=offset, id='a13')
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
    print(Plane46().draw(sys.argv[1] if len(sys.argv) > 1 else None))
