"""Collected question Solid114; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid114:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Solid114'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:443'
        self.question = 'A cubical aquarium has edges $3 \\mathrm{dm}$ long and contains some cubes with edges $1 \\mathrm{dm}$ long, arranged as shown. How many more such cubes can fit in the aquarium?'
        self.answer = '17'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'aquarium000': [0, 0, 0],
         'aquarium001': [0, 0, 3],
         'aquarium010': [0, 3, 0],
         'aquarium011': [0, 3, 3],
         'aquarium100': [3, 0, 0],
         'aquarium101': [3, 0, 3],
         'aquarium110': [3, 3, 0],
         'aquarium111': [3, 3, 3]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-0.10086589209028052, 4.156997796160048], ylim=[-0.1069977961600479, 4.15086589209028], projection=[[1, 0.35, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('stairse0', c.project([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])), ('stairse1', c.project([[0.0, 0.0, 1.0], [1.0, 0.0, 1.0]])), ('stairse2', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('stairse3', c.project([[0.0, 0.0, 1.0], [0.0, 1.0, 1.0]])), ('stairse4', c.project([[1.0, 0.0, 0.0], [1.0, 1.0, 0.0]])), ('stairse5', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('stairse6', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])), ('stairse7', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('stairse8', c.project([[1.0, 1.0, 0.0], [1.0, 1.0, 1.0]])), ('stairse9', c.project([[1.0, 1.0, 1.0], [1.0, 2.0, 1.0]])), ('stairse10', c.project([[0.0, 1.0, 2.0], [1.0, 1.0, 2.0]])), ('stairse11', c.project([[0.0, 2.0, 2.0], [1.0, 2.0, 2.0]])), ('stairse12', c.project([[0.0, 1.0, 2.0], [0.0, 2.0, 2.0]])), ('stairse13', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('stairse14', c.project([[0.0, 1.0, 1.0], [0.0, 1.0, 2.0]])), ('stairse15', c.project([[1.0, 1.0, 1.0], [1.0, 1.0, 2.0]])), ('stairse16', c.project([[1.0, 2.0, 1.0], [1.0, 2.0, 2.0]])), ('stairse17', c.project([[1.0, 2.0, 2.0], [1.0, 3.0, 2.0]])), ('stairse18', c.project([[0.0, 2.0, 3.0], [1.0, 2.0, 3.0]])), ('stairse19', c.project([[0.0, 3.0, 3.0], [1.0, 3.0, 3.0]])), ('stairse20', c.project([[0.0, 2.0, 3.0], [0.0, 3.0, 3.0]])), ('stairse21', c.project([[1.0, 2.0, 3.0], [1.0, 3.0, 3.0]])), ('stairse22', c.project([[0.0, 2.0, 2.0], [0.0, 2.0, 3.0]])), ('stairse23', c.project([[1.0, 2.0, 2.0], [1.0, 2.0, 3.0]])), ('stairse24', c.project([[1.0, 3.0, 2.0], [1.0, 3.0, 3.0]])), ('stairse25', c.project([[1.0, 1.0, 0.0], [2.0, 1.0, 0.0]])), ('stairse26', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('stairse27', c.project([[1.0, 2.0, 1.0], [2.0, 2.0, 1.0]])), ('stairse28', c.project([[2.0, 1.0, 0.0], [2.0, 2.0, 0.0]])), ('stairse29', c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]])), ('stairse30', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]])), ('stairse31', c.project([[2.0, 2.0, 0.0], [2.0, 2.0, 1.0]])), ('stairse32', c.project([[2.0, 2.0, 1.0], [2.0, 3.0, 1.0]])), ('stairse33', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('stairse34', c.project([[1.0, 3.0, 2.0], [2.0, 3.0, 2.0]])), ('stairse35', c.project([[2.0, 2.0, 2.0], [2.0, 3.0, 2.0]])), ('stairse36', c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]])), ('stairse37', c.project([[2.0, 3.0, 1.0], [2.0, 3.0, 2.0]])), ('stairse38', c.project([[2.0, 2.0, 0.0], [3.0, 2.0, 0.0]])), ('stairse39', c.project([[2.0, 2.0, 1.0], [3.0, 2.0, 1.0]])), ('stairse40', c.project([[2.0, 3.0, 1.0], [3.0, 3.0, 1.0]])), ('stairse41', c.project([[3.0, 2.0, 0.0], [3.0, 3.0, 0.0]])), ('stairse42', c.project([[3.0, 2.0, 1.0], [3.0, 3.0, 1.0]])), ('stairse43', c.project([[3.0, 2.0, 0.0], [3.0, 2.0, 1.0]])), ('stairse44', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 1.0]])), ('aquarium000_aquarium100part0', c.project([[0.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('aquarium000_aquarium001part0', c.project([[0.0, 0.0, 0.0], [0.0, 0.0, 3.0]])), ('aquarium001_aquarium101part0', c.project([[0.0, 0.0, 3.0], [3.0, 0.0, 3.0]])), ('aquarium001_aquarium011part0', c.project([[0.0, 0.0, 3.0], [0.0, 3.0, 3.0]])), ('aquarium011_aquarium111part0', c.project([[0.0, 3.0, 3.0], [3.0, 3.0, 3.0]])), ('aquarium100_aquarium110part0', c.project([[3.0, 0.0, 0.0], [3.0, 3.0, 0.0]])), ('aquarium100_aquarium101part0', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 3.0]])), ('aquarium101_aquarium111part0', c.project([[3.0, 0.0, 3.0], [3.0, 3.0, 3.0]])), ('aquarium110_aquarium111part0', c.project([[3.0, 3.0, 0.0], [3.0, 3.0, 3.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid114_C01.png'
        _geometry_01 = [('stairse0', [[0.0, 0.0], [1.0, 0.0]]),
         ('stairse1', [[0.0, 1.0], [1.0, 1.0]]),
         ('stairse2', [[0.35, 1.35], [1.35, 1.35]]),
         ('stairse3', [[0.0, 1.0], [0.35, 1.35]]),
         ('stairse4', [[1.0, 0.0], [1.35, 0.35]]),
         ('stairse5', [[1.0, 1.0], [1.35, 1.35]]),
         ('stairse6', [[0.0, 0.0], [0.0, 1.0]]),
         ('stairse7', [[1.0, 0.0], [1.0, 1.0]]),
         ('stairse8', [[1.35, 0.35], [1.35, 1.35]]),
         ('stairse9', [[1.35, 1.35], [1.7, 1.7]]),
         ('stairse10', [[0.35, 2.35], [1.35, 2.35]]),
         ('stairse11', [[0.7, 2.7], [1.7, 2.7]]),
         ('stairse12', [[0.35, 2.35], [0.7, 2.7]]),
         ('stairse13', [[1.35, 2.35], [1.7, 2.7]]),
         ('stairse14', [[0.35, 1.35], [0.35, 2.35]]),
         ('stairse15', [[1.35, 1.35], [1.35, 2.35]]),
         ('stairse16', [[1.7, 1.7], [1.7, 2.7]]),
         ('stairse17', [[1.7, 2.7], [2.05, 3.05]]),
         ('stairse18', [[0.7, 3.7], [1.7, 3.7]]),
         ('stairse19', [[1.0499999999999998, 4.05], [2.05, 4.05]]),
         ('stairse20', [[0.7, 3.7], [1.0499999999999998, 4.05]]),
         ('stairse21', [[1.7, 3.7], [2.05, 4.05]]),
         ('stairse22', [[0.7, 2.7], [0.7, 3.7]]),
         ('stairse23', [[1.7, 2.7], [1.7, 3.7]]),
         ('stairse24', [[2.05, 3.05], [2.05, 4.05]]),
         ('stairse25', [[1.35, 0.35], [2.35, 0.35]]),
         ('stairse26', [[1.35, 1.35], [2.35, 1.35]]),
         ('stairse27', [[1.7, 1.7], [2.7, 1.7]]),
         ('stairse28', [[2.35, 0.35], [2.7, 0.7]]),
         ('stairse29', [[2.35, 1.35], [2.7, 1.7]]),
         ('stairse30', [[2.35, 0.35], [2.35, 1.35]]),
         ('stairse31', [[2.7, 0.7], [2.7, 1.7]]),
         ('stairse32', [[2.7, 1.7], [3.05, 2.05]]),
         ('stairse33', [[1.7, 2.7], [2.7, 2.7]]),
         ('stairse34', [[2.05, 3.05], [3.05, 3.05]]),
         ('stairse35', [[2.7, 2.7], [3.05, 3.05]]),
         ('stairse36', [[2.7, 1.7], [2.7, 2.7]]),
         ('stairse37', [[3.05, 2.05], [3.05, 3.05]]),
         ('stairse38', [[2.7, 0.7], [3.7, 0.7]]),
         ('stairse39', [[2.7, 1.7], [3.7, 1.7]]),
         ('stairse40', [[3.05, 2.05], [4.05, 2.05]]),
         ('stairse41', [[3.7, 0.7], [4.05, 1.0499999999999998]]),
         ('stairse42', [[3.7, 1.7], [4.05, 2.05]]),
         ('stairse43', [[3.7, 0.7], [3.7, 1.7]]),
         ('stairse44', [[4.05, 1.0499999999999998], [4.05, 2.05]]),
         ('aquarium000_aquarium100part0', [[0.0, 0.0], [3.0, 0.0]]),
         ('aquarium000_aquarium001part0', [[0.0, 0.0], [0.0, 3.0]]),
         ('aquarium001_aquarium101part0', [[0.0, 3.0], [3.0, 3.0]]),
         ('aquarium001_aquarium011part0', [[0.0, 3.0], [1.0499999999999998, 4.05]]),
         ('aquarium011_aquarium111part0', [[1.0499999999999998, 4.05], [4.05, 4.05]]),
         ('aquarium100_aquarium110part0', [[3.0, 0.0], [4.05, 1.0499999999999998]]),
         ('aquarium100_aquarium101part0', [[3.0, 0.0], [3.0, 3.0]]),
         ('aquarium101_aquarium111part0', [[3.0, 3.0], [4.05, 4.05]]),
         ('aquarium110_aquarium111part0', [[4.05, 1.0499999999999998], [4.05, 4.05]])]
        with Canvas(SOLID, xlim=(-0.10086589209028052, 4.156997796160048), ylim=(-0.1069977961600479, 4.15086589209028), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [(None, [[1.1975390275497808, 3.2264155038937736]]), (None, [[0.8757641981681177, 1.8784398672949156]]), (None, [[2.258526302808237, 2.2306528562126817]]), (None, [[3.2151541739429104, 1.1740138894593835]]), (None, [[1.8584819203337368, 0.891373836624139]]), (None, [[0.43658503914719954, 0.46523960311869317]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid114')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid114().draw(args.output, variant=args.variant))
