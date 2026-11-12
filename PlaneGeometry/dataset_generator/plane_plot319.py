"""Frozen question Plane319; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane319:

    def __init__(self):
        self.id = 'Plane319'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1005'
        self.question = 'The figure on the left is composed of the smaller three-square and four-square figures shown on the right. The smaller figures may be rotated but not turned over. What is the smallest number of three-square figures needed?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('target_0', [[0, 0], [0, 1]]),
         ('target_1', [[0, 0], [1, 0]]),
         ('target_2', [[0, 1], [0, 2]]),
         ('target_3', [[0, 1], [1, 1]]),
         ('target_4', [[0, 2], [0, 3]]),
         ('target_5', [[0, 2], [1, 2]]),
         ('target_6', [[0, 3], [0, 4]]),
         ('target_7', [[0, 3], [1, 3]]),
         ('target_8', [[0, 4], [0, 5]]),
         ('target_9', [[0, 4], [1, 4]]),
         ('target_10', [[0, 5], [1, 5]]),
         ('target_11', [[1, 0], [1, 1]]),
         ('target_12', [[1, 0], [2, 0]]),
         ('target_13', [[1, 1], [1, 2]]),
         ('target_14', [[1, 1], [2, 1]]),
         ('target_15', [[1, 2], [1, 3]]),
         ('target_16', [[1, 2], [2, 2]]),
         ('target_17', [[1, 3], [1, 4]]),
         ('target_18', [[1, 3], [2, 3]]),
         ('target_19', [[1, 4], [1, 5]]),
         ('target_20', [[1, 4], [2, 4]]),
         ('target_21', [[1, 5], [2, 5]]),
         ('target_22', [[2, 0], [2, 1]]),
         ('target_23', [[2, 0], [3, 0]]),
         ('target_24', [[2, 1], [2, 2]]),
         ('target_25', [[2, 1], [3, 1]]),
         ('target_26', [[2, 2], [2, 3]]),
         ('target_27', [[2, 2], [3, 2]]),
         ('target_28', [[2, 3], [2, 4]]),
         ('target_29', [[2, 3], [3, 3]]),
         ('target_30', [[2, 4], [2, 5]]),
         ('target_31', [[2, 4], [3, 4]]),
         ('target_32', [[2, 5], [3, 5]]),
         ('target_33', [[3, 0], [3, 1]]),
         ('target_34', [[3, 0], [4, 0]]),
         ('target_35', [[3, 1], [3, 2]]),
         ('target_36', [[3, 1], [4, 1]]),
         ('target_37', [[3, 2], [3, 3]]),
         ('target_38', [[3, 2], [4, 2]]),
         ('target_39', [[3, 3], [3, 4]]),
         ('target_40', [[3, 3], [4, 3]]),
         ('target_41', [[3, 4], [3, 5]]),
         ('target_42', [[3, 4], [4, 4]]),
         ('target_43', [[3, 5], [4, 5]]),
         ('target_44', [[4, 0], [4, 1]]),
         ('target_45', [[4, 0], [5, 0]]),
         ('target_46', [[4, 1], [4, 2]]),
         ('target_47', [[4, 1], [5, 1]]),
         ('target_48', [[4, 2], [4, 3]]),
         ('target_49', [[4, 2], [5, 2]]),
         ('target_50', [[4, 3], [4, 4]]),
         ('target_51', [[4, 4], [4, 5]]),
         ('target_52', [[5, 0], [5, 1]]),
         ('target_53', [[5, 1], [5, 2]]),
         ('triomino_0', [[7, 3], [7, 4]]),
         ('triomino_1', [[7, 3], [8, 3]]),
         ('triomino_2', [[7, 4], [7, 5]]),
         ('triomino_3', [[7, 4], [8, 4]]),
         ('triomino_4', [[7, 5], [8, 5]]),
         ('triomino_5', [[8, 3], [8, 4]]),
         ('triomino_6', [[8, 4], [8, 5]]),
         ('triomino_7', [[8, 4], [9, 4]]),
         ('triomino_8', [[8, 5], [9, 5]]),
         ('triomino_9', [[9, 4], [9, 5]]),
         ('tetromino_0', [[7, 0], [7, 1]]),
         ('tetromino_1', [[7, 0], [8, 0]]),
         ('tetromino_2', [[7, 1], [7, 2]]),
         ('tetromino_3', [[7, 1], [8, 1]]),
         ('tetromino_4', [[7, 2], [8, 2]]),
         ('tetromino_5', [[8, 0], [8, 1]]),
         ('tetromino_6', [[8, 1], [8, 2]]),
         ('tetromino_7', [[8, 1], [9, 1]]),
         ('tetromino_8', [[8, 2], [9, 2]]),
         ('tetromino_9', [[9, 1], [9, 2]]),
         ('tetromino_10', [[9, 1], [10, 1]]),
         ('tetromino_11', [[9, 2], [10, 2]]),
         ('tetromino_12', [[10, 1], [10, 2]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane319.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2532566720140723, 10.260325861826704], ylim=[-2.763851227801813, 7.7497313060389645]) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane319().draw(sys.argv[1] if len(sys.argv) > 1 else None))
