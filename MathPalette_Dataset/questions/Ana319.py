"""Collected question Ana319; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS

class Ana319:
    variants = ('C01',)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS) as c:
            c.point([[-2, 2]], id='object_000')
            c.point([[1, 3]], id='object_001')
            for object_id, text, anchor in [(None, 'A', [-1.78, 2.25]), (None, 'B', [1.22, 3.25]), (None, 'l', [6.5, 0.35])]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana319_C01.png'
        with Canvas(ANALYTICS) as c:
            c.point([[-2.0, 2.0]], id='point_001')
            c.point([[1.0, 3.0]], id='point_002')
            for object_id, text, anchor in [('text_001', 'A', (-1.78, 2.25)), ('text_002', 'B', (1.22, 3.25)), ('text_003', 'l', (6.5, 0.35))]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            for object_id, points in [(None, [[-2, 2], [-2, -2]]), (None, [[-2, -2], [1, 2]]), (None, [[-2.0, 2.0], [-0.549287, 0.021026]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana319')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Ana319().draw(args.output, variant=args.variant))
