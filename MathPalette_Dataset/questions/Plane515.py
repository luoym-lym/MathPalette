"""Collected question Plane515; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane515:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Plane515'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane200/extension_01'
        self.question = 'Six identical coins touch in a triangular arrangement with rows of 3, 2 and 1, as shown. What is the smallest number of coins that must be moved to make the two-row parallelogram shown, with 3 coins in each row? In both arrangements, neighboring coins shown touching have centers one coin diameter apart. The coins may be lifted and placed freely, and a coin counts as moved if its center changes. The entire target arrangement may be translated and rotated, but not reflected or scaled; its position in the picture is only illustrative.'
        self.answer = '1'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.4526315789473685, 17.652631578947368], ylim=[-9.052631578947368, 9.052631578947368]) as c:
            for object_id, center, radius in [('initial_coin_01', [1, -1.7320508075688772], 1), ('initial_coin_02', [3, -1.7320508075688772], 1), ('initial_coin_03', [5, -1.7320508075688772], 1), ('initial_coin_04', [2, 0.0], 1), ('initial_coin_05', [4, 0.0], 1), ('initial_coin_06', [3, 1.7320508075688772], 1), ('target_coin_01', [11.2, -0.8660254037844386], 1), ('target_coin_02', [13.2, -0.8660254037844386], 1), ('target_coin_03', [15.2, -0.8660254037844386], 1), ('target_coin_04', [12.2, 0.8660254037844386], 1), ('target_coin_05', [14.2, 0.8660254037844386], 1), ('target_coin_06', [16.2, 0.8660254037844386], 1)]:
                c.circle(center, radius, id=object_id)
            c.path([[6.65, -0.22], [8.999999999999998, -0.22], [8.999999999999998, -0.55], [9.649999999999999, 0], [8.999999999999998, 0.55], [8.999999999999998, 0.22], [6.65, 0.22], [6.65, -0.22]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane515_C01.png'
        with Canvas(PLANE, xlim=(-0.4526315789473685, 17.652631578947368), ylim=(-9.052631578947368, 9.052631578947368), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.circle([1, -1.7320508075688772], 1.0, id='initial_coin_01', zorder=1)
            c.circle([3, -1.7320508075688772], 1.0, id='initial_coin_02', zorder=1)
            c.circle([5, -1.7320508075688772], 1.0, id='initial_coin_03', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5)
            c.circle([2, 0.0], 1.0, id='initial_coin_04', zorder=1)
            c.circle([4, 0.0], 1.0, id='initial_coin_05', zorder=1)
            c.circle([3, 1.7320508075688772], 1.0, id='initial_coin_06', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5)
            for object_id, center, radius in [('target_coin_01', [11.2, -0.8660254037844386], 1.0), ('target_coin_02', [13.2, -0.8660254037844386], 1.0), ('target_coin_03', [15.2, -0.8660254037844386], 1.0), ('target_coin_04', [12.2, 0.8660254037844386], 1.0), ('target_coin_05', [14.2, 0.8660254037844386], 1.0), ('target_coin_06', [16.2, 0.8660254037844386], 1.0)]:
                c.circle(center, radius, id=object_id, zorder=1)
            c.path([[6.65, -0.22], [8.999999999999998, -0.22], [8.999999999999998, -0.55], [9.649999999999999, 0.0], [8.999999999999998, 0.55], [8.999999999999998, 0.22], [6.65, 0.22], [6.65, -0.22]], [1, 2, 2, 2, 2, 2, 2, 79], id='transformation_arrow', zorder=1, capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane515')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane515().draw(args.output, variant=args.variant))
