"""Frozen question Plane244; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane244:

    def __init__(self):
        self.id = 'Plane244'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:693'
        self.question = 'A building block is made up of five identical rectangles as shown.\nHow many of the patterns shown below can be made with two such building blocks without overlap?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane244.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-10.75156509787071, 20.77509736620978), ylim=(-0.7868635003793205, 30.73979896370117), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            c.path([[2.0, 29.0], [4.0, 29.0], [4.0, 30.0], [2.0, 30.0], [2.0, 29.0]], [1, 2, 2, 2, 79], id='image1_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 29.0], [4.0, 29.0], [4.0, 30.0], [2.0, 30.0], [2.0, 29.0]], [1, 2, 2, 2, 79], id='image1_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 29.0], [6.0, 29.0], [6.0, 30.0], [4.0, 30.0], [4.0, 29.0]], [1, 2, 2, 2, 79], id='image1_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 29.0], [6.0, 29.0], [6.0, 30.0], [4.0, 30.0], [4.0, 29.0]], [1, 2, 2, 2, 79], id='image1_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 29.0], [8.0, 29.0], [8.0, 30.0], [6.0, 30.0], [6.0, 29.0]], [1, 2, 2, 2, 79], id='image1_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 29.0], [8.0, 29.0], [8.0, 30.0], [6.0, 30.0], [6.0, 29.0]], [1, 2, 2, 2, 79], id='image1_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 28.0], [4.0, 28.0], [4.0, 29.0], [2.0, 29.0], [2.0, 28.0]], [1, 2, 2, 2, 79], id='image1_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 28.0], [4.0, 28.0], [4.0, 29.0], [2.0, 29.0], [2.0, 28.0]], [1, 2, 2, 2, 79], id='image1_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 28.0], [8.0, 28.0], [8.0, 29.0], [6.0, 29.0], [6.0, 28.0]], [1, 2, 2, 2, 79], id='image1_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 28.0], [8.0, 28.0], [8.0, 29.0], [6.0, 29.0], [6.0, 28.0]], [1, 2, 2, 2, 79], id='image1_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 22.0], [4.0, 22.0], [4.0, 23.0], [2.0, 23.0], [2.0, 22.0]], [1, 2, 2, 2, 79], id='image2_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 22.0], [4.0, 22.0], [4.0, 23.0], [2.0, 23.0], [2.0, 22.0]], [1, 2, 2, 2, 79], id='image2_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 23.0], [4.0, 23.0], [4.0, 24.0], [2.0, 24.0], [2.0, 23.0]], [1, 2, 2, 2, 79], id='image2_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 23.0], [4.0, 23.0], [4.0, 24.0], [2.0, 24.0], [2.0, 23.0]], [1, 2, 2, 2, 79], id='image2_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 24.0], [4.0, 24.0], [4.0, 25.0], [2.0, 25.0], [2.0, 24.0]], [1, 2, 2, 2, 79], id='image2_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 24.0], [4.0, 24.0], [4.0, 25.0], [2.0, 25.0], [2.0, 24.0]], [1, 2, 2, 2, 79], id='image2_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 25.0], [4.0, 25.0], [4.0, 26.0], [2.0, 26.0], [2.0, 25.0]], [1, 2, 2, 2, 79], id='image2_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 25.0], [4.0, 25.0], [4.0, 26.0], [2.0, 26.0], [2.0, 25.0]], [1, 2, 2, 2, 79], id='image2_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 23.0], [6.0, 23.0], [6.0, 24.0], [4.0, 24.0], [4.0, 23.0]], [1, 2, 2, 2, 79], id='image2_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 23.0], [6.0, 23.0], [6.0, 24.0], [4.0, 24.0], [4.0, 23.0]], [1, 2, 2, 2, 79], id='image2_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 24.0], [6.0, 24.0], [6.0, 25.0], [4.0, 25.0], [4.0, 24.0]], [1, 2, 2, 2, 79], id='image2_5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 24.0], [6.0, 24.0], [6.0, 25.0], [4.0, 25.0], [4.0, 24.0]], [1, 2, 2, 2, 79], id='image2_5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 22.0], [8.0, 22.0], [8.0, 23.0], [6.0, 23.0], [6.0, 22.0]], [1, 2, 2, 2, 79], id='image2_6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 22.0], [8.0, 22.0], [8.0, 23.0], [6.0, 23.0], [6.0, 22.0]], [1, 2, 2, 2, 79], id='image2_6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 23.0], [8.0, 23.0], [8.0, 24.0], [6.0, 24.0], [6.0, 23.0]], [1, 2, 2, 2, 79], id='image2_7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 23.0], [8.0, 23.0], [8.0, 24.0], [6.0, 24.0], [6.0, 23.0]], [1, 2, 2, 2, 79], id='image2_7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 24.0], [8.0, 24.0], [8.0, 25.0], [6.0, 25.0], [6.0, 24.0]], [1, 2, 2, 2, 79], id='image2_8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 24.0], [8.0, 24.0], [8.0, 25.0], [6.0, 25.0], [6.0, 24.0]], [1, 2, 2, 2, 79], id='image2_8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 25.0], [8.0, 25.0], [8.0, 26.0], [6.0, 26.0], [6.0, 25.0]], [1, 2, 2, 2, 79], id='image2_9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 25.0], [8.0, 25.0], [8.0, 26.0], [6.0, 26.0], [6.0, 25.0]], [1, 2, 2, 2, 79], id='image2_9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 19.0], [2.0, 19.0], [2.0, 20.0], [0.0, 20.0], [0.0, 19.0]], [1, 2, 2, 2, 79], id='image3_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 19.0], [2.0, 19.0], [2.0, 20.0], [0.0, 20.0], [0.0, 19.0]], [1, 2, 2, 2, 79], id='image3_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 19.0], [4.0, 19.0], [4.0, 20.0], [2.0, 20.0], [2.0, 19.0]], [1, 2, 2, 2, 79], id='image3_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 19.0], [4.0, 19.0], [4.0, 20.0], [2.0, 20.0], [2.0, 19.0]], [1, 2, 2, 2, 79], id='image3_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 19.0], [6.0, 19.0], [6.0, 20.0], [4.0, 20.0], [4.0, 19.0]], [1, 2, 2, 2, 79], id='image3_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 19.0], [6.0, 19.0], [6.0, 20.0], [4.0, 20.0], [4.0, 19.0]], [1, 2, 2, 2, 79], id='image3_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 19.0], [8.0, 19.0], [8.0, 20.0], [6.0, 20.0], [6.0, 19.0]], [1, 2, 2, 2, 79], id='image3_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 19.0], [8.0, 19.0], [8.0, 20.0], [6.0, 20.0], [6.0, 19.0]], [1, 2, 2, 2, 79], id='image3_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 19.0], [10.0, 19.0], [10.0, 20.0], [8.0, 20.0], [8.0, 19.0]], [1, 2, 2, 2, 79], id='image3_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 19.0], [10.0, 19.0], [10.0, 20.0], [8.0, 20.0], [8.0, 19.0]], [1, 2, 2, 2, 79], id='image3_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 18.0], [2.0, 18.0], [2.0, 19.0], [0.0, 19.0], [0.0, 18.0]], [1, 2, 2, 2, 79], id='image3_5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 18.0], [2.0, 18.0], [2.0, 19.0], [0.0, 19.0], [0.0, 18.0]], [1, 2, 2, 2, 79], id='image3_5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 18.0], [6.0, 18.0], [6.0, 19.0], [4.0, 19.0], [4.0, 18.0]], [1, 2, 2, 2, 79], id='image3_6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 18.0], [6.0, 18.0], [6.0, 19.0], [4.0, 19.0], [4.0, 18.0]], [1, 2, 2, 2, 79], id='image3_6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.0, 18.0], [10.0, 18.0], [10.0, 19.0], [8.0, 19.0], [8.0, 18.0]], [1, 2, 2, 2, 79], id='image3_7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 18.0], [10.0, 18.0], [10.0, 19.0], [8.0, 19.0], [8.0, 18.0]], [1, 2, 2, 2, 79], id='image3_7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 15.0], [5.0, 15.0], [5.0, 16.0], [3.0, 16.0], [3.0, 15.0]], [1, 2, 2, 2, 79], id='image4_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 15.0], [5.0, 15.0], [5.0, 16.0], [3.0, 16.0], [3.0, 15.0]], [1, 2, 2, 2, 79], id='image4_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 15.0], [7.0, 15.0], [7.0, 16.0], [5.0, 16.0], [5.0, 15.0]], [1, 2, 2, 2, 79], id='image4_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 15.0], [7.0, 15.0], [7.0, 16.0], [5.0, 16.0], [5.0, 15.0]], [1, 2, 2, 2, 79], id='image4_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.0, 15.0], [9.0, 15.0], [9.0, 16.0], [7.0, 16.0], [7.0, 15.0]], [1, 2, 2, 2, 79], id='image4_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 15.0], [9.0, 15.0], [9.0, 16.0], [7.0, 16.0], [7.0, 15.0]], [1, 2, 2, 2, 79], id='image4_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 14.0], [3.0, 14.0], [3.0, 15.0], [1.0, 15.0], [1.0, 14.0]], [1, 2, 2, 2, 79], id='image4_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 14.0], [3.0, 14.0], [3.0, 15.0], [1.0, 15.0], [1.0, 14.0]], [1, 2, 2, 2, 79], id='image4_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 14.0], [5.0, 14.0], [5.0, 15.0], [3.0, 15.0], [3.0, 14.0]], [1, 2, 2, 2, 79], id='image4_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 14.0], [5.0, 14.0], [5.0, 15.0], [3.0, 15.0], [3.0, 14.0]], [1, 2, 2, 2, 79], id='image4_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 14.0], [7.0, 14.0], [7.0, 15.0], [5.0, 15.0], [5.0, 14.0]], [1, 2, 2, 2, 79], id='image4_5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 14.0], [7.0, 14.0], [7.0, 15.0], [5.0, 15.0], [5.0, 14.0]], [1, 2, 2, 2, 79], id='image4_5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.0, 14.0], [9.0, 14.0], [9.0, 15.0], [7.0, 15.0], [7.0, 14.0]], [1, 2, 2, 2, 79], id='image4_6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 14.0], [9.0, 14.0], [9.0, 15.0], [7.0, 15.0], [7.0, 14.0]], [1, 2, 2, 2, 79], id='image4_6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 13.0], [3.0, 13.0], [3.0, 14.0], [1.0, 14.0], [1.0, 13.0]], [1, 2, 2, 2, 79], id='image4_7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 13.0], [3.0, 13.0], [3.0, 14.0], [1.0, 14.0], [1.0, 13.0]], [1, 2, 2, 2, 79], id='image4_7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 13.0], [5.0, 13.0], [5.0, 14.0], [3.0, 14.0], [3.0, 13.0]], [1, 2, 2, 2, 79], id='image4_8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 13.0], [5.0, 13.0], [5.0, 14.0], [3.0, 14.0], [3.0, 13.0]], [1, 2, 2, 2, 79], id='image4_8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 13.0], [7.0, 13.0], [7.0, 14.0], [5.0, 14.0], [5.0, 13.0]], [1, 2, 2, 2, 79], id='image4_9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 13.0], [7.0, 13.0], [7.0, 14.0], [5.0, 14.0], [5.0, 13.0]], [1, 2, 2, 2, 79], id='image4_9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='image5_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='image5_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 8.0], [4.0, 8.0], [4.0, 9.0], [2.0, 9.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='image5_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 8.0], [4.0, 8.0], [4.0, 9.0], [2.0, 9.0], [2.0, 8.0]], [1, 2, 2, 2, 79], id='image5_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 9.0], [4.0, 9.0], [4.0, 10.0], [2.0, 10.0], [2.0, 9.0]], [1, 2, 2, 2, 79], id='image5_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 9.0], [4.0, 9.0], [4.0, 10.0], [2.0, 10.0], [2.0, 9.0]], [1, 2, 2, 2, 79], id='image5_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 11.0], [2.0, 11.0], [2.0, 10.0]], [1, 2, 2, 2, 79], id='image5_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 10.0], [4.0, 10.0], [4.0, 11.0], [2.0, 11.0], [2.0, 10.0]], [1, 2, 2, 2, 79], id='image5_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 7.0], [6.0, 7.0], [6.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='image5_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 7.0], [6.0, 7.0], [6.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='image5_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 10.0], [6.0, 10.0], [6.0, 11.0], [4.0, 11.0], [4.0, 10.0]], [1, 2, 2, 2, 79], id='image5_5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 10.0], [6.0, 10.0], [6.0, 11.0], [4.0, 11.0], [4.0, 10.0]], [1, 2, 2, 2, 79], id='image5_5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 7.0], [8.0, 7.0], [8.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='image5_6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 7.0], [8.0, 7.0], [8.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='image5_6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 8.0], [8.0, 8.0], [8.0, 9.0], [6.0, 9.0], [6.0, 8.0]], [1, 2, 2, 2, 79], id='image5_7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 8.0], [8.0, 8.0], [8.0, 9.0], [6.0, 9.0], [6.0, 8.0]], [1, 2, 2, 2, 79], id='image5_7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 9.0], [8.0, 9.0], [8.0, 10.0], [6.0, 10.0], [6.0, 9.0]], [1, 2, 2, 2, 79], id='image5_8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 9.0], [8.0, 9.0], [8.0, 10.0], [6.0, 10.0], [6.0, 9.0]], [1, 2, 2, 2, 79], id='image5_8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 10.0], [8.0, 10.0], [8.0, 11.0], [6.0, 11.0], [6.0, 10.0]], [1, 2, 2, 2, 79], id='image5_9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 10.0], [8.0, 10.0], [8.0, 11.0], [6.0, 11.0], [6.0, 10.0]], [1, 2, 2, 2, 79], id='image5_9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='image6_0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='image6_0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 6.0], [3.0, 6.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='image6_1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 6.0], [3.0, 6.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='image6_1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 2.0], [4.0, 2.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='image6_2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 2.0], [4.0, 2.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='image6_2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 4.0], [4.0, 4.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='image6_3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 4.0], [4.0, 4.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='image6_3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 6.0], [4.0, 6.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='image6_4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 6.0], [4.0, 6.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='image6_4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 2.0], [5.0, 2.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='image6_5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 2.0], [5.0, 2.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='image6_5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 4.0], [5.0, 4.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='image6_6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 4.0], [5.0, 4.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='image6_6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 6.0], [5.0, 6.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='image6_7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 6.0], [5.0, 6.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='image6_7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='image6_8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='image6_8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 6.0], [6.0, 6.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='image6_9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 6.0], [6.0, 6.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='image6_9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane244().draw(sys.argv[1] if len(sys.argv) > 1 else None))
