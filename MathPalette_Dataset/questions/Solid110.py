"""Collected question Solid110; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid110:
    variants = ('C01',)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(0.2167574018066678, 5.841342767766978), ylim=(-1.4663427677669767, 4.158242598193333), projection=[[1, 0.35, 0], [0, 0.35, 1]]) as c:
            for object_id, points in [('structuree0', c.project([[0.0, 1.0, 0.0], [0.65, 1.0, 0.0]])), ('structuree1', c.project([[0.0, 1.0, 1.0], [1.0, 1.0, 1.0]])), ('structuree2', c.project([[0.0, 2.0, 1.0], [0.65, 2.0, 1.0]])), ('structuree3', c.project([[0.0, 1.0, 1.0], [0.0, 2.0, 1.0]])), ('structuree4', c.project([[0.0, 1.0, 0.0], [0.0, 1.0, 1.0]])), ('structuree5', c.project([[1.0, 1.0, 1.0], [2.0, 1.0, 1.0]])), ('structuree6', c.project([[2.0, 1.0, 1.0], [2.0, 2.0, 1.0]])), ('structuree7', c.project([[2.0, 1.0, 0.0], [2.0, 1.0, 1.0]])), ('structuree8', c.project([[2.0, 1.0, 0.0], [2.65, 1.0, 0.0]])), ('structuree9', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('structuree10', c.project([[2.0, 2.0, 1.0], [2.65, 2.0, 1.0]])), ('structuree11', c.project([[3.0, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('structuree12', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('structuree13', c.project([[4.0, 1.0, 0.0], [4.0, 1.0, 1.0]])), ('structuree14', c.project([[4.0, 1.0, 0.0], [5.0, 1.0, 0.0]])), ('structuree15', c.project([[4.0, 1.0, 1.0], [5.0, 1.0, 1.0]])), ('structuree16', c.project([[4.0, 2.0, 1.0], [5.0, 2.0, 1.0]])), ('structuree17', c.project([[5.0, 1.0, 0.0], [5.0, 2.0, 0.0]])), ('structuree18', c.project([[5.0, 1.0, 1.0], [5.0, 2.0, 1.0]])), ('structuree19', c.project([[5.0, 1.0, 0.0], [5.0, 1.0, 1.0]])), ('structuree20', c.project([[5.0, 2.0, 0.0], [5.0, 2.0, 1.0]])), ('structuree21', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('structuree22', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('structuree23', c.project([[1.0, 0.0, 1.0], [1.0, 1.0, 1.0]])), ('structuree24', c.project([[2.0, 0.0, 0.0], [2.0, 1.0, 0.0]])), ('structuree25', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('structuree26', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('structuree27', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('structuree28', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('structuree29', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('structuree30', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('structuree31', c.project([[4.0, 0.0, 0.0], [4.0, 1.0, 0.0]])), ('structuree32', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('structuree33', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('structuree34', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('structuree35', c.project([[1.0, 1.0, 2.0], [2.0, 1.0, 2.0]])), ('structuree36', c.project([[1.0, 2.0, 2.0], [2.0, 2.0, 2.0]])), ('structuree37', c.project([[1.0, 1.0, 2.0], [1.0, 2.0, 2.0]])), ('structuree38', c.project([[2.0, 1.0, 2.0], [2.0, 2.0, 2.0]])), ('structuree39', c.project([[1.0, 1.0, 1.0], [1.0, 1.0, 2.0]])), ('structuree40', c.project([[2.0, 1.0, 1.0], [2.0, 1.0, 2.0]])), ('structuree41', c.project([[2.0, 2.0, 1.0], [2.0, 2.0, 2.0]])), ('structuree42', c.project([[3.0, 1.0, 2.0], [4.0, 1.0, 2.0]])), ('structuree43', c.project([[3.0, 2.0, 2.0], [4.0, 2.0, 2.0]])), ('structuree44', c.project([[3.0, 1.0, 2.0], [3.0, 2.0, 2.0]])), ('structuree45', c.project([[4.0, 1.0, 2.0], [4.0, 2.0, 2.0]])), ('structuree46', c.project([[3.0, 1.0, 1.0], [3.0, 1.0, 2.0]])), ('structuree47', c.project([[4.0, 1.0, 1.0], [4.0, 1.0, 2.0]])), ('structuree48', c.project([[4.0, 2.0, 1.0], [4.0, 2.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid110_C01.png'
        _geometry_01 = [
            ('structuree0', [[0.35, 0.35], [1.0, 0.35]]), ('structuree1', [[0.35, 1.35], [1.35, 1.35]]),
            ('structuree2', [[0.7, 1.7], [1.35, 1.7]]), ('structuree3', [[0.35, 1.35], [0.7, 1.7]]),
            ('structuree4', [[0.35, 0.35], [0.35, 1.35]]), ('structuree5', [[1.35, 1.35], [2.35, 1.35]]),
            ('structuree6', [[2.35, 1.35], [2.7, 1.7]]), ('structuree7', [[2.35, 0.35], [2.35, 1.35]]),
            ('structuree8', [[2.35, 0.35], [3.0, 0.35]]), ('structuree9', [[2.35, 1.35], [3.35, 1.35]]),
            ('structuree10', [[2.7, 1.7], [3.3499999999999996, 1.7]]),
            ('structuree11', [[3.35, 1.35], [4.35, 1.35]]), ('structuree12', [[4.35, 1.35], [4.7, 1.7]]),
            ('structuree13', [[4.35, 0.35], [4.35, 1.35]]), ('structuree14', [[4.35, 0.35], [5.35, 0.35]]),
            ('structuree15', [[4.35, 1.35], [5.35, 1.35]]), ('structuree16', [[4.7, 1.7], [5.7, 1.7]]),
            ('structuree17', [[5.35, 0.35], [5.7, 0.7]]), ('structuree18', [[5.35, 1.35], [5.7, 1.7]]),
            ('structuree19', [[5.35, 0.35], [5.35, 1.35]]), ('structuree20', [[5.7, 0.7], [5.7, 1.7]]),
            ('structuree21', [[1.0, 0.0], [2.0, 0.0]]), ('structuree22', [[1.0, 1.0], [2.0, 1.0]]),
            ('structuree23', [[1.0, 1.0], [1.35, 1.35]]), ('structuree24', [[2.0, 0.0], [2.35, 0.35]]),
            ('structuree25', [[2.0, 1.0], [2.35, 1.35]]), ('structuree26', [[1.0, 0.0], [1.0, 1.0]]),
            ('structuree27', [[2.0, 0.0], [2.0, 1.0]]), ('structuree28', [[3.0, 0.0], [4.0, 0.0]]),
            ('structuree29', [[3.0, 1.0], [4.0, 1.0]]), ('structuree30', [[3.0, 1.0], [3.35, 1.35]]),
            ('structuree31', [[4.0, 0.0], [4.35, 0.35]]), ('structuree32', [[4.0, 1.0], [4.35, 1.35]]),
            ('structuree33', [[3.0, 0.0], [3.0, 1.0]]), ('structuree34', [[4.0, 0.0], [4.0, 1.0]]),
            ('structuree35', [[1.35, 2.35], [2.35, 2.35]]), ('structuree36', [[1.7, 2.7], [2.7, 2.7]]),
            ('structuree37', [[1.35, 2.35], [1.7, 2.7]]), ('structuree38', [[2.35, 2.35], [2.7, 2.7]]),
            ('structuree39', [[1.35, 1.35], [1.35, 2.35]]), ('structuree40', [[2.35, 1.35], [2.35, 2.35]]),
            ('structuree41', [[2.7, 1.7], [2.7, 2.7]]), ('structuree42', [[3.35, 2.35], [4.35, 2.35]]),
            ('structuree43', [[3.7, 2.7], [4.7, 2.7]]), ('structuree44', [[3.35, 2.35], [3.7, 2.7]]),
            ('structuree45', [[4.35, 2.35], [4.7, 2.7]]), ('structuree46', [[3.35, 1.35], [3.35, 2.35]]),
            ('structuree47', [[4.35, 1.35], [4.35, 2.35]]), ('structuree48', [[4.7, 1.7], [4.7, 2.7]])
        ]
        with Canvas(SOLID, xlim=(0.2167574018066678, 5.841342767766978), ylim=(-1.4663427677669767, 4.158242598193333)) as c:
            for object_id, points in _geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [(None, [[1.8802377142883933, 1.9031239149049153]]), (None, [[1.5987786835162783, 0.5360371940117843]]), (None, [[0.7486575293474405, 0.869192781456329]]), (None, [[2.78205542512966, 0.955353709243711]]), (None, [[3.517295342248655, 0.4728525136343702]]), (None, [[3.902147486365629, 1.8284511108225172]]), (None, [[4.993519238339136, 0.8232402866363913]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid110')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid110().draw(args.output, variant=args.variant))
