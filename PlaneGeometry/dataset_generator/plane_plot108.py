"""Frozen question Plane108; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane108:

    def __init__(self):
        self.id = 'Plane108'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:angle_match'
        self.question = 'Which marked angle, A, B, or C, has the same measure as R? All diagrams are drawn to scale.\nChoices:\nA: Angle A\nB: Angle B\nC: Angle C'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Angle A', 'B': 'Angle B', 'C': 'Angle C'}
        self.query = self.question
        self.points = {'R_0': [-6.25, 2.051442841485013],
         'R_1': [-1.75, 2.051442841485013],
         'R_2': [-3.9999999999999996, 5.948557158514987],
         'name_anchor_R': [-4.0, 2.051442841485013],
         'A_0': [1.885691603231706, 1.9608074791675376],
         'A_1': [6.114308396768294, 3.499898124133047],
         'A_2': [3.787473781064853, 6.039192520832462],
         'name_anchor_A': [4.0, 1.9608074791675376],
         'B_0': [-1.75, -1.8266668908495967],
         'B_1': [-6.25, -1.8266668908495962],
         'B_2': [-2.914685702961343, -6.173333109150404],
         'name_anchor_B': [-4.0, -6.173333109150404],
         'C_0': [6.114308396768294, -6.215817444277468],
         'C_1': [5.332891597267108, -1.7841825557225315],
         'C_2': [1.8856916032317068, -4.6767267993119574],
         'name_anchor_C': [4.0, -6.215817444277468]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane108.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.912125353849197, 6.776433750617491], ylim=[-7.345176381312743, 6.343382723153945]) as c:
            c.line([self.points['R_0'], self.points['R_1']], id='ray_R_1')
            c.line([self.points['R_0'], self.points['R_2']], id='ray_R_2')
            center, direction, start, end = self._angle(self.points['R_1'], self.points['R_0'], self.points['R_2'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='arc_R')
            c.line([self.points['A_0'], self.points['A_1']], id='ray_A_1')
            c.line([self.points['A_0'], self.points['A_2']], id='ray_A_2')
            center, direction, start, end = self._angle(self.points['A_1'], self.points['A_0'], self.points['A_2'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='arc_A')
            c.line([self.points['B_0'], self.points['B_1']], id='ray_B_1')
            c.line([self.points['B_0'], self.points['B_2']], id='ray_B_2')
            center, direction, start, end = self._angle(self.points['B_1'], self.points['B_0'], self.points['B_2'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='arc_B')
            c.line([self.points['C_0'], self.points['C_1']], id='ray_C_1')
            c.line([self.points['C_0'], self.points['C_2']], id='ray_C_2')
            center, direction, start, end = self._angle(self.points['C_1'], self.points['C_0'], self.points['C_2'], reflex=False)
            c.arc(center, 20, start, end, radius_pt=True, id='arc_C')
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
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
    print(Plane108().draw(sys.argv[1] if len(sys.argv) > 1 else None))
