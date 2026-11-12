"""Frozen question Plane93; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane93:

    def __init__(self):
        self.id = 'Plane93'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:514'
        self.question = 'As shown in the figure, then angle AOC = ()\nChoices:\nA:100°\nB:110°\nC:120°\nD:130°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '100°', 'B': '110°', 'C': '120°', 'D': '130°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0], 'A': [-2.298133329356934, -1.9283628290596178], 'B': [-5.51091059616309e-16, -3.0], 'C': [2.2981333293569333, -1.9283628290596186]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane93.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.287914199491929, 3.28791419949193], ylim=[-3.415633599461695, 3.1601947995221638]) as c:
            c.point([self.points['O']], filled=True, id='point_0')
            c.circle(self.points['O'], 3, id='circle_1')
            for object_id, points in [('segment_2', [self.points['A'], self.points['O']]), ('segment_3', [self.points['O'], self.points['C']]), ('segment_4', [self.points['C'], self.points['B']]), ('segment_5', [self.points['B'], self.points['A']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 23, start, end, radius_pt=True, id='angle_arc_6')
            c.text('O', self.points['O'], offset_pt=[0, 17], vertex=True, id='label_0')
            c.text('A', self.points['A'], offset_pt=[-11.49066664678467, -9.641814145298088], vertex=True, id='label_1')
            c.text('B', self.points['B'], offset_pt=[-2.7554552980815444e-15, -15.0], vertex=True, id='label_2')
            c.text('C', self.points['C'], offset_pt=[11.490666646784668, -9.641814145298094], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 52 + np.array([0, 0])
            c.text('130°', center, offset_pt=offset, id='label_4')
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
    print(Plane93().draw(sys.argv[1] if len(sys.argv) > 1 else None))
