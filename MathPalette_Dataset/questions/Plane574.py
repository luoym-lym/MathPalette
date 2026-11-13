"""Collected question Plane574; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane574:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self._samples_001 = [
            [0.0, 0.0], [400.0, 0.0], [800.0, 0.0], [1200.0, 0.0], [1200.0, 80.0], [1302.0, 160.0],
            [1302.0, 240.0], [1302.0, 300.0], [1359.0, 360.0], [1359.0, 420.0], [1359.0, 480.0],
            [1200.0, 540.0], [1200.0, 600.0], [1200.0, 660.0], [1041.0, 720.0], [1041.0, 780.0],
            [1041.0, 840.0], [1098.0, 900.0], [1098.0, 960.0], [1098.0, 1040.0], [1200.0, 1120.0],
            [1200.0, 1200.0], [1120.0, 1200.0], [1040.0, 1098.0], [960.0, 1098.0], [900.0, 1098.0],
            [840.0, 1041.0], [780.0, 1041.0], [720.0, 1041.0], [660.0, 1200.0], [600.0, 1200.0],
            [540.0, 1200.0], [480.0, 1359.0], [420.0, 1359.0], [360.0, 1359.0], [300.0, 1302.0],
            [240.0, 1302.0], [160.0, 1302.0], [80.0, 1200.0], [0.0, 1200.0], [0.0, 800.0], [0.0, 400.0],
            [0.0, 0.0], [0.0, 0.0]
        ]
        self._samples_002 = [
            [1850.0, 0.0], [2250.0, 0.0], [2650.0, 0.0], [3050.0, 0.0], [3050.0, 120.0], [2873.0, 240.0],
            [2873.0, 360.0], [2873.0, 440.0], [3050.0, 520.0], [3050.0, 600.0], [3050.0, 680.0],
            [3227.0, 760.0], [3227.0, 840.0], [3227.0, 960.0], [3050.0, 1080.0], [3050.0, 1200.0],
            [3000.0, 1200.0], [2950.0, 1284.0], [2900.0, 1284.0], [2850.0, 1284.0], [2800.0, 1200.0],
            [2750.0, 1200.0], [2700.0, 1200.0], [2650.0, 1116.0], [2600.0, 1116.0], [2550.0, 1116.0],
            [2500.0, 1200.0], [2450.0, 1200.0], [2400.0, 1200.0], [2350.0, 1284.0], [2300.0, 1284.0],
            [2250.0, 1284.0], [2200.0, 1200.0], [2150.0, 1200.0], [2100.0, 1200.0], [2050.0, 1116.0],
            [2000.0, 1116.0], [1950.0, 1116.0], [1900.0, 1200.0], [1850.0, 1200.0], [1850.0, 800.0],
            [1850.0, 400.0], [1850.0, 0.0], [1850.0, 0.0]
        ]
        self._samples_003 = [
            [3700.0, 0.0], [4100.0, 0.0], [4500.0, 0.0], [4900.0, 0.0], [4900.0, 120.0], [5077.0, 240.0],
            [5077.0, 360.0], [5077.0, 440.0], [4900.0, 520.0], [4900.0, 600.0], [4900.0, 680.0],
            [4723.0, 760.0], [4723.0, 840.0], [4723.0, 960.0], [4900.0, 1080.0], [4900.0, 1200.0],
            [4820.0, 1200.0], [4740.0, 1302.0], [4660.0, 1302.0], [4600.0, 1302.0], [4540.0, 1359.0],
            [4480.0, 1359.0], [4420.0, 1359.0], [4360.0, 1200.0], [4300.0, 1200.0], [4240.0, 1200.0],
            [4180.0, 1041.0], [4120.0, 1041.0], [4060.0, 1041.0], [4000.0, 1098.0], [3940.0, 1098.0],
            [3860.0, 1098.0], [3780.0, 1200.0], [3700.0, 1200.0], [3700.0, 800.0], [3700.0, 400.0],
            [3700.0, 0.0], [3700.0, 0.0]
        ]
        self._samples_004 = [
            [5550.0, 0.0], [5950.0, 0.0], [6350.0, 0.0], [6750.0, 0.0], [6750.0, 80.0], [6852.0, 160.0],
            [6852.0, 240.0], [6852.0, 300.0], [6909.0, 360.0], [6909.0, 420.0], [6909.0, 480.0],
            [6750.0, 540.0], [6750.0, 600.0], [6750.0, 660.0], [6591.0, 720.0], [6591.0, 780.0],
            [6591.0, 840.0], [6648.0, 900.0], [6648.0, 960.0], [6648.0, 1040.0], [6750.0, 1120.0],
            [6750.0, 1200.0], [6630.0, 1200.0], [6510.0, 1377.0], [6390.0, 1377.0], [6310.0, 1377.0],
            [6230.0, 1200.0], [6150.0, 1200.0], [6070.0, 1200.0], [5990.0, 1023.0], [5910.0, 1023.0],
            [5790.0, 1023.0], [5670.0, 1200.0], [5550.0, 1200.0], [5550.0, 800.0], [5550.0, 400.0],
            [5550.0, 0.0], [5550.0, 0.0]
        ]
        self._samples_005 = [
            [7400.0, 0.0], [7800.0, 0.0], [8200.0, 0.0], [8600.0, 0.0], [8600.0, 80.0], [8498.0, 160.0],
            [8498.0, 240.0], [8498.0, 300.0], [8441.0, 360.0], [8441.0, 420.0], [8441.0, 480.0],
            [8600.0, 540.0], [8600.0, 600.0], [8600.0, 660.0], [8759.0, 720.0], [8759.0, 780.0],
            [8759.0, 840.0], [8702.0, 900.0], [8702.0, 960.0], [8702.0, 1040.0], [8600.0, 1120.0],
            [8600.0, 1200.0], [8520.0, 1200.0], [8440.0, 1302.0], [8360.0, 1302.0], [8300.0, 1302.0],
            [8240.0, 1359.0], [8180.0, 1359.0], [8120.0, 1359.0], [8060.0, 1200.0], [8000.0, 1200.0],
            [7940.0, 1200.0], [7880.0, 1041.0], [7820.0, 1041.0], [7760.0, 1041.0], [7700.0, 1098.0],
            [7640.0, 1098.0], [7560.0, 1098.0], [7480.0, 1200.0], [7400.0, 1200.0], [7400.0, 800.0],
            [7400.0, 400.0], [7400.0, 0.0], [7400.0, 0.0]
        ]
        self._geometry_02 = [1] + [4] * 42 + [79]
        self._geometry_06 = [1] + [4] * 36 + [79]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _defs = [{}, {}, {'edgecolor': '#DC2626', 'linewidth': 2.0}, {}, {}]
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, vertices, codes) in enumerate([('piece_A', self._samples_001, self._geometry_02), ('piece_B', self._samples_002, self._geometry_02), ('piece_C', self._samples_003, self._geometry_06), ('piece_D', self._samples_004, self._geometry_06), ('piece_E', self._samples_005, self._geometry_02)]):
            c.path(vertices, codes, id=object_id, zorder=1, joinstyle='round', **_ov.get(i, _defs[i]))
        for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
            c.text(text, anchor, id=object_id, zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({2}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C01.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C02.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({2}, {'edgecolor': '#DC2626', 'linewidth': 3.0})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C03.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({3, 4}, {'edgecolor': '#16A34A'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C04.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({0, 1, 3, 4}, {'edgecolor': '#EA580C'}), ({2}, {'edgecolor': '#2563EB', 'linewidth': 2.0})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C05.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({0, 4}, {'edgecolor': '#16A34A'})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane574_C06.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4149.622093023256, 5053.684593023256)) as c:
            self._draw_base(c, hi={0: [({2}, {'edgecolor': '#DC2626', 'linewidth': 3.0}), ({3, 4}, {'edgecolor': '#16A34A'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane574')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane574().draw(args.output, variant=args.variant))
