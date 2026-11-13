"""Collected question Plane293; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane293:
    variants = ('C01',)

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black0_0', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='black0_0', capstyle='butt', fill=False)
        for object_id, points in [('grid0_0', [[0.0, 0.0], [0.0, 1.0]]), ('grid0_1', [[0.0, 0.0], [1.0, 0.0]]), ('grid0_2', [[0.0, 1.0], [0.0, 2.0]]), ('grid0_3', [[0.0, 1.0], [1.0, 1.0]]), ('grid0_4', [[0.0, 2.0], [1.0, 2.0]]), ('grid0_5', [[1.0, 0.0], [1.0, 1.0]]), ('grid0_6', [[1.0, 0.0], [2.0, 0.0]]), ('grid0_7', [[1.0, 1.0], [1.0, 2.0]]), ('grid0_8', [[1.0, 1.0], [2.0, 1.0]]), ('grid0_9', [[1.0, 2.0], [2.0, 2.0]]), ('grid0_10', [[2.0, 0.0], [2.0, 1.0]]), ('grid0_11', [[2.0, 1.0], [2.0, 2.0]]), ('diag0_0', [[0.0, 0.0], [1.0, 1.0]]), ('diag0_1', [[1.0, 1.0], [2.0, 2.0]]), ('antidiag0', [[1.0, 1.0], [2.0, 0.0]])]:
            c.line(points, id=object_id)
        c.path([[3.5, 1.0], [4.5, 1.0], [3.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='black1_0', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[3.5, 1.0], [4.5, 1.0], [3.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='black1_0', capstyle='butt', fill=False)
        c.path([[4.5, 1.0], [5.5, 1.0], [5.5, 0.0], [4.5, 1.0]], [1, 2, 2, 79], id='black1_1', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[4.5, 1.0], [5.5, 1.0], [5.5, 0.0], [4.5, 1.0]], [1, 2, 2, 79], id='black1_1', capstyle='butt', fill=False)
        for object_id, points in [('grid1_0', [[3.5, 0.0], [3.5, 1.0]]), ('grid1_1', [[3.5, 0.0], [4.5, 0.0]]), ('grid1_2', [[3.5, 1.0], [3.5, 2.0]]), ('grid1_3', [[3.5, 1.0], [4.5, 1.0]]), ('grid1_4', [[3.5, 2.0], [4.5, 2.0]]), ('grid1_5', [[4.5, 0.0], [4.5, 1.0]]), ('grid1_6', [[4.5, 0.0], [5.5, 0.0]]), ('grid1_7', [[4.5, 1.0], [4.5, 2.0]]), ('grid1_8', [[4.5, 1.0], [5.5, 1.0]]), ('grid1_9', [[4.5, 2.0], [5.5, 2.0]]), ('grid1_10', [[5.5, 0.0], [5.5, 1.0]]), ('grid1_11', [[5.5, 1.0], [5.5, 2.0]]), ('diag1_0', [[3.5, 0.0], [4.5, 1.0]]), ('diag1_1', [[4.5, 1.0], [5.5, 2.0]]), ('antidiag1', [[3.5, 2.0], [5.5, 0.0]])]:
            c.line(points, id=object_id)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='black2_0', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='black2_0', capstyle='butt', fill=False)
        c.path([[8.0, 1.0], [8.5, 1.5], [9.0, 1.0], [8.5, 0.5], [8.0, 1.0]], [1, 2, 2, 2, 79], id='black2_1', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 1.0], [8.5, 1.5], [9.0, 1.0], [8.5, 0.5], [8.0, 1.0]], [1, 2, 2, 2, 79], id='black2_1', capstyle='butt', fill=False)
        for object_id, points in [('grid2_0', [[7.0, 0.0], [7.0, 1.0]]), ('grid2_1', [[7.0, 0.0], [8.0, 0.0]]), ('grid2_2', [[7.0, 1.0], [7.0, 2.0]]), ('grid2_3', [[7.0, 1.0], [8.0, 1.0]]), ('grid2_4', [[7.0, 2.0], [8.0, 2.0]]), ('grid2_5', [[8.0, 0.0], [8.0, 1.0]]), ('grid2_6', [[8.0, 0.0], [9.0, 0.0]]), ('grid2_7', [[8.0, 1.0], [8.0, 2.0]]), ('grid2_8', [[8.0, 1.0], [9.0, 1.0]]), ('grid2_9', [[8.0, 2.0], [9.0, 2.0]]), ('grid2_10', [[9.0, 0.0], [9.0, 1.0]]), ('grid2_11', [[9.0, 1.0], [9.0, 2.0]]), ('diag200', [[7.0, 0.0], [8.0, 1.0]]), ('anti200', [[7.0, 1.0], [8.0, 0.0]]), ('diag201', [[7.0, 1.0], [8.0, 2.0]]), ('anti201', [[7.0, 2.0], [8.0, 1.0]]), ('diag210', [[8.0, 0.0], [9.0, 1.0]]), ('anti210', [[8.0, 1.0], [9.0, 0.0]]), ('diag211', [[8.0, 1.0], [9.0, 2.0]]), ('anti211', [[8.0, 2.0], [9.0, 1.0]])]:
            c.line(points, id=object_id)
        c.path([[10.5, 2.0], [11.5, 2.0], [11.0, 1.5], [10.5, 2.0]], [1, 2, 2, 79], id='black3_0', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[10.5, 2.0], [11.5, 2.0], [11.0, 1.5], [10.5, 2.0]], [1, 2, 2, 79], id='black3_0', capstyle='butt', fill=False)
        c.path([[11.5, 2.0], [12.5, 2.0], [12.0, 1.5], [11.5, 2.0]], [1, 2, 2, 79], id='black3_1', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[11.5, 2.0], [12.5, 2.0], [12.0, 1.5], [11.5, 2.0]], [1, 2, 2, 79], id='black3_1', capstyle='butt', fill=False)
        c.path([[10.5, 0.0], [10.5, 1.0], [11.0, 0.5], [10.5, 0.0]], [1, 2, 2, 79], id='black3_2', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[10.5, 0.0], [10.5, 1.0], [11.0, 0.5], [10.5, 0.0]], [1, 2, 2, 79], id='black3_2', capstyle='butt', fill=False)
        c.path([[12.5, 0.0], [12.5, 1.0], [12.0, 0.5], [12.5, 0.0]], [1, 2, 2, 79], id='black3_3', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[12.5, 0.0], [12.5, 1.0], [12.0, 0.5], [12.5, 0.0]], [1, 2, 2, 79], id='black3_3', capstyle='butt', fill=False)
        _ov = {j: s for idxs, s in _hi.get(21, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('grid3_0', [[10.5, 0.0], [10.5, 1.0]]), ('grid3_1', [[10.5, 0.0], [11.5, 0.0]]), ('grid3_2', [[10.5, 1.0], [10.5, 2.0]]), ('grid3_3', [[10.5, 1.0], [11.5, 1.0]]), ('grid3_4', [[10.5, 2.0], [11.5, 2.0]]), ('grid3_5', [[11.5, 0.0], [11.5, 1.0]]), ('grid3_6', [[11.5, 0.0], [12.5, 0.0]]), ('grid3_7', [[11.5, 1.0], [11.5, 2.0]]), ('grid3_8', [[11.5, 1.0], [12.5, 1.0]]), ('grid3_9', [[11.5, 2.0], [12.5, 2.0]]), ('grid3_10', [[12.5, 0.0], [12.5, 1.0]]), ('grid3_11', [[12.5, 1.0], [12.5, 2.0]]), ('diag300', [[10.5, 0.0], [11.5, 1.0]]), ('anti300', [[10.5, 1.0], [11.5, 0.0]]), ('diag301', [[10.5, 1.0], [11.5, 2.0]]), ('anti301', [[10.5, 2.0], [11.5, 1.0]]), ('diag310', [[11.5, 0.0], [12.5, 1.0]]), ('anti310', [[11.5, 1.0], [12.5, 0.0]]), ('diag311', [[11.5, 1.0], [12.5, 2.0]]), ('anti311', [[11.5, 2.0], [12.5, 1.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, text, anchor in [('label0', 'A', (1.0, -0.4)), ('label1', 'B', (4.5, -0.4)), ('label2', 'C', (8.0, -0.4)), ('label3', 'D', (11.5, -0.4))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.3071312127620942, 12.825615244577339), ylim=(-5.812123793915195, 7.320622663424238)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane293_C01.png'
        with Canvas(PLANE, xlim=(-0.3071312127620942, 12.825615244577339), ylim=(-5.812123793915195, 7.320622663424238)) as c:
            self._draw_base(c, hi={21: [({3, 5, 7, 8}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane293')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane293().draw(args.output, variant=args.variant))
