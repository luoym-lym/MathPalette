"""Frozen question Plane87; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane87:

    def __init__(self):
        self.id = 'Plane87'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:239'
        self.question = 'As shown in the figure, then the degree of angle BAC is ()\nChoices:\nA:50°\nB:80°\nC:100°\nD:130°'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '50°', 'B': '80°', 'C': '100°', 'D': '130°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0],
         'B': [-2.298133329356934, -1.9283628290596178],
         'C': [2.2981333293569333, -1.9283628290596186],
         'A': [0.26146722824297364, -2.988584094275237]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane87.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.2890860332654137, 3.2890860332654137], ylim=[-3.4179180749410722, 3.160253991589755]) as c:
            c.circle(self.points['O'], 3, id='circle_0')
            for object_id, points in [('segment_1', [self.points['B'], self.points['O']]), ('segment_2', [self.points['O'], self.points['C']]), ('segment_3', [self.points['C'], self.points['A']]), ('segment_4', [self.points['A'], self.points['B']]), ('segment_5', [self.points['B'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['C'], reflex=False)
            c.arc(center, 25, start, end, radius_pt=True, id='angle_arc_6')
            c.text('O', self.points['O'], offset_pt=[-8, 15], vertex=True, id='label_0')
            c.text('B', self.points['B'], offset_pt=[-13, -9], vertex=True, id='label_1')
            c.text('C', self.points['C'], offset_pt=[17.38666487320323, -4.658742811845372], vertex=True, id='label_2')
            c.text('A', self.points['A'], offset_pt=[5, -16], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['B'], self.points['O'], self.points['C'], reflex=False)
            offset = direction * 52 + np.array([0, 0])
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
    print(Plane87().draw(sys.argv[1] if len(sys.argv) > 1 else None))
