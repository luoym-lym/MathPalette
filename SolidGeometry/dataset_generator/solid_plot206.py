"""Frozen question Solid206; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid206:

    def __init__(self):
        self.id = 'Solid206'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2036'
        self.question = 'The solid shown has a square base of side length $s$.  The upper edge is parallel to the base and has length $2s$.  All other edges have length $s$.  Given that $s = 6 \\sqrt{2}$, what is the volume of the solid?'
        self.answer = '288'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [0, 0, 0],
         'B': [8.485281374238571, 0, 0],
         'C': [8.485281374238571, 8.485281374238571, 0],
         'D': [0, 8.485281374238571, 0],
         'L': [-4.242640687119286, 4.242640687119286, 6.0],
         'R': [12.727922061357857, 4.242640687119286, 6.0],
         'ab': [4.242640687119286, 0, 0],
         'lr': [4.242640687119286, 4.242640687119286, 6.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid206.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.8470772379015923, 16.96911184895488], ylim=[-5.202028526250254, 12.614160560606217], projection=[[1, 0.9, 0], [-0.25, 0.3, 1.2]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['A'], self.points['B']])), ('line_1', c.project([self.points['B'], self.points['C']])), ('line_2', c.project([self.points['A'], self.points['L']])), ('line_3', c.project([self.points['B'], self.points['R']])), ('line_4', c.project([self.points['C'], self.points['R']])), ('line_5', c.project([self.points['L'], self.points['R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('line_6', c.project([self.points['A'], self.points['D']])), ('line_7', c.project([self.points['C'], self.points['D']])), ('line_8', c.project([self.points['L'], self.points['D']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            c.text('s', c.project(self.points['ab']), offset_pt=[0, -18], vertex=False, id='label_0')
            c.text('2s', c.project(self.points['lr']), offset_pt=[0, 18], vertex=False, id='label_1')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid206().draw(sys.argv[1] if len(sys.argv) > 1 else None))
