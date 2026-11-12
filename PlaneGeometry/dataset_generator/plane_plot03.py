"""Frozen question Plane03; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane03:

    def __init__(self):
        self.id = 'Plane03'
        self.source_dataset = 'MathVerse'
        self.source_key = 's244'
        self.question = 'As shown in the figure, in the inscribed pentagon ABCDE of circle O, find the measure of angle B: ____.'
        self.answer = '95°'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0],
         'A': [3.061616997868383e-16, 5.0],
         'E': [4.330127018922194, 2.4999999999999996],
         'D': [3.83022221559489, -3.2139380484326963],
         'C': [-0.8682408883346515, -4.92403876506104],
         'B': [-4.330127018922194, -2.4999999999999996]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane03.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.708553134718092, 5.708553134718092], ylim=[-5.613988596638043, 5.803117672798141]) as c:
            c.circle(self.points['O'], 5, id='circ')
            for object_id, points in [('chord_AE', [self.points['A'], self.points['E']]), ('chord_ED', [self.points['E'], self.points['D']]), ('chord_DC', [self.points['D'], self.points['C']]), ('chord_CB', [self.points['C'], self.points['B']]), ('chord_BA', [self.points['B'], self.points['A']]), ('chord_AD', [self.points['A'], self.points['D']]), ('chord_AC', [self.points['A'], self.points['C']])]:
                c.line(points, id=object_id)
            c.point([self.points['O']], filled=True, id='center_O')
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['D'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_CAD')
            center, direction, start, end = self._angle(self.points['A'], self.points['E'], self.points['D'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_AED')
            c.text('A', self.points['A'], offset_pt=[0.0, 15.0], vertex=True, id='label_A')
            c.text('E', self.points['E'], offset_pt=[13.5, 6.0], vertex=True, id='label_E')
            c.text('D', self.points['D'], offset_pt=[12.0, -12.0], vertex=True, id='label_D')
            c.text('C', self.points['C'], offset_pt=[-10.5, -13.5], vertex=True, id='label_C')
            c.text('B', self.points['B'], offset_pt=[-15.0, 0.0], vertex=True, id='label_B')
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['D'], reflex=False)
            offset = direction * 80.0 + np.array([-2.842170943040401e-14, 0.0])
            c.text('30°', center, offset_pt=offset, id='given_CAD')
            center, direction, start, end = self._angle(self.points['A'], self.points['E'], self.points['D'], reflex=False)
            offset = direction * 48.0 + np.array([0.0, 1.4210854715202004e-14])
            c.text('115°', center, offset_pt=offset, id='given_AED')
            c.text('O', self.points['O'], offset_pt=[12.0, -12.0], vertex=True, id='label_O')
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
    print(Plane03().draw(sys.argv[1] if len(sys.argv) > 1 else None))
