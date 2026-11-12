"""Frozen question Plane84; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane84:

    def __init__(self):
        self.id = 'Plane84'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:144'
        self.question = 'As shown in the figure, D is the intersection point of the angular bisector BD and CD of triangle ABC. then angle D = ()\nChoices:\nA:120°\nB:130°\nC:115°\nD:110°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '120°', 'B': '130°', 'C': '115°', 'D': '110°'}
        self.query = self.question
        self.points = {'B': [0.0, 0.0], 'C': [7.0, 0.0], 'A': [7.0, 5.873697418240959], 'D': [5.132076803542494, 1.8679231964575047]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane84.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.49393414570520955, 7.473368077484716], ylim=[-0.969742678582834, 6.997559544607093]) as c:
            for object_id, points in [('segment_0', [self.points['A'], self.points['B']]), ('segment_1', [self.points['B'], self.points['C']]), ('segment_2', [self.points['C'], self.points['A']]), ('segment_3', [self.points['B'], self.points['D']]), ('segment_4', [self.points['D'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_5')
            c.text('B', self.points['B'], offset_pt=[-14, -10], vertex=True, id='label_0')
            c.text('C', self.points['C'], offset_pt=[12, -11], vertex=True, id='label_1')
            c.text('A', self.points['A'], offset_pt=[3, 17], vertex=True, id='label_2')
            c.text('D', self.points['D'], offset_pt=[0, 16], vertex=True, id='label_3')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 44 + np.array([0, 0])
            c.text('50°', center, offset_pt=offset, id='label_4')
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
    print(Plane84().draw(sys.argv[1] if len(sys.argv) > 1 else None))
