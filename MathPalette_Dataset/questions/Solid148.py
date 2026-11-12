"""Collected question Solid148; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid148:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Solid148'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1091'
        self.question = 'The diagram shows the 7 positions $1,2,3,4,5,6,7$ of the bottom side of a die which is rolled around its edge in this order. Which two of these positions were taken up by the same face of the die?\nChoices:\nA:1 and 7\nB:1 and 6\nC:1 and 5\nD:2 and 7\nE:2 and 6'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 7', 'B': '1 and 6', 'C': '1 and 5', 'D': '2 and 7', 'E': '2 and 6'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-0.12452579270404929, 5.132096044642034], ylim=[-1.1320960446420338, 4.124525792704049], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('grid0', c.project([[0, 0, 0], [1, 0, 0]])), ('grid1', c.project([[1, 0, 0], [1, 1, 0]])), ('grid2', c.project([[1, 1, 0], [0, 1, 0]])), ('grid3', c.project([[0, 1, 0], [0, 0, 0]])), ('grid4', c.project([[1, 0, 0], [2, 0, 0]])), ('grid5', c.project([[2, 0, 0], [2, 1, 0]])), ('grid6', c.project([[2, 1, 0], [1, 1, 0]])), ('grid7', c.project([[2, 0, 0], [3, 0, 0]])), ('grid8', c.project([[3, 0, 0], [3, 1, 0]])), ('grid9', c.project([[3, 1, 0], [2, 1, 0]])), ('grid10', c.project([[3, 1, 0], [3, 2, 0]])), ('grid11', c.project([[3, 2, 0], [2, 2, 0]])), ('grid12', c.project([[2, 2, 0], [2, 1, 0]])), ('grid13', c.project([[3, 1, 0], [4, 1, 0]])), ('grid14', c.project([[4, 1, 0], [4, 2, 0]])), ('grid15', c.project([[4, 2, 0], [3, 2, 0]])), ('grid16', c.project([[4, 2, 0], [4, 3, 0]])), ('grid17', c.project([[4, 3, 0], [3, 3, 0]])), ('grid18', c.project([[3, 3, 0], [3, 2, 0]])), ('grid19', c.project([[4, 2, 0], [5, 2, 0]])), ('grid20', c.project([[5, 2, 0], [5, 3, 0]])), ('grid21', c.project([[5, 3, 0], [4, 3, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, text, anchor in [('position1', '1', c.project([0.5, 0.5, 0])), ('position2', '2', c.project([1.5, 0.5, 0])), ('position3', '3', c.project([2.5, 0.5, 0])), ('position4', '4', c.project([2.5, 1.5, 0])), ('position5', '5', c.project([3.5, 1.5, 0])), ('position6', '6', c.project([3.5, 2.5, 0])), ('position7', '7', c.project([4.5, 2.5, 0]))]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid148_C01.png'
        with Canvas(SOLID, xlim=(-0.12452579270404929, 5.132096044642034), ylim=(-1.1320960446420338, 4.124525792704049), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('grid0', [[0.0, 0.0], [1.0, 0.0]]), ('grid1', [[1.0, 0.0], [1.0, 1.0]]), ('grid2', [[1.0, 1.0], [0.0, 1.0]]), ('grid3', [[0.0, 1.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
            for object_id, points in [('grid4', [[1.0, 0.0], [2.0, 0.0]]), ('grid5', [[2.0, 0.0], [2.0, 1.0]]), ('grid6', [[2.0, 1.0], [1.0, 1.0]]), ('grid7', [[2.0, 0.0], [3.0, 0.0]]), ('grid8', [[3.0, 0.0], [3.0, 1.0]]), ('grid9', [[3.0, 1.0], [2.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[3.0, 1.0], [3.0, 2.0]], id='grid10', zorder=3, clip_on=False, color='#DC2626')
            c.line([[3.0, 2.0], [2.0, 2.0]], id='grid11', zorder=3, clip_on=False)
            c.line([[2.0, 2.0], [2.0, 1.0]], id='grid12', zorder=3, clip_on=False)
            for object_id, points in [('grid13', [[3.0, 1.0], [4.0, 1.0]]), ('grid14', [[4.0, 1.0], [4.0, 2.0]]), ('grid15', [[4.0, 2.0], [3.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
            for object_id, points in [('grid16', [[4.0, 2.0], [4.0, 3.0]]), ('grid17', [[4.0, 3.0], [3.0, 3.0]]), ('grid18', [[3.0, 3.0], [3.0, 2.0]]), ('grid19', [[4.0, 2.0], [5.0, 2.0]]), ('grid20', [[5.0, 2.0], [5.0, 3.0]]), ('grid21', [[5.0, 3.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('position1', '1', (0.5, 0.5)), ('position2', '2', (1.5, 0.5)), ('position3', '3', (2.5, 0.5)), ('position4', '4', (2.5, 1.5)), ('position5', '5', (3.5, 1.5)), ('position6', '6', (3.5, 2.5)), ('position7', '7', (4.5, 2.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid148_C02.png'
        with Canvas(SOLID, xlim=(-0.12452579270404929, 5.132096044642034), ylim=(-1.1320960446420338, 4.124525792704049), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.line([[0.0, 0.0], [1.0, 0.0]], id='grid0', zorder=3, clip_on=False)
            c.line([[1.0, 0.0], [1.0, 1.0]], id='grid1', zorder=3, clip_on=False, color='#DC2626')
            c.line([[1.0, 1.0], [0.0, 1.0]], id='grid2', zorder=3, clip_on=False)
            c.line([[0.0, 1.0], [0.0, 0.0]], id='grid3', zorder=3, clip_on=False)
            for object_id, points in [('grid4', [[1.0, 0.0], [2.0, 0.0]]), ('grid5', [[2.0, 0.0], [2.0, 1.0]]), ('grid6', [[2.0, 1.0], [1.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
            for object_id, points in [('grid7', [[2.0, 0.0], [3.0, 0.0]]), ('grid8', [[3.0, 0.0], [3.0, 1.0]]), ('grid9', [[3.0, 1.0], [2.0, 1.0]]), ('grid10', [[3.0, 1.0], [3.0, 2.0]]), ('grid11', [[3.0, 2.0], [2.0, 2.0]]), ('grid12', [[2.0, 2.0], [2.0, 1.0]]), ('grid13', [[3.0, 1.0], [4.0, 1.0]]), ('grid14', [[4.0, 1.0], [4.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('grid15', [[4.0, 2.0], [3.0, 2.0]]), ('grid16', [[4.0, 2.0], [4.0, 3.0]]), ('grid17', [[4.0, 3.0], [3.0, 3.0]]), ('grid18', [[3.0, 3.0], [3.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626')
            for object_id, points in [('grid19', [[4.0, 2.0], [5.0, 2.0]]), ('grid20', [[5.0, 2.0], [5.0, 3.0]]), ('grid21', [[5.0, 3.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('position1', '1', (0.5, 0.5)), ('position2', '2', (1.5, 0.5)), ('position3', '3', (2.5, 0.5)), ('position4', '4', (2.5, 1.5)), ('position5', '5', (3.5, 1.5)), ('position6', '6', (3.5, 2.5)), ('position7', '7', (4.5, 2.5))]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid148')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid148().draw(args.output, variant=args.variant))
