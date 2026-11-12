"""Frozen question Solid184; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid184:

    def __init__(self):
        self.id = 'Solid184'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1703'
        self.question = 'Two identical bricks are placed side by side in three different ways, as shown. The surface areas of the three shapes obtained are 72, 96 and 102 .\nWhat is the surface area of the original brick?'
        self.answer = '54'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'stack000': [6, 0, 6],
         'stack001': [6, 0, 8],
         'stack010': [6, 6, 6],
         'stack011': [6, 6, 8],
         'stack100': [9, 0, 6],
         'stack101': [9, 0, 8],
         'stack110': [9, 6, 6],
         'stack111': [9, 6, 8],
         'wide000': [0, 0, 0],
         'wide001': [0, 0, 1],
         'wide010': [0, 6, 0],
         'wide011': [0, 6, 1],
         'wide100': [6, 0, 0],
         'wide101': [6, 0, 1],
         'wide110': [6, 6, 0],
         'wide111': [6, 6, 1],
         'long000': [9, 0, 0],
         'long001': [9, 0, 1],
         'long010': [9, 12, 0],
         'long011': [9, 12, 1],
         'long100': [12, 0, 0],
         'long101': [12, 0, 1],
         'long110': [12, 12, 0],
         'long111': [12, 12, 1]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid184.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.5080652342325216, 20.938951862139493], ylim=[-7.644277282036139, 13.802739814335876], projection=[[1, 0.7, 0], [-0.25, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('stack000_stack100', c.project([self.points['stack000'], self.points['stack100']])), ('stack000_stack001', c.project([self.points['stack000'], self.points['stack001']])), ('stack001_stack101', c.project([self.points['stack001'], self.points['stack101']])), ('stack001_stack011', c.project([self.points['stack001'], self.points['stack011']])), ('stack011_stack111', c.project([self.points['stack011'], self.points['stack111']])), ('stack100_stack110', c.project([self.points['stack100'], self.points['stack110']])), ('stack100_stack101', c.project([self.points['stack100'], self.points['stack101']])), ('stack101_stack111', c.project([self.points['stack101'], self.points['stack111']])), ('stack110_stack111', c.project([self.points['stack110'], self.points['stack111']])), ('stackseam0', c.project([[6, 0, 7], [9, 0, 7]])), ('stackseam1', c.project([[9, 0, 7], [9, 6, 7]])), ('wide000_wide100', c.project([self.points['wide000'], self.points['wide100']])), ('wide000_wide001', c.project([self.points['wide000'], self.points['wide001']])), ('wide001_wide101', c.project([self.points['wide001'], self.points['wide101']])), ('wide001_wide011', c.project([self.points['wide001'], self.points['wide011']])), ('wide011_wide111', c.project([self.points['wide011'], self.points['wide111']])), ('wide100_wide110', c.project([self.points['wide100'], self.points['wide110']])), ('wide100_wide101', c.project([self.points['wide100'], self.points['wide101']])), ('wide101_wide111', c.project([self.points['wide101'], self.points['wide111']])), ('wide110_wide111', c.project([self.points['wide110'], self.points['wide111']])), ('wideseam0', c.project([[3, 0, 0], [3, 0, 1]])), ('wideseam1', c.project([[3, 0, 1], [3, 6, 1]])), ('long000_long100', c.project([self.points['long000'], self.points['long100']])), ('long000_long001', c.project([self.points['long000'], self.points['long001']])), ('long001_long101', c.project([self.points['long001'], self.points['long101']])), ('long001_long011', c.project([self.points['long001'], self.points['long011']])), ('long011_long111', c.project([self.points['long011'], self.points['long111']])), ('long100_long110', c.project([self.points['long100'], self.points['long110']])), ('long100_long101', c.project([self.points['long100'], self.points['long101']])), ('long101_long111', c.project([self.points['long101'], self.points['long111']])), ('long110_long111', c.project([self.points['long110'], self.points['long111']])), ('longseam0', c.project([[9, 6, 1], [12, 6, 1]])), ('longseam1', c.project([[12, 6, 0], [12, 6, 1]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('stackarea', '72', c.project([7.5, 6, 8])), ('widearea', '96', c.project([1, 6, 1])), ('longarea', '102', c.project([10.5, 12, 1]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 16], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid184().draw(sys.argv[1] if len(sys.argv) > 1 else None))
