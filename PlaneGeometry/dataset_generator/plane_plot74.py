"""Frozen question Plane74; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane74:

    def __init__(self):
        self.id = 'Plane74'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:14'
        self.question = 'As shown in the figure, BD bisects angle ABC, CD parallel AB, then the degree of angle CDB is ()\nChoices:\nA:55°\nB:50°\nC:45°\nD:30°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '55°', 'B': '50°', 'C': '45°', 'D': '30°'}
        self.query = self.question
        self.points = {'C': [0.0, 0.0], 'B': [6.0, 0.0], 'D': [2.052120859954013, 5.63815572471545], 'A': [7.3680805733026755, 3.7587704831436333], 'L': [-1.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane74.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.221718424060613, 7.8849706131194655], ylim=[-1.701254716542655, 7.405434320637424]) as c:
            for object_id, points in [('segment_0', [self.points['L'], self.points['B']]), ('segment_1', [self.points['C'], self.points['D']]), ('segment_2', [self.points['D'], self.points['B']]), ('segment_3', [self.points['B'], self.points['A']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_4')
            c.text('C', self.points['C'], offset_pt=[-5, -16], vertex=True, id='label_0')
            c.text('B', self.points['B'], offset_pt=[6, -16], vertex=True, id='label_1')
            c.text('D', self.points['D'], offset_pt=[-5, 16], vertex=True, id='label_2')
            c.text('A', self.points['A'], offset_pt=[12, 6], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 41 + np.array([0, 0])
            c.text('70°', center, offset_pt=offset, id='label_4')
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
    print(Plane74().draw(sys.argv[1] if len(sys.argv) > 1 else None))
