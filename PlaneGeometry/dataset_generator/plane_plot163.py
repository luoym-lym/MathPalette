"""Frozen question Plane163; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane163:

    def __init__(self):
        self.id = 'Plane163'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:119'
        self.question = 'Three sticks are arranged as shown. Without breaking or bending the sticks, which shape can be made?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane163.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.4504749183223646, 17.327659913032356], ylim=[-9.856388555341482, 9.921746276013238]) as c:
            for object_id, points in [('option0_stick0', [[-1, 0], [1, 0]]), ('option0_stick1', [[0, -1], [0, 1]]), ('option0_stick2', [[-0.71, -0.71], [0.71, 0.71]]), ('option0_stick3', [[-0.71, 0.71], [0.71, -0.71]]), ('option1_stick0', [[3.5, -1], [3.5, 1]]), ('option1_stick1', [[4.5, -1], [4.5, 1]]), ('option1_stick2', [[3.29, -0.71], [4.71, 0.71]]), ('option1_stick3', [[3.29, 0.71], [4.71, -0.71]]), ('option2_stick0', [[7.2, 0.2], [8.6, 1.6]]), ('option2_stick1', [[8.2, -1.2], [9.6, 0.2]]), ('option2_stick2', [[7.5, 0.5], [8.9, -0.9]]), ('option2_stick3', [[8.2, 1.2], [9.6, -0.2]]), ('option3_stick0', [[10.8, -0.3], [12.3, 1.2]]), ('option3_stick1', [[11.7, -1.2], [13.2, 0.3]]), ('option3_stick2', [[11.7, 1.2], [13.2, -0.3]]), ('option3_stick3', [[10.8, 0.3], [12.3, -1.2]]), ('option4_stick0', [[16, -1], [16, 1]]), ('option4_stick1', [[15.134, -0.5], [16.866, 0.5]]), ('option4_stick2', [[15.134, 0.5], [16.866, -0.5]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', [-1.6, -1.3]), ('label1', '(B)', [2.4, -1.3]), ('label2', '(C)', [6.4, -1.3]), ('label3', '(D)', [10.4, -1.3]), ('label4', '(E)', [14.4, -1.3])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane163().draw(sys.argv[1] if len(sys.argv) > 1 else None))
