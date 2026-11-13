"""Collected question Plane307; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane307:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
        _ov = {j: s for idxs, s in _hi.get(6, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C01.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759)) as c:
            self._draw_base(c, hi={6: [({2, 7}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C02.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759)) as c:
            self._draw_base(c)
            c.line([[0, 6], [6, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 6], [0, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C03.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759)) as c:
            self._draw_base(c)
            c.line([[6, 6], [0, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0, 6], [6, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane307_C04.png'
        with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759)) as c:
            self._draw_base(c)
            c.line([[0, 3], [6, 3]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[3, 6], [3, 0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane307')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane307().draw(args.output, variant=args.variant))
