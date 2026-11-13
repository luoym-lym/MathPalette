"""Collected question Plane104; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane104:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.points = {
            'R_0': [-6.5, 2.0], 'R_1': [-3.5, 2.0], 'R_2': [-1.5, 4.0], 'R_3': [-3.5, 6.0],
            'R_4': [-6.5, 6.0], 'R_5': [-5.0, 4.5], 'name_anchor_R': [-4.0, 2.0], 'A_0': [1.5, 2.0],
            'A_1': [4.5, 2.0], 'A_2': [6.5, 4.0], 'A_3': [4.5, 6.0], 'A_4': [1.5, 6.0], 'A_5': [2.25, 4.5],
            'name_anchor_A': [4.0, 2.0], 'B_0': [-2.0, -1.5], 'B_1': [-2.0, -4.5], 'B_2': [-4.0, -6.5],
            'B_3': [-6.0, -4.5], 'B_4': [-6.0, -1.4999999999999998], 'B_5': [-4.5, -3.0],
            'name_anchor_B': [-4.0, -6.5], 'C_0': [1.5, -6.0], 'C_1': [4.5, -6.0], 'C_2': [6.5, -3.0],
            'C_3': [4.5, -2.0], 'C_4': [1.5, -2.0], 'C_5': [3.0, -3.5], 'name_anchor_C': [4.0, -6.0]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            for object_id, vertices, codes in [('outline_R', [self.points['R_0'], self.points['R_1'], self.points['R_2'], self.points['R_3'], self.points['R_4'], self.points['R_5'], self.points['R_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_A', [self.points['A_0'], self.points['A_1'], self.points['A_2'], self.points['A_3'], self.points['A_4'], self.points['A_5'], self.points['A_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_B', [self.points['B_0'], self.points['B_1'], self.points['B_2'], self.points['B_3'], self.points['B_4'], self.points['B_5'], self.points['B_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_C', [self.points['C_0'], self.points['C_1'], self.points['C_2'], self.points['C_3'], self.points['C_4'], self.points['C_5'], self.points['C_0']], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=(0, -22))
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', capstyle='butt', **_kw.get(0, {'edgecolor': '#DC2626'}))
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', capstyle='butt', **_kw.get(1, {}))
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt', **_kw.get(2, {}))
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', capstyle='butt', **_kw.get(3, {}))
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, offset_pt=(0, -22))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C01.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            self._draw_choices(c, kw={1: {'edgecolor': '#DC2626'}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C02.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            self._draw_choices(c, kw={0: {'edgecolor': '#2563EB', 'linestyle': (0, [3.7, 1.6])}, 3: {'edgecolor': '#2563EB', 'linestyle': (0, [3.7, 1.6])}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C03.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            self._draw_choices(c, kw={0: {'edgecolor': '#EA580C', 'linestyle': (0, [3.7, 1.6])}, 1: {'linestyle': (0, [3.7, 1.6])}, 2: {'linestyle': (0, [3.7, 1.6])}, 3: {'edgecolor': '#EA580C', 'linestyle': (0, [3.7, 1.6])}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C04.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            self._draw_choices(c, kw={0: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 1: {'edgecolor': '#DC2626', 'linewidth': 3.0}, 2: {'linestyle': (0, [3.7, 1.6]), 'linewidth': 0.5}, 3: {'linestyle': (0, [3.7, 1.6]), 'linewidth': 0.5}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C05.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573)) as c:
            self._draw_choices(c, kw={0: {'edgecolor': '#16A34A', 'linestyle': (0, [3.7, 1.6])}, 3: {'edgecolor': '#16A34A', 'linestyle': (0, [3.7, 1.6])}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane104')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane104().draw(args.output, variant=args.variant))
