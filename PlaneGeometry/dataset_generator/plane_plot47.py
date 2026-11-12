"""Frozen question Plane47; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane47:

    def __init__(self):
        self.id = 'Plane47'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/526'
        self.question = 'What has been done to this letter?\nChoices:\nA: slide\nB: flip\nC: turn'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'slide', 'B': 'flip', 'C': 'turn'}
        self.query = self.question
        self._geometry_01 = [('segment_1', [[0.0, 0.0], [0.0, 5.0]]),
         ('segment_2', [[0.0, 0.0], [5.0, 0.0]]),
         ('segment_3', [[1.0, 0.0], [1.0, 5.0]]),
         ('segment_4', [[0.0, 1.0], [5.0, 1.0]]),
         ('segment_5', [[2.0, 0.0], [2.0, 5.0]]),
         ('segment_6', [[0.0, 2.0], [5.0, 2.0]]),
         ('segment_7', [[3.0, 0.0], [3.0, 5.0]]),
         ('segment_8', [[0.0, 3.0], [5.0, 3.0]]),
         ('segment_9', [[4.0, 0.0], [4.0, 5.0]]),
         ('segment_10', [[0.0, 4.0], [5.0, 4.0]]),
         ('segment_11', [[5.0, 0.0], [5.0, 5.0]]),
         ('segment_12', [[0.0, 5.0], [5.0, 5.0]]),
         ('segment_13', [[7.5, 0.0], [7.5, 5.0]]),
         ('segment_14', [[7.5, 0.0], [12.5, 0.0]]),
         ('segment_15', [[8.5, 0.0], [8.5, 5.0]]),
         ('segment_16', [[7.5, 1.0], [12.5, 1.0]]),
         ('segment_17', [[9.5, 0.0], [9.5, 5.0]]),
         ('segment_18', [[7.5, 2.0], [12.5, 2.0]]),
         ('segment_19', [[10.5, 0.0], [10.5, 5.0]]),
         ('segment_20', [[7.5, 3.0], [12.5, 3.0]]),
         ('segment_21', [[11.5, 0.0], [11.5, 5.0]]),
         ('segment_22', [[7.5, 4.0], [12.5, 4.0]]),
         ('segment_23', [[12.5, 0.0], [12.5, 5.0]]),
         ('segment_24', [[7.5, 5.0], [12.5, 5.0]]),
         ('segment_25', [[5.0, 0.0], [7.5, 0.0]]),
         ('segment_26', [[5.0, 5.0], [7.5, 5.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane47.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.31484987429958444, 12.838359712262548), ylim=(-4.088359712262548, 9.064849874299584), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[2.7, 3.75], [3.15, 3.75], [3.15, 1.65], [3.03, 1.31], [2.78, 1.12], [2.35, 1.03], [1.98, 1.11], [1.66, 1.3], [1.43, 1.69], [1.94, 1.69], [2.1, 1.5], [2.4, 1.45], [2.61, 1.53], [2.7, 1.73], [2.7, 3.75]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[2.7, 3.75], [3.15, 3.75], [3.15, 1.65], [3.03, 1.31], [2.78, 1.12], [2.35, 1.03], [1.98, 1.11], [1.66, 1.3], [1.43, 1.69], [1.94, 1.69], [2.1, 1.5], [2.4, 1.45], [2.61, 1.53], [2.7, 1.73], [2.7, 3.75]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='polygon_27', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.2, 4.45], [10.65, 4.45], [10.65, 2.3499999999999996], [10.53, 2.01], [10.28, 1.82], [9.85, 1.73], [9.48, 1.81], [9.16, 2.0], [8.93, 2.3899999999999997], [9.44, 2.3899999999999997], [9.6, 2.2], [9.9, 2.15], [10.11, 2.23], [10.2, 2.4299999999999997], [10.2, 4.45]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[10.2, 4.45], [10.65, 4.45], [10.65, 2.3499999999999996], [10.53, 2.01], [10.28, 1.82], [9.85, 1.73], [9.48, 1.81], [9.16, 2.0], [8.93, 2.3899999999999997], [9.44, 2.3899999999999997], [9.6, 2.2], [9.9, 2.15], [10.11, 2.23], [10.2, 2.4299999999999997], [10.2, 4.45]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='polygon_28', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('segment_29', [[5.4, 2.5], [7.1, 2.5]]), ('segment_30', [[6.65, 2.9], [7.1, 2.5]]), ('segment_31', [[6.65, 2.1], [7.1, 2.5]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane47().draw(sys.argv[1] if len(sys.argv) > 1 else None))
