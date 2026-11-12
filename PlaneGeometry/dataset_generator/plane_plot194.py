"""Frozen question Plane194; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane194:

    def __init__(self):
        self.id = 'Plane194'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:446'
        self.question = 'A square piece of paper is folded twice so that the result is a square again. In this square one of the corners is cut off. Then the paper is folded out. Which sample below cannot be obtained in this way?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane194.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4614981459566856, 19.309501465266326], ylim=[-5.749671806492165, 14.021327804730847]) as c:
            c.path([[4, 6], [7, 6], [7, 9], [4, 9], [4, 6]], [1, 2, 2, 2, 79], id='o0')
            c.line([[5.5, 6], [5.5, 9]], id='o1', linestyle=(0, [4, 3]))
            c.path([[8, 6], [9.5, 6], [9.5, 9], [8, 9], [8, 6]], [1, 2, 2, 2, 79], id='o2')
            c.line([[8, 7.5], [9.5, 7.5]], id='o3', linestyle=(0, [4, 3]))
            c.path([[10.5, 6.6], [12.0, 6.6], [12.0, 8.1], [10.5, 8.1], [10.5, 6.6]], [1, 2, 2, 2, 79], id='o4')
            c.path([[13.2, 6.6], [14.7, 6.6], [14.7, 7.35], [13.95, 8.1], [13.2, 8.1], [13.2, 6.6]], [1, 2, 2, 2, 2, 79], id='o5')
            c.line([[13.95, 8.1], [14.7, 8.1]], id='o6', linestyle=(0, [4, 3]))
            c.line([[14.7, 8.1], [14.7, 7.35]], id='o7', linestyle=(0, [4, 3]))
            for object_id, vertices, codes in [('o8', [[0.55, 0], [2.25, 0], [2.8, 0.55], [2.8, 2.25], [2.25, 2.8], [0.55, 2.8], [0, 2.25], [0, 0.55], [0.55, 0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('o9', [[4, 0], [4.9, 0], [5.4, 0.5], [5.9, 0], [6.8, 0], [6.8, 2.8], [5.9, 2.8], [5.4, 2.3], [4.9, 2.8], [4, 2.8], [4, 0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('o10', [[8, 0], [10.8, 0], [10.8, 2.8], [8, 2.8], [8, 0]], [1, 2, 2, 2, 79]), ('o11', [[8.85, 1.4], [9.4, 0.85], [9.95, 1.4], [9.4, 1.95], [8.85, 1.4]], [1, 2, 2, 2, 79]), ('o12', [[12, 0], [14.8, 0], [14.8, 0.9], [14.3, 1.4], [14.8, 1.9], [14.8, 2.8], [12, 2.8], [12, 1.9], [12.5, 1.4], [12, 0.9], [12, 0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('o13', [[16, 0], [18.8, 0], [18.8, 2.8], [16, 2.8], [16, 0]], [1, 2, 2, 2, 79]), ('o14', [[17, 1], [17.8, 1], [17.8, 1.8], [17, 1.8], [17, 1]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('t0', 'A', [1.4, -0.6]), ('t1', 'B', [5.4, -0.6]), ('t2', 'C', [9.4, -0.6]), ('t3', 'D', [13.4, -0.6]), ('t4', 'E', [17.4, -0.6])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane194().draw(sys.argv[1] if len(sys.argv) > 1 else None))
