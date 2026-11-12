"""Frozen question Plane290; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane290:

    def __init__(self):
        self.id = 'Plane290'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:868'
        self.question = 'Four identical building blocks each have the shape shown. Which shape cannot be formed with them?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane290.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-2.6846212406450576, 43.13391941213918), ylim=(-19.63930504861434, 26.179235604169897), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[18.0, 7.0], [19.0, 7.0], [19.0, 8.0], [18.0, 8.0], [18.0, 7.0]], [1, 2, 2, 2, 79], id='given0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 7.0], [19.0, 7.0], [19.0, 8.0], [18.0, 8.0], [18.0, 7.0]], [1, 2, 2, 2, 79], id='given0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, 7.0], [20.0, 7.0], [20.0, 8.0], [19.0, 8.0], [19.0, 7.0]], [1, 2, 2, 2, 79], id='given1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, 7.0], [20.0, 7.0], [20.0, 8.0], [19.0, 8.0], [19.0, 7.0]], [1, 2, 2, 2, 79], id='given1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 7.0], [21.0, 7.0], [21.0, 8.0], [20.0, 8.0], [20.0, 7.0]], [1, 2, 2, 2, 79], id='given2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 7.0], [21.0, 7.0], [21.0, 8.0], [20.0, 8.0], [20.0, 7.0]], [1, 2, 2, 2, 79], id='given2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='option00', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='option00', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option01', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option01', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='option02', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='option02', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='option03', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='option03', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='option04', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='option04', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='option05', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='option05', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='option06', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='option06', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='option07', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='option07', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='option08', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='option08', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='option09', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='option09', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='option010', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='option010', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='option011', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='option011', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='option10', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='option10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 1.0], [10.0, 1.0], [10.0, 2.0], [9.0, 2.0], [9.0, 1.0]], [1, 2, 2, 2, 79], id='option11', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 1.0], [10.0, 1.0], [10.0, 2.0], [9.0, 2.0], [9.0, 1.0]], [1, 2, 2, 2, 79], id='option11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 2.0], [10.0, 2.0], [10.0, 3.0], [9.0, 3.0], [9.0, 2.0]], [1, 2, 2, 2, 79], id='option12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 2.0], [10.0, 2.0], [10.0, 3.0], [9.0, 3.0], [9.0, 2.0]], [1, 2, 2, 2, 79], id='option12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='option13', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='option13', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='option14', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='option14', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='option15', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='option15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [11.0, 1.0], [11.0, 0.0]], [1, 2, 2, 2, 79], id='option16', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [11.0, 1.0], [11.0, 0.0]], [1, 2, 2, 2, 79], id='option16', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0]], [1, 2, 2, 2, 79], id='option17', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0]], [1, 2, 2, 2, 79], id='option17', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.0, 2.0], [12.0, 2.0], [12.0, 3.0], [11.0, 3.0], [11.0, 2.0]], [1, 2, 2, 2, 79], id='option18', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.0, 2.0], [12.0, 2.0], [12.0, 3.0], [11.0, 3.0], [11.0, 2.0]], [1, 2, 2, 2, 79], id='option18', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='option19', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='option19', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 79], id='option110', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 79], id='option110', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 2.0], [13.0, 2.0], [13.0, 3.0], [12.0, 3.0], [12.0, 2.0]], [1, 2, 2, 2, 79], id='option111', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 2.0], [13.0, 2.0], [13.0, 3.0], [12.0, 3.0], [12.0, 2.0]], [1, 2, 2, 2, 79], id='option111', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[18.0, 0.0], [19.0, 0.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='option20', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 0.0], [19.0, 0.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='option20', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[18.0, 2.0], [19.0, 2.0], [19.0, 3.0], [18.0, 3.0], [18.0, 2.0]], [1, 2, 2, 2, 79], id='option21', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[18.0, 2.0], [19.0, 2.0], [19.0, 3.0], [18.0, 3.0], [18.0, 2.0]], [1, 2, 2, 2, 79], id='option21', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, 0.0], [20.0, 0.0], [20.0, 1.0], [19.0, 1.0], [19.0, 0.0]], [1, 2, 2, 2, 79], id='option22', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, 0.0], [20.0, 0.0], [20.0, 1.0], [19.0, 1.0], [19.0, 0.0]], [1, 2, 2, 2, 79], id='option22', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[19.0, 2.0], [20.0, 2.0], [20.0, 3.0], [19.0, 3.0], [19.0, 2.0]], [1, 2, 2, 2, 79], id='option23', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[19.0, 2.0], [20.0, 2.0], [20.0, 3.0], [19.0, 3.0], [19.0, 2.0]], [1, 2, 2, 2, 79], id='option23', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option24', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option24', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 2.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0]], [1, 2, 2, 2, 79], id='option25', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 2.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0]], [1, 2, 2, 2, 79], id='option25', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='option26', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='option26', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='option27', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='option27', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='option28', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='option28', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0]], [1, 2, 2, 2, 79], id='option29', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0]], [1, 2, 2, 2, 79], id='option29', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[23.0, 1.0], [24.0, 1.0], [24.0, 2.0], [23.0, 2.0], [23.0, 1.0]], [1, 2, 2, 2, 79], id='option210', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[23.0, 1.0], [24.0, 1.0], [24.0, 2.0], [23.0, 2.0], [23.0, 1.0]], [1, 2, 2, 2, 79], id='option210', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[24.0, 1.0], [25.0, 1.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 79], id='option211', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[24.0, 1.0], [25.0, 1.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 79], id='option211', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[27.0, 0.0], [28.0, 0.0], [28.0, 1.0], [27.0, 1.0], [27.0, 0.0]], [1, 2, 2, 2, 79], id='option30', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[27.0, 0.0], [28.0, 0.0], [28.0, 1.0], [27.0, 1.0], [27.0, 0.0]], [1, 2, 2, 2, 79], id='option30', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[28.0, 0.0], [29.0, 0.0], [29.0, 1.0], [28.0, 1.0], [28.0, 0.0]], [1, 2, 2, 2, 79], id='option31', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[28.0, 0.0], [29.0, 0.0], [29.0, 1.0], [28.0, 1.0], [28.0, 0.0]], [1, 2, 2, 2, 79], id='option31', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[29.0, 0.0], [30.0, 0.0], [30.0, 1.0], [29.0, 1.0], [29.0, 0.0]], [1, 2, 2, 2, 79], id='option32', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[29.0, 0.0], [30.0, 0.0], [30.0, 1.0], [29.0, 1.0], [29.0, 0.0]], [1, 2, 2, 2, 79], id='option32', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79], id='option33', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79], id='option33', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[31.0, 0.0], [32.0, 0.0], [32.0, 1.0], [31.0, 1.0], [31.0, 0.0]], [1, 2, 2, 2, 79], id='option34', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[31.0, 0.0], [32.0, 0.0], [32.0, 1.0], [31.0, 1.0], [31.0, 0.0]], [1, 2, 2, 2, 79], id='option34', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[32.0, 0.0], [33.0, 0.0], [33.0, 1.0], [32.0, 1.0], [32.0, 0.0]], [1, 2, 2, 2, 79], id='option35', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[32.0, 0.0], [33.0, 0.0], [33.0, 1.0], [32.0, 1.0], [32.0, 0.0]], [1, 2, 2, 2, 79], id='option35', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[33.0, 0.0], [34.0, 0.0], [34.0, 1.0], [33.0, 1.0], [33.0, 0.0]], [1, 2, 2, 2, 79], id='option36', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[33.0, 0.0], [34.0, 0.0], [34.0, 1.0], [33.0, 1.0], [33.0, 0.0]], [1, 2, 2, 2, 79], id='option36', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[30.0, 1.0], [31.0, 1.0], [31.0, 2.0], [30.0, 2.0], [30.0, 1.0]], [1, 2, 2, 2, 79], id='option37', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[30.0, 1.0], [31.0, 1.0], [31.0, 2.0], [30.0, 2.0], [30.0, 1.0]], [1, 2, 2, 2, 79], id='option37', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[30.0, 2.0], [31.0, 2.0], [31.0, 3.0], [30.0, 3.0], [30.0, 2.0]], [1, 2, 2, 2, 79], id='option38', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[30.0, 2.0], [31.0, 2.0], [31.0, 3.0], [30.0, 3.0], [30.0, 2.0]], [1, 2, 2, 2, 79], id='option38', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[33.0, 1.0], [34.0, 1.0], [34.0, 2.0], [33.0, 2.0], [33.0, 1.0]], [1, 2, 2, 2, 79], id='option39', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[33.0, 1.0], [34.0, 1.0], [34.0, 2.0], [33.0, 2.0], [33.0, 1.0]], [1, 2, 2, 2, 79], id='option39', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[33.0, 2.0], [34.0, 2.0], [34.0, 3.0], [33.0, 3.0], [33.0, 2.0]], [1, 2, 2, 2, 79], id='option310', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[33.0, 2.0], [34.0, 2.0], [34.0, 3.0], [33.0, 3.0], [33.0, 2.0]], [1, 2, 2, 2, 79], id='option310', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[33.0, 3.0], [34.0, 3.0], [34.0, 4.0], [33.0, 4.0], [33.0, 3.0]], [1, 2, 2, 2, 79], id='option311', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[33.0, 3.0], [34.0, 3.0], [34.0, 4.0], [33.0, 4.0], [33.0, 3.0]], [1, 2, 2, 2, 79], id='option311', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[36.0, 0.0], [37.0, 0.0], [37.0, 1.0], [36.0, 1.0], [36.0, 0.0]], [1, 2, 2, 2, 79], id='option40', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[36.0, 0.0], [37.0, 0.0], [37.0, 1.0], [36.0, 1.0], [36.0, 0.0]], [1, 2, 2, 2, 79], id='option40', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[36.0, 2.0], [37.0, 2.0], [37.0, 3.0], [36.0, 3.0], [36.0, 2.0]], [1, 2, 2, 2, 79], id='option41', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[36.0, 2.0], [37.0, 2.0], [37.0, 3.0], [36.0, 3.0], [36.0, 2.0]], [1, 2, 2, 2, 79], id='option41', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[37.0, 0.0], [38.0, 0.0], [38.0, 1.0], [37.0, 1.0], [37.0, 0.0]], [1, 2, 2, 2, 79], id='option42', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[37.0, 0.0], [38.0, 0.0], [38.0, 1.0], [37.0, 1.0], [37.0, 0.0]], [1, 2, 2, 2, 79], id='option42', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[37.0, 2.0], [38.0, 2.0], [38.0, 3.0], [37.0, 3.0], [37.0, 2.0]], [1, 2, 2, 2, 79], id='option43', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[37.0, 2.0], [38.0, 2.0], [38.0, 3.0], [37.0, 3.0], [37.0, 2.0]], [1, 2, 2, 2, 79], id='option43', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[38.0, 0.0], [39.0, 0.0], [39.0, 1.0], [38.0, 1.0], [38.0, 0.0]], [1, 2, 2, 2, 79], id='option44', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[38.0, 0.0], [39.0, 0.0], [39.0, 1.0], [38.0, 1.0], [38.0, 0.0]], [1, 2, 2, 2, 79], id='option44', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[38.0, 2.0], [39.0, 2.0], [39.0, 3.0], [38.0, 3.0], [38.0, 2.0]], [1, 2, 2, 2, 79], id='option45', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[38.0, 2.0], [39.0, 2.0], [39.0, 3.0], [38.0, 3.0], [38.0, 2.0]], [1, 2, 2, 2, 79], id='option45', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[39.0, 0.0], [40.0, 0.0], [40.0, 1.0], [39.0, 1.0], [39.0, 0.0]], [1, 2, 2, 2, 79], id='option46', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[39.0, 0.0], [40.0, 0.0], [40.0, 1.0], [39.0, 1.0], [39.0, 0.0]], [1, 2, 2, 2, 79], id='option46', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[39.0, 2.0], [40.0, 2.0], [40.0, 3.0], [39.0, 3.0], [39.0, 2.0]], [1, 2, 2, 2, 79], id='option47', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[39.0, 2.0], [40.0, 2.0], [40.0, 3.0], [39.0, 3.0], [39.0, 2.0]], [1, 2, 2, 2, 79], id='option47', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[38.0, 1.0], [39.0, 1.0], [39.0, 2.0], [38.0, 2.0], [38.0, 1.0]], [1, 2, 2, 2, 79], id='option48', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[38.0, 1.0], [39.0, 1.0], [39.0, 2.0], [38.0, 2.0], [38.0, 1.0]], [1, 2, 2, 2, 79], id='option48', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[39.0, 1.0], [40.0, 1.0], [40.0, 2.0], [39.0, 2.0], [39.0, 1.0]], [1, 2, 2, 2, 79], id='option49', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[39.0, 1.0], [40.0, 1.0], [40.0, 2.0], [39.0, 2.0], [39.0, 1.0]], [1, 2, 2, 2, 79], id='option49', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[40.0, 1.0], [41.0, 1.0], [41.0, 2.0], [40.0, 2.0], [40.0, 1.0]], [1, 2, 2, 2, 79], id='option410', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[40.0, 1.0], [41.0, 1.0], [41.0, 2.0], [40.0, 2.0], [40.0, 1.0]], [1, 2, 2, 2, 79], id='option410', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[41.0, 1.0], [42.0, 1.0], [42.0, 2.0], [41.0, 2.0], [41.0, 1.0]], [1, 2, 2, 2, 79], id='option411', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[41.0, 1.0], [42.0, 1.0], [42.0, 2.0], [41.0, 2.0], [41.0, 1.0]], [1, 2, 2, 2, 79], id='option411', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (-0.7, -0.9)), ('label1', '(B)', (8.3, -0.9)), ('label2', '(C)', (17.3, -0.9)), ('label3', '(D)', (26.3, -0.9)), ('label4', '(E)', (35.3, -0.9))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane290().draw(sys.argv[1] if len(sys.argv) > 1 else None))
