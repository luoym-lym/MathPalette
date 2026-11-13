"""Collected question Ana49; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana49:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self._samples_001 = [[4.0, 0.0], [5.0608124, 0.0], [6.078319483139413, 0.21073261682351663], [6.82842712474619, 0.5857864376269049], [7.578534766352966, 0.9608402584302931], [8.0, 1.4695938], [8.0, 2.0], [8.0, 2.5304062], [7.578534766352966, 3.0391597415697067], [6.82842712474619, 3.414213562373095], [6.078319483139413, 3.789267383176483], [5.0608124, 4.0], [4.0, 4.0], [2.9391876, 4.0], [1.9216805168605862, 3.789267383176483], [1.1715728752538097, 3.414213562373095], [0.42146523364703325, 3.0391597415697067], [0.0, 2.5304062], [0.0, 2.0], [0.0, 1.4695938], [0.42146523364703325, 0.9608402584302931], [1.1715728752538097, 0.5857864376269049], [1.9216805168605862, 0.21073261682351663], [2.9391876, 0.0], [4.0, 0.0], [4.0, 0.0]]
        self._geometry_02 = [1] + [4] * 24 + [79]

    def _draw_base(self, c):
        c.line([[0.0, 0.0], [8.0, 0.0], [8.0, 4.0], [0.0, 4.0], [0.0, 0.0]], id='curve_001', solid_capstyle='butt')
        c.path(self._samples_001, self._geometry_02, id='curve_002', alpha=1.0, capstyle='butt', fill=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana49_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[0, 4], [7, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0, 0], [7, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.497059, 1.952941]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana49_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[3, 8], [3, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, 2], [8, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana49_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[5, 8], [5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[-8, 2], [8, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[5.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana49_C04.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[5.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana49_C05.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[3.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana49')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Ana49().draw(args.output, variant=args.variant))
