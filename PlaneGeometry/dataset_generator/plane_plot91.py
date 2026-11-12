"""Frozen question Plane91; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane91:

    def __init__(self):
        self.id = 'Plane91'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:439'
        self.question = 'As shown in the figure, then angle BOC is equal to ()\nChoices:\nA:128°\nB:108°\nC:86°\nD:64°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '128°', 'B': '108°', 'C': '86°', 'D': '64°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0], 'A': [1.8369701987210297e-16, 3.0], 'C': [-2.9835656861048196, -0.31358538980296047], 'B': [2.0839751113769918, -2.1580194010159537]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane91.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.4365903795858816, 3.1894351827490004], ylim=[-3.161310292041075, 3.464715270293807]) as c:
            c.point([self.points['O']], filled=True, id='point_0')
            c.circle(self.points['O'], 3, id='circle_1')
            for object_id, points in [('segment_2', [self.points['C'], self.points['A']]), ('segment_3', [self.points['A'], self.points['B']]), ('segment_4', [self.points['B'], self.points['O']]), ('segment_5', [self.points['O'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['O'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_6')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['O'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_7')
            c.text('O', self.points['O'], offset_pt=[0, 17], vertex=True, id='label_0')
            c.text('A', self.points['A'], offset_pt=[9.18485099360515e-16, 15.0], vertex=True, id='label_1')
            c.text('C', self.points['C'], offset_pt=[-14.9178284305241, -1.5679269490148025], vertex=True, id='label_2')
            c.text('B', self.points['B'], offset_pt=[10.419875556884959, -10.790097005079767], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['O'], reflex=False)
            offset = direction * 64 + np.array([0, 0])
            c.text('42°', center, offset_pt=offset, id='label_4')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['O'], reflex=False)
            offset = direction * 100 + np.array([0.0, 0.0])
            c.text('22°', center, offset_pt=offset, id='label_5')
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
    print(Plane91().draw(sys.argv[1] if len(sys.argv) > 1 else None))
