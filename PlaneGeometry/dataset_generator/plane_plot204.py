"""Frozen question Plane204; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane204:

    def __init__(self):
        self.id = 'Plane204'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:484'
        self.question = 'The pattern shown is made from identical tiles with no overlaps. Which of the following tiles could not have been used?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane204.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-1.6921829512171769, 21.42190094666249), ylim=(-7.314981180564869, 15.799102717314797), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[9.0, 7.5], [9.0, 8.5], [8.13397459621556, 8.0], [9.0, 7.5]], [1, 2, 2, 79], id='target0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [9.0, 8.5], [8.13397459621556, 8.0], [9.0, 7.5]], [1, 2, 2, 79], id='target0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 7.5], [8.13397459621556, 8.0], [8.13397459621556, 7.0], [9.0, 7.5]], [1, 2, 2, 79], id='target1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [8.13397459621556, 8.0], [8.13397459621556, 7.0], [9.0, 7.5]], [1, 2, 2, 79], id='target1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 7.5], [8.13397459621556, 7.0], [9.0, 6.5], [9.0, 7.5]], [1, 2, 2, 79], id='target2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [8.13397459621556, 7.0], [9.0, 6.5], [9.0, 7.5]], [1, 2, 2, 79], id='target2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 7.5], [9.0, 6.5], [9.866025403784437, 7.0], [9.0, 7.5]], [1, 2, 2, 79], id='target3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [9.0, 6.5], [9.866025403784437, 7.0], [9.0, 7.5]], [1, 2, 2, 79], id='target3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 7.5], [9.866025403784437, 7.0], [9.86602540378444, 8.0], [9.0, 7.5]], [1, 2, 2, 79], id='target4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [9.866025403784437, 7.0], [9.86602540378444, 8.0], [9.0, 7.5]], [1, 2, 2, 79], id='target4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 7.5], [9.86602540378444, 8.0], [9.0, 8.5], [9.0, 7.5]], [1, 2, 2, 79], id='target5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 7.5], [9.86602540378444, 8.0], [9.0, 8.5], [9.0, 7.5]], [1, 2, 2, 79], id='target5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [8.13397459621556, 7.0], [7.267949192431123, 6.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [8.13397459621556, 7.0], [7.267949192431123, 6.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [7.267949192431123, 6.5], [7.267949192431123, 5.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [7.267949192431123, 6.5], [7.267949192431123, 5.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [7.267949192431123, 5.5], [8.13397459621556, 5.0], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [7.267949192431123, 5.5], [8.13397459621556, 5.0], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [8.13397459621556, 5.0], [9.0, 5.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [8.13397459621556, 5.0], [9.0, 5.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [9.0, 5.5], [9.0, 6.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target10', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [9.0, 5.5], [9.0, 6.5], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[8.13397459621556, 6.0], [9.0, 6.5], [8.13397459621556, 7.0], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target11', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.13397459621556, 6.0], [9.0, 6.5], [8.13397459621556, 7.0], [8.13397459621556, 6.0]], [1, 2, 2, 79], id='target11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [9.86602540378444, 7.0], [9.0, 6.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [9.86602540378444, 7.0], [9.0, 6.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [9.0, 6.5], [9.0, 5.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target13', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [9.0, 6.5], [9.0, 5.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target13', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [9.0, 5.5], [9.866025403784437, 5.0], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target14', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [9.0, 5.5], [9.866025403784437, 5.0], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target14', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [9.866025403784437, 5.0], [10.732050807568877, 5.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target15', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [9.866025403784437, 5.0], [10.732050807568877, 5.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [10.732050807568877, 5.5], [10.732050807568877, 6.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target16', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [10.732050807568877, 5.5], [10.732050807568877, 6.5], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target16', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.86602540378444, 6.0], [10.732050807568877, 6.5], [9.86602540378444, 7.0], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target17', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.86602540378444, 6.0], [10.732050807568877, 6.5], [9.86602540378444, 7.0], [9.86602540378444, 6.0]], [1, 2, 2, 79], id='target17', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [6.123233995736766e-17, 2.0], [-0.8660254037844387, 1.5], [0.0, 1.0]], [1, 2, 2, 79], id='optionA0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [6.123233995736766e-17, 2.0], [-0.8660254037844387, 1.5], [0.0, 1.0]], [1, 2, 2, 79], id='optionA0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [-0.8660254037844387, 1.5], [-0.8660254037844386, 0.4999999999999999], [0.0, 1.0]], [1, 2, 2, 79], id='optionA1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [-0.8660254037844387, 1.5], [-0.8660254037844386, 0.4999999999999999], [0.0, 1.0]], [1, 2, 2, 79], id='optionA1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [-0.8660254037844386, 0.4999999999999999], [-1.8369701987210297e-16, 0.0], [0.0, 1.0]], [1, 2, 2, 79], id='optionA2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [-0.8660254037844386, 0.4999999999999999], [-1.8369701987210297e-16, 0.0], [0.0, 1.0]], [1, 2, 2, 79], id='optionA2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [-1.8369701987210297e-16, 0.0], [0.8660254037844384, 0.49999999999999956], [0.0, 1.0]], [1, 2, 2, 79], id='optionA3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [-1.8369701987210297e-16, 0.0], [0.8660254037844384, 0.49999999999999956], [0.0, 1.0]], [1, 2, 2, 79], id='optionA3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [0.8660254037844384, 0.49999999999999956], [0.8660254037844386, 1.5], [0.0, 1.0]], [1, 2, 2, 79], id='optionA4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [0.8660254037844384, 0.49999999999999956], [0.8660254037844386, 1.5], [0.0, 1.0]], [1, 2, 2, 79], id='optionA4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [0.8660254037844386, 1.5], [6.123233995736766e-17, 2.0], [0.0, 1.0]], [1, 2, 2, 79], id='optionA5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [0.8660254037844386, 1.5], [6.123233995736766e-17, 2.0], [0.0, 1.0]], [1, 2, 2, 79], id='optionA5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 1.5], [5.0, 0.5], [5.866025403784438, 1.0], [5.0, 1.5]], [1, 2, 2, 79], id='optionB0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.5], [5.0, 0.5], [5.866025403784438, 1.0], [5.0, 1.5]], [1, 2, 2, 79], id='optionB0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 0.5], [5.866025403784438, 1.0], [5.866025403784438, 0.0], [5.0, 0.5]], [1, 2, 2, 79], id='optionB1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.5], [5.866025403784438, 1.0], [5.866025403784438, 0.0], [5.0, 0.5]], [1, 2, 2, 79], id='optionB1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 1.5], [10.86602540378444, 2.0], [10.86602540378444, 1.0], [10.0, 1.5]], [1, 2, 2, 79], id='optionC0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 1.5], [10.86602540378444, 2.0], [10.86602540378444, 1.0], [10.0, 1.5]], [1, 2, 2, 79], id='optionC0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 1.5], [10.86602540378444, 1.0], [10.0, 0.5], [10.0, 1.5]], [1, 2, 2, 79], id='optionC1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 1.5], [10.86602540378444, 1.0], [10.0, 0.5], [10.0, 1.5]], [1, 2, 2, 79], id='optionC1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.0, 0.5], [10.86602540378444, 1.0], [10.86602540378444, 0.0], [10.0, 0.5]], [1, 2, 2, 79], id='optionC2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.5], [10.86602540378444, 1.0], [10.86602540378444, 0.0], [10.0, 0.5]], [1, 2, 2, 79], id='optionC2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.86602540378444, 1.0], [10.86602540378444, 0.0], [11.732050807568877, 0.5], [10.86602540378444, 1.0]], [1, 2, 2, 79], id='optionC3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.86602540378444, 1.0], [10.86602540378444, 0.0], [11.732050807568877, 0.5], [10.86602540378444, 1.0]], [1, 2, 2, 79], id='optionC3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[10.86602540378444, 1.0], [11.732050807568877, 1.5], [11.732050807568877, 0.5], [10.86602540378444, 1.0]], [1, 2, 2, 79], id='optionC4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[10.86602540378444, 1.0], [11.732050807568877, 1.5], [11.732050807568877, 0.5], [10.86602540378444, 1.0]], [1, 2, 2, 79], id='optionC4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[11.732050807568877, 1.5], [12.598076211353316, 1.0], [11.732050807568877, 0.5], [11.732050807568877, 1.5]], [1, 2, 2, 79], id='optionC5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[11.732050807568877, 1.5], [12.598076211353316, 1.0], [11.732050807568877, 0.5], [11.732050807568877, 1.5]], [1, 2, 2, 79], id='optionC5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.13397459621556, 2.5], [15.0, 3.0], [15.0, 2.0], [14.13397459621556, 2.5]], [1, 2, 2, 79], id='optionD0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.13397459621556, 2.5], [15.0, 3.0], [15.0, 2.0], [14.13397459621556, 2.5]], [1, 2, 2, 79], id='optionD0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[15.0, 3.0], [15.86602540378444, 2.5], [15.0, 2.0], [15.0, 3.0]], [1, 2, 2, 79], id='optionD1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[15.0, 3.0], [15.86602540378444, 2.5], [15.0, 2.0], [15.0, 3.0]], [1, 2, 2, 79], id='optionD1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.13397459621556, 2.5], [14.13397459621556, 1.5], [15.0, 2.0], [14.13397459621556, 2.5]], [1, 2, 2, 79], id='optionD2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.13397459621556, 2.5], [14.13397459621556, 1.5], [15.0, 2.0], [14.13397459621556, 2.5]], [1, 2, 2, 79], id='optionD2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.13397459621556, 1.5], [15.0, 2.0], [15.0, 1.0], [14.13397459621556, 1.5]], [1, 2, 2, 79], id='optionD3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.13397459621556, 1.5], [15.0, 2.0], [15.0, 1.0], [14.13397459621556, 1.5]], [1, 2, 2, 79], id='optionD3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.13397459621556, 1.5], [14.13397459621556, 0.5], [15.0, 1.0], [14.13397459621556, 1.5]], [1, 2, 2, 79], id='optionD4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.13397459621556, 1.5], [14.13397459621556, 0.5], [15.0, 1.0], [14.13397459621556, 1.5]], [1, 2, 2, 79], id='optionD4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.13397459621556, 0.5], [15.0, 1.0], [15.0, 0.0], [14.13397459621556, 0.5]], [1, 2, 2, 79], id='optionD5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.13397459621556, 0.5], [15.0, 1.0], [15.0, 0.0], [14.13397459621556, 0.5]], [1, 2, 2, 79], id='optionD5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 1.5], [20.866025403784437, 2.0], [20.866025403784437, 1.0], [20.0, 1.5]], [1, 2, 2, 79], id='optionE0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 1.5], [20.866025403784437, 2.0], [20.866025403784437, 1.0], [20.0, 1.5]], [1, 2, 2, 79], id='optionE0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 1.5], [20.866025403784437, 1.0], [20.0, 0.5], [20.0, 1.5]], [1, 2, 2, 79], id='optionE1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 1.5], [20.866025403784437, 1.0], [20.0, 0.5], [20.0, 1.5]], [1, 2, 2, 79], id='optionE1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 0.5], [20.866025403784437, 1.0], [20.866025403784437, 0.0], [20.0, 0.5]], [1, 2, 2, 79], id='optionE2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.5], [20.866025403784437, 1.0], [20.866025403784437, 0.0], [20.0, 0.5]], [1, 2, 2, 79], id='optionE2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', 'A)', (-0.8, 3.8)), ('label1', 'B)', (4.2, 3.8)), ('label2', 'C)', (9.2, 3.8)), ('label3', 'D)', (14.2, 3.8)), ('label4', 'E)', (19.2, 3.8))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane204().draw(sys.argv[1] if len(sys.argv) > 1 else None))
