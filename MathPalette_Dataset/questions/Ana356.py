"""Collected question Ana356; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana356:
    variants = ('C01', 'C02')

    def _draw_base(self, c):
        c.line([[-7, 2.5], [7, -4.5]], id='object_000', solid_capstyle='butt')
        c.point([[2, 3]], id='object_001')
        c.text('L', [2.22, 3.25], ha='left', va='bottom')

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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana356_C01.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[2, 3], [0, -1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[0.0, -1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana356_C02.png'
        with Canvas(ANALYTICS) as c:
            self._draw_base(c)
            c.line([[2, 3], [-1, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[-1.0, 0.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana356')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana356().draw(args.output, variant=args.variant))
