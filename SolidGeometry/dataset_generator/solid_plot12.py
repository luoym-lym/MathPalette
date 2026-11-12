"""Frozen question Solid12; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid12:

    def __init__(self):
        self.id = 'Solid12'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3544'
        self.question = 'Find the surface area of the square pyramid.\n\nRound your answer to one decimal place.'
        self.answer = '\\[256.2 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-5, -5, 0],
         'B': [5, -5, 0],
         'C': [5, 5, 0],
         'D': [-5, 5, 0],
         'O': [0, 0, 0],
         'V': [0, 0, 6],
         'RA': [0.45, 0, 0],
         'RB': [0.45, 0, 0.45],
         'RC': [0, 0, 0.45],
         'M_SIDE': [0.0, -5.0, 0.0],
         'M_H': [0.0, 0.0, 3.0],
         'T0a': [0.0, -4.55, 0.0],
         'T0b': [0.0, -5.45, 0.0],
         'T1a': [4.55, 0.0, 0.0],
         'T1b': [5.45, 0.0, 0.0],
         'T2a': [0.0, 4.55, 0.0],
         'T2b': [0.0, 5.45, 0.0],
         'T3a': [-4.55, 0.0, 0.0],
         'T3b': [-5.45, 0.0, 0.0],
         'M_RIGHT': [5, 0, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid12.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.249178183373868, 7.516182805326936], ylim=[-6.156073802556434, 8.609287186144371], projection=[[1, 0.38, 0], [0, 0.65, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['A'], self.points['B']]), id='AB', clip_on=False, zorder=3)
            c.line(c.project([self.points['B'], self.points['C']]), id='BC', clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='CD', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('DA', c.project([self.points['D'], self.points['A']])), ('VA', c.project([self.points['V'], self.points['A']])), ('VB', c.project([self.points['V'], self.points['B']])), ('VC', c.project([self.points['V'], self.points['C']])), ('VD', c.project([self.points['V'], self.points['D']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['V'], self.points['O']]), id='vertical_height_VO', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('equal_tick_1', c.project([self.points['T0a'], self.points['T0b']])), ('equal_tick_2', c.project([self.points['T1a'], self.points['T1b']])), ('equal_tick_3', c.project([self.points['T2a'], self.points['T2b']])), ('equal_tick_4', c.project([self.points['T3a'], self.points['T3b']])), ('right_angle_a', c.project([self.points['RA'], self.points['RB']])), ('right_angle_b', c.project([self.points['RB'], self.points['RC']])), ('right_angle_c', c.project([self.points['O'], self.points['RA']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('6 cm', c.project(self.points['M_H']), offset_pt=[-30, -17], vertex=False, id='given_height')
            c.text('10 cm', c.project(self.points['M_RIGHT']), offset_pt=[50, -7], vertex=False, id='given_side_right')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid12().draw(sys.argv[1] if len(sys.argv) > 1 else None))
