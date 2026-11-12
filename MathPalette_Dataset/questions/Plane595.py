"""Collected question Plane595; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane595:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane595'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane456/extension_01'
        self.question = 'Each of the three large squares shown below is the same size. Where a segment meets a side of a square, or a side of the inner diamond in I, it meets that side at its midpoint. How do the shaded areas of these squares compare?\n\nChoices:\nA: $S_{I} = S_{II} = S_{III}$\nB: $S_{I} < S_{II} < S_{III}$\nC: $S_{II} < S_{I} < S_{III}$\nD: $S_{I} = S_{II} < S_{III}$\nE: $S_{III} < S_{II} < S_{I}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$S_{I} = S_{II} = S_{III}$',
         'B': '$S_{I} < S_{II} < S_{III}$',
         'C': '$S_{II} < S_{I} < S_{III}$',
         'D': '$S_{I} = S_{II} < S_{III}$',
         'E': '$S_{III} < S_{II} < S_{I}$'}
        self.query = self.question
        self.points = {'I_point_1': [0.0, 0.0],
         'I_point_2': [0.0, 1.0],
         'I_point_3': [0.0, 2.0],
         'I_point_4': [0.5, 0.5],
         'I_point_5': [0.5, 1.5],
         'I_point_6': [1.0, 0.0],
         'I_point_7': [1.0, 2.0],
         'I_point_8': [1.5, 0.5],
         'I_point_9': [1.5, 1.5],
         'I_point_10': [2.0, 0.0],
         'I_point_11': [2.0, 1.0],
         'I_point_12': [2.0, 2.0],
         'I_panel_anchor': [1.0, 2.25],
         'II_point_1': [3.0, 0.0],
         'II_point_2': [3.0, 2.0],
         'II_point_3': [4.0, 2.0],
         'II_point_4': [5.0, 0.0],
         'II_point_5': [5.0, 1.0],
         'II_point_6': [5.0, 2.0],
         'II_panel_anchor': [4.0, 2.25],
         'III_point_1': [6.0, 0.0],
         'III_point_2': [6.0, 2.0],
         'III_point_3': [7.0, 0.0],
         'III_point_4': [8.0, 0.0],
         'III_point_5': [8.0, 2.0],
         'III_panel_anchor': [7.0, 2.25]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.205, 8.205], ylim=[-3.027, 5.383]) as c:
            for object_id, points in [('I_shade_1', [self.points['I_point_2'], self.points['I_point_4'], self.points['I_point_5']]), ('I_shade_3', [self.points['I_point_4'], self.points['I_point_6'], self.points['I_point_8']]), ('I_shade_5', [self.points['I_point_5'], self.points['I_point_9'], self.points['I_point_7']]), ('I_shade_8', [self.points['I_point_8'], self.points['I_point_11'], self.points['I_point_9']])]:
                c.fill(points, id=object_id, facecolor='#E8E8E8', alpha=1)
            for object_id, points in [('I_outer_AB', [self.points['I_point_1'], self.points['I_point_10']]), ('I_outer_BC', [self.points['I_point_10'], self.points['I_point_12']]), ('I_outer_CD', [self.points['I_point_12'], self.points['I_point_3']]), ('I_outer_DA', [self.points['I_point_3'], self.points['I_point_1']]), ('I_cut_1', [self.points['I_point_6'], self.points['I_point_11']]), ('I_cut_2', [self.points['I_point_11'], self.points['I_point_7']]), ('I_cut_3', [self.points['I_point_7'], self.points['I_point_2']]), ('I_cut_4', [self.points['I_point_2'], self.points['I_point_6']]), ('I_cut_5', [self.points['I_point_8'], self.points['I_point_9']]), ('I_cut_6', [self.points['I_point_9'], self.points['I_point_5']]), ('I_cut_7', [self.points['I_point_5'], self.points['I_point_4']]), ('I_cut_8', [self.points['I_point_4'], self.points['I_point_8']])]:
                c.line(points, id=object_id)
            c.fill([self.points['II_point_1'], self.points['II_point_5'], self.points['II_point_3']], facecolor='#E8E8E8', alpha=1, id='II_shade_2')
            for object_id, points in [('II_outer_AB', [self.points['II_point_1'], self.points['II_point_4']]), ('II_outer_BC', [self.points['II_point_4'], self.points['II_point_6']]), ('II_outer_CD', [self.points['II_point_6'], self.points['II_point_2']]), ('II_outer_DA', [self.points['II_point_2'], self.points['II_point_1']]), ('II_cut_1', [self.points['II_point_1'], self.points['II_point_3']]), ('II_cut_2', [self.points['II_point_3'], self.points['II_point_5']]), ('II_cut_3', [self.points['II_point_5'], self.points['II_point_1']])]:
                c.line(points, id=object_id)
            c.fill([self.points['III_point_2'], self.points['III_point_3'], self.points['III_point_5']], facecolor='#E8E8E8', alpha=1, id='III_shade_1')
            for object_id, points in [('III_outer_AB', [self.points['III_point_1'], self.points['III_point_4']]), ('III_outer_BC', [self.points['III_point_4'], self.points['III_point_5']]), ('III_outer_CD', [self.points['III_point_5'], self.points['III_point_2']]), ('III_outer_DA', [self.points['III_point_2'], self.points['III_point_1']]), ('III_cut_1', [self.points['III_point_2'], self.points['III_point_3']]), ('III_cut_2', [self.points['III_point_3'], self.points['III_point_5']])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('I_panel_label', 'I', self.points['I_panel_anchor']), ('II_panel_label', 'II', self.points['II_panel_anchor']), ('III_panel_label', 'III', self.points['III_panel_anchor'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane595_C01.png'
        with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('I_shade_1', [[0.0, 1.0], [0.5, 0.5], [0.5, 1.5], [0.0, 1.0]], [1, 2, 2, 79]), ('I_shade_3', [[0.5, 0.5], [1.0, 0.0], [1.5, 0.5], [0.5, 0.5]], [1, 2, 2, 79]), ('I_shade_5', [[0.5, 1.5], [1.5, 1.5], [1.0, 2.0], [0.5, 1.5]], [1, 2, 2, 79]), ('I_shade_8', [[1.5, 0.5], [2.0, 1.0], [1.5, 1.5], [1.5, 0.5]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[1.0, 0.0], [2.0, 1.0]]), ('I_cut_2', [[2.0, 1.0], [1.0, 2.0]]), ('I_cut_3', [[1.0, 2.0], [0.0, 1.0]]), ('I_cut_4', [[0.0, 1.0], [1.0, 0.0]]), ('I_cut_5', [[1.5, 0.5], [1.5, 1.5]]), ('I_cut_6', [[1.5, 1.5], [0.5, 1.5]]), ('I_cut_7', [[0.5, 1.5], [0.5, 0.5]]), ('I_cut_8', [[0.5, 0.5], [1.5, 0.5]])]:
                c.line(points, id=object_id)
            c.path([[3.0, 0.0], [5.0, 1.0], [4.0, 2.0], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [4.0, 2.0]]), ('II_cut_2', [[4.0, 2.0], [5.0, 1.0]]), ('II_cut_3', [[5.0, 1.0], [3.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[6.0, 2.0], [7.0, 0.0], [8.0, 2.0], [6.0, 2.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 2.0], [7.0, 0.0]]), ('III_cut_2', [[7.0, 0.0], [8.0, 2.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
            c.line([[0, 1], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 1], [5, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane595_C02.png'
        with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('I_shade_1', [[0.0, 1.0], [0.5, 0.5], [0.5, 1.5], [0.0, 1.0]], [1, 2, 2, 79]), ('I_shade_3', [[0.5, 0.5], [1.0, 0.0], [1.5, 0.5], [0.5, 0.5]], [1, 2, 2, 79]), ('I_shade_5', [[0.5, 1.5], [1.5, 1.5], [1.0, 2.0], [0.5, 1.5]], [1, 2, 2, 79]), ('I_shade_8', [[1.5, 0.5], [2.0, 1.0], [1.5, 1.5], [1.5, 0.5]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[1.0, 0.0], [2.0, 1.0]]), ('I_cut_2', [[2.0, 1.0], [1.0, 2.0]]), ('I_cut_3', [[1.0, 2.0], [0.0, 1.0]]), ('I_cut_4', [[0.0, 1.0], [1.0, 0.0]]), ('I_cut_5', [[1.5, 0.5], [1.5, 1.5]]), ('I_cut_6', [[1.5, 1.5], [0.5, 1.5]]), ('I_cut_7', [[0.5, 1.5], [0.5, 0.5]]), ('I_cut_8', [[0.5, 0.5], [1.5, 0.5]])]:
                c.line(points, id=object_id)
            c.path([[3.0, 0.0], [5.0, 1.0], [4.0, 2.0], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [4.0, 2.0]]), ('II_cut_2', [[4.0, 2.0], [5.0, 1.0]]), ('II_cut_3', [[5.0, 1.0], [3.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[6.0, 2.0], [7.0, 0.0], [8.0, 2.0], [6.0, 2.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
            for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 2.0], [7.0, 0.0]]), ('III_cut_2', [[7.0, 0.0], [8.0, 2.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
                c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
            c.line([[0, 1], [2, 1]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 1], [5, 1]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane595')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane595().draw(args.output, variant=args.variant))
