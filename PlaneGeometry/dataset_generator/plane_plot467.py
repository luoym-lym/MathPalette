"""Frozen question Plane467; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane467:

    def __init__(self):
        self.id = 'Plane467'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2656'
        self.question = 'What is the area enclosed by the geoboard quadrilateral below?\n\nChoices:\nA:$15$\nB:$18\\frac{1}{2}$\nC:$22\\frac{1}{2}$\nD:$27$\nE:$41$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$15$', 'B': '$18\\frac{1}{2}$', 'C': '$22\\frac{1}{2}$', 'D': '$27$', 'E': '$41$'}
        self.query = self.question
        self.points = {'p0_0': [0, 0],
         'p0_1': [0, 1],
         'p0_2': [0, 2],
         'p0_3': [0, 3],
         'p0_4': [0, 4],
         'p0_5': [0, 5],
         'p0_6': [0, 6],
         'p0_7': [0, 7],
         'p0_8': [0, 8],
         'p0_9': [0, 9],
         'p0_10': [0, 10],
         'p1_0': [1, 0],
         'p1_1': [1, 1],
         'p1_2': [1, 2],
         'p1_3': [1, 3],
         'p1_4': [1, 4],
         'p1_5': [1, 5],
         'p1_6': [1, 6],
         'p1_7': [1, 7],
         'p1_8': [1, 8],
         'p1_9': [1, 9],
         'p1_10': [1, 10],
         'p2_0': [2, 0],
         'p2_1': [2, 1],
         'p2_2': [2, 2],
         'p2_3': [2, 3],
         'p2_4': [2, 4],
         'p2_5': [2, 5],
         'p2_6': [2, 6],
         'p2_7': [2, 7],
         'p2_8': [2, 8],
         'p2_9': [2, 9],
         'p2_10': [2, 10],
         'p3_0': [3, 0],
         'p3_1': [3, 1],
         'p3_2': [3, 2],
         'p3_3': [3, 3],
         'p3_4': [3, 4],
         'p3_5': [3, 5],
         'p3_6': [3, 6],
         'p3_7': [3, 7],
         'p3_8': [3, 8],
         'p3_9': [3, 9],
         'p3_10': [3, 10],
         'p4_0': [4, 0],
         'p4_1': [4, 1],
         'p4_2': [4, 2],
         'p4_3': [4, 3],
         'p4_4': [4, 4],
         'p4_5': [4, 5],
         'p4_6': [4, 6],
         'p4_7': [4, 7],
         'p4_8': [4, 8],
         'p4_9': [4, 9],
         'p4_10': [4, 10],
         'p5_0': [5, 0],
         'p5_1': [5, 1],
         'p5_2': [5, 2],
         'p5_3': [5, 3],
         'p5_4': [5, 4],
         'p5_5': [5, 5],
         'p5_6': [5, 6],
         'p5_7': [5, 7],
         'p5_8': [5, 8],
         'p5_9': [5, 9],
         'p5_10': [5, 10],
         'p6_0': [6, 0],
         'p6_1': [6, 1],
         'p6_2': [6, 2],
         'p6_3': [6, 3],
         'p6_4': [6, 4],
         'p6_5': [6, 5],
         'p6_6': [6, 6],
         'p6_7': [6, 7],
         'p6_8': [6, 8],
         'p6_9': [6, 9],
         'p6_10': [6, 10],
         'p7_0': [7, 0],
         'p7_1': [7, 1],
         'p7_2': [7, 2],
         'p7_3': [7, 3],
         'p7_4': [7, 4],
         'p7_5': [7, 5],
         'p7_6': [7, 6],
         'p7_7': [7, 7],
         'p7_8': [7, 8],
         'p7_9': [7, 9],
         'p7_10': [7, 10],
         'p8_0': [8, 0],
         'p8_1': [8, 1],
         'p8_2': [8, 2],
         'p8_3': [8, 3],
         'p8_4': [8, 4],
         'p8_5': [8, 5],
         'p8_6': [8, 6],
         'p8_7': [8, 7],
         'p8_8': [8, 8],
         'p8_9': [8, 9],
         'p8_10': [8, 10],
         'p9_0': [9, 0],
         'p9_1': [9, 1],
         'p9_2': [9, 2],
         'p9_3': [9, 3],
         'p9_4': [9, 4],
         'p9_5': [9, 5],
         'p9_6': [9, 6],
         'p9_7': [9, 7],
         'p9_8': [9, 8],
         'p9_9': [9, 9],
         'p9_10': [9, 10],
         'p10_0': [10, 0],
         'p10_1': [10, 1],
         'p10_2': [10, 2],
         'p10_3': [10, 3],
         'p10_4': [10, 4],
         'p10_5': [10, 5],
         'p10_6': [10, 6],
         'p10_7': [10, 7],
         'p10_8': [10, 8],
         'p10_9': [10, 9],
         'p10_10': [10, 10]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane467.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3172936416641834, 10.333955597982342], ylim=[-0.3339555979823432, 10.317293641664183]) as c:
            for object_id, points in [('p0_0', [self.points['p0_0']]), ('p0_1', [self.points['p0_1']]), ('p0_2', [self.points['p0_2']]), ('p0_3', [self.points['p0_3']]), ('p0_4', [self.points['p0_4']]), ('p0_5', [self.points['p0_5']]), ('p0_6', [self.points['p0_6']]), ('p0_7', [self.points['p0_7']]), ('p0_8', [self.points['p0_8']]), ('p0_9', [self.points['p0_9']]), ('p0_10', [self.points['p0_10']]), ('p1_0', [self.points['p1_0']]), ('p1_1', [self.points['p1_1']]), ('p1_2', [self.points['p1_2']]), ('p1_3', [self.points['p1_3']]), ('p1_4', [self.points['p1_4']]), ('p1_5', [self.points['p1_5']]), ('p1_6', [self.points['p1_6']]), ('p1_7', [self.points['p1_7']]), ('p1_8', [self.points['p1_8']]), ('p1_9', [self.points['p1_9']]), ('p1_10', [self.points['p1_10']]), ('p2_0', [self.points['p2_0']]), ('p2_1', [self.points['p2_1']]), ('p2_2', [self.points['p2_2']]), ('p2_3', [self.points['p2_3']]), ('p2_4', [self.points['p2_4']]), ('p2_5', [self.points['p2_5']]), ('p2_6', [self.points['p2_6']]), ('p2_7', [self.points['p2_7']]), ('p2_8', [self.points['p2_8']]), ('p2_9', [self.points['p2_9']]), ('p2_10', [self.points['p2_10']]), ('p3_0', [self.points['p3_0']]), ('p3_1', [self.points['p3_1']]), ('p3_2', [self.points['p3_2']]), ('p3_3', [self.points['p3_3']]), ('p3_4', [self.points['p3_4']]), ('p3_5', [self.points['p3_5']]), ('p3_6', [self.points['p3_6']]), ('p3_7', [self.points['p3_7']]), ('p3_8', [self.points['p3_8']]), ('p3_9', [self.points['p3_9']]), ('p3_10', [self.points['p3_10']]), ('p4_0', [self.points['p4_0']]), ('p4_1', [self.points['p4_1']]), ('p4_2', [self.points['p4_2']]), ('p4_3', [self.points['p4_3']]), ('p4_4', [self.points['p4_4']]), ('p4_5', [self.points['p4_5']]), ('p4_6', [self.points['p4_6']]), ('p4_7', [self.points['p4_7']]), ('p4_8', [self.points['p4_8']]), ('p4_9', [self.points['p4_9']]), ('p4_10', [self.points['p4_10']]), ('p5_0', [self.points['p5_0']]), ('p5_1', [self.points['p5_1']]), ('p5_2', [self.points['p5_2']]), ('p5_3', [self.points['p5_3']]), ('p5_4', [self.points['p5_4']]), ('p5_5', [self.points['p5_5']]), ('p5_6', [self.points['p5_6']]), ('p5_7', [self.points['p5_7']]), ('p5_8', [self.points['p5_8']]), ('p5_9', [self.points['p5_9']]), ('p5_10', [self.points['p5_10']]), ('p6_0', [self.points['p6_0']]), ('p6_1', [self.points['p6_1']]), ('p6_2', [self.points['p6_2']]), ('p6_3', [self.points['p6_3']]), ('p6_4', [self.points['p6_4']]), ('p6_5', [self.points['p6_5']]), ('p6_6', [self.points['p6_6']]), ('p6_7', [self.points['p6_7']]), ('p6_8', [self.points['p6_8']]), ('p6_9', [self.points['p6_9']]), ('p6_10', [self.points['p6_10']]), ('p7_0', [self.points['p7_0']]), ('p7_1', [self.points['p7_1']]), ('p7_2', [self.points['p7_2']]), ('p7_3', [self.points['p7_3']]), ('p7_4', [self.points['p7_4']]), ('p7_5', [self.points['p7_5']]), ('p7_6', [self.points['p7_6']]), ('p7_7', [self.points['p7_7']]), ('p7_8', [self.points['p7_8']]), ('p7_9', [self.points['p7_9']]), ('p7_10', [self.points['p7_10']]), ('p8_0', [self.points['p8_0']]), ('p8_1', [self.points['p8_1']]), ('p8_2', [self.points['p8_2']]), ('p8_3', [self.points['p8_3']]), ('p8_4', [self.points['p8_4']]), ('p8_5', [self.points['p8_5']]), ('p8_6', [self.points['p8_6']]), ('p8_7', [self.points['p8_7']]), ('p8_8', [self.points['p8_8']]), ('p8_9', [self.points['p8_9']]), ('p8_10', [self.points['p8_10']]), ('p9_0', [self.points['p9_0']]), ('p9_1', [self.points['p9_1']]), ('p9_2', [self.points['p9_2']]), ('p9_3', [self.points['p9_3']]), ('p9_4', [self.points['p9_4']]), ('p9_5', [self.points['p9_5']]), ('p9_6', [self.points['p9_6']]), ('p9_7', [self.points['p9_7']]), ('p9_8', [self.points['p9_8']]), ('p9_9', [self.points['p9_9']]), ('p9_10', [self.points['p9_10']]), ('p10_0', [self.points['p10_0']]), ('p10_1', [self.points['p10_1']]), ('p10_2', [self.points['p10_2']]), ('p10_3', [self.points['p10_3']]), ('p10_4', [self.points['p10_4']]), ('p10_5', [self.points['p10_5']]), ('p10_6', [self.points['p10_6']]), ('p10_7', [self.points['p10_7']]), ('p10_8', [self.points['p10_8']]), ('p10_9', [self.points['p10_9']]), ('p10_10', [self.points['p10_10']])]:
                c.point(points, id=object_id, filled=True)
            c.path([self.points['p0_5'], self.points['p3_4'], self.points['p10_10'], self.points['p4_0'], self.points['p0_5']], [1, 2, 2, 2, 79], id='quad')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane467().draw(sys.argv[1] if len(sys.argv) > 1 else None))
