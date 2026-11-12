"""Frozen question Solid217; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid217:

    def __init__(self):
        self.id = 'Solid217'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2415'
        self.question = 'The figure shown can be folded into the shape of a cube. In the resulting cube, which of the lettered faces is opposite the face marked $x$?\n\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'c0_0': [0.5, 0.5, 0],
         'c1_0': [1.5, 0.5, 0],
         'c1_1': [1.5, 1.5, 0],
         'c2_1': [2.5, 1.5, 0],
         'c2_2': [2.5, 2.5, 0],
         'c3_2': [3.5, 2.5, 0],
         'v0_0': [0, 0, 0],
         'v1_0': [1, 0, 0],
         'v1_1': [1, 1, 0],
         'v0_1': [0, 1, 0],
         'v2_0': [2, 0, 0],
         'v2_1': [2, 1, 0],
         'v2_2': [2, 2, 0],
         'v1_2': [1, 2, 0],
         'v3_1': [3, 1, 0],
         'v3_2': [3, 2, 0],
         'v3_3': [3, 3, 0],
         'v2_3': [2, 3, 0],
         'v4_2': [4, 2, 0],
         'v4_3': [4, 3, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid217.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.0998422759077271, 4.1079304667417205], ylim=[-0.6048890441844166, 3.6028836984650305], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['v0_0'], self.points['v1_0']]), id='line_0', clip_on=False, zorder=3)
            c.line(c.project([self.points['v1_0'], self.points['v1_1']]), id='line_1', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('line_2', c.project([self.points['v0_1'], self.points['v1_1']])), ('line_3', c.project([self.points['v0_0'], self.points['v0_1']])), ('line_4', c.project([self.points['v1_0'], self.points['v2_0']])), ('line_5', c.project([self.points['v2_0'], self.points['v2_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['v1_1'], self.points['v2_1']]), id='line_6', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['v2_1'], self.points['v2_2']]), id='line_7', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('line_8', c.project([self.points['v1_2'], self.points['v2_2']])), ('line_9', c.project([self.points['v1_1'], self.points['v1_2']])), ('line_10', c.project([self.points['v2_1'], self.points['v3_1']])), ('line_11', c.project([self.points['v3_1'], self.points['v3_2']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['v2_2'], self.points['v3_2']]), id='line_12', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['v3_2'], self.points['v3_3']]), id='line_13', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            for object_id, points in [('line_14', c.project([self.points['v2_3'], self.points['v3_3']])), ('line_15', c.project([self.points['v2_2'], self.points['v2_3']])), ('line_16', c.project([self.points['v3_2'], self.points['v4_2']])), ('line_17', c.project([self.points['v4_2'], self.points['v4_3']])), ('line_18', c.project([self.points['v3_3'], self.points['v4_3']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'x', c.project(self.points['c0_0'])), ('label_1', 'A', c.project(self.points['c1_0'])), ('label_2', 'B', c.project(self.points['c1_1'])), ('label_3', 'C', c.project(self.points['c2_1'])), ('label_4', 'D', c.project(self.points['c2_2'])), ('label_5', 'E', c.project(self.points['c3_2']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid217().draw(sys.argv[1] if len(sys.argv) > 1 else None))
