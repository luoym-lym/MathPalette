"""Collected question Plane550; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane550:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self._samples_001 = [
            [6.15, 8.8], [6.15, 8.64], [6.32, 8.56], [6.425, 8.665000000000001], [6.32, 8.42],
            [6.64, 8.370000000000001], [6.7, 8.56], [6.75, 8.66], [6.7, 8.745000000000001], [6.65, 8.755],
            [6.74, 8.755], [6.79, 8.72], [6.84, 8.67], [6.84, 8.930000000000001], [6.79, 8.88], [6.74, 8.845],
            [6.65, 8.845], [6.7, 8.855], [6.75, 8.940000000000001], [6.7, 9.040000000000001], [6.64, 9.23],
            [6.32, 9.180000000000001], [6.425, 8.935], [6.32, 9.040000000000001], [6.15, 8.96], [6.15, 8.8],
            [6.15, 8.8]
        ]
        self._samples_002 = [[x + 2.0, y + 1.0] for x, y in self._samples_001]
        self._samples_003 = [
            [9.5, 10.15], [9.34, 10.15], [9.26, 9.98], [9.365, 9.875], [9.12, 9.98], [9.07, 9.66],
            [9.26, 9.600000000000001], [9.36, 9.55], [9.445, 9.600000000000001], [9.455, 9.65], [9.455, 9.56],
            [9.42, 9.510000000000002], [9.37, 9.46], [9.63, 9.46], [9.58, 9.510000000000002], [9.545, 9.56],
            [9.545, 9.65], [9.555, 9.600000000000001], [9.64, 9.55], [9.74, 9.600000000000001], [9.93, 9.66],
            [9.88, 9.98], [9.635, 9.875], [9.74, 9.98], [9.66, 10.15], [9.5, 10.15], [9.5, 10.15]
        ]
        self._samples_004 = [
            [10.85, 9.8], [10.85, 9.96], [10.68, 10.040000000000001], [10.575, 9.935],
            [10.68, 10.180000000000001], [10.36, 10.23], [10.3, 10.040000000000001],
            [10.25, 9.940000000000001], [10.3, 9.855], [10.35, 9.845], [10.26, 9.845], [10.21, 9.88],
            [10.16, 9.930000000000001], [10.16, 9.67], [10.21, 9.72], [10.26, 9.755], [10.35, 9.755],
            [10.3, 9.745000000000001], [10.25, 9.66], [10.3, 9.56], [10.36, 9.370000000000001], [10.68, 9.42],
            [10.575, 9.665000000000001], [10.68, 9.56], [10.85, 9.64], [10.85, 9.8], [10.85, 9.8]
        ]
        self._samples_005 = [[x + -7.0, y + -6.2] for x, y in self._samples_003]
        self._samples_006 = [[x + 0.0, y + -6.2] for x, y in self._samples_003]
        self._samples_007 = [[x + 1.5, y + -6.2] for x, y in self._samples_003]
        self._samples_008 = [[x + 10.0, y + -5.2] for x, y in self._samples_001]
        self._samples_009 = [
            [6.15, 7.800000000000001], [6.378647450843758, 7.711832212156129],
            [6.391844051968769, 7.467130219296697], [6.546352549156242, 7.657341522555727],
            [6.783155948031231, 7.594275161697635], [6.65, 7.800000000000001],
            [6.783155948031232, 8.005724838302367], [6.546352549156242, 7.942658477444274],
            [6.391844051968769, 8.132869780703304], [6.378647450843758, 7.888167787843872],
            [6.15, 7.800000000000001]
        ]
        self._samples_010 = [
            [7.85, 7.800000000000001], [7.621352549156242, 7.888167787843872],
            [7.608155948031231, 8.132869780703304], [7.453647450843758, 7.942658477444274],
            [7.216844051968769, 8.005724838302367], [7.35, 7.800000000000001],
            [7.216844051968768, 7.594275161697635], [7.453647450843758, 7.657341522555727],
            [7.608155948031231, 7.467130219296697], [7.621352549156242, 7.711832212156129],
            [7.85, 7.800000000000001]
        ]
        self._samples_011 = [[x + 1.0, y + 0.0] for x, y in self._samples_010]
        self._samples_012 = [
            [9.85, 7.800000000000001], [9.73, 7.9], [9.58, 8.110000000000001], [9.42, 8.110000000000001],
            [9.21, 8.110000000000001], [9.19, 7.9], [9.34, 7.855], [9.25, 7.855], [9.2, 7.890000000000001],
            [9.16, 7.920000000000001], [9.16, 7.680000000000001], [9.2, 7.710000000000001],
            [9.25, 7.745000000000001], [9.34, 7.745000000000001], [9.19, 7.700000000000001],
            [9.21, 7.490000000000001], [9.42, 7.490000000000001], [9.58, 7.490000000000001],
            [9.73, 7.700000000000001], [9.85, 7.800000000000001], [9.85, 7.800000000000001]
        ]
        self._samples_013 = [
            [10.5, 7.460000000000001], [10.4, 7.550000000000001], [10.16, 7.750000000000001],
            [10.16, 7.920000000000001], [10.16, 8.14], [10.39, 8.23], [10.5, 8.0], [10.61, 8.23],
            [10.84, 8.14], [10.84, 7.920000000000001], [10.84, 7.750000000000001], [10.6, 7.550000000000001],
            [10.5, 7.460000000000001], [10.5, 7.460000000000001]
        ]
        self._samples_014 = [
            [10.5, 9.15], [10.4, 9.030000000000001], [10.19, 8.88], [10.19, 8.72], [10.19, 8.510000000000002],
            [10.4, 8.49], [10.445, 8.64], [10.445, 8.55], [10.41, 8.5], [10.38, 8.46], [10.62, 8.46],
            [10.59, 8.5], [10.555, 8.55], [10.555, 8.64], [10.6, 8.49], [10.81, 8.510000000000002],
            [10.81, 8.72], [10.81, 8.88], [10.6, 9.030000000000001], [10.5, 9.15], [10.5, 9.15]
        ]
        self._samples_015 = [[x + -1.0, y + 2.0] for x, y in self._samples_010]
        self._samples_016 = [
            [7.15, 9.8], [7.27, 9.700000000000001], [7.42, 9.49], [7.58, 9.49], [7.79, 9.49],
            [7.81, 9.700000000000001], [7.66, 9.745000000000001], [7.75, 9.745000000000001], [7.8, 9.71],
            [7.84, 9.680000000000001], [7.84, 9.92], [7.8, 9.89], [7.75, 9.855], [7.66, 9.855], [7.81, 9.9],
            [7.79, 10.110000000000001], [7.58, 10.110000000000001], [7.42, 10.110000000000001], [7.27, 9.9],
            [7.15, 9.8], [7.15, 9.8]
        ]
        self._samples_017 = [[x + 0.0, y + 2.0] for x, y in self._samples_014]
        self._samples_018 = [[x + -7.0, y + -4.2] for x, y in self._samples_010]
        self._samples_019 = [
            [1.5, 3.9399999999999995], [1.6, 3.8499999999999996], [1.84, 3.6499999999999995],
            [1.84, 3.4799999999999995], [1.84, 3.26], [1.61, 3.1699999999999995], [1.5, 3.3999999999999995],
            [1.39, 3.1699999999999995], [1.16, 3.26], [1.16, 3.4799999999999995], [1.16, 3.6499999999999995],
            [1.4, 3.8499999999999996], [1.5, 3.9399999999999995], [1.5, 3.9399999999999995]
        ]
        self._samples_020 = [
            [4.0, 3.2499999999999996], [4.088167787843871, 3.4786474508437575],
            [4.332869780703303, 3.491844051968768], [4.142658477444273, 3.6463525491562416],
            [4.205724838302365, 3.883155948031231], [4.0, 3.7499999999999996],
            [3.7942751616976347, 3.883155948031231], [3.857341522555727, 3.6463525491562416],
            [3.667130219296696, 3.4918440519687683], [3.911832212156129, 3.4786474508437575],
            [4.0, 3.2499999999999996]
        ]
        self._samples_021 = [[x + 3.5, y + 0.0] for x, y in self._samples_019]
        self._samples_022 = [
            [6.0, 3.9499999999999997], [5.911832212156129, 3.721352549156242],
            [5.667130219296697, 3.7081559480312314], [5.857341522555727, 3.5536474508437577],
            [5.794275161697635, 3.316844051968768], [6.0, 3.4499999999999997],
            [6.205724838302365, 3.316844051968768], [6.142658477444273, 3.5536474508437577],
            [6.332869780703303, 3.708155948031231], [6.088167787843871, 3.721352549156242],
            [6.0, 3.9499999999999997]
        ]
        self._samples_023 = [[x + 3.5, y + 0.0] for x, y in self._samples_020]
        self._samples_024 = [[x + 7.0, y + 0.0] for x, y in self._samples_019]
        self._samples_025 = [[x + 10.5, y + 0.0] for x, y in self._samples_019]
        self._samples_026 = [[x + 9.0, y + 0.0] for x, y in self._samples_020]
        self._samples_027 = [[x + 10.5, y + 0.0] for x, y in self._samples_020]
        self._samples_028 = [
            [15.16, 3.5999999999999996], [15.25, 3.6999999999999997], [15.45, 3.9399999999999995],
            [15.62, 3.9399999999999995], [15.84, 3.9399999999999995], [15.93, 3.7099999999999995],
            [15.7, 3.5999999999999996], [15.93, 3.4899999999999998], [15.84, 3.26], [15.62, 3.26],
            [15.45, 3.26], [15.25, 3.4999999999999996], [15.16, 3.5999999999999996],
            [15.16, 3.5999999999999996]
        ]
        self._geometry_01 = [
            ('template_grid_edge_00', [[7.0, 13.1], [7.0, 14.1]]),
            ('template_grid_edge_01', [[7.0, 13.1], [8.0, 13.1]]),
            ('template_grid_edge_02', [[7.0, 14.1], [8.0, 14.1]]),
            ('template_grid_edge_03', [[8.0, 13.1], [8.0, 14.1]]),
            ('template_grid_edge_04', [[8.0, 13.1], [9.0, 13.1]]),
            ('template_grid_edge_05', [[8.0, 14.1], [9.0, 14.1]]),
            ('template_grid_edge_06', [[9.0, 13.1], [9.0, 14.1]]),
            ('template_grid_edge_07', [[9.0, 13.1], [10.0, 13.1]]),
            ('template_grid_edge_08', [[9.0, 14.1], [10.0, 14.1]]),
            ('template_grid_edge_09', [[10.0, 13.1], [10.0, 14.1]]),
            ('board_grid_edge_00', [[6.0, 7.300000000000001], [6.0, 8.3]]),
            ('board_grid_edge_01', [[6.0, 7.300000000000001], [7.0, 7.300000000000001]]),
            ('board_grid_edge_02', [[6.0, 8.3], [6.0, 9.3]]),
            ('board_grid_edge_03', [[6.0, 8.3], [7.0, 8.3]]),
            ('board_grid_edge_04', [[6.0, 9.3], [6.0, 10.3]]),
            ('board_grid_edge_05', [[6.0, 9.3], [7.0, 9.3]]),
            ('board_grid_edge_06', [[6.0, 10.3], [6.0, 11.3]]),
            ('board_grid_edge_07', [[6.0, 10.3], [7.0, 10.3]]),
            ('board_grid_edge_08', [[6.0, 11.3], [7.0, 11.3]]),
            ('board_grid_edge_09', [[7.0, 7.300000000000001], [7.0, 8.3]]),
            ('board_grid_edge_10', [[7.0, 7.300000000000001], [8.0, 7.300000000000001]]),
            ('board_grid_edge_11', [[7.0, 8.3], [7.0, 9.3]]),
            ('board_grid_edge_12', [[7.0, 8.3], [8.0, 8.3]]),
            ('board_grid_edge_13', [[7.0, 9.3], [7.0, 10.3]]),
            ('board_grid_edge_14', [[7.0, 9.3], [8.0, 9.3]]),
            ('board_grid_edge_15', [[7.0, 10.3], [7.0, 11.3]]),
            ('board_grid_edge_16', [[7.0, 10.3], [8.0, 10.3]]),
            ('board_grid_edge_17', [[7.0, 11.3], [8.0, 11.3]]),
            ('board_grid_edge_18', [[8.0, 7.300000000000001], [8.0, 8.3]]),
            ('board_grid_edge_19', [[8.0, 7.300000000000001], [9.0, 7.300000000000001]]),
            ('board_grid_edge_20', [[8.0, 8.3], [8.0, 9.3]]),
            ('board_grid_edge_21', [[8.0, 8.3], [9.0, 8.3]]),
            ('board_grid_edge_22', [[8.0, 9.3], [8.0, 10.3]]),
            ('board_grid_edge_23', [[8.0, 9.3], [9.0, 9.3]]),
            ('board_grid_edge_24', [[8.0, 10.3], [8.0, 11.3]]),
            ('board_grid_edge_25', [[8.0, 10.3], [9.0, 10.3]]),
            ('board_grid_edge_26', [[8.0, 11.3], [9.0, 11.3]]),
            ('board_grid_edge_27', [[9.0, 7.300000000000001], [9.0, 8.3]]),
            ('board_grid_edge_28', [[9.0, 7.300000000000001], [10.0, 7.300000000000001]]),
            ('board_grid_edge_29', [[9.0, 8.3], [9.0, 9.3]]),
            ('board_grid_edge_30', [[9.0, 8.3], [10.0, 8.3]]),
            ('board_grid_edge_31', [[9.0, 9.3], [9.0, 10.3]]),
            ('board_grid_edge_32', [[9.0, 9.3], [10.0, 9.3]]),
            ('board_grid_edge_33', [[9.0, 10.3], [9.0, 11.3]]),
            ('board_grid_edge_34', [[9.0, 10.3], [10.0, 10.3]]),
            ('board_grid_edge_35', [[9.0, 11.3], [10.0, 11.3]]),
            ('board_grid_edge_36', [[10.0, 7.300000000000001], [10.0, 8.3]]),
            ('board_grid_edge_37', [[10.0, 7.300000000000001], [11.0, 7.300000000000001]]),
            ('board_grid_edge_38', [[10.0, 8.3], [10.0, 9.3]]),
            ('board_grid_edge_39', [[10.0, 8.3], [11.0, 8.3]]),
            ('board_grid_edge_40', [[10.0, 9.3], [10.0, 10.3]]),
            ('board_grid_edge_41', [[10.0, 9.3], [11.0, 9.3]]),
            ('board_grid_edge_42', [[10.0, 10.3], [10.0, 11.3]]),
            ('board_grid_edge_43', [[10.0, 10.3], [11.0, 10.3]]),
            ('board_grid_edge_44', [[10.0, 11.3], [11.0, 11.3]]),
            ('board_grid_edge_45', [[11.0, 7.300000000000001], [11.0, 8.3]]),
            ('board_grid_edge_46', [[11.0, 8.3], [11.0, 9.3]]),
            ('board_grid_edge_47', [[11.0, 9.3], [11.0, 10.3]]),
            ('board_grid_edge_48', [[11.0, 10.3], [11.0, 11.3]])
        ]
        self._geometry_03 = [1] + [4] * 12 + [2] + [4] * 12 + [79]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _defs = [
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {'color': '#16A34A', 'linewidth': 1.5},
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        c.path(self._samples_009, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_009, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_010, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_010, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_011, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_011, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_012, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_012, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_013, [1] + [4] * 12 + [79], id='board_cell_4_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_013, [1] + [4] * 12 + [79], id='board_cell_4_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_001, self._geometry_03, id='board_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_001, self._geometry_03, id='board_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path([[7.15, 8.8], [7.5, 9.040000000000001], [7.85, 8.8], [7.5, 8.56], [7.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.15, 8.8], [7.5, 9.040000000000001], [7.85, 8.8], [7.5, 8.56], [7.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[8.16, 8.8], [8.25, 8.9], [8.45, 9.14], [8.62, 9.14], [8.84, 9.14], [8.93, 8.91], [8.7, 8.8], [8.93, 8.690000000000001], [8.84, 8.46], [8.62, 8.46], [8.45, 8.46], [8.25, 8.700000000000001], [8.16, 8.8], [8.16, 8.8]], [1] + [4] * 12 + [79], id='board_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.16, 8.8], [8.25, 8.9], [8.45, 9.14], [8.62, 9.14], [8.84, 9.14], [8.93, 8.91], [8.7, 8.8], [8.93, 8.690000000000001], [8.84, 8.46], [8.62, 8.46], [8.45, 8.46], [8.25, 8.700000000000001], [8.16, 8.8], [8.16, 8.8]], [1] + [4] * 12 + [79], id='board_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path([[9.15, 8.8], [9.5, 9.040000000000001], [9.85, 8.8], [9.5, 8.56], [9.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_3_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.15, 8.8], [9.5, 9.040000000000001], [9.85, 8.8], [9.5, 8.56], [9.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_3_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_015, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_015, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_002, self._geometry_03, id='board_cell_2_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_002, self._geometry_03, id='board_cell_2_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_003, self._geometry_03, id='board_cell_3_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_003, self._geometry_03, id='board_cell_3_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_004, self._geometry_03, id='board_cell_4_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_004, self._geometry_03, id='board_cell_4_2_mark', capstyle='butt', joinstyle='round')
        c.path([[6.84, 10.8], [6.75, 10.700000000000001], [6.55, 10.46], [6.38, 10.46], [6.16, 10.46], [6.07, 10.690000000000001], [6.3, 10.8], [6.07, 10.91], [6.16, 11.14], [6.38, 11.14], [6.55, 11.14], [6.75, 10.9], [6.84, 10.8], [6.84, 10.8]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.84, 10.8], [6.75, 10.700000000000001], [6.55, 10.46], [6.38, 10.46], [6.16, 10.46], [6.07, 10.690000000000001], [6.3, 10.8], [6.07, 10.91], [6.16, 11.14], [6.38, 11.14], [6.55, 11.14], [6.75, 10.9], [6.84, 10.8], [6.84, 10.8]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark', capstyle='butt', joinstyle='round')
        c.path([[7.5, 11.15], [7.74, 10.8], [7.5, 10.450000000000001], [7.26, 10.8], [7.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_1_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.5, 11.15], [7.74, 10.8], [7.5, 10.450000000000001], [7.26, 10.8], [7.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_1_3_mark', capstyle='butt', joinstyle='round')
        c.path([[8.5, 11.14], [8.6, 11.05], [8.84, 10.850000000000001], [8.84, 10.680000000000001], [8.84, 10.46], [8.61, 10.370000000000001], [8.5, 10.600000000000001], [8.39, 10.370000000000001], [8.16, 10.46], [8.16, 10.680000000000001], [8.16, 10.850000000000001], [8.4, 11.05], [8.5, 11.14], [8.5, 11.14]], [1] + [4] * 12 + [79], id='board_cell_2_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.5, 11.14], [8.6, 11.05], [8.84, 10.850000000000001], [8.84, 10.680000000000001], [8.84, 10.46], [8.61, 10.370000000000001], [8.5, 10.600000000000001], [8.39, 10.370000000000001], [8.16, 10.46], [8.16, 10.680000000000001], [8.16, 10.850000000000001], [8.4, 11.05], [8.5, 11.14], [8.5, 11.14]], [1] + [4] * 12 + [79], id='board_cell_2_3_mark', capstyle='butt', joinstyle='round')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_017, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_017, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_3_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(41, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_A_grid_edge_00', [[0.0, 3.0999999999999996], [0.0, 4.1]]), ('option_A_grid_edge_01', [[0.0, 3.0999999999999996], [1.0, 3.0999999999999996]]), ('option_A_grid_edge_02', [[0.0, 4.1], [1.0, 4.1]]), ('option_A_grid_edge_03', [[1.0, 3.0999999999999996], [1.0, 4.1]]), ('option_A_grid_edge_04', [[1.0, 3.0999999999999996], [2.0, 3.0999999999999996]]), ('option_A_grid_edge_05', [[1.0, 4.1], [2.0, 4.1]]), ('option_A_grid_edge_06', [[2.0, 3.0999999999999996], [2.0, 4.1]]), ('option_A_grid_edge_07', [[2.0, 3.0999999999999996], [3.0, 3.0999999999999996]]), ('option_A_grid_edge_08', [[2.0, 4.1], [3.0, 4.1]]), ('option_A_grid_edge_09', [[3.0, 3.0999999999999996], [3.0, 4.1]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_018, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_A_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_018, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_A_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_019, [1] + [4] * 12 + [79], id='option_A_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_019, [1] + [4] * 12 + [79], id='option_A_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_2_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_B_grid_edge_00', [[3.5, 3.0999999999999996], [3.5, 4.1]]), ('option_B_grid_edge_01', [[3.5, 3.0999999999999996], [4.5, 3.0999999999999996]]), ('option_B_grid_edge_02', [[3.5, 4.1], [4.5, 4.1]]), ('option_B_grid_edge_03', [[4.5, 3.0999999999999996], [4.5, 4.1]]), ('option_B_grid_edge_04', [[4.5, 3.0999999999999996], [5.5, 3.0999999999999996]]), ('option_B_grid_edge_05', [[4.5, 4.1], [5.5, 4.1]]), ('option_B_grid_edge_06', [[5.5, 3.0999999999999996], [5.5, 4.1]]), ('option_B_grid_edge_07', [[5.5, 3.0999999999999996], [6.5, 3.0999999999999996]]), ('option_B_grid_edge_08', [[5.5, 4.1], [6.5, 4.1]]), ('option_B_grid_edge_09', [[6.5, 3.0999999999999996], [6.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_020, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_B_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_020, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_B_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_021, [1] + [4] * 12 + [79], id='option_B_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_021, [1] + [4] * 12 + [79], id='option_B_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_B_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_B_cell_2_0_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(55, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_C_grid_edge_00', [[7.0, 3.0999999999999996], [7.0, 4.1]]), ('option_C_grid_edge_01', [[7.0, 3.0999999999999996], [8.0, 3.0999999999999996]]), ('option_C_grid_edge_02', [[7.0, 4.1], [8.0, 4.1]]), ('option_C_grid_edge_03', [[8.0, 3.0999999999999996], [8.0, 4.1]]), ('option_C_grid_edge_04', [[8.0, 3.0999999999999996], [9.0, 3.0999999999999996]]), ('option_C_grid_edge_05', [[8.0, 4.1], [9.0, 4.1]]), ('option_C_grid_edge_06', [[9.0, 3.0999999999999996], [9.0, 4.1]]), ('option_C_grid_edge_07', [[9.0, 3.0999999999999996], [10.0, 3.0999999999999996]]), ('option_C_grid_edge_08', [[9.0, 4.1], [10.0, 4.1]]), ('option_C_grid_edge_09', [[10.0, 3.0999999999999996], [10.0, 4.1]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_023, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_023, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_024, [1] + [4] * 12 + [79], id='option_C_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_024, [1] + [4] * 12 + [79], id='option_C_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_006, self._geometry_03, id='option_C_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_006, self._geometry_03, id='option_C_cell_2_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_D_grid_edge_00', [[10.5, 3.0999999999999996], [10.5, 4.1]]), ('option_D_grid_edge_01', [[10.5, 3.0999999999999996], [11.5, 3.0999999999999996]]), ('option_D_grid_edge_02', [[10.5, 4.1], [11.5, 4.1]]), ('option_D_grid_edge_03', [[11.5, 3.0999999999999996], [11.5, 4.1]]), ('option_D_grid_edge_04', [[11.5, 3.0999999999999996], [12.5, 3.0999999999999996]]), ('option_D_grid_edge_05', [[11.5, 4.1], [12.5, 4.1]]), ('option_D_grid_edge_06', [[12.5, 3.0999999999999996], [12.5, 4.1]]), ('option_D_grid_edge_07', [[12.5, 3.0999999999999996], [13.5, 3.0999999999999996]]), ('option_D_grid_edge_08', [[12.5, 4.1], [13.5, 4.1]]), ('option_D_grid_edge_09', [[13.5, 3.0999999999999996], [13.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_007, self._geometry_03, id='option_D_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_007, self._geometry_03, id='option_D_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_D_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_D_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_026, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_D_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_026, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_D_cell_2_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_E_grid_edge_00', [[14.0, 3.0999999999999996], [14.0, 4.1]]), ('option_E_grid_edge_01', [[14.0, 3.0999999999999996], [15.0, 3.0999999999999996]]), ('option_E_grid_edge_02', [[14.0, 4.1], [15.0, 4.1]]), ('option_E_grid_edge_03', [[15.0, 3.0999999999999996], [15.0, 4.1]]), ('option_E_grid_edge_04', [[15.0, 3.0999999999999996], [16.0, 3.0999999999999996]]), ('option_E_grid_edge_05', [[15.0, 4.1], [16.0, 4.1]]), ('option_E_grid_edge_06', [[16.0, 3.0999999999999996], [16.0, 4.1]]), ('option_E_grid_edge_07', [[16.0, 3.0999999999999996], [17.0, 3.0999999999999996]]), ('option_E_grid_edge_08', [[16.0, 4.1], [17.0, 4.1]]), ('option_E_grid_edge_09', [[17.0, 3.0999999999999996], [17.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_027, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_E_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_027, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_E_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_028, [1] + [4] * 12 + [79], id='option_E_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_028, [1] + [4] * 12 + [79], id='option_E_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_008, self._geometry_03, id='option_E_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_008, self._geometry_03, id='option_E_cell_2_0_mark', capstyle='butt', joinstyle='round')
        for object_id, text, anchor in [('option_A_label', '(A)', (1.5, 2.4999999999999996)), ('option_B_label', '(B)', (5.0, 2.4999999999999996)), ('option_C_label', '(C)', (8.5, 2.4999999999999996)), ('option_D_label', '(D)', (12.0, 2.4999999999999996)), ('option_E_label', '(E)', (15.5, 2.4999999999999996))]:
            c.text(text, anchor, id=object_id, zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({14}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C01.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({23, 32, 41}, {'color': '#16A34A', 'linewidth': 1.5})], 41: [({1, 4, 7}, {'color': '#16A34A', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C02.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({10, 12, 14}, {'color': '#EA580C', 'linewidth': 1.5})], 41: [({0, 9}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C03.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({14, 15, 17, 24, 26, 33, 35, 41}, {'color': '#DC2626', 'linewidth': 1.5})], 55: [({0, 1, 2, 4, 5, 7, 8, 9}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C04.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({15, 17, 24, 26, 33, 35, 41}, {'color': '#16A34A', 'linewidth': 1.5})], 55: [({0, 1, 2, 4, 5, 7, 8, 9}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C05.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({14, 15, 17, 24, 26, 33, 35, 41}, {'color': '#16A34A', 'linewidth': 2.0})], 55: [({0, 1, 2, 4, 5, 7, 8, 9}, {'color': '#16A34A', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane550_C06.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-0.7665453803962681, 17.07818794483761)) as c:
            self._draw_base(c, hi={0: [({14, 15, 17, 24, 26, 33, 35, 41}, {'color': '#EA580C', 'linewidth': 2.0})], 55: [({0, 1, 2, 4, 5, 7, 8, 9}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane550')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane550().draw(args.output, variant=args.variant))
