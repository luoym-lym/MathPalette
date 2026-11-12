"""Frozen question Plane391; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane391:

    def __init__(self):
        self.id = 'Plane391'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1609'
        self.question = 'Several square pieces of paper each have area $4 \\mathrm{~cm}^{2}$. Each square is cut into smaller squares and right-angled triangles in the manner shown in the first diagram. Some of the pieces are used to make the shape shown in the second diagram.\nWhat is the area in $\\mathrm{cm}^{2}$ of the shape?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p0_0': [0, 3],
         'p0_1': [0, 5],
         'p0_2': [2, 5],
         'p1_0': [0, 3],
         'p1_1': [1, 3],
         'p1_2': [1, 4],
         'p2_0': [1, 3],
         'p2_1': [2, 3],
         'p2_2': [2, 4],
         'p2_3': [1, 4],
         'p3_0': [1, 4],
         'p3_1': [2, 4],
         'p3_2': [2, 5],
         'p4_0': [0, 1],
         'p4_1': [1, 2],
         'p4_2': [1, 1],
         'p5_0': [1, 1],
         'p5_1': [2, 1],
         'p5_2': [2, 2],
         'p5_3': [1, 2],
         'p6_0': [2, 1],
         'p6_1': [3, 1],
         'p6_2': [2, 2],
         'p7_0': [2, 2],
         'p7_1': [4, 2],
         'p7_2': [4, 0],
         'p8_0': [3, 0],
         'p8_1': [4, 0],
         'p8_2': [3, 1],
         'p9_0': [3, 2],
         'p9_1': [4, 2],
         'p9_2': [4, 3],
         'p9_3': [3, 3],
         'p10_0': [4, 2],
         'p10_1': [5, 2],
         'p10_2': [4, 3]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane391.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1240849572099414, 5.123373581336278], ylim=[-0.12372926927310957, 5.12372926927311]) as c:
            for object_id, vertices, codes in [('piece0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_0']], [1, 2, 2, 79]), ('piece1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_0']], [1, 2, 2, 79]), ('piece2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_0']], [1, 2, 2, 2, 79]), ('piece3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_0']], [1, 2, 2, 79]), ('piece4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_0']], [1, 2, 2, 79]), ('piece5', [self.points['p5_0'], self.points['p5_1'], self.points['p5_2'], self.points['p5_3'], self.points['p5_0']], [1, 2, 2, 2, 79]), ('piece6', [self.points['p6_0'], self.points['p6_1'], self.points['p6_2'], self.points['p6_0']], [1, 2, 2, 79]), ('piece7', [self.points['p7_0'], self.points['p7_1'], self.points['p7_2'], self.points['p7_0']], [1, 2, 2, 79]), ('piece8', [self.points['p8_0'], self.points['p8_1'], self.points['p8_2'], self.points['p8_0']], [1, 2, 2, 79]), ('piece9', [self.points['p9_0'], self.points['p9_1'], self.points['p9_2'], self.points['p9_3'], self.points['p9_0']], [1, 2, 2, 2, 79]), ('piece10', [self.points['p10_0'], self.points['p10_1'], self.points['p10_2'], self.points['p10_0']], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane391().draw(sys.argv[1] if len(sys.argv) > 1 else None))
