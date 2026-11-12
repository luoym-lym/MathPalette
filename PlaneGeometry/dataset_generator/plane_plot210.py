"""Frozen question Plane210; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane210:

    def __init__(self):
        self.id = 'Plane210'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:514'
        self.question = 'Which square should replace the question mark so that the white and black areas are equal?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane210.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.6241903583124317, 17.479527269618583], ylim=[-6.113398112242287, 12.990319515688729], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='source0_0_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.15, 6.0], [8.15, 6.0], [8.15, 7.0], [7.15, 7.0], [7.15, 6.0]], [1, 2, 2, 2, 79], id='source1_0_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.15, 6.0], [8.15, 6.0], [8.15, 7.0], [7.15, 7.0], [7.15, 6.0]], [1, 2, 2, 2, 79], id='source1_0_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.15, 6.0], [8.15, 6.0], [8.15, 7.0], [7.15, 7.0], [7.15, 6.0]], [1, 2, 2, 2, 79], id='source1_0_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.3, 6.0], [9.3, 6.0], [9.3, 7.0], [8.3, 7.0], [8.3, 6.0]], [1, 2, 2, 2, 79], id='source2_0_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[8.3, 6.0], [9.3, 6.0], [9.3, 7.0], [8.3, 7.0], [8.3, 6.0]], [1, 2, 2, 2, 79], id='source2_0_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.3, 6.0], [9.3, 6.0], [9.3, 7.0], [8.3, 7.0], [8.3, 6.0]], [1, 2, 2, 2, 79], id='source2_0_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 4.85], [7.0, 4.85], [7.0, 5.85], [6.0, 5.85], [6.0, 4.85]], [1, 2, 2, 2, 79], id='source0_1_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 4.85], [7.0, 4.85], [7.0, 5.85], [6.0, 4.85]], [1, 2, 2, 79], id='source0_1_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.85], [7.0, 4.85], [7.0, 5.85], [6.0, 4.85]], [1, 2, 2, 79], id='source0_1_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.15, 4.85], [8.15, 4.85], [8.15, 5.85], [7.15, 5.85], [7.15, 4.85]], [1, 2, 2, 2, 79], id='source1_1_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.15, 4.85], [7.15, 5.85], [8.15, 5.85], [7.15, 4.85]], [1, 2, 2, 79], id='source1_1_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.15, 4.85], [7.15, 5.85], [8.15, 5.85], [7.15, 4.85]], [1, 2, 2, 79], id='source1_1_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.3, 4.85], [9.3, 4.85], [9.3, 5.85], [8.3, 5.85], [8.3, 4.85]], [1, 2, 2, 2, 79], id='source2_1_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 3.7], [7.0, 3.7], [7.0, 4.7], [6.0, 4.7], [6.0, 3.7]], [1, 2, 2, 2, 79], id='source0_2_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 4.2], [7.0, 4.2], [7.0, 4.7], [6.0, 4.7], [6.0, 4.2]], [1, 2, 2, 2, 79], id='source0_2_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.2], [7.0, 4.2], [7.0, 4.7], [6.0, 4.7], [6.0, 4.2]], [1, 2, 2, 2, 79], id='source0_2_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('source1_2_border', [[7.15, 3.7], [8.15, 3.7], [8.15, 4.7], [7.15, 4.7], [7.15, 3.7]], [1, 2, 2, 2, 79]), ('A_border', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('B_border', [[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='B_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='B_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='C_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 0.5], [8.0, 0.5], [8.0, 0.0]], [1, 2, 2, 2, 79], id='C_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 0.5], [8.0, 0.5], [8.0, 0.0]], [1, 2, 2, 2, 79], id='C_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='D_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [12.5, 0.5], [12.0, 1.0]], [1, 2, 2, 79], id='D_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [12.5, 0.5], [12.0, 1.0]], [1, 2, 2, 79], id='D_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='E_border', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.5, 0.5], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 2, 79], id='E_gray', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.5, 0.5], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 2, 79], id='E_gray', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '?', [8.8, 4.2]), ('label1', '(A)', [-0.8, 0.1]), ('label2', '(B)', [3.2, 0.1]), ('label3', '(C)', [7.2, 0.1]), ('label4', '(D)', [11.2, 0.1]), ('label5', '(E)', [15.2, 0.1])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane210().draw(sys.argv[1] if len(sys.argv) > 1 else None))
