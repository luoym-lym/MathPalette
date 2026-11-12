"""Frozen question Plane208; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane208:

    def __init__(self):
        self.id = 'Plane208'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:505'
        self.question = 'Which of the following pieces can be joined to the one pictured so that a rectangle is formed?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane208.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.3179473620595203, 28.783865750989158], ylim=[-10.14310759886392, 20.958705514184757], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[12.0, 7.0], [13.0, 7.0], [14.0, 7.0], [15.0, 7.0], [16.0, 7.0], [16.0, 8.0], [16.0, 9.0], [15.0, 9.0], [15.0, 10.0], [14.0, 10.0], [14.0, 9.0], [13.0, 9.0], [13.0, 10.0], [13.0, 11.0], [12.0, 11.0], [12.0, 10.0], [12.0, 9.0], [12.0, 8.0], [12.0, 7.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='given', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 7.0], [13.0, 7.0], [14.0, 7.0], [15.0, 7.0], [16.0, 7.0], [16.0, 8.0], [16.0, 9.0], [15.0, 9.0], [15.0, 10.0], [14.0, 10.0], [14.0, 9.0], [13.0, 9.0], [13.0, 10.0], [13.0, 11.0], [12.0, 11.0], [12.0, 10.0], [12.0, 9.0], [12.0, 8.0], [12.0, 7.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='given', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 3.0], [2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0], [0.0, 2.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='A', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 3.0], [2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0], [0.0, 2.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='A', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 3.0], [9.0, 3.0], [9.0, 4.0], [8.0, 4.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0], [6.0, 2.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='B', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 3.0], [9.0, 3.0], [9.0, 4.0], [8.0, 4.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0], [6.0, 2.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='B', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 0.0], [14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [15.0, 2.0], [15.0, 3.0], [15.0, 4.0], [14.0, 4.0], [13.0, 4.0], [13.0, 3.0], [14.0, 3.0], [14.0, 2.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='C', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 0.0], [14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [15.0, 2.0], [15.0, 3.0], [15.0, 4.0], [14.0, 4.0], [13.0, 4.0], [13.0, 3.0], [14.0, 3.0], [14.0, 2.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='C', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[18.0, 0.0], [19.0, 0.0], [20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [22.0, 2.0], [22.0, 3.0], [22.0, 4.0], [21.0, 4.0], [20.0, 4.0], [19.0, 4.0], [19.0, 3.0], [20.0, 3.0], [21.0, 3.0], [21.0, 2.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[18.0, 0.0], [19.0, 0.0], [20.0, 0.0], [21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [22.0, 2.0], [22.0, 3.0], [22.0, 4.0], [21.0, 4.0], [20.0, 4.0], [19.0, 4.0], [19.0, 3.0], [20.0, 3.0], [21.0, 3.0], [21.0, 2.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='D', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[24.0, 0.0], [25.0, 0.0], [26.0, 0.0], [26.0, 1.0], [25.0, 1.0], [25.0, 2.0], [26.0, 2.0], [27.0, 2.0], [28.0, 2.0], [28.0, 3.0], [27.0, 3.0], [27.0, 4.0], [26.0, 4.0], [25.0, 4.0], [24.0, 4.0], [24.0, 3.0], [24.0, 2.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[24.0, 0.0], [25.0, 0.0], [26.0, 0.0], [26.0, 1.0], [25.0, 1.0], [25.0, 2.0], [26.0, 2.0], [27.0, 2.0], [28.0, 2.0], [28.0, 3.0], [27.0, 3.0], [27.0, 4.0], [26.0, 4.0], [25.0, 4.0], [24.0, 4.0], [24.0, 3.0], [24.0, 2.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='E', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', [-1.0, 0.2]), ('label1', '(B)', [5.0, 0.2]), ('label2', '(C)', [11.0, 0.2]), ('label3', '(D)', [17.0, 0.2]), ('label4', '(E)', [23.0, 0.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane208().draw(sys.argv[1] if len(sys.argv) > 1 else None))
