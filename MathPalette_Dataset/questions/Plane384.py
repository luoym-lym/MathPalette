"""Collected question Plane384; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane384:
    variants = ('C01',)

    def _draw_base(self, c):
        c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0', capstyle='butt')
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('cell2', [[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79]), ('cell3', [[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79]), ('cell4', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79]), ('cell5', [[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell6', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell6', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell7', capstyle='butt')
        c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell8', capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('cell10', [[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79]), ('cell11', [[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79]), ('cell12', [[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell13', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell13', capstyle='butt', fill=False)
        c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell14', capstyle='butt')
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell15', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('cell16', [[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79]), ('cell17', [[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79]), ('cell18', [[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79]), ('cell19', [[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79]), ('cell20', [[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79]), ('cell21', [[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell22', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell22', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('cell23', [[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79]), ('cell24', [[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79]), ('cell25', [[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79]), ('cell26', [[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79]), ('cell27', [[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79]), ('cell28', [[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79]), ('cell29', [[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79]), ('cell30', [[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79]), ('cell31', [[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79]), ('cell32', [[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79]), ('cell33', [[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell34', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell34', capstyle='butt', fill=False)
        c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell35', capstyle='butt')
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell36', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell36', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('cell37', [[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79]), ('cell38', [[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79]), ('cell39', [[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79]), ('cell40', [[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.2230502095313236, 9.238034935319352), ylim=(-0.2380349353193525, 9.223050209531323)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane384_C01.png'
        with Canvas(PLANE, xlim=(-0.2230502095313236, 9.238034935319352), ylim=(-0.2380349353193525, 9.223050209531323)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[1.5025929755895202, 5.4490511719714005]]), (None, [[4.575126754248133, 2.434489728759176]]), (None, [[5.541332345021282, 3.42968148725552]]), (None, [[2.5944052931631787, 2.492462064205565]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane384')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane384().draw(args.output, variant=args.variant))
