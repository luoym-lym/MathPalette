"""Collected question Plane597; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane597:
    variants = ('C01', 'C02')

    def __init__(self):
        self.points = {
            'I_point_1': [0.0, 0.0], 'I_point_2': [0.0, 2.0],
            'I_point_3': [0.6666666666666666, 1.3333333333333333], 'I_point_4': [1.0, 2.0],
            'I_point_5': [2.0, 0.0], 'I_point_6': [2.0, 2.0], 'I_panel_anchor': [1.0, 2.25],
            'II_point_1': [3.0, 0.0], 'II_point_2': [3.0, 2.0],
            'II_point_3': [4.333333333333333, 0.6666666666666666], 'II_point_4': [5.0, 0.0],
            'II_point_5': [5.0, 1.0], 'II_point_6': [5.0, 2.0], 'II_panel_anchor': [4.0, 2.25],
            'III_point_1': [6.0, 0.0], 'III_point_2': [6.0, 2.0], 'III_point_3': [6.8, 0.4],
            'III_point_4': [7.0, 0.0], 'III_point_5': [8.0, 0.0], 'III_point_6': [8.0, 1.0],
            'III_point_7': [8.0, 2.0], 'III_panel_anchor': [7.0, 2.25]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383)) as c:
            c.fill([self.points['I_point_1'], self.points['I_point_5'], self.points['I_point_3']], facecolor='#E8E8E8', alpha=1, id='I_shade_1')
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_5']]), ('I_outer_BC', [self.points['I_point_5'], self.points['I_point_6']]), ('I_outer_CD', [self.points['I_point_6'], self.points['I_point_2']]), ('I_outer_DA', [self.points['I_point_2'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_1'], self.points['I_point_4']]), ('I_cut_2', [self.points['I_point_5'], self.points['I_point_2']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_1'], self.points['II_point_4'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_1')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_4']]), ('II_outer_BC', [self.points['II_point_4'], self.points['II_point_6']]), ('II_outer_CD', [self.points['II_point_6'], self.points['II_point_2']]), ('II_outer_DA', [self.points['II_point_2'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_1'], self.points['II_point_5']]), ('II_cut_2', [self.points['II_point_4'], self.points['II_point_2']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_1'], self.points['III_point_3'], self.points['III_point_2']], facecolor='#E8E8E8', alpha=1, id='III_shade_0')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_5']]), ('III_outer_BC', [self.points['III_point_5'], self.points['III_point_7']]), ('III_outer_CD', [self.points['III_point_7'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_1'], self.points['III_point_6']]), ('III_cut_2', [self.points['III_point_2'], self.points['III_point_4']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('I_panel_label', 'I', self.points['I_panel_anchor']), ('II_panel_label', 'II', self.points['II_panel_anchor']), ('III_panel_label', 'III', self.points['III_panel_anchor'])]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def _draw_choices(self, c, custom=None):
        c.path([[0.0, 0.0], [2.0, 0.0], [0.6666666666666666, 1.3333333333333333], [0.0, 0.0]], [1, 2, 2, 79], id='I_shade_1', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[0.0, 0.0], [1.0, 2.0]]), ('I_cut_2', [[2.0, 0.0], [0.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[3.0, 0.0], [5.0, 0.0], [4.333333333333333, 0.6666666666666666], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_1', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [5.0, 1.0]]), ('II_cut_2', [[5.0, 0.0], [3.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, 0.0], [6.8, 0.4], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 79], id='III_shade_0', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
        if custom and 5 in custom:
            custom[5](c)
        else:
            for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 0.0], [8.0, 1.0]]), ('III_cut_2', [[6.0, 2.0], [7.0, 0.0]])]:
                c.line(points, id=object_id)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, offset_pt=(0, 0), annotation_clip=False)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane597_C01.png'
        with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383)) as c:
            self._draw_choices(c)
            for object_id, points in [(None, [[0.0, 1.3333333333333333], [2.0, 1.3333333333333333]]), (None, [[3.0, 0.6666666666666666], [5.0, 0.6666666666666666]]), (None, [[6.0, 0.4], [8.0, 0.4]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane597_C02.png'
        with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383)) as c:

            def _slot_5(c):
                c.path([[6.0, -4.440892098500626e-16], [7.0, -4.440892098500626e-16]], [1, 2], id='III_outer_AB', edgecolor='#DC2626', joinstyle='round', fill=False)
                c.path([[7.0, -4.440892098500626e-16], [8.0, -4.440892098500626e-16]], [1, 2], id='III_outer_AB', joinstyle='round', fill=False)
                for object_id, points in [('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]])]:
                    c.line(points, id=object_id)
                c.path([[6.0, -4.440892098500626e-16], [6.8, 0.3999999999999996]], [1, 2], id='III_cut_1', edgecolor='#DC2626', joinstyle='round', fill=False)
                c.path([[6.8, 0.3999999999999996], [8.0, 0.9999999999999996]], [1, 2], id='III_cut_1', joinstyle='round', fill=False)
                c.path([[6.0, 1.9999999999999996], [6.800000000000001, 0.39999999999999947]], [1, 2], id='III_cut_2', joinstyle='round', fill=False)
                c.path([[6.800000000000001, 0.39999999999999947], [7.0, -4.440892098500626e-16]], [1, 2], id='III_cut_2', edgecolor='#DC2626', joinstyle='round', fill=False)
            self._draw_choices(c, custom={5: _slot_5})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane597')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane597().draw(args.output, variant=args.variant))
