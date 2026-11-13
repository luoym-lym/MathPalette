"""Collected question Ana16; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana16:
    variants = ('C01', 'C02', 'C03')

    def _draw_base(self, c):
        x = np.linspace(0, 2 * np.pi, 300)
        c.line(np.column_stack((x, 2.5 * np.cos(x))), id='curve_001', solid_capstyle='butt')
        x = np.linspace(0, 2 * np.pi, 300)
        c.line(np.column_stack((x, 2.5 * np.sin(x))), id='curve_002', solid_capstyle='butt')
        c.text('y1', [0.3, 2.8], id='text_001', ha='left', va='bottom')
        c.text('y2', [2.2, 2.8], id='text_002', ha='left', va='bottom')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana16_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[0.794853, 1.750735]]), (None, [[3.956618, -1.778676]]), (None, [[3.147794, 0.022794]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana16_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.point([[0.794853, 1.713971]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana16_C03.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[3.938235, -1.815441]]), (None, [[3.129412, 0.004412]]), (None, [[1.548529, -0.013971]]), (None, [[0.813235, 1.750735]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana16')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Ana16().draw(args.output, variant=args.variant))
