"""Frozen question Plane228; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane228:

    def __init__(self):
        self.id = 'Plane228'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:609'
        self.question = 'One square is removed from the shape shown.\nHow many of the following 5 shapes can result?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('source_0', [[10, 6], [10, 7]]),
         ('source_1', [[10, 6], [11, 6]]),
         ('source_2', [[10, 7], [11, 7]]),
         ('source_3', [[11, 6], [11, 7]]),
         ('source_4', [[11, 6], [12, 6]]),
         ('source_5', [[11, 7], [11, 8]]),
         ('source_6', [[11, 7], [12, 7]]),
         ('source_7', [[11, 8], [11, 9]]),
         ('source_8', [[11, 8], [12, 8]]),
         ('source_9', [[11, 9], [12, 9]]),
         ('source_10', [[12, 6], [12, 7]]),
         ('source_11', [[12, 7], [12, 8]]),
         ('source_12', [[12, 7], [13, 7]]),
         ('source_13', [[12, 8], [12, 9]]),
         ('source_14', [[12, 8], [13, 8]]),
         ('source_15', [[13, 7], [13, 8]]),
         ('option0_0', [[0, 0], [0, 1]]),
         ('option0_1', [[0, 0], [1, 0]]),
         ('option0_2', [[0, 1], [0, 2]]),
         ('option0_3', [[0, 1], [1, 1]]),
         ('option0_4', [[0, 2], [1, 2]]),
         ('option0_5', [[1, 0], [1, 1]]),
         ('option0_6', [[1, 0], [2, 0]]),
         ('option0_7', [[1, 1], [1, 2]]),
         ('option0_8', [[1, 1], [2, 1]]),
         ('option0_9', [[2, 0], [2, 1]]),
         ('option0_10', [[2, 0], [3, 0]]),
         ('option0_11', [[2, 1], [3, 1]]),
         ('option0_12', [[3, 0], [3, 1]]),
         ('option1_0', [[6, 0], [6, 1]]),
         ('option1_1', [[6, 0], [7, 0]]),
         ('option1_2', [[6, 1], [7, 1]]),
         ('option1_3', [[7, 0], [7, 1]]),
         ('option1_4', [[7, 0], [8, 0]]),
         ('option1_5', [[7, 1], [7, 2]]),
         ('option1_6', [[7, 1], [8, 1]]),
         ('option1_7', [[7, 2], [8, 2]]),
         ('option1_8', [[8, 0], [8, 1]]),
         ('option1_9', [[8, 0], [9, 0]]),
         ('option1_10', [[8, 1], [8, 2]]),
         ('option1_11', [[8, 1], [9, 1]]),
         ('option1_12', [[9, 0], [9, 1]]),
         ('option2_0', [[12, 1], [12, 2]]),
         ('option2_1', [[12, 1], [13, 1]]),
         ('option2_2', [[12, 2], [12, 3]]),
         ('option2_3', [[12, 2], [13, 2]]),
         ('option2_4', [[12, 3], [13, 3]]),
         ('option2_5', [[13, 0], [13, 1]]),
         ('option2_6', [[13, 0], [14, 0]]),
         ('option2_7', [[13, 1], [13, 2]]),
         ('option2_8', [[13, 1], [14, 1]]),
         ('option2_9', [[13, 2], [13, 3]]),
         ('option2_10', [[13, 2], [14, 2]]),
         ('option2_11', [[14, 0], [14, 1]]),
         ('option2_12', [[14, 1], [14, 2]]),
         ('option3_0', [[18, 0], [18, 1]]),
         ('option3_1', [[18, 0], [19, 0]]),
         ('option3_2', [[18, 1], [18, 2]]),
         ('option3_3', [[18, 1], [19, 1]]),
         ('option3_4', [[18, 2], [19, 2]]),
         ('option3_5', [[19, 0], [19, 1]]),
         ('option3_6', [[19, 0], [20, 0]]),
         ('option3_7', [[19, 1], [19, 2]]),
         ('option3_8', [[19, 1], [20, 1]]),
         ('option3_9', [[19, 2], [20, 2]]),
         ('option3_10', [[20, 0], [20, 1]]),
         ('option3_11', [[20, 1], [20, 2]]),
         ('option4_0', [[24, 0], [24, 1]]),
         ('option4_1', [[24, 0], [25, 0]]),
         ('option4_2', [[24, 1], [25, 1]]),
         ('option4_3', [[25, 0], [25, 1]]),
         ('option4_4', [[25, 0], [26, 0]]),
         ('option4_5', [[25, 1], [26, 1]]),
         ('option4_6', [[26, 0], [26, 1]]),
         ('option4_7', [[26, 0], [27, 0]]),
         ('option4_8', [[26, 1], [27, 1]]),
         ('option4_9', [[27, 0], [27, 1]]),
         ('option4_10', [[27, 0], [28, 0]]),
         ('option4_11', [[27, 1], [28, 1]]),
         ('option4_12', [[28, 0], [28, 1]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane228.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.6774595292423111, 28.759113878580365], ylim=[-10.24080161450386, 19.19577179331882]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane228().draw(sys.argv[1] if len(sys.argv) > 1 else None))
