"""Frozen question Plane278; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane278:

    def __init__(self):
        self.id = 'Plane278'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:836'
        self.question = 'A square can be made out of four of the given pieces. Which piece will not be used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane278.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4015892095474243, 16.38927256083307], ylim=[-7.6466291006707205, 9.144232669709774], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('piece0', [[0.0, 0.0], [2.0, 0.0], [1.5999999999999996, 0.6066666666666672], [1.5999999999999999, 1.393333333333333], [1.9999999999999993, 1.9999999999999996], [1.3933333333333333, 1.5999999999999999], [0.6066666666666661, 1.5999999999999999], [-4.440892098500626e-16, 2.0], [0.0, 0.0], [0.0, 0.0]], [1, 2, 4, 4, 4, 4, 4, 4, 2, 79]), ('piece1', [[3.5, 0.0], [5.5, 0.0], [5.1, 0.6066666666666672], [5.1, 1.393333333333333], [5.499999999999999, 1.9999999999999996], [4.8933333333333335, 2.4], [4.1066666666666665, 2.4000000000000004], [3.5, 2.0000000000000004], [3.5, 0.0], [3.5, 0.0]], [1, 2, 4, 4, 4, 4, 4, 4, 2, 79]), ('piece2', [[7.0, 0.0], [9.0, 0.0], [9.4, 0.6066666666666665], [9.4, 1.3933333333333333], [9.0, 2.0], [8.393333333333334, 2.4], [7.6066666666666665, 2.4000000000000004], [7.0, 2.0000000000000004], [7.0, 0.0], [7.0, 0.0]], [1, 2, 4, 4, 4, 4, 4, 4, 2, 79]), ('piece3', [[10.5, 0.0], [12.5, 0.0], [12.5, 2.0], [11.893333333333334, 2.4], [11.106666666666667, 2.4000000000000004], [10.5, 2.0000000000000004], [10.5, 0.0], [10.5, 0.0]], [1, 2, 2, 4, 4, 4, 2, 79]), ('piece4', [[14.0, 0.0], [16.0, 0.0], [15.6, 0.6066666666666662], [15.599999999999998, 1.3933333333333335], [15.999999999999998, 2.0000000000000004], [14.0, 2.0], [14.0, 0.0], [14.0, 0.0]], [1, 2, 4, 4, 4, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', [1.0, 1.0]), ('label1', '(A) A', [1.0, -0.6]), ('label2', 'B', [4.5, 1.0]), ('label3', '(B) B', [4.5, -0.6]), ('label4', 'C', [8.0, 1.0]), ('label5', '(C) C', [8.0, -0.6]), ('label6', 'D', [11.5, 1.0]), ('label7', '(D) D', [11.5, -0.6]), ('label8', 'E', [15.0, 1.0]), ('label9', '(E) E', [15.0, -0.6])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane278().draw(sys.argv[1] if len(sys.argv) > 1 else None))
