"""Collected question Plane536; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane536:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c):
        for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
            c.circle(center, radius, id=object_id, zorder=3)
        c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
        c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
        c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor='black')
        c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor='black', capstyle='butt')
        c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
        c.text('A', (10, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, -15), annotation_clip=False)
        c.text('B', (10, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(16, 15), annotation_clip=False)
        c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, 15), annotation_clip=False)
        c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-16, -15), annotation_clip=False)
        c.text('45°', (2, 6), id='angle_label', clip_on=True, offset_pt=(65, -17), annotation_clip=False)
        c.text('P', (2, 6), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, 19), annotation_clip=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C01.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            c.line([[2, 6], [8, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[8, 0], [10, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[8.0, 0.0]], zorder=10, s=50, facecolors='#EA580C', edgecolors='#EA580C')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C02.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            c.line([[8, 0], [10, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C03.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            c.line([[2, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[8, 0], [10, 6]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[8.0, 0.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C04.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[2, 6], [8, 0]]), (None, [[8, 0], [10, 2]]), (None, [[10, 2], [0, 6]])]:
                c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[10.0, 2.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C05.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            c.line([[8, 0], [10, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane536_C06.png'
        with Canvas(PLANE, xlim=(-0.79232376, 10.775252), ylim=(-2.69842908, 8.86914668)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[2, 6], [8, 0]]), (None, [[8, 0], [10, 2]]), (None, [[10, 2], [0, 6]])]:
                c.line(points, id=object_id, zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[10.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane536')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane536().draw(args.output, variant=args.variant))
