"""Frozen question Plane293; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane293:

    def __init__(self):
        self.id = 'Plane293'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:891'
        self.question = 'Four equally big squares are partially coloured in black. In which of the four squares is the total area of the black parts biggest?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:The total area of the black parts is always equally big.'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'The total area of the black parts is always equally big.'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane293.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3071312127620942, 12.825615244577339], ylim=[-5.812123793915195, 7.320622663424238], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('grid0_0', [[0.0, 0.0], [0.0, 1.0]]), ('grid0_1', [[0.0, 0.0], [1.0, 0.0]]), ('grid0_2', [[0.0, 1.0], [0.0, 2.0]]), ('grid0_3', [[0.0, 1.0], [1.0, 1.0]]), ('grid0_4', [[0.0, 2.0], [1.0, 2.0]]), ('grid0_5', [[1.0, 0.0], [1.0, 1.0]]), ('grid0_6', [[1.0, 0.0], [2.0, 0.0]]), ('grid0_7', [[1.0, 1.0], [1.0, 2.0]]), ('grid0_8', [[1.0, 1.0], [2.0, 1.0]]), ('grid0_9', [[1.0, 2.0], [2.0, 2.0]]), ('grid0_10', [[2.0, 0.0], [2.0, 1.0]]), ('grid0_11', [[2.0, 1.0], [2.0, 2.0]]), ('diag0_0', [[0.0, 0.0], [1.0, 1.0]]), ('diag0_1', [[1.0, 1.0], [2.0, 2.0]]), ('antidiag0', [[1.0, 1.0], [2.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[3.5, 1.0], [4.5, 1.0], [3.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='black1_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.5, 1.0], [4.5, 1.0], [3.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='black1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.5, 1.0], [5.5, 1.0], [5.5, 0.0], [4.5, 1.0]], [1, 2, 2, 79], id='black1_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.5, 1.0], [5.5, 1.0], [5.5, 0.0], [4.5, 1.0]], [1, 2, 2, 79], id='black1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('grid1_0', [[3.5, 0.0], [3.5, 1.0]]), ('grid1_1', [[3.5, 0.0], [4.5, 0.0]]), ('grid1_2', [[3.5, 1.0], [3.5, 2.0]]), ('grid1_3', [[3.5, 1.0], [4.5, 1.0]]), ('grid1_4', [[3.5, 2.0], [4.5, 2.0]]), ('grid1_5', [[4.5, 0.0], [4.5, 1.0]]), ('grid1_6', [[4.5, 0.0], [5.5, 0.0]]), ('grid1_7', [[4.5, 1.0], [4.5, 2.0]]), ('grid1_8', [[4.5, 1.0], [5.5, 1.0]]), ('grid1_9', [[4.5, 2.0], [5.5, 2.0]]), ('grid1_10', [[5.5, 0.0], [5.5, 1.0]]), ('grid1_11', [[5.5, 1.0], [5.5, 2.0]]), ('diag1_0', [[3.5, 0.0], [4.5, 1.0]]), ('diag1_1', [[4.5, 1.0], [5.5, 2.0]]), ('antidiag1', [[3.5, 2.0], [5.5, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='black2_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='black2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 1.0], [8.5, 1.5], [9.0, 1.0], [8.5, 0.5], [8.0, 1.0]], [1, 2, 2, 2, 79], id='black2_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [8.5, 1.5], [9.0, 1.0], [8.5, 0.5], [8.0, 1.0]], [1, 2, 2, 2, 79], id='black2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('grid2_0', [[7.0, 0.0], [7.0, 1.0]]), ('grid2_1', [[7.0, 0.0], [8.0, 0.0]]), ('grid2_2', [[7.0, 1.0], [7.0, 2.0]]), ('grid2_3', [[7.0, 1.0], [8.0, 1.0]]), ('grid2_4', [[7.0, 2.0], [8.0, 2.0]]), ('grid2_5', [[8.0, 0.0], [8.0, 1.0]]), ('grid2_6', [[8.0, 0.0], [9.0, 0.0]]), ('grid2_7', [[8.0, 1.0], [8.0, 2.0]]), ('grid2_8', [[8.0, 1.0], [9.0, 1.0]]), ('grid2_9', [[8.0, 2.0], [9.0, 2.0]]), ('grid2_10', [[9.0, 0.0], [9.0, 1.0]]), ('grid2_11', [[9.0, 1.0], [9.0, 2.0]]), ('diag200', [[7.0, 0.0], [8.0, 1.0]]), ('anti200', [[7.0, 1.0], [8.0, 0.0]]), ('diag201', [[7.0, 1.0], [8.0, 2.0]]), ('anti201', [[7.0, 2.0], [8.0, 1.0]]), ('diag210', [[8.0, 0.0], [9.0, 1.0]]), ('anti210', [[8.0, 1.0], [9.0, 0.0]]), ('diag211', [[8.0, 1.0], [9.0, 2.0]]), ('anti211', [[8.0, 2.0], [9.0, 1.0]])]:
                c.line(points, id=object_id)
            c.path([[10.5, 2.0], [11.5, 2.0], [11.0, 1.5], [10.5, 2.0]], [1, 2, 2, 79], id='black3_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.5, 2.0], [11.5, 2.0], [11.0, 1.5], [10.5, 2.0]], [1, 2, 2, 79], id='black3_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[11.5, 2.0], [12.5, 2.0], [12.0, 1.5], [11.5, 2.0]], [1, 2, 2, 79], id='black3_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[11.5, 2.0], [12.5, 2.0], [12.0, 1.5], [11.5, 2.0]], [1, 2, 2, 79], id='black3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.5, 0.0], [10.5, 1.0], [11.0, 0.5], [10.5, 0.0]], [1, 2, 2, 79], id='black3_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.5, 0.0], [10.5, 1.0], [11.0, 0.5], [10.5, 0.0]], [1, 2, 2, 79], id='black3_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.5, 0.0], [12.5, 1.0], [12.0, 0.5], [12.5, 0.0]], [1, 2, 2, 79], id='black3_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.5, 0.0], [12.5, 1.0], [12.0, 0.5], [12.5, 0.0]], [1, 2, 2, 79], id='black3_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('grid3_0', [[10.5, 0.0], [10.5, 1.0]]), ('grid3_1', [[10.5, 0.0], [11.5, 0.0]]), ('grid3_2', [[10.5, 1.0], [10.5, 2.0]]), ('grid3_3', [[10.5, 1.0], [11.5, 1.0]]), ('grid3_4', [[10.5, 2.0], [11.5, 2.0]]), ('grid3_5', [[11.5, 0.0], [11.5, 1.0]]), ('grid3_6', [[11.5, 0.0], [12.5, 0.0]]), ('grid3_7', [[11.5, 1.0], [11.5, 2.0]]), ('grid3_8', [[11.5, 1.0], [12.5, 1.0]]), ('grid3_9', [[11.5, 2.0], [12.5, 2.0]]), ('grid3_10', [[12.5, 0.0], [12.5, 1.0]]), ('grid3_11', [[12.5, 1.0], [12.5, 2.0]]), ('diag300', [[10.5, 0.0], [11.5, 1.0]]), ('anti300', [[10.5, 1.0], [11.5, 0.0]]), ('diag301', [[10.5, 1.0], [11.5, 2.0]]), ('anti301', [[10.5, 2.0], [11.5, 1.0]]), ('diag310', [[11.5, 0.0], [12.5, 1.0]]), ('anti310', [[11.5, 1.0], [12.5, 0.0]]), ('diag311', [[11.5, 1.0], [12.5, 2.0]]), ('anti311', [[11.5, 2.0], [12.5, 1.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', 'A', [1.0, -0.4]), ('label1', 'B', [4.5, -0.4]), ('label2', 'C', [8.0, -0.4]), ('label3', 'D', [11.5, -0.4])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane293().draw(sys.argv[1] if len(sys.argv) > 1 else None))
