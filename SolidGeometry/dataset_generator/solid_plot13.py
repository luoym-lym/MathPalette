"""Frozen question Solid13; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid13:

    def __init__(self):
        self.id = 'Solid13'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3559'
        self.question = 'Find the surface area of the pyramid.\n\nRound your answer to two decimal places.'
        self.answer = '\\[288.68 \\mathrm{mm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-5, -5, 0],
         'B': [5, -5, 0],
         'C': [5, 5, 0],
         'D': [-5, 5, 0],
         'O': [0, 0, 0],
         'V': [0, 0, 8],
         'RA': [0.45, 0, 0],
         'RB': [0.45, 0, 0.45],
         'RC': [0, 0, 0.45],
         'M_SIDE': [0.0, -5.0, 0.0],
         'M_H': [0.0, 0.0, 4.0],
         'M_RIGHT': [5, 0, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid13.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.047448734435899, 7.110563545487117], ylim=[-4.093239180777301, 10.064773099145714], projection=[[1, 0.34, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['A'], self.points['B']]), id='AB', clip_on=False, zorder=3)
            c.line(c.project([self.points['B'], self.points['C']]), id='BC', clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['A']]), id='DA', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('VA', c.project([self.points['V'], self.points['A']])), ('VB', c.project([self.points['V'], self.points['B']])), ('VC', c.project([self.points['V'], self.points['C']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['V'], self.points['D']]), id='VD', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('vertical_height_VO', c.project([self.points['V'], self.points['O']])), ('right_angle_a', c.project([self.points['RA'], self.points['RB']])), ('right_angle_b', c.project([self.points['RB'], self.points['RC']])), ('right_angle_c', c.project([self.points['O'], self.points['RA']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('8 mm', c.project(self.points['M_H']), offset_pt=[-30, 0], vertex=False, id='given_height')
            c.text('10 mm', c.project(self.points['M_RIGHT']), offset_pt=[36, -22], vertex=False, id='given_side_right')
            c.text('10 mm', c.project(self.points['M_SIDE']), offset_pt=[0, -15], vertex=False, id='given_side_front')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid13().draw(sys.argv[1] if len(sys.argv) > 1 else None))
