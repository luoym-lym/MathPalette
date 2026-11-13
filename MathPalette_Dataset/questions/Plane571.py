"""Collected question Plane571; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane571:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self._samples_001 = [
            [0.0, 0.0], [400.0, 0.0], [800.0, 0.0], [1200.0, 0.0], [1200.0, 90.0], [1371.0, 180.0],
            [1371.0, 270.0], [1371.0, 380.0], [1200.0, 490.0], [1200.0, 600.0], [1200.0, 710.0],
            [1029.0, 820.0], [1029.0, 930.0], [1029.0, 1020.0], [1200.0, 1110.0], [1200.0, 1200.0],
            [1070.0, 1200.0], [940.0, 1083.0], [810.0, 1083.0], [740.0, 1083.0], [670.0, 1200.0],
            [600.0, 1200.0], [530.0, 1200.0], [460.0, 1317.0], [390.0, 1317.0], [260.0, 1317.0],
            [130.0, 1200.0], [0.0, 1200.0], [0.0, 800.0], [0.0, 400.0], [0.0, 0.0], [0.0, 0.0]
        ]
        self._samples_002 = [
            [1850.0, 0.0], [2250.0, 0.0], [2650.0, 0.0], [3050.0, 0.0], [3050.0, 80.0], [2966.0, 160.0],
            [2966.0, 240.0], [2966.0, 300.0], [2897.0, 360.0], [2897.0, 420.0], [2897.0, 480.0],
            [3050.0, 540.0], [3050.0, 600.0], [3050.0, 660.0], [3203.0, 720.0], [3203.0, 780.0],
            [3203.0, 840.0], [3134.0, 900.0], [3134.0, 960.0], [3134.0, 1040.0], [3050.0, 1120.0],
            [3050.0, 1200.0], [2960.0, 1200.0], [2870.0, 1371.0], [2780.0, 1371.0], [2670.0, 1371.0],
            [2560.0, 1200.0], [2450.0, 1200.0], [2340.0, 1200.0], [2230.0, 1029.0], [2120.0, 1029.0],
            [2030.0, 1029.0], [1940.0, 1200.0], [1850.0, 1200.0], [1850.0, 800.0], [1850.0, 400.0],
            [1850.0, 0.0], [1850.0, 0.0]
        ]
        self._samples_003 = [
            [3700.0, 0.0], [4100.0, 0.0], [4500.0, 0.0], [4900.0, 0.0], [4900.0, 90.0], [5071.0, 180.0],
            [5071.0, 270.0], [5071.0, 380.0], [4900.0, 490.0], [4900.0, 600.0], [4900.0, 710.0],
            [4729.0, 820.0], [4729.0, 930.0], [4729.0, 1020.0], [4900.0, 1110.0], [4900.0, 1200.0],
            [4850.0, 1200.0], [4800.0, 1290.0], [4750.0, 1290.0], [4700.0, 1290.0], [4650.0, 1200.0],
            [4600.0, 1200.0], [4550.0, 1200.0], [4500.0, 1110.0], [4450.0, 1110.0], [4400.0, 1110.0],
            [4350.0, 1200.0], [4300.0, 1200.0], [4250.0, 1200.0], [4200.0, 1290.0], [4150.0, 1290.0],
            [4100.0, 1290.0], [4050.0, 1200.0], [4000.0, 1200.0], [3950.0, 1200.0], [3900.0, 1110.0],
            [3850.0, 1110.0], [3800.0, 1110.0], [3750.0, 1200.0], [3700.0, 1200.0], [3700.0, 800.0],
            [3700.0, 400.0], [3700.0, 0.0], [3700.0, 0.0]
        ]
        self._samples_004 = [
            [5550.0, 0.0], [5950.0, 0.0], [6350.0, 0.0], [6750.0, 0.0], [6750.0, 50.0], [6840.0, 100.0],
            [6840.0, 150.0], [6840.0, 200.0], [6750.0, 250.0], [6750.0, 300.0], [6750.0, 350.0],
            [6660.0, 400.0], [6660.0, 450.0], [6660.0, 500.0], [6750.0, 550.0], [6750.0, 600.0],
            [6750.0, 650.0], [6840.0, 700.0], [6840.0, 750.0], [6840.0, 800.0], [6750.0, 850.0],
            [6750.0, 900.0], [6750.0, 950.0], [6660.0, 1000.0], [6660.0, 1050.0], [6660.0, 1100.0],
            [6750.0, 1150.0], [6750.0, 1200.0], [6670.0, 1200.0], [6590.0, 1116.0], [6510.0, 1116.0],
            [6450.0, 1116.0], [6390.0, 1047.0], [6330.0, 1047.0], [6270.0, 1047.0], [6210.0, 1200.0],
            [6150.0, 1200.0], [6090.0, 1200.0], [6030.0, 1353.0], [5970.0, 1353.0], [5910.0, 1353.0],
            [5850.0, 1284.0], [5790.0, 1284.0], [5710.0, 1284.0], [5630.0, 1200.0], [5550.0, 1200.0],
            [5550.0, 800.0], [5550.0, 400.0], [5550.0, 0.0], [5550.0, 0.0]
        ]
        self._samples_005 = [
            [7400.0, 0.0], [7800.0, 0.0], [8200.0, 0.0], [8600.0, 0.0], [8600.0, 90.0], [8771.0, 180.0],
            [8771.0, 270.0], [8771.0, 380.0], [8600.0, 490.0], [8600.0, 600.0], [8600.0, 710.0],
            [8429.0, 820.0], [8429.0, 930.0], [8429.0, 1020.0], [8600.0, 1110.0], [8600.0, 1200.0],
            [8510.0, 1200.0], [8420.0, 1371.0], [8330.0, 1371.0], [8220.0, 1371.0], [8110.0, 1200.0],
            [8000.0, 1200.0], [7890.0, 1200.0], [7780.0, 1029.0], [7670.0, 1029.0], [7580.0, 1029.0],
            [7490.0, 1200.0], [7400.0, 1200.0], [7400.0, 800.0], [7400.0, 400.0], [7400.0, 0.0], [7400.0, 0.0]
        ]
        self._samples_006 = self._samples_001[3:-4]
        self._samples_007 = self._samples_002[3:-4]
        self._samples_008 = [
            [4899.999999999999, 1199.9999999999989], [4849.999999999999, 1199.9999999999989],
            [4799.999999999999, 1289.9999999999989], [4749.999999999999, 1289.9999999999989],
            [4699.999999999999, 1289.9999999999989], [4649.999999999999, 1199.9999999999989],
            [4599.999999999999, 1199.9999999999989], [4549.999999999999, 1199.9999999999989],
            [4499.999999999999, 1109.9999999999989], [4449.999999999999, 1109.9999999999989],
            [4399.999999999999, 1109.9999999999989], [4349.999999999999, 1199.9999999999989],
            [4299.999999999999, 1199.9999999999989], [4249.999999999999, 1199.9999999999989],
            [4199.999999999999, 1289.9999999999989], [4149.999999999999, 1289.9999999999989],
            [4099.999999999999, 1289.9999999999989], [4049.9999999999995, 1199.9999999999989],
            [3999.9999999999995, 1199.9999999999989], [3949.9999999999995, 1199.9999999999989],
            [3899.9999999999995, 1109.9999999999989], [3849.9999999999995, 1109.9999999999989],
            [3799.9999999999995, 1109.9999999999989], [3749.9999999999995, 1199.9999999999989],
            [3699.9999999999995, 1199.9999999999989], [3699.9999999999995, 799.999999999999],
            [3699.9999999999995, 399.99999999999903], [3699.9999999999995, -9.094947017729282e-13]
        ]
        self._samples_009 = self._samples_004[3:-4]
        self._samples_010 = self._samples_005[3:-4]
        self._samples_011 = [
            [4899.999999999999, -9.094947017729282e-13], [4899.999999999999, 89.99999999999908],
            [5070.999999999999, 179.99999999999906], [5070.999999999999, 269.99999999999903],
            [5070.999999999999, 379.99999999999903], [4899.999999999999, 489.99999999999903],
            [4899.999999999999, 599.999999999999], [4899.999999999999, 709.999999999999],
            [4728.999999999999, 819.999999999999], [4728.999999999999, 929.999999999999],
            [4728.999999999999, 1019.999999999999], [4899.999999999999, 1109.9999999999989],
            [4899.999999999999, 1199.9999999999989]
        ]
        self._samples_012 = [
            [8599.999999999998, -9.094947017729282e-13], [8599.999999999998, 89.99999999999908],
            [8770.999999999998, 179.99999999999906], [8770.999999999998, 269.99999999999903],
            [8770.999999999998, 379.99999999999903], [8599.999999999998, 489.99999999999903],
            [8599.999999999998, 599.999999999999], [8599.999999999998, 709.999999999999],
            [8428.999999999998, 819.999999999999], [8428.999999999998, 929.999999999999],
            [8428.999999999998, 1019.999999999999], [8599.999999999998, 1109.9999999999989],
            [8599.999999999998, 1199.9999999999989]
        ]
        self._samples_013 = [
            [8599.999999999998, 1199.9999999999989], [8509.999999999998, 1199.9999999999989],
            [8419.999999999998, 1370.9999999999989], [8329.999999999998, 1370.9999999999989],
            [8219.999999999998, 1370.9999999999989], [8109.999999999999, 1199.9999999999989],
            [7999.999999999999, 1199.9999999999989], [7889.999999999999, 1199.9999999999989],
            [7779.999999999999, 1028.9999999999989], [7669.999999999999, 1028.9999999999989],
            [7579.999999999999, 1028.9999999999989], [7489.999999999999, 1199.9999999999989],
            [7399.999999999999, 1199.9999999999989], [7399.999999999999, 799.999999999999],
            [7399.999999999999, 399.99999999999903], [7399.999999999999, -9.094947017729282e-13]
        ]
        self._geometry_02 = [1] + [4] * 30 + [79]
        self._geometry_04 = [1] + [4] * 36 + [79]
        self._geometry_06 = [1] + [4] * 42 + [79]
        self._geometry_08 = [1] + [4] * 48 + [79]
        self._g01 = [1] + [4] * 24
        self._g02 = [1] + [4] * 30
        self._g03 = [1] + [4] * 27
        self._g04 = [1] + [4] * 42

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            for object_id, vertices, codes in [('piece_A', self._samples_001, self._geometry_02), ('piece_B', self._samples_002, self._geometry_04), ('piece_C', self._samples_003, self._geometry_06), ('piece_D', self._samples_004, self._geometry_08), ('piece_E', self._samples_005, self._geometry_02)]:
                c.path(vertices, codes, id=object_id, zorder=1, joinstyle='round')
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane571_C01.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            c.path(self._samples_001, self._geometry_02, id='piece_A', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[0.0, -9.094947017729282e-13], [399.99999999999994, -9.094947017729282e-13], [799.9999999999999, -9.094947017729282e-13], [1199.9999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_006, self._g01, id='piece_A', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[0.0, 1199.9999999999989], [0.0, 799.999999999999], [0.0, 399.99999999999903], [0.0, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_002, self._geometry_04, id='piece_B', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[1849.9999999999998, -9.094947017729282e-13], [2249.9999999999995, -9.094947017729282e-13], [2649.9999999999995, -9.094947017729282e-13], [3049.9999999999995, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_B', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_007, self._g02, id='piece_B', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[1849.9999999999998, 1199.9999999999989], [1849.9999999999998, 799.999999999999], [1849.9999999999998, 399.99999999999903], [1849.9999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_B', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_003, self._geometry_06, id='piece_C', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[3699.9999999999995, -9.094947017729282e-13], [4099.999999999999, -9.094947017729282e-13], [4499.999999999999, -9.094947017729282e-13], [4899.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_011, [1] + [4] * 12, id='piece_C', zorder=1, edgecolor='#DC2626', linewidth=2.0, joinstyle='round', fill=False)
            c.path(self._samples_008, self._g03, id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_004, self._geometry_08, id='piece_D', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[5549.999999999999, -9.094947017729282e-13], [5949.999999999999, -9.094947017729282e-13], [6349.999999999999, -9.094947017729282e-13], [6749.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_009, self._g04, id='piece_D', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[5549.999999999999, 1199.9999999999989], [5549.999999999999, 799.999999999999], [5549.999999999999, 399.99999999999903], [5549.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_005, self._geometry_02, id='piece_E', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[7399.999999999999, -9.094947017729282e-13], [7799.999999999999, -9.094947017729282e-13], [8199.999999999998, -9.094947017729282e-13], [8599.999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_010, self._g01, id='piece_E', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[7399.999999999999, 1199.9999999999989], [7399.999999999999, 799.999999999999], [7399.999999999999, 399.99999999999903], [7399.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane571_C02.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            c.path(self._samples_001, self._geometry_02, id='piece_A', zorder=1, joinstyle='round')
            c.path(self._samples_002, self._geometry_04, id='piece_B', zorder=1, joinstyle='round')
            c.path(self._samples_003, self._geometry_06, id='piece_C', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[3699.9999999999995, -9.094947017729282e-13], [4099.999999999999, -9.094947017729282e-13], [4499.999999999999, -9.094947017729282e-13], [4899.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_011, [1] + [4] * 12, id='piece_C', zorder=1, edgecolor='#DC2626', linewidth=2.0, joinstyle='round', fill=False)
            c.path(self._samples_008, self._g03, id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_004, self._geometry_08, id='piece_D', zorder=1, joinstyle='round')
            c.path(self._samples_005, self._geometry_02, id='piece_E', zorder=1, joinstyle='round')
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane571_C03.png'
        _geometry_11 = [
            [5549.999999999999, -9.094947017729282e-13], [5949.999999999999, -9.094947017729282e-13],
            [6349.999999999999, -9.094947017729282e-13], [6749.999999999999, -9.094947017729282e-13],
            [6749.999999999999, 49.99999999999908], [6839.999999999999, 99.99999999999908],
            [6839.999999999999, 149.99999999999906], [6839.999999999999, 199.99999999999906],
            [6749.999999999999, 249.99999999999906], [6749.999999999999, 299.99999999999903],
            [6749.999999999999, 349.99999999999903], [6659.999999999999, 399.99999999999903],
            [6659.999999999999, 449.99999999999903], [6659.999999999999, 499.99999999999903],
            [6749.999999999999, 549.999999999999], [6749.999999999999, 599.999999999999],
            [6749.999999999999, 649.999999999999], [6839.999999999999, 699.999999999999],
            [6839.999999999999, 749.999999999999], [6839.999999999999, 799.999999999999],
            [6749.999999999999, 849.999999999999], [6749.999999999999, 899.999999999999],
            [6749.999999999999, 949.999999999999], [6659.999999999999, 999.999999999999],
            [6659.999999999999, 1049.9999999999989], [6659.999999999999, 1099.9999999999989],
            [6749.999999999999, 1149.9999999999989], [6749.999999999999, 1199.9999999999989]
        ]
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            c.path(self._samples_001, self._geometry_02, id='piece_A', zorder=1, joinstyle='round')
            c.path(self._samples_002, self._geometry_04, id='piece_B', zorder=1, joinstyle='round')
            c.path(self._samples_003, self._geometry_06, id='piece_C', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[3699.9999999999995, -9.094947017729282e-13], [4099.999999999999, -9.094947017729282e-13], [4499.999999999999, -9.094947017729282e-13], [4899.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_011, [1] + [4] * 12, id='piece_C', zorder=1, edgecolor='#DC2626', linewidth=2.0, joinstyle='round', fill=False)
            c.path(self._samples_008, self._g03, id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_004, self._geometry_08, id='piece_D', zorder=1, edgecolor='none', joinstyle='round')
            c.path(_geometry_11, self._g03, id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path([[6749.999999999999, 1199.9999999999989], [6669.999999999999, 1199.9999999999989], [6589.999999999999, 1115.9999999999989], [6509.999999999999, 1115.9999999999989], [6449.999999999999, 1115.9999999999989], [6389.999999999999, 1046.9999999999989], [6329.999999999999, 1046.9999999999989], [6269.999999999999, 1046.9999999999989], [6209.999999999999, 1199.9999999999989], [6149.999999999999, 1199.9999999999989], [6089.999999999999, 1199.9999999999989], [6029.999999999999, 1352.9999999999989], [5969.999999999999, 1352.9999999999989], [5909.999999999999, 1352.9999999999989], [5849.999999999999, 1283.9999999999989], [5789.999999999999, 1283.9999999999989], [5709.999999999999, 1283.9999999999989], [5629.999999999999, 1199.9999999999989], [5549.999999999999, 1199.9999999999989]], [1] + [4] * 18, id='piece_D', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[5549.999999999999, 1199.9999999999989], [5549.999999999999, 799.999999999999], [5549.999999999999, 399.99999999999903], [5549.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_005, self._geometry_02, id='piece_E', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[7399.999999999999, -9.094947017729282e-13], [7799.999999999999, -9.094947017729282e-13], [8199.999999999998, -9.094947017729282e-13], [8599.999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_012, [1] + [4] * 12, id='piece_E', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path(self._samples_013, [1] + [4] * 15, id='piece_E', zorder=1, joinstyle='round', fill=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane571_C04.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            c.path(self._samples_001, self._geometry_02, id='piece_A', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[0.0, -9.094947017729282e-13], [399.99999999999994, -9.094947017729282e-13], [799.9999999999999, -9.094947017729282e-13], [1199.9999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_006, self._g01, id='piece_A', zorder=1, edgecolor='#EA580C', joinstyle='round', fill=False)
            c.path([[0.0, 1199.9999999999989], [0.0, 799.999999999999], [0.0, 399.99999999999903], [0.0, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_002, self._geometry_04, id='piece_B', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[1849.9999999999998, -9.094947017729282e-13], [2249.9999999999995, -9.094947017729282e-13], [2649.9999999999995, -9.094947017729282e-13], [3049.9999999999995, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_B', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_007, self._g02, id='piece_B', zorder=1, edgecolor='#EA580C', joinstyle='round', fill=False)
            c.path([[1849.9999999999998, 1199.9999999999989], [1849.9999999999998, 799.999999999999], [1849.9999999999998, 399.99999999999903], [1849.9999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_B', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_003, self._geometry_06, id='piece_C', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[3699.9999999999995, -9.094947017729282e-13], [4099.999999999999, -9.094947017729282e-13], [4499.999999999999, -9.094947017729282e-13], [4899.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_011, [1] + [4] * 12, id='piece_C', zorder=1, edgecolor='#2563EB', linewidth=2.0, joinstyle='round', fill=False)
            c.path(self._samples_008, self._g03, id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_004, self._geometry_08, id='piece_D', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[5549.999999999999, -9.094947017729282e-13], [5949.999999999999, -9.094947017729282e-13], [6349.999999999999, -9.094947017729282e-13], [6749.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_009, self._g04, id='piece_D', zorder=1, edgecolor='#EA580C', joinstyle='round', fill=False)
            c.path([[5549.999999999999, 1199.9999999999989], [5549.999999999999, 799.999999999999], [5549.999999999999, 399.99999999999903], [5549.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_D', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_005, self._geometry_02, id='piece_E', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[7399.999999999999, -9.094947017729282e-13], [7799.999999999999, -9.094947017729282e-13], [8199.999999999998, -9.094947017729282e-13], [8599.999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_010, self._g01, id='piece_E', zorder=1, edgecolor='#EA580C', joinstyle='round', fill=False)
            c.path([[7399.999999999999, 1199.9999999999989], [7399.999999999999, 799.999999999999], [7399.999999999999, 399.99999999999903], [7399.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane571_C05.png'
        with Canvas(PLANE, xlim=(-215.9762596899227, 8987.330426356588), ylim=(-4156.783551356589, 5046.523134689923)) as c:
            c.path(self._samples_001, self._geometry_02, id='piece_A', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[0.0, -9.094947017729282e-13], [399.99999999999994, -9.094947017729282e-13], [799.9999999999999, -9.094947017729282e-13], [1199.9999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_006, self._g01, id='piece_A', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path([[0.0, 1199.9999999999989], [0.0, 799.999999999999], [0.0, 399.99999999999903], [0.0, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_A', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_002, self._geometry_04, id='piece_B', zorder=1, joinstyle='round')
            c.path(self._samples_003, self._geometry_06, id='piece_C', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[3699.9999999999995, -9.094947017729282e-13], [4099.999999999999, -9.094947017729282e-13], [4499.999999999999, -9.094947017729282e-13], [4899.999999999999, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_011, [1] + [4] * 12, id='piece_C', zorder=1, edgecolor='#DC2626', linewidth=2.0, joinstyle='round', fill=False)
            c.path(self._samples_008, self._g03, id='piece_C', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_004, self._geometry_08, id='piece_D', zorder=1, joinstyle='round')
            c.path(self._samples_005, self._geometry_02, id='piece_E', zorder=1, edgecolor='none', joinstyle='round')
            c.path([[7399.999999999999, -9.094947017729282e-13], [7799.999999999999, -9.094947017729282e-13], [8199.999999999998, -9.094947017729282e-13], [8599.999999999998, -9.094947017729282e-13]], [1, 4, 4, 4], id='piece_E', zorder=1, joinstyle='round', fill=False)
            c.path(self._samples_012, [1] + [4] * 12, id='piece_E', zorder=1, edgecolor='#16A34A', joinstyle='round', fill=False)
            c.path(self._samples_013, [1] + [4] * 15, id='piece_E', zorder=1, joinstyle='round', fill=False)
            for object_id, text, anchor in [('label_A', 'A', (600, 600)), ('choice_label_A', '(A) A', (600, -360)), ('label_B', 'B', (2450, 600)), ('choice_label_B', '(B) B', (2450, -360)), ('label_C', 'C', (4300, 600)), ('choice_label_C', '(C) C', (4300, -360)), ('label_D', 'D', (6150, 600)), ('choice_label_D', '(D) D', (6150, -360)), ('label_E', 'E', (8000, 600)), ('choice_label_E', '(E) E', (8000, -360))]:
                c.text(text, anchor, id=object_id, zorder=3)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane571')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane571().draw(args.output, variant=args.variant))
