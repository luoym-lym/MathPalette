"""Frozen question Plane50; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane50:

    def __init__(self):
        self.id = 'Plane50'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/630'
        self.question = 'Find the size of angle MBD in the figure below.'
        self.answer = '72'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0.0, 0.0],
         'B': [7.119168125571498, -3.1696578650386336],
         'C': [0.5209445330007912, -2.954423259036624],
         'D': [7.43541214517853, -0.16079700602902425],
         'M': [3.72667672691138, -1.6592233796926723]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane50.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4689237143116718, 7.902610673119918], ylim=[-5.75574910627229, 2.6157852811592996]) as c:
            for object_id, points in [('segment_1', [self.points['A'], self.points['B']]), ('segment_2', [self.points['C'], self.points['D']]), ('segment_3', [self.points['A'], self.points['C']]), ('segment_4', [self.points['B'], self.points['D']])]:
                c.line(points, id=object_id)
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['B'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_5')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['D'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_7')
            center, direction, start, end = self._angle(self.points['C'], self.points['D'], self.points['B'], reflex=False)
            c.arc(center, 18, start, end, radius_pt=True, id='angle_arc_9')
            c.text('A', self.points['A'], offset_pt=[-10, 12], vertex=True, id='name_A')
            c.text('B', self.points['B'], offset_pt=[10, -13], vertex=True, id='name_B')
            c.text('C', self.points['C'], offset_pt=[-7, -13], vertex=True, id='name_C')
            c.text('D', self.points['D'], offset_pt=[10, 12], vertex=True, id='name_D')
            c.text('M', self.points['M'], offset_pt=[0, -16], vertex=True, id='name_M')
            center, direction, start, end = self._angle(self.points['C'], self.points['A'], self.points['B'], reflex=False)
            offset = direction * 36 + np.array([0, 0])
            c.text('56°', center, offset_pt=offset, id='angle_label_6')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['D'], reflex=False)
            offset = direction * 34 + np.array([0, 0])
            c.text('78°', center, offset_pt=offset, id='angle_label_8')
            center, direction, start, end = self._angle(self.points['C'], self.points['D'], self.points['B'], reflex=False)
            offset = direction * 35 + np.array([0, 0])
            c.text('62°', center, offset_pt=offset, id='angle_label_10')
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
    print(Plane50().draw(sys.argv[1] if len(sys.argv) > 1 else None))
