"""Frozen question Plane248; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane248:

    def __init__(self):
        self.id = 'Plane248'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:713'
        self.question = 'Two identical pieces may be rotated but may not be turned upside down. Which of the following pictures cannot be made with these two pieces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane248.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.3532246852867402, 27.67854144687496], ylim=[-11.02219427296967, 18.00957185919203]) as c:
            for object_id, vertices, codes in [('source0', [[8, 6], [9, 7], [10, 6], [10, 5], [9, 5], [9, 6], [8, 6]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11, 6], [12, 7], [13, 6], [13, 5], [12, 5], [12, 6], [11, 6]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0, 2], [1, 2], [1, 1], [2, 2], [3, 1], [3, 0], [2, 0], [2, 1], [1, 0], [0, 1], [0, 2]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6, 1], [7, 2], [8, 2], [9, 1], [8, 0], [7, 0], [6, 1]], [1, 2, 2, 2, 2, 2, 79]), ('option2', [[12, 1], [13, 2], [15, 2], [15, 3], [16, 2], [15, 1], [13, 1], [13, 0], [12, 1]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18, 0], [19, 0], [21, 2], [21, 3], [20, 3], [20, 2], [19, 2], [19, 1], [18, 1], [18, 0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24, 1], [25, 1], [26, 0], [26, 1], [27, 1], [27, 2], [26, 2], [25, 3], [25, 2], [24, 2], [24, 1]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', [-0.4, 3.3]), ('label1', 'B', [5.6, 3.3]), ('label2', 'C', [11.6, 3.3]), ('label3', 'D', [17.6, 3.3]), ('label4', 'E', [23.6, 3.3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane248().draw(sys.argv[1] if len(sys.argv) > 1 else None))
