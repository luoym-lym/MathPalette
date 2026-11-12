"""Frozen question Solid62; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid62:

    def __init__(self):
        self.id = 'Solid62'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3519'
        self.question = 'Find the surface area of this prism.'
        self.answer = '534 cm²'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'F0': [0.0, 0.0, 0.0],
         'B0': [0.0, 3.0, 0.0],
         'F1': [17.0, 0.0, 0.0],
         'B1': [17.0, 3.0, 0.0],
         'F2': [17.0, 0.0, 16.0],
         'B2': [17.0, 3.0, 16.0],
         'F3': [13.0, 0.0, 16.0],
         'B3': [13.0, 3.0, 16.0],
         'F4': [13.0, 0.0, 8.0],
         'B4': [13.0, 3.0, 8.0],
         'F5': [0.0, 0.0, 8.0],
         'B5': [0.0, 3.0, 8.0],
         'base_anchor': [8.5, 0.0, 0.0],
         'height_anchor': [17.0, 0.0, 8.0],
         'top_anchor': [15.0, 0.0, 16.0],
         'low_anchor': [0.0, 0.0, 4.0],
         'depth_anchor': [0.0, 1.5, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid62.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.156020087346075, 20.422976068355013], ylim=[-4.3664332374229975, 21.21256291827809], projection=[[1, -0.65, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_0_0', c.project([self.points['F0'], self.points['F1']])), ('edge_1_0', c.project([self.points['F1'], self.points['F2']])), ('edge_2_0', c.project([self.points['F2'], self.points['F3']])), ('edge_3_0', c.project([self.points['F3'], self.points['F4']])), ('edge_4_0', c.project([self.points['F4'], self.points['F5']])), ('edge_5_0', c.project([self.points['F5'], self.points['F0']])), ('edge_8_0', c.project([self.points['B2'], self.points['B3']])), ('edge_9_0', c.project([self.points['B3'], self.points['B4']])), ('edge_10_0', c.project([self.points['B4'], self.points['B5']])), ('edge_11_0', c.project([self.points['B5'], self.points['B0']])), ('edge_12_0', c.project([self.points['F0'], self.points['B0']])), ('edge_14_0', c.project([self.points['F2'], self.points['B2']])), ('edge_15_0', c.project([self.points['F3'], self.points['B3']])), ('edge_16_0', c.project([self.points['F4'], self.points['B4']])), ('edge_17_0', c.project([self.points['F5'], self.points['B5']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('17 cm', c.project(self.points['base_anchor']), offset_pt=[0, -17], vertex=False, id='base')
            c.text('16 cm', c.project(self.points['height_anchor']), offset_pt=[32, 0], vertex=False, id='height')
            c.text('4 cm', c.project(self.points['top_anchor']), offset_pt=[0.0, 30.420000000000005], vertex=False, id='top')
            c.text('8 cm', c.project(self.points['low_anchor']), offset_pt=[-70.30400000000002, 0.0], vertex=False, id='low')
            c.text('3 cm', c.project(self.points['depth_anchor']), offset_pt=[-30, -17], vertex=False, id='depth')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid62().draw(sys.argv[1] if len(sys.argv) > 1 else None))
