"""Collected question Plane411; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane411:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane411'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1750'
        self.question = 'Two identical cards in the shape of equilateral triangles are placed onto a sheet of paper so that they touch or overlap. Their combined outline is traced. Which one of the following outlines is impossible?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'p0_0': [0, 0],
         'p0_1': [2, 0],
         'p0_2': [1.5, 0.8660254037844386],
         'p0_3': [2, 1.7320508075688772],
         'p0_4': [0, 1.7320508075688772],
         'p0_5': [0.5, 0.8660254037844386],
         'label0': [-1, 1],
         'p1_0': [5.0, 1],
         'p1_1': [6.732050807568877, 0.0],
         'p1_2': [8.464101615137753, 1],
         'p1_3': [6.732050807568877, 2.0],
         'label1': [4, 1],
         'p2_0': [10, 0],
         'p2_1': [10.866025403784437, 0.5],
         'p2_2': [10.866025403784437, 0],
         'p2_3': [12.598076211353316, 1.0],
         'p2_4': [10.866025403784437, 2],
         'p2_5': [10.866025403784437, 1.5],
         'p2_6': [10, 2],
         'label2': [9, 1],
         'p3_0': [15, 0],
         'p3_1': [15, 2],
         'p3_2': [16.039230484541328, 1.4],
         'p3_3': [17.598076211353316, 2.3],
         'p3_4': [17.598076211353316, 0.3],
         'p3_5': [16.558845726811988, 0.9],
         'label3': [14, 1],
         'p4_0': [20, 0],
         'p4_1': [22, 0],
         'p4_2': [22, 1.6],
         'p4_3': [20, 1.6],
         'label4': [19, 1]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-1.804695903400967, 22.61336199136393], ylim=[-11.078162338586152, 13.339895556178744]) as c:
            for object_id, vertices, codes in [('option0', [self.points['p0_0'], self.points['p0_1'], self.points['p0_2'], self.points['p0_3'], self.points['p0_4'], self.points['p0_5'], self.points['p0_0']], [1, 2, 2, 2, 2, 2, 79]), ('option1', [self.points['p1_0'], self.points['p1_1'], self.points['p1_2'], self.points['p1_3'], self.points['p1_0']], [1, 2, 2, 2, 79]), ('option2', [self.points['p2_0'], self.points['p2_1'], self.points['p2_2'], self.points['p2_3'], self.points['p2_4'], self.points['p2_5'], self.points['p2_6'], self.points['p2_0']], [1, 2, 2, 2, 2, 2, 2, 79]), ('option3', [self.points['p3_0'], self.points['p3_1'], self.points['p3_2'], self.points['p3_3'], self.points['p3_4'], self.points['p3_5'], self.points['p3_0']], [1, 2, 2, 2, 2, 2, 79]), ('option4', [self.points['p4_0'], self.points['p4_1'], self.points['p4_2'], self.points['p4_3'], self.points['p4_0']], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label0', 'A', self.points['label0']), ('label1', 'B', self.points['label1']), ('label2', 'C', self.points['label2']), ('label3', 'D', self.points['label3']), ('label4', 'E', self.points['label4'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane411_C01.png'
        with Canvas(PLANE, xlim=(-1.804695903400967, 22.61336199136393), ylim=(-11.078162338586152, 13.339895556178744), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [2.0, 0.0], [1.5, 0.8660254037844386], [2.0, 1.7320508075688772], [0.0, 1.7320508075688772], [0.5, 0.8660254037844386], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
            c.path([[5.0, 1.0], [6.732050807568877, 0.0], [8.464101615137753, 1.0], [6.732050807568877, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='option1', capstyle='butt')
            c.path([[10.0, 0.0], [10.866025403784437, 0.5], [10.866025403784437, 0.0], [12.598076211353316, 1.0], [10.866025403784437, 2.0], [10.866025403784437, 1.5], [10.0, 2.0], [10.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[15.0, 0.0], [15.0, 2.0], [16.039230484541328, 1.4], [17.598076211353316, 2.3], [17.598076211353316, 0.3], [16.558845726811988, 0.9], [15.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
            c.path([[20.0, 0.0], [22.0, 0.0], [22.0, 1.6], [20.0, 1.6], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', capstyle='butt')
            for object_id, text, anchor in [('label0', 'A', (-1.0, 1.0)), ('label1', 'B', (4.0, 1.0)), ('label2', 'C', (9.0, 1.0)), ('label3', 'D', (14.0, 1.0)), ('label4', 'E', (19.0, 1.0))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[10.866025403784437, 1.5], [10.866025403784437, 0.5]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane411')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane411().draw(args.output, variant=args.variant))
