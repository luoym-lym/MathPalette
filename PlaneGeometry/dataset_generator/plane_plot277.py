"""Frozen question Plane277; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane277:

    def __init__(self):
        self.id = 'Plane277'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:834'
        self.question = 'Which square has to replace the question mark so that the white area and the black area are equally big?\nChoices:\nA:(A)\nB:(B)\nC:(C)\nD:(D)\nE:(E)'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '(A)', 'B': '(B)', 'C': '(C)', 'D': '(D)', 'E': '(E)'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane277.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.3269875340725017, 13.376313810734903], ylim=[-3.933384623153354, 10.769916721654049], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[6.0, 7.0], [7.0, 7.0], [6.0, 6.0], [6.0, 7.0]], [1, 2, 2, 79], id='given_gray0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 7.0], [7.0, 7.0], [6.0, 6.0], [6.0, 7.0]], [1, 2, 2, 79], id='given_gray0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 7.0], [8.0, 7.0], [7.5, 6.5], [7.0, 7.0]], [1, 2, 2, 79], id='given_gray1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 7.0], [8.0, 7.0], [7.5, 6.5], [7.0, 7.0]], [1, 2, 2, 79], id='given_gray1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 6.0], [8.0, 6.0], [7.5, 6.5], [7.0, 6.0]], [1, 2, 2, 79], id='given_gray2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 6.0], [8.0, 6.0], [7.5, 6.5], [7.0, 6.0]], [1, 2, 2, 79], id='given_gray2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 7.0], [9.0, 7.0], [9.0, 6.0], [8.0, 7.0]], [1, 2, 2, 79], id='given_gray3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 7.0], [9.0, 7.0], [9.0, 6.0], [8.0, 7.0]], [1, 2, 2, 79], id='given_gray3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 5.0]], [1, 2, 2, 79], id='given_gray4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 5.0]], [1, 2, 2, 79], id='given_gray4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 5.0], [7.0, 6.0], [8.0, 6.0], [7.0, 5.0]], [1, 2, 2, 79], id='given_gray5', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 5.0], [7.0, 6.0], [8.0, 6.0], [7.0, 5.0]], [1, 2, 2, 79], id='given_gray5', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.0], [7.0, 5.0], [6.5, 4.5], [6.0, 5.0]], [1, 2, 2, 79], id='given_gray6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 5.0], [7.0, 5.0], [6.5, 4.5], [6.0, 5.0]], [1, 2, 2, 79], id='given_gray6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 4.0], [7.0, 4.0], [6.5, 4.5], [6.0, 4.0]], [1, 2, 2, 79], id='given_gray7', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 4.0], [7.0, 4.0], [6.5, 4.5], [6.0, 4.0]], [1, 2, 2, 79], id='given_gray7', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 4.0]], [1, 2, 2, 79], id='given_gray8', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 4.0]], [1, 2, 2, 79], id='given_gray8', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('given_grid_0', [[6.0, 4.0], [6.0, 5.0]]), ('given_grid_1', [[6.0, 4.0], [7.0, 4.0]]), ('given_grid_2', [[6.0, 5.0], [6.0, 6.0]]), ('given_grid_3', [[6.0, 5.0], [7.0, 5.0]]), ('given_grid_4', [[6.0, 6.0], [6.0, 7.0]]), ('given_grid_5', [[6.0, 6.0], [7.0, 6.0]]), ('given_grid_6', [[6.0, 7.0], [7.0, 7.0]]), ('given_grid_7', [[7.0, 4.0], [7.0, 5.0]]), ('given_grid_8', [[7.0, 4.0], [8.0, 4.0]]), ('given_grid_9', [[7.0, 5.0], [7.0, 6.0]]), ('given_grid_10', [[7.0, 5.0], [8.0, 5.0]]), ('given_grid_11', [[7.0, 6.0], [7.0, 7.0]]), ('given_grid_12', [[7.0, 6.0], [8.0, 6.0]]), ('given_grid_13', [[7.0, 7.0], [8.0, 7.0]]), ('given_grid_14', [[8.0, 4.0], [8.0, 5.0]]), ('given_grid_15', [[8.0, 5.0], [8.0, 6.0]]), ('given_grid_16', [[8.0, 5.0], [9.0, 5.0]]), ('given_grid_17', [[8.0, 6.0], [8.0, 7.0]]), ('given_grid_18', [[8.0, 6.0], [9.0, 6.0]]), ('given_grid_19', [[8.0, 7.0], [9.0, 7.0]]), ('given_grid_20', [[9.0, 5.0], [9.0, 6.0]]), ('given_grid_21', [[9.0, 6.0], [9.0, 7.0]])]:
                c.line(points, id=object_id)
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='option_square0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='option1_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='option1_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='option_square1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 79], id='option2_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 79], id='option2_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [6.5, 0.5], [6.0, 0.0]], [1, 2, 2, 79], id='option2_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [6.5, 0.5], [6.0, 0.0]], [1, 2, 2, 79], id='option2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='option_square2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 0.0]], [1, 2, 2, 79], id='option3_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 0.0]], [1, 2, 2, 79], id='option3_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='option_square3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.5, 0.5], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option4_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.5, 0.5], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option4_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='option_square4', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, text, anchor in [('label0', '?', [8.5, 4.5]), ('label1', '(A)', [-0.7, 0.0]), ('label2', '(B)', [2.3, 0.0]), ('label3', '(C)', [5.3, 0.0]), ('label4', '(D)', [8.3, 0.0]), ('label5', '(E)', [11.3, 0.0])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane277().draw(sys.argv[1] if len(sys.argv) > 1 else None))
