"""Collected question Solid73; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid73:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self.points = {
            'T0': [0.0, 1.5, 0.0], 'T1': [1.0, 1.5, 0.0], 'T2': [2.0, 1.5, 0.0], 'T3': [3.0, 1.5, 0.0],
            'B0': [0.0, 0.0, 0.0], 'B1': [1.0, 0.0, 0.0], 'B2': [2.0, 0.0, 0.0], 'B3': [3.0, 0.0, 0.0],
            'P': [0.5, 2.3660254037844384, 0.0], 'Q': [2.5, -0.8660254037844386, 0.0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487), projection=[[1, 0, 0], [0, 1, 0]]) as c:
            for object_id, points in [('net_edge_B0_B1', c.project([self.points['B0'], self.points['B1']])), ('net_edge_B1_T1', c.project([self.points['B1'], self.points['T1']])), ('net_edge_T0_T1', c.project([self.points['T0'], self.points['T1']])), ('net_edge_B0_T0', c.project([self.points['B0'], self.points['T0']])), ('net_edge_B1_B2', c.project([self.points['B1'], self.points['B2']])), ('net_edge_B2_T2', c.project([self.points['B2'], self.points['T2']])), ('net_edge_T1_T2', c.project([self.points['T1'], self.points['T2']])), ('net_edge_B2_B3', c.project([self.points['B2'], self.points['B3']])), ('net_edge_B3_T3', c.project([self.points['B3'], self.points['T3']])), ('net_edge_T2_T3', c.project([self.points['T2'], self.points['T3']])), ('net_edge_P_T1', c.project([self.points['P'], self.points['T1']])), ('net_edge_P_T0', c.project([self.points['P'], self.points['T0']])), ('net_edge_B2_Q', c.project([self.points['B2'], self.points['Q']])), ('net_edge_B3_Q', c.project([self.points['B3'], self.points['Q']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('P', c.project(self.points['P']), offset_pt=(0, 16), vertex=True, id='P_label')
            c.text('Q', c.project(self.points['Q']), offset_pt=(0, -16), vertex=True, id='Q_label')
            c.text('R', c.project(self.points['B2']), offset_pt=(-15, -12), vertex=True, id='R_label')
            c.text('S', c.project(self.points['B3']), offset_pt=(13, 0), vertex=True, id='S_label')
            return c.save(output_path)

    def _draw_choices(self, c, kw=None, custom=None):
        _kw = kw or {}
        for object_id, points in [('net_edge_B0_B1', [[0.0, 0.0], [1.0, 0.0]]), ('net_edge_B1_T1', [[1.0, 0.0], [1.0, 1.5]]), ('net_edge_T0_T1', [[0.0, 1.5], [1.0, 1.5]]), ('net_edge_B0_T0', [[0.0, 0.0], [0.0, 1.5]]), ('net_edge_B1_B2', [[1.0, 0.0], [2.0, 0.0]]), ('net_edge_B2_T2', [[2.0, 0.0], [2.0, 1.5]]), ('net_edge_T1_T2', [[1.0, 1.5], [2.0, 1.5]]), ('net_edge_B2_B3', [[2.0, 0.0], [3.0, 0.0]]), ('net_edge_B3_T3', [[3.0, 0.0], [3.0, 1.5]]), ('net_edge_T2_T3', [[2.0, 1.5], [3.0, 1.5]]), ('net_edge_P_T1', [[0.5, 2.3660254037844384], [1.0, 1.5]]), ('net_edge_P_T0', [[0.5, 2.3660254037844384], [0.0, 1.5]]), ('net_edge_B2_Q', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('net_edge_B3_Q', [[3.0, 0.0], [2.5, -0.8660254037844386]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (0.5, 2.3660254037844384), fontsize=18.0, fontstyle='italic', offset_pt=(0, 16))
        c.text('Q', (2.5, -0.8660254037844386), fontsize=18.0, fontstyle='italic', offset_pt=(0, -16))
        c.text('R', (2.0, 0.0), fontsize=18.0, fontstyle='italic', offset_pt=(-15, -12))
        c.text('S', (3.0, 0.0), fontsize=18.0, fontstyle='italic', offset_pt=(13, 0))
        if custom and 5 in custom:
            custom[5](c)
        else:
            c.point([[0.5, 2.3660254037844384]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
        c.point([[3.0, 0.0]], zorder=10, s=50, **_kw.get(6, {'facecolors': '#DC2626', 'edgecolors': '#DC2626'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid73_C01.png'
        with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487)) as c:

            def _slot_5(c):
                c.line([[0.5, 2.3660254037844384], [3.0, 0.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            self._draw_choices(c, custom={5: _slot_5})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid73_C02.png'
        with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487)) as c:

            def _slot_5(c):
                c.point([[0.0, 1.5]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
                c.point([[2.0, 0.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
                c.point([[1.0, 1.5]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
                c.point([[2.5, -0.8660254037844386]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
                c.point([[0.5, 2.3660254037844384]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            self._draw_choices(c, custom={5: _slot_5}, kw={6: {'facecolors': '#2563EB', 'edgecolors': '#2563EB'}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid73_C03.png'
        with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487)) as c:

            def _slot_5(c):
                c.point([[0.5, 2.3660254037844384]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
                c.point([[2.5, -0.8660254037844386]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
                c.point([[0.0, 1.5]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            self._draw_choices(c, custom={5: _slot_5}, kw={6: {'facecolors': '#2563EB', 'edgecolors': '#2563EB'}})
            c.point([[1.0, 1.5]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.point([[2.0, 0.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid73_C04.png'
        with Canvas(SOLID, xlim=(-0.3194144470766229, 3.4524195679314893), ylim=(-1.1292619149114638, 2.6425721000966487)) as c:
            self._draw_choices(c)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid73')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Solid73().draw(args.output, variant=args.variant))
