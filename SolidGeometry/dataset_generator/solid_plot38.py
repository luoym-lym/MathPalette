"""Frozen question Solid38; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid38:

    def __init__(self):
        self.id = 'Solid38'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3189'
        self.question = 'Calculate the area of the triangular divider correct to two decimal places.'
        self.answer = '124.85 cm²'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0.0, 0.0, 0.0],
         'B': [17.0, 0.0, 0.0],
         'C': [17.0, 12.0, 0.0],
         'D': [0.0, 12.0, 0.0],
         'E': [0.0, 0.0, 12.0],
         'F': [17.0, 0.0, 12.0],
         'G': [17.0, 12.0, 12.0],
         'H': [0.0, 12.0, 12.0],
         'value_0_anchor': [8.5, 0.0, 0.0],
         'value_1_anchor': [17.0, 6.0, 0.0],
         'value_2_anchor': [17.0, 12.0, 6.0],
         'unknown_diagonal_anchor': [8.5, 6.0, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid38.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.645296673006106, 27.40332502485858], ylim=[-6.66548062638281, 22.383141071481877], projection=[[1, 0.55, 0], [0, 0.32, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.fill(c.project([self.points['A'], self.points['C'], self.points['G']]), facecolor='#E6E6E6', alpha=1, id='triangular_divider')
            c.line(c.project([self.points['A'], self.points['B']]), id='edge_AB', clip_on=False, zorder=3)
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['D'], self.points['A']]), id='edge_DA', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_EF', c.project([self.points['E'], self.points['F']])), ('edge_FG', c.project([self.points['F'], self.points['G']])), ('edge_GH', c.project([self.points['G'], self.points['H']])), ('edge_HE', c.project([self.points['H'], self.points['E']])), ('edge_AE', c.project([self.points['A'], self.points['E']])), ('edge_BF', c.project([self.points['B'], self.points['F']])), ('edge_CG', c.project([self.points['C'], self.points['G']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['D'], self.points['H']]), id='edge_DH', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['A'], self.points['G']]), id='divider_diagonal', clip_on=False, zorder=3)
            c.line(c.project([self.points['A'], self.points['C']]), id='base_diagonal', linestyle=(0, [4, 3]), clip_on=False)
            c.text('17 cm', c.project(self.points['value_0_anchor']), offset_pt=[0, -16], vertex=False, id='value_0')
            c.text('12 cm', c.project(self.points['value_1_anchor']), offset_pt=[24, -24], vertex=False, id='value_1')
            c.text('12 cm', c.project(self.points['value_2_anchor']), offset_pt=[30, 0], vertex=False, id='value_2')
            c.text('z cm', c.project(self.points['unknown_diagonal_anchor']), offset_pt=[0, -15], vertex=False, id='unknown_diagonal')
            c.text('A', c.project(self.points['A']), offset_pt=[-10, -10], vertex=True, id='name_A')
            c.text('B', c.project(self.points['B']), offset_pt=[0, -15], vertex=True, id='name_B')
            c.text('C', c.project(self.points['C']), offset_pt=[12, -6], vertex=True, id='name_C')
            c.text('D', c.project(self.points['G']), offset_pt=[10, 10], vertex=True, id='name_G')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid38().draw(sys.argv[1] if len(sys.argv) > 1 else None))
