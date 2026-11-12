"""Frozen question Plane138; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane138:

    def __init__(self):
        self.id = 'Plane138'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:894'
        self.question = 'As shown in the figure, PB = AB, then the length of PA is ( )\nChoices:\nA:5\nB:\\frac{5√{3}}{2}\nC:5√{2}\nD:5√{3}'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '5', 'B': '\\frac{5√{3}}{2}', 'C': '5√{2}', 'D': '5√{3}'}
        self.query = self.question
        self.points = {'O': [0, 0],
         'A': [-2.499999999999999, -4.330127018922194],
         'B': [2.5000000000000004, -4.330127018922193],
         'P': [5.0, 0.0],
         'C': [-3.8302222155948895, 3.2139380484326976],
         'T': [1.7101007166283442, 4.698463103929542]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane138.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.257809274684361, 5.715027999837104], ylim=[-5.486418637260733, 5.486418637260733]) as c:
            c.circle(self.points['O'], 5, id='o0')
            for object_id, points in [('o1', [self.points['C'], self.points['A']]), ('o2', [self.points['C'], self.points['B']]), ('o3', [self.points['A'], self.points['B']]), ('o4', [self.points['A'], self.points['P']]), ('o5', [self.points['B'], self.points['P']]), ('o6', [self.points['O'], self.points['T']])]:
                c.line(points, id=object_id)
            c.point([self.points['O']], filled=True, id='o7')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='o8')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 58 + np.array([5.071419140888398, -10.875693444439797])
            c.text('30°', center, offset_pt=offset, id='l0')
            c.text('5', [0.8550503583141721, 2.349231551964771], offset_pt=[-16, 2], vertex=False, id='l1')
            c.text('O', self.points['O'], offset_pt=[-13, 0], vertex=True, id='l2')
            c.text('A', self.points['A'], offset_pt=[-8, -14], vertex=True, id='l3')
            c.text('B', self.points['B'], offset_pt=[8, -14], vertex=True, id='l4')
            c.text('C', self.points['C'], offset_pt=[-12, 6], vertex=True, id='l5')
            c.text('P', self.points['P'], offset_pt=[15, 0], vertex=True, id='l6')
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
    print(Plane138().draw(sys.argv[1] if len(sys.argv) > 1 else None))
