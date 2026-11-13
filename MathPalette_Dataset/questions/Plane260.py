"""Collected question Plane260; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane260:
    variants = ('C01', 'C02')

    def _draw_base(self, c):
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor='#D0D0D0', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane260_C01.png'
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[2.50732973761175, 4.528298269615471]]), (None, [[4.558263856072971, 3.4598797105217973]]), (None, [[3.527427859359478, 2.5256845885001935]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane260_C02.png'
        with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[3.575748296705422, 0.4854883450047369]]), (None, [[3.548903609291009, 2.4451505262569517]]), (None, [[2.6683978620982325, 4.528298269615471]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane260')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane260().draw(args.output, variant=args.variant))
