"""Frozen question Solid219; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid219:

    def __init__(self):
        self.id = 'Solid219'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2463'
        self.question = 'A unit cube is cut twice to form three triangular prisms, two of which are congruent, as shown in Figure 1. The cube is then cut in the same manner along the dashed lines shown in Figure 2. This creates nine pieces. What is the volume of the piece that contains vertex $ W$?\nChoices:\nA:$\\frac{1}{12}$\nB:$\\frac{1}{9}$\nC:$\\frac{1}{8}$\nD:$\\frac{1}{6}$\nE:$\\frac{1}{4}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{12}$', 'B': '$\\frac{1}{9}$', 'C': '$\\frac{1}{8}$', 'D': '$\\frac{1}{6}$', 'E': '$\\frac{1}{4}$'}
        self.query = self.question
        self.points = {'1_000': [0, 0, 0],
         '1_001': [0, 0, 1],
         '1_010': [0, 1, 0],
         '1_011': [0, 1, 1],
         '1_100': [1, 0, 0],
         '1_101': [1, 0, 1],
         '1_110': [1, 1, 0],
         '1_111': [1, 1, 1],
         '1_L': [0, 0.5, 1],
         '1_R': [1, 0.5, 1],
         '1_caption': [0.65, -0.1, -0.17],
         '2_000': [2.05, 0, 0],
         '2_001': [2.05, 0, 1],
         '2_010': [2.05, 1, 0],
         '2_011': [2.05, 1, 1],
         '2_100': [3.05, 0, 0],
         '2_101': [3.05, 0, 1],
         '2_110': [3.05, 1, 0],
         '2_111': [3.05, 1, 1],
         '2_L': [2.05, 0.5, 1],
         '2_R': [3.05, 0.5, 1],
         '2_F': [2.55, 0, 1],
         '2_K': [2.55, 1, 1],
         '2_caption': [2.6999999999999997, -0.1, -0.17],
         'W': [1.55, -0.1, -0.05],
         'lead0a': [1.45, 0, 0.06],
         'lead0b': [1.04, 0, 0.96],
         'lead1a': [1.8, 0, 0.06],
         'lead1b': [3.01, 0, 0.96]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid219.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.0872530437383483, 3.6444313131035155], ylim=[-1.294079500632163, 2.437604856209701], projection=[[1, 0.5, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['1_000'], self.points['1_100']])), ('line_1', c.project([self.points['1_000'], self.points['1_001']])), ('line_2', c.project([self.points['1_100'], self.points['1_101']])), ('line_3', c.project([self.points['1_001'], self.points['1_101']])), ('line_4', c.project([self.points['1_001'], self.points['1_011']])), ('line_5', c.project([self.points['1_101'], self.points['1_111']])), ('line_6', c.project([self.points['1_011'], self.points['1_111']])), ('line_7', c.project([self.points['1_100'], self.points['1_110']])), ('line_8', c.project([self.points['1_110'], self.points['1_111']])), ('line_9', c.project([self.points['1_L'], self.points['1_R']])), ('line_10', c.project([self.points['1_000'], self.points['1_L']])), ('line_11', c.project([self.points['1_100'], self.points['1_R']])), ('line_12', c.project([self.points['1_110'], self.points['1_R']])), ('line_13', c.project([self.points['2_000'], self.points['2_100']])), ('line_14', c.project([self.points['2_000'], self.points['2_001']])), ('line_15', c.project([self.points['2_100'], self.points['2_101']])), ('line_16', c.project([self.points['2_001'], self.points['2_101']])), ('line_17', c.project([self.points['2_001'], self.points['2_011']])), ('line_18', c.project([self.points['2_101'], self.points['2_111']])), ('line_19', c.project([self.points['2_011'], self.points['2_111']])), ('line_20', c.project([self.points['2_100'], self.points['2_110']])), ('line_21', c.project([self.points['2_110'], self.points['2_111']])), ('line_22', c.project([self.points['2_L'], self.points['2_R']])), ('line_23', c.project([self.points['2_000'], self.points['2_L']])), ('line_24', c.project([self.points['2_100'], self.points['2_R']])), ('line_25', c.project([self.points['2_110'], self.points['2_R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('line_26', c.project([self.points['2_F'], self.points['2_K']])), ('line_27', c.project([self.points['2_000'], self.points['2_F']])), ('line_28', c.project([self.points['2_100'], self.points['2_F']])), ('line_29', c.project([self.points['2_110'], self.points['2_K']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['lead0a'], self.points['lead0b']]), id='line_30', clip_on=False, zorder=3)
            c.line(c.project([self.points['lead1a'], self.points['lead1b']]), id='line_31', clip_on=False, zorder=3)
            c.text('Figure 1', c.project(self.points['1_caption']), offset_pt=[0, -12], vertex=False, id='label_0')
            c.text('Figure 2', c.project(self.points['2_caption']), offset_pt=[0, -12], vertex=False, id='label_1')
            c.text('W', c.project(self.points['W']), offset_pt=[0, -8], vertex=True, id='label_2')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid219().draw(sys.argv[1] if len(sys.argv) > 1 else None))
