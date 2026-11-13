"""Collected question Plane518; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane518:
    variants = ('C01', 'C02', 'C03', 'C04')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.11627906976744207, 5.116279069767442)) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor='#D0D0D0', capstyle='butt')
            for object_id, points in [('v0', [[0, 0], [0, 5]]), ('v1', [[1, 0], [1, 5]]), ('v2', [[2, 0], [2, 5]]), ('v3', [[3, 0], [3, 5]]), ('v4', [[4, 0], [4, 5]]), ('v5', [[5, 0], [5, 5]]), ('h0', [[0, 0], [5, 0]]), ('h1', [[0, 1], [5, 1]]), ('h2', [[0, 2], [5, 2]]), ('h3', [[0, 3], [5, 3]]), ('h4', [[0, 4], [5, 4]]), ('h5', [[0, 5], [5, 5]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane518_C01.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.11627906976744207, 5.116279069767442)) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor='#D0D0D0', capstyle='butt')
            c.line([[0, 0], [0, 5]], id='v0')
            c.line([[1, 0], [1, 5]], id='v1')
            c.path([[2.0, 5.551115123125783e-17], [2.0, 2.0]], [1, 2], id='v2', joinstyle='round', fill=False)
            c.path([[2.0, 2.0], [2.0, 3.0]], [1, 2], id='v2', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[2.0, 3.0], [2.0, 5.0]], [1, 2], id='v2', joinstyle='round', fill=False)
            c.path([[3.0, 5.551115123125783e-17], [3.0, 2.0]], [1, 2], id='v3', joinstyle='round', fill=False)
            c.path([[3.0, 2.0], [3.0, 3.0]], [1, 2], id='v3', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[3.0, 3.0], [3.0, 5.0]], [1, 2], id='v3', joinstyle='round', fill=False)
            for object_id, points in [('v4', [[4, 0], [4, 5]]), ('v5', [[5, 0], [5, 5]]), ('h0', [[0, 0], [5, 0]]), ('h1', [[0, 1], [5, 1]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 2.0], [2.0, 2.0]], [1, 2], id='h2', joinstyle='round', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0]], [1, 2], id='h2', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[3.0, 2.0], [5.0, 2.0]], [1, 2], id='h2', joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, 3.0], [2.0, 3.0]], [1, 2], id='h3', joinstyle='round', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0]], [1, 2], id='h3', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[3.0, 3.0], [5.0, 3.0]], [1, 2], id='h3', joinstyle='round', fill=False)
            c.line([[0, 4], [5, 4]], id='h4')
            c.line([[0, 5], [5, 5]], id='h5')
            c.line([[2.5, 0.0], [2.5, 5.0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[0.0, 2.5], [5.0, 2.5]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[0, 0], [5, 5]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0, 5], [5, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane518_C02.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.11627906976744207, 5.116279069767442)) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor='#D0D0D0', capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [5.551115123125783e-17, 5.0]], [1, 2], id='v0', edgecolor='#DC2626', joinstyle='round', fill=False)
            for object_id, points in [('v1', [[1, 0], [1, 5]]), ('v2', [[2, 0], [2, 5]]), ('v3', [[3, 0], [3, 5]]), ('v4', [[4, 0], [4, 5]])]:
                c.line(points, id=object_id)
            c.path([[5.0, 5.551115123125783e-17], [5.0, 5.0]], [1, 2], id='v5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [5.0, 5.551115123125783e-17]], [1, 2], id='h0', edgecolor='#DC2626', joinstyle='round', fill=False)
            for object_id, points in [('h1', [[0, 1], [5, 1]]), ('h2', [[0, 2], [5, 2]]), ('h3', [[0, 3], [5, 3]]), ('h4', [[0, 4], [5, 4]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 5.0], [5.0, 5.0]], [1, 2], id='h5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.line([[2.5, 0.0], [2.5, 5.0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[0.0, 2.5], [5.0, 2.5]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane518_C03.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.11627906976744207, 5.116279069767442)) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor='#D0D0D0', capstyle='butt')
            c.line([[0, 0], [0, 5]], id='v0')
            c.line([[1, 0], [1, 5]], id='v1')
            c.line([[2, 0], [2, 5]], id='v2', color='#DC2626')
            c.line([[3, 0], [3, 5]], id='v3', color='#DC2626')
            for object_id, points in [('v4', [[4, 0], [4, 5]]), ('v5', [[5, 0], [5, 5]]), ('h0', [[0, 0], [5, 0]]), ('h1', [[0, 1], [5, 1]])]:
                c.line(points, id=object_id)
            c.line([[0, 2], [5, 2]], id='h2', color='#DC2626')
            c.line([[0, 3], [5, 3]], id='h3', color='#DC2626')
            c.line([[0, 4], [5, 4]], id='h4')
            c.line([[0, 5], [5, 5]], id='h5')
            c.line([[2.5, 0.0], [2.5, 5.0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[0.0, 2.5], [5.0, 2.5]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane518_C04.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.11627906976744207, 5.116279069767442)) as c:
            for object_id, vertices, codes in [(None, [[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor='#D0D0D0', capstyle='butt')
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [5.551115123125783e-17, 1.0]], [1, 2], id='v0', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, 1.0], [5.551115123125783e-17, 4.0]], [1, 2], id='v0', joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, 4.0], [5.551115123125783e-17, 5.0]], [1, 2], id='v0', edgecolor='#DC2626', joinstyle='round', fill=False)
            for object_id, points in [('v1', [[1, 0], [1, 5]]), ('v2', [[2, 0], [2, 5]]), ('v3', [[3, 0], [3, 5]]), ('v4', [[4, 0], [4, 5]])]:
                c.line(points, id=object_id)
            c.path([[5.0, 5.551115123125783e-17], [5.0, 1.0]], [1, 2], id='v5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[5.0, 1.0], [5.0, 4.0]], [1, 2], id='v5', joinstyle='round', fill=False)
            c.path([[5.0, 4.0], [5.0, 5.0]], [1, 2], id='v5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, 5.551115123125783e-17], [1.0, 5.551115123125783e-17]], [1, 2], id='h0', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[1.0, 5.551115123125783e-17], [4.0, 5.551115123125783e-17]], [1, 2], id='h0', joinstyle='round', fill=False)
            c.path([[4.0, 5.551115123125783e-17], [5.0, 5.551115123125783e-17]], [1, 2], id='h0', edgecolor='#DC2626', joinstyle='round', fill=False)
            for object_id, points in [('h1', [[0, 1], [5, 1]]), ('h2', [[0, 2], [5, 2]]), ('h3', [[0, 3], [5, 3]]), ('h4', [[0, 4], [5, 4]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 5.0], [1.0, 5.0]], [1, 2], id='h5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.path([[1.0, 5.0], [4.0, 5.0]], [1, 2], id='h5', joinstyle='round', fill=False)
            c.path([[4.0, 5.0], [5.0, 5.0]], [1, 2], id='h5', edgecolor='#DC2626', joinstyle='round', fill=False)
            c.line([[2.5, 0.0], [2.5, 5.0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[0.0, 2.5], [5.0, 2.5]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane518')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane518().draw(args.output, variant=args.variant))
