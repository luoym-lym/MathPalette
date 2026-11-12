"""Frozen question Plane01; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane01:

    def __init__(self):
        self.id = 'Plane01'
        self.source_dataset = 'MathVerse'
        self.source_key = 's34'
        self.question = 'As shown in the figure, triangle ABC congruent triangle ADE, then the degree of angle EAC is ()\nChoices:\nA:40°\nB:45°\nC:35°\nD:25°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '40°', 'B': '45°', 'C': '35°', 'D': '25°'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0],
         'B': [-2.2943057454041846, 3.2766081771559668],
         'C': [5.315704195109398, 5.315704195109398],
         'D': [0.6945927106677217, 3.939231012048832],
         'E': [7.517540966287267, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane01.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.9467026058628965, 8.164241680979984], ylim=[-2.8769955683043538, 8.233948718538526]) as c:
            for object_id, points in [('AB', [self.points['A'], self.points['B']]), ('BC', [self.points['B'], self.points['C']]), ('AC', [self.points['A'], self.points['C']]), ('AD', [self.points['A'], self.points['D']]), ('DE', [self.points['D'], self.points['E']]), ('AE', [self.points['A'], self.points['E']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_B')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['A'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_C')
            center, direction, start, end = self._angle(self.points['D'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_DAC')
            c.text('A', self.points['A'], offset_pt=[-12.0, -13.5], vertex=True, id='label_A')
            c.text('B', self.points['B'], offset_pt=[-12.0, 12.0], vertex=True, id='label_B')
            c.text('C', self.points['C'], offset_pt=[10.5, 12.0], vertex=True, id='label_C')
            c.text('D', self.points['D'], offset_pt=[10, -19.5], vertex=True, id='label_D')
            c.text('E', self.points['E'], offset_pt=[12.0, -12.0], vertex=True, id='label_E')
            center, direction, start, end = self._angle(self.points['A'], self.points['B'], self.points['C'], reflex=False)
            offset = direction * 64.0 + np.array([3.8499247597109063, 23.006243184828904])
            c.text('70°', center, offset_pt=offset, id='given_B')
            center, direction, start, end = self._angle(self.points['B'], self.points['C'], self.points['A'], reflex=False)
            offset = direction * 80.0 + np.array([9.473903143468002e-15, 0.0])
            c.text('30°', center, offset_pt=offset, id='given_C')
            center, direction, start, end = self._angle(self.points['D'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 64.0 + np.array([-9.473903143468002e-15, 0.0])
            c.text('35°', center, offset_pt=offset, id='given_DAC')
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
    print(Plane01().draw(sys.argv[1] if len(sys.argv) > 1 else None))
