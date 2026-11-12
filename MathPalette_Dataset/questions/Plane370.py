"""Collected question Plane370; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane370:
    variants = ('C01', 'C02', 'C03')

    def __init__(self):
        self.id = 'Plane370'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1390'
        self.question = 'Each small square in the diagram has side length 1. What is the length of the shortest path from "Start" to "Ziel" using only the sides and diagonals of the squares?\nChoices:\nA:$2 \\sqrt{5}$\nB:$\\sqrt{10}+\\sqrt{2}$\nC:$2+2 \\sqrt{2}$\nD:$4 \\sqrt{2}$\nE:6'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$2 \\sqrt{5}$', 'B': '$\\sqrt{10}+\\sqrt{2}$', 'C': '$2+2 \\sqrt{2}$', 'D': '$4 \\sqrt{2}$', 'E': '6'}
        self.query = self.question
        self.points = {'gva0': [0, 0],
         'gvb0': [0, 2],
         'gva1': [1, 0],
         'gvb1': [1, 2],
         'gva2': [2, 0],
         'gvb2': [2, 2],
         'gva3': [3, 0],
         'gvb3': [3, 2],
         'gva4': [4, 0],
         'gvb4': [4, 2],
         'gha0': [0, 0],
         'ghb0': [4, 0],
         'gha1': [0, 1],
         'ghb1': [4, 1],
         'gha2': [0, 2],
         'ghb2': [4, 2],
         'Start': [0, 2],
         'Ziel': [4, 0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.12691745666567344, 4.133582239192938], ylim=[-1.1269223016330092, 3.1335773942256018]) as c:
            for object_id, points in [('gv0', [self.points['gva0'], self.points['gvb0']]), ('gv1', [self.points['gva1'], self.points['gvb1']]), ('gv2', [self.points['gva2'], self.points['gvb2']]), ('gv3', [self.points['gva3'], self.points['gvb3']]), ('gv4', [self.points['gva4'], self.points['gvb4']]), ('gh0', [self.points['gha0'], self.points['ghb0']]), ('gh1', [self.points['gha1'], self.points['ghb1']]), ('gh2', [self.points['gha2'], self.points['ghb2']])]:
                c.line(points, id=object_id)
            c.point([self.points['Start']], filled=True, id='start')
            c.point([self.points['Ziel']], filled=True, id='end')
            c.text('Start', self.points['Start'], offset_pt=[17, 18], vertex=False, id='startname')
            c.text('Ziel', self.points['Ziel'], offset_pt=[-10, -20], vertex=False, id='zielname')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane370_C01.png'
        with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 2.0]], id='start')
            c.point([[4.0, 0.0]], id='end')
            c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
            c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
            c.line([[0, 2], [4, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane370_C02.png'
        with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 2.0]], id='start')
            c.point([[4.0, 0.0]], id='end')
            c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
            c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
            c.line([[0.0, 2.0], [4.0, 0.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0.0, 2.0], [1.0, 1.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane370_C03.png'
        with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id)
            c.point([[0.0, 2.0]], id='start')
            c.point([[4.0, 0.0]], id='end')
            c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
            c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
            c.line([[0, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[2, 1], [4, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane370')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane370().draw(args.output, variant=args.variant))
