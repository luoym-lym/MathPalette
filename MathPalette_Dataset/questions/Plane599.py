"""Collected question Plane599; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane599:
    variants = ('C01',)

    def __init__(self):
        self.points = {
            'I_point_1': [0.0, 0.0], 'I_point_2': [0.0, 1.3333333333333333], 'I_point_3': [0.0, 2.0],
            'I_point_4': [0.6666666666666666, 0.0], 'I_point_5': [1.3333333333333333, 2.0],
            'I_point_6': [2.0, 0.0], 'I_point_7': [2.0, 0.6666666666666666], 'I_point_8': [2.0, 2.0],
            'I_panel_anchor': [1.0, 2.58], 'II_point_1': [3.0, 0.0], 'II_point_2': [3.0, 1.3333333333333333],
            'II_point_3': [3.0, 2.0], 'II_point_4': [3.6666666666666665, 0.0],
            'II_point_5': [4.333333333333333, 2.0], 'II_point_6': [5.0, 0.0],
            'II_point_7': [5.0, 0.6666666666666666], 'II_point_8': [5.0, 2.0], 'II_panel_anchor': [4.0, 2.58],
            'III_point_1': [6.0, 0.0], 'III_point_2': [6.0, 2.0], 'III_point_3': [6.666666666666667, 0.0],
            'III_point_4': [8.0, 0.0], 'III_point_5': [8.0, 1.3333333333333333], 'III_point_6': [8.0, 2.0],
            'III_panel_anchor': [7.0, 2.58]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.57, 8.57), ylim=(-3.392, 5.748)) as c:
            c.fill([self.points['I_point_4'], self.points['I_point_7'], self.points['I_point_5']], facecolor='#E8E8E8', alpha=1, id='I_shade_4')
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_6']]), ('I_outer_BC', [self.points['I_point_6'], self.points['I_point_8']]), ('I_outer_CD', [self.points['I_point_8'], self.points['I_point_3']]), ('I_outer_DA', [self.points['I_point_3'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_4'], self.points['I_point_7']]), ('I_cut_2', [self.points['I_point_7'], self.points['I_point_5']]), ('I_cut_3', [self.points['I_point_5'], self.points['I_point_2']]), ('I_cut_4', [self.points['I_point_2'], self.points['I_point_4']]), ('I_cut_5', [self.points['I_point_4'], self.points['I_point_5']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_2'], self.points['II_point_5'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_2')
            c.fill([self.points['II_point_4'], self.points['II_point_6'], self.points['II_point_7']], facecolor='#E8E8E8', alpha=1, id='II_shade_3')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_6']]), ('II_outer_BC', [self.points['II_point_6'], self.points['II_point_8']]), ('II_outer_CD', [self.points['II_point_8'], self.points['II_point_3']]), ('II_outer_DA', [self.points['II_point_3'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_4'], self.points['II_point_7']]), ('II_cut_2', [self.points['II_point_7'], self.points['II_point_5']]), ('II_cut_3', [self.points['II_point_5'], self.points['II_point_2']]), ('II_cut_4', [self.points['II_point_2'], self.points['II_point_4']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_3'], self.points['III_point_4'], self.points['III_point_5']], facecolor='#E8E8E8', alpha=1, id='III_shade_1')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_4']]), ('III_outer_BC', [self.points['III_point_4'], self.points['III_point_6']]), ('III_outer_CD', [self.points['III_point_6'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_3'], self.points['III_point_5']])]:
                c.line(points, id=object_id)
            c.text('I', self.points['I_panel_anchor'], id='I_panel_label')
            c.text('P', self.points['I_point_4'], offset_pt=(0, -15), vertex=True, id='I_label_P')
            c.text('Q', self.points['I_point_7'], offset_pt=(13, 0), vertex=True, id='I_label_Q')
            c.text('R', self.points['I_point_5'], offset_pt=(0, 15), vertex=True, id='I_label_R')
            c.text('S', self.points['I_point_2'], offset_pt=(-13, 0), vertex=True, id='I_label_S')
            c.text('II', self.points['II_panel_anchor'], id='II_panel_label')
            c.text('P', self.points['II_point_4'], offset_pt=(0, -15), vertex=True, id='II_label_P')
            c.text('Q', self.points['II_point_7'], offset_pt=(13, 0), vertex=True, id='II_label_Q')
            c.text('R', self.points['II_point_5'], offset_pt=(0, 15), vertex=True, id='II_label_R')
            c.text('S', self.points['II_point_2'], offset_pt=(-13, 0), vertex=True, id='II_label_S')
            c.text('III', self.points['III_panel_anchor'], id='III_panel_label')
            c.text('U', self.points['III_point_3'], offset_pt=(0, -15), vertex=True, id='III_label_U')
            c.text('V', self.points['III_point_5'], offset_pt=(13, 0), vertex=True, id='III_label_V')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane599_C01.png'
        with Canvas(PLANE, xlim=(-0.57, 8.57), ylim=(-3.392, 5.748)) as c:
            c.path([[0.6666666666666666, 0.0], [2.0, 0.6666666666666666], [1.3333333333333333, 2.0], [0.6666666666666666, 0.0]], [1, 2, 2, 79], id='I_shade_4', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
            for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('I_cut_1', [[0.6666666666666666, 0.0], [2.0, 0.6666666666666666]]), ('I_cut_2', [[2.0, 0.6666666666666666], [1.3333333333333333, 2.0]]), ('I_cut_3', [[1.3333333333333333, 2.0], [0.0, 1.3333333333333333]]), ('I_cut_4', [[0.0, 1.3333333333333333], [0.6666666666666666, 0.0]])]:
                c.line(points, id=object_id, color='#DC2626')
            c.line([[0.6666666666666666, 0.0], [1.3333333333333333, 2.0]], id='I_cut_5')
            c.path([[3.0, 1.3333333333333333], [4.333333333333333, 2.0], [3.0, 2.0], [3.0, 1.3333333333333333]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
            c.path([[3.6666666666666665, 0.0], [5.0, 0.0], [5.0, 0.6666666666666666], [3.6666666666666665, 0.0]], [1, 2, 2, 79], id='II_shade_3', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
            for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('II_cut_1', [[3.6666666666666665, 0.0], [5.0, 0.6666666666666666]]), ('II_cut_2', [[5.0, 0.6666666666666666], [4.333333333333333, 2.0]]), ('II_cut_3', [[4.333333333333333, 2.0], [3.0, 1.3333333333333333]]), ('II_cut_4', [[3.0, 1.3333333333333333], [3.6666666666666665, 0.0]])]:
                c.line(points, id=object_id, color='#DC2626')
            c.path([[6.666666666666667, 0.0], [8.0, 0.0], [8.0, 1.3333333333333333], [6.666666666666667, 0.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor='#E8E8E8', linewidth=0.0, capstyle='butt')
            for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]])]:
                c.line(points, id=object_id, color='#DC2626')
            c.line([[6.666666666666667, 0.0], [8.0, 1.3333333333333333]], id='III_cut_1')
            c.text('I', (1.0, 2.58), id='I_panel_label', clip_on=True, offset_pt=(0, 0), annotation_clip=False)
            c.text('P', (0.6666666666666666, 0.0), id='I_label_P', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15), annotation_clip=False)
            c.text('Q', (2.0, 0.6666666666666666), id='I_label_Q', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(13, 0), annotation_clip=False)
            c.text('R', (1.3333333333333333, 2.0), id='I_label_R', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, 15), annotation_clip=False)
            c.text('S', (0.0, 1.3333333333333333), id='I_label_S', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-13, 0), annotation_clip=False)
            c.text('II', (4.0, 2.58), id='II_panel_label', clip_on=True, offset_pt=(0, 0), annotation_clip=False)
            c.text('P', (3.6666666666666665, 0.0), id='II_label_P', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15), annotation_clip=False)
            c.text('Q', (5.0, 0.6666666666666666), id='II_label_Q', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(13, 0), annotation_clip=False)
            c.text('R', (4.333333333333333, 2.0), id='II_label_R', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, 15), annotation_clip=False)
            c.text('S', (3.0, 1.3333333333333333), id='II_label_S', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(-13, 0), annotation_clip=False)
            c.text('III', (7.0, 2.58), id='III_panel_label', clip_on=True, offset_pt=(0, 0), annotation_clip=False)
            c.text('U', (6.666666666666667, 0.0), id='III_label_U', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15), annotation_clip=False)
            c.text('V', (8.0, 1.3333333333333333), id='III_label_V', clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(13, 0), annotation_clip=False)
            c.line([[6.666666666666667, 0.0], [8.0, 2.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane599')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane599().draw(args.output, variant=args.variant))
