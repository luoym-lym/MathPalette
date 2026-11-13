"""Collected question Plane558; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane558:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 5.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 5.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 5.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_row_3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_row_4', [[0.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
                c.line(points, id=object_id, zorder=3)
            c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round')
            c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor='black', joinstyle='round')
            c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, offset_pt=(-15, 0))
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, offset_pt=(0, -15))
            c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, offset_pt=(0, 15))
            c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, offset_pt=(-15, 0))
            c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, offset_pt=(0, 15))
            return c.save(output_path)

    def _draw_choices(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 5.0]]), ('boundary_3', [[4.0, 5.0], [0.0, 5.0]]), ('boundary_4', [[0.0, 5.0], [0.0, 0.0]])]:
            c.line(points, id=object_id, zorder=3)
        _defs = [
            {'color': '#999999'}, {'color': '#999999'}, {'color': '#999999'}, {'color': '#999999'},
            {'color': '#2563EB', 'linewidth': 1.5}, {'color': '#999999'}, {'color': '#999999'}
        ]
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('grid_column_1', [[1.0, 0.0], [1.0, 5.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 5.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 5.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_row_3', [[0.0, 3.0], [4.0, 3.0]]), ('grid_row_4', [[0.0, 4.0], [4.0, 4.0]])]):
            c.line(points, id=object_id, zorder=1, linestyle=(0.0, [4.0, 3.0]), **_ov.get(i, _defs[i]))
        for object_id, points in [('mirror_c1_r3', [[0.66, 2.66], [1.34, 3.34]]), ('mirror_c1_r4', [[0.66, 4.34], [1.34, 3.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c2_r3', [[1.66, 3.34], [2.34, 2.66]]), ('mirror_c2_r4', [[1.66, 4.34], [2.34, 3.66]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 1.66], [3.34, 2.34]]), ('mirror_c3_r3', [[2.66, 3.34], [3.34, 2.66]]), ('mirror_c3_r4', [[2.66, 3.66], [3.34, 4.34]])]:
            c.line(points, id=object_id, zorder=3)
        c.path([[681.5065294454746, 321.74616905140124], [607.1790738774332, 321.74616905140124], [534.4044432937667, 321.74616905140124]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round')
        c.path([[541.0711099604333, 318.4128357180679], [534.4044432937667, 321.74616905140124], [541.0711099604333, 325.07950238473455], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor='black', joinstyle='round')
        c.text('A', (0, 2), id='exit_label_A', fontsize=18.0, offset_pt=(-15, 0))
        c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, offset_pt=(0, -15))
        c.text('C', (3, 5), id='exit_label_C', fontsize=18.0, offset_pt=(0, 15))
        c.text('D', (0, 4), id='exit_label_D', fontsize=18.0, offset_pt=(-15, 0))
        c.text('E', (1, 5), id='exit_label_E', fontsize=18.0, offset_pt=(0, 15))
        c.point([[3.0, 5.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C01.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({2}, {'color': '#2563EB', 'linewidth': 1.5}), ({4}, {'color': '#2563EB', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C02.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({0}, {'color': '#2563EB', 'linewidth': 3.0})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C03.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({2}, {'color': '#EA580C', 'linewidth': 1.5}), ({4}, {'color': '#EA580C', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C04.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({0}, {'color': '#16A34A', 'linewidth': 3.0}), ({4}, {'color': '#16A34A', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C05.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({2}, {'color': '#2563EB', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane558_C06.png'
        with Canvas(PLANE, xlim=(-0.6444517387143618, 5.121170086019016), ylim=(-0.3635226508063538, 5.402099173927024)) as c:
            self._draw_choices(c, hi={1: [({2}, {'color': '#EA580C', 'linewidth': 2.0}), ({4}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane558')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane558().draw(args.output, variant=args.variant))
