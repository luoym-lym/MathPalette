"""Collected question Plane497; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane497:
    variants = ('C01', 'C02', 'C03')

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
            ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]), ('grid_h_0', [[-0.5, 0.0], [31.0, 0.0]]),
            ('grid_h_1', [[-0.5, 1.0], [31.0, 1.0]]), ('grid_h_2', [[-0.5, 2.0], [31.0, 2.0]]),
            ('grid_h_3', [[-0.5, 3.0], [31.0, 3.0]]), ('grid_h_4', [[-0.5, 4.0], [31.0, 4.0]])
        ]

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.722205988063724, 31.772842562137793), ylim=(-14.284649057032848, 19.21039949316867)) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
            for object_id, points in [('pattern_1', [[0, 0], [0, 4]]), ('pattern_2', [[0, 4], [4, 4]]), ('pattern_3', [[4, 4], [4, 0]]), ('pattern_4', [[4, 0], [5, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_42', [[0.0, 0.0]]), ('corner_43', [[0.0, 4.0]]), ('corner_44', [[4.0, 4.0]]), ('corner_45', [[4.0, 0.0]]), ('corner_46', [[5.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            for object_id, points in [('pattern_5', [[5, 0], [5, 2]]), ('pattern_6', [[5, 2], [7, 2]]), ('pattern_7', [[7, 2], [7, 0]]), ('pattern_8', [[7, 0], [8, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_51', [[5.0, 0.0]]), ('corner_52', [[5.0, 2.0]]), ('corner_53', [[7.0, 2.0]]), ('corner_54', [[7.0, 0.0]]), ('corner_55', [[8.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            for object_id, points in [('pattern_9', [[8, 0], [8, 1]]), ('pattern_10', [[8, 1], [9, 1]]), ('pattern_11', [[9, 1], [9, 0]]), ('pattern_12', [[9, 0], [10, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_60', [[8.0, 0.0]]), ('corner_61', [[8.0, 1.0]]), ('corner_62', [[9.0, 1.0]]), ('corner_63', [[9.0, 0.0]]), ('corner_64', [[10.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            for object_id, points in [('pattern_13', [[10, 0], [10, 4]]), ('pattern_14', [[10, 4], [14, 4]]), ('pattern_15', [[14, 4], [14, 0]]), ('pattern_16', [[14, 0], [15, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_69', [[10.0, 0.0]]), ('corner_70', [[10.0, 4.0]]), ('corner_71', [[14.0, 4.0]]), ('corner_72', [[14.0, 0.0]]), ('corner_73', [[15.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            for object_id, points in [('pattern_17', [[15, 0], [15, 2]]), ('pattern_18', [[15, 2], [17, 2]]), ('pattern_19', [[17, 2], [17, 0]]), ('pattern_20', [[17, 0], [18, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_78', [[15.0, 0.0]]), ('corner_79', [[15.0, 2.0]]), ('corner_80', [[17.0, 2.0]]), ('corner_81', [[17.0, 0.0]]), ('corner_82', [[18.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            for object_id, points in [('pattern_21', [[18, 0], [18, 1]]), ('pattern_22', [[18, 1], [19, 1]]), ('pattern_23', [[19, 1], [19, 0]]), ('pattern_24', [[19, 0], [20, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_87', [[18.0, 0.0]]), ('corner_88', [[18.0, 1.0]]), ('corner_89', [[19.0, 1.0]]), ('corner_90', [[19.0, 0.0]]), ('corner_91', [[20.0, 0.0]])]:
                c.point(points, id=object_id, s=24)
            c.line([[-0.5, 5.0], [31.0, 5.0]], id='grid_h_5', zorder=1, color='#A8A8A8', linewidth=0.5)
            c.point([[22.0, 2.0]], id='choice_A', s=24)
            c.point([[27.0, 1.0]], id='choice_B', s=24)
            c.text('A', [22, 2], clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15))
            c.text('B', [27, 1], clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15))
            return c.save(output_path)

    def _draw_choices(self, c, hi=None):
        _hi = hi or {}
        for object_id, points in self._geometry_01:
            c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_1', [[0, 0], [0, 4]]), ('pattern_2', [[0, 4], [4, 4]]), ('pattern_3', [[4, 4], [4, 0]]), ('pattern_4', [[4, 0], [5, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_42', [[0.0, 0.0]]), ('corner_43', [[0.0, 4.0]]), ('corner_44', [[4.0, 4.0]]), ('corner_45', [[4.0, 0.0]]), ('corner_46', [[5.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(3, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_5', [[5, 0], [5, 2]]), ('pattern_6', [[5, 2], [7, 2]]), ('pattern_7', [[7, 2], [7, 0]]), ('pattern_8', [[7, 0], [8, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_51', [[5.0, 0.0]]), ('corner_52', [[5.0, 2.0]]), ('corner_53', [[7.0, 2.0]]), ('corner_54', [[7.0, 0.0]]), ('corner_55', [[8.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _ov = {j: s for idxs, s in _hi.get(5, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_9', [[8, 0], [8, 1]]), ('pattern_10', [[8, 1], [9, 1]]), ('pattern_11', [[9, 1], [9, 0]]), ('pattern_12', [[9, 0], [10, 0]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        for object_id, points in [('corner_60', [[8.0, 0.0]]), ('corner_61', [[8.0, 1.0]]), ('corner_62', [[9.0, 1.0]]), ('corner_63', [[9.0, 0.0]]), ('corner_64', [[10.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _defs = [
            {'color': '#2563EB', 'linewidth': 1.5}, {'color': '#2563EB', 'linewidth': 1.5},
            {'color': '#2563EB', 'linewidth': 1.5}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(7, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_13', [[10, 0], [10, 4]]), ('pattern_14', [[10, 4], [14, 4]]), ('pattern_15', [[14, 4], [14, 0]]), ('pattern_16', [[14, 0], [15, 0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        for object_id, points in [('corner_69', [[10.0, 0.0]]), ('corner_70', [[10.0, 4.0]]), ('corner_71', [[14.0, 4.0]]), ('corner_72', [[14.0, 0.0]]), ('corner_73', [[15.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _defs = [
            {'color': '#16A34A', 'linewidth': 1.5}, {'color': '#16A34A', 'linewidth': 1.5},
            {'color': '#16A34A', 'linewidth': 1.5}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(9, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_17', [[15, 0], [15, 2]]), ('pattern_18', [[15, 2], [17, 2]]), ('pattern_19', [[17, 2], [17, 0]]), ('pattern_20', [[17, 0], [18, 0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        for object_id, points in [('corner_78', [[15.0, 0.0]]), ('corner_79', [[15.0, 2.0]]), ('corner_80', [[17.0, 2.0]]), ('corner_81', [[17.0, 0.0]]), ('corner_82', [[18.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        _defs = [
            {'color': '#EA580C', 'linewidth': 1.5}, {'color': '#EA580C', 'linewidth': 1.5},
            {'color': '#EA580C', 'linewidth': 1.5}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(11, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('pattern_21', [[18, 0], [18, 1]]), ('pattern_22', [[18, 1], [19, 1]]), ('pattern_23', [[19, 1], [19, 0]]), ('pattern_24', [[19, 0], [20, 0]])]):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        for object_id, points in [('corner_87', [[18.0, 0.0]]), ('corner_88', [[18.0, 1.0]]), ('corner_89', [[19.0, 1.0]]), ('corner_90', [[19.0, 0.0]]), ('corner_91', [[20.0, 0.0]])]:
            c.point(points, id=object_id, s=24)
        c.line([[-0.5, 5.0], [31.0, 5.0]], id='grid_h_5', zorder=1, color='#A8A8A8', linewidth=0.5)
        c.point([[22.0, 2.0]], id='choice_A', s=24)
        c.point([[27.0, 1.0]], id='choice_B', s=24)
        c.text('A', (22, 2), clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15))
        c.text('B', (27, 1), clip_on=True, fontsize=18.0, fontstyle='italic', offset_pt=(0, -15))
        c.point([[22.0, 2.0]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane497_C01.png'
        with Canvas(PLANE, xlim=(-1.722205988063724, 31.772842562137793), ylim=(-14.284649057032848, 19.21039949316867)) as c:
            self._draw_choices(c, hi={7: [({3}, {'color': '#2563EB', 'linewidth': 1.5})], 9: [({0, 1, 2, 3}, {'color': '#2563EB', 'linewidth': 1.5})], 11: [({0, 1, 2, 3}, {'color': '#2563EB', 'linewidth': 1.5})]})
            c.point([[27.0, 1.0]], zorder=10, s=50, facecolors='#16A34A', edgecolors='#16A34A')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane497_C02.png'
        with Canvas(PLANE, xlim=(-1.722205988063724, 31.772842562137793), ylim=(-14.284649057032848, 19.21039949316867)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane497_C03.png'
        with Canvas(PLANE, xlim=(-1.722205988063724, 31.772842562137793), ylim=(-14.284649057032848, 19.21039949316867)) as c:
            self._draw_choices(c, hi={1: [({0, 1, 2}, {'color': '#2563EB', 'linewidth': 1.5})], 3: [({0, 1, 2}, {'color': '#16A34A', 'linewidth': 1.5})], 5: [({0, 1, 2}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane497')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03'))
    args = parser.parse_args()
    print(Plane497().draw(args.output, variant=args.variant))
