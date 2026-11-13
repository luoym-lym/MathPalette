"""Collected question Plane586; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane586:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def _draw_base(self, c):
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 9]]), ('grid_vertical_1', [[1, 0], [1, 9]]), ('grid_vertical_2', [[2, 0], [2, 9]]), ('grid_vertical_3', [[3, 0], [3, 9]]), ('grid_vertical_4', [[4, 0], [4, 9]]), ('grid_vertical_5', [[5, 0], [5, 9]]), ('grid_vertical_6', [[6, 0], [6, 9]]), ('grid_vertical_7', [[7, 0], [7, 9]]), ('grid_vertical_8', [[8, 0], [8, 9]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]]), ('grid_horizontal_7', [[0, 7], [8, 7]]), ('grid_horizontal_8', [[0, 8], [8, 8]]), ('grid_horizontal_9', [[0, 9], [8, 9]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 3], [7, 3]], id='given_segment_AB', zorder=3)
        c.line([[4, 2], [4, 8]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 4], 0.05677688953488369), ('point_marker_Y', [5, 4], 0.05677688953488369), ('point_marker_Z', [4, 4], 0.05677688953488369), ('point_marker_T', [2, 6], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 4), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-14, 14), annotation_clip=False)
        c.text('Y', (5, 4), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(14, 14), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(14, -14), annotation_clip=False)
        c.text('T', (2, 6), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-14, 14), annotation_clip=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane586_C01.png'
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            c.point([[3.0, 4.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[3, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane586_C02.png'
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            c.point([[4.0, 4.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[4, 4], [1, 3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4, 4], [4, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane586_C03.png'
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            c.point([[4.0, 4.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane586_C04.png'
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane586_C05.png'
        with Canvas(PLANE, xlim=(-0.7093023255813948, 8.709302325581394), ylim=(-0.20930232558139483, 9.209302325581394)) as c:
            self._draw_base(c)
            c.point([[4.0, 4.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.line([[4, 4], [1, 3]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[4, 4], [4, 2]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane586')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane586().draw(args.output, variant=args.variant))
