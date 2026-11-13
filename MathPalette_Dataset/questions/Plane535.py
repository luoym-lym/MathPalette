"""Collected question Plane535; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane535:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c):
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[9.0, 0.21], [9.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [8.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [8.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [9.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [9.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [9.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [9.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [9.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [9, 0], 0.21), ('pocket_B', [9, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
        c.line([[0.0, 3.0], [2.6, 5.6]], id='outgoing_path')
        c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor='black')
        c.path([[2.6, 5.6], [2.324228355, 5.451507576], [2.451507576, 5.324228355], [2.6, 5.6]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor='black', capstyle='butt')
        c.path([[0.32582973051120945, 3.3258297305112094], [0.2830421623364028, 3.368617298686016], [0.23224243139867845, 3.4025605937106516], [0.17633777946435292, 3.4257170587415966], [0.12043312753002736, 3.4488735237725416], [0.060510759213775106, 3.460792823913323], [2.821542284377605e-17, 3.460792823913323]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (9, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (9, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (0, 3), id='angle_label', clip_on=True, offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
        c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-17, 0), annotation_clip=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C01.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [0, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C02.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [9, 4]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C03.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [9, 4]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            c.line([[9, 4], [3, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C04.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [9, 4]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            c.line([[9, 4], [3, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C05.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [9, 4]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.line([[9, 4], [3, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane535_C06.png'
        with Canvas(PLANE, xlim=(-0.71963068, 9.70400568), ylim=(-2.17275568, 8.25088068)) as c:
            self._draw_base(c)
            c.line([[0, 3], [3, 6]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [9, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            c.line([[9, 4], [3, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane535')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane535().draw(args.output, variant=args.variant))
