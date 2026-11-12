"""Frozen question Plane249; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane249:

    def __init__(self):
        self.id = 'Plane249'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:716'
        self.question = 'What is the smallest number of little squares that need to be painted to get at least one axis of symmetry in the picture?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [('white_grid_0', [[0.0, 0.0], [0.0, 1.0]]),
         ('white_grid_1', [[0.0, 0.0], [1.0, 0.0]]),
         ('white_grid_2', [[0.0, 1.0], [1.0, 1.0]]),
         ('white_grid_3', [[0.0, 2.0], [0.0, 3.0]]),
         ('white_grid_4', [[0.0, 2.0], [1.0, 2.0]]),
         ('white_grid_5', [[0.0, 3.0], [0.0, 4.0]]),
         ('white_grid_6', [[0.0, 3.0], [1.0, 3.0]]),
         ('white_grid_7', [[0.0, 4.0], [1.0, 4.0]]),
         ('white_grid_8', [[1.0, 0.0], [1.0, 1.0]]),
         ('white_grid_9', [[1.0, 0.0], [2.0, 0.0]]),
         ('white_grid_10', [[1.0, 1.0], [1.0, 2.0]]),
         ('white_grid_11', [[1.0, 1.0], [2.0, 1.0]]),
         ('white_grid_12', [[1.0, 2.0], [1.0, 3.0]]),
         ('white_grid_13', [[1.0, 2.0], [2.0, 2.0]]),
         ('white_grid_14', [[1.0, 3.0], [1.0, 4.0]]),
         ('white_grid_15', [[1.0, 3.0], [2.0, 3.0]]),
         ('white_grid_16', [[1.0, 4.0], [2.0, 4.0]]),
         ('white_grid_17', [[2.0, 0.0], [2.0, 1.0]]),
         ('white_grid_18', [[2.0, 0.0], [3.0, 0.0]]),
         ('white_grid_19', [[2.0, 1.0], [2.0, 2.0]]),
         ('white_grid_20', [[2.0, 1.0], [3.0, 1.0]]),
         ('white_grid_21', [[2.0, 2.0], [2.0, 3.0]]),
         ('white_grid_22', [[2.0, 2.0], [3.0, 2.0]]),
         ('white_grid_23', [[2.0, 3.0], [2.0, 4.0]]),
         ('white_grid_24', [[3.0, 0.0], [3.0, 1.0]]),
         ('white_grid_25', [[3.0, 1.0], [3.0, 2.0]]),
         ('white_grid_26', [[3.0, 1.0], [4.0, 1.0]]),
         ('white_grid_27', [[3.0, 2.0], [3.0, 3.0]]),
         ('white_grid_28', [[3.0, 2.0], [4.0, 2.0]]),
         ('white_grid_29', [[3.0, 3.0], [4.0, 3.0]]),
         ('white_grid_30', [[4.0, 1.0], [4.0, 2.0]]),
         ('white_grid_31', [[4.0, 2.0], [4.0, 3.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane249.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1016344986486386, 4.10848473551341], ylim=[-0.10749905020093209, 4.1026201839611165], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black01', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black01', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='black23', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='black23', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='black33', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='black33', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='black22', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='black22', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='black30', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='black30', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 4.0], [0.0, 4.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='boundary', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane249().draw(sys.argv[1] if len(sys.argv) > 1 else None))
