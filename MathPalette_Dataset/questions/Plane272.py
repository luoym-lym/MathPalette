"""Collected question Plane272; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane272:
    variants = ('C01', 'C02')

    def _draw_base(self, c, kw=None):
        _kw = kw or {}
        c.path([[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79], id='tile0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79], id='tile0', capstyle='butt', fill=False)
        c.path([[2.0, 7.0], [3.0, 7.0], [3.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='tile1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 7.0], [3.0, 7.0], [3.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='tile1', capstyle='butt', fill=False)
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='tile2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='tile2', capstyle='butt', fill=False)
        c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='tile3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='tile3', capstyle='butt', fill=False)
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='board00', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='board00', capstyle='butt', fill=False, **_kw.get(9, {}))
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='board01', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='board01', capstyle='butt', fill=False)
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='board02', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='board02', capstyle='butt', fill=False, **_kw.get(13, {}))
        c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='board03', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='board03', capstyle='butt', fill=False)
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='board10', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='board10', capstyle='butt', fill=False, **_kw.get(17, {}))
        c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='board11', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='board11', capstyle='butt', fill=False, **_kw.get(19, {}))
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='board12', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='board12', capstyle='butt', fill=False, **_kw.get(21, {}))
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='board13', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='board13', capstyle='butt', fill=False, **_kw.get(23, {}))
        c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='board20', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='board20', capstyle='butt', fill=False, **_kw.get(25, {}))
        c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='board21', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='board21', capstyle='butt', fill=False)
        c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='board22', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='board22', capstyle='butt', fill=False, **_kw.get(29, {}))
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='board23', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='board23', capstyle='butt', fill=False)
        c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='board30', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='board30', capstyle='butt', fill=False)
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='board31', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='board31', capstyle='butt', fill=False, **_kw.get(35, {}))
        c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='board32', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='board32', capstyle='butt', fill=False, **_kw.get(37, {}))
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='board33', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='board33', capstyle='butt', fill=False, **_kw.get(39, {}))
        c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='board40', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='board40', capstyle='butt', fill=False)
        c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='board41', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='board41', capstyle='butt', fill=False)
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='board42', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='board42', capstyle='butt', fill=False, **_kw.get(45, {}))
        c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='board43', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='board43', capstyle='butt', fill=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.698234308178546, 6.714686156125894), ylim=(-0.21450330891172031, 8.19841715539272)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane272_C01.png'
        with Canvas(PLANE, xlim=(-1.698234308178546, 6.714686156125894), ylim=(-0.21450330891172031, 8.19841715539272)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[1.5115972741990462, 3.5108258509355075]]), (None, [[1.537372153072528, 2.4884223222873985]]), (None, [[0.43764398780397373, 2.4540558171227556]]), (None, [[2.4996342976825128, 2.36813955421115]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            for object_id, points in [(None, [[3.5134462000394606, 3.424909588023901]]), (None, [[3.522037826330622, 2.4798306959962373]]), (None, [[3.4876713211659798, 1.3629192781453625]]), (None, [[4.527258102396409, 2.4970139485785587]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            for object_id, points in [(None, [[1.5287805267813668, 1.4230606621834871]]), (None, [[0.5063769981332582, 0.47798177015582155]]), (None, [[1.57173865823717, 0.46939014386466305]]), (None, [[2.5511840554294754, 0.43502363870002014]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane272_C02.png'
        with Canvas(PLANE, xlim=(-1.698234308178546, 6.714686156125894), ylim=(-0.21450330891172031, 8.19841715539272)) as c:
            self._draw_base(c, kw={9: {'edgecolor': '#16A34A', 'linewidth': 1.5}, 13: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 17: {'edgecolor': '#16A34A', 'linewidth': 1.5}, 19: {'edgecolor': '#16A34A', 'linewidth': 1.5}, 21: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 23: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 25: {'edgecolor': '#16A34A'}, 29: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 35: {'edgecolor': '#2563EB', 'linewidth': 1.5}, 37: {'edgecolor': '#2563EB', 'linewidth': 1.5}, 39: {'edgecolor': '#2563EB', 'linewidth': 1.5}, 45: {'edgecolor': '#2563EB', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane272')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane272().draw(args.output, variant=args.variant))
