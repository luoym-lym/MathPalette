"""Frozen question Plane23; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane23:

    def __init__(self):
        self.id = 'Plane23'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/88'
        self.question = 'A square is tangent to a line at point P in the figure above. What is the value of x?'
        self.answer = '30'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P': [0.0, 0.0],
         'U': [-3.464101615137755, 1.9999999999999998],
         'V': [2.0000000000000004, 3.4641016151377544],
         'W': [-1.4641016151377544, 5.464101615137754],
         'L': [-6.0, 0.0],
         'R': [5.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane23.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.289678863017406, 5.620445565516598], ylim=[-3.458492035860362, 8.451632392673643]) as c:
            c.path([self.points['P'], self.points['U'], self.points['W'], self.points['V'], self.points['P']], [1, 2, 2, 2, 79], id='o1')
            c.line([self.points['L'], self.points['R']], id='o2')
            center, direction, start, end = self._angle(self.points['L'], self.points['P'], self.points['U'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='o3')
            center, direction, start, end = self._angle(self.points['V'], self.points['P'], self.points['R'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='o4')
            c.text('P', self.points['P'], offset_pt=[0, -15], vertex=True, id='l1')
            c.text('l', self.points['R'], offset_pt=[13, 0], vertex=False, id='l2')
            center, direction, start, end = self._angle(self.points['L'], self.points['P'], self.points['U'], reflex=False)
            offset = direction * 46 + np.array([0, 0])
            c.text('x°', center, offset_pt=offset, id='l3')
            center, direction, start, end = self._angle(self.points['V'], self.points['P'], self.points['R'], reflex=False)
            offset = direction * 42 + np.array([0, 0])
            c.text('2x°', center, offset_pt=offset, id='l4')
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
    print(Plane23().draw(sys.argv[1] if len(sys.argv) > 1 else None))
