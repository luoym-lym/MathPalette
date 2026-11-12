"""Frozen question Solid22; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid22:

    def __init__(self):
        self.id = 'Solid22'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '2024'
        self.question = 'A rectangular container has length and width 2 units each and height 8 units. It is partially filled with water to a height of 5 units, as shown in Figure (1). The container is then tilted without spilling any water, and its front view is shown in Figure (2). Find the length of $CD$.\n\nChoices:\nA: $2 \\sqrt{5}$\nB: $3 \\sqrt{5}$\nC: $3 \\sqrt{10}$\nD: $2 \\sqrt{10}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$2 \\sqrt{5}$', 'B': '$3 \\sqrt{5}$', 'C': '$3 \\sqrt{10}$', 'D': '$2 \\sqrt{10}$'}
        self.query = self.question
        self.points = {'o0_point_0': [0, 0, 0],
         'o0_point_1': [2, 0, 0],
         'o0_point_2': [2, 0, 5],
         'o0_point_3': [0, 0, 5],
         'o1_point_0': [2, 0, 0],
         'o1_point_1': [2, 2, 0],
         'o1_point_2': [2, 2, 5],
         'o1_point_3': [2, 0, 5],
         'o2_point_0': [0.0, 0.0, 0.0],
         'o2_point_1': [0.0, 0.0, 8.0],
         'o3_point_0': [0.0, 0.0, 0.0],
         'o3_point_1': [2.0, 0.0, 0.0],
         'o4_point_0': [0.0, 0.0, 8.0],
         'o4_point_1': [0.0, 2.0, 8.0],
         'o5_point_0': [0.0, 0.0, 8.0],
         'o5_point_1': [2.0, 0.0, 8.0],
         'o6_point_0': [0.0, 2.0, 8.0],
         'o6_point_1': [2.0, 2.0, 8.0],
         'o7_point_0': [2.0, 0.0, 0.0],
         'o7_point_1': [2.0, 0.0, 8.0],
         'o8_point_0': [2.0, 0.0, 0.0],
         'o8_point_1': [2.0, 2.0, 0.0],
         'o9_point_0': [2.0, 0.0, 8.0],
         'o9_point_1': [2.0, 2.0, 8.0],
         'o10_point_0': [2.0, 2.0, 0.0],
         'o10_point_1': [2.0, 2.0, 8.0],
         'o11_point_0': [0, 0, 5],
         'o11_point_1': [2, 0, 5],
         'o11_point_2': [2, 2, 5],
         'o11_point_3': [0, 2, 5],
         'o11_point_4': [0, 0, 5],
         'o12_point_0': [0, 2, 0],
         'o12_point_1': [0, 2, 8],
         'o13_point_0': [0, 0, 0],
         'o13_point_1': [0, 2, 0],
         'o14_point_0': [0, 2, 0],
         'o14_point_1': [2, 2, 0],
         'o15_point_0': [6.367544467966324, 0, 1.8973665961010275],
         'o15_point_1': [7.0, 0, 0.0],
         'o15_point_2': [14.58946638440411, 0, 2.5298221281347035],
         'o15_point_3': [8.264911064067352, 0, 2.5298221281347035],
         'o16_point_0': [6.367544467966324, 0, 1.8973665961010275],
         'o16_point_1': [7.0, 0, 0.0],
         'o16_point_2': [14.58946638440411, 0, 2.5298221281347035],
         'o16_point_3': [13.957010852370434, 0, 4.427188724235731],
         'o16_point_4': [6.367544467966324, 0, 1.8973665961010275],
         'o17_point_0': [8.264911064067352, 0, 2.5298221281347035],
         'o17_point_1': [14.58946638440411, 0, 2.5298221281347035],
         'o18_point_0': [-0.5, 0, 0.0],
         'o18_point_1': [15.7, 0, 0.0],
         'A': [6.367544467966324, 0.0, 1.8973665961010275],
         'B': [7.0, 0.0, 0.0],
         'C': [14.58946638440411, 0.0, 2.5298221281347035],
         'E': [13.957010852370434, 0.0, 4.427188724235731],
         'D': [8.264911064067352, 0.0, 2.5298221281347035],
         'A_back': [6.367544467966324, 2.0, 1.8973665961010275],
         'B_back': [7.0, 2.0, 0.0],
         'C_back': [14.58946638440411, 2.0, 2.5298221281347035],
         'E_back': [13.957010852370434, 2.0, 4.427188724235731],
         'D_back': [8.264911064067352, 2.0, 2.5298221281347035],
         'L000': [0, 0, 0],
         'L200': [2, 0, 0],
         'L220': [2, 2, 0],
         'L008': [0, 0, 8],
         'L005': [0, 0, 5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid22.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.8984726222034265, 16.135075631462684], ylim=[-4.526343545622757, 12.507204708043353], projection=[[1.0, 0.4, 0.0], [0.0, 0.3, 1.0]], origin=[0, 0, 0], offset=[0.0, 0.0]) as c:
            c.fill(c.project([self.points['o0_point_0'], self.points['o0_point_1'], self.points['o0_point_2'], self.points['o0_point_3']]), facecolor='#E6E6E6', alpha=1, id='o0')
            c.fill(c.project([self.points['o1_point_0'], self.points['o1_point_1'], self.points['o1_point_2'], self.points['o1_point_3']]), facecolor='#E6E6E6', alpha=1, id='o1')
            for object_id, points in [('o2', c.project([self.points['o2_point_0'], self.points['o2_point_1']])), ('o3', c.project([self.points['o3_point_0'], self.points['o3_point_1']])), ('o4', c.project([self.points['o4_point_0'], self.points['o4_point_1']])), ('o5', c.project([self.points['o5_point_0'], self.points['o5_point_1']])), ('o6', c.project([self.points['o6_point_0'], self.points['o6_point_1']])), ('o7', c.project([self.points['o7_point_0'], self.points['o7_point_1']])), ('o8', c.project([self.points['o8_point_0'], self.points['o8_point_1']])), ('o9', c.project([self.points['o9_point_0'], self.points['o9_point_1']])), ('o10', c.project([self.points['o10_point_0'], self.points['o10_point_1']])), ('o11', c.project([self.points['o11_point_0'], self.points['o11_point_1'], self.points['o11_point_2'], self.points['o11_point_3'], self.points['o11_point_4']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('o12', c.project([self.points['o12_point_0'], self.points['o12_point_1']])), ('o13', c.project([self.points['o13_point_0'], self.points['o13_point_1']])), ('o14', c.project([self.points['o14_point_0'], self.points['o14_point_1']]))]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]), clip_on=False)
            c.fill(c.project([self.points['o15_point_0'], self.points['o15_point_1'], self.points['o15_point_2'], self.points['o15_point_3']]), facecolor='#E6E6E6', alpha=1, id='o15')
            for object_id, points in [('o16', c.project([self.points['o16_point_0'], self.points['o16_point_1'], self.points['o16_point_2'], self.points['o16_point_3'], self.points['o16_point_4']])), ('o17', c.project([self.points['o17_point_0'], self.points['o17_point_1']])), ('o18', c.project([self.points['o18_point_0'], self.points['o18_point_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project([6.367544467966324, 0, 1.8973665961010275]), offset_pt=[-13, 0], vertex=True, id='l0')
            c.text('B', c.project([7.0, 0, 0.0]), offset_pt=[0, -14], vertex=True, id='l1')
            c.text('C', c.project([14.58946638440411, 0, 2.5298221281347035]), offset_pt=[14, 0], vertex=True, id='l2')
            c.text('D', c.project([8.264911064067352, 0, 2.5298221281347035]), offset_pt=[-10, 12], vertex=True, id='l3')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid22().draw(sys.argv[1] if len(sys.argv) > 1 else None))
