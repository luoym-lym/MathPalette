"""Collected question Solid112; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid112:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Solid112'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:427'
        self.question = 'How many cubes have been taken from the block?'
        self.answer = '7'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-0.23286323235657225, 9.597019603480604], ylim=[-3.3970196034806035, 6.432863232356573], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('beforee0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('beforee1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('beforee2', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('beforee3', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('beforee4', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('beforee5', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('beforee6', c.project([[0.0, 0.0, 2.0], [0.0, 1.0, 2.0]])), ('beforee7', c.project([[1.0, 0.0, 2.0], [1.0, 1.0, 2.0]])), ('beforee8', c.project([[0.0, 0.0, 1.0], [0.0, 0.0, 2.0]])), ('beforee9', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('beforee10', c.project([[0.0, 2.0, 2.0], [1.0, 2.0, 2.0]])), ('beforee11', c.project([[0.0, 1.0, 2.0], [0.0, 2.0, 2.0]])), ('beforee12', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('beforee13', c.project([[0.0, 3.0, 2.0], [1.0, 3.0, 2.0]])), ('beforee14', c.project([[0.0, 2.0, 2.0], [0.0, 3.0, 2.0]])), ('beforee15', c.project([[1.0, 2.0, 2.0], [1.0, 3.0, 2.0]])), ('beforee16', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('beforee17', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('beforee18', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('beforee19', c.project([[1.0, 0.0, 2.0], [2.0, 0.0, 2.0]])), ('beforee20', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('beforee21', c.project([[2.0, 0.0, 2.0], [2.0, 1.0, 2.0]])), ('beforee22', c.project([[2.0, 0.0, 1.0], [2.0, 0.0, 2.0]])), ('beforee23', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('beforee24', c.project([[2.0, 1.0, 2.0], [2.0, 2.0, 2.0]])), ('beforee25', c.project([[1.0, 3.0, 2.0], [2.0, 3.0, 2.0]])), ('beforee26', c.project([[2.0, 2.0, 2.0], [2.0, 3.0, 2.0]])), ('beforee27', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('beforee28', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('beforee29', c.project([[3.0, 0.0, 0.0], [3.0, 1.0, 0.0]])), ('beforee30', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('beforee31', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('beforee32', c.project([[3.0, 1.0, 0.0], [3.0, 1.0, 1.0]])), ('beforee33', c.project([[2.0, 0.0, 2.0], [3.0, 0.0, 2.0]])), ('beforee34', c.project([[2.0, 1.0, 2.0], [3.0, 1.0, 2.0]])), ('beforee35', c.project([[3.0, 0.0, 2.0], [3.0, 1.0, 2.0]])), ('beforee36', c.project([[3.0, 0.0, 1.0], [3.0, 0.0, 2.0]])), ('beforee37', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('beforee38', c.project([[3.0, 1.0, 0.0], [3.0, 2.0, 0.0]])), ('beforee39', c.project([[3.0, 1.0, 1.0], [3.0, 2.0, 1.0]])), ('beforee40', c.project([[3.0, 2.0, 0.0], [3.0, 2.0, 1.0]])), ('beforee41', c.project([[2.0, 2.0, 2.0], [3.0, 2.0, 2.0]])), ('beforee42', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('beforee43', c.project([[3.0, 2.0, 1.0], [3.0, 2.0, 2.0]])), ('beforee44', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('beforee45', c.project([[3.0, 2.0, 1.0], [3.0, 3.0, 1.0]])), ('beforee46', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 1.0]])), ('beforee47', c.project([[2.0, 3.0, 2.0], [3.0, 3.0, 2.0]])), ('beforee48', c.project([[3.0, 2.0, 2.0], [3.0, 3.0, 2.0]])), ('beforee49', c.project([[3.0, 3.0, 1.0], [3.0, 3.0, 2.0]])), ('aftere0', c.project([[5.3, 0.0, 0.0], [6.3, 0.0, 0.0]])), ('aftere1', c.project([[5.3, 0.0, 1.0], [6.3, 0.0, 1.0]])), ('aftere2', c.project([[6.3, 0.0, 1.0], [6.3, 1.0, 1.0]])), ('aftere3', c.project([[5.3, 0.0, 0.0], [5.3, 0.0, 1.0]])), ('aftere4', c.project([[6.3, 0.0, 0.0], [6.3, 0.0, 1.0]])), ('aftere5', c.project([[5.95, 2.0, 1.0], [6.3, 2.0, 1.0]])), ('aftere6', c.project([[6.3, 1.0, 1.0], [6.3, 2.0, 1.0]])), ('aftere7', c.project([[5.6, 3.0, 1.0], [6.3, 3.0, 1.0]])), ('aftere8', c.project([[6.3, 2.0, 1.0], [6.3, 3.0, 1.0]])), ('aftere9', c.project([[6.3, 0.0, 0.0], [7.3, 0.0, 0.0]])), ('aftere10', c.project([[6.3, 0.0, 1.0], [7.3, 0.0, 1.0]])), ('aftere11', c.project([[6.3, 1.0, 1.0], [7.3, 1.0, 1.0]])), ('aftere12', c.project([[7.3, 0.0, 1.0], [7.3, 1.0, 1.0]])), ('aftere13', c.project([[7.3, 0.0, 0.0], [7.3, 0.0, 1.0]])), ('aftere14', c.project([[6.3, 2.0, 1.0], [7.3, 2.0, 1.0]])), ('aftere15', c.project([[7.3, 1.0, 1.0], [7.3, 2.0, 1.0]])), ('aftere16', c.project([[6.3, 3.0, 1.0], [6.95, 3.0, 1.0]])), ('aftere17', c.project([[7.3, 0.0, 0.0], [8.3, 0.0, 0.0]])), ('aftere18', c.project([[7.3, 0.0, 1.0], [8.3, 0.0, 1.0]])), ('aftere19', c.project([[7.3, 1.0, 1.0], [8.3, 1.0, 1.0]])), ('aftere20', c.project([[8.3, 0.0, 0.0], [8.3, 1.0, 0.0]])), ('aftere21', c.project([[8.3, 0.0, 1.0], [8.3, 1.0, 1.0]])), ('aftere22', c.project([[8.3, 0.0, 0.0], [8.3, 0.0, 1.0]])), ('aftere23', c.project([[8.3, 1.0, 0.0], [8.3, 1.0, 1.0]])), ('aftere24', c.project([[7.3, 2.0, 1.0], [8.3, 2.0, 1.0]])), ('aftere25', c.project([[8.3, 1.0, 0.0], [8.3, 2.0, 0.0]])), ('aftere26', c.project([[8.3, 1.0, 1.0], [8.3, 2.0, 1.0]])), ('aftere27', c.project([[8.3, 2.0, 0.0], [8.3, 2.0, 1.0]])), ('aftere28', c.project([[8.3, 2.0, 0.0], [8.3, 3.0, 0.0]])), ('aftere29', c.project([[8.3, 2.0, 1.0], [8.3, 3.0, 1.0]])), ('aftere30', c.project([[8.3, 3.0, 0.0], [8.3, 3.0, 1.0]])), ('aftere31', c.project([[5.3, 0.0, 2.0], [6.3, 0.0, 2.0]])), ('aftere32', c.project([[5.3, 1.0, 2.0], [6.3, 1.0, 2.0]])), ('aftere33', c.project([[5.3, 0.0, 2.0], [5.3, 1.0, 2.0]])), ('aftere34', c.project([[6.3, 0.0, 2.0], [6.3, 1.0, 2.0]])), ('aftere35', c.project([[5.3, 0.0, 1.0], [5.3, 0.0, 2.0]])), ('aftere36', c.project([[6.3, 0.0, 1.0], [6.3, 0.0, 2.0]])), ('aftere37', c.project([[6.3, 1.0, 1.0], [6.3, 1.0, 2.0]])), ('aftere38', c.project([[7.3, 2.0, 2.0], [8.3, 2.0, 2.0]])), ('aftere39', c.project([[7.3, 3.0, 2.0], [8.3, 3.0, 2.0]])), ('aftere40', c.project([[7.3, 2.0, 2.0], [7.3, 3.0, 2.0]])), ('aftere41', c.project([[8.3, 2.0, 2.0], [8.3, 3.0, 2.0]])), ('aftere42', c.project([[7.3, 2.0, 1.0], [7.3, 2.0, 2.0]])), ('aftere43', c.project([[8.3, 2.0, 1.0], [8.3, 2.0, 2.0]])), ('aftere44', c.project([[8.3, 3.0, 1.0], [8.3, 3.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid112_C01.png'
        _geometry_01 = [('beforee0', [[0.0, 0.0], [1.0, 0.0]]),
         ('beforee1', [[0.0, 1.0], [1.0, 1.0]]),
         ('beforee2', [[0.0, 0.0], [0.0, 1.0]]),
         ('beforee3', [[1.0, 0.0], [1.0, 1.0]]),
         ('beforee4', [[0.0, 2.0], [1.0, 2.0]]),
         ('beforee5', [[0.35, 2.35], [1.35, 2.35]]),
         ('beforee6', [[0.0, 2.0], [0.35, 2.35]]),
         ('beforee7', [[1.0, 2.0], [1.35, 2.35]]),
         ('beforee8', [[0.0, 1.0], [0.0, 2.0]]),
         ('beforee9', [[1.0, 1.0], [1.0, 2.0]]),
         ('beforee10', [[0.7, 2.7], [1.7, 2.7]]),
         ('beforee11', [[0.35, 2.35], [0.7, 2.7]]),
         ('beforee12', [[1.35, 2.35], [1.7, 2.7]]),
         ('beforee13', [[1.0499999999999998, 3.05], [2.05, 3.05]]),
         ('beforee14', [[0.7, 2.7], [1.0499999999999998, 3.05]]),
         ('beforee15', [[1.7, 2.7], [2.05, 3.05]]),
         ('beforee16', [[1.0, 0.0], [2.0, 0.0]]),
         ('beforee17', [[1.0, 1.0], [2.0, 1.0]]),
         ('beforee18', [[2.0, 0.0], [2.0, 1.0]]),
         ('beforee19', [[1.0, 2.0], [2.0, 2.0]]),
         ('beforee20', [[1.35, 2.35], [2.35, 2.35]]),
         ('beforee21', [[2.0, 2.0], [2.35, 2.35]]),
         ('beforee22', [[2.0, 1.0], [2.0, 2.0]]),
         ('beforee23', [[1.7, 2.7], [2.7, 2.7]]),
         ('beforee24', [[2.35, 2.35], [2.7, 2.7]]),
         ('beforee25', [[2.05, 3.05], [3.05, 3.05]]),
         ('beforee26', [[2.7, 2.7], [3.05, 3.05]]),
         ('beforee27', [[2.0, 0.0], [3.0, 0.0]]),
         ('beforee28', [[2.0, 1.0], [3.0, 1.0]]),
         ('beforee29', [[3.0, 0.0], [3.35, 0.35]]),
         ('beforee30', [[3.0, 1.0], [3.35, 1.35]]),
         ('beforee31', [[3.0, 0.0], [3.0, 1.0]]),
         ('beforee32', [[3.35, 0.35], [3.35, 1.35]]),
         ('beforee33', [[2.0, 2.0], [3.0, 2.0]]),
         ('beforee34', [[2.35, 2.35], [3.35, 2.35]]),
         ('beforee35', [[3.0, 2.0], [3.35, 2.35]]),
         ('beforee36', [[3.0, 1.0], [3.0, 2.0]]),
         ('beforee37', [[3.35, 1.35], [3.35, 2.35]]),
         ('beforee38', [[3.35, 0.35], [3.7, 0.7]]),
         ('beforee39', [[3.35, 1.35], [3.7, 1.7]]),
         ('beforee40', [[3.7, 0.7], [3.7, 1.7]]),
         ('beforee41', [[2.7, 2.7], [3.7, 2.7]]),
         ('beforee42', [[3.35, 2.35], [3.7, 2.7]]),
         ('beforee43', [[3.7, 1.7], [3.7, 2.7]]),
         ('beforee44', [[3.7, 0.7], [4.05, 1.0499999999999998]]),
         ('beforee45', [[3.7, 1.7], [4.05, 2.05]]),
         ('beforee46', [[4.05, 1.0499999999999998], [4.05, 2.05]]),
         ('beforee47', [[3.05, 3.05], [4.05, 3.05]]),
         ('beforee48', [[3.7, 2.7], [4.05, 3.05]]),
         ('beforee49', [[4.05, 2.05], [4.05, 3.05]]),
         ('aftere0', [[5.3, 0.0], [6.3, 0.0]]),
         ('aftere1', [[5.3, 1.0], [6.3, 1.0]]),
         ('aftere2', [[6.3, 1.0], [6.6499999999999995, 1.35]]),
         ('aftere3', [[5.3, 0.0], [5.3, 1.0]]),
         ('aftere4', [[6.3, 0.0], [6.3, 1.0]]),
         ('aftere5', [[6.65, 1.7], [7.0, 1.7]]),
         ('aftere6', [[6.6499999999999995, 1.35], [7.0, 1.7]]),
         ('aftere7', [[6.6499999999999995, 2.05], [7.35, 2.05]]),
         ('aftere8', [[7.0, 1.7], [7.35, 2.05]]),
         ('aftere9', [[6.3, 0.0], [7.3, 0.0]]),
         ('aftere10', [[6.3, 1.0], [7.3, 1.0]]),
         ('aftere11', [[6.6499999999999995, 1.35], [7.6499999999999995, 1.35]])]
        with Canvas(SOLID, xlim=(-0.23286323235657225, 9.597019603480604), ylim=(-3.3970196034806035, 6.432863232356573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[7.3, 1.0], [7.6499999999999995, 1.35]], id='aftere12', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            for object_id, points in [('aftere13', [[7.3, 0.0], [7.3, 1.0]]), ('aftere14', [[7.0, 1.7], [8.0, 1.7]]), ('aftere15', [[7.6499999999999995, 1.35], [8.0, 1.7]]), ('aftere16', [[7.35, 2.05], [8.0, 2.05]]), ('aftere17', [[7.3, 0.0], [8.3, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            c.line([[7.3, 1.0], [8.3, 1.0]], id='aftere18', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[7.6499999999999995, 1.35], [8.65, 1.35]], id='aftere19', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            c.line([[8.3, 0.0], [8.65, 0.35]], id='aftere20', zorder=3, clip_on=False, simplify=False)
            c.line([[8.3, 1.0], [8.65, 1.35]], id='aftere21', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            for object_id, points in [('aftere22', [[8.3, 0.0], [8.3, 1.0]]), ('aftere23', [[8.65, 0.35], [8.65, 1.35]]), ('aftere24', [[8.0, 1.7], [9.0, 1.7]]), ('aftere25', [[8.65, 0.35], [9.0, 0.7]]), ('aftere26', [[8.65, 1.35], [9.0, 1.7]]), ('aftere27', [[9.0, 0.7], [9.0, 1.7]]), ('aftere28', [[9.0, 0.7], [9.350000000000001, 1.0499999999999998]]), ('aftere29', [[9.0, 1.7], [9.350000000000001, 2.05]]), ('aftere30', [[9.350000000000001, 1.0499999999999998], [9.350000000000001, 2.05]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('aftere31', [[5.3, 2.0], [6.3, 2.0]]), ('aftere32', [[5.6499999999999995, 2.35], [6.6499999999999995, 2.35]]), ('aftere33', [[5.3, 2.0], [5.6499999999999995, 2.35]]), ('aftere34', [[6.3, 2.0], [6.6499999999999995, 2.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            for object_id, points in [('aftere35', [[5.3, 1.0], [5.3, 2.0]]), ('aftere36', [[6.3, 1.0], [6.3, 2.0]]), ('aftere37', [[6.6499999999999995, 1.35], [6.6499999999999995, 2.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            for object_id, points in [('aftere38', [[8.0, 2.7], [9.0, 2.7]]), ('aftere39', [[8.35, 3.05], [9.350000000000001, 3.05]]), ('aftere40', [[8.0, 2.7], [8.35, 3.05]]), ('aftere41', [[9.0, 2.7], [9.350000000000001, 3.05]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
            for object_id, points in [('aftere42', [[8.0, 1.7], [8.0, 2.7]]), ('aftere43', [[9.0, 1.7], [9.0, 2.7]]), ('aftere44', [[9.350000000000001, 2.05], [9.350000000000001, 3.05]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid112')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid112().draw(args.output, variant=args.variant))
