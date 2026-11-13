"""Collected question Plane588; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane588:
    variants = ('C01', 'C02', 'C03')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.20930232558139483, 9.209302325581394), ylim=(-0.7093023255813948, 8.709302325581394)) as c:
            for object_id, points in [('grid_vertical_0', [[0, 0], [0, 8]]), ('grid_vertical_1', [[1, 0], [1, 8]]), ('grid_vertical_2', [[2, 0], [2, 8]]), ('grid_vertical_3', [[3, 0], [3, 8]]), ('grid_vertical_4', [[4, 0], [4, 8]]), ('grid_vertical_5', [[5, 0], [5, 8]]), ('grid_vertical_6', [[6, 0], [6, 8]]), ('grid_vertical_7', [[7, 0], [7, 8]]), ('grid_vertical_8', [[8, 0], [8, 8]]), ('grid_vertical_9', [[9, 0], [9, 8]]), ('grid_horizontal_0', [[0, 0], [9, 0]]), ('grid_horizontal_1', [[0, 1], [9, 1]]), ('grid_horizontal_2', [[0, 2], [9, 2]]), ('grid_horizontal_3', [[0, 3], [9, 3]]), ('grid_horizontal_4', [[0, 4], [9, 4]]), ('grid_horizontal_5', [[0, 5], [9, 5]]), ('grid_horizontal_6', [[0, 6], [9, 6]]), ('grid_horizontal_7', [[0, 7], [9, 7]]), ('grid_horizontal_8', [[0, 8], [9, 8]])]:
                c.line(points, id=object_id, zorder=1, color='#AAAAAA')
            c.line([[1, 1], [6, 1]], id='given_segment_AB', zorder=3)
            c.line([[5, 3], [8, 7]], id='given_segment_CD', zorder=3)
            for object_id, center, radius in [('point_marker_X', [6, 2], 0.05677688953488369), ('point_marker_Y', [3, 4], 0.05677688953488369), ('point_marker_Z', [1, 6], 0.05677688953488369), ('point_marker_T', [5, 4], 0.05677688953488369)]:
                c.circle(center, radius, id=object_id, zorder=4, fill=False)
            c.text('X', [6, 2], id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -16), annotation_clip=False)
            for object_id, text, anchor in [('label_Y', 'Y', (3, 4)), ('label_Z', 'Z', (1, 6)), ('label_T', 'T', (5, 4))]:
                c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
            return c.save(output_path)

    def _draw_choices(self, c, kw=None, custom=None):
        _kw = kw or {}
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 8]]), ('grid_vertical_1', [[1, 0], [1, 8]]), ('grid_vertical_2', [[2, 0], [2, 8]]), ('grid_vertical_3', [[3, 0], [3, 8]]), ('grid_vertical_4', [[4, 0], [4, 8]]), ('grid_vertical_5', [[5, 0], [5, 8]]), ('grid_vertical_6', [[6, 0], [6, 8]]), ('grid_vertical_7', [[7, 0], [7, 8]]), ('grid_vertical_8', [[8, 0], [8, 8]]), ('grid_vertical_9', [[9, 0], [9, 8]]), ('grid_horizontal_0', [[0, 0], [9, 0]]), ('grid_horizontal_1', [[0, 1], [9, 1]]), ('grid_horizontal_2', [[0, 2], [9, 2]]), ('grid_horizontal_3', [[0, 3], [9, 3]]), ('grid_horizontal_4', [[0, 4], [9, 4]]), ('grid_horizontal_5', [[0, 5], [9, 5]]), ('grid_horizontal_6', [[0, 6], [9, 6]]), ('grid_horizontal_7', [[0, 7], [9, 7]]), ('grid_horizontal_8', [[0, 8], [9, 8]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 1], [6, 1]], id='given_segment_AB', zorder=3)
        c.line([[5, 3], [8, 7]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [6, 2], 0.05677688953488369), ('point_marker_Y', [3, 4], 0.05677688953488369), ('point_marker_Z', [1, 6], 0.05677688953488369), ('point_marker_T', [5, 4], 0.05677688953488369)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (6, 2), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -16), annotation_clip=False)
        for object_id, text, anchor in [('label_Y', 'Y', (3, 4)), ('label_Z', 'Z', (1, 6)), ('label_T', 'T', (5, 4))]:
            c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
        if custom and 6 in custom:
            custom[6](c)
        else:
            c.point([[6.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
        c.line([[6, 2], [5, 3]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(7, {'color': '#DC2626'}))
        c.line([[6, 2], [6, 1]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(8, {'color': '#DC2626'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane588_C01.png'
        with Canvas(PLANE, xlim=(-0.20930232558139483, 9.209302325581394), ylim=(-0.7093023255813948, 8.709302325581394)) as c:

            def _slot_6(c):
                pass
            self._draw_choices(c, custom={6: _slot_6}, kw={7: {'color': '#2563EB'}, 8: {'color': '#2563EB'}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane588_C02.png'
        with Canvas(PLANE, xlim=(-0.20930232558139483, 9.209302325581394), ylim=(-0.7093023255813948, 8.709302325581394)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane588_C03.png'
        with Canvas(PLANE, xlim=(-0.20930232558139483, 9.209302325581394), ylim=(-0.7093023255813948, 8.709302325581394)) as c:
            self._draw_choices(c, kw={7: {'color': '#EA580C'}, 8: {'color': '#EA580C'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane588')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane588().draw(args.output, variant=args.variant))
