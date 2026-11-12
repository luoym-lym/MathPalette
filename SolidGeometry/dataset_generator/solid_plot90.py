"""Frozen question Solid90; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid90:

    def __init__(self):
        self.id = 'Solid90'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:192'
        self.question = 'The lengths of the sides of triangle $X Y Z$ are $X Z=\\sqrt{55}$, $X Y=8, Y Z=9$. Find the length of the diagonal $X A$ of the rectangular parallelepiped in the figure.'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p000': [0.0, 0.0, 0],
         'p001': [0.0, 0.0, 6],
         'p010': [0.0, 4.358898943540674, 0],
         'p011': [0.0, 4.358898943540674, 6],
         'p100': [6.708203932499369, 0.0, 0],
         'p101': [6.708203932499369, 0.0, 6],
         'p110': [6.708203932499369, 4.358898943540674, 0],
         'p111': [6.708203932499369, 4.358898943540674, 6]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid90.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.49527246339301056, 8.452256468705684], ylim=[-0.6941089018261168, 8.25342003027258], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['p000'], self.points['p100']]), id='p000_p100', clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p010']]), id='p000_p010', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('p000_p001', c.project([self.points['p000'], self.points['p001']])), ('p001_p101', c.project([self.points['p001'], self.points['p101']])), ('p001_p011', c.project([self.points['p001'], self.points['p011']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p010'], self.points['p110']]), id='p010_p110', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p010'], self.points['p011']]), id='p010_p011', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('p011_p111', c.project([self.points['p011'], self.points['p111']])), ('p100_p110', c.project([self.points['p100'], self.points['p110']])), ('p100_p101', c.project([self.points['p100'], self.points['p101']])), ('p101_p111', c.project([self.points['p101'], self.points['p111']])), ('p110_p111', c.project([self.points['p110'], self.points['p111']])), ('diagp011p101', c.project([self.points['p011'], self.points['p101']])), ('diagp101p000', c.project([self.points['p101'], self.points['p000']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['p000'], self.points['p011']]), id='diagp000p011', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['p011'], self.points['p100']]), id='diagp011p100', linestyle=(0, [4, 3]), clip_on=False)
            c.text('X', c.project(self.points['p011']), offset_pt=[-5, 14], vertex=True, id='labelX')
            c.text('Y', c.project(self.points['p101']), offset_pt=[13, -6], vertex=True, id='labelY')
            c.text('Z', c.project(self.points['p000']), offset_pt=[-10, -15], vertex=True, id='labelZ')
            c.text('A', c.project(self.points['p100']), offset_pt=[0, -15], vertex=True, id='labelA')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid90().draw(sys.argv[1] if len(sys.argv) > 1 else None))
