"""Frozen question Plane453; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane453:

    def __init__(self):
        self.id = 'Plane453'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2529'
        self.question = 'Which of the five "T-like shapes" would be symmetric to the one shown with respect to the dashed line?\n\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane453.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.7855663532019843, 23.648322731575185], ylim=[-8.488165377992994, 16.94572370678418], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[14.0, 5.0], [17.0, 5.0], [17.0, 8.0], [14.0, 8.0], [14.0, 5.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[14.0, 7.4], [14.6, 7.4], [14.6, 8.0], [14.0, 8.0], [14.0, 7.4]], [1, 2, 2, 2, 79], id='o1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[14.0, 7.4], [14.6, 7.4], [14.6, 8.0], [14.0, 8.0], [14.0, 7.4]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[14.6, 6.2], [15.8, 7.4]], id='o2')
            c.line([[15.2, 6.8], [16.4, 5.6]], id='o3')
            c.path([[0.0, 0.0], [3.0, 0.0], [3.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o4', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.4, 2.4], [3.0, 2.4], [3.0, 3.0], [2.4, 3.0], [2.4, 2.4]], [1, 2, 2, 2, 79], id='o5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.4, 2.4], [3.0, 2.4], [3.0, 3.0], [2.4, 3.0], [2.4, 2.4]], [1, 2, 2, 2, 79], id='o5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[0.6, 1.2], [1.8, 2.4]], id='o6')
            c.line([[1.2, 1.8], [2.4, 0.6]], id='o7')
            c.path([[5.0, 0.0], [8.0, 0.0], [8.0, 3.0], [5.0, 3.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='o8', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.4, 2.4], [8.0, 2.4], [8.0, 3.0], [7.4, 3.0], [7.4, 2.4]], [1, 2, 2, 2, 79], id='o9', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.4, 2.4], [8.0, 2.4], [8.0, 3.0], [7.4, 3.0], [7.4, 2.4]], [1, 2, 2, 2, 79], id='o9', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[7.4, 1.2], [6.2, 2.4]], id='o10')
            c.line([[6.8, 1.8], [5.6, 0.6]], id='o11')
            c.path([[10.0, 0.0], [13.0, 0.0], [13.0, 3.0], [10.0, 3.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='o12', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[12.4, 2.4], [13.0, 2.4], [13.0, 3.0], [12.4, 3.0], [12.4, 2.4]], [1, 2, 2, 2, 79], id='o13', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.4, 2.4], [13.0, 2.4], [13.0, 3.0], [12.4, 3.0], [12.4, 2.4]], [1, 2, 2, 2, 79], id='o13', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[10.6, 2.4], [11.8, 1.2]], id='o14')
            c.line([[11.2, 0.6], [12.4, 1.8]], id='o15')
            c.path([[15.0, 0.0], [18.0, 0.0], [18.0, 3.0], [15.0, 3.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='o16', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[17.4, 0.0], [18.0, 0.0], [18.0, 0.6], [17.4, 0.6], [17.4, 0.0]], [1, 2, 2, 2, 79], id='o17', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.4, 0.0], [18.0, 0.0], [18.0, 0.6], [17.4, 0.6], [17.4, 0.0]], [1, 2, 2, 2, 79], id='o17', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[15.6, 1.8], [16.8, 0.6]], id='o18')
            c.line([[16.2, 1.2], [17.4, 2.4]], id='o19')
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 3.0], [20.0, 3.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='o20', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[20.0, 2.4], [20.6, 2.4], [20.6, 3.0], [20.0, 3.0], [20.0, 2.4]], [1, 2, 2, 2, 79], id='o21', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.0, 2.4], [20.6, 2.4], [20.6, 3.0], [20.0, 3.0], [20.0, 2.4]], [1, 2, 2, 2, 79], id='o21', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[21.2, 2.4], [22.4, 2.4]], id='o22')
            c.line([[21.8, 2.4], [21.8, 0.6]], id='o23')
            c.line([[12.8, 4.4], [12.8, 8.6]], id='o24', linestyle=(0.0, [4.0, 3.0]))
            for object_id, text, anchor in [('t0', '(A)', [-0.7, 3.1]), ('t1', '(B)', [4.3, 3.1]), ('t2', '(C)', [9.3, 3.1]), ('t3', '(D)', [14.3, 3.1]), ('t4', '(E)', [19.3, 3.1])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane453().draw(sys.argv[1] if len(sys.argv) > 1 else None))
