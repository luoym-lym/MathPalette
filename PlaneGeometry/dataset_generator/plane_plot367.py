"""Frozen question Plane367; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane367:

    def __init__(self):
        self.id = 'Plane367'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1355'
        self.question = 'Which of the shapes to the right has the largest area?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:All shapes have the same area.'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'All shapes have the same area.'}
        self.query = self.question
        self.points = {'v0a': [0, -0.25],
         'v0b': [0, 2.25],
         'v1a': [1, -0.25],
         'v1b': [1, 2.25],
         'v2a': [2, -0.25],
         'v2b': [2, 2.25],
         'v3a': [3, -0.25],
         'v3b': [3, 2.25],
         'v4a': [4, -0.25],
         'v4b': [4, 2.25],
         'v5a': [5, -0.25],
         'v5b': [5, 2.25],
         'v6a': [6, -0.25],
         'v6b': [6, 2.25],
         'v7a': [7, -0.25],
         'v7b': [7, 2.25],
         'v8a': [8, -0.25],
         'v8b': [8, 2.25],
         'v9a': [9, -0.25],
         'v9b': [9, 2.25],
         'v10a': [10, -0.25],
         'v10b': [10, 2.25],
         'v11a': [11, -0.25],
         'v11b': [11, 2.25],
         'v12a': [12, -0.25],
         'v12b': [12, 2.25],
         'v13a': [13, -0.25],
         'v13b': [13, 2.25],
         'v14a': [14, -0.25],
         'v14b': [14, 2.25],
         'h0a': [-0.25, 0],
         'h0b': [14.25, 0],
         'h1a': [-0.25, 1],
         'h1b': [14.25, 1],
         'h2a': [-0.25, 2],
         'h2b': [14.25, 2],
         'p0_0': [0, 1],
         'p0_1': [1, 2],
         'p0_2': [2, 2],
         'p0_3': [2, 0],
         'p0_4': [1, 1],
         'label0': [0.2, 1.75],
         'p1_0': [3, 1],
         'p1_1': [4, 1],
         'p1_2': [4, 2],
         'p1_3': [5, 2],
         'p1_4': [5, 1],
         'p1_5': [4, 0],
         'label1': [3.2, 1.75],
         'p2_0': [6, 1],
         'p2_1': [7, 2],
         'p2_2': [8, 2],
         'p2_3': [8, 1],
         'p2_4': [7, 0],
         'p2_5': [7, 1],
         'label2': [6.2, 1.75],
         'p3_0': [9, 0],
         'p3_1': [11, 0],
         'p3_2': [11, 2],
         'label3': [9.2, 1.75],
         'p4_0': [12, 1],
         'p4_1': [13, 2],
         'p4_2': [14, 1],
         'p4_3': [13, 0],
         'label4': [12.2, 1.75]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane367.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6093586709115764, 14.633500729125622], ylim=[-6.633492055342674, 8.609367344694526]) as c:
            for object_id, points in [('v0', [self.points['v0a'], self.points['v0b']]), ('v1', [self.points['v1a'], self.points['v1b']]), ('v2', [self.points['v2a'], self.points['v2b']]), ('v3', [self.points['v3a'], self.points['v3b']]), ('v4', [self.points['v4a'], self.points['v4b']]), ('v5', [self.points['v5a'], self.points['v5b']]), ('v6', [self.points['v6a'], self.points['v6b']]), ('v7', [self.points['v7a'], self.points['v7b']]), ('v8', [self.points['v8a'], self.points['v8b']]), ('v9', [self.points['v9a'], self.points['v9b']]), ('v10', [self.points['v10a'], self.points['v10b']]), ('v11', [self.points['v11a'], self.points['v11b']]), ('v12', [self.points['v12a'], self.points['v12b']]), ('v13', [self.points['v13a'], self.points['v13b']]), ('v14', [self.points['v14a'], self.points['v14b']]), ('h0', [self.points['h0a'], self.points['h0b']]), ('h1', [self.points['h1a'], self.points['h1b']]), ('h2', [self.points['h2a'], self.points['h2b']])]:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('shape0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_3'], self.points['p0_4'], self.points['p0_0']], [1, 2, 2, 2, 2, 79]), ('shape1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_3'], self.points['p1_4'], self.points['p1_5'], self.points['p1_0']], [1, 2, 2, 2, 2, 2, 79]), ('shape2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_4'], self.points['p2_5'], self.points['p2_0']], [1, 2, 2, 2, 2, 2, 79]), ('shape3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_0']], [1, 2, 2, 79]), ('shape4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_3'], self.points['p4_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', self.points['label0']), ('label1', 'B', self.points['label1']), ('label2', 'C', self.points['label2']), ('label3', 'D', self.points['label3']), ('label4', 'E', self.points['label4'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane367().draw(sys.argv[1] if len(sys.argv) > 1 else None))
