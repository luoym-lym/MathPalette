"""Frozen question Solid225; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid225:

    def __init__(self):
        self.id = 'Solid225'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2539'
        self.question = 'The numbers on the faces of this cube are consecutive whole numbers. The sums of the two numbers on each of the three pairs of opposite faces are equal. The sum of the six numbers on this cube is'
        self.answer = '81'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p000': [0, 0, 0],
         'p001': [0, 0, 1],
         'p010': [0, 1, 0],
         'p011': [0, 1, 1],
         'p100': [1, 0, 0],
         'p101': [1, 0, 1],
         'p110': [1, 1, 0],
         'p111': [1, 1, 1],
         'front': [0.5, 0, 0.5],
         'top': [0.5, 0.5, 1],
         'right': [1, 0.5, 0.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid225.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.04143454450170703, 1.7047911436978136], ylim=[-0.04479114369781345, 1.7014345445017072], projection=[[1, 0.66, 0], [0, 0.66, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['p000'], self.points['p100']])), ('line_1', c.project([self.points['p000'], self.points['p001']])), ('line_2', c.project([self.points['p100'], self.points['p101']])), ('line_3', c.project([self.points['p001'], self.points['p101']])), ('line_4', c.project([self.points['p001'], self.points['p011']])), ('line_5', c.project([self.points['p101'], self.points['p111']])), ('line_6', c.project([self.points['p011'], self.points['p111']])), ('line_7', c.project([self.points['p100'], self.points['p110']])), ('line_8', c.project([self.points['p110'], self.points['p111']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', '15', c.project(self.points['front'])), ('label_1', '14', c.project(self.points['top'])), ('label_2', '11', c.project(self.points['right']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid225().draw(sys.argv[1] if len(sys.argv) > 1 else None))
