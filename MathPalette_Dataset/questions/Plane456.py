"""Collected question Plane456; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane456:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

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

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
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
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane456_C01.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outerI', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='outerII', capstyle='butt')
            c.path([[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='outerIII', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 1], [8, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane456_C02.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane456_C03.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane456_C04.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.point([[7.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.point([[7.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane456_C05.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
            c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
            c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
            c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
            c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
            c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
            c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
            for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane456')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane456().draw(args.output, variant=args.variant))
