"""Frozen question Plane90; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane90:

    def __init__(self):
        self.id = 'Plane90'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:414'
        self.question = 'As shown in the figure, then the angle of circumference angle ACB is equal to ().\nChoices:\nA:130°\nB:120°\nC:110°\nD:100°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '130°', 'B': '120°', 'C': '110°', 'D': '100°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0], 'A': [-1.7207293090531386, 2.457456132866975], 'B': [-2.121320343559643, -2.1213203435596424], 'C': [-3.0, 3.6739403974420594e-16]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane90.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.4230799500369646, 3.1602670796624044], ylim=[-3.291673514849684, 3.291673514849685]) as c:
            c.circle(self.points['O'], 3, id='circle_0')
            for object_id, points in [('segment_1', [self.points['A'], self.points['O']]), ('segment_2', [self.points['O'], self.points['B']]), ('segment_3', [self.points['B'], self.points['C']]), ('segment_4', [self.points['C'], self.points['A']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            c.arc(center, 24, start, end, radius_pt=True, id='angle_arc_5')
            c.text('O', self.points['O'], offset_pt=[4.658742811845373, 17.38666487320323], vertex=True, id='label_0')
            c.text('A', self.points['A'], offset_pt=[-8.999999999999996, 15.588457268119896], vertex=True, id='label_1')
            c.text('B', self.points['B'], offset_pt=[-10.606601717798215, -10.606601717798211], vertex=True, id='label_2')
            c.text('C', self.points['C'], offset_pt=[-15.0, 1.83697019872103e-15], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            offset = direction * 51 + np.array([0, 0])
            c.text('100°', center, offset_pt=offset, id='label_4')
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
    print(Plane90().draw(sys.argv[1] if len(sys.argv) > 1 else None))
