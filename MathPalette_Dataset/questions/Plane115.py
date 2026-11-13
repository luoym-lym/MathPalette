"""Collected question Plane115; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane115:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self.points = {'P': [0.0, 0.0], 'O': [3.0, 2.0], 'A': [6.0, 4.0], 'B': [6.0, 2.7], 'C': [6.0, 5.3]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411)) as c:
            c.line([self.points['P'], self.points['O']], id='PO')
            for object_id, points in [('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id)
            c.text('P', self.points['P'], offset_pt=(-20, -17), vertex=True, ha='right', id='P_label')
            c.text('O', self.points['O'], offset_pt=(0, -20), vertex=True, id='O_label')
            for object_id, text, anchor in [('A_label', 'A', self.points['A']), ('B_label', 'B', self.points['B']), ('C_label', 'C', self.points['C'])]:
                c.text(text, anchor, id=object_id, offset_pt=(15, 0), vertex=True, ha='left')
            return c.save(output_path)

    def _draw_choices(self, c):
        c.line([[0.0, 0.0], [3.0, 2.0]], id='PO')
        for object_id, points in [('A_dot', [[6.0, 4.0]]), ('B_dot', [[6.0, 2.7]]), ('C_dot', [[6.0, 5.3]])]:
            c.point(points, id=object_id)
        c.text('P', (0.0, 0.0), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', offset_pt=(-20, -17))
        c.text('O', (3.0, 2.0), id='O_label', fontsize=18.0, fontstyle='italic', offset_pt=(0, -20))
        for object_id, text, anchor in [('A_label', 'A', (6.0, 4.0)), ('B_label', 'B', (6.0, 2.7)), ('C_label', 'C', (6.0, 5.3))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', ha='left', offset_pt=(15, 0))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane115_C01.png'
        with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411)) as c:
            self._draw_choices(c)
            c.line([[3.0, 2.0], [6.0, 2.7]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[2.941782804302842, 6.063618784990867], [2.978385416666666, -0.9128391315541187]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane115_C02.png'
        with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411)) as c:
            self._draw_choices(c)
            c.line([[3.0, 2.0], [6.0, 5.3]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[1.594806669314093, 6.027016172627042], [1.6314092816779178, -0.7957107719898797]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4.9256443944221395, 6.027016172627042], [4.991529096677024, -0.8542749517719992]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane115_C03.png'
        with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411)) as c:
            self._draw_choices(c)
            c.line([[3.0, 2.0], [6.0, 2.7]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane115_C04.png'
        with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411)) as c:
            self._draw_choices(c)
            c.line([[3.0, 2.0], [6.0, 5.3]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane115')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane115().draw(args.output, variant=args.variant))
