"""Frozen question Plane48; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane48:

    def __init__(self):
        self.id = 'Plane48'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/583'
        self.question = 'Find x. Round to the nearest tenth.\r\n\nChoices:\nA: 5.8\nB: 6.5\nC: 14.2\nD: 44.3'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '5.8', 'B': '6.5', 'C': '14.2', 'D': '44.3'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0], 'B': [3.8655325071954145, 4.293108778970295], 'C': [9.337854800406113, -10.741973153604238]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane48.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.916933236070406, 13.141676887678216], ylim=[-11.626514898162451, 5.4320952255861705]) as c:
            c.path([self.points['A'], self.points['B'], self.points['C'], self.points['A']], [1, 2, 2, 79], id='polygon_1')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            c.arc(center, 19, start, end, radius_pt=True, id='angle_arc_2')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            c.arc(center, 25, start, end, radius_pt=True, id='angle_arc_4')
            c.text('A', self.points['A'], offset_pt=[-14, 0], vertex=True, id='name_A')
            c.text('B', self.points['B'], offset_pt=[0, 14], vertex=True, id='name_B')
            c.text('C', self.points['C'], offset_pt=[11, -10], vertex=True, id='name_C')
            center, direction, start, end = self._angle(self.points['B'], self.points['A'], self.points['C'], reflex=False)
            offset = direction * 35 + np.array([0, 0])
            c.text('97°', center, offset_pt=offset, id='angle_label_3')
            center, direction, start, end = self._angle(self.points['A'], self.points['C'], self.points['B'], reflex=False)
            offset = direction * 90 + np.array([0, 0])
            c.text('21°', center, offset_pt=offset, id='angle_label_5')
            c.text('x', [1.9327662535977073, 2.1465543894851473], offset_pt=[-12, 7], vertex=False, id='label_6')
            c.text('16', [6.601693653800764, -3.224432187316972], offset_pt=[16, 4], vertex=False, id='label_7')
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
    print(Plane48().draw(sys.argv[1] if len(sys.argv) > 1 else None))
