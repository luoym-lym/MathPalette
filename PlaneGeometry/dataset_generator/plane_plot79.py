"""Frozen question Plane79; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane79:

    def __init__(self):
        self.id = 'Plane79'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:54'
        self.question = 'In the figure, F is the intersection of AD and BC, and angle CAD equals angle BAE. Find the measure of angle AFC.\nChoices:\nA:84°\nB:80°\nC:60°\nD:90°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '84°', 'B': '80°', 'C': '60°', 'D': '90°'}
        self.query = self.question
        self.points = {'A': [3.0, 0.0],
         'E': [-0.2139380484326976, -3.8302222155948895],
         'D': [-0.21393804843269804, 3.213938048432699],
         'C': [4.294095225512604, 4.8296291314453415],
         'B': [-0.834955118715996, 0.6762060572356641],
         'F': [0.9104183642757016, 2.089581635724299]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane79.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.2925920508609208, 6.605123789184431], ylim=[-4.392808859276525, 5.504906980768827]) as c:
            for object_id, points in [('segment_0', [self.points['D'], self.points['E']]), ('segment_1', [self.points['E'], self.points['A']]), ('segment_2', [self.points['A'], self.points['D']]), ('segment_3', [self.points['A'], self.points['B']]), ('segment_4', [self.points['B'], self.points['C']]), ('segment_5', [self.points['C'], self.points['A']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['E'], reflex=False)
            c.arc(center, 22, start, end, radius_pt=True, id='angle_arc_6')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='angle_arc_7')
            c.text('A', self.points['A'], offset_pt=[13, -10], vertex=True, id='label_0')
            c.text('E', self.points['E'], offset_pt=[-12, -12], vertex=True, id='label_1')
            c.text('D', self.points['D'], offset_pt=[-10, 14], vertex=True, id='label_2')
            c.text('C', self.points['C'], offset_pt=[8, 14], vertex=True, id='label_3')
            c.text('B', self.points['B'], offset_pt=[-16, 0], vertex=True, id='label_4')
            c.text('F', self.points['F'], offset_pt=[1.102182119232618e-15, 18.0], vertex=True, id='label_5')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['E'], reflex=False)
            offset = direction * 53 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='label_6')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 60 + np.array([0.0, 0.0])
            c.text('36°', center, offset_pt=offset, id='label_7')
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
    print(Plane79().draw(sys.argv[1] if len(sys.argv) > 1 else None))
