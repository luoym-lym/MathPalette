"""Collected question Plane553; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane553:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self._samples_001 = [
            [10.0, 6.450000000000001], [10.16, 6.450000000000001], [10.24, 6.620000000000001],
            [10.135, 6.7250000000000005], [10.38, 6.620000000000001], [10.43, 6.94],
            [10.24, 7.000000000000001], [10.14, 7.050000000000001], [10.055, 7.000000000000001],
            [10.045, 6.950000000000001], [10.045, 7.040000000000001], [10.08, 7.090000000000001],
            [10.13, 7.140000000000001], [9.87, 7.140000000000001], [9.92, 7.090000000000001],
            [9.955, 7.040000000000001], [9.955, 6.950000000000001], [9.945, 7.000000000000001],
            [9.86, 7.050000000000001], [9.76, 7.000000000000001], [9.57, 6.94], [9.62, 6.620000000000001],
            [9.865, 6.7250000000000005], [9.76, 6.620000000000001], [9.84, 6.450000000000001],
            [10.0, 6.450000000000001], [10.0, 6.450000000000001]
        ]
        self._samples_002 = [
            [9.65, 7.800000000000001], [9.65, 7.640000000000001], [9.82, 7.5600000000000005],
            [9.925, 7.665000000000001], [9.82, 7.420000000000001], [10.14, 7.370000000000001],
            [10.2, 7.5600000000000005], [10.25, 7.660000000000001], [10.2, 7.745000000000001],
            [10.15, 7.755000000000001], [10.24, 7.755000000000001], [10.29, 7.720000000000001],
            [10.34, 7.670000000000001], [10.34, 7.930000000000001], [10.29, 7.880000000000001],
            [10.24, 7.845000000000001], [10.15, 7.845000000000001], [10.2, 7.855], [10.25, 7.94],
            [10.2, 8.040000000000001], [10.14, 8.23], [9.82, 8.180000000000001], [9.925, 7.9350000000000005],
            [9.82, 8.040000000000001], [9.65, 7.960000000000001], [9.65, 7.800000000000001],
            [9.65, 7.800000000000001]
        ]
        self._samples_003 = [[x + -2.0, y + 2.0] for x, y in self._samples_002]
        self._samples_004 = [[x + 0.0, y + 2.0] for x, y in self._samples_002]
        self._samples_005 = [
            [1.5, 2.9499999999999997], [1.34, 2.9499999999999997], [1.26, 2.78], [1.365, 2.675], [1.12, 2.78],
            [1.07, 2.4599999999999995], [1.26, 2.3999999999999995], [1.3599999999999999, 2.3499999999999996],
            [1.445, 2.3999999999999995], [1.455, 2.4499999999999997], [1.455, 2.3599999999999994],
            [1.42, 2.3099999999999996], [1.37, 2.26], [1.63, 2.26], [1.58, 2.3099999999999996],
            [1.545, 2.3599999999999994], [1.545, 2.4499999999999997], [1.555, 2.3999999999999995],
            [1.6400000000000001, 2.3499999999999996], [1.74, 2.3999999999999995], [1.93, 2.4599999999999995],
            [1.88, 2.78], [1.635, 2.675], [1.74, 2.78], [1.66, 2.9499999999999997], [1.5, 2.9499999999999997],
            [1.5, 2.9499999999999997]
        ]
        self._samples_006 = [
            [5.35, 2.5999999999999996], [5.35, 2.76], [5.18, 2.84], [5.075, 2.7349999999999994],
            [5.18, 2.9799999999999995], [4.86, 3.03], [4.8, 2.84], [4.75, 2.7399999999999998], [4.8, 2.655],
            [4.85, 2.6449999999999996], [4.76, 2.6449999999999996], [4.71, 2.6799999999999997],
            [4.66, 2.7299999999999995], [4.66, 2.4699999999999998], [4.71, 2.5199999999999996],
            [4.76, 2.5549999999999997], [4.85, 2.5549999999999997], [4.8, 2.5449999999999995],
            [4.75, 2.4599999999999995], [4.8, 2.3599999999999994], [4.86, 2.1699999999999995],
            [5.18, 2.2199999999999998], [5.075, 2.465], [5.18, 2.3599999999999994],
            [5.35, 2.4399999999999995], [5.35, 2.5999999999999996], [5.35, 2.5999999999999996]
        ]
        self._samples_007 = [[x + -2.5, y + -4.2] for x, y in self._samples_002]
        self._samples_008 = [[x + 3.5, y + 0.0] for x, y in self._samples_006]
        self._samples_009 = [[x + 7.0, y + 0.0] for x, y in self._samples_006]
        self._samples_010 = [[x + 10.5, y + 0.0] for x, y in self._samples_006]
        self._samples_011 = [
            [9.35, 6.800000000000001], [9.121352549156242, 6.888167787843872],
            [9.108155948031232, 7.132869780703304], [8.953647450843757, 6.942658477444274],
            [8.716844051968769, 7.005724838302366], [8.85, 6.800000000000001],
            [8.716844051968769, 6.594275161697635], [8.953647450843757, 6.657341522555727],
            [9.108155948031232, 6.467130219296697], [9.121352549156242, 6.711832212156129],
            [9.35, 6.800000000000001]
        ]
        self._samples_012 = [
            [7.65, 7.800000000000001], [7.878647450843758, 7.711832212156129],
            [7.891844051968769, 7.467130219296697], [8.046352549156243, 7.657341522555727],
            [8.283155948031231, 7.594275161697635], [8.15, 7.800000000000001],
            [8.283155948031231, 8.005724838302367], [8.046352549156243, 7.942658477444274],
            [7.891844051968769, 8.132869780703304], [7.878647450843758, 7.888167787843872],
            [7.65, 7.800000000000001]
        ]
        self._samples_013 = [
            [9.0, 8.15], [8.91183221215613, 7.921352549156243], [8.667130219296697, 7.908155948031232],
            [8.857341522555727, 7.753647450843759], [8.794275161697634, 7.51684405196877], [9.0, 7.65],
            [9.205724838302366, 7.516844051968769], [9.142658477444273, 7.753647450843759],
            [9.332869780703303, 7.908155948031232], [9.08816778784387, 7.921352549156243], [9.0, 8.15]
        ]
        self._samples_014 = [
            [10.35, 8.8], [10.23, 8.9], [10.08, 9.110000000000001], [9.92, 9.110000000000001],
            [9.71, 9.110000000000001], [9.69, 8.9], [9.84, 8.855], [9.75, 8.855], [9.7, 8.89], [9.66, 8.92],
            [9.66, 8.680000000000001], [9.7, 8.71], [9.75, 8.745000000000001], [9.84, 8.745000000000001],
            [9.69, 8.700000000000001], [9.71, 8.49], [9.92, 8.49], [10.08, 8.49], [10.23, 8.700000000000001],
            [10.35, 8.8], [10.35, 8.8]
        ]
        self._samples_015 = [
            [7.0, 10.15], [6.9, 10.030000000000001], [6.69, 9.88], [6.69, 9.72], [6.69, 9.510000000000002],
            [6.9, 9.49], [6.945, 9.64], [6.945, 9.55], [6.91, 9.5], [6.88, 9.46], [7.12, 9.46], [7.09, 9.5],
            [7.055, 9.55], [7.055, 9.64], [7.1, 9.49], [7.31, 9.510000000000002], [7.31, 9.72], [7.31, 9.88],
            [7.1, 10.030000000000001], [7.0, 10.15], [7.0, 10.15]
        ]
        self._samples_016 = [
            [9.0, 9.450000000000001], [9.1, 9.57], [9.31, 9.72], [9.31, 9.88], [9.31, 10.09],
            [9.1, 10.110000000000001], [9.055, 9.96], [9.055, 10.05], [9.09, 10.100000000000001],
            [9.12, 10.14], [8.88, 10.14], [8.91, 10.100000000000001], [8.945, 10.05], [8.945, 9.96],
            [8.9, 10.110000000000001], [8.69, 10.09], [8.69, 9.88], [8.69, 9.72], [8.9, 9.57],
            [9.0, 9.450000000000001], [9.0, 9.450000000000001]
        ]
        self._samples_017 = [[x + -1.0, y + 3.0] for x, y in self._samples_012]
        self._samples_018 = [[x + -2.0, y + 2.0] for x, y in self._samples_014]
        self._samples_019 = [
            [1.5, 3.9399999999999995], [1.6, 3.8499999999999996], [1.84, 3.6499999999999995],
            [1.84, 3.4799999999999995], [1.84, 3.26], [1.61, 3.1699999999999995], [1.5, 3.3999999999999995],
            [1.39, 3.1699999999999995], [1.16, 3.26], [1.16, 3.4799999999999995], [1.16, 3.6499999999999995],
            [1.4, 3.8499999999999996], [1.5, 3.9399999999999995], [1.5, 3.9399999999999995]
        ]
        self._samples_020 = [
            [2.16, 3.5999999999999996], [2.25, 3.6999999999999997], [2.45, 3.9399999999999995],
            [2.62, 3.9399999999999995], [2.84, 3.9399999999999995], [2.93, 3.7099999999999995],
            [2.7, 3.5999999999999996], [2.93, 3.4899999999999998], [2.84, 3.26], [2.62, 3.26], [2.45, 3.26],
            [2.25, 3.4999999999999996], [2.16, 3.5999999999999996], [2.16, 3.5999999999999996]
        ]
        self._samples_021 = [[x + 3.5, y + 0.0] for x, y in self._samples_019]
        self._samples_022 = [[x + 3.5, y + 0.0] for x, y in self._samples_020]
        self._samples_023 = [[x + 7.0, y + 0.0] for x, y in self._samples_019]
        self._samples_024 = [[x + 7.0, y + 0.0] for x, y in self._samples_020]
        self._samples_025 = [[x + 9.5, y + 0.0] for x, y in self._samples_020]
        self._samples_026 = [[x + 11.5, y + 0.0] for x, y in self._samples_019]
        self._samples_027 = [[x + 13.0, y + 0.0] for x, y in self._samples_020]
        self._geometry_01 = [
            ('template_grid_edge_00', [[7.0, 13.1], [7.0, 14.1]]),
            ('template_grid_edge_01', [[7.0, 13.1], [8.0, 13.1]]),
            ('template_grid_edge_02', [[7.0, 14.1], [8.0, 14.1]]),
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
            ('board_grid_edge_00', [[6.5, 6.300000000000001], [6.5, 7.300000000000001]]),
            ('board_grid_edge_01', [[6.5, 6.300000000000001], [7.5, 6.300000000000001]]),
            ('board_grid_edge_02', [[6.5, 7.300000000000001], [6.5, 8.3]]),
            ('board_grid_edge_03', [[6.5, 7.300000000000001], [7.5, 7.300000000000001]]),
            ('board_grid_edge_04', [[6.5, 8.3], [6.5, 9.3]]),
            ('board_grid_edge_05', [[6.5, 8.3], [7.5, 8.3]]),
            ('board_grid_edge_06', [[6.5, 9.3], [6.5, 10.3]]),
            ('board_grid_edge_07', [[6.5, 9.3], [7.5, 9.3]]),
            ('board_grid_edge_08', [[6.5, 10.3], [6.5, 11.3]]),
            ('board_grid_edge_09', [[6.5, 10.3], [7.5, 10.3]]),
            ('board_grid_edge_10', [[6.5, 11.3], [7.5, 11.3]]),
            ('board_grid_edge_11', [[7.5, 6.300000000000001], [7.5, 7.300000000000001]]),
            ('board_grid_edge_12', [[7.5, 6.300000000000001], [8.5, 6.300000000000001]]),
            ('board_grid_edge_13', [[7.5, 7.300000000000001], [7.5, 8.3]]),
            ('board_grid_edge_14', [[7.5, 7.300000000000001], [8.5, 7.300000000000001]]),
            ('board_grid_edge_15', [[7.5, 8.3], [7.5, 9.3]]),
            ('board_grid_edge_16', [[7.5, 8.3], [8.5, 8.3]]),
            ('board_grid_edge_17', [[7.5, 9.3], [7.5, 10.3]]),
            ('board_grid_edge_18', [[7.5, 9.3], [8.5, 9.3]]),
            ('board_grid_edge_19', [[7.5, 10.3], [7.5, 11.3]]),
            ('board_grid_edge_20', [[7.5, 10.3], [8.5, 10.3]]),
            ('board_grid_edge_21', [[7.5, 11.3], [8.5, 11.3]]),
            ('board_grid_edge_22', [[8.5, 6.300000000000001], [8.5, 7.300000000000001]]),
            ('board_grid_edge_23', [[8.5, 6.300000000000001], [9.5, 6.300000000000001]]),
            ('board_grid_edge_24', [[8.5, 7.300000000000001], [8.5, 8.3]]),
            ('board_grid_edge_25', [[8.5, 7.300000000000001], [9.5, 7.300000000000001]]),
            ('board_grid_edge_26', [[8.5, 8.3], [8.5, 9.3]]),
            ('board_grid_edge_27', [[8.5, 8.3], [9.5, 8.3]]),
            ('board_grid_edge_28', [[8.5, 9.3], [8.5, 10.3]]),
            ('board_grid_edge_29', [[8.5, 9.3], [9.5, 9.3]]),
            ('board_grid_edge_30', [[8.5, 10.3], [8.5, 11.3]]),
            ('board_grid_edge_31', [[8.5, 10.3], [9.5, 10.3]]),
            ('board_grid_edge_32', [[8.5, 11.3], [9.5, 11.3]]),
            ('board_grid_edge_33', [[9.5, 6.300000000000001], [9.5, 7.300000000000001]]),
            ('board_grid_edge_34', [[9.5, 6.300000000000001], [10.5, 6.300000000000001]]),
            ('board_grid_edge_35', [[9.5, 7.300000000000001], [9.5, 8.3]]),
            ('board_grid_edge_36', [[9.5, 7.300000000000001], [10.5, 7.300000000000001]]),
            ('board_grid_edge_37', [[9.5, 8.3], [9.5, 9.3]]),
            ('board_grid_edge_38', [[9.5, 8.3], [10.5, 8.3]]),
            ('board_grid_edge_39', [[9.5, 9.3], [9.5, 10.3]]),
            ('board_grid_edge_40', [[9.5, 9.3], [10.5, 9.3]]),
            ('board_grid_edge_41', [[9.5, 10.3], [9.5, 11.3]]),
            ('board_grid_edge_42', [[9.5, 10.3], [10.5, 10.3]]),
            ('board_grid_edge_43', [[9.5, 11.3], [10.5, 11.3]]),
            ('board_grid_edge_44', [[10.5, 6.300000000000001], [10.5, 7.300000000000001]]),
            ('board_grid_edge_45', [[10.5, 7.300000000000001], [10.5, 8.3]]),
            ('board_grid_edge_46', [[10.5, 8.3], [10.5, 9.3]]),
            ('board_grid_edge_47', [[10.5, 9.3], [10.5, 10.3]]),
            ('board_grid_edge_48', [[10.5, 10.3], [10.5, 11.3]])
        ]
        self._geometry_03 = [1] + [4] * 12 + [2] + [4] * 12 + [79]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[7.0, 7.15], [7.24, 6.800000000000001], [7.0, 6.450000000000001], [6.76, 6.800000000000001], [7.0, 7.15]], [1, 2, 2, 2, 79], id='board_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.0, 7.15], [7.24, 6.800000000000001], [7.0, 6.450000000000001], [6.76, 6.800000000000001], [7.0, 7.15]], [1, 2, 2, 2, 79], id='board_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path([[7.65, 6.800000000000001], [8.0, 7.040000000000001], [8.35, 6.800000000000001], [8.0, 6.5600000000000005], [7.65, 6.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.65, 6.800000000000001], [8.0, 7.040000000000001], [8.35, 6.800000000000001], [8.0, 6.5600000000000005], [7.65, 6.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_011, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_011, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_001, self._geometry_03, id='board_cell_3_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_001, self._geometry_03, id='board_cell_3_0_mark', capstyle='butt', joinstyle='round')
        c.path([[6.65, 7.800000000000001], [7.0, 8.040000000000001], [7.35, 7.800000000000001], [7.0, 7.5600000000000005], [6.65, 7.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.65, 7.800000000000001], [7.0, 8.040000000000001], [7.35, 7.800000000000001], [7.0, 7.5600000000000005], [6.65, 7.800000000000001]], [1, 2, 2, 2, 79], id='board_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_012, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_012, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_013, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_013, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_1_mark', capstyle='butt', joinstyle='round')
        c.path([[7.34, 8.8], [7.25, 8.700000000000001], [7.05, 8.46], [6.88, 8.46], [6.66, 8.46], [6.57, 8.690000000000001], [6.8, 8.8], [6.57, 8.91], [6.66, 9.14], [6.88, 9.14], [7.05, 9.14], [7.25, 8.9], [7.34, 8.8], [7.34, 8.8]], [1] + [4] * 12 + [79], id='board_cell_0_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.34, 8.8], [7.25, 8.700000000000001], [7.05, 8.46], [6.88, 8.46], [6.66, 8.46], [6.57, 8.690000000000001], [6.8, 8.8], [6.57, 8.91], [6.66, 9.14], [6.88, 9.14], [7.05, 9.14], [7.25, 8.9], [7.34, 8.8], [7.34, 8.8]], [1] + [4] * 12 + [79], id='board_cell_0_2_mark', capstyle='butt', joinstyle='round')
        c.path([[8.0, 8.46], [7.9, 8.55], [7.66, 8.75], [7.66, 8.92], [7.66, 9.14], [7.89, 9.23], [8.0, 9.0], [8.11, 9.23], [8.34, 9.14], [8.34, 8.92], [8.34, 8.75], [8.1, 8.55], [8.0, 8.46], [8.0, 8.46]], [1] + [4] * 12 + [79], id='board_cell_1_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.0, 8.46], [7.9, 8.55], [7.66, 8.75], [7.66, 8.92], [7.66, 9.14], [7.89, 9.23], [8.0, 9.0], [8.11, 9.23], [8.34, 9.14], [8.34, 8.92], [8.34, 8.75], [8.1, 8.55], [8.0, 8.46], [8.0, 8.46]], [1] + [4] * 12 + [79], id='board_cell_1_2_mark', capstyle='butt', joinstyle='round')
        c.path([[8.65, 8.8], [9.0, 9.040000000000001], [9.35, 8.8], [9.0, 8.56], [8.65, 8.8]], [1, 2, 2, 2, 79], id='board_cell_2_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.65, 8.8], [9.0, 9.040000000000001], [9.35, 8.8], [9.0, 8.56], [8.65, 8.8]], [1, 2, 2, 2, 79], id='board_cell_2_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_014, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_015, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_015, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_2_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_2_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_004, self._geometry_03, id='board_cell_3_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_004, self._geometry_03, id='board_cell_3_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_017, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_017, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_4_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_4_mark', capstyle='butt', joinstyle='round')
        c.path([[9.0, 11.14], [9.1, 11.05], [9.34, 10.850000000000001], [9.34, 10.680000000000001], [9.34, 10.46], [9.11, 10.370000000000001], [9.0, 10.600000000000001], [8.89, 10.370000000000001], [8.66, 10.46], [8.66, 10.680000000000001], [8.66, 10.850000000000001], [8.9, 11.05], [9.0, 11.14], [9.0, 11.14]], [1] + [4] * 12 + [79], id='board_cell_2_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.0, 11.14], [9.1, 11.05], [9.34, 10.850000000000001], [9.34, 10.680000000000001], [9.34, 10.46], [9.11, 10.370000000000001], [9.0, 10.600000000000001], [8.89, 10.370000000000001], [8.66, 10.46], [8.66, 10.680000000000001], [8.66, 10.850000000000001], [8.9, 11.05], [9.0, 11.14], [9.0, 11.14]], [1] + [4] * 12 + [79], id='board_cell_2_4_mark', capstyle='butt', joinstyle='round')
        c.path([[10.34, 10.8], [10.25, 10.700000000000001], [10.05, 10.46], [9.88, 10.46], [9.66, 10.46], [9.57, 10.690000000000001], [9.8, 10.8], [9.57, 10.91], [9.66, 11.14], [9.88, 11.14], [10.05, 11.14], [10.25, 10.9], [10.34, 10.8], [10.34, 10.8]], [1] + [4] * 12 + [79], id='board_cell_3_4_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.34, 10.8], [10.25, 10.700000000000001], [10.05, 10.46], [9.88, 10.46], [9.66, 10.46], [9.57, 10.690000000000001], [9.8, 10.8], [9.57, 10.91], [9.66, 11.14], [9.88, 11.14], [10.05, 11.14], [10.25, 10.9], [10.34, 10.8], [10.34, 10.8]], [1] + [4] * 12 + [79], id='board_cell_3_4_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(41, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_A_grid_edge_00', [[0.0, 3.0999999999999996], [0.0, 4.1]]), ('option_A_grid_edge_01', [[0.0, 3.0999999999999996], [1.0, 3.0999999999999996]]), ('option_A_grid_edge_02', [[0.0, 4.1], [1.0, 4.1]]), ('option_A_grid_edge_03', [[1.0, 2.0999999999999996], [1.0, 3.0999999999999996]]), ('option_A_grid_edge_04', [[1.0, 2.0999999999999996], [2.0, 2.0999999999999996]]), ('option_A_grid_edge_05', [[1.0, 3.0999999999999996], [1.0, 4.1]]), ('option_A_grid_edge_06', [[1.0, 3.0999999999999996], [2.0, 3.0999999999999996]]), ('option_A_grid_edge_07', [[1.0, 4.1], [2.0, 4.1]]), ('option_A_grid_edge_08', [[2.0, 2.0999999999999996], [2.0, 3.0999999999999996]]), ('option_A_grid_edge_09', [[2.0, 3.0999999999999996], [2.0, 4.1]]), ('option_A_grid_edge_10', [[2.0, 3.0999999999999996], [3.0, 3.0999999999999996]]), ('option_A_grid_edge_11', [[2.0, 4.1], [3.0, 4.1]]), ('option_A_grid_edge_12', [[3.0, 3.0999999999999996], [3.0, 4.1]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path([[0.15000000000000002, 3.5999999999999996], [0.5, 3.84], [0.85, 3.5999999999999996], [0.5, 3.3599999999999994], [0.15000000000000002, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[0.15000000000000002, 3.5999999999999996], [0.5, 3.84], [0.85, 3.5999999999999996], [0.5, 3.3599999999999994], [0.15000000000000002, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_019, [1] + [4] * 12 + [79], id='option_A_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_019, [1] + [4] * 12 + [79], id='option_A_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_020, [1] + [4] * 12 + [79], id='option_A_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_020, [1] + [4] * 12 + [79], id='option_A_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_1_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_B_grid_edge_00', [[3.5, 3.0999999999999996], [3.5, 4.1]]), ('option_B_grid_edge_01', [[3.5, 3.0999999999999996], [4.5, 3.0999999999999996]]), ('option_B_grid_edge_02', [[3.5, 4.1], [4.5, 4.1]]), ('option_B_grid_edge_03', [[4.5, 2.0999999999999996], [4.5, 3.0999999999999996]]), ('option_B_grid_edge_04', [[4.5, 2.0999999999999996], [5.5, 2.0999999999999996]]), ('option_B_grid_edge_05', [[4.5, 3.0999999999999996], [4.5, 4.1]]), ('option_B_grid_edge_06', [[4.5, 3.0999999999999996], [5.5, 3.0999999999999996]]), ('option_B_grid_edge_07', [[4.5, 4.1], [5.5, 4.1]]), ('option_B_grid_edge_08', [[5.5, 2.0999999999999996], [5.5, 3.0999999999999996]]), ('option_B_grid_edge_09', [[5.5, 3.0999999999999996], [5.5, 4.1]]), ('option_B_grid_edge_10', [[5.5, 3.0999999999999996], [6.5, 3.0999999999999996]]), ('option_B_grid_edge_11', [[5.5, 4.1], [6.5, 4.1]]), ('option_B_grid_edge_12', [[6.5, 3.0999999999999996], [6.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path([[3.65, 3.5999999999999996], [4.0, 3.84], [4.35, 3.5999999999999996], [4.0, 3.3599999999999994], [3.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[3.65, 3.5999999999999996], [4.0, 3.84], [4.35, 3.5999999999999996], [4.0, 3.3599999999999994], [3.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_021, [1] + [4] * 12 + [79], id='option_B_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_021, [1] + [4] * 12 + [79], id='option_B_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_022, [1] + [4] * 12 + [79], id='option_B_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_022, [1] + [4] * 12 + [79], id='option_B_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_006, self._geometry_03, id='option_B_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_006, self._geometry_03, id='option_B_cell_1_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_C_grid_edge_00', [[7.0, 3.0999999999999996], [7.0, 4.1]]), ('option_C_grid_edge_01', [[7.0, 3.0999999999999996], [8.0, 3.0999999999999996]]), ('option_C_grid_edge_02', [[7.0, 4.1], [8.0, 4.1]]), ('option_C_grid_edge_03', [[8.0, 2.0999999999999996], [8.0, 3.0999999999999996]]), ('option_C_grid_edge_04', [[8.0, 2.0999999999999996], [9.0, 2.0999999999999996]]), ('option_C_grid_edge_05', [[8.0, 3.0999999999999996], [8.0, 4.1]]), ('option_C_grid_edge_06', [[8.0, 3.0999999999999996], [9.0, 3.0999999999999996]]), ('option_C_grid_edge_07', [[8.0, 4.1], [9.0, 4.1]]), ('option_C_grid_edge_08', [[9.0, 2.0999999999999996], [9.0, 3.0999999999999996]]), ('option_C_grid_edge_09', [[9.0, 3.0999999999999996], [9.0, 4.1]]), ('option_C_grid_edge_10', [[9.0, 3.0999999999999996], [10.0, 3.0999999999999996]]), ('option_C_grid_edge_11', [[9.0, 4.1], [10.0, 4.1]]), ('option_C_grid_edge_12', [[10.0, 3.0999999999999996], [10.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_007, self._geometry_03, id='option_C_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_007, self._geometry_03, id='option_C_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_023, [1] + [4] * 12 + [79], id='option_C_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_023, [1] + [4] * 12 + [79], id='option_C_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_024, [1] + [4] * 12 + [79], id='option_C_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_024, [1] + [4] * 12 + [79], id='option_C_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_008, self._geometry_03, id='option_C_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_008, self._geometry_03, id='option_C_cell_1_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_D_grid_edge_00', [[10.5, 3.0999999999999996], [10.5, 4.1]]), ('option_D_grid_edge_01', [[10.5, 3.0999999999999996], [11.5, 3.0999999999999996]]), ('option_D_grid_edge_02', [[10.5, 4.1], [11.5, 4.1]]), ('option_D_grid_edge_03', [[11.5, 2.0999999999999996], [11.5, 3.0999999999999996]]), ('option_D_grid_edge_04', [[11.5, 2.0999999999999996], [12.5, 2.0999999999999996]]), ('option_D_grid_edge_05', [[11.5, 3.0999999999999996], [11.5, 4.1]]), ('option_D_grid_edge_06', [[11.5, 3.0999999999999996], [12.5, 3.0999999999999996]]), ('option_D_grid_edge_07', [[11.5, 4.1], [12.5, 4.1]]), ('option_D_grid_edge_08', [[12.5, 2.0999999999999996], [12.5, 3.0999999999999996]]), ('option_D_grid_edge_09', [[12.5, 3.0999999999999996], [12.5, 4.1]]), ('option_D_grid_edge_10', [[12.5, 3.0999999999999996], [13.5, 3.0999999999999996]]), ('option_D_grid_edge_11', [[12.5, 4.1], [13.5, 4.1]]), ('option_D_grid_edge_12', [[13.5, 3.0999999999999996], [13.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path([[10.65, 3.5999999999999996], [11.0, 3.84], [11.35, 3.5999999999999996], [11.0, 3.3599999999999994], [10.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.65, 3.5999999999999996], [11.0, 3.84], [11.35, 3.5999999999999996], [11.0, 3.3599999999999994], [10.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_D_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_D_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_026, [1] + [4] * 12 + [79], id='option_D_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_026, [1] + [4] * 12 + [79], id='option_D_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_009, self._geometry_03, id='option_D_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_009, self._geometry_03, id='option_D_cell_1_0_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_E_grid_edge_00', [[14.0, 3.0999999999999996], [14.0, 4.1]]), ('option_E_grid_edge_01', [[14.0, 3.0999999999999996], [15.0, 3.0999999999999996]]), ('option_E_grid_edge_02', [[14.0, 4.1], [15.0, 4.1]]), ('option_E_grid_edge_03', [[15.0, 2.0999999999999996], [15.0, 3.0999999999999996]]), ('option_E_grid_edge_04', [[15.0, 2.0999999999999996], [16.0, 2.0999999999999996]]), ('option_E_grid_edge_05', [[15.0, 3.0999999999999996], [15.0, 4.1]]), ('option_E_grid_edge_06', [[15.0, 3.0999999999999996], [16.0, 3.0999999999999996]]), ('option_E_grid_edge_07', [[15.0, 4.1], [16.0, 4.1]]), ('option_E_grid_edge_08', [[16.0, 2.0999999999999996], [16.0, 3.0999999999999996]]), ('option_E_grid_edge_09', [[16.0, 3.0999999999999996], [16.0, 4.1]]), ('option_E_grid_edge_10', [[16.0, 3.0999999999999996], [17.0, 3.0999999999999996]]), ('option_E_grid_edge_11', [[16.0, 4.1], [17.0, 4.1]]), ('option_E_grid_edge_12', [[17.0, 3.0999999999999996], [17.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path([[14.15, 3.5999999999999996], [14.5, 3.84], [14.85, 3.5999999999999996], [14.5, 3.3599999999999994], [14.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_E_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[14.15, 3.5999999999999996], [14.5, 3.84], [14.85, 3.5999999999999996], [14.5, 3.3599999999999994], [14.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_E_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_027, [1] + [4] * 12 + [79], id='option_E_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_027, [1] + [4] * 12 + [79], id='option_E_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[16.5, 3.26], [16.4, 3.3499999999999996], [16.16, 3.55], [16.16, 3.7199999999999998], [16.16, 3.9399999999999995], [16.39, 4.029999999999999], [16.5, 3.8], [16.61, 4.029999999999999], [16.84, 3.9399999999999995], [16.84, 3.7199999999999998], [16.84, 3.55], [16.6, 3.3499999999999996], [16.5, 3.26], [16.5, 3.26]], [1] + [4] * 12 + [79], id='option_E_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[16.5, 3.26], [16.4, 3.3499999999999996], [16.16, 3.55], [16.16, 3.7199999999999998], [16.16, 3.9399999999999995], [16.39, 4.029999999999999], [16.5, 3.8], [16.61, 4.029999999999999], [16.84, 3.9399999999999995], [16.84, 3.7199999999999998], [16.84, 3.55], [16.6, 3.3499999999999996], [16.5, 3.26], [16.5, 3.26]], [1] + [4] * 12 + [79], id='option_E_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_010, self._geometry_03, id='option_E_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_010, self._geometry_03, id='option_E_cell_1_0_mark', capstyle='butt', joinstyle='round')
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
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane553_C01.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({17, 18, 20, 28, 29, 30, 31, 33, 39, 40, 41, 42, 50}, {'color': '#DC2626', 'linewidth': 1.5})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane553_C02.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({17, 18, 20, 28, 29, 30, 31, 33, 39, 40, 41, 42, 50}, {'color': '#2563EB', 'linewidth': 1.5})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane553_C03.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({17, 18, 20, 28, 29, 30, 31, 33, 39, 40, 41, 42, 50}, {'color': '#EA580C', 'linewidth': 2.0})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane553_C04.png'
        with Canvas(PLANE, xlim=(-0.4223666626169358, 17.422366662616938), ylim=(-1.266545380396268, 16.57818794483761)) as c:
            self._draw_base(c, hi={0: [({17, 18, 20, 28, 29, 30, 31, 33, 39, 40, 41, 42, 50}, {'color': '#2563EB', 'linewidth': 2.0})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane553')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane553().draw(args.output, variant=args.variant))
