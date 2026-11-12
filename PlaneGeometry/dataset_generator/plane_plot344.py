"""Frozen question Plane344; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane344:

    def __init__(self):
        self.id = 'Plane344'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1147'
        self.question = 'A piece of paper is folded, a hole is punched in it, and it is then unfolded to give the picture on the right. Along which dotted line could the paper have been folded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane344.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.4453489548654161, 20.3311548245613], ylim=[-6.664119958672776, 15.112383820753939]) as c:
            c.path([[8, 6], [11, 6], [11, 9], [8, 9], [8, 6]], [1, 2, 2, 2, 79], id='o0')
            c.circle([8.33, 7.1], 0.075, id='o1')
            c.circle([9.1, 6.33], 0.075, id='o2')
            c.path([[0.0, 0], [3.0, 0], [3.0, 3], [0.0, 3], [0.0, 0]], [1, 2, 2, 2, 79], id='o3')
            c.line([[0.0, 0], [3.0, 3]], id='o4', linestyle=(0, [4, 3]))
            c.line([[0.0, 3], [3.0, 0]], id='o5', linestyle=(0, [4, 3]))
            c.path([[4.2, 0], [7.2, 0], [7.2, 3], [4.2, 3], [4.2, 0]], [1, 2, 2, 2, 79], id='o6')
            for object_id, points in [('o7', [[4.95, 0], [4.95, 3]]), ('o8', [[5.7, 0], [5.7, 3]]), ('o9', [[6.45, 0], [6.45, 3]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[8.4, 0], [11.4, 0], [11.4, 3], [8.4, 3], [8.4, 0]], [1, 2, 2, 2, 79], id='o10')
            c.line([[9.9, 0], [9.9, 3]], id='o11', linestyle=(0, [4, 3]))
            c.line([[8.4, 1.5], [11.4, 1.5]], id='o12', linestyle=(0, [4, 3]))
            c.path([[12.600000000000001, 0], [15.600000000000001, 0], [15.600000000000001, 3], [12.600000000000001, 3], [12.600000000000001, 0]], [1, 2, 2, 2, 79], id='o13')
            for object_id, points in [('o14', [[12.600000000000001, 0], [15.600000000000001, 3]]), ('o15', [[12.600000000000001, 1.5], [14.100000000000001, 3]]), ('o16', [[14.100000000000001, 0], [15.600000000000001, 1.5]])]:
                c.line(points, id=object_id, linestyle=(0, [4, 3]))
            c.path([[16.8, 0], [19.8, 0], [19.8, 3], [16.8, 3], [16.8, 0]], [1, 2, 2, 2, 79], id='o17')
            c.line([[17.8, 0], [17.8, 3]], id='o18', linestyle=(0, [4, 3]))
            c.line([[18.8, 0], [18.8, 3]], id='o19', linestyle=(0, [4, 3]))
            for object_id, text, anchor in [('t0', '(A)', [-0.5, -0.3]), ('t1', '(B)', [3.7, -0.3]), ('t2', '(C)', [7.9, -0.3]), ('t3', '(D)', [12.100000000000001, -0.3]), ('t4', '(E)', [16.3, -0.3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane344().draw(sys.argv[1] if len(sys.argv) > 1 else None))
