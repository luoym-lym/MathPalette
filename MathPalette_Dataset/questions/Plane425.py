"""Collected question Plane425; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane425:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane425'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1871'
        self.question = 'One of the line segments shown on the grid is the image produced by a rotation of the other line segment. Which of the points $T, U, V$, $W$ could be the centre of such a rotation?\nChoices:\nA:only $T$\nB:only $U$\nC:either of $U$ and $W$\nD:any of $U, V$ and $W$\nE:any of $T, U, V$ and $W$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'only $T$', 'B': 'only $U$', 'C': 'either of $U$ and $W$', 'D': 'any of $U, V$ and $W$', 'E': 'any of $T, U, V$ and $W$'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.14831072575800563, 6.159906313357347], ylim=[-0.8104426647939471, 5.497774374321405], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('o1', [[1.0, 0.2], [1.0, 4.4]]), ('o2', [[2.0, 0.2], [2.0, 4.4]]), ('o3', [[3.0, 0.2], [3.0, 4.4]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
            c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
            for object_id, points in [('o15', [[3.0, 4.0]]), ('o16', [[2.0, 3.0]]), ('o17', [[1.0, 1.0]]), ('o18', [[2.0, 1.0]])]:
                c.point(points, id=object_id)
            c.text('W', [3.0, 4.0], id='label_X0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[31.541044653535405, 31.54104465353544], annotation_clip=None)
            c.text('V', [2.0, 3.0], id='label_Y1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[27.598414071843493, 31.541044653535405], annotation_clip=None)
            c.text('T', [1.0, 1.0], id='label_Z2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-39.42630581691927, -43.3689363986112], annotation_clip=None)
            c.text('U', [2.0, 1.0], id='label_T3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[31.541044653535405, -43.3689363986112], annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane425_C01.png'
        with Canvas(PLANE, xlim=(-0.14831072575800563, 6.159906313357347), ylim=(-0.8104426647939471, 5.497774374321405), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('o1', [[1.0, 0.2], [1.0, 4.4]]), ('o2', [[2.0, 0.2], [2.0, 4.4]]), ('o3', [[3.0, 0.2], [3.0, 4.4]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
            c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
            for object_id, points in [('o15', [[3.0, 4.0]]), ('o16', [[2.0, 3.0]]), ('o17', [[1.0, 1.0]]), ('o18', [[2.0, 1.0]])]:
                c.point(points, id=object_id)
            c.text('W', (3.0, 4.0), id='label_X0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, 31.54104465353544), annotation_clip=None)
            c.text('V', (2.0, 3.0), id='label_Y1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(27.598414071843493, 31.541044653535405), annotation_clip=None)
            c.text('T', (1.0, 1.0), id='label_Z2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-39.42630581691927, -43.3689363986112), annotation_clip=None)
            c.text('U', (2.0, 1.0), id='label_T3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, -43.3689363986112), annotation_clip=None)
            c.line([[1, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane425_C02.png'
        with Canvas(PLANE, xlim=(-0.14831072575800563, 6.159906313357347), ylim=(-0.8104426647939471, 5.497774374321405), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('o1', [[1.0, 0.2], [1.0, 4.4]]), ('o2', [[2.0, 0.2], [2.0, 4.4]]), ('o3', [[3.0, 0.2], [3.0, 4.4]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
            c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
            for object_id, points in [('o15', [[3.0, 4.0]]), ('o16', [[2.0, 3.0]]), ('o17', [[1.0, 1.0]]), ('o18', [[2.0, 1.0]])]:
                c.point(points, id=object_id)
            c.text('W', (3.0, 4.0), id='label_X0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, 31.54104465353544), annotation_clip=None)
            c.text('V', (2.0, 3.0), id='label_Y1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(27.598414071843493, 31.541044653535405), annotation_clip=None)
            c.text('T', (1.0, 1.0), id='label_Z2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-39.42630581691927, -43.3689363986112), annotation_clip=None)
            c.text('U', (2.0, 1.0), id='label_T3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, -43.3689363986112), annotation_clip=None)
            c.line([[1, 4], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[5, 2], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane425')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane425().draw(args.output, variant=args.variant))
