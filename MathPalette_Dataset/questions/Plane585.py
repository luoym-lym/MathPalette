"""Collected question Plane585; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane585:
    variants = ('C01', 'C02', 'C03', 'C04')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907)) as c:
            for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
                c.line(points, id=object_id, zorder=1, color='#AAAAAA')
            c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
            c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
            for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
                c.circle(center, radius, id=object_id, zorder=4, fill=False)
            c.text('X', [3, 3], id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, 16), annotation_clip=False)
            c.text('Y', [5, 3], id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
            c.text('Z', [4, 4], id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
            c.text('T', [4, 3], id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -16), annotation_clip=False)
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
            c.line(points, id=object_id, zorder=1, color='#AAAAAA')
        c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
        c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
        for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
            c.circle(center, radius, id=object_id, zorder=4, fill=False)
        c.text('X', (3, 3), id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, 16), annotation_clip=False)
        c.text('Y', (5, 3), id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
        c.text('Z', (4, 4), id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 16), annotation_clip=False)
        c.text('T', (4, 3), id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -16), annotation_clip=False)
        c.point([[3.0, 3.0]], zorder=10, s=50, **_kw.get(8, {'facecolors': '#EA580C', 'edgecolors': '#EA580C'}))
        c.line([[3.0, 3.0], [4.0, 5.0]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(9, {'color': '#EA580C'}))
        c.line([[3.0, 3.0], [4.0, 1.0]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(10, {'color': '#EA580C'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane585_C01.png'
        with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907)) as c:
            self._draw_choices(c, kw={9: {'color': '#16A34A'}, 10: {'color': '#16A34A'}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane585_C02.png'
        with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane585_C03.png'
        with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907)) as c:
            self._draw_choices(c, kw={8: {'facecolors': '#DC2626', 'edgecolors': '#DC2626'}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane585_C04.png'
        with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-1.1860465116279073, 7.186046511627907)) as c:
            self._draw_choices(c, kw={9: {'color': '#2563EB'}, 10: {'color': '#2563EB'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane585')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane585().draw(args.output, variant=args.variant))
