"""Frozen question Plane279; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane279:

    def __init__(self):
        self.id = 'Plane279'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:839'
        self.question = 'In which shape is exactly one half coloured grey?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane279.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.137020027764734, 17.412928242879904], ylim=[-8.990930852547052, 10.559017418097586], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[1.0, 1.0], [1.0, 1.1755235951100511], [0.9537872013394643, 1.3479921076711214], [0.8660254037844387, 1.5], [0.7782636062294132, 1.6520078923288783], [0.6520078923288785, 1.778263606229413], [0.5000000000000001, 1.8660254037844386], [0.34799210767112176, 1.9537872013394642], [0.1755235951100512, 2.0], [6.123233995736766e-17, 2.0], [-0.17552359511005108, 2.0], [-0.34799210767112143, 1.9537872013394644], [-0.49999999999999983, 1.8660254037844388], [0.0, 1.0], [0.0, 1.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 79], id='A_sector0', facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], capstyle='butt')
            c.path([[-0.49999999999999983, 1.8660254037844388], [-0.6520078923288782, 1.7782636062294133], [-0.7782636062294128, 1.6520078923288786], [-0.8660254037844385, 1.5000000000000004], [-0.9537872013394642, 1.3479921076711219], [-1.0, 1.1755235951100513], [-1.0, 1.0000000000000002], [-1.0, 0.824476404889949], [-0.9537872013394644, 0.6520078923288786], [-0.8660254037844388, 0.5000000000000002], [-0.7782636062294133, 0.3479921076711219], [-0.6520078923288788, 0.2217363937705873], [-0.5000000000000004, 0.13397459621556163], [0.0, 1.0], [0.0, 1.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 79], id='A_sector1', facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.path([[-0.5000000000000004, 0.13397459621556163], [-0.3479921076711221, 0.04621279866053596], [-0.1755235951100514, 0.0], [-1.8369701987210297e-16, 0.0], [0.175523595110051, 0.0], [0.3479921076711209, 0.046212798660535515], [0.49999999999999933, 0.13397459621556096], [0.6520078923288778, 0.2217363937705864], [0.7782636062294127, 0.3479921076711212], [0.8660254037844384, 0.49999999999999956], [0.953787201339464, 0.6520078923288779], [1.0, 0.8244764048899486], [1.0, 0.9999999999999998], [0.0, 1.0], [0.0, 1.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 79], id='A_sector2', facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.path([[3.0, 0.0], [5.0, 0.0], [4.0, 2.0], [3.0, 0.0]], [1, 2, 2, 79], id='B_triangle', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [4.0, 2.0], [4.0, 0.0]], [1, 2, 2, 79], id='B_gray_half', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.0, 0.0], [5.0, 0.0], [4.0, 2.0], [4.0, 0.0]], [1, 2, 2, 79], id='B_gray_half', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='C00', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='C00', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='C01', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='C01', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='C10', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='C10', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='C11', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='C11', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[11.0, 0.0], [13.0, 0.0], [13.0, 2.0], [11.0, 2.0], [11.0, 0.0]], [1, 2, 2, 2, 79], id='D_square', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[11.0, 2.0], [13.0, 2.0], [12.0, 1.0], [11.0, 2.0]], [1, 2, 2, 79], id='D_gray_quarter', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[11.0, 2.0], [13.0, 2.0], [12.0, 1.0], [11.0, 2.0]], [1, 2, 2, 79], id='D_gray_quarter', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[11.0, 0.0], [13.0, 2.0]], id='D_diag1')
            c.line([[11.0, 2.0], [13.0, 0.0]], id='D_diag2')
            c.path([[16.0, 1.0], [16.0, 2.0], [15.048943483704846, 1.3090169943749475], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 1.0], [16.0, 2.0], [15.048943483704846, 1.3090169943749475], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 1.0], [15.048943483704846, 1.3090169943749475], [15.412214747707527, 0.19098300562505266], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 1.0], [15.048943483704846, 1.3090169943749475], [15.412214747707527, 0.19098300562505266], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 1.0], [15.412214747707527, 0.19098300562505266], [16.587785252292473, 0.19098300562505244], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 1.0], [15.412214747707527, 0.19098300562505266], [16.587785252292473, 0.19098300562505244], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 1.0], [16.587785252292473, 0.19098300562505244], [16.951056516295154, 1.3090169943749472], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 1.0], [16.587785252292473, 0.19098300562505244], [16.951056516295154, 1.3090169943749472], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[16.0, 1.0], [16.951056516295154, 1.3090169943749472], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle4', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 1.0], [16.951056516295154, 1.3090169943749472], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 79], id='E_triangle4', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', [-1.3, -0.2]), ('label1', '(B)', [2.7, -0.2]), ('label2', '(C)', [6.7, -0.2]), ('label3', '(D)', [10.7, -0.2]), ('label4', '(E)', [14.7, -0.2])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane279().draw(sys.argv[1] if len(sys.argv) > 1 else None))
