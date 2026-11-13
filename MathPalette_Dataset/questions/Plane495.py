"""Collected question Plane495; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane495:
    variants = ('C01', 'C02')

    def __init__(self):
        self._geometry_01 = [
            ('grid_v_0', [[-1.0, -0.5], [-1.0, 5.5]]), ('grid_v_1', [[0.0, -0.5], [0.0, 5.5]]),
            ('grid_v_2', [[1.0, -0.5], [1.0, 5.5]]), ('grid_v_3', [[2.0, -0.5], [2.0, 5.5]]),
            ('grid_v_4', [[3.0, -0.5], [3.0, 5.5]]), ('grid_v_5', [[4.0, -0.5], [4.0, 5.5]]),
            ('grid_v_6', [[5.0, -0.5], [5.0, 5.5]]), ('grid_v_7', [[6.0, -0.5], [6.0, 5.5]]),
            ('grid_v_8', [[7.0, -0.5], [7.0, 5.5]]), ('grid_v_9', [[8.0, -0.5], [8.0, 5.5]]),
            ('grid_v_10', [[9.0, -0.5], [9.0, 5.5]]), ('grid_v_11', [[10.0, -0.5], [10.0, 5.5]]),
            ('grid_v_12', [[11.0, -0.5], [11.0, 5.5]]), ('grid_v_13', [[12.0, -0.5], [12.0, 5.5]]),
            ('grid_v_14', [[13.0, -0.5], [13.0, 5.5]]), ('grid_v_15', [[14.0, -0.5], [14.0, 5.5]]),
            ('grid_v_16', [[15.0, -0.5], [15.0, 5.5]]), ('grid_v_17', [[16.0, -0.5], [16.0, 5.5]]),
            ('grid_v_18', [[17.0, -0.5], [17.0, 5.5]]), ('grid_v_19', [[18.0, -0.5], [18.0, 5.5]]),
            ('grid_v_20', [[19.0, -0.5], [19.0, 5.5]]), ('grid_v_21', [[20.0, -0.5], [20.0, 5.5]]),
            ('grid_v_22', [[21.0, -0.5], [21.0, 5.5]]), ('grid_v_23', [[22.0, -0.5], [22.0, 5.5]]),
            ('grid_v_24', [[23.0, -0.5], [23.0, 5.5]]), ('grid_v_25', [[24.0, -0.5], [24.0, 5.5]]),
            ('grid_v_26', [[25.0, -0.5], [25.0, 5.5]]), ('grid_v_27', [[26.0, -0.5], [26.0, 5.5]]),
            ('grid_v_28', [[27.0, -0.5], [27.0, 5.5]]), ('grid_v_29', [[28.0, -0.5], [28.0, 5.5]]),
            ('grid_v_30', [[29.0, -0.5], [29.0, 5.5]]), ('grid_v_31', [[30.0, -0.5], [30.0, 5.5]]),
            ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]), ('grid_v_33', [[32.0, -0.5], [32.0, 5.5]]),
            ('grid_v_34', [[33.0, -0.5], [33.0, 5.5]]), ('grid_v_35', [[34.0, -0.5], [34.0, 5.5]]),
            ('grid_h_0', [[-0.5, 0.0], [34.0, 0.0]]), ('grid_h_1', [[-0.5, 1.0], [34.0, 1.0]]),
            ('grid_h_2', [[-0.5, 2.0], [34.0, 2.0]]), ('grid_h_3', [[-0.5, 3.0], [34.0, 3.0]]),
            ('grid_h_4', [[-0.5, 4.0], [34.0, 4.0]])
        ]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in self._geometry_01:
            c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_1', [[0, 0], [0, 4]]), ('pattern_2', [[0, 4], [4, 4]]), ('pattern_3', [[4, 4], [4, 0]]), ('pattern_4', [[4, 0], [5, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_45', [[0.0, 0.0]]), ('corner_46', [[0.0, 4.0]]), ('corner_47', [[4.0, 4.0]]), ('corner_48', [[4.0, 0.0]]), ('corner_49', [[5.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(3, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_5', [[5, 0], [5, 3]]), ('pattern_6', [[5, 3], [8, 3]]), ('pattern_7', [[8, 3], [8, 0]]), ('pattern_8', [[8, 0], [9, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_54', [[5.0, 0.0]]), ('corner_55', [[5.0, 3.0]]), ('corner_56', [[8.0, 3.0]]), ('corner_57', [[8.0, 0.0]]), ('corner_58', [[9.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(5, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_9', [[9, 0], [9, 1]]), ('pattern_10', [[9, 1], [10, 1]]), ('pattern_11', [[10, 1], [10, 0]]), ('pattern_12', [[10, 0], [11, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_63', [[9.0, 0.0]]), ('corner_64', [[9.0, 1.0]]), ('corner_65', [[10.0, 1.0]]), ('corner_66', [[10.0, 0.0]]), ('corner_67', [[11.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(7, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_13', [[11, 0], [11, 4]]), ('pattern_14', [[11, 4], [15, 4]]), ('pattern_15', [[15, 4], [15, 0]]), ('pattern_16', [[15, 0], [16, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_72', [[11.0, 0.0]]), ('corner_73', [[11.0, 4.0]]), ('corner_74', [[15.0, 4.0]]), ('corner_75', [[15.0, 0.0]]), ('corner_76', [[16.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(9, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_17', [[16, 0], [16, 3]]), ('pattern_18', [[16, 3], [19, 3]]), ('pattern_19', [[19, 3], [19, 0]]), ('pattern_20', [[19, 0], [20, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_81', [[16.0, 0.0]]), ('corner_82', [[16.0, 3.0]]), ('corner_83', [[19.0, 3.0]]), ('corner_84', [[19.0, 0.0]]), ('corner_85', [[20.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(11, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_21', [[20, 0], [20, 1]]), ('pattern_22', [[20, 1], [21, 1]]), ('pattern_23', [[21, 1], [21, 0]]), ('pattern_24', [[21, 0], [22, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_90', [[20.0, 0.0]]), ('corner_91', [[20.0, 1.0]]), ('corner_92', [[21.0, 1.0]]), ('corner_93', [[21.0, 0.0]]), ('corner_94', [[22.0, 0.0]]), ('choice_A', [[24.0, 2.0]]), ('choice_B', [[26.0, 5.0]]), ('choice_C', [[28.0, 1.0]]), ('choice_D', [[30.0, 2.0]]), ('choice_E', [[32.0, 3.0]])]:
            c.point(points, id=object_id, s=24)
        c.line([[-0.5, 5.0], [34.0, 5.0]], id='grid_h_5', zorder=1, color='#A8A8A8', linewidth=0.5)
        for object_id, text, anchor in [(None, 'A', (24, 2)), (None, 'B', (26, 5)), (None, 'C', (28, 1)), (None, 'D', (30, 2)), (None, 'E', (32, 3))]:
            c.text(text, anchor, id=None, clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.797063415159343, 34.8520402670112), ylim=(-15.829760174418604, 20.819343507751938)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane495_C01.png'
        with Canvas(PLANE, xlim=(-1.797063415159343, 34.8520402670112), ylim=(-15.829760174418604, 20.819343507751938)) as c:
            self._draw_base(c, hi={1: [({0, 1, 2, 3}, {'color': '#2563EB', 'linewidth': 1.5})], 3: [({0, 1, 2, 3}, {'color': '#2563EB', 'linewidth': 1.5})], 5: [({0, 1, 2, 3}, {'color': '#2563EB', 'linewidth': 1.5})], 7: [({0, 1, 2, 3}, {'color': '#EA580C', 'linewidth': 1.5})], 9: [({0, 1, 2, 3}, {'color': '#EA580C', 'linewidth': 1.5})], 11: [({0, 1, 2, 3}, {'color': '#EA580C', 'linewidth': 1.5})]})
            c.point([[28.0, 1.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane495_C02.png'
        with Canvas(PLANE, xlim=(-1.797063415159343, 34.8520402670112), ylim=(-15.829760174418604, 20.819343507751938)) as c:
            self._draw_base(c)
            c.line([[13, 2], [24, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[13.0, 2.0]], zorder=10, s=50, facecolors='#2563EB', edgecolors='#2563EB')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane495')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane495().draw(args.output, variant=args.variant))
