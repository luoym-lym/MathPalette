"""Frozen question Plane118; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane118:

    def __init__(self):
        self.id = 'Plane118'
        self.source_dataset = 'Author Designed'
        self.source_key = 'equal_angle:reference_R:candidates_A_B_C'
        self.question = 'Which labeled angle A, B, or C has the same measure as angle R? All angles are drawn to scale.\nChoices:\nA: Angle A\nB: Angle B\nC: Angle C'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Angle A', 'B': 'Angle B', 'C': 'Angle C'}
        self.query = self.question
        self.points = {'R1': [3.0, 5.0],
         'R2': [2.638304088577984, 6.147152872702092],
         'RV': [1.0, 5.0],
         'A1': [7.5, 5.0],
         'A2': [6.7855752193730785, 6.532088886237956],
         'AV': [5.5, 5.0],
         'B1': [2.879385241571817, 1.8840402866513375],
         'B2': [2.414213562373095, 2.614213562373095],
         'BV': [1.0, 1.2],
         'C1': [6.914213562373095, 2.614213562373095],
         'C2': [5.847296355333861, 3.169615506024416],
         'CV': [5.5, 1.2]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane118.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.8321785654889005, 7.670926026373584], ylim=[0.4504179362243246, 7.2891653971090085]) as c:
            c.line([self.points['RV'], self.points['R1']], id='R_arm1')
            c.line([self.points['RV'], self.points['R2']], id='R_arm2')
            center, direction, start, end = self._angle(self.points['R1'], self.points['RV'], self.points['R2'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='R_arc')
            c.line([self.points['AV'], self.points['A1']], id='A_arm1')
            c.line([self.points['AV'], self.points['A2']], id='A_arm2')
            center, direction, start, end = self._angle(self.points['A1'], self.points['AV'], self.points['A2'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='A_arc')
            c.line([self.points['BV'], self.points['B1']], id='B_arm1')
            c.line([self.points['BV'], self.points['B2']], id='B_arm2')
            center, direction, start, end = self._angle(self.points['B1'], self.points['BV'], self.points['B2'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='B_arc')
            c.line([self.points['CV'], self.points['C1']], id='C_arm1')
            c.line([self.points['CV'], self.points['C2']], id='C_arm2')
            center, direction, start, end = self._angle(self.points['C1'], self.points['CV'], self.points['C2'], reflex=False)
            c.arc(center, 16, start, end, radius_pt=True, id='C_arc')
            center, direction, start, end = self._angle(self.points['R1'], self.points['RV'], self.points['R2'], reflex=False)
            offset = direction * 48 + np.array([0, 0])
            c.text('R', center, offset_pt=offset, id='R_label')
            center, direction, start, end = self._angle(self.points['A1'], self.points['AV'], self.points['A2'], reflex=False)
            offset = direction * 48 + np.array([0, 0])
            c.text('A', center, offset_pt=offset, id='A_label')
            center, direction, start, end = self._angle(self.points['B1'], self.points['BV'], self.points['B2'], reflex=False)
            offset = direction * 48 + np.array([0, 0])
            c.text('B', center, offset_pt=offset, id='B_label')
            center, direction, start, end = self._angle(self.points['C1'], self.points['CV'], self.points['C2'], reflex=False)
            offset = direction * 48 + np.array([0, 0])
            c.text('C', center, offset_pt=offset, id='C_label')
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
    print(Plane118().draw(sys.argv[1] if len(sys.argv) > 1 else None))
