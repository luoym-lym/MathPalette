"""Collected question Plane128; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane128:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='shade', capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C01.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C02.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', edgecolor='#DC2626', linewidth=1.5, capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor='#DC2626', linewidth=1.5, joinstyle='round', fill=False)
            for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C03.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C04.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', edgecolor='#DC2626', linewidth=3.0, capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor='#DC2626', linewidth=3.0, joinstyle='round', fill=False)
            for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C05.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]]), ('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
                c.line(points, id=object_id)
            c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane128_C06.png'
        with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442)) as c:
            c.path([[0.0, 0.0], [3.0, 1.0], [5.0, 4.0], [2.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [3.0, 0.9999999999999999], [5.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
            c.path([[5.0, 4.0], [2.0, 3.0], [5.551115123125783e-17, -1.1102230246251565e-16]], [1, 2, 2], id='shade', edgecolor='#2563EB', linewidth=3.0, capstyle='butt', fill=False)
            for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor='#2563EB', linewidth=3.0, joinstyle='round', fill=False)
            for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane128')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane128().draw(args.output, variant=args.variant))
