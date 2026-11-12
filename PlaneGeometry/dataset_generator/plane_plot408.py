"""Frozen question Plane408; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane408:

    def __init__(self):
        self.id = 'Plane408'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1744'
        self.question = 'Four ribbons each have width $10 \\mathrm{~cm}$. Each ribbon is $25 \\mathrm{~cm}$ longer than the next smallest ribbon. The ribbons are then arranged to form two different shapes as shown in the diagram. How much longer is the perimeter of the second shape than the perimeter of the first shape?\nChoices:\nA:$75 \\mathrm{~cm}$\nB:$50 \\mathrm{~cm}$\nC:$25 \\mathrm{~cm}$\nD:$20 \\mathrm{~cm}$\nE:$0 \\mathrm{~cm}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$75 \\mathrm{~cm}$', 'B': '$50 \\mathrm{~cm}$', 'C': '$25 \\mathrm{~cm}$', 'D': '$20 \\mathrm{~cm}$', 'E': '$0 \\mathrm{~cm}$'}
        self.query = self.question
        self.points = {'p0_0_0': [0, 0],
         'p0_0_1': [10, 0],
         'p0_0_2': [10, 35],
         'p0_0_3': [0, 35],
         'p0_1_0': [10, 0],
         'p0_1_1': [20, 0],
         'p0_1_2': [20, 60],
         'p0_1_3': [10, 60],
         'p0_2_0': [20, 0],
         'p0_2_1': [30, 0],
         'p0_2_2': [30, 85],
         'p0_2_3': [20, 85],
         'p0_3_0': [30, 0],
         'p0_3_1': [40, 0],
         'p0_3_2': [40, 110],
         'p0_3_3': [30, 110],
         'p1_0_0': [70, 0],
         'p1_0_1': [80, 0],
         'p1_0_2': [80, 85],
         'p1_0_3': [70, 85],
         'p1_1_0': [80, 0],
         'p1_1_1': [90, 0],
         'p1_1_2': [90, 60],
         'p1_1_3': [80, 60],
         'p1_2_0': [90, 0],
         'p1_2_1': [100, 0],
         'p1_2_2': [100, 110],
         'p1_2_3': [90, 110],
         'p1_3_0': [100, 0],
         'p1_3_1': [110, 0],
         'p1_3_2': [110, 35],
         'p1_3_3': [100, 35]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane408.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.7261692276050695, 112.9093158761254], ylim=[-2.9093158761254045, 112.72616922760507]) as c:
            for object_id, vertices, codes in [('ribbon0_0', [self.points['p0_0_0'], self.points['p0_0_1'], self.points['p0_0_2'], self.points['p0_0_3'], self.points['p0_0_0']], [1, 2, 2, 2, 79]), ('ribbon0_1', [self.points['p0_1_0'], self.points['p0_1_1'], self.points['p0_1_2'], self.points['p0_1_3'], self.points['p0_1_0']], [1, 2, 2, 2, 79]), ('ribbon0_2', [self.points['p0_2_0'], self.points['p0_2_1'], self.points['p0_2_2'], self.points['p0_2_3'], self.points['p0_2_0']], [1, 2, 2, 2, 79]), ('ribbon0_3', [self.points['p0_3_0'], self.points['p0_3_1'], self.points['p0_3_2'], self.points['p0_3_3'], self.points['p0_3_0']], [1, 2, 2, 2, 79]), ('ribbon1_0', [self.points['p1_0_0'], self.points['p1_0_1'], self.points['p1_0_2'], self.points['p1_0_3'], self.points['p1_0_0']], [1, 2, 2, 2, 79]), ('ribbon1_1', [self.points['p1_1_0'], self.points['p1_1_1'], self.points['p1_1_2'], self.points['p1_1_3'], self.points['p1_1_0']], [1, 2, 2, 2, 79]), ('ribbon1_2', [self.points['p1_2_0'], self.points['p1_2_1'], self.points['p1_2_2'], self.points['p1_2_3'], self.points['p1_2_0']], [1, 2, 2, 2, 79]), ('ribbon1_3', [self.points['p1_3_0'], self.points['p1_3_1'], self.points['p1_3_2'], self.points['p1_3_3'], self.points['p1_3_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane408().draw(sys.argv[1] if len(sys.argv) > 1 else None))
