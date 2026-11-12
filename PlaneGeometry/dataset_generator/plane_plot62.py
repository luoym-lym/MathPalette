"""Frozen question Plane62; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane62:

    def __init__(self):
        self.id = 'Plane62'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/798'
        self.question = 'In the figure above, l || m. Which of the following must equal 180?\nChoices:\nA: k + n + r\nB: k + p + s\nC: n + p + s\nD: n + p + t\nE: r + s + t'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'k + n + r', 'B': 'k + p + s', 'C': 'n + p + s', 'D': 'n + p + t', 'E': 'r + s + t'}
        self.query = self.question
        self.points = {'O': [0.0, 3.0],
         'lL': [-3.0, 3.0],
         'lR': [3.0, 3.0],
         'mL': [-3.0, 0.0],
         'mR': [3.0, 0.0],
         'U': [-1.0, 5.0],
         'V': [1.0, 5.0],
         'X': [-2.5, -2.0],
         'Y': [2.5, -2.0],
         'B': [-1.5, 0.0],
         'C': [1.5, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane62.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.5407668602494526, 3.808085467550203], ylim=[-2.174426163899828, 5.1744261638998275]) as c:
            for object_id, points in [('segment1', [self.points['lL'], self.points['lR']]), ('segment2', [self.points['mL'], self.points['mR']]), ('segment3', [self.points['U'], self.points['Y']]), ('segment4', [self.points['V'], self.points['X']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['lL'], self.points['O'], self.points['U'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc8')
            center, direction, start, end = self._angle(self.points['lL'], self.points['O'], self.points['B'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc10')
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['C'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc12')
            center, direction, start, end = self._angle(self.points['C'], self.points['O'], self.points['lR'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc14')
            center, direction, start, end = self._angle(self.points['O'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc16')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['O'], reflex=False)
            c.arc(center, 14, start, end, radius_pt=True, id='angle_arc18')
            c.text('ℓ', self.points['lR'], offset_pt=[12, 0], vertex=False, id='text5')
            c.text('m', self.points['mR'], offset_pt=[12, 0], vertex=False, id='text6')
            center, direction, start, end = self._angle(self.points['lL'], self.points['O'], self.points['U'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('s°', center, offset_pt=offset, id='anglelabel9')
            center, direction, start, end = self._angle(self.points['lL'], self.points['O'], self.points['B'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('r°', center, offset_pt=offset, id='anglelabel11')
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['C'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('p°', center, offset_pt=offset, id='anglelabel13')
            center, direction, start, end = self._angle(self.points['C'], self.points['O'], self.points['lR'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('t°', center, offset_pt=offset, id='anglelabel15')
            center, direction, start, end = self._angle(self.points['O'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('k°', center, offset_pt=offset, id='anglelabel17')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['O'], reflex=False)
            offset = direction * 28 + np.array([0, 0])
            c.text('n°', center, offset_pt=offset, id='anglelabel19')
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
    print(Plane62().draw(sys.argv[1] if len(sys.argv) > 1 else None))
