"""Frozen question Plane436; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane436:

    def __init__(self):
        self.id = 'Plane436'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1974'
        self.question = 'Twelve congruent rectangles are placed together to make a rectangle $P Q R S$ as shown. What is the ratio $P Q: Q R$?\nChoices:\nA:$2: 3$\nB:$3: 4$\nC:$5: 6$\nD:$7: 8$\nE:$8: 9$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$2: 3$', 'B': '$3: 4$', 'C': '$5: 6$', 'D': '$7: 8$', 'E': '$8: 9$'}
        self.query = self.question
        self.points = {'top0_0': [0.0, 3],
         'top0_1': [1.5, 3],
         'top0_2': [1.5, 4],
         'top0_3': [0.0, 4],
         'top1_0': [1.5, 3],
         'top1_1': [3.0, 3],
         'top1_2': [3.0, 4],
         'top1_3': [1.5, 4],
         'top2_0': [3.0, 3],
         'top2_1': [4.5, 3],
         'top2_2': [4.5, 4],
         'top2_3': [3.0, 4],
         'left0_0': [0, 0.0],
         'left0_1': [1, 0.0],
         'left0_2': [1, 1.5],
         'left0_3': [0, 1.5],
         'left1_0': [0, 1.5],
         'left1_1': [1, 1.5],
         'left1_2': [1, 3.0],
         'left1_3': [0, 3.0],
         'mid0_0': [1, 0],
         'mid0_1': [2.5, 0],
         'mid0_2': [2.5, 1],
         'mid0_3': [1, 1],
         'mid1_0': [1, 1],
         'mid1_1': [2.5, 1],
         'mid1_2': [2.5, 2],
         'mid1_3': [1, 2],
         'mid2_0': [1, 2],
         'mid2_1': [2.5, 2],
         'mid2_2': [2.5, 3],
         'mid2_3': [1, 3],
         'right00_0': [2.5, 0.0],
         'right00_1': [3.5, 0.0],
         'right00_2': [3.5, 1.5],
         'right00_3': [2.5, 1.5],
         'right01_0': [2.5, 1.5],
         'right01_1': [3.5, 1.5],
         'right01_2': [3.5, 3.0],
         'right01_3': [2.5, 3.0],
         'right10_0': [3.5, 0.0],
         'right10_1': [4.5, 0.0],
         'right10_2': [4.5, 1.5],
         'right10_3': [3.5, 1.5],
         'right11_0': [3.5, 1.5],
         'right11_1': [4.5, 1.5],
         'right11_2': [4.5, 3.0],
         'right11_3': [3.5, 3.0],
         'P': [0, 4],
         'Q': [0, 0],
         'R': [4.5, 0],
         'S': [4.5, 4]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane436.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.33793961915396364, 4.830447662491748], ylim=[-0.5804501512395226, 4.587937130406189]) as c:
            for object_id, vertices, codes in [('top0', [self.points['top0_0'], self.points['top0_1'], self.points['top0_2'], self.points['top0_3'], self.points['top0_0']], [1, 2, 2, 2, 79]), ('top1', [self.points['top1_0'], self.points['top1_1'], self.points['top1_2'], self.points['top1_3'], self.points['top1_0']], [1, 2, 2, 2, 79]), ('top2', [self.points['top2_0'], self.points['top2_1'], self.points['top2_2'], self.points['top2_3'], self.points['top2_0']], [1, 2, 2, 2, 79]), ('left0', [self.points['left0_0'], self.points['left0_1'], self.points['left0_2'], self.points['left0_3'], self.points['left0_0']], [1, 2, 2, 2, 79]), ('left1', [self.points['left1_0'], self.points['left1_1'], self.points['left1_2'], self.points['left1_3'], self.points['left1_0']], [1, 2, 2, 2, 79]), ('mid0', [self.points['mid0_0'], self.points['mid0_1'], self.points['mid0_2'], self.points['mid0_3'], self.points['mid0_0']], [1, 2, 2, 2, 79]), ('mid1', [self.points['mid1_0'], self.points['mid1_1'], self.points['mid1_2'], self.points['mid1_3'], self.points['mid1_0']], [1, 2, 2, 2, 79]), ('mid2', [self.points['mid2_0'], self.points['mid2_1'], self.points['mid2_2'], self.points['mid2_3'], self.points['mid2_0']], [1, 2, 2, 2, 79]), ('right00', [self.points['right00_0'], self.points['right00_1'], self.points['right00_2'], self.points['right00_3'], self.points['right00_0']], [1, 2, 2, 2, 79]), ('right01', [self.points['right01_0'], self.points['right01_1'], self.points['right01_2'], self.points['right01_3'], self.points['right01_0']], [1, 2, 2, 2, 79]), ('right10', [self.points['right10_0'], self.points['right10_1'], self.points['right10_2'], self.points['right10_3'], self.points['right10_0']], [1, 2, 2, 2, 79]), ('right11', [self.points['right11_0'], self.points['right11_1'], self.points['right11_2'], self.points['right11_3'], self.points['right11_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.text('P', self.points['P'], offset_pt=[-15, 13], vertex=True, id='nameP')
            c.text('Q', self.points['Q'], offset_pt=[-15, -13], vertex=True, id='nameQ')
            c.text('R', self.points['R'], offset_pt=[15, -13], vertex=True, id='nameR')
            c.text('S', self.points['S'], offset_pt=[15, 13], vertex=True, id='nameS')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane436().draw(sys.argv[1] if len(sys.argv) > 1 else None))
