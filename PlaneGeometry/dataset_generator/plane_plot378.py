"""Frozen question Plane378; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane378:

    def __init__(self):
        self.id = 'Plane378'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1474'
        self.question = 'The rectangle $A B C D$ is made up of 12 congruent rectangles (see diagram). How big is the ratio $\\frac{A D}{D C}$?\nChoices:\nA:$\\frac{8}{9}$\nB:$\\frac{5}{6}$\nC:$\\frac{7}{8}$\nD:$\\frac{2}{3}$\nE:$\\frac{9}{8}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{8}{9}$', 'B': '$\\frac{5}{6}$', 'C': '$\\frac{7}{8}$', 'D': '$\\frac{2}{3}$', 'E': '$\\frac{9}{8}$'}
        self.query = self.question
        self.points = {'p0_0': [0, 6],
         'p0_1': [3, 6],
         'p0_2': [3, 8],
         'p0_3': [0, 8],
         'p1_0': [3, 6],
         'p1_1': [6, 6],
         'p1_2': [6, 8],
         'p1_3': [3, 8],
         'p2_0': [6, 6],
         'p2_1': [9, 6],
         'p2_2': [9, 8],
         'p2_3': [6, 8],
         'p3_0': [0, 0],
         'p3_1': [2, 0],
         'p3_2': [2, 3],
         'p3_3': [0, 3],
         'p4_0': [0, 3],
         'p4_1': [2, 3],
         'p4_2': [2, 6],
         'p4_3': [0, 6],
         'p5_0': [2, 0],
         'p5_1': [5, 0],
         'p5_2': [5, 2],
         'p5_3': [2, 2],
         'p6_0': [2, 2],
         'p6_1': [5, 2],
         'p6_2': [5, 4],
         'p6_3': [2, 4],
         'p7_0': [2, 4],
         'p7_1': [5, 4],
         'p7_2': [5, 6],
         'p7_3': [2, 6],
         'p8_0': [5, 0],
         'p8_1': [7, 0],
         'p8_2': [7, 3],
         'p8_3': [5, 3],
         'p9_0': [5, 3],
         'p9_1': [7, 3],
         'p9_2': [7, 6],
         'p9_3': [5, 6],
         'p10_0': [7, 0],
         'p10_1': [9, 0],
         'p10_2': [9, 3],
         'p10_3': [7, 3],
         'p11_0': [7, 3],
         'p11_1': [9, 3],
         'p11_2': [9, 6],
         'p11_3': [7, 6],
         'A': [0, 0],
         'B': [9, 0],
         'C': [9, 8],
         'D': [0, 8]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane378.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6915829408118421, 9.676562713718706], ylim=[-1.1541194566309096, 9.214026197899639]) as c:
            for object_id, vertices, codes in [('rectangle0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_3'], self.points['p0_0']], [1, 2, 2, 2, 79]), ('rectangle1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_3'], self.points['p1_0']], [1, 2, 2, 2, 79]), ('rectangle2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_0']], [1, 2, 2, 2, 79]), ('rectangle3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_3'], self.points['p3_0']], [1, 2, 2, 2, 79]), ('rectangle4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_3'], self.points['p4_0']], [1, 2, 2, 2, 79]), ('rectangle5', [self.points['p5_0'], self.points['p5_1'], self.points['p5_2'], self.points['p5_3'], self.points['p5_0']], [1, 2, 2, 2, 79]), ('rectangle6', [self.points['p6_0'], self.points['p6_1'], self.points['p6_2'], self.points['p6_3'], self.points['p6_0']], [1, 2, 2, 2, 79]), ('rectangle7', [self.points['p7_0'], self.points['p7_1'], self.points['p7_2'], self.points['p7_3'], self.points['p7_0']], [1, 2, 2, 2, 79]), ('rectangle8', [self.points['p8_0'], self.points['p8_1'], self.points['p8_2'], self.points['p8_3'], self.points['p8_0']], [1, 2, 2, 2, 79]), ('rectangle9', [self.points['p9_0'], self.points['p9_1'], self.points['p9_2'], self.points['p9_3'], self.points['p9_0']], [1, 2, 2, 2, 79]), ('rectangle10', [self.points['p10_0'], self.points['p10_1'], self.points['p10_2'], self.points['p10_3'], self.points['p10_0']], [1, 2, 2, 2, 79]), ('rectangle11', [self.points['p11_0'], self.points['p11_1'], self.points['p11_2'], self.points['p11_3'], self.points['p11_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            c.text('A', self.points['A'], offset_pt=[-15, 0], vertex=True, id='labelA')
            c.text('B', self.points['B'], offset_pt=[15, 0], vertex=True, id='labelB')
            c.text('C', self.points['C'], offset_pt=[15, 0], vertex=True, id='labelC')
            c.text('D', self.points['D'], offset_pt=[-15, 0], vertex=True, id='labelD')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane378().draw(sys.argv[1] if len(sys.argv) > 1 else None))
