"""Collected question Plane122; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane122:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'L1': [0.54, 1.82], 'L2': [6.94, 5.82], 'P': [3.48, 6.62],
            'A': [6.142921348314605, 2.359325842696628], 'B': [5.230561797752809, 1.7891011235955059],
            'C': [4.011685393258427, 1.0273033707865171], 'H': [4.811460674157303, 4.489662921348314]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            c.line([self.points['L1'], self.points['L2']], id='axis_l')
            for object_id, points in [('P_dot', [self.points['P']]), ('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id)
            c.text('P', self.points['P'], offset_pt=(0, 16), vertex=True, id='P_label')
            c.text('A', self.points['A'], offset_pt=(9, -15), vertex=True, id='A_label')
            c.text('B', self.points['B'], offset_pt=(-9, -15), vertex=True, id='B_label')
            c.text('C', self.points['C'], offset_pt=(0, -16), vertex=True, id='C_label')
            c.text('l', self.points['L2'], offset_pt=(-13, 8), vertex=True, id='l_label')
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        c.line([[0.54, 1.82], [6.94, 5.82]], id='axis_l', **_kw.get(0, {'linewidth': 2.0}))
        for object_id, points in [('P_dot', [[3.48, 6.62]]), ('A_dot', [[6.142921348314605, 2.359325842696628]]), ('B_dot', [[5.230561797752809, 1.7891011235955059]]), ('C_dot', [[4.011685393258427, 1.0273033707865171]])]:
            c.point(points, id=object_id)
        c.text('P', (3.48, 6.62), id='P_label', fontsize=18.0, fontstyle='italic', offset_pt=(0, 16))
        c.text('A', (6.142921348314605, 2.359325842696628), id='A_label', fontsize=18.0, fontstyle='italic', offset_pt=(9, -15))
        c.text('B', (5.230561797752809, 1.7891011235955059), id='B_label', fontsize=18.0, fontstyle='italic', offset_pt=(-9, -15))
        c.text('C', (4.011685393258427, 1.0273033707865171), id='C_label', fontsize=18.0, fontstyle='italic', offset_pt=(0, -16))
        c.text('l', (6.94, 5.82), id='l_label', fontsize=18.0, fontstyle='italic', offset_pt=(-13, 8))
        c.point([[3.48, 6.62]], zorder=10, s=50, **_kw.get(7, {'facecolors': '#EA580C', 'edgecolors': '#EA580C'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane122_C01.png'
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            self._draw_choices(c, kw={7: {'facecolors': '#2563EB', 'edgecolors': '#2563EB'}})
            c.point([[5.230561797752809, 1.7891011235955059]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.line([[3.48, 6.62], [5.230561797752809, 1.7891011235955059]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane122_C02.png'
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            self._draw_choices(c, kw={7: {'facecolors': '#DC2626', 'edgecolors': '#DC2626'}})
            c.point([[5.230561797752809, 1.7891011235955059]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[3.48, 6.62], [5.230561797752809, 1.7891011235955059]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane122_C03.png'
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            self._draw_choices(c, kw={0: {}})
            c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane122_C04.png'
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            self._draw_choices(c, kw={7: {'facecolors': '#2563EB', 'edgecolors': '#2563EB'}})
            c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane122_C05.png'
        with Canvas(PLANE, xlim=(0.38156223083548646, 7.096678509905254), ylim=(0.49270227713178283, 7.20781855620155)) as c:
            self._draw_choices(c, kw={0: {}})
            c.point([[4.011685393258427, 1.0273033707865171]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[3.48, 6.62], [4.011685393258427, 1.0273033707865171]], zorder=9, color='#EA580C', solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane122')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane122().draw(args.output, variant=args.variant))
