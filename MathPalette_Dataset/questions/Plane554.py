"""Collected question Plane554; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane554:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self._samples_001 = [
            [9.15, 6.800000000000001], [9.15, 6.640000000000001], [9.32, 6.5600000000000005],
            [9.425, 6.665000000000001], [9.32, 6.420000000000001], [9.64, 6.370000000000001],
            [9.7, 6.5600000000000005], [9.75, 6.660000000000001], [9.7, 6.745000000000001],
            [9.65, 6.755000000000001], [9.74, 6.755000000000001], [9.79, 6.720000000000001],
            [9.84, 6.670000000000001], [9.84, 6.930000000000001], [9.79, 6.880000000000001],
            [9.74, 6.845000000000001], [9.65, 6.845000000000001], [9.7, 6.855], [9.75, 6.94],
            [9.7, 7.040000000000001], [9.64, 7.23], [9.32, 7.180000000000001], [9.425, 6.9350000000000005],
            [9.32, 7.040000000000001], [9.15, 6.960000000000001], [9.15, 6.800000000000001],
            [9.15, 6.800000000000001]
        ]
        self._samples_002 = [
            [7.85, 7.800000000000001], [7.85, 7.960000000000001], [7.68, 8.040000000000001],
            [7.575, 7.9350000000000005], [7.68, 8.180000000000001], [7.36, 8.23], [7.3, 8.040000000000001],
            [7.25, 7.94], [7.3, 7.855], [7.35, 7.845000000000001], [7.26, 7.845000000000001],
            [7.21, 7.880000000000001], [7.16, 7.930000000000001], [7.16, 7.670000000000001],
            [7.21, 7.720000000000001], [7.26, 7.755000000000001], [7.35, 7.755000000000001],
            [7.3, 7.745000000000001], [7.25, 7.660000000000001], [7.3, 7.5600000000000005],
            [7.36, 7.370000000000001], [7.68, 7.420000000000001], [7.575, 7.665000000000001],
            [7.68, 7.5600000000000005], [7.85, 7.640000000000001], [7.85, 7.800000000000001],
            [7.85, 7.800000000000001]
        ]
        self._samples_003 = [[x + 1.0, y + 1.0] for x, y in self._samples_002]
        self._samples_004 = [
            [7.5, 10.15], [7.34, 10.15], [7.26, 9.98], [7.365, 9.875], [7.12, 9.98], [7.07, 9.66],
            [7.26, 9.600000000000001], [7.36, 9.55], [7.445, 9.600000000000001], [7.455, 9.65], [7.455, 9.56],
            [7.42, 9.510000000000002], [7.37, 9.46], [7.63, 9.46], [7.58, 9.510000000000002], [7.545, 9.56],
            [7.545, 9.65], [7.555, 9.600000000000001], [7.64, 9.55], [7.74, 9.600000000000001], [7.93, 9.66],
            [7.88, 9.98], [7.635, 9.875], [7.74, 9.98], [7.66, 10.15], [7.5, 10.15], [7.5, 10.15]
        ]
        self._samples_005 = [
            [10.5, 10.450000000000001], [10.66, 10.450000000000001], [10.74, 10.620000000000001],
            [10.635, 10.725000000000001], [10.88, 10.620000000000001], [10.93, 10.940000000000001],
            [10.74, 11.0], [10.64, 11.05], [10.555, 11.0], [10.545, 10.950000000000001],
            [10.545, 11.040000000000001], [10.58, 11.09], [10.63, 11.14], [10.37, 11.14], [10.42, 11.09],
            [10.455, 11.040000000000001], [10.455, 10.950000000000001], [10.445, 11.0], [10.36, 11.05],
            [10.26, 11.0], [10.07, 10.940000000000001], [10.12, 10.620000000000001],
            [10.365, 10.725000000000001], [10.26, 10.620000000000001], [10.34, 10.450000000000001],
            [10.5, 10.450000000000001], [10.5, 10.450000000000001]
        ]
        self._samples_006 = [[x + -9.0, y + -7.2] for x, y in self._samples_005]
        self._samples_007 = [[x + -5.5, y + -4.2] for x, y in self._samples_001]
        self._samples_008 = [[x + -5.5, y + -7.2] for x, y in self._samples_005]
        self._samples_009 = [[x + -3.0, y + -8.2] for x, y in self._samples_005]
        self._samples_010 = [[x + 1.5, y + -7.2] for x, y in self._samples_005]
        self._samples_011 = [[x + 5.0, y + -7.2] for x, y in self._samples_005]
        self._samples_012 = [
            [6.5, 7.140000000000001], [6.6, 7.050000000000001], [6.84, 6.8500000000000005],
            [6.84, 6.680000000000001], [6.84, 6.460000000000001], [6.61, 6.370000000000001],
            [6.5, 6.6000000000000005], [6.39, 6.370000000000001], [6.16, 6.460000000000001],
            [6.16, 6.680000000000001], [6.16, 6.8500000000000005], [6.4, 7.050000000000001],
            [6.5, 7.140000000000001], [6.5, 7.140000000000001]
        ]
        self._samples_013 = [[x + 2.0, y + 0.0] for x, y in self._samples_012]
        self._samples_014 = [
            [10.15, 6.800000000000001], [10.27, 6.700000000000001], [10.42, 6.490000000000001],
            [10.58, 6.490000000000001], [10.79, 6.490000000000001], [10.81, 6.700000000000001],
            [10.66, 6.745000000000001], [10.75, 6.745000000000001], [10.8, 6.710000000000001],
            [10.84, 6.680000000000001], [10.84, 6.920000000000001], [10.8, 6.890000000000001], [10.75, 6.855],
            [10.66, 6.855], [10.81, 6.9], [10.79, 7.11], [10.58, 7.11], [10.42, 7.11], [10.27, 6.9],
            [10.15, 6.800000000000001], [10.15, 6.800000000000001]
        ]
        self._samples_015 = [
            [6.85, 7.800000000000001], [6.73, 7.9], [6.58, 8.110000000000001], [6.42, 8.110000000000001],
            [6.21, 8.110000000000001], [6.19, 7.9], [6.34, 7.855], [6.25, 7.855], [6.2, 7.890000000000001],
            [6.16, 7.920000000000001], [6.16, 7.680000000000001], [6.2, 7.710000000000001],
            [6.25, 7.745000000000001], [6.34, 7.745000000000001], [6.19, 7.700000000000001],
            [6.21, 7.490000000000001], [6.42, 7.490000000000001], [6.58, 7.490000000000001],
            [6.73, 7.700000000000001], [6.85, 7.800000000000001], [6.85, 7.800000000000001]
        ]
        self._samples_016 = [[x + 3.0, y + 0.0] for x, y in self._samples_015]
        self._samples_017 = [
            [10.84, 7.800000000000001], [10.75, 7.700000000000001], [10.55, 7.460000000000001],
            [10.38, 7.460000000000001], [10.16, 7.460000000000001], [10.07, 7.69], [10.3, 7.800000000000001],
            [10.07, 7.910000000000001], [10.16, 8.14], [10.38, 8.14], [10.55, 8.14], [10.75, 7.9],
            [10.84, 7.800000000000001], [10.84, 7.800000000000001]
        ]
        self._samples_018 = [
            [6.15, 8.8], [6.378647450843758, 8.71183221215613], [6.391844051968769, 8.467130219296697],
            [6.546352549156242, 8.657341522555727], [6.783155948031231, 8.594275161697635], [6.65, 8.8],
            [6.783155948031232, 9.005724838302367], [6.546352549156242, 8.942658477444274],
            [6.391844051968769, 9.132869780703304], [6.378647450843758, 8.888167787843871], [6.15, 8.8]
        ]
        self._samples_019 = [[x + -3.0, y + 2.0] for x, y in self._samples_014]
        self._samples_020 = [[x + 3.0, y + 1.0] for x, y in self._samples_015]
        self._samples_021 = [
            [10.5, 8.450000000000001], [10.58816778784387, 8.678647450843759],
            [10.832869780703303, 8.691844051968769], [10.642658477444273, 8.846352549156244],
            [10.705724838302366, 9.083155948031232], [10.5, 8.950000000000001],
            [10.294275161697634, 9.083155948031232], [10.357341522555727, 8.846352549156244],
            [10.167130219296697, 8.691844051968769], [10.41183221215613, 8.678647450843759],
            [10.5, 8.450000000000001]
        ]
        self._samples_022 = [[x + -2.0, y + 1.0] for x, y in self._samples_021]
        self._samples_023 = [
            [6.5, 11.15], [6.411832212156129, 10.921352549156243], [6.167130219296697, 10.908155948031233],
            [6.357341522555727, 10.753647450843758], [6.294275161697635, 10.51684405196877], [6.5, 10.65],
            [6.705724838302365, 10.51684405196877], [6.642658477444273, 10.753647450843758],
            [6.832869780703303, 10.908155948031233], [6.588167787843871, 10.921352549156243], [6.5, 11.15]
        ]
        self._samples_024 = [[x + 1.0, y + 0.0] for x, y in self._samples_023]
        self._samples_025 = [
            [1.5, 2.2499999999999996], [1.6, 2.3699999999999997], [1.81, 2.5199999999999996],
            [1.81, 2.6799999999999997], [1.81, 2.8899999999999997], [1.6, 2.9099999999999997], [1.555, 2.76],
            [1.555, 2.8499999999999996], [1.59, 2.8999999999999995], [1.62, 2.9399999999999995],
            [1.38, 2.9399999999999995], [1.41, 2.8999999999999995], [1.445, 2.8499999999999996],
            [1.445, 2.76], [1.4, 2.9099999999999997], [1.19, 2.8899999999999997], [1.19, 2.6799999999999997],
            [1.19, 2.5199999999999996], [1.4, 2.3699999999999997], [1.5, 2.2499999999999996],
            [1.5, 2.2499999999999996]
        ]
        self._samples_026 = [[x + 3.5, y + 0.0] for x, y in self._samples_025]
        self._samples_027 = [[x + 7.0, y + 0.0] for x, y in self._samples_025]
        self._samples_028 = [[x + 10.5, y + 0.0] for x, y in self._samples_025]
        self._samples_029 = [[x + 9.0, y + -5.2] for x, y in self._samples_015]
        self._geometry_01 = [
            ('template_grid_edge_00', [[7.0, 12.1], [7.0, 13.1]]),
            ('template_grid_edge_01', [[7.0, 12.1], [8.0, 12.1]]),
            ('template_grid_edge_02', [[7.0, 13.1], [8.0, 13.1]]),
            ('template_grid_edge_03', [[8.0, 12.1], [8.0, 13.1]]),
            ('template_grid_edge_04', [[8.0, 12.1], [9.0, 12.1]]),
            ('template_grid_edge_05', [[8.0, 13.1], [8.0, 14.1]]),
            ('template_grid_edge_06', [[8.0, 13.1], [9.0, 13.1]]),
            ('template_grid_edge_07', [[8.0, 14.1], [9.0, 14.1]]),
            ('template_grid_edge_08', [[9.0, 12.1], [9.0, 13.1]]),
            ('template_grid_edge_09', [[9.0, 13.1], [9.0, 14.1]]),
            ('template_grid_edge_10', [[9.0, 13.1], [10.0, 13.1]]),
            ('template_grid_edge_11', [[9.0, 14.1], [10.0, 14.1]]),
            ('template_grid_edge_12', [[10.0, 13.1], [10.0, 14.1]]),
            ('board_grid_edge_00', [[6.0, 6.300000000000001], [6.0, 7.300000000000001]]),
            ('board_grid_edge_01', [[6.0, 6.300000000000001], [7.0, 6.300000000000001]]),
            ('board_grid_edge_02', [[6.0, 7.300000000000001], [6.0, 8.3]]),
            ('board_grid_edge_03', [[6.0, 7.300000000000001], [7.0, 7.300000000000001]]),
            ('board_grid_edge_04', [[6.0, 8.3], [6.0, 9.3]]),
            ('board_grid_edge_05', [[6.0, 8.3], [7.0, 8.3]]),
            ('board_grid_edge_06', [[6.0, 9.3], [6.0, 10.3]]),
            ('board_grid_edge_07', [[6.0, 9.3], [7.0, 9.3]]),
            ('board_grid_edge_08', [[6.0, 10.3], [6.0, 11.3]]),
            ('board_grid_edge_09', [[6.0, 10.3], [7.0, 10.3]]),
            ('board_grid_edge_10', [[6.0, 11.3], [7.0, 11.3]]),
            ('board_grid_edge_11', [[7.0, 6.300000000000001], [7.0, 7.300000000000001]]),
            ('board_grid_edge_12', [[7.0, 6.300000000000001], [8.0, 6.300000000000001]]),
            ('board_grid_edge_13', [[7.0, 7.300000000000001], [7.0, 8.3]]),
            ('board_grid_edge_14', [[7.0, 7.300000000000001], [8.0, 7.300000000000001]]),
            ('board_grid_edge_15', [[7.0, 8.3], [7.0, 9.3]]),
            ('board_grid_edge_16', [[7.0, 8.3], [8.0, 8.3]]),
            ('board_grid_edge_17', [[7.0, 9.3], [7.0, 10.3]]),
            ('board_grid_edge_18', [[7.0, 9.3], [8.0, 9.3]]),
            ('board_grid_edge_19', [[7.0, 10.3], [7.0, 11.3]]),
            ('board_grid_edge_20', [[7.0, 10.3], [8.0, 10.3]]),
            ('board_grid_edge_21', [[7.0, 11.3], [8.0, 11.3]]),
            ('board_grid_edge_22', [[8.0, 6.300000000000001], [8.0, 7.300000000000001]]),
            ('board_grid_edge_23', [[8.0, 6.300000000000001], [9.0, 6.300000000000001]]),
            ('board_grid_edge_24', [[8.0, 7.300000000000001], [8.0, 8.3]]),
            ('board_grid_edge_25', [[8.0, 7.300000000000001], [9.0, 7.300000000000001]]),
            ('board_grid_edge_26', [[8.0, 8.3], [8.0, 9.3]]),
            ('board_grid_edge_27', [[8.0, 8.3], [9.0, 8.3]]),
            ('board_grid_edge_28', [[8.0, 9.3], [8.0, 10.3]]),
            ('board_grid_edge_29', [[8.0, 9.3], [9.0, 9.3]]),
            ('board_grid_edge_30', [[8.0, 10.3], [8.0, 11.3]]),
            ('board_grid_edge_31', [[8.0, 10.3], [9.0, 10.3]]),
            ('board_grid_edge_32', [[8.0, 11.3], [9.0, 11.3]]),
            ('board_grid_edge_33', [[9.0, 6.300000000000001], [9.0, 7.300000000000001]]),
            ('board_grid_edge_34', [[9.0, 6.300000000000001], [10.0, 6.300000000000001]]),
            ('board_grid_edge_35', [[9.0, 7.300000000000001], [9.0, 8.3]]),
            ('board_grid_edge_36', [[9.0, 7.300000000000001], [10.0, 7.300000000000001]]),
            ('board_grid_edge_37', [[9.0, 8.3], [9.0, 9.3]]),
            ('board_grid_edge_38', [[9.0, 8.3], [10.0, 8.3]]),
            ('board_grid_edge_39', [[9.0, 9.3], [9.0, 10.3]]),
            ('board_grid_edge_40', [[9.0, 9.3], [10.0, 9.3]]),
            ('board_grid_edge_41', [[9.0, 10.3], [9.0, 11.3]]),
            ('board_grid_edge_42', [[9.0, 10.3], [10.0, 10.3]]),
            ('board_grid_edge_43', [[9.0, 11.3], [10.0, 11.3]]),
            ('board_grid_edge_44', [[10.0, 6.300000000000001], [10.0, 7.300000000000001]]),
            ('board_grid_edge_45', [[10.0, 6.300000000000001], [11.0, 6.300000000000001]]),
            ('board_grid_edge_46', [[10.0, 7.300000000000001], [10.0, 8.3]]),
            ('board_grid_edge_47', [[10.0, 7.300000000000001], [11.0, 7.300000000000001]]),
            ('board_grid_edge_48', [[10.0, 8.3], [10.0, 9.3]]),
            ('board_grid_edge_49', [[10.0, 8.3], [11.0, 8.3]]),
            ('board_grid_edge_50', [[10.0, 9.3], [10.0, 10.3]]),
            ('board_grid_edge_51', [[10.0, 9.3], [11.0, 9.3]]),
            ('board_grid_edge_52', [[10.0, 10.3], [10.0, 11.3]]),
            ('board_grid_edge_53', [[10.0, 10.3], [11.0, 10.3]]),
            ('board_grid_edge_54', [[10.0, 11.3], [11.0, 11.3]]),
            ('board_grid_edge_55', [[11.0, 6.300000000000001], [11.0, 7.300000000000001]]),
            ('board_grid_edge_56', [[11.0, 7.300000000000001], [11.0, 8.3]]),
            ('board_grid_edge_57', [[11.0, 8.3], [11.0, 9.3]]),
            ('board_grid_edge_58', [[11.0, 9.3], [11.0, 10.3]]),
            ('board_grid_edge_59', [[11.0, 10.3], [11.0, 11.3]])
        ]
        self._geometry_03 = [1] + [4] * 12 + [2] + [4] * 12 + [79]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_012, [1] + [4] * 12 + [79], id='board_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_012, [1] + [4] * 12 + [79], id='board_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path([[7.15, 6.800000000000001], [7.5, 7.040000000000001], [7.85, 6.800000000000001], [7.5, 6.5600000000000005], [7.15, 6.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.15, 6.800000000000001], [7.5, 7.040000000000001], [7.85, 6.800000000000001], [7.5, 6.5600000000000005], [7.15, 6.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_013, [1] + [4] * 12 + [79], id='board_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_013, [1] + [4] * 12 + [79], id='board_cell_2_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_001, self._geometry_03, id='board_cell_3_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_001, self._geometry_03, id='board_cell_3_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_4_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_015, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_015, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_002, self._geometry_03, id='board_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_002, self._geometry_03, id='board_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[8.5, 8.15], [8.74, 7.800000000000001], [8.5, 7.450000000000001], [8.26, 7.800000000000001], [8.5, 8.15]], [1, 2, 2, 2, 79], id='board_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.5, 8.15], [8.74, 7.800000000000001], [8.5, 7.450000000000001], [8.26, 7.800000000000001], [8.5, 8.15]], [1, 2, 2, 2, 79], id='board_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_017, [1] + [4] * 12 + [79], id='board_cell_4_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_017, [1] + [4] * 12 + [79], id='board_cell_4_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_018, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_018, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_019, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_019, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_003, self._geometry_03, id='board_cell_2_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_003, self._geometry_03, id='board_cell_2_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_021, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_4_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_021, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_4_2_mark', capstyle='butt', joinstyle='round')
        c.path([[6.5, 9.46], [6.4, 9.55], [6.16, 9.75], [6.16, 9.92], [6.16, 10.14], [6.39, 10.23], [6.5, 10.0], [6.61, 10.23], [6.84, 10.14], [6.84, 9.92], [6.84, 9.75], [6.6, 9.55], [6.5, 9.46], [6.5, 9.46]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.5, 9.46], [6.4, 9.55], [6.16, 9.75], [6.16, 9.92], [6.16, 10.14], [6.39, 10.23], [6.5, 10.0], [6.61, 10.23], [6.84, 10.14], [6.84, 9.92], [6.84, 9.75], [6.6, 9.55], [6.5, 9.46], [6.5, 9.46]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_004, self._geometry_03, id='board_cell_1_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_004, self._geometry_03, id='board_cell_1_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_3_mark', capstyle='butt', joinstyle='round')
        c.path([[9.5, 10.15], [9.74, 9.8], [9.5, 9.450000000000001], [9.26, 9.8], [9.5, 10.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.5, 10.15], [9.74, 9.8], [9.5, 9.450000000000001], [9.26, 9.8], [9.5, 10.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark', capstyle='butt', joinstyle='round')
        c.path([[10.84, 9.8], [10.75, 9.700000000000001], [10.55, 9.46], [10.38, 9.46], [10.16, 9.46], [10.07, 9.690000000000001], [10.3, 9.8], [10.07, 9.91], [10.16, 10.14], [10.38, 10.14], [10.55, 10.14], [10.75, 9.9], [10.84, 9.8], [10.84, 9.8]], [1] + [4] * 12 + [79], id='board_cell_4_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.84, 9.8], [10.75, 9.700000000000001], [10.55, 9.46], [10.38, 9.46], [10.16, 9.46], [10.07, 9.690000000000001], [10.3, 9.8], [10.07, 9.91], [10.16, 10.14], [10.38, 10.14], [10.55, 10.14], [10.75, 9.9], [10.84, 9.8], [10.84, 9.8]], [1] + [4] * 12 + [79], id='board_cell_4_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_023, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_023, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_4_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_024, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_024, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_4_mark', capstyle='butt', joinstyle='round')
        c.path([[8.15, 10.8], [8.5, 11.040000000000001], [8.85, 10.8], [8.5, 10.56], [8.15, 10.8]], [1, 2, 2, 2, 79], id='board_cell_2_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.15, 10.8], [8.5, 11.040000000000001], [8.85, 10.8], [8.5, 10.56], [8.15, 10.8]], [1, 2, 2, 2, 79], id='board_cell_2_4_mark', capstyle='butt', joinstyle='round')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_4_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_005, self._geometry_03, id='board_cell_4_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_005, self._geometry_03, id='board_cell_4_4_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(51, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_A_grid_edge_00', [[0.0, 2.0999999999999996], [0.0, 3.0999999999999996]]), ('option_A_grid_edge_01', [[0.0, 2.0999999999999996], [1.0, 2.0999999999999996]]), ('option_A_grid_edge_02', [[0.0, 3.0999999999999996], [1.0, 3.0999999999999996]]), ('option_A_grid_edge_03', [[1.0, 2.0999999999999996], [1.0, 3.0999999999999996]]), ('option_A_grid_edge_04', [[1.0, 2.0999999999999996], [2.0, 2.0999999999999996]]), ('option_A_grid_edge_05', [[1.0, 3.0999999999999996], [1.0, 4.1]]), ('option_A_grid_edge_06', [[1.0, 3.0999999999999996], [2.0, 3.0999999999999996]]), ('option_A_grid_edge_07', [[1.0, 4.1], [2.0, 4.1]]), ('option_A_grid_edge_08', [[2.0, 2.0999999999999996], [2.0, 3.0999999999999996]]), ('option_A_grid_edge_09', [[2.0, 3.0999999999999996], [2.0, 4.1]]), ('option_A_grid_edge_10', [[2.0, 3.0999999999999996], [3.0, 3.0999999999999996]]), ('option_A_grid_edge_11', [[2.0, 4.1], [3.0, 4.1]]), ('option_A_grid_edge_12', [[3.0, 3.0999999999999996], [3.0, 4.1]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[0.5, 2.9499999999999997], [0.74, 2.5999999999999996], [0.5, 2.2499999999999996], [0.26, 2.5999999999999996], [0.5, 2.9499999999999997]], [1, 2, 2, 2, 79], id='option_A_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[0.5, 2.9499999999999997], [0.74, 2.5999999999999996], [0.5, 2.2499999999999996], [0.26, 2.5999999999999996], [0.5, 2.9499999999999997]], [1, 2, 2, 2, 79], id='option_A_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_025, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_A_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_025, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_A_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_006, self._geometry_03, id='option_A_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_006, self._geometry_03, id='option_A_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[2.15, 3.5999999999999996], [2.5, 3.84], [2.85, 3.5999999999999996], [2.5, 3.3599999999999994], [2.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[2.15, 3.5999999999999996], [2.5, 3.84], [2.85, 3.5999999999999996], [2.5, 3.3599999999999994], [2.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_2_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_B_grid_edge_00', [[3.5, 2.0999999999999996], [3.5, 3.0999999999999996]]), ('option_B_grid_edge_01', [[3.5, 2.0999999999999996], [4.5, 2.0999999999999996]]), ('option_B_grid_edge_02', [[3.5, 3.0999999999999996], [4.5, 3.0999999999999996]]), ('option_B_grid_edge_03', [[4.5, 2.0999999999999996], [4.5, 3.0999999999999996]]), ('option_B_grid_edge_04', [[4.5, 2.0999999999999996], [5.5, 2.0999999999999996]]), ('option_B_grid_edge_05', [[4.5, 3.0999999999999996], [4.5, 4.1]]), ('option_B_grid_edge_06', [[4.5, 3.0999999999999996], [5.5, 3.0999999999999996]]), ('option_B_grid_edge_07', [[4.5, 4.1], [5.5, 4.1]]), ('option_B_grid_edge_08', [[5.5, 2.0999999999999996], [5.5, 3.0999999999999996]]), ('option_B_grid_edge_09', [[5.5, 3.0999999999999996], [5.5, 4.1]]), ('option_B_grid_edge_10', [[5.5, 3.0999999999999996], [6.5, 3.0999999999999996]]), ('option_B_grid_edge_11', [[5.5, 4.1], [6.5, 4.1]]), ('option_B_grid_edge_12', [[6.5, 3.0999999999999996], [6.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_007, self._geometry_03, id='option_B_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_007, self._geometry_03, id='option_B_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_026, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_B_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_026, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_B_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_008, self._geometry_03, id='option_B_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_008, self._geometry_03, id='option_B_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[5.65, 3.5999999999999996], [6.0, 3.84], [6.35, 3.5999999999999996], [6.0, 3.3599999999999994], [5.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[5.65, 3.5999999999999996], [6.0, 3.84], [6.35, 3.5999999999999996], [6.0, 3.3599999999999994], [5.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_2_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_C_grid_edge_00', [[7.0, 2.0999999999999996], [7.0, 3.0999999999999996]]), ('option_C_grid_edge_01', [[7.0, 2.0999999999999996], [8.0, 2.0999999999999996]]), ('option_C_grid_edge_02', [[7.0, 3.0999999999999996], [8.0, 3.0999999999999996]]), ('option_C_grid_edge_03', [[8.0, 2.0999999999999996], [8.0, 3.0999999999999996]]), ('option_C_grid_edge_04', [[8.0, 2.0999999999999996], [9.0, 2.0999999999999996]]), ('option_C_grid_edge_05', [[8.0, 3.0999999999999996], [8.0, 4.1]]), ('option_C_grid_edge_06', [[8.0, 3.0999999999999996], [9.0, 3.0999999999999996]]), ('option_C_grid_edge_07', [[8.0, 4.1], [9.0, 4.1]]), ('option_C_grid_edge_08', [[9.0, 2.0999999999999996], [9.0, 3.0999999999999996]]), ('option_C_grid_edge_09', [[9.0, 3.0999999999999996], [9.0, 4.1]]), ('option_C_grid_edge_10', [[9.0, 3.0999999999999996], [10.0, 3.0999999999999996]]), ('option_C_grid_edge_11', [[9.0, 4.1], [10.0, 4.1]]), ('option_C_grid_edge_12', [[10.0, 3.0999999999999996], [10.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_009, self._geometry_03, id='option_C_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_009, self._geometry_03, id='option_C_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_027, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_C_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_027, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_C_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[8.15, 3.5999999999999996], [8.5, 3.84], [8.85, 3.5999999999999996], [8.5, 3.3599999999999994], [8.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_C_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.15, 3.5999999999999996], [8.5, 3.84], [8.85, 3.5999999999999996], [8.5, 3.3599999999999994], [8.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_C_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[9.15, 3.5999999999999996], [9.5, 3.84], [9.85, 3.5999999999999996], [9.5, 3.3599999999999994], [9.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_C_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.15, 3.5999999999999996], [9.5, 3.84], [9.85, 3.5999999999999996], [9.5, 3.3599999999999994], [9.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_C_cell_2_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_D_grid_edge_00', [[10.5, 2.0999999999999996], [10.5, 3.0999999999999996]]), ('option_D_grid_edge_01', [[10.5, 2.0999999999999996], [11.5, 2.0999999999999996]]), ('option_D_grid_edge_02', [[10.5, 3.0999999999999996], [11.5, 3.0999999999999996]]), ('option_D_grid_edge_03', [[11.5, 2.0999999999999996], [11.5, 3.0999999999999996]]), ('option_D_grid_edge_04', [[11.5, 2.0999999999999996], [12.5, 2.0999999999999996]]), ('option_D_grid_edge_05', [[11.5, 3.0999999999999996], [11.5, 4.1]]), ('option_D_grid_edge_06', [[11.5, 3.0999999999999996], [12.5, 3.0999999999999996]]), ('option_D_grid_edge_07', [[11.5, 4.1], [12.5, 4.1]]), ('option_D_grid_edge_08', [[12.5, 2.0999999999999996], [12.5, 3.0999999999999996]]), ('option_D_grid_edge_09', [[12.5, 3.0999999999999996], [12.5, 4.1]]), ('option_D_grid_edge_10', [[12.5, 3.0999999999999996], [13.5, 3.0999999999999996]]), ('option_D_grid_edge_11', [[12.5, 4.1], [13.5, 4.1]]), ('option_D_grid_edge_12', [[13.5, 3.0999999999999996], [13.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path([[10.65, 2.5999999999999996], [11.0, 2.84], [11.35, 2.5999999999999996], [11.0, 2.3599999999999994], [10.65, 2.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.65, 2.5999999999999996], [11.0, 2.84], [11.35, 2.5999999999999996], [11.0, 2.3599999999999994], [10.65, 2.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_028, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_D_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_028, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_D_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_010, self._geometry_03, id='option_D_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_010, self._geometry_03, id='option_D_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[12.65, 3.5999999999999996], [13.0, 3.84], [13.35, 3.5999999999999996], [13.0, 3.3599999999999994], [12.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[12.65, 3.5999999999999996], [13.0, 3.84], [13.35, 3.5999999999999996], [13.0, 3.3599999999999994], [12.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_2_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_E_grid_edge_00', [[14.0, 2.0999999999999996], [14.0, 3.0999999999999996]]), ('option_E_grid_edge_01', [[14.0, 2.0999999999999996], [15.0, 2.0999999999999996]]), ('option_E_grid_edge_02', [[14.0, 3.0999999999999996], [15.0, 3.0999999999999996]]), ('option_E_grid_edge_03', [[15.0, 2.0999999999999996], [15.0, 3.0999999999999996]]), ('option_E_grid_edge_04', [[15.0, 2.0999999999999996], [16.0, 2.0999999999999996]]), ('option_E_grid_edge_05', [[15.0, 3.0999999999999996], [15.0, 4.1]]), ('option_E_grid_edge_06', [[15.0, 3.0999999999999996], [16.0, 3.0999999999999996]]), ('option_E_grid_edge_07', [[15.0, 4.1], [16.0, 4.1]]), ('option_E_grid_edge_08', [[16.0, 2.0999999999999996], [16.0, 3.0999999999999996]]), ('option_E_grid_edge_09', [[16.0, 3.0999999999999996], [16.0, 4.1]]), ('option_E_grid_edge_10', [[16.0, 3.0999999999999996], [17.0, 3.0999999999999996]]), ('option_E_grid_edge_11', [[16.0, 4.1], [17.0, 4.1]]), ('option_E_grid_edge_12', [[17.0, 3.0999999999999996], [17.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path([[14.15, 2.5999999999999996], [14.5, 2.84], [14.85, 2.5999999999999996], [14.5, 2.3599999999999994], [14.15, 2.5999999999999996]], [1, 2, 2, 2, 79], id='option_E_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[14.15, 2.5999999999999996], [14.5, 2.84], [14.85, 2.5999999999999996], [14.5, 2.3599999999999994], [14.15, 2.5999999999999996]], [1, 2, 2, 2, 79], id='option_E_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_029, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_E_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_029, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_E_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_011, self._geometry_03, id='option_E_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_011, self._geometry_03, id='option_E_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[16.5, 3.9499999999999997], [16.74, 3.5999999999999996], [16.5, 3.2499999999999996], [16.26, 3.5999999999999996], [16.5, 3.9499999999999997]], [1, 2, 2, 2, 79], id='option_E_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[16.5, 3.9499999999999997], [16.74, 3.5999999999999996], [16.5, 3.2499999999999996], [16.26, 3.5999999999999996], [16.5, 3.9499999999999997]], [1, 2, 2, 2, 79], id='option_E_cell_2_1_mark', capstyle='butt', joinstyle='round')
        for object_id, text, anchor in [('option_A_label', '(A)', (1.5, 1.4999999999999996)), ('option_B_label', '(B)', (5.0, 1.4999999999999996)), ('option_C_label', '(C)', (8.5, 1.4999999999999996)), ('option_D_label', '(D)', (12.0, 1.4999999999999996)), ('option_E_label', '(E)', (15.5, 1.4999999999999996))]:
            c.text(text, anchor, id=object_id, zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane554_C01.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({37, 38, 39, 40, 42, 48, 50, 51, 52, 53, 55, 61, 63}, {'color': '#DC2626', 'linewidth': 1.5})], 51: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane554_C02.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({37, 38, 39, 40, 42, 48, 50, 51, 52, 53, 55, 61, 63}, {'color': '#16A34A', 'linewidth': 1.5})], 51: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane554_C03.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({37, 38, 39, 40, 42, 48, 50, 51, 52, 53, 55, 61, 63}, {'color': '#EA580C', 'linewidth': 1.5})], 51: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#EA580C'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane554_C04.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({37, 38, 39, 40, 42, 48, 50, 51, 52, 53, 55, 61, 63}, {'color': '#EA580C', 'linewidth': 2.0})], 51: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane554')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane554().draw(args.output, variant=args.variant))
