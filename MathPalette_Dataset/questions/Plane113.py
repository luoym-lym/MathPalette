"""Collected question Plane113; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane113:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.id = 'Plane113'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:overlapping_rectangles'
        self.question = 'Count the intersection points in the figure.'
        self.answer = 6
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'rectangle_a_v0': [-2.4000000000000004, -1.15],
         'rectangle_a_v1': [2.0, -1.15],
         'rectangle_a_v2': [2.0, 1.25],
         'rectangle_a_v3': [-2.4000000000000004, 1.25],
         'rectangle_b_v0': [0.06359541457745188, -2.083568733392411],
         'rectangle_b_v1': [2.4381300838154445, -0.5997947935394372],
         'rectangle_b_v2': [0.6364045854225482, 2.2835687333924106],
         'rectangle_b_v3': [-1.7381300838154448, 0.7997947935394372],
         'crossing_1': [-1.0176511467625504, 1.25],
         'crossing_2': [-0.5197630748202755, -1.15],
         'crossing_3': [1.2822500100112082, 1.25],
         'crossing_4': [1.5576176938584463, -1.15],
         'crossing_5': [2.0, -0.8735688550651733],
         'crossing_6': [2.0, 0.10135990780206794]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-2.512514653111988, 2.550644736927432], ylim=[-2.4315796950197104, 2.6315796950197097]) as c:
            c.path([self.points['rectangle_a_v0'], self.points['rectangle_a_v1'], self.points['rectangle_a_v2'], self.points['rectangle_a_v3'], self.points['rectangle_a_v0']], [1, 2, 2, 2, 79], id='rectangle_a')
            c.path([self.points['rectangle_b_v0'], self.points['rectangle_b_v1'], self.points['rectangle_b_v2'], self.points['rectangle_b_v3'], self.points['rectangle_b_v0']], [1, 2, 2, 2, 79], id='rectangle_b')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane113_C01.png'
        with Canvas(PLANE, xlim=(-2.512514653111988, 2.550644736927432), ylim=(-2.4315796950197104, 2.6315796950197097), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-2.4000000000000004, -1.15], [2.0, -1.15], [2.0, 1.25], [-2.4000000000000004, 1.25], [-2.4000000000000004, -1.15]], [1, 2, 2, 2, 79], id='rectangle_a', capstyle='butt')
            c.path([[0.06359541457745188, -2.083568733392411], [2.4381300838154445, -0.5997947935394372], [0.6364045854225482, 2.2835687333924106], [-1.7381300838154448, 0.7997947935394372], [0.06359541457745188, -2.083568733392411]], [1, 2, 2, 2, 79], id='rectangle_b', capstyle='butt')
            for object_id, points in [(None, [[-1.0357598310171574, 1.2478976558300148]]), (None, [[1.2807183212884596, 1.2582390761528075]]), (None, [[2.009788454045361, 0.10517071016139523]]), (None, [[1.797789337428107, -0.9961905542160516]]), (None, [[-0.5186888148775108, -1.140970438735153]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane113_C02.png'
        with Canvas(PLANE, xlim=(-2.512514653111988, 2.550644736927432), ylim=(-2.4315796950197104, 2.6315796950197097), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-2.4000000000000004, -1.15], [2.0, -1.15], [2.0, 1.25], [-2.4000000000000004, 1.25], [-2.4000000000000004, -1.15]], [1, 2, 2, 2, 79], id='rectangle_a', capstyle='butt')
            c.path([[0.06359541457745188, -2.083568733392411], [2.4381300838154445, -0.5997947935394372], [0.6364045854225482, 2.2835687333924106], [-1.7381300838154448, 0.7997947935394372], [0.06359541457745188, -2.083568733392411]], [1, 2, 2, 2, 79], id='rectangle_b', capstyle='butt')
            for object_id, points in [(None, [[-1.020247700532968, 1.2582390761528075]]), (None, [[1.2858890314498566, 1.2478976558300148]]), (None, [[1.9942763235611722, 0.0999999999999992]]), (None, [[2.0046177438839643, -0.8669228001811402]]), (None, [[-0.49283526407052847, -1.156482569219342]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane113_C03.png'
        with Canvas(PLANE, xlim=(-2.512514653111988, 2.550644736927432), ylim=(-2.4315796950197104, 2.6315796950197097), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-2.4000000000000004, -1.15], [2.0, -1.15], [2.0, 1.25], [-2.4000000000000004, 1.25], [-2.4000000000000004, -1.15]], [1, 2, 2, 2, 79], id='rectangle_a', capstyle='butt')
            c.path([[0.06359541457745188, -2.083568733392411], [2.4381300838154445, -0.5997947935394372], [0.6364045854225482, 2.2835687333924106], [-1.7381300838154448, 0.7997947935394372], [0.06359541457745188, -2.083568733392411]], [1, 2, 2, 2, 79], id='rectangle_b', capstyle='butt')
            for object_id, points in [(None, [[2.0, -1.15]]), (None, [[1.9994470337225692, 0.11034142032279215]]), (None, [[1.5547659598424723, -1.1513118590579468]]), (None, [[1.9994470337225692, -0.8876056408267265]]), (None, [[1.2962304517726495, 1.2685804964756004]]), (None, [[-1.0047355700487786, 1.2737512066369971]]), (None, [[-0.5290302352003033, -1.13062901841236]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane113_C04.png'
        with Canvas(PLANE, xlim=(-2.512514653111988, 2.550644736927432), ylim=(-2.4315796950197104, 2.6315796950197097), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-2.4000000000000004, -1.15], [2.0, -1.15], [2.0, 1.25], [-2.4000000000000004, 1.25], [-2.4000000000000004, -1.15]], [1, 2, 2, 2, 79], id='rectangle_a', capstyle='butt')
            c.path([[0.06359541457745188, -2.083568733392411], [2.4381300838154445, -0.5997947935394372], [0.6364045854225482, 2.2835687333924106], [-1.7381300838154448, 0.7997947935394372], [0.06359541457745188, -2.083568733392411]], [1, 2, 2, 2, 79], id='rectangle_b', capstyle='butt')
            for object_id, points in [(None, [[-0.9995648598873821, 1.263409786314204]]), (None, [[1.2910597416112526, 1.2582390761528075]]), (None, [[2.020129874368154, 0.11034142032279215]]), (None, [[1.9787641930769824, -0.8669228001811402]]), (None, [[1.5289124090354904, -1.1513118590579468]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane113_C05.png'
        with Canvas(PLANE, xlim=(-2.512514653111988, 2.550644736927432), ylim=(-2.4315796950197104, 2.6315796950197097), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-2.4000000000000004, -1.15], [2.0, -1.15], [2.0, 1.25], [-2.4000000000000004, 1.25], [-2.4000000000000004, -1.15]], [1, 2, 2, 2, 79], id='rectangle_a', capstyle='butt')
            c.path([[0.06359541457745188, -2.083568733392411], [2.4381300838154445, -0.5997947935394372], [0.6364045854225482, 2.2835687333924106], [-1.7381300838154448, 0.7997947935394372], [0.06359541457745188, -2.083568733392411]], [1, 2, 2, 2, 79], id='rectangle_b', capstyle='butt')
            for object_id, points in [(None, [[0.6364045854225482, 2.2835687333924106]]), (None, [[-0.5290302352003033, -1.1461411488965498]]), (None, [[1.5082295683899036, -1.1719946997035318]]), (None, [[2.0046177438839643, -0.8772642205039332]]), (None, [[2.0046177438839643, 0.11551213048418862]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane113')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane113().draw(args.output, variant=args.variant))
