"""Collected question Solid203; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid203:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, vertices, codes in [('face40', [[5.528452523744346, -0.5562422413460985], [5.40952674073674, 0.065], [6.445253957014124, 0.35], [5.528452523744346, -0.5562422413460985]], [1, 2, 2, 79]), ('face39', [[5.528452523744346, -0.5562422413460985], [4.554746042985876, 0.35], [5.40952674073674, 0.065], [5.528452523744346, -0.5562422413460985]], [1, 2, 2, 79]), ('face38', [[5.471547476255654, 1.2562422413460985], [5.40952674073674, 0.065], [6.445253957014124, 0.35], [5.471547476255654, 1.2562422413460985]], [1, 2, 2, 79]), ('face37', [[5.471547476255654, 1.2562422413460985], [4.554746042985876, 0.35], [5.40952674073674, 0.065], [5.471547476255654, 1.2562422413460985]], [1, 2, 2, 79]), ('face7', [[2.0, 0.0], [3.0, 0.0], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79]), ('face6', [[2.0, 0.0], [2.5, 0.8660254037844386], [3.0, 0.0], [2.0, 0.0]], [1, 2, 2, 79]), ('face5', [[1.5, 0.8660254037844386], [2.0, 0.0], [2.5, 0.8660254037844386], [1.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face4', [[1.0, 0.0], [1.5, 0.8660254037844386], [2.0, 0.0], [1.0, 0.0]], [1, 2, 2, 79]), ('face3', [[0.5, 0.8660254037844386], [1.0, 0.0], [1.5, 0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face2', [[0.5, 0.8660254037844386], [0.0, 0.0], [1.0, 0.0], [0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face1', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386], [0.0, 0.0], [-0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face0', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772], [0.5, 0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        _defs = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {'color': '#DC2626'}, {}, {}, {}, {}]
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('line_8', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]]), ('line_9', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('line_10', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('line_11', [[0.0, 0.0], [1.0, 0.0]]), ('line_12', [[2.0, 0.0], [3.0, 0.0]]), ('line_13', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('line_14', [[1.0, 0.0], [2.0, 0.0]]), ('line_15', [[1.5, 0.8660254037844386], [2.5, 0.8660254037844386]]), ('line_16', [[0.5, 0.8660254037844386], [0.0, 0.0]]), ('line_17', [[2.0, 0.0], [2.5, 0.8660254037844386]]), ('line_18', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('line_19', [[1.0, 0.0], [1.5, 0.8660254037844386]]), ('line_20', [[3.0, 0.0], [2.5, -0.8660254037844386]]), ('line_21', [[1.5, 0.8660254037844386], [2.0, 0.0]]), ('line_22', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('line_23', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('line_24', [[2.5, 0.8660254037844386], [3.0, 0.0]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov.get(i, _defs[i]))
        c.line([[6.445253957014124, 0.35], [5.59047325926326, 0.635]], id='line_25', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_26', [[6.445253957014124, 0.35], [5.40952674073674, 0.065]]), ('line_27', [[6.445253957014124, 0.35], [5.471547476255654, 1.2562422413460985]]), ('line_28', [[6.445253957014124, 0.35], [5.528452523744346, -0.5562422413460985]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[4.554746042985876, 0.35], [5.59047325926326, 0.635]], id='line_29', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        for object_id, points in [('line_30', [[4.554746042985876, 0.35], [5.40952674073674, 0.065]]), ('line_31', [[4.554746042985876, 0.35], [5.471547476255654, 1.2562422413460985]]), ('line_32', [[4.554746042985876, 0.35], [5.528452523744346, -0.5562422413460985]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[5.59047325926326, 0.635], [5.471547476255654, 1.2562422413460985]], id='line_33', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[5.59047325926326, 0.635], [5.528452523744346, -0.5562422413460985]], id='line_34', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[5.40952674073674, 0.065], [5.471547476255654, 1.2562422413460985]], id='line_35', zorder=3, clip_on=False)
        c.line([[5.40952674073674, 0.065], [5.528452523744346, -0.5562422413460985]], id='line_36', zorder=3, clip_on=False)
        c.text('C', (-0.25, 1.299038105676658), id='label_0', offset_pt=(-18, 6))
        c.text('D', (-0.25, 0.4330127018922193), id='label_1', offset_pt=(-18, 0))
        c.text('E', (0.5, 0.0), id='label_2', offset_pt=(0, -18))
        c.text('B', (2.0, 0.8660254037844386), id='label_3', offset_pt=(0, 18))
        c.text('A', (2.75, 0.4330127018922193), id='label_4', offset_pt=(18, 3))
        c.text('x', (2.75, -0.4330127018922193), id='label_5', offset_pt=(18, -3))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583)) as c:
            self._draw_base(c, hi={1: [({12}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid203_C01.png'
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583)) as c:
            self._draw_base(c, hi={1: [({0}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid203_C02.png'
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583)) as c:
            self._draw_base(c, hi={1: [({7, 12}, {'color': '#DC2626', 'linewidth': 2.0, 'solid_capstyle': 'butt'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid203_C03.png'
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583)) as c:
            self._draw_base(c, hi={1: [({7, 12}, {'color': '#EA580C', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({9}, {'color': '#2563EB', 'linewidth': 1.5, 'solid_capstyle': 'butt'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid203_C04.png'
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583)) as c:
            self._draw_base(c, hi={1: [({0}, {'color': '#DC2626'}), ({2, 15}, {'color': '#2563EB'}), ({4, 10}, {'color': '#16A34A'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid203')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Solid203().draw(args.output, variant=args.variant))
