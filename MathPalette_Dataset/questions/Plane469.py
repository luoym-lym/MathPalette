"""Collected question Plane469; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane469:
    variants = ('C01',)

    def _draw_base(self, c):
        for object_id, vertices, codes in [('c00', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('c01', [[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79]), ('c02', [[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='c03', capstyle='butt', fill=False)
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c10', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('c11', [[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79]), ('c12', [[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79]), ('c13', [[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79]), ('c20', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('c21', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('c22', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='c23', capstyle='butt', fill=False)
        c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='c30', capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='c31', capstyle='butt', fill=False)
        c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='c32', capstyle='butt')
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', zorder=1, edgecolor='none', facecolor='black', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='c33', capstyle='butt', fill=False)
        c.text('A', (0.0, 4.0), id='nameA', fontsize=18.0, fontstyle='italic', offset_pt=(-15, 15))
        c.text('B', (4.0, 4.0), id='nameB', fontsize=18.0, fontstyle='italic', offset_pt=(15, 15))
        c.text('C', (4.0, 0.0), id='nameC', fontsize=18.0, fontstyle='italic', offset_pt=(15, -15))
        c.text('D', (0.0, 0.0), id='nameD', fontsize=18.0, fontstyle='italic', offset_pt=(-15, -15))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.3073701959163735, 4.300694539430536), ylim=(-0.29072218248826953, 4.31734255285864)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane469_C01.png'
        with Canvas(PLANE, xlim=(-0.3073701959163735, 4.300694539430536), ylim=(-0.29072218248826953, 4.31734255285864)) as c:
            self._draw_base(c)
            c.line([[4, 4], [0, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[3.497859731576999, 1.500361802676185]]), (None, [[2.5472581419731637, 3.4956839511515625]]), (None, [[1.535479222345319, 0.5074066769018817]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            for object_id, points in [(None, [[3.568448958527779, 2.4509633922800202]]), (None, [[1.5448911192720902, 3.4815661057614067]]), (None, [[0.5142884057907041, 1.4956558542127998]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane469')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane469().draw(args.output, variant=args.variant))
