"""Frozen question Plane72; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane72:

    def __init__(self):
        self.id = 'Plane72'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:4'
        self.question = 'As shown in the figure, DE parallel BC, then the size of angle CED is ()\nChoices:\nA:40°\nB:60°\nC:120°\nD:140°'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '40°', 'B': '60°', 'C': '120°', 'D': '140°'}
        self.query = self.question
        self.points = {'B': [0.0, 0.0],
         'C': [8.0, 0.0],
         'A': [2.610814578664558, 4.522063499388545],
         'D': [1.435948018265507, 2.4871349246637],
         'E': [5.035948018265506, 2.4871349246637]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane72.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5253578167892199, 8.538500487741668], ylim=[-2.1832347240083148, 6.880623580522574]) as c:
            for object_id, points in [('segment_0', [self.points['A'], self.points['B']]), ('segment_1', [self.points['B'], self.points['C']]), ('segment_2', [self.points['C'], self.points['A']]), ('segment_3', [self.points['D'], self.points['E']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_4')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_5')
            c.text('B', self.points['B'], offset_pt=[-12, -10], vertex=True, id='label_0')
            c.text('C', self.points['C'], offset_pt=[12, -10], vertex=True, id='label_1')
            c.text('A', self.points['A'], offset_pt=[0, 16], vertex=True, id='label_2')
            c.text('D', self.points['D'], offset_pt=[-16, 0], vertex=True, id='label_3')
            c.text('E', self.points['E'], offset_pt=[14, 7], vertex=True, id='label_4')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 38 + np.array([0, 0])
            c.text('80°', center, offset_pt=offset, id='label_5')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 40 + np.array([0, 0])
            c.text('60°', center, offset_pt=offset, id='label_6')
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
    print(Plane72().draw(sys.argv[1] if len(sys.argv) > 1 else None))
