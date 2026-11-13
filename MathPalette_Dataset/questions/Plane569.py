"""Collected question Plane569; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane569:
    variants = ('C01', 'C02')

    def __init__(self):
        self.points = {
            'source0.v00': [10.5, 8.5], 'source0.v01': [11.5, 8.5], 'source0.v02': [11.5, 10.5],
            'source0.v03': [12.5, 10.5], 'source0.v04': [12.5, 11.5], 'source0.v05': [11.5, 11.5],
            'source0.v06': [11.5, 12.5], 'source0.v07': [10.5, 12.5], 'source1.v00': [15.5, 8.5],
            'source1.v01': [16.5, 8.5], 'source1.v02': [16.5, 10.5], 'source1.v03': [17.5, 10.5],
            'source1.v04': [17.5, 11.5], 'source1.v05': [16.5, 11.5], 'source1.v06': [16.5, 12.5],
            'source1.v07': [15.5, 12.5], 'option_A.v00': [-2.0, 0.2999999999999998],
            'option_A.v01': [2.0, 0.2999999999999998], 'option_A.v02': [2.0, 1.2999999999999998],
            'option_A.v03': [0.0, 1.2999999999999998], 'option_A.v04': [0.0, 3.3],
            'option_A.v05': [-1.0, 3.3], 'option_A.v06': [-1.0, 5.3], 'option_A.v07': [-2.0, 5.3],
            'option_B.v00': [5.0, 1.7999999999999998], 'option_B.v01': [7.0, 1.7999999999999998],
            'option_B.v02': [7.0, 0.7999999999999998], 'option_B.v03': [8.0, 0.7999999999999998],
            'option_B.v04': [8.0, 1.7999999999999998], 'option_B.v05': [9.0, 1.7999999999999998],
            'option_B.v06': [9.0, 3.8], 'option_B.v07': [7.0, 3.8], 'option_B.v08': [7.0, 4.8],
            'option_B.v09': [6.0, 4.8], 'option_B.v10': [6.0, 3.8], 'option_B.v11': [5.0, 3.8],
            'option_C.v00': [11.0, 1.2999999999999998], 'option_C.v01': [12.0, 1.2999999999999998],
            'option_C.v02': [12.0, 0.2999999999999998], 'option_C.v03': [13.0, 0.2999999999999998],
            'option_C.v04': [13.0, 3.3], 'option_C.v05': [17.0, 3.3], 'option_C.v06': [17.0, 4.3],
            'option_C.v07': [15.0, 4.3], 'option_C.v08': [15.0, 5.3], 'option_C.v09': [14.0, 5.3],
            'option_C.v10': [14.0, 4.3], 'option_C.v11': [12.0, 4.3], 'option_C.v12': [12.0, 2.3],
            'option_C.v13': [11.0, 2.3], 'option_D.v00': [18.0, 1.7999999999999998],
            'option_D.v01': [23.0, 1.7999999999999998], 'option_D.v02': [23.0, 2.8],
            'option_D.v03': [24.0, 2.8], 'option_D.v04': [24.0, 3.8], 'option_D.v05': [19.0, 3.8],
            'option_D.v06': [19.0, 2.8], 'option_D.v07': [18.0, 2.8],
            'option_E.v00': [26.5, -0.20000000000000018], 'option_E.v01': [27.5, -0.20000000000000018],
            'option_E.v02': [27.5, 1.7999999999999998], 'option_E.v03': [29.5, 1.7999999999999998],
            'option_E.v04': [29.5, 5.8], 'option_E.v05': [28.5, 5.8], 'option_E.v06': [28.5, 3.8],
            'option_E.v07': [26.5, 3.8]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.7675699459853114, 30.26756994598532), ylim=(-10.367569945985313, 22.667569945985317)) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v06'], self.points['source0.v07'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v06'], self.points['source1.v07'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v12'], self.points['option_C.v13'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label_A', 'A', (0, 6.6)), ('label_B', 'B', (7, 6.6)), ('label_C', 'C', (14, 6.6)), ('label_D', 'D', (21, 6.6)), ('label_E', 'E', (28, 6.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def _draw_choices(self, c, hi=None, kw=None):
        _hi = hi or {}
        _kw = kw or {}
        _defs = [{}, {'edgecolor': '#16A34A'}, {}]
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, vertices, codes) in enumerate([('source0', [[10.5, 8.5], [11.5, 8.5], [11.5, 10.5], [12.5, 10.5], [12.5, 11.5], [11.5, 11.5], [11.5, 12.5], [10.5, 12.5], [10.5, 8.5]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('source1', [[15.5, 8.5], [16.5, 8.5], [16.5, 10.5], [17.5, 10.5], [17.5, 11.5], [16.5, 11.5], [16.5, 12.5], [15.5, 12.5], [15.5, 8.5]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_A', [[-2.0, 0.2999999999999998], [2.0, 0.2999999999999998], [2.0, 1.2999999999999998], [0.0, 1.2999999999999998], [0.0, 3.3], [-1.0, 3.3], [-1.0, 5.3], [-2.0, 5.3], [-2.0, 0.2999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 79])]):
            c.path(vertices, codes, id=object_id, zorder=1, **_ov.get(i, _defs[i]))
        c.path([[5.0, 1.7999999999999998], [7.0, 1.7999999999999998], [7.0, 0.7999999999999998], [8.0, 0.7999999999999998], [8.0, 1.7999999999999998], [9.0, 1.7999999999999998], [9.0, 3.8], [7.0, 3.8], [7.0, 4.8], [6.0, 4.8], [6.0, 3.8], [5.0, 3.8], [5.0, 1.7999999999999998]], [1] + [2] * 11 + [79], id='option_B', zorder=1, edgecolor='#16A34A', **_kw.get(1, {}))
        for object_id, vertices, codes in [('option_C', [[11.0, 1.2999999999999998], [12.0, 1.2999999999999998], [12.0, 0.2999999999999998], [13.0, 0.2999999999999998], [13.0, 3.3], [17.0, 3.3], [17.0, 4.3], [15.0, 4.3], [15.0, 5.3], [14.0, 5.3], [14.0, 4.3], [12.0, 4.3], [12.0, 2.3], [11.0, 2.3], [11.0, 1.2999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [[18.0, 1.7999999999999998], [23.0, 1.7999999999999998], [23.0, 2.8], [24.0, 2.8], [24.0, 3.8], [19.0, 3.8], [19.0, 2.8], [18.0, 2.8], [18.0, 1.7999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [[26.5, -0.20000000000000018], [27.5, -0.20000000000000018], [27.5, 1.7999999999999998], [29.5, 1.7999999999999998], [29.5, 5.8], [28.5, 5.8], [28.5, 3.8], [26.5, 3.8], [26.5, -0.20000000000000018]], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1)
        for object_id, text, anchor in [('label_A', 'A', (0, 6.6)), ('label_B', 'B', (7, 6.6)), ('label_C', 'C', (14, 6.6)), ('label_D', 'D', (21, 6.6)), ('label_E', 'E', (28, 6.6))]:
            c.text(text, anchor, id=object_id, zorder=3)
        c.line([[5.0, 2.8], [9.0, 2.8]], zorder=9, linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', **_kw.get(4, {'color': '#DC2626'}))

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane569_C01.png'
        with Canvas(PLANE, xlim=(-2.7675699459853114, 30.26756994598532), ylim=(-10.367569945985313, 22.667569945985317)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane569_C02.png'
        with Canvas(PLANE, xlim=(-2.7675699459853114, 30.26756994598532), ylim=(-10.367569945985313, 22.667569945985317)) as c:
            self._draw_choices(c, hi={0: [({1}, {})]}, kw={1: {'linewidth': 2.0}, 4: {'color': '#2563EB'}})
            c.line([[5.0, 2.8], [9.0, 2.8]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane569')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane569().draw(args.output, variant=args.variant))
