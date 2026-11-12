"""Frozen question Plane205; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane205:

    def __init__(self):
        self.id = 'Plane205'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:488'
        self.question = 'In which of the five pictures is the white area bigger than the grey area?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane205.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4664793323475376, 18.466739326729446], ylim=[-8.826081901674582, 10.107136757402403], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 2.0], [2.0, 2.0], [2.0, 1.0], [0.0, 2.0]], [1, 2, 2, 79], id='gray0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [2.0, 2.0], [2.0, 1.0], [0.0, 2.0]], [1, 2, 2, 79], id='gray0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [0.0, 1.0], [2.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='gray0_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [0.0, 1.0], [2.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='gray0_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='frame0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('partition0_0', [[0.0, 1.0], [2.0, 1.0]]), ('partition0_1', [[0.0, 0.0], [2.0, 1.0]]), ('partition0_2', [[0.0, 2.0], [2.0, 1.0]])]:
                c.line(points, id=object_id)
            c.path([[4.0, 0.0], [4.0, 2.0], [5.0, 1.0], [4.0, 0.0]], [1, 2, 2, 79], id='gray1_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [4.0, 2.0], [5.0, 1.0], [4.0, 0.0]], [1, 2, 2, 79], id='gray1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [6.0, 2.0], [5.0, 1.0], [6.0, 0.0]], [1, 2, 2, 79], id='gray1_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [6.0, 2.0], [5.0, 1.0], [6.0, 0.0]], [1, 2, 2, 79], id='gray1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.0, 0.0], [6.0, 0.0], [6.0, 2.0], [4.0, 2.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='frame1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[4.0, 0.0], [6.0, 2.0]], id='partition1_0')
            c.line([[4.0, 2.0], [6.0, 0.0]], id='partition1_1')
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='gray2_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='gray2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='gray2_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='gray2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 0.0], [10.0, 0.0], [10.0, 2.0], [8.0, 2.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='frame2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[9.0, 0.0], [9.0, 2.0]], id='partition2_0')
            c.line([[8.0, 1.0], [10.0, 1.0]], id='partition2_1')
            c.path([[12.0, 1.0], [12.0, 2.0], [13.0, 1.0], [12.0, 1.0]], [1, 2, 2, 79], id='gray3_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [12.0, 2.0], [13.0, 1.0], [12.0, 1.0]], [1, 2, 2, 79], id='gray3_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[13.0, 1.0], [14.0, 1.0], [14.0, 0.0], [13.0, 1.0]], [1, 2, 2, 79], id='gray3_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[13.0, 1.0], [14.0, 1.0], [14.0, 0.0], [13.0, 1.0]], [1, 2, 2, 79], id='gray3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 0.0], [14.0, 0.0], [14.0, 2.0], [12.0, 2.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='frame3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[12.0, 2.0], [14.0, 0.0]], id='partition3_0')
            c.line([[12.0, 1.0], [14.0, 1.0]], id='partition3_1')
            c.path([[16.0, 2.0], [17.0, 2.0], [17.0, 1.0], [16.0, 2.0]], [1, 2, 2, 79], id='gray4_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 2.0], [17.0, 2.0], [17.0, 1.0], [16.0, 2.0]], [1, 2, 2, 79], id='gray4_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 2.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='gray4_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 2.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='gray4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 0.0], [18.0, 0.0], [18.0, 2.0], [16.0, 2.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='frame4', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('partition4_0', [[17.0, 0.0], [17.0, 2.0]]), ('partition4_1', [[16.0, 2.0], [17.0, 1.0]]), ('partition4_2', [[17.0, 1.0], [18.0, 2.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', '(A)', [1.0, -0.5]), ('label1', '(B)', [5.0, -0.5]), ('label2', '(C)', [9.0, -0.5]), ('label3', '(D)', [13.0, -0.5]), ('label4', '(E)', [17.0, -0.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane205().draw(sys.argv[1] if len(sys.argv) > 1 else None))
