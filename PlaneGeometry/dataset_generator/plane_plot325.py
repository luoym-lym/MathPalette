"""Frozen question Plane325; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane325:

    def __init__(self):
        self.id = 'Plane325'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1032'
        self.question = 'What is the minimum number of additional small squares that must be shaded in the diagram on the right so that it has an axis of symmetry?'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane325.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.22437711759410206, 9.240158404748396], ylim=[-0.24077445742880865, 9.223761064913688], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='cell4_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='cell4_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='cell3_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='cell3_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='cell4_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='cell4_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell3_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell3_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='cell5_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='cell5_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79], id='cell7_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79], id='cell7_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='cell4_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='cell4_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79], id='cell4_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79], id='cell4_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell3_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell3_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79], id='cell4_8', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79], id='cell4_8', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79], id='cell5_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79], id='cell5_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell2_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell2_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79], id='cell7_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79], id='cell7_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell3_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell3_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='cell4_7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='cell4_7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell3_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell3_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='cell4_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='cell4_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79], id='cell8_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79], id='cell8_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell2_3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell2_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell6_6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
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
    print(Plane325().draw(sys.argv[1] if len(sys.argv) > 1 else None))
