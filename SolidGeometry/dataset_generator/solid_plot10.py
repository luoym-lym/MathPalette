"""Frozen question Solid10; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid10:

    def __init__(self):
        self.id = 'Solid10'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3524'
        self.question = 'Find the surface area of the trapezoidal prism.\n\nGive your answer to the nearest one decimal place.'
        self.answer = '\\[577.0 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [13, 0, 0],
         'C': [13, 0, 3],
         'D': [0, 0, 10],
         'A2': [0, 10, 0],
         'B2': [13, 10, 0],
         'C2': [13, 10, 3],
         'D2': [0, 10, 10],
         'M_left10': [0.0, 0.0, 5.0],
         'M_bottom13': [6.5, 0.0, 0.0],
         'M_right3': [13.0, 0.0, 1.5],
         'M_depth10': [13, 5, 0],
         'M_top_y': [6.5, 0.0, 6.5],
         'M_back_y': [6.5, 10.0, 6.5],
         'M_back3': [13.0, 10.0, 1.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid10.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.6645669472431335, 17.893511295132768], ylim=[-3.180465419537927, 17.377612822837975], projection=[[1.0, 0.26, 0.0], [0.0, 0.38, 1.13]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('A_B', c.project([self.points['A'], self.points['B']])), ('B_C', c.project([self.points['B'], self.points['C']])), ('C_D', c.project([self.points['C'], self.points['D']])), ('D_A', c.project([self.points['D'], self.points['A']])), ('D_D2', c.project([self.points['D'], self.points['D2']])), ('C_C2', c.project([self.points['C'], self.points['C2']])), ('B_B2', c.project([self.points['B'], self.points['B2']])), ('D2_C2', c.project([self.points['D2'], self.points['C2']])), ('C2_B2', c.project([self.points['C2'], self.points['B2']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('A_A2', c.project([self.points['A'], self.points['A2']])), ('A2_B2', c.project([self.points['A2'], self.points['B2']])), ('A2_D2', c.project([self.points['A2'], self.points['D2']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            c.text('10 cm', c.project(self.points['M_left10']), offset_pt=[-30, 0], vertex=False, id='left')
            c.text('13 cm', c.project(self.points['M_bottom13']), offset_pt=[0, -18], vertex=False, id='bottom')
            c.text('3 cm', c.project(self.points['M_back3']), offset_pt=[25, 0], vertex=False, id='right')
            c.text('10 cm', c.project(self.points['M_depth10']), offset_pt=[40, -10], vertex=False, id='depth')
            c.text('y cm', c.project(self.points['M_back_y']), offset_pt=[0, 30], vertex=False, id='y')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid10().draw(sys.argv[1] if len(sys.argv) > 1 else None))
