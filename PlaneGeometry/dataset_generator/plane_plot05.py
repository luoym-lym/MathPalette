"""Frozen question Plane05; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane05:

    def __init__(self):
        self.id = 'Plane05'
        self.source_dataset = 'MathVerse'
        self.source_key = 's449'
        self.question = 'As shown in the figure, then the degree of the angle of circumference angle ACB is ____.'
        self.answer = '25°'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0, 0], 'A': [3.2139380484326967, -3.83022221559489], 'B': [5.0, 0.0], 'C': [-4.53153893518325, -2.1130913087034964]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane05.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.264325811750094, 5.678502706668269], ylim=[-5.4714142592091815, 5.4714142592091815]) as c:
            c.point([self.points['O']], filled=True, id='center_O')
            c.circle(self.points['O'], 5, id='circle')
            for object_id, points in [('OA', [self.points['O'], self.points['A']]), ('OB', [self.points['O'], self.points['B']]), ('AB', [self.points['A'], self.points['B']]), ('CA', [self.points['C'], self.points['A']]), ('CB', [self.points['C'], self.points['B']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='angle_arc_given_AOB')
            c.text('O', self.points['O'], offset_pt=[-13.5, 12.0], vertex=True, id='v_O')
            c.text('A', self.points['A'], offset_pt=[12.0, -13.5], vertex=True, id='v_A')
            c.text('B', self.points['B'], offset_pt=[13.5, 10.5], vertex=True, id='v_B')
            c.text('C', self.points['C'], offset_pt=[-13.5, -10.5], vertex=True, id='v_C')
            center, direction, start, end = self._angle(self.points['A'], self.points['O'], self.points['B'], reflex=False)
            offset = direction * 40.0 + np.array([1.896366548463078, 4.876498489457058])
            c.text('50°', center, offset_pt=offset, id='given_AOB')
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
    print(Plane05().draw(sys.argv[1] if len(sys.argv) > 1 else None))
