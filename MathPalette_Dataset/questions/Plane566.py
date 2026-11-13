"""Collected question Plane566; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane566:
    variants = ('C01', 'C02')

    def __init__(self):
        self.points = {
            'source0.v00': [10.5, 8.5], 'source0.v01': [12.5, 8.5], 'source0.v02': [12.5, 10.5],
            'source0.v03': [11.5, 10.5], 'source0.v04': [11.5, 11.5], 'source0.v05': [10.5, 11.5],
            'source1.v00': [15.5, 8.5], 'source1.v01': [17.5, 8.5], 'source1.v02': [17.5, 10.5],
            'source1.v03': [16.5, 10.5], 'source1.v04': [16.5, 11.5], 'source1.v05': [15.5, 11.5],
            'option_A.v00': [-1.5, 0.7999999999999998], 'option_A.v01': [0.5, 0.7999999999999998],
            'option_A.v02': [0.5, 1.7999999999999998], 'option_A.v03': [1.5, 1.7999999999999998],
            'option_A.v04': [1.5, 4.8], 'option_A.v05': [-0.5, 4.8], 'option_A.v06': [-0.5, 3.8],
            'option_A.v07': [-1.5, 3.8], 'option_B.v00': [4.0, 1.2999999999999998],
            'option_B.v01': [7.0, 1.2999999999999998], 'option_B.v02': [7.0, 2.3], 'option_B.v03': [9.0, 2.3],
            'option_B.v04': [9.0, 3.3], 'option_B.v05': [10.0, 3.3], 'option_B.v06': [10.0, 4.3],
            'option_B.v07': [7.0, 4.3], 'option_B.v08': [7.0, 3.3], 'option_B.v09': [5.0, 3.3],
            'option_B.v10': [5.0, 2.3], 'option_B.v11': [4.0, 2.3],
            'option_C.v00': [12.5, 0.7999999999999998], 'option_C.v01': [13.5, 0.7999999999999998],
            'option_C.v02': [13.5, -0.20000000000000018], 'option_C.v03': [14.5, -0.20000000000000018],
            'option_C.v04': [14.5, 2.8], 'option_C.v05': [15.5, 2.8], 'option_C.v06': [15.5, 4.8],
            'option_C.v07': [14.5, 4.8], 'option_C.v08': [14.5, 5.8], 'option_C.v09': [13.5, 5.8],
            'option_C.v10': [13.5, 2.8], 'option_C.v11': [12.5, 2.8],
            'option_D.v00': [19.0, 1.7999999999999998], 'option_D.v01': [20.0, 1.7999999999999998],
            'option_D.v02': [20.0, 0.7999999999999998], 'option_D.v03': [21.0, 0.7999999999999998],
            'option_D.v04': [21.0, 1.7999999999999998], 'option_D.v05': [23.0, 1.7999999999999998],
            'option_D.v06': [23.0, 3.8], 'option_D.v07': [22.0, 3.8], 'option_D.v08': [22.0, 4.8],
            'option_D.v09': [21.0, 4.8], 'option_D.v10': [21.0, 3.8], 'option_D.v11': [19.0, 3.8],
            'option_E.v00': [26.5, 0.7999999999999998], 'option_E.v01': [28.5, 0.7999999999999998],
            'option_E.v02': [28.5, 1.7999999999999998], 'option_E.v03': [29.5, 1.7999999999999998],
            'option_E.v04': [29.5, 3.8], 'option_E.v05': [28.5, 3.8], 'option_E.v06': [28.5, 4.8],
            'option_E.v07': [26.5, 4.8]
        }

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-2.2553862960490356, 30.255386296049036), ylim=(-10.605386296049037, 21.905386296049034)) as c:
            for object_id, vertices, codes in [('source0', [self.points['source0.v00'], self.points['source0.v01'], self.points['source0.v02'], self.points['source0.v03'], self.points['source0.v04'], self.points['source0.v05'], self.points['source0.v00']], [1, 2, 2, 2, 2, 2, 79]), ('source1', [self.points['source1.v00'], self.points['source1.v01'], self.points['source1.v02'], self.points['source1.v03'], self.points['source1.v04'], self.points['source1.v05'], self.points['source1.v00']], [1, 2, 2, 2, 2, 2, 79]), ('option_A', [self.points['option_A.v00'], self.points['option_A.v01'], self.points['option_A.v02'], self.points['option_A.v03'], self.points['option_A.v04'], self.points['option_A.v05'], self.points['option_A.v06'], self.points['option_A.v07'], self.points['option_A.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_B', [self.points['option_B.v00'], self.points['option_B.v01'], self.points['option_B.v02'], self.points['option_B.v03'], self.points['option_B.v04'], self.points['option_B.v05'], self.points['option_B.v06'], self.points['option_B.v07'], self.points['option_B.v08'], self.points['option_B.v09'], self.points['option_B.v10'], self.points['option_B.v11'], self.points['option_B.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_C', [self.points['option_C.v00'], self.points['option_C.v01'], self.points['option_C.v02'], self.points['option_C.v03'], self.points['option_C.v04'], self.points['option_C.v05'], self.points['option_C.v06'], self.points['option_C.v07'], self.points['option_C.v08'], self.points['option_C.v09'], self.points['option_C.v10'], self.points['option_C.v11'], self.points['option_C.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [self.points['option_D.v00'], self.points['option_D.v01'], self.points['option_D.v02'], self.points['option_D.v03'], self.points['option_D.v04'], self.points['option_D.v05'], self.points['option_D.v06'], self.points['option_D.v07'], self.points['option_D.v08'], self.points['option_D.v09'], self.points['option_D.v10'], self.points['option_D.v11'], self.points['option_D.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [self.points['option_E.v00'], self.points['option_E.v01'], self.points['option_E.v02'], self.points['option_E.v03'], self.points['option_E.v04'], self.points['option_E.v05'], self.points['option_E.v06'], self.points['option_E.v07'], self.points['option_E.v00']], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id)
            for object_id, text, anchor in [('label_A', 'A', (0, 6.6)), ('label_B', 'B', (7, 6.6)), ('label_C', 'C', (14, 6.6)), ('label_D', 'D', (21, 6.6)), ('label_E', 'E', (28, 6.6))]:
                c.text(text, anchor, id=object_id)
            return c.save(output_path)

    def _draw_choices(self, c, kw=None):
        _kw = kw or {}
        c.path([[10.5, 8.5], [12.5, 8.5], [12.5, 10.5], [11.5, 10.5], [11.5, 11.5], [10.5, 11.5], [10.5, 8.5]], [1, 2, 2, 2, 2, 2, 79], id='source0', zorder=1)
        c.path([[15.5, 8.5], [17.5, 8.5], [17.5, 10.5], [16.5, 10.5], [16.5, 11.5], [15.5, 11.5], [15.5, 8.5]], [1, 2, 2, 2, 2, 2, 79], id='source1', zorder=1, **_kw.get(1, {'edgecolor': '#16A34A'}))
        c.path([[-1.5, 0.7999999999999998], [0.5, 0.7999999999999998], [0.5, 1.7999999999999998], [1.5, 1.7999999999999998], [1.5, 4.8], [-0.5, 4.8], [-0.5, 3.8], [-1.5, 3.8], [-1.5, 0.7999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option_A', zorder=1)
        c.path([[4.0, 1.2999999999999998], [7.0, 1.2999999999999998], [7.0, 2.3], [9.0, 2.3], [9.0, 3.3], [10.0, 3.3], [10.0, 4.3], [7.0, 4.3], [7.0, 3.3], [5.0, 3.3], [5.0, 2.3], [4.0, 2.3], [4.0, 1.2999999999999998]], [1] + [2] * 11 + [79], id='option_B', zorder=1, **_kw.get(3, {'edgecolor': '#16A34A'}))
        for object_id, vertices, codes in [('option_C', [[12.5, 0.7999999999999998], [13.5, 0.7999999999999998], [13.5, -0.20000000000000018], [14.5, -0.20000000000000018], [14.5, 2.8], [15.5, 2.8], [15.5, 4.8], [14.5, 4.8], [14.5, 5.8], [13.5, 5.8], [13.5, 2.8], [12.5, 2.8], [12.5, 0.7999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_D', [[19.0, 1.7999999999999998], [20.0, 1.7999999999999998], [20.0, 0.7999999999999998], [21.0, 0.7999999999999998], [21.0, 1.7999999999999998], [23.0, 1.7999999999999998], [23.0, 3.8], [22.0, 3.8], [22.0, 4.8], [21.0, 4.8], [21.0, 3.8], [19.0, 3.8], [19.0, 1.7999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option_E', [[26.5, 0.7999999999999998], [28.5, 0.7999999999999998], [28.5, 1.7999999999999998], [29.5, 1.7999999999999998], [29.5, 3.8], [28.5, 3.8], [28.5, 4.8], [26.5, 4.8], [26.5, 0.7999999999999998]], [1, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1)
        for object_id, text, anchor in [('label_A', 'A', (0, 6.6)), ('label_B', 'B', (7, 6.6)), ('label_C', 'C', (14, 6.6)), ('label_D', 'D', (21, 6.6)), ('label_E', 'E', (28, 6.6))]:
            c.text(text, anchor, id=object_id, zorder=3)
        c.line([[7.0, 2.3], [7.0, 3.3]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane566_C01.png'
        with Canvas(PLANE, xlim=(-2.2553862960490356, 30.255386296049036), ylim=(-10.605386296049037, 21.905386296049034)) as c:
            self._draw_choices(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane566_C02.png'
        with Canvas(PLANE, xlim=(-2.2553862960490356, 30.255386296049036), ylim=(-10.605386296049037, 21.905386296049034)) as c:
            self._draw_choices(c, kw={1: {'edgecolor': '#2563EB'}, 3: {'edgecolor': '#2563EB'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane566')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane566().draw(args.output, variant=args.variant))
