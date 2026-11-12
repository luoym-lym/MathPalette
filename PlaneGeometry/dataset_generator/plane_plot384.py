"""Frozen question Plane384; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane384:

    def __init__(self):
        self.id = 'Plane384'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1542'
        self.question = 'What is the least number of additional small squares that must be shaded in the diagram on the right so that the whole diagram has a line of symmetry?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane384.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2230502095313236, 9.238034935319352], ylim=[-0.2380349353193525, 9.223050209531323], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('cell2', [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), ('cell3', [[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79]), ('cell4', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79]), ('cell5', [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell7', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell8', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('cell10', [[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79]), ('cell11', [[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79]), ('cell12', [[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell13', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell13', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell14', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell15', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell15', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('cell16', [[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79]), ('cell17', [[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79]), ('cell18', [[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79]), ('cell19', [[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79]), ('cell20', [[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79]), ('cell21', [[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell22', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell22', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('cell23', [[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79]), ('cell24', [[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79]), ('cell25', [[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79]), ('cell26', [[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79]), ('cell27', [[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79]), ('cell28', [[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79]), ('cell29', [[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79]), ('cell30', [[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79]), ('cell31', [[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79]), ('cell32', [[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79]), ('cell33', [[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell34', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell34', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell35', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell36', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell36', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('cell37', [[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79]), ('cell38', [[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79]), ('cell39', [[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79]), ('cell40', [[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane384().draw(sys.argv[1] if len(sys.argv) > 1 else None))
