"""Frozen question Plane190; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane190:

    def __init__(self):
        self.id = 'Plane190'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:419'
        self.question = 'A square piece of paper has been cut in three pieces. Two of them are in the picture on the right. What is the third one?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane190.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0541089856614807, 18.45277253047299], ylim=[-6.75789206620677, 12.7489894499277]) as c:
            for object_id, vertices, codes in [('piece1', [[6, 4], [7, 5], [7, 6], [6, 6], [6, 4]], [1, 2, 2, 2, 79]), ('piece2', [[8, 4], [10, 4], [10, 5], [9, 5], [8, 4]], [1, 2, 2, 2, 79]), ('A', [[0, 0], [1, 0], [2, 1], [1, 1], [0, 0]], [1, 2, 2, 2, 79]), ('B', [[4, 0], [5, 0], [5, 1], [4, 1], [4, 0]], [1, 2, 2, 2, 79]), ('C', [[8, 0], [10, 0], [10, 1], [8, 1], [8, 0]], [1, 2, 2, 2, 79]), ('D', [[12, 0], [14, 0], [14, 1], [13, 1], [12, 0]], [1, 2, 2, 2, 79]), ('E', [[16, 0], [18, 0], [17.5, 1], [16.5, 1], [16, 0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', [-0.4, 1.25]), ('label1', 'B', [3.6, 1.25]), ('label2', 'C', [7.6, 1.25]), ('label3', 'D', [11.6, 1.25]), ('label4', 'E', [15.6, 1.25])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane190().draw(sys.argv[1] if len(sys.argv) > 1 else None))
