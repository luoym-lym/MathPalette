"""Collected question Plane286; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane286:
    variants = ('C01', 'C02')

    def __init__(self):
        self._samples_001 = [[5.0, 2.8284271247461903],
         [5.414213562373095, 2.414213562373095],
         [6.0, 2.414213562373095],
         [6.0, 1.8284271247461903],
         [6.414213562373095, 1.4142135623730951],
         [6.0, 1.0],
         [6.0, 0.41421356237309515],
         [5.414213562373095, 0.41421356237309515],
         [5.0, 0.0],
         [4.585786437626905, 0.41421356237309515],
         [4.0, 0.41421356237309515],
         [4.0, 1.0],
         [3.585786437626905, 1.4142135623730951],
         [4.0, 1.8284271247461903],
         [4.0, 2.414213562373095],
         [4.585786437626905, 2.414213562373095],
         [5.0, 2.8284271247461903]]
        self.id = 'Plane286'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:861'
        self.question = 'Two equally sized paper squares are glued together. Which of the following shapes cannot be made?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.5784647898110062, 23.612350182978226), ylim=(-8.5433576584356, 15.64745731435363), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (0.7, -0.6)), ('label1', '(B)', (5.7, -0.6)), ('label2', '(C)', (10.7, -0.6)), ('label3', '(D)', (15.7, -0.6)), ('label4', '(E)', (20.7, -0.6))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane286_C01.png'
        with Canvas(PLANE, xlim=(-0.5784647898110062, 23.612350182978226), ylim=(-8.5433576584356, 15.64745731435363), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', capstyle='butt', fill=False)
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', capstyle='butt', fill=False)
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', capstyle='butt', fill=False)
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt', fill=False)
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (0.7, -0.6)), ('label1', '(B)', (5.7, -0.6)), ('label2', '(C)', (10.7, -0.6)), ('label3', '(D)', (15.7, -0.6)), ('label4', '(E)', (20.7, -0.6))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.line([[9.0, 1.8284271247461903], [11.0, 1.8284271247461903]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane286_C02.png'
        with Canvas(PLANE, xlim=(-0.5784647898110062, 23.612350182978226), ylim=(-8.5433576584356, 15.64745731435363), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[8.0, 6.0], [10.0, 6.0], [10.0, 8.0], [8.0, 8.0], [8.0, 6.0]], [1, 2, 2, 2, 79], id='given0', capstyle='butt', fill=False)
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[12.0, 6.0], [14.0, 6.0], [14.0, 8.0], [12.0, 8.0], [12.0, 6.0]], [1, 2, 2, 2, 79], id='given1', capstyle='butt', fill=False)
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [1.0, 3.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 79], id='option0', capstyle='butt', fill=False)
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path(self._samples_001, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option1', capstyle='butt', fill=False)
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.0, 3.414213562373095], [11.0, 3.414213562373095], [11.0, 1.8284271247461903], [11.414213562373096, 1.4142135623730951], [10.0, 0.0], [8.585786437626904, 1.4142135623730951], [9.0, 1.8284271247461903], [9.0, 3.414213562373095]], [1, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[14.0, 0.0], [16.0, 0.0], [16.0, 1.0], [17.0, 1.0], [17.0, 3.0], [15.0, 3.0], [15.0, 2.0], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt', fill=False)
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[20.0, 0.0], [23.0, 0.0], [23.0, 2.0], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4', capstyle='butt', fill=False)
            for object_id, text, anchor in [('label0', '(A)', (0.7, -0.6)), ('label1', '(B)', (5.7, -0.6)), ('label2', '(C)', (10.7, -0.6)), ('label3', '(D)', (15.7, -0.6)), ('label4', '(E)', (20.7, -0.6))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane286')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane286().draw(args.output, variant=args.variant))
