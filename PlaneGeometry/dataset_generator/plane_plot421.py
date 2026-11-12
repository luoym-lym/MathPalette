"""Frozen question Plane421; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane421:

    def __init__(self):
        self.id = 'Plane421'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1844'
        self.question = "A parallelogram contains two identical regular hexagons. The hexagons share a common side, and each has two sides touching the sides of the parallelogram. What fraction of the parallelogram's area is shaded?\nChoices:\nA:$\\frac{2}{3}$\nB:$\\frac{1}{2}$\nC:$\\frac{1}{3}$\nD:$\\frac{1}{4}$\nE:$\\frac{3}{5}$"
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{2}{3}$', 'B': '$\\frac{1}{2}$', 'C': '$\\frac{1}{3}$', 'D': '$\\frac{1}{4}$', 'E': '$\\frac{3}{5}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane421.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.13610219620042008, 5.6361021962004205], ylim=[-1.587064090523762, 4.1851403018770785], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.0, 0.0], [2.5, 0.8660254037844386], [1.5, 0.8660254037844386], [1.0, 1.7320508075688772], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='lowGrey', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [3.0, 0.0], [2.5, 0.8660254037844386], [1.5, 0.8660254037844386], [1.0, 1.7320508075688772], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='lowGrey', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 2.598076211353316], [5.5, 2.598076211353316], [4.5, 0.8660254037844386], [4.0, 1.7320508075688772], [3.0, 1.7320508075688772], [2.5, 2.598076211353316]], [1, 2, 2, 2, 2, 79], id='upGrey', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 2.598076211353316], [5.5, 2.598076211353316], [4.5, 0.8660254037844386], [4.0, 1.7320508075688772], [3.0, 1.7320508075688772], [2.5, 2.598076211353316]], [1, 2, 2, 2, 2, 79], id='upGrey', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('hex1', [[1.0, 1.7320508075688772], [1.5, 2.598076211353316], [2.5, 2.598076211353316], [3.0, 1.7320508075688772], [2.5, 0.8660254037844386], [1.5, 0.8660254037844386], [1.0, 1.7320508075688772]], [1, 2, 2, 2, 2, 2, 79]), ('hex2', [[2.5, 0.8660254037844386], [3.0, 1.7320508075688772], [4.0, 1.7320508075688772], [4.5, 0.8660254037844386], [4.0, 0.0], [3.0, 0.0], [2.5, 0.8660254037844386]], [1, 2, 2, 2, 2, 2, 79]), ('outline', [[0.0, 0.0], [4.0, 0.0], [5.5, 2.598076211353316], [1.5, 2.598076211353316], [0.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane421().draw(sys.argv[1] if len(sys.argv) > 1 else None))
