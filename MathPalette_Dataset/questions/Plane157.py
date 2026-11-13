"""Collected question Plane157; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane157:
    variants = ('C01', 'C02')

    def __init__(self):
        self._geometry_01 = [
            ('tile_edge0', [[0.0, 0.0], [0.0, 1.0]]), ('tile_edge1', [[0.0, 0.0], [4.0, 0.0]]),
            ('tile_edge2', [[0.0, 1.0], [0.0, 5.0]]), ('tile_edge3', [[0.0, 1.0], [1.0, 1.0]]),
            ('tile_edge4', [[0.0, 1.0], [4.0, 1.0]]), ('tile_edge5', [[0.0, 5.0], [0.0, 6.0]]),
            ('tile_edge6', [[0.0, 5.0], [1.0, 5.0]]), ('tile_edge7', [[0.0, 5.0], [4.0, 5.0]]),
            ('tile_edge8', [[0.0, 6.0], [0.0, 7.0]]), ('tile_edge9', [[0.0, 6.0], [4.0, 6.0]]),
            ('tile_edge10', [[0.0, 7.0], [0.0, 11.0]]), ('tile_edge11', [[0.0, 7.0], [1.0, 7.0]]),
            ('tile_edge12', [[0.0, 7.0], [4.0, 7.0]]), ('tile_edge13', [[0.0, 11.0], [0.0, 12.0]]),
            ('tile_edge14', [[0.0, 11.0], [1.0, 11.0]]), ('tile_edge15', [[0.0, 11.0], [4.0, 11.0]]),
            ('tile_edge16', [[0.0, 12.0], [4.0, 12.0]]), ('tile_edge17', [[1.0, 1.0], [1.0, 5.0]]),
            ('tile_edge18', [[1.0, 1.0], [2.0, 1.0]]), ('tile_edge19', [[1.0, 5.0], [2.0, 5.0]]),
            ('tile_edge20', [[1.0, 7.0], [1.0, 11.0]]), ('tile_edge21', [[1.0, 7.0], [2.0, 7.0]]),
            ('tile_edge22', [[1.0, 11.0], [2.0, 11.0]]), ('tile_edge23', [[2.0, 1.0], [2.0, 2.0]]),
            ('tile_edge24', [[2.0, 1.0], [2.0, 5.0]]), ('tile_edge25', [[2.0, 1.0], [6.0, 1.0]]),
            ('tile_edge26', [[2.0, 2.0], [2.0, 3.0]]), ('tile_edge27', [[2.0, 2.0], [6.0, 2.0]]),
            ('tile_edge28', [[2.0, 3.0], [2.0, 4.0]]), ('tile_edge29', [[2.0, 3.0], [6.0, 3.0]]),
            ('tile_edge30', [[2.0, 4.0], [2.0, 5.0]]), ('tile_edge31', [[2.0, 4.0], [6.0, 4.0]]),
            ('tile_edge32', [[2.0, 5.0], [6.0, 5.0]]), ('tile_edge33', [[2.0, 7.0], [2.0, 11.0]]),
            ('tile_edge34', [[2.0, 7.0], [3.0, 7.0]]), ('tile_edge35', [[2.0, 11.0], [3.0, 11.0]]),
            ('tile_edge36', [[3.0, 7.0], [3.0, 11.0]]), ('tile_edge37', [[3.0, 7.0], [4.0, 7.0]]),
            ('tile_edge38', [[3.0, 11.0], [4.0, 11.0]]), ('tile_edge39', [[4.0, 0.0], [4.0, 1.0]]),
            ('tile_edge40', [[4.0, 0.0], [8.0, 0.0]]), ('tile_edge41', [[4.0, 1.0], [8.0, 1.0]]),
            ('tile_edge42', [[4.0, 5.0], [4.0, 6.0]]), ('tile_edge43', [[4.0, 5.0], [4.0, 9.0]]),
            ('tile_edge44', [[4.0, 5.0], [5.0, 5.0]]), ('tile_edge45', [[4.0, 6.0], [4.0, 7.0]]),
            ('tile_edge46', [[4.0, 7.0], [4.0, 11.0]]), ('tile_edge47', [[4.0, 9.0], [4.0, 10.0]]),
            ('tile_edge48', [[4.0, 9.0], [5.0, 9.0]]), ('tile_edge49', [[4.0, 9.0], [8.0, 9.0]]),
            ('tile_edge50', [[4.0, 10.0], [4.0, 11.0]]), ('tile_edge51', [[4.0, 10.0], [8.0, 10.0]]),
            ('tile_edge52', [[4.0, 11.0], [4.0, 12.0]]), ('tile_edge53', [[4.0, 11.0], [8.0, 11.0]]),
            ('tile_edge54', [[4.0, 12.0], [8.0, 12.0]]), ('tile_edge55', [[5.0, 5.0], [5.0, 9.0]]),
            ('tile_edge56', [[5.0, 5.0], [6.0, 5.0]]), ('tile_edge57', [[5.0, 9.0], [6.0, 9.0]]),
            ('tile_edge58', [[6.0, 1.0], [6.0, 2.0]]), ('tile_edge59', [[6.0, 1.0], [6.0, 5.0]]),
            ('tile_edge60', [[6.0, 1.0], [7.0, 1.0]]), ('tile_edge61', [[6.0, 2.0], [6.0, 3.0]]),
            ('tile_edge62', [[6.0, 3.0], [6.0, 4.0]]), ('tile_edge63', [[6.0, 4.0], [6.0, 5.0]]),
            ('tile_edge64', [[6.0, 5.0], [6.0, 9.0]]), ('tile_edge65', [[6.0, 5.0], [7.0, 5.0]]),
            ('tile_edge66', [[6.0, 9.0], [7.0, 9.0]]), ('tile_edge67', [[7.0, 1.0], [7.0, 5.0]]),
            ('tile_edge68', [[7.0, 1.0], [8.0, 1.0]]), ('tile_edge69', [[7.0, 5.0], [7.0, 9.0]]),
            ('tile_edge70', [[7.0, 5.0], [8.0, 5.0]]), ('tile_edge71', [[7.0, 9.0], [8.0, 9.0]]),
            ('tile_edge72', [[8.0, 0.0], [8.0, 1.0]]), ('tile_edge73', [[8.0, 1.0], [8.0, 5.0]]),
            ('tile_edge74', [[8.0, 5.0], [8.0, 9.0]]), ('tile_edge75', [[8.0, 9.0], [8.0, 10.0]]),
            ('tile_edge76', [[8.0, 10.0], [8.0, 11.0]]), ('tile_edge77', [[8.0, 11.0], [8.0, 12.0]]),
            ('dimension0', [[8.0, 0.0], [9.0, 0.0]]), ('dimension1', [[8.0, 12.0], [9.0, 12.0]])
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.078369326452087, 10.53104832799903), ylim=(-0.3140950984895561, 12.295322555961562)) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.line([[9.0, 0.0], [9.0, 12.0]], id='dimension2', linestyle=(0.0, [4.0, 3.0]))
            c.text('?', [9.5, 6.0], id='label0')
            c.text('1 m', [-0.8, 0.5], id='label1')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane157_C01.png'
        with Canvas(PLANE, xlim=(-2.078369326452087, 10.53104832799903), ylim=(-0.3140950984895561, 12.295322555961562)) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.line([[9.0, 0.0], [9.0, 12.0]], id='dimension2', linestyle=(0.0, [4.0, 3.0]))
            c.text('?', (9.5, 6.0), id='label0')
            c.text('1 m', (-0.8, 0.5), id='label1')
            for object_id, points in [(None, [[8.0, 11.0]]), (None, [[8.0, 12.0]]), (None, [[8.0, 10.0]]), (None, [[8.0, 9.0]]), (None, [[7.999378075890075, 7.085181233462662]]), (None, [[7.999378075890075, 6.132263641112393]]), (None, [[8.0, 5.0]]), (None, [[8.012255340651564, 4.046146749750996]]), (None, [[8.012255340651564, 3.0159655688317883]]), (None, [[8.012255340651564, 2.0372934469585378]]), (None, [[8.0, 1.0]]), (None, [[8.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane157_C02.png'
        with Canvas(PLANE, xlim=(-2.078369326452087, 10.53104832799903), ylim=(-0.3140950984895561, 12.295322555961562)) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.line([[9.0, 0.0], [9.0, 12.0]], id='dimension2', linestyle=(0.0, [4.0, 3.0]))
            c.text('?', (9.5, 6.0), id='label0')
            c.text('1 m', (-0.8, 0.5), id='label1')
            for object_id, points in [(None, [[8.0, 12.0]]), (None, [[8.0, 11.0]]), (None, [[8.0, 10.0]]), (None, [[8.0, 9.0]]), (None, [[8.012255340651564, 8.398662239134655]]), (None, [[8.025132605413056, 7.806308060106108]]), (None, [[8.025132605413056, 7.033672174416702]]), (None, [[8.012255340651564, 6.029245523020474]]), (None, [[8.0, 5.0]]), (None, [[8.012255340651564, 4.046146749750996]]), (None, [[7.999378075890075, 3.067474627877747]]), (None, [[7.999378075890075, 1.9729071231510869]]), (None, [[8.0, 1.0]]), (None, [[8.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane157')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane157().draw(args.output, variant=args.variant))
