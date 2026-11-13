"""Collected question Plane301; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane301:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in [('wire0_0', [[3.0, 2.0], [2.0, 2.0]]), ('wire0_1', [[2.0, 2.0], [1.0, 2.0]]), ('wire0_2', [[1.0, 2.0], [0.0, 2.0]]), ('wire0_3', [[0.0, 2.0], [0.0, 1.0]]), ('wire0_4', [[0.0, 1.0], [0.0, 0.0]]), ('wire0_5', [[0.0, 0.0], [1.0, 0.0]]), ('wire0_6', [[1.0, 0.0], [2.0, 0.0]]), ('wire0_7', [[2.0, 0.0], [2.0, 1.0]]), ('wire0_8', [[2.0, 1.0], [1.0, 1.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('joint0_0', [3.0, 2.0], 0.055), ('joint0_1', [2.0, 2.0], 0.055), ('joint0_2', [1.0, 2.0], 0.055), ('joint0_3', [0.0, 2.0], 0.055), ('joint0_4', [0.0, 1.0], 0.055), ('joint0_5', [0.0, 0.0], 0.055), ('joint0_6', [1.0, 0.0], 0.055), ('joint0_7', [2.0, 0.0], 0.055), ('joint0_8', [2.0, 1.0], 0.055), ('joint0_9', [1.0, 1.0], 0.055)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        for object_id, points in [('wire1_0', [[6.0, 0.0], [6.0, 1.0]]), ('wire1_1', [[6.0, 1.0], [6.0, 2.0]]), ('wire1_2', [[6.0, 2.0], [7.0, 2.0]]), ('wire1_3', [[7.0, 2.0], [7.0, 1.0]]), ('wire1_4', [[7.0, 1.0], [8.0, 1.0]]), ('wire1_5', [[8.0, 1.0], [8.0, 2.0]]), ('wire1_6', [[8.0, 2.0], [9.0, 2.0]]), ('wire1_7', [[9.0, 2.0], [9.0, 1.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('joint1_0', [6.0, 0.0], 0.055), ('joint1_1', [6.0, 1.0], 0.055), ('joint1_2', [6.0, 2.0], 0.055), ('joint1_3', [7.0, 2.0], 0.055), ('joint1_4', [7.0, 1.0], 0.055), ('joint1_5', [8.0, 1.0], 0.055), ('joint1_6', [8.0, 2.0], 0.055), ('joint1_7', [9.0, 2.0], 0.055), ('joint1_8', [9.0, 1.0], 0.055)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        _ov = {j: s for idxs, s in _hi.get(4, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('wire2_0', [[12.0, 2.0], [12.0, 3.0]]), ('wire2_1', [[12.0, 3.0], [13.0, 3.0]]), ('wire2_2', [[13.0, 3.0], [14.0, 3.0]]), ('wire2_3', [[14.0, 3.0], [15.0, 3.0]]), ('wire2_4', [[15.0, 3.0], [15.0, 2.0]]), ('wire2_5', [[15.0, 2.0], [15.0, 1.0]]), ('wire2_6', [[15.0, 1.0], [15.0, 0.0]]), ('wire2_7', [[15.0, 0.0], [14.0, 0.0]]), ('wire2_8', [[14.0, 0.0], [13.0, 0.0]]), ('wire2_9', [[13.0, 0.0], [13.0, 1.0]]), ('wire2_10', [[13.0, 1.0], [14.0, 1.0]]), ('wire2_11', [[14.0, 1.0], [14.0, 2.0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        _ov = {j: s for idxs, s in _hi.get(5, ()) for j in idxs}
        for i, (object_id, center, radius) in enumerate([('joint2_0', [12.0, 2.0], 0.055), ('joint2_1', [12.0, 3.0], 0.055), ('joint2_2', [13.0, 3.0], 0.055), ('joint2_3', [14.0, 3.0], 0.055), ('joint2_4', [15.0, 3.0], 0.055), ('joint2_5', [15.0, 2.0], 0.055), ('joint2_6', [15.0, 1.0], 0.055), ('joint2_7', [15.0, 0.0], 0.055), ('joint2_8', [14.0, 0.0], 0.055), ('joint2_9', [13.0, 0.0], 0.055), ('joint2_10', [13.0, 1.0], 0.055), ('joint2_11', [14.0, 1.0], 0.055), ('joint2_12', [14.0, 2.0], 0.055)]):
            c.circle(center, radius, id=object_id, facecolor='black', **_ov[i]) if i in _ov else c.circle(center, radius, id=object_id, facecolor='black')
        for object_id, points in [('wire3_0', [[19.0, 2.0], [19.0, 3.0]]), ('wire3_1', [[19.0, 3.0], [20.0, 3.0]]), ('wire3_2', [[20.0, 3.0], [21.0, 3.0]]), ('wire3_3', [[21.0, 3.0], [21.0, 2.0]]), ('wire3_4', [[21.0, 2.0], [21.0, 1.0]]), ('wire3_5', [[21.0, 1.0], [21.0, 0.0]]), ('wire3_6', [[21.0, 0.0], [20.0, 0.0]]), ('wire3_7', [[20.0, 0.0], [19.0, 0.0]]), ('wire3_8', [[19.0, 0.0], [18.0, 0.0]]), ('wire3_9', [[18.0, 0.0], [18.0, 1.0]]), ('wire3_10', [[18.0, 1.0], [19.0, 1.0]]), ('wire3_11', [[19.0, 1.0], [20.0, 1.0]]), ('wire3_12', [[20.0, 1.0], [20.0, 2.0]])]:
            c.line(points, id=object_id)
        for object_id, center, radius in [('joint3_0', [19.0, 2.0], 0.055), ('joint3_1', [19.0, 3.0], 0.055), ('joint3_2', [20.0, 3.0], 0.055), ('joint3_3', [21.0, 3.0], 0.055), ('joint3_4', [21.0, 2.0], 0.055), ('joint3_5', [21.0, 1.0], 0.055), ('joint3_6', [21.0, 0.0], 0.055), ('joint3_7', [20.0, 0.0], 0.055), ('joint3_8', [19.0, 0.0], 0.055), ('joint3_9', [18.0, 0.0], 0.055), ('joint3_10', [18.0, 1.0], 0.055), ('joint3_11', [19.0, 1.0], 0.055), ('joint3_12', [20.0, 1.0], 0.055), ('joint3_13', [20.0, 2.0], 0.055)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        _defs = [
            {'color': '#EA580C'}, {'color': '#EA580C'}, {'color': '#EA580C'}, {'color': '#EA580C'},
            {'color': '#EA580C'}, {}, {}, {}, {}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(8, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('wire4_0', [[24.0, 2.0], [24.0, 1.0]]), ('wire4_1', [[24.0, 1.0], [24.0, 0.0]]), ('wire4_2', [[24.0, 0.0], [25.0, 0.0]]), ('wire4_3', [[25.0, 0.0], [25.0, 1.0]]), ('wire4_4', [[25.0, 1.0], [25.0, 2.0]]), ('wire4_5', [[25.0, 2.0], [26.0, 2.0]]), ('wire4_6', [[26.0, 2.0], [26.0, 1.0]]), ('wire4_7', [[26.0, 1.0], [27.0, 1.0]]), ('wire4_8', [[27.0, 1.0], [28.0, 1.0]]), ('wire4_9', [[28.0, 1.0], [28.0, 0.0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        for object_id, center, radius in [('joint4_0', [24.0, 2.0], 0.055), ('joint4_1', [24.0, 1.0], 0.055), ('joint4_2', [24.0, 0.0], 0.055), ('joint4_3', [25.0, 0.0], 0.055), ('joint4_4', [25.0, 1.0], 0.055), ('joint4_5', [25.0, 2.0], 0.055), ('joint4_6', [26.0, 2.0], 0.055), ('joint4_7', [26.0, 1.0], 0.055), ('joint4_8', [27.0, 1.0], 0.055), ('joint4_9', [28.0, 1.0], 0.055), ('joint4_10', [28.0, 0.0], 0.055)]:
            c.circle(center, radius, id=object_id, facecolor='black')
        for object_id, text, anchor in [('label0', '(A)', (-1.0, 0.0)), ('label1', '(B)', (5.0, 0.0)), ('label2', '(C)', (11.0, 0.0)), ('label3', '(D)', (17.0, 0.0)), ('label4', '(E)', (23.0, 0.0))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={8: [({0, 1, 2, 3, 4}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C01.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={4: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#2563EB'})], 5: [({3}, {'edgecolor': '#2563EB'})], 8: [({0, 1, 2, 3, 4}, {})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C02.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={8: [({5, 6, 7, 8, 9}, {'color': '#EA580C'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C03.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C04.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={8: [({0, 1, 2, 3, 4, 5}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C05.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={8: [({6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane301_C06.png'
        with Canvas(PLANE, xlim=(-2.3178967481021218, 28.78384518088098), ylim=(-14.217392114093188, 16.884349814889916)) as c:
            self._draw_base(c, hi={8: [({7, 8, 9}, {'color': '#EA580C'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane301')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane301().draw(args.output, variant=args.variant))
