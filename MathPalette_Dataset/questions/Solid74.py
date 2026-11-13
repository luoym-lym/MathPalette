"""Collected question Solid74; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid74:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'v0_0': [0.0, 0.0, 0.0], 'v0_1': [0.0, 1.0, 0.0], 'v1_0': [1.0, 0.0, 0.0],
            'v1_1': [1.0, 1.0, 0.0], 'v1_2': [1.0, 2.0, 0.0], 'v2_-1': [2.0, -1.0, 0.0],
            'v2_0': [2.0, 0.0, 0.0], 'v2_1': [2.0, 1.0, 0.0], 'v2_2': [2.0, 2.0, 0.0],
            'v3_-1': [3.0, -1.0, 0.0], 'v3_0': [3.0, 0.0, 0.0], 'v3_1': [3.0, 1.0, 0.0],
            'v4_0': [4.0, 0.0, 0.0], 'v4_1': [4.0, 1.0, 0.0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682), projection=[[1, 0, 0], [0, 1, 0]]) as c:
            for object_id, points in [('edge_v0_0_v1_0', c.project([self.points['v0_0'], self.points['v1_0']])), ('edge_v1_0_v1_1', c.project([self.points['v1_0'], self.points['v1_1']])), ('edge_v0_1_v1_1', c.project([self.points['v0_1'], self.points['v1_1']])), ('edge_v0_0_v0_1', c.project([self.points['v0_0'], self.points['v0_1']])), ('edge_v1_0_v2_0', c.project([self.points['v1_0'], self.points['v2_0']])), ('edge_v2_0_v2_1', c.project([self.points['v2_0'], self.points['v2_1']])), ('edge_v1_1_v2_1', c.project([self.points['v1_1'], self.points['v2_1']])), ('edge_v2_1_v2_2', c.project([self.points['v2_1'], self.points['v2_2']])), ('edge_v1_2_v2_2', c.project([self.points['v1_2'], self.points['v2_2']])), ('edge_v1_1_v1_2', c.project([self.points['v1_1'], self.points['v1_2']])), ('edge_v2_-1_v3_-1', c.project([self.points['v2_-1'], self.points['v3_-1']])), ('edge_v3_-1_v3_0', c.project([self.points['v3_-1'], self.points['v3_0']])), ('edge_v2_0_v3_0', c.project([self.points['v2_0'], self.points['v3_0']])), ('edge_v2_-1_v2_0', c.project([self.points['v2_-1'], self.points['v2_0']])), ('edge_v3_0_v3_1', c.project([self.points['v3_0'], self.points['v3_1']])), ('edge_v2_1_v3_1', c.project([self.points['v2_1'], self.points['v3_1']])), ('edge_v3_0_v4_0', c.project([self.points['v3_0'], self.points['v4_0']])), ('edge_v4_0_v4_1', c.project([self.points['v4_0'], self.points['v4_1']])), ('edge_v3_1_v4_1', c.project([self.points['v3_1'], self.points['v4_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('P', c.project(self.points['v1_2']), offset_pt=(0, 16), vertex=True, id='P_label')
            c.text('Q', c.project(self.points['v3_-1']), offset_pt=(12, -12), vertex=True, id='Q_label')
            c.text('R', c.project(self.points['v0_1']), offset_pt=(-14, 0), vertex=True, id='R_label')
            c.text('S', c.project(self.points['v1_1']), offset_pt=(22, 17), vertex=True, id='S_label')
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        for object_id, points in [('edge_v0_0_v1_0', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v1_0_v1_1', [[1.0, 0.0], [1.0, 1.0]]), ('edge_v0_1_v1_1', [[0.0, 1.0], [1.0, 1.0]]), ('edge_v0_0_v0_1', [[0.0, 0.0], [0.0, 1.0]]), ('edge_v1_0_v2_0', [[1.0, 0.0], [2.0, 0.0]]), ('edge_v2_0_v2_1', [[2.0, 0.0], [2.0, 1.0]]), ('edge_v1_1_v2_1', [[1.0, 1.0], [2.0, 1.0]]), ('edge_v2_1_v2_2', [[2.0, 1.0], [2.0, 2.0]]), ('edge_v1_2_v2_2', [[1.0, 2.0], [2.0, 2.0]]), ('edge_v1_1_v1_2', [[1.0, 1.0], [1.0, 2.0]]), ('edge_v2_-1_v3_-1', [[2.0, -1.0], [3.0, -1.0]]), ('edge_v3_-1_v3_0', [[3.0, -1.0], [3.0, 0.0]]), ('edge_v2_0_v3_0', [[2.0, 0.0], [3.0, 0.0]]), ('edge_v2_-1_v2_0', [[2.0, -1.0], [2.0, 0.0]]), ('edge_v3_0_v3_1', [[3.0, 0.0], [3.0, 1.0]]), ('edge_v2_1_v3_1', [[2.0, 1.0], [3.0, 1.0]]), ('edge_v3_0_v4_0', [[3.0, 0.0], [4.0, 0.0]]), ('edge_v4_0_v4_1', [[4.0, 0.0], [4.0, 1.0]]), ('edge_v3_1_v4_1', [[3.0, 1.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('P', (1.0, 2.0), fontsize=18.0, fontstyle='italic', offset_pt=(0, 16))
        c.text('Q', (3.0, -1.0), fontsize=18.0, fontstyle='italic', offset_pt=(12, -12))
        c.text('R', (0.0, 1.0), fontsize=18.0, fontstyle='italic', offset_pt=(-14, 0))
        c.text('S', (1.0, 1.0), fontsize=18.0, fontstyle='italic', offset_pt=(22, 17))
        c.point([[1.0, 2.0]], zorder=10, s=50, **_kw.get(5, {'facecolors': '#2563EB', 'edgecolors': '#2563EB'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid74_C01.png'
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682)) as c:
            self._draw_choices(c)
            c.point([[3.0, -1.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.point([[0.0, 1.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid74_C02.png'
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682)) as c:
            self._draw_choices(c, kw={5: {'facecolors': '#16A34A', 'edgecolors': '#16A34A'}})
            c.point([[3.0, -1.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.line([[1.0, 2.0], [3.0, -1.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid74_C03.png'
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682)) as c:
            self._draw_choices(c, kw={5: {'facecolors': '#EA580C', 'edgecolors': '#EA580C'}})
            c.point([[3.0, -1.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[1.0, 2.0], [3.0, -1.0]], zorder=9, color='#EA580C', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid74_C04.png'
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682)) as c:
            self._draw_choices(c)
            c.point([[1.0, 1.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.point([[0.0, 1.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid74_C05.png'
        with Canvas(SOLID, xlim=(-0.2784482720289403, 4.09723746072793), ylim=(-1.6698298632670028, 2.7058558694898682)) as c:
            self._draw_choices(c, kw={5: {'facecolors': '#16A34A', 'edgecolors': '#16A34A'}})
            c.point([[1.0, 1.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.line([[1.0, 2.0], [1.0, 1.0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid74')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Solid74().draw(args.output, variant=args.variant))
