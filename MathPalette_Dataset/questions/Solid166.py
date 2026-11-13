"""Collected question Solid166; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid166:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        c.path([[0.0, 0.8660254037844386], [1.0, 0.8660254037844386], [0.5, 0.0], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface0', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('netedge0', [[0.0, 0.8660254037844386], [1.0, 0.8660254037844386]]), ('netedge1', [[1.0, 0.8660254037844386], [0.5, 0.0]]), ('netedge2', [[0.5, 0.0], [0.0, 0.8660254037844386]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[0.5, 0.0], [1.0, 0.8660254037844386], [1.5, 0.0], [0.5, 0.0]], [1, 2, 2, 79], id='netface1', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [1.5, 0.0]], id='netedge3', zorder=3, clip_on=False)
        c.line([[1.5, 0.0], [0.5, 0.0]], id='netedge4', zorder=3, clip_on=False)
        c.path([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386], [1.5, 0.0], [1.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface2', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[1.0, 0.8660254037844386], [2.0, 0.8660254037844386]], id='netedge5', zorder=3, clip_on=False)
        c.line([[2.0, 0.8660254037844386], [1.5, 0.0]], id='netedge6', zorder=3, clip_on=False)
        c.path([[1.5, 0.0], [2.0, 0.8660254037844386], [2.5, 0.0], [1.5, 0.0]], [1, 2, 2, 79], id='netface3', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [2.5, 0.0]], id='netedge7', zorder=3, clip_on=False)
        c.line([[2.5, 0.0], [1.5, 0.0]], id='netedge8', zorder=3, clip_on=False)
        c.path([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386], [2.5, 0.0], [2.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface4', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[2.0, 0.8660254037844386], [3.0, 0.8660254037844386]], id='netedge9', zorder=3, clip_on=False)
        c.line([[3.0, 0.8660254037844386], [2.5, 0.0]], id='netedge10', zorder=3, clip_on=False)
        c.path([[2.5, 0.0], [3.0, 0.8660254037844386], [3.5, 0.0], [2.5, 0.0]], [1, 2, 2, 79], id='netface5', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[3.0, 0.8660254037844386], [3.5, 0.0]], id='netedge11', zorder=3, clip_on=False)
        c.line([[3.5, 0.0], [2.5, 0.0]], id='netedge12', zorder=3, clip_on=False, **_kw.get(16, {}))
        c.path([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772], [1.0, 0.8660254037844386], [0.0, 0.8660254037844386]], [1, 2, 2, 79], id='netface6', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.line([[0.0, 0.8660254037844386], [0.5, 1.7320508075688772]], id='netedge13', zorder=3, clip_on=False, **_kw.get(18, {}))
        c.line([[0.5, 1.7320508075688772], [1.0, 0.8660254037844386]], id='netedge14', zorder=3, clip_on=False, **_kw.get(19, {}))
        c.path([[2.5, 0.0], [3.5, 0.0], [3.0, -0.8660254037844386], [2.5, 0.0]], [1, 2, 2, 79], id='netface7', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        _ov = {j: s for idxs, s in _hi.get(21, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('netedge15', [[3.5, 0.0], [3.0, -0.8660254037844386]]), ('netedge16', [[3.0, -0.8660254037844386], [2.5, 0.0]]), ('octa0-11-1', [[4.014935923627798, 0.4780638448170429], [5.14974038854417, 0.10957436788638075]]), ('octa1-12-1', [[5.14974038854417, 0.10957436788638075], [5.35, -0.8805408353447026]]), ('octa0-12-1', [[4.014935923627798, 0.4780638448170429], [5.35, -0.8805408353447026]]), ('octa1-121', [[5.14974038854417, 0.10957436788638075], [5.35, 1.7405408353447025]]), ('octa0-121', [[4.014935923627798, 0.4780638448170429], [5.35, 1.7405408353447025]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, points in [('octa0-111', [[4.014935923627798, 0.4780638448170429], [5.55025961145583, 0.7504256321136192]]), ('octa112-1', [[5.55025961145583, 0.7504256321136192], [5.35, -0.8805408353447026]]), ('octa1121', [[5.55025961145583, 0.7504256321136192], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('octa011-1', [[6.685064076372202, 0.3819361551829571], [5.14974038854417, 0.10957436788638075]]), ('octa012-1', [[6.685064076372202, 0.3819361551829571], [5.35, -0.8805408353447026]]), ('octa0121', [[6.685064076372202, 0.3819361551829571], [5.35, 1.7405408353447025]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[6.685064076372202, 0.3819361551829571], [5.55025961145583, 0.7504256321136192]], id='octa0111', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.text('3', (0.25, 1.299038105676658), id='edge_label3', offset_pt=(-14, 4))
        c.text('4', (0.25, 0.4330127018922193), id='edge_label4', offset_pt=(-14, -4))
        c.text('5', (1.0, 0.0), id='edge_label5', offset_pt=(0, -17))
        c.text('2', (2.5, 0.8660254037844386), id='edge_label2', offset_pt=(0, 18))
        c.text('1', (3.25, 0.4330127018922193), id='edge_label1', offset_pt=(16, 4))
        c.text('x', (3.25, -0.4330127018922193), id='edge_labelx', offset_pt=(17, -3))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid166_C01.png'
        with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446)) as c:
            self._draw_base(c, hi={1: [({2}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'})], 21: [({0}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid166_C02.png'
        with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446)) as c:
            self._draw_base(c, hi={1: [({2}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'})], 21: [({0}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({1}, {'color': '#2563EB'})]}, kw={18: {'color': '#2563EB'}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid166_C03.png'
        with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446)) as c:
            self._draw_base(c, hi={21: [({0}, {'color': '#DC2626'}), ({1}, {'color': '#2563EB'})]}, kw={18: {'color': '#DC2626'}, 19: {'color': '#2563EB'}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid166_C04.png'
        with Canvas(SOLID, xlim=(-0.17034455212169997, 6.856642330527192), ylim=(-3.0834934413244457, 3.943493441324446)) as c:
            self._draw_base(c, hi={1: [({0}, {'color': '#EA580C'})], 21: [({1}, {'color': '#16A34A'})]}, kw={16: {'color': '#EA580C'}, 19: {'color': '#16A34A'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid166')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Solid166().draw(args.output, variant=args.variant))
