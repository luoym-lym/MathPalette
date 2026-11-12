"""Collected question Plane383; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane383:
    variants = ('C01', 'C02', 'C03')

    def __init__(self):
        self.id = 'Plane383'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1541'
        self.question = 'The robot in the diagram has been programmed to move in a straight line and, if it meets a wall (shown by bold lines), to turn right by $90^{\\circ}$ and then to continue straight on. If it cannot go straight or turn right it will stop. What will happen to this robot?\nChoices:\nA:It will stop at $\\mathrm{P} 2$.\nB:It will stop at P1.\nC:It will stop at $\\mathrm{T} 1$.\nD:It will stop at $S 1$.\nE:It will never stop.'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'It will stop at $\\mathrm{P} 2$.',
         'B': 'It will stop at P1.',
         'C': 'It will stop at $\\mathrm{T} 1$.',
         'D': 'It will stop at $S 1$.',
         'E': 'It will never stop.'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-2.1562432139387218, 5.748376138404537], ylim=[-2.277507572611529, 5.62711177973173], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('gridv1', [[1.0, 0.0], [1.0, 4.0]]), ('gridv2', [[2.0, 0.0], [2.0, 4.0]]), ('gridv3', [[3.0, 0.0], [3.0, 4.0]]), ('gridv4', [[4.0, 0.0], [4.0, 4.0]]), ('gridh1', [[0.0, 1.0], [5.0, 1.0]]), ('gridh2', [[0.0, 2.0], [5.0, 2.0]]), ('gridh3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('wall0', [[0.0, 0.0], [5.0, 0.0]]), ('wall1', [[5.0, 0.0], [5.0, 4.0]]), ('wall2', [[5.0, 4.0], [0.0, 4.0]]), ('wall3', [[0.0, 4.0], [0.0, 2.0]]), ('wall4', [[0.0, 0.0], [0.0, 1.0]]), ('wall5', [[1.0, 2.0], [1.0, 3.0]]), ('wall6', [[2.0, 1.0], [2.0, 2.0]]), ('wall7', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('arrow', [[-1.1, 1.5], [-0.15, 1.5]]), ('head1', [[-0.4, 1.65], [-0.15, 1.5]]), ('head2', [[-0.4, 1.35], [-0.15, 1.5]])]:
                c.line(points, id=object_id)
            c.circle([-1.6, 1.5], 0.18, id='robotcircle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('ray0', [[-1.4000000000000001, 1.5], [-1.28, 1.5]]), ('ray1', [[-1.4585786437626906, 1.6414213562373094], [-1.3737258300203048, 1.7262741699796953]]), ('ray2', [[-1.6, 1.7], [-1.6, 1.82]]), ('ray3', [[-1.7414213562373095, 1.6414213562373094], [-1.8262741699796954, 1.7262741699796953]]), ('ray4', [[-1.8, 1.5], [-1.9200000000000002, 1.5]]), ('ray5', [[-1.7414213562373095, 1.3585786437626906], [-1.8262741699796954, 1.2737258300203047]]), ('ray6', [[-1.6, 1.3], [-1.6, 1.18]]), ('ray7', [[-1.4585786437626906, 1.3585786437626906], [-1.373725830020305, 1.2737258300203047]])]:
                c.line(points, id=object_id)
            c.path([[-1.9700000000000002, 1.13], [-1.23, 1.13], [-1.23, 1.87], [-1.9700000000000002, 1.87], [-1.9700000000000002, 1.13]], [1, 2, 2, 2, 79], id='roboticon', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, text, anchor in [('labelP', 'P', [0.5, -0.55]), ('labelQ', 'Q', [1.5, -0.55]), ('labelR', 'R', [2.5, -0.55]), ('labelS', 'S', [3.5, -0.55]), ('labelT', 'T', [4.5, -0.55]), ('row0', '1', [5.5, 0.5]), ('row1', '2', [5.5, 1.5]), ('row2', '3', [5.5, 2.5]), ('row3', '4', [5.5, 3.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane383_C01.png'
        with Canvas(PLANE, xlim=(-2.1562432139387218, 5.748376138404537), ylim=(-2.277507572611529, 5.62711177973173), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gridv1', [[1.0, 0.0], [1.0, 4.0]]), ('gridv2', [[2.0, 0.0], [2.0, 4.0]]), ('gridv3', [[3.0, 0.0], [3.0, 4.0]]), ('gridv4', [[4.0, 0.0], [4.0, 4.0]]), ('gridh1', [[0.0, 1.0], [5.0, 1.0]]), ('gridh2', [[0.0, 2.0], [5.0, 2.0]]), ('gridh3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('wall0', [[0.0, 0.0], [5.0, 0.0]]), ('wall1', [[5.0, 0.0], [5.0, 4.0]]), ('wall2', [[5.0, 4.0], [0.0, 4.0]]), ('wall3', [[0.0, 4.0], [0.0, 2.0]]), ('wall4', [[0.0, 0.0], [0.0, 1.0]]), ('wall5', [[1.0, 2.0], [1.0, 3.0]]), ('wall6', [[2.0, 1.0], [2.0, 2.0]]), ('wall7', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('arrow', [[-1.1, 1.5], [-0.15, 1.5]]), ('head1', [[-0.4, 1.65], [-0.15, 1.5]]), ('head2', [[-0.4, 1.35], [-0.15, 1.5]])]:
                c.line(points, id=object_id)
            c.circle([-1.6, 1.5], 0.18, id='robotcircle', fill=False)
            for object_id, points in [('ray0', [[-1.4000000000000001, 1.5], [-1.28, 1.5]]), ('ray1', [[-1.4585786437626906, 1.6414213562373094], [-1.3737258300203048, 1.7262741699796953]]), ('ray2', [[-1.6, 1.7], [-1.6, 1.82]]), ('ray3', [[-1.7414213562373095, 1.6414213562373094], [-1.8262741699796954, 1.7262741699796953]]), ('ray4', [[-1.8, 1.5], [-1.9200000000000002, 1.5]]), ('ray5', [[-1.7414213562373095, 1.3585786437626906], [-1.8262741699796954, 1.2737258300203047]]), ('ray6', [[-1.6, 1.3], [-1.6, 1.18]]), ('ray7', [[-1.4585786437626906, 1.3585786437626906], [-1.373725830020305, 1.2737258300203047]])]:
                c.line(points, id=object_id)
            c.path([[-1.9700000000000002, 1.13], [-1.23, 1.13], [-1.23, 1.87], [-1.9700000000000002, 1.87], [-1.9700000000000002, 1.13]], [1, 2, 2, 2, 79], id='roboticon', capstyle='butt')
            for object_id, text, anchor in [('labelP', 'P', (0.5, -0.55)), ('labelQ', 'Q', (1.5, -0.55)), ('labelR', 'R', (2.5, -0.55)), ('labelS', 'S', (3.5, -0.55)), ('labelT', 'T', (4.5, -0.55)), ('row0', '1', (5.5, 0.5)), ('row1', '2', (5.5, 1.5)), ('row2', '3', (5.5, 2.5)), ('row3', '4', (5.5, 3.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[4.468073208174102, 3.515338472365516], [4.47614573610746, 0.4316328018231088]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[4.47614573610746, 0.4881404973566088]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane383_C02.png'
        with Canvas(PLANE, xlim=(-2.1562432139387218, 5.748376138404537), ylim=(-2.277507572611529, 5.62711177973173), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gridv1', [[1.0, 0.0], [1.0, 4.0]]), ('gridv2', [[2.0, 0.0], [2.0, 4.0]]), ('gridv3', [[3.0, 0.0], [3.0, 4.0]]), ('gridv4', [[4.0, 0.0], [4.0, 4.0]]), ('gridh1', [[0.0, 1.0], [5.0, 1.0]]), ('gridh2', [[0.0, 2.0], [5.0, 2.0]]), ('gridh3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('wall0', [[0.0, 0.0], [5.0, 0.0]]), ('wall1', [[5.0, 0.0], [5.0, 4.0]]), ('wall2', [[5.0, 4.0], [0.0, 4.0]]), ('wall3', [[0.0, 4.0], [0.0, 2.0]]), ('wall4', [[0.0, 0.0], [0.0, 1.0]]), ('wall5', [[1.0, 2.0], [1.0, 3.0]]), ('wall6', [[2.0, 1.0], [2.0, 2.0]]), ('wall7', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('arrow', [[-1.1, 1.5], [-0.15, 1.5]]), ('head1', [[-0.4, 1.65], [-0.15, 1.5]]), ('head2', [[-0.4, 1.35], [-0.15, 1.5]])]:
                c.line(points, id=object_id)
            c.circle([-1.6, 1.5], 0.18, id='robotcircle', fill=False)
            for object_id, points in [('ray0', [[-1.4000000000000001, 1.5], [-1.28, 1.5]]), ('ray1', [[-1.4585786437626906, 1.6414213562373094], [-1.3737258300203048, 1.7262741699796953]]), ('ray2', [[-1.6, 1.7], [-1.6, 1.82]]), ('ray3', [[-1.7414213562373095, 1.6414213562373094], [-1.8262741699796954, 1.7262741699796953]]), ('ray4', [[-1.8, 1.5], [-1.9200000000000002, 1.5]]), ('ray5', [[-1.7414213562373095, 1.3585786437626906], [-1.8262741699796954, 1.2737258300203047]]), ('ray6', [[-1.6, 1.3], [-1.6, 1.18]]), ('ray7', [[-1.4585786437626906, 1.3585786437626906], [-1.373725830020305, 1.2737258300203047]])]:
                c.line(points, id=object_id)
            c.path([[-1.9700000000000002, 1.13], [-1.23, 1.13], [-1.23, 1.87], [-1.9700000000000002, 1.87], [-1.9700000000000002, 1.13]], [1, 2, 2, 2, 79], id='roboticon', capstyle='butt')
            for object_id, text, anchor in [('labelP', 'P', (0.5, -0.55)), ('labelQ', 'Q', (1.5, -0.55)), ('labelR', 'R', (2.5, -0.55)), ('labelS', 'S', (3.5, -0.55)), ('labelT', 'T', (4.5, -0.55)), ('row0', '1', (5.5, 0.5)), ('row1', '2', (5.5, 1.5)), ('row2', '3', (5.5, 2.5)), ('row3', '4', (5.5, 3.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[2.5, 0.49], [0.5, 0.49]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[0.5, 0.49]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane383_C03.png'
        with Canvas(PLANE, xlim=(-2.1562432139387218, 5.748376138404537), ylim=(-2.277507572611529, 5.62711177973173), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gridv1', [[1.0, 0.0], [1.0, 4.0]]), ('gridv2', [[2.0, 0.0], [2.0, 4.0]]), ('gridv3', [[3.0, 0.0], [3.0, 4.0]]), ('gridv4', [[4.0, 0.0], [4.0, 4.0]]), ('gridh1', [[0.0, 1.0], [5.0, 1.0]]), ('gridh2', [[0.0, 2.0], [5.0, 2.0]]), ('gridh3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('wall0', [[0.0, 0.0], [5.0, 0.0]]), ('wall1', [[5.0, 0.0], [5.0, 4.0]]), ('wall2', [[5.0, 4.0], [0.0, 4.0]]), ('wall3', [[0.0, 4.0], [0.0, 2.0]]), ('wall4', [[0.0, 0.0], [0.0, 1.0]]), ('wall5', [[1.0, 2.0], [1.0, 3.0]]), ('wall6', [[2.0, 1.0], [2.0, 2.0]]), ('wall7', [[3.0, 0.0], [3.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('arrow', [[-1.1, 1.5], [-0.15, 1.5]]), ('head1', [[-0.4, 1.65], [-0.15, 1.5]]), ('head2', [[-0.4, 1.35], [-0.15, 1.5]])]:
                c.line(points, id=object_id)
            c.circle([-1.6, 1.5], 0.18, id='robotcircle', fill=False)
            for object_id, points in [('ray0', [[-1.4000000000000001, 1.5], [-1.28, 1.5]]), ('ray1', [[-1.4585786437626906, 1.6414213562373094], [-1.3737258300203048, 1.7262741699796953]]), ('ray2', [[-1.6, 1.7], [-1.6, 1.82]]), ('ray3', [[-1.7414213562373095, 1.6414213562373094], [-1.8262741699796954, 1.7262741699796953]]), ('ray4', [[-1.8, 1.5], [-1.9200000000000002, 1.5]]), ('ray5', [[-1.7414213562373095, 1.3585786437626906], [-1.8262741699796954, 1.2737258300203047]]), ('ray6', [[-1.6, 1.3], [-1.6, 1.18]]), ('ray7', [[-1.4585786437626906, 1.3585786437626906], [-1.373725830020305, 1.2737258300203047]])]:
                c.line(points, id=object_id)
            c.path([[-1.9700000000000002, 1.13], [-1.23, 1.13], [-1.23, 1.87], [-1.9700000000000002, 1.87], [-1.9700000000000002, 1.13]], [1, 2, 2, 2, 79], id='roboticon', capstyle='butt')
            for object_id, text, anchor in [('labelP', 'P', (0.5, -0.55)), ('labelQ', 'Q', (1.5, -0.55)), ('labelR', 'R', (2.5, -0.55)), ('labelS', 'S', (3.5, -0.55)), ('labelT', 'T', (4.5, -0.55)), ('row0', '1', (5.5, 0.5)), ('row1', '2', (5.5, 1.5)), ('row2', '3', (5.5, 2.5)), ('row3', '4', (5.5, 3.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[1.2, 1.35], [1.2, 0.45]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[1.2, 0.45], [0.5, 0.45]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[0.5, 0.45]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane383')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane383().draw(args.output, variant=args.variant))
