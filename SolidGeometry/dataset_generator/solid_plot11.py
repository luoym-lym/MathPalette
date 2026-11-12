"""Frozen question Solid11; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid11:

    def __init__(self):
        self.id = 'Solid11'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3534'
        self.question = 'Find the surface area of the figure shown.\n\nGive your answer to the nearest two decimal places.'
        self.answer = '\\[200.49 \\mathrm{cm}^2\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [12, 0, 0],
         'C': [9, 0, 5],
         'D': [0, 0, 5],
         'A2': [0, 3, 0],
         'B2': [12, 3, 0],
         'C2': [9, 3, 5],
         'D2': [0, 3, 5],
         'M_bottom12': [6.0, 0.0, 0.0],
         'M_top9': [4.5, 0.0, 5.0],
         'M_left5': [0.0, 0.0, 2.5],
         'M_depth3': [12, 1.5, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid11.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.7985332035831316, 14.635589412071289], ylim=[-4.254951140401836, 12.179171475252584], projection=[[1.0, 0.53, 0.0], [0.0, 0.87, 1.2]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('A_B', c.project([self.points['A'], self.points['B']])), ('B_C', c.project([self.points['B'], self.points['C']])), ('C_D', c.project([self.points['C'], self.points['D']])), ('D_A', c.project([self.points['D'], self.points['A']])), ('D_D2', c.project([self.points['D'], self.points['D2']])), ('C_C2', c.project([self.points['C'], self.points['C2']])), ('B_B2', c.project([self.points['B'], self.points['B2']])), ('D2_C2', c.project([self.points['D2'], self.points['C2']])), ('C2_B2', c.project([self.points['C2'], self.points['B2']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('12 cm', c.project(self.points['M_bottom12']), offset_pt=[0, -17], vertex=False, id='bottom')
            c.text('9 cm', c.project(self.points['M_top9']), offset_pt=[0, 14], vertex=False, id='top')
            c.text('5 cm', c.project(self.points['M_left5']), offset_pt=[-25, 0], vertex=False, id='left')
            c.text('3 cm', c.project(self.points['M_depth3']), offset_pt=[26, -4], vertex=False, id='depth')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid11().draw(sys.argv[1] if len(sys.argv) > 1 else None))
