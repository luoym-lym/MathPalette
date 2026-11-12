"""Frozen question Solid247; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid247:

    def __init__(self):
        self.id = 'Solid247'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:3011'
        self.question = 'A solid right prism $ABCDEF$ has a height of $16$ and equilateral triangle bases with side length $12,$ as shown. $ABCDEF$ is sliced with a straight cut through points $M,$ $N,$ $P,$ and $Q$ on edges $DE,$ $DF,$ $CB,$ and $CA,$ respectively. If $DM=4,$ $DN=2,$ and $CQ=8,$ determine the volume of the solid $QPCDMN.$'
        self.answer = '\\frac{224\\sqrt{3}}{3}'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'A': [-6, 0, 16],
         'B': [6, 0, 16],
         'C': [0, 10.392304845413264, 16],
         'E': [-6, 0, 0],
         'F': [6, 0, 0],
         'D': [0, 10.392304845413264, 0],
         'M': [-2.0, 6.9282032302755105, 0.0],
         'N': [1.0, 8.660254037844387, 0.0],
         'Q': [-4.0, 3.4641016151377553, 16.0],
         'P': [2.0, 6.9282032302755105, 16.0],
         'ab': [0, 0, 16],
         'bf': [6, 0, 8]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid247.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-12.74262916420312, 13.02372757272001], ylim=[-7.88313654174217, 17.88322019518096], projection=[[1, 0, 0], [0, -0.5773502691896258, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['A'], self.points['B']])), ('line_1', c.project([self.points['B'], self.points['C']])), ('line_2', c.project([self.points['C'], self.points['A']])), ('line_3', c.project([self.points['A'], self.points['E']])), ('line_4', c.project([self.points['B'], self.points['F']])), ('line_5', c.project([self.points['C'], self.points['D']])), ('line_6', c.project([self.points['E'], self.points['D']])), ('line_7', c.project([self.points['D'], self.points['F']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['Q'], self.points['P']]), id='line_8', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['P'], self.points['N']]), id='line_9', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['N'], self.points['M']]), id='line_10', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['M'], self.points['Q']]), id='line_11', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.text('A', c.project(self.points['A']), offset_pt=[-15, 15], vertex=True, id='label_0')
            c.text('B', c.project(self.points['B']), offset_pt=[15, 15], vertex=True, id='label_1')
            c.text('C', c.project(self.points['C']), offset_pt=[0, 19], vertex=True, id='label_2')
            c.text('D', c.project(self.points['D']), offset_pt=[0, -20], vertex=True, id='label_3')
            c.text('E', c.project(self.points['E']), offset_pt=[-20, -10], vertex=True, id='label_4')
            c.text('F', c.project(self.points['F']), offset_pt=[20, -10], vertex=True, id='label_5')
            c.text('M', c.project(self.points['M']), offset_pt=[-18, -12], vertex=True, id='label_6')
            c.text('N', c.project(self.points['N']), offset_pt=[16, -14], vertex=True, id='label_7')
            c.text('Q', c.project(self.points['Q']), offset_pt=[-20, 0], vertex=True, id='label_8')
            c.text('P', c.project(self.points['P']), offset_pt=[20, 0], vertex=True, id='label_9')
            c.text('12', c.project(self.points['ab']), offset_pt=[0, 18], vertex=False, id='label_10')
            c.text('16', c.project(self.points['bf']), offset_pt=[22, 0], vertex=False, id='label_11')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid247().draw(sys.argv[1] if len(sys.argv) > 1 else None))
