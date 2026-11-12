"""Frozen question Plane444; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane444:

    def __init__(self):
        self.id = 'Plane444'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2204'
        self.question = 'The letter F shown below is rotated $90^\\circ$ clockwise around the origin, then reflected in the $y$-axis, and then rotated a half turn around the origin. What is the final image?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane444.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-8.331692114329279, 44.740382871890816], ylim=[-16.80687082644338, 36.265204159776715]) as c:
            c.line([[12, 19], [22, 19]], id='o0')
            c.line([[15, 17], [15, 26]], id='o1')
            c.path([[15, 19], [16, 19], [16, 21], [17, 21], [17, 22], [16, 22], [16, 23], [18, 23], [18, 24], [15, 24], [15, 19]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o2')
            c.line([[-3, 9], [7, 9]], id='o3')
            c.line([[0, 7], [0, 16]], id='o4')
            c.path([[0, 9], [1, 9], [1, 11], [2, 11], [2, 12], [1, 12], [1, 13], [3, 13], [3, 14], [0, 14], [0, 9]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o5')
            c.line([[16, 9], [26, 9]], id='o6')
            c.line([[19, 7], [19, 16]], id='o7')
            c.path([[19, 9], [18, 9], [18, 11], [17, 11], [17, 12], [18, 12], [18, 13], [16, 13], [16, 14], [19, 14], [19, 9]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o8')
            c.line([[33, 9], [42, 9]], id='o9')
            c.line([[40, 7], [40, 16]], id='o10')
            c.path([[40, 9], [35, 9], [35, 10], [37, 10], [37, 11], [38, 11], [38, 10], [39, 10], [39, 12], [40, 12], [40, 9]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o11')
            c.line([[-3, -6], [7, -6]], id='o12')
            c.line([[0, -8], [0, 1]], id='o13')
            c.path([[0, -1], [1, -1], [1, -3], [2, -3], [2, -4], [1, -4], [1, -5], [3, -5], [3, -6], [0, -6], [0, -1]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o14')
            c.line([[15, -6], [25, -6]], id='o15')
            c.line([[18, -8], [18, 1]], id='o16')
            c.path([[18, -6], [18, -5], [20, -5], [20, -4], [21, -4], [21, -5], [22, -5], [22, -3], [23, -3], [23, -6], [18, -6]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='o17')
            for object_id, text, anchor in [('t0', '$x$', [23, 19]), ('t1', '$y$', [15, 27]), ('t2', '$x$', [8, 9]), ('t3', '$y$', [0, 17]), ('t4', '(A)', [-6, 9]), ('t5', '$x$', [27, 9]), ('t6', '$y$', [19, 17]), ('t7', '(B)', [13, 9]), ('t8', '$x$', [43, 9]), ('t9', '$y$', [40, 17]), ('t10', '(C)', [30, 9]), ('t11', '$x$', [8, -6]), ('t12', '$y$', [0, 2]), ('t13', '(D)', [-6, -6]), ('t14', '$x$', [26, -6]), ('t15', '$y$', [18, 2]), ('t16', '(E)', [12, -6])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane444().draw(sys.argv[1] if len(sys.argv) > 1 else None))
