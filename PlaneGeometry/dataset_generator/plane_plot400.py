"""Frozen question Plane400; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane400:

    def __init__(self):
        self.id = 'Plane400'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1669'
        self.question = 'Some identical rectangles are drawn. A triangle of base $10 \\mathrm{~cm}$ and height $6 \\mathrm{~cm}$ is drawn over them, as shown, and the region inside the rectangles and outside the triangle is shaded. What is the area of the shaded region?\nChoices:\nA:$10 \\mathrm{~cm}^{2}$\nB:$12 \\mathrm{~cm}^{2}$\nC:$14 \\mathrm{~cm}^{2}$\nD:$15 \\mathrm{~cm}^{2}$\nE:$21 \\mathrm{~cm}^{2}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$10 \\mathrm{~cm}^{2}$', 'B': '$12 \\mathrm{~cm}^{2}$', 'C': '$14 \\mathrm{~cm}^{2}$', 'D': '$15 \\mathrm{~cm}^{2}$', 'E': '$21 \\mathrm{~cm}^{2}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane400.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.4139107154211272, 10.315694095403135], ylim=[-3.9527219655973154, 8.776882845226947], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[5.800000000000001, 4.5], [6.4, 4.5], [6.4, 6.0], [4.4, 6.0], [4.4, 6.0], [5.800000000000001, 4.5]], [1, 2, 2, 2, 2, 79], id='fill3_1_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[5.800000000000001, 4.5], [6.4, 4.5], [6.4, 6.0], [4.4, 6.0], [4.4, 6.0], [5.800000000000001, 4.5]], [1, 2, 2, 2, 2, 79], id='fill3_1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.4, 4.5], [3.3000000000000003, 4.5], [4.4, 6.0], [4.4, 6.0], [2.4, 6.0], [2.4, 4.5]], [1, 2, 2, 2, 2, 79], id='fill3_0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.4, 4.5], [3.3000000000000003, 4.5], [4.4, 6.0], [4.4, 6.0], [2.4, 6.0], [2.4, 4.5]], [1, 2, 2, 2, 2, 79], id='fill3_0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.2, 3.0], [8.1, 3.0], [8.1, 4.5], [6.1, 4.5], [6.1, 4.178571428571429], [7.2, 3.0]], [1, 2, 2, 2, 2, 79], id='fill2_2_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.2, 3.0], [8.1, 3.0], [8.1, 4.5], [6.1, 4.5], [6.1, 4.178571428571429], [7.2, 3.0]], [1, 2, 2, 2, 2, 79], id='fill2_2_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.1, 4.17857142857143], [6.1, 4.5], [5.800000000000001, 4.5], [6.1, 4.17857142857143]], [1, 2, 2, 79], id='fill2_1_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.1, 4.17857142857143], [6.1, 4.5], [5.800000000000001, 4.5], [6.1, 4.17857142857143]], [1, 2, 2, 79], id='fill2_1_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.1, 3.0], [2.2, 3.0], [3.3000000000000003, 4.5], [2.1, 4.5], [2.1, 3.0]], [1, 2, 2, 2, 79], id='fill2_0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.1, 3.0], [2.2, 3.0], [3.3000000000000003, 4.5], [2.1, 4.5], [2.1, 3.0]], [1, 2, 2, 2, 79], id='fill2_0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.6, 1.5], [8.8, 1.5], [8.8, 3.0], [7.2, 3.0], [8.6, 1.5]], [1, 2, 2, 2, 79], id='fill1_3_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[8.6, 1.5], [8.8, 1.5], [8.8, 3.0], [7.2, 3.0], [8.6, 1.5]], [1, 2, 2, 2, 79], id='fill1_3_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.8, 1.5], [1.1, 1.5], [2.1999999999999997, 3.0], [0.8, 3.0], [0.8, 1.5]], [1, 2, 2, 2, 79], id='fill1_0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.8, 1.5], [1.1, 1.5], [2.1999999999999997, 3.0], [0.8, 3.0], [0.8, 1.5]], [1, 2, 2, 2, 79], id='fill1_0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[10.0, 0.0], [10.0, 0.0], [10.0, 1.5], [8.6, 1.5], [10.0, 0.0]], [1, 2, 2, 2, 79], id='fill0_4_1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.0], [10.0, 0.0], [10.0, 1.5], [8.6, 1.5], [10.0, 0.0]], [1, 2, 2, 2, 79], id='fill0_4_1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [1.1, 1.5], [0.0, 1.5], [0.0, 0.0]], [1, 2, 2, 79], id='fill0_0_0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.1, 1.5], [0.0, 1.5], [0.0, 0.0]], [1, 2, 2, 79], id='fill0_0_0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('rect0_0', [[0.0, 0.0], [2.0, 0.0], [2.0, 1.5], [0.0, 1.5], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('rect0_1', [[2.0, 0.0], [4.0, 0.0], [4.0, 1.5], [2.0, 1.5], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('rect0_2', [[4.0, 0.0], [6.0, 0.0], [6.0, 1.5], [4.0, 1.5], [4.0, 0.0]], [1, 2, 2, 2, 79]), ('rect0_3', [[6.0, 0.0], [8.0, 0.0], [8.0, 1.5], [6.0, 1.5], [6.0, 0.0]], [1, 2, 2, 2, 79]), ('rect0_4', [[8.0, 0.0], [10.0, 0.0], [10.0, 1.5], [8.0, 1.5], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('rect1_0', [[0.8, 1.5], [2.8, 1.5], [2.8, 3.0], [0.8, 3.0], [0.8, 1.5]], [1, 2, 2, 2, 79]), ('rect1_1', [[2.8, 1.5], [4.8, 1.5], [4.8, 3.0], [2.8, 3.0], [2.8, 1.5]], [1, 2, 2, 2, 79]), ('rect1_2', [[4.8, 1.5], [6.8, 1.5], [6.8, 3.0], [4.8, 3.0], [4.8, 1.5]], [1, 2, 2, 2, 79]), ('rect1_3', [[6.8, 1.5], [8.8, 1.5], [8.8, 3.0], [6.8, 3.0], [6.8, 1.5]], [1, 2, 2, 2, 79]), ('rect2_0', [[2.1, 3.0], [4.1, 3.0], [4.1, 4.5], [2.1, 4.5], [2.1, 3.0]], [1, 2, 2, 2, 79]), ('rect2_1', [[4.1, 3.0], [6.1, 3.0], [6.1, 4.5], [4.1, 4.5], [4.1, 3.0]], [1, 2, 2, 2, 79]), ('rect2_2', [[6.1, 3.0], [8.1, 3.0], [8.1, 4.5], [6.1, 4.5], [6.1, 3.0]], [1, 2, 2, 2, 79]), ('rect3_0', [[2.4, 4.5], [4.4, 4.5], [4.4, 6.0], [2.4, 6.0], [2.4, 4.5]], [1, 2, 2, 2, 79]), ('rect3_1', [[4.4, 4.5], [6.4, 4.5], [6.4, 6.0], [4.4, 6.0], [4.4, 4.5]], [1, 2, 2, 2, 79]), ('whiteTriangle', [[0.0, 0.0], [10.0, 0.0], [4.4, 6.0], [0.0, 0.0]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, -0.7], [10.0, -0.7]], id='width', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -0.7]], id='widthleft')
            c.line([[10.0, 0.0], [10.0, -0.7]], id='widthright')
            c.line([[-1.0, 0.0], [-1.0, 6.0]], id='height', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.4, 0.0], [-1.0, 0.0]], id='heightbottom')
            c.line([[-1.0, 6.0], [4.4, 6.0]], id='heighttop')
            c.text('10 cm', [5.0, -0.7], id='widthtext', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('6 cm', [-1.0, 3.0], id='heighttext', rotation_mode='default', offset_pt=[-25, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane400().draw(sys.argv[1] if len(sys.argv) > 1 else None))
