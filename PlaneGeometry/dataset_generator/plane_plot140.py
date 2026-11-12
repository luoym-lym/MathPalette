"""Frozen question Plane140; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane140:

    def __init__(self):
        self.id = 'Plane140'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:13'
        self.question = 'Which figure differs from the other four?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane140.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.9768162675989913, 18.598866992573427], ylim=[-7.098899497092024, 13.476783763080395]) as c:
            c.circle([0.0, 5], 0.7, id='o0')
            c.path([[-0.7, 2.9], [0.7, 2.9], [0.7, 4.3], [-0.7, 4.3], [-0.7, 2.9]], [1, 2, 2, 2, 79], id='o1')
            c.path([[0.0, 2.9], [-0.85, 1.9], [0.85, 1.9], [0.0, 2.9]], [1, 2, 2, 79], id='o2')
            for object_id, points in [('o3', [[-0.7, 4.3], [-1.3, 3.55]]), ('o4', [[-0.3, 1.9], [-0.3, 0.55]]), ('o5', [[-0.3, 0.55], [-0.52, 0.42]]), ('o6', [[0.7, 4.3], [1.3, 3.55]]), ('o7', [[0.3, 1.9], [0.3, 0.55]]), ('o8', [[0.3, 0.55], [0.52, 0.42]])]:
                c.line(points, id=object_id)
            c.circle([4.2, 5], 0.7, id='o9')
            c.path([[3.5, 2.9], [4.9, 2.9], [4.9, 4.3], [3.5, 4.3], [3.5, 2.9]], [1, 2, 2, 2, 79], id='o10')
            c.path([[4.2, 2.9], [3.35, 1.9], [5.05, 1.9], [4.2, 2.9]], [1, 2, 2, 79], id='o11')
            for object_id, points in [('o12', [[3.5, 4.3], [2.9000000000000004, 3.55]]), ('o13', [[3.9000000000000004, 1.9], [3.9000000000000004, 0.55]]), ('o14', [[3.9000000000000004, 0.55], [3.68, 0.42]]), ('o15', [[4.9, 4.3], [5.5, 3.55]]), ('o16', [[4.5, 1.9], [4.5, 0.55]]), ('o17', [[4.5, 0.55], [4.720000000000001, 0.42]])]:
                c.line(points, id=object_id)
            c.circle([8.4, 5], 0.7, id='o18')
            c.path([[7.7, 2.9], [9.1, 2.9], [9.1, 4.3], [7.7, 4.3], [7.7, 2.9]], [1, 2, 2, 2, 79], id='o19')
            c.path([[8.4, 2.9], [7.550000000000001, 1.9], [9.25, 1.9], [8.4, 2.9]], [1, 2, 2, 79], id='o20')
            for object_id, points in [('o21', [[7.7, 4.3], [7.1000000000000005, 3.55]]), ('o22', [[8.1, 1.9], [8.1, 0.55]]), ('o23', [[8.1, 0.55], [7.880000000000001, 0.42]]), ('o24', [[9.1, 4.3], [9.700000000000001, 3.55]]), ('o25', [[8.700000000000001, 1.9], [8.700000000000001, 0.55]]), ('o26', [[8.700000000000001, 0.55], [8.92, 0.42]])]:
                c.line(points, id=object_id)
            c.circle([12.600000000000001, 5], 0.7, id='o27')
            c.path([[11.900000000000002, 2.9], [13.300000000000002, 2.9], [13.300000000000002, 4.3], [11.900000000000002, 4.3], [11.900000000000002, 2.9]], [1, 2, 2, 2, 79], id='o28')
            c.path([[12.600000000000001, 2.9], [11.750000000000002, 1.9], [13.450000000000001, 1.9], [12.600000000000001, 2.9]], [1, 2, 2, 79], id='o29')
            for object_id, points in [('o30', [[11.900000000000002, 4.3], [11.3, 3.55]]), ('o31', [[12.3, 1.9], [12.3, 0.55]]), ('o32', [[12.3, 0.55], [12.080000000000002, 0.42]]), ('o33', [[13.3, 4.3], [13.900000000000002, 3.55]]), ('o34', [[12.900000000000002, 1.9], [12.900000000000002, 0.55]]), ('o35', [[12.900000000000002, 0.55], [13.120000000000001, 0.42]])]:
                c.line(points, id=object_id)
            c.circle([16.8, 5], 0.7, id='o36')
            c.path([[16.8, 4.3], [15.950000000000001, 3.3], [17.650000000000002, 3.3], [16.8, 4.3]], [1, 2, 2, 79], id='o37')
            c.path([[16.1, 1.9], [17.5, 1.9], [17.5, 3.3], [16.1, 3.3], [16.1, 1.9]], [1, 2, 2, 2, 79], id='o38')
            for object_id, points in [('o39', [[16.8, 4.3], [15.5, 3.55]]), ('o40', [[16.5, 1.9], [16.5, 0.55]]), ('o41', [[16.5, 0.55], [16.28, 0.42]]), ('o42', [[16.8, 4.3], [18.1, 3.55]]), ('o43', [[17.1, 1.9], [17.1, 0.55]]), ('o44', [[17.1, 0.55], [17.32, 0.42]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('t0', 'A', [-1.3, 5.7]), ('t1', 'B', [2.9000000000000004, 5.7]), ('t2', 'C', [7.1000000000000005, 5.7]), ('t3', 'D', [11.3, 5.7]), ('t4', 'E', [15.5, 5.7])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane140().draw(sys.argv[1] if len(sys.argv) > 1 else None))
