"""Frozen question Plane288; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane288:

    def __init__(self):
        self.id = 'Plane288'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:864'
        self.question = 'What is the maximum number of pieces of the shape shown that can be cut from a 5 x 5 square?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('given_0', [[1, 7], [1, 8]]),
         ('given_1', [[1, 7], [2, 7]]),
         ('given_2', [[1, 8], [2, 8]]),
         ('given_3', [[2, 7], [2, 8]]),
         ('given_4', [[2, 7], [3, 7]]),
         ('given_5', [[2, 8], [3, 8]]),
         ('given_6', [[3, 7], [3, 8]]),
         ('given_7', [[3, 7], [4, 7]]),
         ('given_8', [[3, 8], [3, 9]]),
         ('given_9', [[3, 8], [4, 8]]),
         ('given_10', [[3, 9], [4, 9]]),
         ('given_11', [[4, 7], [4, 8]]),
         ('given_12', [[4, 8], [4, 9]]),
         ('board_0', [[0, 0], [0, 1]]),
         ('board_1', [[0, 0], [1, 0]]),
         ('board_2', [[0, 1], [0, 2]]),
         ('board_3', [[0, 1], [1, 1]]),
         ('board_4', [[0, 2], [0, 3]]),
         ('board_5', [[0, 2], [1, 2]]),
         ('board_6', [[0, 3], [0, 4]]),
         ('board_7', [[0, 3], [1, 3]]),
         ('board_8', [[0, 4], [0, 5]]),
         ('board_9', [[0, 4], [1, 4]]),
         ('board_10', [[0, 5], [1, 5]]),
         ('board_11', [[1, 0], [1, 1]]),
         ('board_12', [[1, 0], [2, 0]]),
         ('board_13', [[1, 1], [1, 2]]),
         ('board_14', [[1, 1], [2, 1]]),
         ('board_15', [[1, 2], [1, 3]]),
         ('board_16', [[1, 2], [2, 2]]),
         ('board_17', [[1, 3], [1, 4]]),
         ('board_18', [[1, 3], [2, 3]]),
         ('board_19', [[1, 4], [1, 5]]),
         ('board_20', [[1, 4], [2, 4]]),
         ('board_21', [[1, 5], [2, 5]]),
         ('board_22', [[2, 0], [2, 1]]),
         ('board_23', [[2, 0], [3, 0]]),
         ('board_24', [[2, 1], [2, 2]]),
         ('board_25', [[2, 1], [3, 1]]),
         ('board_26', [[2, 2], [2, 3]]),
         ('board_27', [[2, 2], [3, 2]]),
         ('board_28', [[2, 3], [2, 4]]),
         ('board_29', [[2, 3], [3, 3]]),
         ('board_30', [[2, 4], [2, 5]]),
         ('board_31', [[2, 4], [3, 4]]),
         ('board_32', [[2, 5], [3, 5]]),
         ('board_33', [[3, 0], [3, 1]]),
         ('board_34', [[3, 0], [4, 0]]),
         ('board_35', [[3, 1], [3, 2]]),
         ('board_36', [[3, 1], [4, 1]]),
         ('board_37', [[3, 2], [3, 3]]),
         ('board_38', [[3, 2], [4, 2]]),
         ('board_39', [[3, 3], [3, 4]]),
         ('board_40', [[3, 3], [4, 3]]),
         ('board_41', [[3, 4], [3, 5]]),
         ('board_42', [[3, 4], [4, 4]]),
         ('board_43', [[3, 5], [4, 5]]),
         ('board_44', [[4, 0], [4, 1]]),
         ('board_45', [[4, 0], [5, 0]]),
         ('board_46', [[4, 1], [4, 2]]),
         ('board_47', [[4, 1], [5, 1]]),
         ('board_48', [[4, 2], [4, 3]]),
         ('board_49', [[4, 2], [5, 2]]),
         ('board_50', [[4, 3], [4, 4]]),
         ('board_51', [[4, 3], [5, 3]]),
         ('board_52', [[4, 4], [4, 5]]),
         ('board_53', [[4, 4], [5, 4]]),
         ('board_54', [[4, 5], [5, 5]]),
         ('board_55', [[5, 0], [5, 1]]),
         ('board_56', [[5, 1], [5, 2]]),
         ('board_57', [[5, 2], [5, 3]]),
         ('board_58', [[5, 3], [5, 4]]),
         ('board_59', [[5, 4], [5, 5]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane288.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.228296855985385, 7.236238666357113], ylim=[-0.24077445742880954, 9.223761064913688]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane288().draw(sys.argv[1] if len(sys.argv) > 1 else None))
