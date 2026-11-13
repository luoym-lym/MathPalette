"""Collected question Plane537; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane537:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c):
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 7.79]]), ('rail_right_0', [[12.0, 0.21], [12.0, 7.79]]), ('rail_bottom_0', [[0.21, 0.0], [5.79, 0.0]]), ('rail_bottom_1', [[6.21, 0.0], [11.79, 0.0]]), ('rail_top_0', [[0.21, 8.0], [11.79, 8.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 8.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 8.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 8.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 8.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 8.0]]), ('grid_v_6', [[6.0, 0.21], [6.0, 8.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 8.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 8.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 8.0]]), ('grid_v_10', [[10.0, 0.0], [10.0, 8.0]]), ('grid_v_11', [[11.0, 0.0], [11.0, 8.0]]), ('grid_h_1', [[0.0, 1.0], [12.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [12.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [12.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [12.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [12.0, 5.0]]), ('grid_h_6', [[0.0, 6.0], [12.0, 6.0]]), ('grid_h_7', [[0.0, 7.0], [12.0, 7.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [12, 0], 0.21), ('pocket_B', [12, 8], 0.21), ('pocket_C', [0, 8], 0.21), ('pocket_D', [0, 0], 0.21), ('pocket_E', [6.0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[1.3, 0.7], [0.0, 2.0]], id='incoming_path')
        c.line([[0.0, 2.0], [2.7, 4.7]], id='outgoing_path')
        c.circle([1.3, 0.7], 0.09, id='ball_symbol', zorder=4, facecolor='black')
        c.path([[2.7, 4.7], [2.424228355, 4.551507576], [2.551507576, 4.424228355], [2.7, 4.7]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor='black', capstyle='butt')
        c.path([[0.3137240734431056, 2.3137240734431055], [0.2725262055890451, 2.354921941297166], [0.22361385343937426, 2.3876041301339623], [0.16978624506938783, 2.409900255550918], [0.1159586366994014, 2.432196380967874], [0.05826258346006693, 2.443672839506173], [2.7167126138492594e-17, 2.443672839506173]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (12, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (12, 8), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 8), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, -15), annotation_clip=False)
        c.text('E', (6.0, 0), id='label_E', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -20), annotation_clip=False)
        c.text('45°', (0, 2), id='angle_label', clip_on=True, offset_pt=(17, 55), annotation_clip=False)
        c.text('P', (0, 2), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-17, 0), annotation_clip=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C01.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [6, 8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 8], [12, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[6.0, 8.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C02.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [12, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C03.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [12, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C04.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [6, 8]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 8], [12, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C05.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [6, 8]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 8], [12, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[6.0, 8.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane537_C06.png'
        with Canvas(PLANE, xlim=(-0.9, 12.9), ylim=(-2.9, 10.9)) as c:
            self._draw_base(c)
            c.line([[0, 2], [6, 8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[6, 8], [12, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[6.0, 8.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane537')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane537().draw(args.output, variant=args.variant))
