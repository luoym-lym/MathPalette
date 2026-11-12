"""Frozen question Plane428; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane428:

    def __init__(self):
        self.id = 'Plane428'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1891'
        self.question = 'The diagram shows a shape made from six squares, each measuring $1 \\mathrm{~cm}$ by $1 \\mathrm{~cm}$. The shape has perimeter of length $14 \\mathrm{~cm}$. The zigzag shape is then continued until it has 2013 squares. What is the length, in $\\mathrm{cm}$, of the perimeter of the new shape?'
        self.answer = '4028'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'p0_0': [0.0, 0.0],
         'p0_1': [0.7071067811865475, -0.7071067811865475],
         'p0_2': [1.414213562373095, 0.0],
         'p0_3': [0.7071067811865475, 0.7071067811865475],
         'p1_0': [0.7071067811865475, 0.7071067811865475],
         'p1_1': [1.414213562373095, 0.0],
         'p1_2': [2.1213203435596424, 0.7071067811865475],
         'p1_3': [1.414213562373095, 1.414213562373095],
         'p2_0': [1.414213562373095, 0.0],
         'p2_1': [2.1213203435596424, -0.7071067811865475],
         'p2_2': [2.82842712474619, 0.0],
         'p2_3': [2.1213203435596424, 0.7071067811865475],
         'p3_0': [2.1213203435596424, 0.7071067811865475],
         'p3_1': [2.82842712474619, 0.0],
         'p3_2': [3.5355339059327373, 0.7071067811865475],
         'p3_3': [2.82842712474619, 1.414213562373095],
         'p4_0': [2.82842712474619, 0.0],
         'p4_1': [3.5355339059327373, -0.7071067811865475],
         'p4_2': [4.242640687119285, 0.0],
         'p4_3': [3.5355339059327373, 0.7071067811865475],
         'p5_0': [3.5355339059327373, 0.7071067811865475],
         'p5_1': [4.242640687119285, 0.0],
         'p5_2': [4.949747468305833, 0.7071067811865475],
         'p5_3': [4.242640687119285, 1.414213562373095]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane428.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.12172992349058775, 5.071477391796421], ylim=[-2.2430502670502306, 2.9501570482367776]) as c:
            for object_id, vertices, codes in [('square0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_3'], self.points['p0_0']], [1, 2, 2, 2, 79]), ('square1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_3'], self.points['p1_0']], [1, 2, 2, 2, 79]), ('square2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_0']], [1, 2, 2, 2, 79]), ('square3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_3'], self.points['p3_0']], [1, 2, 2, 2, 79]), ('square4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_3'], self.points['p4_0']], [1, 2, 2, 2, 79]), ('square5', [self.points['p5_0'], self.points['p5_1'], self.points['p5_2'], self.points['p5_3'], self.points['p5_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane428().draw(sys.argv[1] if len(sys.argv) > 1 else None))
