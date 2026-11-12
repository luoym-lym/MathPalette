"""Frozen question Plane36; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane36:

    def __init__(self):
        self.id = 'Plane36'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/304'
        self.question = 'In the figure above, two line segments meet at a point on line l. If the value of y is equal to the square of the value of x, what is the value of y?'
        self.answer = '100'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0], 'L': [-7.0, 0.0], 'R': [7.0, 0.0], 'A': [-4.92403876506104, 0.8682408883346514], 'B': [1.7101007166283442, 4.698463103929542]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane36.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-7.348236401245417, 7.740552090844901], ylim=[-5.249037653705711, 9.839750838384607]) as c:
            for object_id, points in [('o1', [self.points['L'], self.points['R']]), ('o2', [self.points['O'], self.points['A']]), ('o3', [self.points['O'], self.points['B']])]:
                c.line(points, id=object_id)
            c.point([self.points['O']], filled=True, id='o4')
            center, direction, start, end = self._angle(self.points['L'], self.points['O'], self.points['A'], reflex=False)
            c.arc(center, 70, start, end, radius_pt=True, id='o6')
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            c.arc(center, 30, start, end, radius_pt=True, id='o8')
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['R'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='o10')
            c.text('l', self.points['R'], offset_pt=[12, 0], vertex=False, id='t5')
            center, direction, start, end = self._angle(self.points['L'], self.points['O'], self.points['A'], reflex=False)
            offset = direction * 145 + np.array([0, 0])
            c.text('x°', center, offset_pt=offset, id='a7')
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            offset = direction * 55 + np.array([0, 0])
            c.text('y°', center, offset_pt=offset, id='a9')
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['R'], reflex=False)
            offset = direction * 49 + np.array([0, 0])
            c.text('70°', center, offset_pt=offset, id='a11')
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
    print(Plane36().draw(sys.argv[1] if len(sys.argv) > 1 else None))
