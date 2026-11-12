"""Collected question Plane103; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane103:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self.id = 'Plane103'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:l_outline'
        self.question = 'All shapes use the same scale. Which outline, A, B, or C, is congruent to R? Reflections are allowed.\nChoices:\nA: Outline A\nB: Outline B\nC: Outline C'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Outline A', 'B': 'Outline B', 'C': 'Outline C'}
        self.query = self.question
        self.points = {'R0': [0, 7],
         'R1': [4, 7],
         'R2': [4, 8],
         'R3': [1, 8],
         'R4': [1, 10],
         'R5': [0, 10],
         'A0': [7, 6.5],
         'A1': [10, 6.5],
         'A2': [10, 10.5],
         'A3': [9, 10.5],
         'A4': [9, 7.5],
         'A5': [7, 7.5],
         'B0': [0, 0],
         'B1': [4, 0],
         'B2': [4, 2],
         'B3': [1, 2],
         'B4': [1, 3],
         'B5': [0, 3],
         'C0': [7, 0],
         'C1': [11, 0],
         'C2': [11, 1],
         'C3': [9, 1],
         'C4': [9, 3],
         'C5': [7, 3],
         'label_R': [2, 7],
         'label_A': [8.5, 6.5],
         'label_B': [2, 0],
         'label_C': [9, 0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.41, 11.41], ylim=[-1.005, 10.815]) as c:
            for object_id, vertices, codes in [('R', [self.points['R0'], self.points['R1'], self.points['R2'], self.points['R3'], self.points['R4'], self.points['R5'], self.points['R0']], [1, 2, 2, 2, 2, 2, 79]), ('A', [self.points['A0'], self.points['A1'], self.points['A2'], self.points['A3'], self.points['A4'], self.points['A5'], self.points['A0']], [1, 2, 2, 2, 2, 2, 79]), ('B', [self.points['B0'], self.points['B1'], self.points['B2'], self.points['B3'], self.points['B4'], self.points['B5'], self.points['B0']], [1, 2, 2, 2, 2, 2, 79]), ('C', [self.points['C0'], self.points['C1'], self.points['C2'], self.points['C3'], self.points['C4'], self.points['C5'], self.points['C0']], [1, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('name_R', 'R', self.points['label_R']), ('name_A', 'A', self.points['label_A']), ('name_B', 'B', self.points['label_B']), ('name_C', 'C', self.points['label_C'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -22], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane103_C01.png'
        with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane103_C02.png'
        with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
            c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
            c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', linestyle=(0, [3.7, 1.6]), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane103_C03.png'
        with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane103_C04.png'
        with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt')
            c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
            c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt')
            c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane103')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane103().draw(args.output, variant=args.variant))
