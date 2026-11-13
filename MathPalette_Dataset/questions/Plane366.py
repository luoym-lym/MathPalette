"""Collected question Plane366; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane366:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c):
        for object_id, points in [('o0', [[0.0, 0.0], [0.0, 5.0]]), ('o1', [[1.0, 0.0], [1.0, 5.0]]), ('o2', [[2.0, 0.0], [2.0, 5.0]]), ('o3', [[3.0, 0.0], [3.0, 5.0]]), ('o4', [[4.0, 0.0], [4.0, 5.0]]), ('o5', [[5.0, 0.0], [5.0, 5.0]]), ('o6', [[6.0, 0.0], [6.0, 5.0]]), ('o7', [[0.0, 0.0], [6.0, 0.0]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]]), ('o12', [[0.0, 5.0], [6.0, 5.0]])]:
            c.line(points, id=object_id, color='#AAAAAA')
        c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
        c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
        for object_id, center, radius in [('o15', [3.0, 4.0], 0.065), ('o16', [2.0, 3.0], 0.065), ('o17', [1.0, 1.0], 0.065), ('o18', [2.0, 1.0], 0.065)]:
            c.circle(center, radius, id=object_id, fill=False)
        c.text('X', (3.0, 4.0), id='label_X0', fontsize=18.0, fontstyle='italic', offset_pt=(31.541044653535405, 31.54104465353544))
        c.text('Y', (2.0, 3.0), id='label_Y1', fontsize=18.0, fontstyle='italic', offset_pt=(27.598414071843493, 31.541044653535405))
        c.text('Z', (1.0, 1.0), id='label_Z2', fontsize=18.0, fontstyle='italic', offset_pt=(-39.42630581691927, -43.3689363986112))
        c.text('T', (2.0, 1.0), id='label_T3', fontsize=18.0, fontstyle='italic', offset_pt=(31.541044653535405, -43.3689363986112))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C01.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.line([[2, 1], [3, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[1, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C02.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[3, 4], [1, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 4], [3, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C03.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.line([[3, 4], [1, 4]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 4], [3, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C04.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.line([[3, 4], [1, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C05.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.line([[3, 4], [1, 4]], zorder=9, color='#2563EB', solid_capstyle='butt')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane366_C06.png'
        with Canvas(PLANE, xlim=(-0.1479503677176517, 6.159538797762297), ylim=(-0.6595321727622103, 5.647956992717738)) as c:
            self._draw_base(c)
            c.line([[3, 4], [1, 4]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[3, 4], [3, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane366')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane366().draw(args.output, variant=args.variant))
