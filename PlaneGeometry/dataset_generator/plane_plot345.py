"""Frozen question Plane345; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane345:

    def __init__(self):
        self.id = 'Plane345'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1163'
        self.question = 'A large rectangle is made up of 9 equally big rectangles. The longer side of each small rectangle is $10 \\mathrm{~cm}$ long. What is the perimeter of the large rectangle?\nChoices:\nA:$40 \\mathrm{~cm}$\nB:$48 \\mathrm{~cm}$\nC:$76 \\mathrm{~cm}$\nD:$81 \\mathrm{~cm}$\nE:$90 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$40 \\mathrm{~cm}$', 'B': '$48 \\mathrm{~cm}$', 'C': '$76 \\mathrm{~cm}$', 'D': '$81 \\mathrm{~cm}$', 'E': '$90 \\mathrm{~cm}$'}
        self.query = self.question
        self.points = {'p0_0': [0, 0],
         'p0_1': [10, 0],
         'p0_2': [10, 4],
         'p0_3': [0, 4],
         'p1_0': [10, 0],
         'p1_1': [20, 0],
         'p1_2': [20, 4],
         'p1_3': [10, 4],
         'p2_0': [0, 14],
         'p2_1': [10, 14],
         'p2_2': [10, 18],
         'p2_3': [0, 18],
         'p3_0': [10, 14],
         'p3_1': [20, 14],
         'p3_2': [20, 18],
         'p3_3': [10, 18],
         'p4_0': [0, 4],
         'p4_1': [4, 4],
         'p4_2': [4, 14],
         'p4_3': [0, 14],
         'p5_0': [4, 4],
         'p5_1': [8, 4],
         'p5_2': [8, 14],
         'p5_3': [4, 14],
         'p6_0': [8, 4],
         'p6_1': [12, 4],
         'p6_2': [12, 14],
         'p6_3': [8, 14],
         'p7_0': [12, 4],
         'p7_1': [16, 4],
         'p7_2': [16, 14],
         'p7_3': [12, 14],
         'p8_0': [16, 4],
         'p8_1': [20, 4],
         'p8_2': [20, 14],
         'p8_3': [16, 14]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane345.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.49566713229182824, 20.528966522931892], ylim=[-1.528954559093341, 19.49567909613038]) as c:
            for object_id, vertices, codes in [('rectangle0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_3'], self.points['p0_0']], [1, 2, 2, 2, 79]), ('rectangle1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_3'], self.points['p1_0']], [1, 2, 2, 2, 79]), ('rectangle2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_0']], [1, 2, 2, 2, 79]), ('rectangle3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_3'], self.points['p3_0']], [1, 2, 2, 2, 79]), ('rectangle4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_3'], self.points['p4_0']], [1, 2, 2, 2, 79]), ('rectangle5', [self.points['p5_0'], self.points['p5_1'], self.points['p5_2'], self.points['p5_3'], self.points['p5_0']], [1, 2, 2, 2, 79]), ('rectangle6', [self.points['p6_0'], self.points['p6_1'], self.points['p6_2'], self.points['p6_3'], self.points['p6_0']], [1, 2, 2, 2, 79]), ('rectangle7', [self.points['p7_0'], self.points['p7_1'], self.points['p7_2'], self.points['p7_3'], self.points['p7_0']], [1, 2, 2, 2, 79]), ('rectangle8', [self.points['p8_0'], self.points['p8_1'], self.points['p8_2'], self.points['p8_3'], self.points['p8_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane345().draw(sys.argv[1] if len(sys.argv) > 1 else None))
