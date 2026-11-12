"""Frozen question Plane88; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane88:

    def __init__(self):
        self.id = 'Plane88'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:279'
        self.question = 'As shown in the figure, the diameter CD of circle O crosses the midpoint G of chord EF, then angle EOD is equal to ()\nChoices:\nA:10°\nB:20°\nC:40°\nD:80°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '10°', 'B': '20°', 'C': '40°', 'D': '80°'}
        self.query = self.question
        self.points = {'O': [0.0, 0.0],
         'C': [0.0, 3.0],
         'D': [0.0, -3.0],
         'E': [-1.9283628290596184, -2.2981333293569337],
         'F': [1.9283628290596178, -2.2981333293569346],
         'G': [0.0, -2.298133329356934]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane88.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.4773886582626967, 3.4773886582626967], ylim=[-3.451945794164467, 3.5028315223609265]) as c:
            c.point([self.points['O']], filled=True, id='point_0')
            c.circle(self.points['O'], 3, id='circle_1')
            for object_id, points in [('segment_2', [self.points['C'], self.points['D']]), ('segment_3', [self.points['E'], self.points['F']]), ('segment_4', [self.points['O'], self.points['E']]), ('segment_5', [self.points['C'], self.points['F']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['F'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='angle_arc_6')
            c.text('O', self.points['O'], offset_pt=[-17.386664873203227, 4.658742811845379], vertex=True, id='label_0')
            c.text('C', self.points['C'], offset_pt=[0, 16], vertex=True, id='label_1')
            c.text('D', self.points['D'], offset_pt=[0, -16], vertex=True, id='label_2')
            c.text('E', self.points['E'], offset_pt=[-13, -9], vertex=True, id='label_3')
            c.text('F', self.points['F'], offset_pt=[13, -9], vertex=True, id='label_4')
            c.text('G', self.points['G'], offset_pt=[13, 14], vertex=True, id='label_5')
            center, direction, start, end = self._angle(self.points['D'], self.points['C'], self.points['F'], reflex=False)
            offset = direction * 98 + np.array([0.0, -4.0])
            c.text('20°', center, offset_pt=offset, id='label_6')
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
    print(Plane88().draw(sys.argv[1] if len(sys.argv) > 1 else None))
