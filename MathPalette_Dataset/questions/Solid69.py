"""Collected question Solid69; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid69:
    variants = ('C01',)

    def __init__(self):
        self.points = {
            'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [0, 8, 0], 'D': [0, 0, 18], 'M': [0, 4, 0], 'N': [0, 0, 9],
            'P': [6, 0, 9], 'Q': [6, 4, 0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-5.23008677450906, 4.230086774509061), ylim=(-0.9288456473620674, 8.531327901656054), projection=[[0.0, -0.625, 0.2222222222222222], [0.6666666666666666, 0.375, 0.07500000000000001]]) as c:
            c.fill(c.project([self.points['M'], self.points['N'], self.points['P'], self.points['Q']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            for object_id, points in [('edge_BC', c.project([self.points['B'], self.points['C']])), ('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_BD', c.project([self.points['B'], self.points['D']])), ('edge_AD', c.project([self.points['A'], self.points['D']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['C'], self.points['D']]), id='edge_CD', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['P']]), id='section_NP', clip_on=False, zorder=3)
            c.line(c.project([self.points['P'], self.points['Q']]), id='section_PQ', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['Q'], self.points['M']]), id='section_QM', clip_on=False, zorder=3)
            for object_id, points in [('midpoint_M', c.project([self.points['M']])), ('midpoint_N', c.project([self.points['N']])), ('midpoint_P', c.project([self.points['P']])), ('midpoint_Q', c.project([self.points['Q']]))]:
                c.point(points, id=object_id)
            c.text('A', c.project(self.points['A']), offset_pt=(0, -8), vertex=True, va='top', id='label_A')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid69_C01.png'
        with Canvas(SOLID, xlim=(-5.23008677450906, 4.230086774509061), ylim=(-0.9288456473620674, 8.531327901656054)) as c:
            c.path([[-2.5, 1.5], [2.0, 0.675], [2.0, 4.675], [-2.5, 5.5], [-2.5, 1.5]], [1, 2, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='#E6E6E6', capstyle='butt')
            for object_id, points in [('edge_BC', [[0.0, 8.0], [-5.0, 3.0]]), ('edge_AB', [[0.0, 0.0], [0.0, 8.0]]), ('edge_AC', [[0.0, 0.0], [-5.0, 3.0]]), ('edge_BD', [[0.0, 8.0], [4.0, 1.35]]), ('edge_AD', [[0.0, 0.0], [4.0, 1.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-5.0, 3.0], [4.0, 1.35]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-2.5, 1.5], [2.0, 0.675]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[2.0, 0.675], [2.0, 4.675]], id='section_NP', zorder=3, clip_on=False)
            c.line([[2.0, 4.675], [-2.5, 5.5]], id='section_PQ', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[-2.5, 5.5], [-2.5, 1.5]], id='section_QM', zorder=3, clip_on=False)
            c.line([[-2.5, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[2.0, 0.675]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[2.0, 4.675]], id='midpoint_P', zorder=4, color=(0.17254901960784313, 0.6274509803921569, 0.17254901960784313), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.line([[-2.5, 5.5]], id='midpoint_Q', zorder=4, color=(0.8392156862745098, 0.15294117647058825, 0.1568627450980392), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', offset_pt=(0, -8))
            c.point([[0.03136187213643371, 3.7142910026155764]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid69')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid69().draw(args.output, variant=args.variant))
