"""Frozen question Solid221; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid221:

    def __init__(self):
        self.id = 'Solid221'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2514'
        self.question = 'Suppose one of the eight lettered identical squares is included with the four squares in the T-shaped figure outlined.  How many of the resulting figures can be folded into a topless cubical box?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'c1_1': [1.5, 1.5, 0],
         'c1_2': [1.5, 2.5, 0],
         'c1_3': [1.5, 3.5, 0],
         'c2_2': [2.5, 2.5, 0],
         'c1_4': [1.5, 4.5, 0],
         'c0_3': [0.5, 3.5, 0],
         'c2_3': [2.5, 3.5, 0],
         'c0_2': [0.5, 2.5, 0],
         'c3_2': [3.5, 2.5, 0],
         'c0_1': [0.5, 1.5, 0],
         'c2_1': [2.5, 1.5, 0],
         'c1_0': [1.5, 0.5, 0],
         'v1_1': [1, 1, 0],
         'v2_1': [2, 1, 0],
         'v2_2': [2, 2, 0],
         'v1_2': [1, 2, 0],
         'v2_3': [2, 3, 0],
         'v1_3': [1, 3, 0],
         'v2_4': [2, 4, 0],
         'v1_4': [1, 4, 0],
         'v3_2': [3, 2, 0],
         'v3_3': [3, 3, 0],
         'v2_5': [2, 5, 0],
         'v1_5': [1, 5, 0],
         'v0_3': [0, 3, 0],
         'v0_4': [0, 4, 0],
         'v3_4': [3, 4, 0],
         'v0_2': [0, 2, 0],
         'v4_2': [4, 2, 0],
         'v4_3': [4, 3, 0],
         'v0_1': [0, 1, 0],
         'v3_1': [3, 1, 0],
         'v1_0': [1, 0, 0],
         'v2_0': [2, 0, 0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid221.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.628596084945126, 4.631119843366685], ylim=[-0.13491308342715014, 5.124802844884661], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['v1_1'], self.points['v2_1']])), ('line_1', c.project([self.points['v2_1'], self.points['v2_2']])), ('line_2', c.project([self.points['v1_2'], self.points['v2_2']])), ('line_3', c.project([self.points['v1_1'], self.points['v1_2']])), ('line_4', c.project([self.points['v2_2'], self.points['v2_3']])), ('line_5', c.project([self.points['v1_3'], self.points['v2_3']])), ('line_6', c.project([self.points['v1_2'], self.points['v1_3']])), ('line_7', c.project([self.points['v2_3'], self.points['v2_4']])), ('line_8', c.project([self.points['v1_4'], self.points['v2_4']])), ('line_9', c.project([self.points['v1_3'], self.points['v1_4']])), ('line_10', c.project([self.points['v2_2'], self.points['v3_2']])), ('line_11', c.project([self.points['v3_2'], self.points['v3_3']])), ('line_12', c.project([self.points['v2_3'], self.points['v3_3']])), ('line_13', c.project([self.points['v2_4'], self.points['v2_5']])), ('line_14', c.project([self.points['v1_5'], self.points['v2_5']])), ('line_15', c.project([self.points['v1_4'], self.points['v1_5']])), ('line_16', c.project([self.points['v0_3'], self.points['v1_3']])), ('line_17', c.project([self.points['v0_4'], self.points['v1_4']])), ('line_18', c.project([self.points['v0_3'], self.points['v0_4']])), ('line_19', c.project([self.points['v3_3'], self.points['v3_4']])), ('line_20', c.project([self.points['v2_4'], self.points['v3_4']])), ('line_21', c.project([self.points['v0_2'], self.points['v1_2']])), ('line_22', c.project([self.points['v0_2'], self.points['v0_3']])), ('line_23', c.project([self.points['v3_2'], self.points['v4_2']])), ('line_24', c.project([self.points['v4_2'], self.points['v4_3']])), ('line_25', c.project([self.points['v3_3'], self.points['v4_3']])), ('line_26', c.project([self.points['v0_1'], self.points['v1_1']])), ('line_27', c.project([self.points['v0_1'], self.points['v0_2']])), ('line_28', c.project([self.points['v2_1'], self.points['v3_1']])), ('line_29', c.project([self.points['v3_1'], self.points['v3_2']])), ('line_30', c.project([self.points['v1_0'], self.points['v2_0']])), ('line_31', c.project([self.points['v2_0'], self.points['v2_1']])), ('line_32', c.project([self.points['v1_0'], self.points['v1_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('label_0', 'A', c.project(self.points['c1_4'])), ('label_1', 'B', c.project(self.points['c0_3'])), ('label_2', 'C', c.project(self.points['c2_3'])), ('label_3', 'D', c.project(self.points['c0_2'])), ('label_4', 'E', c.project(self.points['c3_2'])), ('label_5', 'F', c.project(self.points['c0_1'])), ('label_6', 'G', c.project(self.points['c2_1'])), ('label_7', 'H', c.project(self.points['c1_0']))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid221().draw(sys.argv[1] if len(sys.argv) > 1 else None))
