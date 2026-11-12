"""Frozen question Solid61; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid61:

    def __init__(self):
        self.id = 'Solid61'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3514'
        self.question = 'Find the surface area of the trapezoidal prism.'
        self.answer = '388 cm²'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'F0': [0.0, 0.0, 0.0],
         'B0': [0.0, 8.0, 0.0],
         'F1': [18.0, 0.0, 0.0],
         'B1': [18.0, 8.0, 0.0],
         'F2': [14.0, 0.0, 3.0],
         'B2': [14.0, 8.0, 3.0],
         'F3': [4.0, 0.0, 3.0],
         'B3': [4.0, 8.0, 3.0],
         'H': [4.0, 0.0, 0.0],
         'bot_anchor': [9.0, 0.0, 0.0],
         'top_anchor': [9.0, 0.0, 3.0],
         'left_anchor': [2.0, 0.0, 1.5],
         'right_anchor': [16.0, 8.0, 1.5],
         'depth_anchor': [18.0, 4.0, 0.0],
         'alt_anchor': [4.0, 0.0, 1.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid61.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.9521085104116196, 24.386471481261427], ylim=[-10.457384850339862, 14.881195141333185], projection=[[1, 0.65, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_0_0', c.project([self.points['F0'], self.points['F1']])), ('edge_1_0', c.project([self.points['F1'], self.points['F2']])), ('edge_2_0', c.project([self.points['F2'], self.points['F3']])), ('edge_3_0', c.project([self.points['F3'], self.points['F0']])), ('edge_5_0', c.project([self.points['B1'], self.points['B2']])), ('edge_6_0', c.project([self.points['B2'], self.points['B3']])), ('edge_9_0', c.project([self.points['F1'], self.points['B1']])), ('edge_10_0', c.project([self.points['F2'], self.points['B2']])), ('edge_11_0', c.project([self.points['F3'], self.points['B3']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['H'], self.points['F3']]), id='trapezoid_height', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.text('18 cm', c.project(self.points['bot_anchor']), offset_pt=[0, -16], vertex=False, id='bot')
            c.text('10 cm', c.project(self.points['top_anchor']), offset_pt=[0, 17], vertex=False, id='top')
            c.text('5 cm', c.project(self.points['left_anchor']), offset_pt=[-28.6, 9.1], vertex=False, id='left')
            c.text('5 cm', c.project(self.points['right_anchor']), offset_pt=[32.5, 6.5], vertex=False, id='right')
            c.text('8 cm', c.project(self.points['depth_anchor']), offset_pt=[24, -20], vertex=False, id='depth')
            c.text('3 cm', c.project(self.points['alt_anchor']), offset_pt=[24, 0], vertex=False, id='alt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid61().draw(sys.argv[1] if len(sys.argv) > 1 else None))
