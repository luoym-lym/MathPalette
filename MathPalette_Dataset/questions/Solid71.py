"""Collected question Solid71; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid71:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'A': [0, 0, 0], 'B': [12, 0, 0], 'C': [0, 7, 0], 'T': [0, 0, 12], 'U': [12, 0, 12],
            'V': [0, 7, 12], 'M': [6, 0, 0], 'N': [0, 3.5, 0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408), projection=[[-0.6, 0.6, 0.0], [0.18, 0.3, 0.7]]) as c:
            c.fill(c.project([self.points['T'], self.points['M'], self.points['N']]), facecolor='#E6E6E6', alpha=1, id='cut_fill')
            c.line(c.project([self.points['B'], self.points['C']]), id='edge_BC', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('edge_AB', c.project([self.points['A'], self.points['B']])), ('edge_AC', c.project([self.points['A'], self.points['C']])), ('edge_TU', c.project([self.points['T'], self.points['U']])), ('edge_UV', c.project([self.points['U'], self.points['V']])), ('edge_TV', c.project([self.points['T'], self.points['V']])), ('edge_BU', c.project([self.points['B'], self.points['U']])), ('edge_AT', c.project([self.points['A'], self.points['T']])), ('edge_CV', c.project([self.points['C'], self.points['V']])), ('section_TM', c.project([self.points['T'], self.points['M']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['M'], self.points['N']]), id='section_MN', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['N'], self.points['T']]), id='section_NT', clip_on=False, zorder=3)
            c.point(c.project([self.points['M']]), id='midpoint_M')
            c.point(c.project([self.points['N']]), id='midpoint_N')
            c.text('A', c.project(self.points['A']), offset_pt=(0, -8), vertex=True, va='top', id='label_A')
            return c.save(output_path)

    def _draw_choices(self, c):
        c.path([[0.0, 8.399999999999999], [-3.5999999999999996, 1.08], [2.1, 1.05], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='#E6E6E6', capstyle='butt')
        c.line([[-7.199999999999999, 2.16], [4.2, 2.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-7.199999999999999, 2.16]]), ('edge_AC', [[0.0, 0.0], [4.2, 2.1]]), ('edge_TU', [[0.0, 8.399999999999999], [-7.199999999999999, 10.559999999999999]]), ('edge_UV', [[-7.199999999999999, 10.559999999999999], [4.2, 10.5]]), ('edge_TV', [[0.0, 8.399999999999999], [4.2, 10.5]]), ('edge_BU', [[-7.199999999999999, 2.16], [-7.199999999999999, 10.559999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]]), ('edge_CV', [[4.2, 2.1], [4.2, 10.5]]), ('section_TM', [[0.0, 8.399999999999999], [-3.5999999999999996, 1.08]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08], [2.1, 1.05]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.1, 1.05], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.5999999999999996, 1.08]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.1, 1.05]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', offset_pt=(0, -8))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid71_C01.png'
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408)) as c:
            self._draw_choices(c)
            c.point([[-1.4999999999999996, 10.53]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid71_C02.png'
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408)) as c:
            self._draw_choices(c)
            c.point([[2.1, 9.45]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid71_C03.png'
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408)) as c:
            self._draw_choices(c)
            c.point([[-7.199999999999999, 6.359999999999999]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid71_C04.png'
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408)) as c:
            self._draw_choices(c)
            c.point([[0.0, 4.199999999999999]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid71_C05.png'
        with Canvas(SOLID, xlim=(-7.49184549297819, 4.509142039446911), ylim=(-0.9722550051596937, 11.028732527265408)) as c:
            self._draw_choices(c)
            c.point([[-3.5999999999999996, 9.479999999999999]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.point([[-1.4999999999999996, 10.53]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid71')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Solid71().draw(args.output, variant=args.variant))
