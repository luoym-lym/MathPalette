"""Collected question Ana04; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana04:
    variants = ('C01', 'C02', 'C03')

    def _draw_base(self, c):
        x = np.linspace(-8, 8, 255)
        c.line(np.column_stack((x, np.cos(2 * x))), id='curve_001', solid_capstyle='butt')
        x = np.linspace(-8, 8, 255)
        c.line(np.column_stack((x, 3 * np.sin(2 * x))), id='curve_002', solid_capstyle='butt')
        c.text('y1', [3.061592653589793, 1.4], id='text_001', ha='right', va='bottom')
        c.text('y2', [0.7853981633974483, 3.4], id='text_002', va='bottom')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana04_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[-3.2125, 7.963971], [-3.433088, -7.991912]]), (None, [[-2.348529, 7.982353], [-2.348529, -7.826471]]), (None, [[-6, 8], [-6, -8]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana04_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[4, -8], [4, 8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4.728676, 7.982353], [4.783824, -7.918382]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana04_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[0.721324, 7.963971], [0.739706, -7.918382]]), (None, [[3, 8], [3, -8]]), (None, [[4, 8], [4, -8]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana04')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Ana04().draw(args.output, variant=args.variant))
