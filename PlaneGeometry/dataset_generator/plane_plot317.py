"""Frozen question Plane317; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane317:

    def __init__(self):
        self.id = 'Plane317'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:999'
        self.question = 'The composite board shown in the picture consists of 44 fields $1 \\times 1$. How many possibilities are there to cover all 40 white fields with 20 rectangular stones $1 \\times 2$? (The board cannot be turned. Two possibilities are different if at least one stone lies in another way.)'
        self.answer = '16'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane317.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.19968932249153415, 8.213231141812912], ylim=[-0.2145033089117243, 8.198417155392722], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell0_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell0_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 5.0], [1.0, 5.0], [1.0, 6.0], [0.0, 6.0], [0.0, 5.0]], [1, 2, 2, 2, 79], id='cell0_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 5.0], [1.0, 5.0], [1.0, 6.0], [0.0, 6.0], [0.0, 5.0]], [1, 2, 2, 2, 79], id='cell0_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell1_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 6.0], [2.0, 6.0], [2.0, 7.0], [1.0, 7.0], [1.0, 6.0]], [1, 2, 2, 2, 79], id='cell1_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 6.0], [2.0, 6.0], [2.0, 7.0], [1.0, 7.0], [1.0, 6.0]], [1, 2, 2, 2, 79], id='cell1_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='cell7_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='cell7_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 7.0], [8.0, 7.0], [8.0, 8.0], [7.0, 8.0], [7.0, 7.0]], [1, 2, 2, 2, 79], id='cell7_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 7.0], [8.0, 7.0], [8.0, 8.0], [7.0, 8.0], [7.0, 7.0]], [1, 2, 2, 2, 79], id='cell7_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='cell5_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='cell5_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell0_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell0_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 7.0], [1.0, 7.0], [1.0, 8.0], [0.0, 8.0], [0.0, 7.0]], [1, 2, 2, 2, 79], id='cell0_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 7.0], [1.0, 7.0], [1.0, 8.0], [0.0, 8.0], [0.0, 7.0]], [1, 2, 2, 2, 79], id='cell0_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell1_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell1_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell2_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 7.0], [3.0, 7.0], [3.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='cell2_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 7.0], [3.0, 7.0], [3.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='cell2_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell6_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell6_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='cell7_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='cell7_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 7.0], [7.0, 7.0], [7.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='cell6_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 7.0], [7.0, 7.0], [7.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='cell6_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 6.0], [8.0, 6.0], [8.0, 7.0], [7.0, 7.0], [7.0, 6.0]], [1, 2, 2, 2, 79], id='cell7_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 6.0], [8.0, 6.0], [8.0, 7.0], [7.0, 7.0], [7.0, 6.0]], [1, 2, 2, 2, 79], id='cell7_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell1_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell2_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 6.0], [1.0, 6.0], [1.0, 7.0], [0.0, 7.0], [0.0, 6.0]], [1, 2, 2, 2, 79], id='cell0_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 6.0], [1.0, 6.0], [1.0, 7.0], [0.0, 7.0], [0.0, 6.0]], [1, 2, 2, 2, 79], id='cell0_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79], id='cell1_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79], id='cell1_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell7_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell7_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='cell6_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='cell6_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell6_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell6_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79], id='cell7_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79], id='cell7_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='cell6_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='cell6_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane317().draw(sys.argv[1] if len(sys.argv) > 1 else None))
