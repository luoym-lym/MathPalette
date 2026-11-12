"""Frozen question Plane73; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane73:

    def __init__(self):
        self.id = 'Plane73'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:9'
        self.question = 'As shown in the figure, AB parallel CD, EG bisects angle BEF, then angle 2 is equal to ()\nChoices:\nA:50°\nB:60°\nC:65°\nD:90°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '50°', 'B': '60°', 'C': '65°', 'D': '90°'}
        self.query = self.question
        self.points = {'E': [0.0, 3.0],
         'F': [-2.51729889353184, 0.0],
         'G': [1.3989229744649958, 0.0],
         'A': [-5.0, 3.0],
         'B': [5.0, 3.0],
         'C': [-5.0, 0.0],
         'D': [5.0, 0.0],
         'U': [1.7621092254722879, 5.1],
         'V': [-3.524218450944576, -1.2000000000000002],
         'W': [2.2382767591439934, -1.7999999999999998]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane73.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.687908198143201, 5.626003814066203], ylim=[-4.006956006104701, 7.306956006104702]) as c:
            for object_id, points in [('segment_0', [self.points['A'], self.points['B']]), ('segment_1', [self.points['C'], self.points['D']]), ('segment_2', [self.points['V'], self.points['U']]), ('segment_3', [self.points['E'], self.points['W']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['E'], self.points['F'], self.points['G'], reflex=False)
            c.arc(center, 17, start, end, radius_pt=True, id='angle_arc_4')
            center, direction, start, end = self._angle(self.points['F'], self.points['G'], self.points['E'], reflex=False)
            c.arc(center, 19, start, end, radius_pt=True, id='angle_arc_5')
            c.text('E', self.points['E'], offset_pt=[-10, 14], vertex=True, id='label_0')
            c.text('F', self.points['F'], offset_pt=[-3.857637417314163e-15, -21.0], vertex=True, id='label_1')
            c.text('G', self.points['G'], offset_pt=[-10, -16], vertex=True, id='label_2')
            c.text('A', self.points['A'], offset_pt=[-12, -8], vertex=True, id='label_3')
            c.text('B', self.points['B'], offset_pt=[10, -8], vertex=True, id='label_4')
            c.text('C', self.points['C'], offset_pt=[-12, -8], vertex=True, id='label_5')
            c.text('D', self.points['D'], offset_pt=[10, -8], vertex=True, id='label_6')
            center, direction, start, end = self._angle(self.points['E'], self.points['F'], self.points['G'], reflex=False)
            offset = direction * 61 + np.array([4.0, 0.0])
            c.text('1: 50°', center, offset_pt=offset, id='label_7')
            center, direction, start, end = self._angle(self.points['F'], self.points['G'], self.points['E'], reflex=False)
            offset = direction * 34 + np.array([0, 0])
            c.text('2', center, offset_pt=offset, id='label_8')
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
    print(Plane73().draw(sys.argv[1] if len(sys.argv) > 1 else None))
