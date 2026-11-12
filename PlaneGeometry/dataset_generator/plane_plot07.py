"""Frozen question Plane07; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane07:

    def __init__(self):
        self.id = 'Plane07'
        self.source_dataset = 'MathVerse'
        self.source_key = 's724'
        self.question = 'As shown in the figure, then the degree of angle BOC is ()\nChoices:\nA:60°\nB:70°\nC:120°\nD:140°'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '60°', 'B': '70°', 'C': '120°', 'D': '140°'}
        self.query = self.question
        self.points = {'O': [0, 0], 'A': [3.061616997868383e-16, 5.0], 'B': [-4.330127018922193, -2.5000000000000004], 'C': [4.92403876506104, -0.868240888334652]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane07.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.316344947097437, 5.652542989934969], ylim=[-5.25810394980927, 5.710783987223136]) as c:
            c.circle(self.points['O'], 5, id='circle')
            c.point([self.points['O']], filled=True, id='point_O')
            for object_id, points in [('OB', [self.points['O'], self.points['B']]), ('OC', [self.points['O'], self.points['C']]), ('AB', [self.points['A'], self.points['B']]), ('AC', [self.points['A'], self.points['C']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['O'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_ABO')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['O'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_ACO')
            c.text('A', self.points['A'], offset_pt=[10.5, 12.0], vertex=True, id='v_A')
            c.text('B', self.points['B'], offset_pt=[-13.5, -7.5], vertex=True, id='v_B')
            c.text('C', self.points['C'], offset_pt=[12.0, -12.0], vertex=True, id='v_C')
            c.text('O', self.points['O'], offset_pt=[15, 15], vertex=True, id='v_O')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['O'], reflex=False)
            offset = direction * 80.0 + np.array([0.0, -9.473903143468002e-15])
            c.text('30°', center, offset_pt=offset, id='given_ABO')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['O'], reflex=False)
            offset = direction * 56.0 + np.array([-2.6611230160570756, -5.222747987755179])
            c.text('40°', center, offset_pt=offset, id='given_ACO')
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
    print(Plane07().draw(sys.argv[1] if len(sys.argv) > 1 else None))
