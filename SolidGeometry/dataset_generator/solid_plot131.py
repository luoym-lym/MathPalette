"""Frozen question Solid131; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid131:

    def __init__(self):
        self.id = 'Solid131'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:902'
        self.question = 'The sum of the dots on opposite sides of an ordinary die is 7. Which of the following dice could be an ordinary die?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid131.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-1.014466360101534, 10.788238780529145), ylim=(-5.119651439950348, 6.683053700680332), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('die0e0', [[0.0, 0.0], [1.0, 0.0]]), ('die0e1', [[0.0, 1.0], [1.0, 1.0]]), ('die0e2', [[0.7, 1.65], [1.7, 1.65]]), ('die0e3', [[0.0, 1.0], [0.7, 1.65]]), ('die0e4', [[1.0, 0.0], [1.7, 0.65]]), ('die0e5', [[1.0, 1.0], [1.7, 1.65]]), ('die0e6', [[0.0, 0.0], [0.0, 1.0]]), ('die0e7', [[1.0, 0.0], [1.0, 1.0]]), ('die0e8', [[1.7, 0.65], [1.7, 1.65]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[1.0, 0.0], [1.7, 0.65], [1.7, 1.65], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='sidegray0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('pip0top0', [[0.7749999999999999, 1.4875]]), ('pip0top1', [[0.925, 1.1625]]), ('pip0front0', [[0.25, 0.25]]), ('pip0front1', [[0.25, 0.75]]), ('pip0front2', [[0.5, 0.5]]), ('pip0front3', [[0.75, 0.25]]), ('pip0front4', [[0.75, 0.75]]), ('pip0right0', [[1.175, 0.4125]]), ('pip0right1', [[1.175, 0.9125]]), ('pip0right2', [[1.525, 0.7375]]), ('pip0right3', [[1.525, 1.2375]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            for object_id, points in [('die1e0', [[2.2, 0.0], [3.2, 0.0]]), ('die1e1', [[2.2, 1.0], [3.2, 1.0]]), ('die1e2', [[2.9000000000000004, 1.65], [3.9000000000000004, 1.65]]), ('die1e3', [[2.2, 1.0], [2.9000000000000004, 1.65]]), ('die1e4', [[3.2, 0.0], [3.9000000000000004, 0.65]]), ('die1e5', [[3.2, 1.0], [3.9000000000000004, 1.65]]), ('die1e6', [[2.2, 0.0], [2.2, 1.0]]), ('die1e7', [[3.2, 0.0], [3.2, 1.0]]), ('die1e8', [[3.9000000000000004, 0.65], [3.9000000000000004, 1.65]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[3.2, 0.0], [3.9000000000000004, 0.65], [3.9000000000000004, 1.65], [3.2, 1.0], [3.2, 0.0]], [1, 2, 2, 2, 79], id='sidegray1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('pip1top0', [[2.625, 1.1625]]), ('pip1top1', [[2.975, 1.4875]]), ('pip1top2', [[3.125, 1.1625]]), ('pip1top3', [[3.475, 1.4875]]), ('pip1front0', [[2.45, 0.75]]), ('pip1front1', [[2.7, 0.5]]), ('pip1front2', [[2.95, 0.25]]), ('pip1right0', [[3.5500000000000003, 0.825]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            for object_id, points in [('die2e0', [[4.4, 0.0], [5.4, 0.0]]), ('die2e1', [[4.4, 1.0], [5.4, 1.0]]), ('die2e2', [[5.1000000000000005, 1.65], [6.1000000000000005, 1.65]]), ('die2e3', [[4.4, 1.0], [5.1000000000000005, 1.65]]), ('die2e4', [[5.4, 0.0], [6.1000000000000005, 0.65]]), ('die2e5', [[5.4, 1.0], [6.1000000000000005, 1.65]]), ('die2e6', [[4.4, 0.0], [4.4, 1.0]]), ('die2e7', [[5.4, 0.0], [5.4, 1.0]]), ('die2e8', [[6.1000000000000005, 0.65], [6.1000000000000005, 1.65]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[5.4, 0.0], [6.1000000000000005, 0.65], [6.1000000000000005, 1.65], [5.4, 1.0], [5.4, 0.0]], [1, 2, 2, 2, 79], id='sidegray2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('pip2top0', [[4.775, 1.1625]]), ('pip2top1', [[5.25, 1.325]]), ('pip2top2', [[5.725, 1.4875]]), ('pip2front0', [[4.65, 0.25]]), ('pip2front1', [[4.65, 0.75]]), ('pip2front2', [[5.15, 0.25]]), ('pip2front3', [[5.15, 0.75]]), ('pip2right0', [[5.575, 0.4125]]), ('pip2right1', [[5.575, 0.9125]]), ('pip2right2', [[5.75, 0.825]]), ('pip2right3', [[5.925000000000001, 0.7375]]), ('pip2right4', [[5.925000000000001, 1.2375]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            for object_id, points in [('die3e0', [[6.6000000000000005, 0.0], [7.6000000000000005, 0.0]]), ('die3e1', [[6.6000000000000005, 1.0], [7.6000000000000005, 1.0]]), ('die3e2', [[7.300000000000001, 1.65], [8.3, 1.65]]), ('die3e3', [[6.6000000000000005, 1.0], [7.300000000000001, 1.65]]), ('die3e4', [[7.6000000000000005, 0.0], [8.3, 0.65]]), ('die3e5', [[7.6000000000000005, 1.0], [8.3, 1.65]]), ('die3e6', [[6.6000000000000005, 0.0], [6.6000000000000005, 1.0]]), ('die3e7', [[7.6000000000000005, 0.0], [7.6000000000000005, 1.0]]), ('die3e8', [[8.3, 0.65], [8.3, 1.65]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[7.6000000000000005, 0.0], [8.3, 0.65], [8.3, 1.65], [7.6000000000000005, 1.0], [7.6000000000000005, 0.0]], [1, 2, 2, 2, 79], id='sidegray3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('pip3top0', [[7.45, 1.325]]), ('pip3front0', [[6.82, 0.28]]), ('pip3front1', [[6.82, 0.72]]), ('pip3front2', [[7.1000000000000005, 0.28]]), ('pip3front3', [[7.1000000000000005, 0.72]]), ('pip3front4', [[7.380000000000001, 0.28]]), ('pip3front5', [[7.380000000000001, 0.72]]), ('pip3right0', [[7.775, 0.4125]]), ('pip3right1', [[7.775, 0.9125]]), ('pip3right2', [[7.95, 0.825]]), ('pip3right3', [[8.125, 0.7375]]), ('pip3right4', [[8.125, 1.2375]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            for object_id, points in [('die4e0', [[8.8, 0.0], [9.8, 0.0]]), ('die4e1', [[8.8, 1.0], [9.8, 1.0]]), ('die4e2', [[9.5, 1.65], [10.5, 1.65]]), ('die4e3', [[8.8, 1.0], [9.5, 1.65]]), ('die4e4', [[9.8, 0.0], [10.5, 0.65]]), ('die4e5', [[9.8, 1.0], [10.5, 1.65]]), ('die4e6', [[8.8, 0.0], [8.8, 1.0]]), ('die4e7', [[9.8, 0.0], [9.8, 1.0]]), ('die4e8', [[10.5, 0.65], [10.5, 1.65]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[9.8, 0.0], [10.5, 0.65], [10.5, 1.65], [9.8, 1.0], [9.8, 0.0]], [1, 2, 2, 2, 79], id='sidegray4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('pip4top0', [[9.22, 1.13]]), ('pip4top1', [[9.43, 1.325]]), ('pip4top2', [[9.64, 1.52]]), ('pip4top3', [[9.660000000000002, 1.13]]), ('pip4top4', [[9.870000000000001, 1.325]]), ('pip4top5', [[10.080000000000002, 1.52]]), ('pip4front0', [[9.08, 0.72]]), ('pip4front1', [[9.520000000000001, 0.28]]), ('pip4right0', [[9.975000000000001, 0.4125]]), ('pip4right1', [[9.975000000000001, 0.9125]]), ('pip4right2', [[10.325000000000001, 0.7375]]), ('pip4right3', [[10.325000000000001, 1.2375]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            for object_id, text, anchor in [('option0', '(A)', (-0.5, 0.05)), ('option1', '(B)', (1.7000000000000002, 0.05)), ('option2', '(C)', (3.9000000000000004, 0.05)), ('option3', '(D)', (6.1000000000000005, 0.05)), ('option4', '(E)', (8.3, 0.05))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid131().draw(sys.argv[1] if len(sys.argv) > 1 else None))
