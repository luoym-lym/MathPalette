"""Frozen question Plane195; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane195:

    def __init__(self):
        self.id = 'Plane195'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:451'
        self.question = 'Two equilateral triangular cards are placed beside each other or with one partly covering the other. The outline of the two cards is traced on a sheet of paper. Which of the following shapes cannot be obtained?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane195.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.611269070719386, 22.61017902865146], ylim=[-8.757989029445206, 15.46345906992564]) as c:
            for object_id, vertices, codes in [('given0', [[8, 5], [10, 5], [9, 6.732050807568877], [8, 5]], [1, 2, 2, 79]), ('given1', [[11, 5], [13, 5], [12, 6.732050807568877], [11, 5]], [1, 2, 2, 79]), ('option0', [[-1, 0], [1, 0], [0.4, 1.0392304845413263], [1, 2.0784609690826525], [-1, 2.0784609690826525], [-0.4, 1.0392304845413263], [-1, 0]], [1, 2, 2, 2, 2, 2, 79]), ('option1', [[3.267949192431123, 1], [5, 2], [6.732050807568877, 1], [5, 0], [3.267949192431123, 1]], [1, 2, 2, 2, 79]), ('option2', [[10, 2], [11.039230484541326, 1.4], [11.039230484541326, 2], [12.771281292110203, 1], [11.039230484541326, 0], [11.039230484541326, 0.6], [10, 0], [10, 2]], [1, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[15, 2.0], [15.433012701892219, 1.75], [16.73205080756888, 2.5], [16.73205080756888, 0.5], [16.299038105676658, 0.75], [15, 0.0], [15, 2.0]], [1, 2, 2, 2, 2, 2, 79]), ('option4', [[20, 0], [22, 0], [22, 1.6], [20, 1.6], [20, 0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', [-0.8, 3]), ('label1', 'B', [4.2, 3]), ('label2', 'C', [9.2, 3]), ('label3', 'D', [14.2, 3]), ('label4', 'E', [19.2, 3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane195().draw(sys.argv[1] if len(sys.argv) > 1 else None))
