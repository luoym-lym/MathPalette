"""Collected question Plane117; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane117:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane117'
        self.source_dataset = 'Author Designed'
        self.source_key = 'perpendicularity:reference_PQ:candidates_OA_OB_OC'
        self.question = 'Which segment OA, OB, or OC is perpendicular to segment PQ? All segments are drawn to scale.\nChoices:\nA: Segment OA\nB: Segment OB\nC: Segment OC'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Segment OA', 'B': 'Segment OB', 'C': 'Segment OC'}
        self.query = self.question
        self.points = {'P': [0.5, 4.2], 'Q': [3, 5.45], 'O': [6.3, 1], 'A': [6.3, 4.6], 'B': [3.754415587728429, 3.545584412271571], 'C': [4.690031056200151, 4.219937887599697]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[0.047923313001905665, 6.768743353664762], ylim=[-0.13818779810920567, 6.58263224255365]) as c:
            for object_id, points in [('PQ', [self.points['P'], self.points['Q']]), ('OA', [self.points['O'], self.points['A']]), ('OB', [self.points['O'], self.points['B']]), ('OC', [self.points['O'], self.points['C']])]:
                c.line(points, id=object_id)
            for object_id, points in [('P_dot', [self.points['P']]), ('Q_dot', [self.points['Q']]), ('O_dot', [self.points['O']]), ('A_dot', [self.points['A']]), ('B_dot', [self.points['B']]), ('C_dot', [self.points['C']])]:
                c.point(points, id=object_id, filled=True)
            c.text('P', self.points['P'], offset_pt=[-12, -13], vertex=True, ha='right', id='P_label')
            c.text('Q', self.points['Q'], offset_pt=[10, 10], vertex=True, ha='left', id='Q_label')
            c.text('O', self.points['O'], offset_pt=[10, -14], vertex=True, ha='left', id='O_label')
            c.text('A', self.points['A'], offset_pt=[0, 12], vertex=True, va='bottom', id='A_label')
            c.text('B', self.points['B'], offset_pt=[-12, 9], vertex=True, ha='right', id='B_label')
            c.text('C', self.points['C'], offset_pt=[3, 13], vertex=True, va='bottom', id='C_label')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane117_C01.png'
        with Canvas(PLANE, xlim=(0.047923313001905665, 6.768743353664762), ylim=(-0.13818779810920567, 6.58263224255365), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.line([[0.5, 4.2], [3.0, 5.45]], id='PQ', color='#16A34A', linewidth=3.0)
            c.line([[6.3, 1.0], [6.3, 4.6]], id='OA', color='#16A34A', linewidth=3.0)
            c.line([[6.3, 1.0], [3.754415587728429, 3.545584412271571]], id='OB')
            c.line([[6.3, 1.0], [4.690031056200151, 4.219937887599697]], id='OC')
            for object_id, points in [('P_dot', [[0.5, 4.2]]), ('Q_dot', [[3.0, 5.45]]), ('O_dot', [[6.3, 1.0]]), ('A_dot', [[6.3, 4.6]]), ('B_dot', [[3.754415587728429, 3.545584412271571]]), ('C_dot', [[4.690031056200151, 4.219937887599697]])]:
                c.point(points, id=object_id)
            c.text('P', (0.5, 4.2), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-12, -13), annotation_clip=None)
            c.text('Q', (3.0, 5.45), id='Q_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, 10), annotation_clip=None)
            c.text('O', (6.3, 1.0), id='O_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, -14), annotation_clip=None)
            c.text('A', (6.3, 4.6), id='A_label', fontsize=18.0, fontstyle='italic', va='bottom', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
            c.text('B', (3.754415587728429, 3.545584412271571), id='B_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-12, 9), annotation_clip=None)
            c.text('C', (4.690031056200151, 4.219937887599697), id='C_label', fontsize=18.0, fontstyle='italic', va='bottom', rotation_mode='default', offset_pt=(3, 13), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane117')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane117().draw(args.output, variant=args.variant))
