"""Frozen question Plane209; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane209:

    def __init__(self):
        self.id = 'Plane209'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:511'
        self.question = 'Which of the houses shown use exactly the same building blocks?\nChoices:\nA:House 1 and 4\nB:House 3 and 4\nC:House 1, 4 and 5\nD:House 3, 4 and 5\nE:House 1, 2, 4 and 5'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'House 1 and 4', 'B': 'House 3 and 4', 'C': 'House 1, 4 and 5', 'D': 'House 3, 4 and 5', 'E': 'House 1, 2, 4 and 5'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane209.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.1233819356196957, 23.729157068805847], ylim=[-9.94130276085295, 14.91123624357259], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='body0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='body0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[-0.15, 3.0], [1.5, 5.0], [3.15, 3.0], [-0.15, 3.0]], [1, 2, 2, 79], id='roof0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[-0.15, 3.0], [1.5, 5.0], [3.15, 3.0], [-0.15, 3.0]], [1, 2, 2, 79], id='roof0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 2.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='door0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 2.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='door0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.28, 0.85], [1.73, 0.85], [1.73, 1.85], [1.28, 1.85], [1.28, 0.85]], [1, 2, 2, 2, 79], id='orange0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.28, 0.85], [1.73, 0.85], [1.73, 1.85], [1.28, 1.85], [1.28, 0.85]], [1, 2, 2, 2, 79], id='orange0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.3, 2.7], [0.9, 2.7], [0.3, 2.1], [0.3, 2.7]], [1, 2, 2, 79], id='green0_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.3, 2.7], [0.9, 2.7], [0.3, 2.1], [0.3, 2.7]], [1, 2, 2, 79], id='green0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.2, 2.7], [2.8, 2.7], [2.8, 2.1], [2.2, 2.7]], [1, 2, 2, 79], id='green0_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.2, 2.7], [2.8, 2.7], [2.8, 2.1], [2.2, 2.7]], [1, 2, 2, 79], id='green0_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.22, 4.1], [2.82, 4.1], [2.82, 3.5], [2.22, 4.1]], [1, 2, 2, 79], id='green0_2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.22, 4.1], [2.82, 4.1], [2.82, 3.5], [2.22, 4.1]], [1, 2, 2, 79], id='green0_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([-0.1, 4.25], 0.43, id='badge0', facecolor=[0.0, 0.0, 0.0, 0.0])
            c.path([[5.65, 1.3], [7.3500000000000005, 1.3], [7.3500000000000005, 3.0], [5.65, 3.0], [5.65, 1.3]], [1, 2, 2, 2, 79], id='body1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.65, 1.3], [7.3500000000000005, 1.3], [7.3500000000000005, 3.0], [5.65, 3.0], [5.65, 1.3]], [1, 2, 2, 2, 79], id='body1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.85, 3.0], [6.5, 5.0], [8.15, 3.0], [4.85, 3.0]], [1, 2, 2, 79], id='roof1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.85, 3.0], [6.5, 5.0], [8.15, 3.0], [4.85, 3.0]], [1, 2, 2, 79], id='roof1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.4, 0.25], [7.4, 0.25], [7.4, 1.25], [5.4, 1.25], [5.4, 0.25]], [1, 2, 2, 2, 79], id='base1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.4, 0.25], [7.4, 0.25], [7.4, 1.25], [5.4, 1.25], [5.4, 0.25]], [1, 2, 2, 2, 79], id='base1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.12, 3.7], [7.62, 3.7], [7.62, 4.7], [7.12, 4.7], [7.12, 3.7]], [1, 2, 2, 2, 79], id='orange1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.12, 3.7], [7.62, 3.7], [7.62, 4.7], [7.12, 4.7], [7.12, 3.7]], [1, 2, 2, 2, 79], id='orange1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.85, 2.8], [5.85, 2.2], [6.45, 2.2], [5.85, 2.8]], [1, 2, 2, 79], id='green1_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[5.85, 2.8], [5.85, 2.2], [6.45, 2.2], [5.85, 2.8]], [1, 2, 2, 79], id='green1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.55, 2.8], [7.15, 2.8], [7.15, 2.2], [6.55, 2.8]], [1, 2, 2, 79], id='green1_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.55, 2.8], [7.15, 2.8], [7.15, 2.2], [6.55, 2.8]], [1, 2, 2, 79], id='green1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([4.9, 4.25], 0.43, id='badge1', facecolor=[0.0, 0.0, 0.0, 0.0])
            c.path([[10.0, 0.0], [13.0, 0.0], [13.0, 3.0], [10.0, 3.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='body2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.0], [13.0, 0.0], [13.0, 3.0], [10.0, 3.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='body2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[9.85, 3.0], [11.5, 5.0], [13.15, 3.0], [9.85, 3.0]], [1, 2, 2, 79], id='roof2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.85, 3.0], [11.5, 5.0], [13.15, 3.0], [9.85, 3.0]], [1, 2, 2, 79], id='roof2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[11.8, 0.0], [12.25, 0.0], [12.25, 1.0], [11.8, 1.0], [11.8, 0.0]], [1, 2, 2, 2, 79], id='orange2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[11.8, 0.0], [12.25, 0.0], [12.25, 1.0], [11.8, 1.0], [11.8, 0.0]], [1, 2, 2, 2, 79], id='orange2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.15, 3.4], [12.65, 3.4], [12.65, 4.4], [12.15, 4.4], [12.15, 3.4]], [1, 2, 2, 2, 79], id='chimney2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.15, 3.4], [12.65, 3.4], [12.65, 4.4], [12.15, 4.4], [12.15, 3.4]], [1, 2, 2, 2, 79], id='chimney2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.3, 1.0], [10.9, 1.0], [10.3, 1.6], [10.3, 1.0]], [1, 2, 2, 79], id='green2_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.3, 1.0], [10.9, 1.0], [10.3, 1.6], [10.3, 1.0]], [1, 2, 2, 79], id='green2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.9, 1.0], [10.9, 1.6], [10.3, 1.6], [10.9, 1.0]], [1, 2, 2, 79], id='green2_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.9, 1.0], [10.9, 1.6], [10.3, 1.6], [10.9, 1.0]], [1, 2, 2, 79], id='green2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.3, 2.1], [10.9, 2.1], [10.3, 2.7], [10.3, 2.1]], [1, 2, 2, 79], id='green2_2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.3, 2.1], [10.9, 2.1], [10.3, 2.7], [10.3, 2.1]], [1, 2, 2, 79], id='green2_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.9, 2.1], [10.9, 2.7], [10.3, 2.7], [10.9, 2.1]], [1, 2, 2, 79], id='green2_3', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.9, 2.1], [10.9, 2.7], [10.3, 2.7], [10.9, 2.1]], [1, 2, 2, 79], id='green2_3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([9.9, 4.25], 0.43, id='badge2', facecolor=[0.0, 0.0, 0.0, 0.0])
            c.path([[15.0, 0.0], [18.0, 0.0], [18.0, 3.0], [15.0, 3.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='body3', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[15.0, 0.0], [18.0, 0.0], [18.0, 3.0], [15.0, 3.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='body3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[14.85, 3.0], [16.5, 5.0], [18.15, 3.0], [14.85, 3.0]], [1, 2, 2, 79], id='roof3', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[14.85, 3.0], [16.5, 5.0], [18.15, 3.0], [14.85, 3.0]], [1, 2, 2, 79], id='roof3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 2.0], [16.0, 2.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='door3', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 2.0], [16.0, 2.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='door3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[17.2, 3.75], [17.65, 3.75], [17.65, 4.75], [17.2, 4.75], [17.2, 3.75]], [1, 2, 2, 2, 79], id='orange3', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.2, 3.75], [17.65, 3.75], [17.65, 4.75], [17.2, 4.75], [17.2, 3.75]], [1, 2, 2, 2, 79], id='orange3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[15.2, 2.2], [15.8, 2.2], [15.2, 2.8], [15.2, 2.2]], [1, 2, 2, 79], id='green3_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[15.2, 2.2], [15.8, 2.2], [15.2, 2.8], [15.2, 2.2]], [1, 2, 2, 79], id='green3_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[15.8, 2.2], [15.8, 2.8], [15.2, 2.8], [15.8, 2.2]], [1, 2, 2, 79], id='green3_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[15.8, 2.2], [15.8, 2.8], [15.2, 2.8], [15.8, 2.2]], [1, 2, 2, 79], id='green3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.1, 1.3], [16.95, 1.3], [16.525, 1.725], [16.1, 1.3]], [1, 2, 2, 79], id='green3_2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.1, 1.3], [16.95, 1.3], [16.525, 1.725], [16.1, 1.3]], [1, 2, 2, 79], id='green3_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([14.9, 4.25], 0.43, id='badge3', facecolor=[0.0, 0.0, 0.0, 0.0])
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 3.0], [20.0, 3.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='body4', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 3.0], [20.0, 3.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='body4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[19.85, 3.0], [21.5, 3.7], [23.15, 3.0], [19.85, 3.0]], [1, 2, 2, 79], id='roof4', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[19.85, 3.0], [21.5, 3.7], [23.15, 3.0], [19.85, 3.0]], [1, 2, 2, 79], id='roof4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[20.5, 0.0], [22.5, 0.0], [22.5, 1.0], [20.5, 1.0], [20.5, 0.0]], [1, 2, 2, 2, 79], id='garage4', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.5, 0.0], [22.5, 0.0], [22.5, 1.0], [20.5, 1.0], [20.5, 0.0]], [1, 2, 2, 2, 79], id='garage4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[22.2, 3.3], [22.65, 3.3], [22.65, 4.3], [22.2, 4.3], [22.2, 3.3]], [1, 2, 2, 2, 79], id='orange4', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.2, 3.3], [22.65, 3.3], [22.65, 4.3], [22.2, 4.3], [22.2, 3.3]], [1, 2, 2, 2, 79], id='orange4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[20.2, 2.2], [20.8, 2.2], [20.2, 2.8], [20.2, 2.2]], [1, 2, 2, 79], id='green4_0', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.2, 2.2], [20.8, 2.2], [20.2, 2.8], [20.2, 2.2]], [1, 2, 2, 79], id='green4_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[20.8, 2.2], [20.8, 2.8], [20.2, 2.8], [20.8, 2.2]], [1, 2, 2, 79], id='green4_1', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.8, 2.2], [20.8, 2.8], [20.2, 2.8], [20.8, 2.2]], [1, 2, 2, 79], id='green4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[22.2, 2.2], [22.8, 2.2], [22.2, 2.8], [22.2, 2.2]], [1, 2, 2, 79], id='green4_2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.2, 2.2], [22.8, 2.2], [22.2, 2.8], [22.2, 2.2]], [1, 2, 2, 79], id='green4_2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.circle([19.9, 4.25], 0.43, id='badge4', facecolor=[0.0, 0.0, 0.0, 0.0])
            for object_id, text, anchor in [('label0', '1', [-0.1, 4.25]), ('label1', '2', [4.9, 4.25]), ('label2', '3', [9.9, 4.25]), ('label3', '4', [14.9, 4.25]), ('label4', '5', [19.9, 4.25])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane209().draw(sys.argv[1] if len(sys.argv) > 1 else None))
