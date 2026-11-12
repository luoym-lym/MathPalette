"""Frozen question Plane456; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane456:

    def __init__(self):
        self.id = 'Plane456'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2572'
        self.question = 'Each of the three large squares shown below is the same size.  Segments that intersect the sides of the squares intersect at the midpoints of the sides.  How do the shaded areas of these squares compare?\n\nChoices:\nA:$\\text{The shaded areas in all three are equal.}$\nB:$\\text{Only the shaded areas of }I\\text{ and }II\\text{ are equal.}$\nC:$\\text{Only the shaded areas of }I\\text{ and }III\\text{ are equal.}$\nD:$\\text{Only the shaded areas of }II\\text{ and }III\\text{ are equal.}$\nE:$\\text{The shaded areas of }I, II\\text{ and }III\\text{ are all different.}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\text{The shaded areas in all three are equal.}$',
         'B': '$\\text{Only the shaded areas of }I\\text{ and }II\\text{ are equal.}$',
         'C': '$\\text{Only the shaded areas of }I\\text{ and }III\\text{ are equal.}$',
         'D': '$\\text{Only the shaded areas of }II\\text{ and }III\\text{ are equal.}$',
         'E': '$\\text{The shaded areas of }I, II\\text{ and }III\\text{ are all different.}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane456.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1982668529167313, 8.211586609172755], ylim=[-3.026694478975208, 5.383158983114279], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', [1.0, 2.25]), ('labelII', 'II', [4.0, 2.25]), ('labelIII', 'III', [7.0, 2.25])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane456().draw(sys.argv[1] if len(sys.argv) > 1 else None))
