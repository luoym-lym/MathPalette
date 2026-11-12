"""Collected question Plane104; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane104:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.id = 'Plane104'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:notched_arrow'
        self.question = 'All outlines use the same scale. Which outline, A, B, or C, is congruent to R? Rotations and reflections are allowed.\nChoices:\nA: Outline A\nB: Outline B\nC: Outline C'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Outline A', 'B': 'Outline B', 'C': 'Outline C'}
        self.query = self.question
        self.points = {'R_0': [-6.5, 2.0],
         'R_1': [-3.5, 2.0],
         'R_2': [-1.5, 4.0],
         'R_3': [-3.5, 6.0],
         'R_4': [-6.5, 6.0],
         'R_5': [-5.0, 4.5],
         'name_anchor_R': [-4.0, 2.0],
         'A_0': [1.5, 2.0],
         'A_1': [4.5, 2.0],
         'A_2': [6.5, 4.0],
         'A_3': [4.5, 6.0],
         'A_4': [1.5, 6.0],
         'A_5': [2.25, 4.5],
         'name_anchor_A': [4.0, 2.0],
         'B_0': [-2.0, -1.5],
         'B_1': [-2.0, -4.5],
         'B_2': [-4.0, -6.5],
         'B_3': [-6.0, -4.5],
         'B_4': [-6.0, -1.4999999999999998],
         'B_5': [-4.5, -3.0],
         'name_anchor_B': [-4.0, -6.5],
         'C_0': [1.5, -6.0],
         'C_1': [4.5, -6.0],
         'C_2': [6.5, -3.0],
         'C_3': [4.5, -2.0],
         'C_4': [1.5, -2.0],
         'C_5': [3.0, -3.5],
         'name_anchor_C': [4.0, -6.0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-6.981103617740445, 6.981103617740446], ylim=[-7.651935963581318, 6.310271271899573]) as c:
            for object_id, vertices, codes in [('outline_R', [self.points['R_0'], self.points['R_1'], self.points['R_2'], self.points['R_3'], self.points['R_4'], self.points['R_5'], self.points['R_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_A', [self.points['A_0'], self.points['A_1'], self.points['A_2'], self.points['A_3'], self.points['A_4'], self.points['A_5'], self.points['A_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_B', [self.points['B_0'], self.points['B_1'], self.points['B_2'], self.points['B_3'], self.points['B_4'], self.points['B_5'], self.points['B_0']], [1, 2, 2, 2, 2, 2, 79]), ('outline_C', [self.points['C_0'], self.points['C_1'], self.points['C_2'], self.points['C_3'], self.points['C_4'], self.points['C_5'], self.points['C_0']], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['name_anchor_R']), ('name_A', 'A', self.points['name_anchor_A']), ('name_B', 'B', self.points['name_anchor_B']), ('name_C', 'C', self.points['name_anchor_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C01.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
            c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C02.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', capstyle='butt')
            c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
            c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C03.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C04.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt')
            c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt')
            c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', linewidth=0.5, linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', linewidth=0.5, linestyle=(0, [3.7, 1.6]), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane104_C05.png'
        with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', capstyle='butt')
            c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
            c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane104')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane104().draw(args.output, variant=args.variant))
