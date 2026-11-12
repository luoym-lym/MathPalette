"""Frozen question Solid220; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid220:

    def __init__(self):
        self.id = 'Solid220'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2507'
        self.question = 'A piece of paper containing six joined squares labeled as shown in the diagram is folded along the edges of the squares to form a cube.  The label of the face opposite the face labeled $ \\text{X}$ is:\nChoices:\nA:$\\text{Z}$\nB:$\\text{U}$\nC:$\\text{V}$\nD:$\\text{W}$\nE:$\\text{Y}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\text{Z}$', 'B': '$\\text{U}$', 'C': '$\\text{V}$', 'D': '$\\text{W}$', 'E': '$\\text{Y}$'}
        self.query = self.question
        self.points = {'c0_2': [0.5, 2.5, 0],
         'c1_2': [1.5, 2.5, 0],
         'c2_2': [2.5, 2.5, 0],
         'c2_3': [2.5, 3.5, 0],
         'c1_1': [1.5, 1.5, 0],
         'c1_0': [1.5, 0.5, 0],
         'v0_2': [0, 2, 0],
         'v1_2': [1, 2, 0],
         'v1_3': [1, 3, 0],
         'v0_3': [0, 3, 0],
         'v2_2': [2, 2, 0],
         'v2_3': [2, 3, 0],
         'v3_2': [3, 2, 0],
         'v3_3': [3, 3, 0],
         'v3_4': [3, 4, 0],
         'v2_4': [2, 4, 0],
         'v1_1': [1, 1, 0],
         'v2_1': [2, 1, 0],
         'v1_0': [1, 0, 0],
         'v2_0': [2, 0, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid220.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.6028836984650305, 3.6048890441844166], ylim=[-0.10793046674171913, 4.0998422759077275], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['v0_2'], self.points['v1_2']])), ('line_1', c.project([self.points['v1_2'], self.points['v1_3']])), ('line_2', c.project([self.points['v0_3'], self.points['v1_3']])), ('line_3', c.project([self.points['v0_2'], self.points['v0_3']])), ('line_4', c.project([self.points['v1_2'], self.points['v2_2']])), ('line_5', c.project([self.points['v2_2'], self.points['v2_3']])), ('line_6', c.project([self.points['v1_3'], self.points['v2_3']])), ('line_7', c.project([self.points['v2_2'], self.points['v3_2']])), ('line_8', c.project([self.points['v3_2'], self.points['v3_3']])), ('line_9', c.project([self.points['v2_3'], self.points['v3_3']])), ('line_10', c.project([self.points['v3_3'], self.points['v3_4']])), ('line_11', c.project([self.points['v2_4'], self.points['v3_4']])), ('line_12', c.project([self.points['v2_3'], self.points['v2_4']])), ('line_13', c.project([self.points['v1_1'], self.points['v2_1']])), ('line_14', c.project([self.points['v2_1'], self.points['v2_2']])), ('line_15', c.project([self.points['v1_1'], self.points['v1_2']])), ('line_16', c.project([self.points['v1_0'], self.points['v2_0']])), ('line_17', c.project([self.points['v2_0'], self.points['v2_1']])), ('line_18', c.project([self.points['v1_0'], self.points['v1_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'U', c.project(self.points['c0_2'])), ('label_1', 'V', c.project(self.points['c1_2'])), ('label_2', 'W', c.project(self.points['c2_2'])), ('label_3', 'Y', c.project(self.points['c2_3'])), ('label_4', 'X', c.project(self.points['c1_1'])), ('label_5', 'Z', c.project(self.points['c1_0']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid220().draw(sys.argv[1] if len(sys.argv) > 1 else None))
