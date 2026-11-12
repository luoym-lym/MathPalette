"""Frozen question Solid01; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid01:

    def __init__(self):
        self.id = 'Solid01'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3184'
        self.question = 'We want to find $y$, the length of the diagonal $DF$.\n\nCalculate $y$ to two decimal places.'
        self.answer = '$y=21.61$'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-7.5, 5.5, 5.5],
         'B': [-7.5, -5.5, 5.5],
         'C': [7.5, -5.5, 5.5],
         'D': [7.5, 5.5, 5.5],
         'E': [-7.5, 5.5, -5.5],
         'F': [-7.5, -5.5, -5.5],
         'G': [7.5, -5.5, -5.5],
         'H': [7.5, 5.5, -5.5],
         'M_DF': [0.0, 0.0, 0.0],
         'M_y': [4.200000000000001, 3.08, 3.08],
         'M_z': [0.0, 0.0, -5.5],
         'M_AB': [-7.5, 0.0, 5.5],
         'M_BF': [-7.5, -5.5, 0.0],
         'M_FG': [0.0, -5.5, -5.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid01.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-16.06656823961508, 18.41518954428905], ylim=[-17.112495655237577, 17.369262128666552], projection=[[-1.396629213483146, -0.6797752808988763, 0.0], [-0.46554307116104865, 0.3876404494382022, 1.0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('AB', c.project([self.points['A'], self.points['B']])), ('BC', c.project([self.points['B'], self.points['C']])), ('CD', c.project([self.points['C'], self.points['D']])), ('DA', c.project([self.points['D'], self.points['A']])), ('BF', c.project([self.points['B'], self.points['F']])), ('FG', c.project([self.points['F'], self.points['G']])), ('GC', c.project([self.points['G'], self.points['C']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['F'], self.points['E']]), id='FE', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['E'], self.points['H']]), id='EH', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['H'], self.points['G']]), id='HG', clip_on=False, zorder=3)
            c.line(c.project([self.points['A'], self.points['E']]), id='AE', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['H']]), id='DH', clip_on=False, zorder=3)
            c.line(c.project([self.points['D'], self.points['F']]), id='space_diagonal_DF', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['H'], self.points['F']]), id='z_diagonal_HF', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-1, 13], vertex=True, id='vertex_A')
            c.text('B', c.project(self.points['B']), offset_pt=[2.0, 14.0], vertex=True, id='vertex_B')
            c.text('C', c.project(self.points['C']), offset_pt=[6.0, 15.0], vertex=True, id='vertex_C')
            c.text('D', c.project(self.points['D']), offset_pt=[-5.0, 12.0], vertex=True, id='vertex_D')
            c.text('E', c.project(self.points['E']), offset_pt=[-1.0, -14.0], vertex=True, id='vertex_E')
            c.text('F', c.project(self.points['F']), offset_pt=[7, -10], vertex=True, id='vertex_F')
            c.text('G', c.project(self.points['G']), offset_pt=[0, -13], vertex=True, id='vertex_G')
            c.text('H', c.project(self.points['H']), offset_pt=[-9.0, -6.0], vertex=True, id='vertex_H')
            c.text('y cm', c.project(self.points['M_y']), offset_pt=[0, 18], vertex=False, id='label_y')
            c.text('z cm', c.project(self.points['M_z']), offset_pt=[0, -13], vertex=False, id='label_z')
            c.text('11 cm', c.project(self.points['M_AB']), offset_pt=[4.0, 22.0], vertex=False, id='dimension_text_AB')
            c.text('11 cm', c.project(self.points['M_BF']), offset_pt=[26.0, 0.0], vertex=False, id='dimension_text_BF')
            c.text('15 cm', c.project(self.points['M_FG']), offset_pt=[1.0, -18.0], vertex=False, id='dimension_text_FG')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid01().draw(sys.argv[1] if len(sys.argv) > 1 else None))
