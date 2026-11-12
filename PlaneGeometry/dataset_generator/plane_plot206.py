"""Frozen question Plane206; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane206:

    def __init__(self):
        self.id = 'Plane206'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:493'
        self.question = 'Two $L$ shapes are made from 8 squares. How many of the following 4 shapes can be formed using both $L$ shapes?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('source_0', [[9, 7], [9, 8]]),
         ('source_1', [[9, 7], [10, 7]]),
         ('source_2', [[9, 8], [10, 8]]),
         ('source_3', [[10, 7], [10, 8]]),
         ('source_4', [[10, 7], [11, 7]]),
         ('source_5', [[10, 8], [11, 8]]),
         ('source_6', [[11, 7], [11, 8]]),
         ('source_7', [[11, 7], [12, 7]]),
         ('source_8', [[11, 8], [11, 9]]),
         ('source_9', [[11, 8], [12, 8]]),
         ('source_10', [[11, 9], [12, 9]]),
         ('source_11', [[12, 7], [12, 8]]),
         ('source_12', [[12, 8], [12, 9]]),
         ('option0_0', [[0, 0], [0, 1]]),
         ('option0_1', [[0, 0], [1, 0]]),
         ('option0_2', [[0, 1], [0, 2]]),
         ('option0_3', [[0, 1], [1, 1]]),
         ('option0_4', [[0, 2], [0, 3]]),
         ('option0_5', [[0, 2], [1, 2]]),
         ('option0_6', [[0, 3], [0, 4]]),
         ('option0_7', [[0, 3], [1, 3]]),
         ('option0_8', [[0, 4], [1, 4]]),
         ('option0_9', [[1, 0], [1, 1]]),
         ('option0_10', [[1, 0], [2, 0]]),
         ('option0_11', [[1, 1], [1, 2]]),
         ('option0_12', [[1, 1], [2, 1]]),
         ('option0_13', [[1, 2], [1, 3]]),
         ('option0_14', [[1, 2], [2, 2]]),
         ('option0_15', [[1, 3], [1, 4]]),
         ('option0_16', [[1, 3], [2, 3]]),
         ('option0_17', [[1, 4], [2, 4]]),
         ('option0_18', [[2, 0], [2, 1]]),
         ('option0_19', [[2, 1], [2, 2]]),
         ('option0_20', [[2, 2], [2, 3]]),
         ('option0_21', [[2, 3], [2, 4]]),
         ('option1_0', [[6, 0], [6, 1]]),
         ('option1_1', [[6, 0], [7, 0]]),
         ('option1_2', [[6, 1], [6, 2]]),
         ('option1_3', [[6, 1], [7, 1]]),
         ('option1_4', [[6, 2], [6, 3]]),
         ('option1_5', [[6, 2], [7, 2]]),
         ('option1_6', [[6, 3], [7, 3]]),
         ('option1_7', [[7, 0], [7, 1]]),
         ('option1_8', [[7, 0], [8, 0]]),
         ('option1_9', [[7, 1], [7, 2]]),
         ('option1_10', [[7, 1], [8, 1]]),
         ('option1_11', [[7, 2], [7, 3]]),
         ('option1_12', [[7, 2], [8, 2]]),
         ('option1_13', [[7, 3], [7, 4]]),
         ('option1_14', [[7, 3], [8, 3]]),
         ('option1_15', [[7, 4], [8, 4]]),
         ('option1_16', [[8, 0], [8, 1]]),
         ('option1_17', [[8, 1], [8, 2]]),
         ('option1_18', [[8, 1], [9, 1]]),
         ('option1_19', [[8, 2], [8, 3]]),
         ('option1_20', [[8, 2], [9, 2]]),
         ('option1_21', [[8, 3], [8, 4]]),
         ('option1_22', [[9, 1], [9, 2]]),
         ('option2_0', [[12, 2], [12, 3]]),
         ('option2_1', [[12, 2], [13, 2]]),
         ('option2_2', [[12, 3], [12, 4]]),
         ('option2_3', [[12, 3], [13, 3]]),
         ('option2_4', [[12, 4], [13, 4]]),
         ('option2_5', [[13, 0], [13, 1]]),
         ('option2_6', [[13, 0], [14, 0]]),
         ('option2_7', [[13, 1], [13, 2]]),
         ('option2_8', [[13, 1], [14, 1]]),
         ('option2_9', [[13, 2], [13, 3]]),
         ('option2_10', [[13, 2], [14, 2]]),
         ('option2_11', [[13, 3], [13, 4]]),
         ('option2_12', [[13, 3], [14, 3]]),
         ('option2_13', [[13, 4], [14, 4]]),
         ('option2_14', [[14, 0], [14, 1]]),
         ('option2_15', [[14, 0], [15, 0]]),
         ('option2_16', [[14, 1], [14, 2]]),
         ('option2_17', [[14, 1], [15, 1]]),
         ('option2_18', [[14, 2], [14, 3]]),
         ('option2_19', [[14, 3], [14, 4]]),
         ('option2_20', [[14, 3], [15, 3]]),
         ('option2_21', [[14, 4], [15, 4]]),
         ('option2_22', [[15, 0], [15, 1]]),
         ('option2_23', [[15, 3], [15, 4]]),
         ('option3_0', [[18, 0], [18, 1]]),
         ('option3_1', [[18, 0], [19, 0]]),
         ('option3_2', [[18, 1], [18, 2]]),
         ('option3_3', [[18, 1], [19, 1]]),
         ('option3_4', [[18, 2], [18, 3]]),
         ('option3_5', [[18, 2], [19, 2]]),
         ('option3_6', [[18, 3], [18, 4]]),
         ('option3_7', [[18, 3], [19, 3]]),
         ('option3_8', [[18, 4], [19, 4]]),
         ('option3_9', [[19, 0], [19, 1]]),
         ('option3_10', [[19, 0], [20, 0]]),
         ('option3_11', [[19, 1], [19, 2]]),
         ('option3_12', [[19, 1], [20, 1]]),
         ('option3_13', [[19, 2], [19, 3]]),
         ('option3_14', [[19, 2], [20, 2]]),
         ('option3_15', [[19, 3], [19, 4]]),
         ('option3_16', [[20, 0], [20, 1]]),
         ('option3_17', [[20, 0], [21, 0]]),
         ('option3_18', [[20, 1], [20, 2]]),
         ('option3_19', [[20, 1], [21, 1]]),
         ('option3_20', [[20, 2], [21, 2]]),
         ('option3_21', [[21, 0], [21, 1]]),
         ('option3_22', [[21, 1], [21, 2]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane206.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5372698625248731, 21.5698410116779], ylim=[-6.56531645899594, 15.541794415206834]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane206().draw(sys.argv[1] if len(sys.argv) > 1 else None))
