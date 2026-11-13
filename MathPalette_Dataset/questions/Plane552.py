"""Collected question Plane552; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane552:
    variants = ('C01', 'C02', 'C03', 'C04')

    def __init__(self):
        self._samples_001 = [
            [10.15, 7.800000000000001], [10.15, 7.640000000000001], [10.32, 7.5600000000000005],
            [10.425, 7.665000000000001], [10.32, 7.420000000000001], [10.64, 7.370000000000001],
            [10.7, 7.5600000000000005], [10.75, 7.660000000000001], [10.7, 7.745000000000001],
            [10.65, 7.755000000000001], [10.74, 7.755000000000001], [10.79, 7.720000000000001],
            [10.84, 7.670000000000001], [10.84, 7.930000000000001], [10.79, 7.880000000000001],
            [10.74, 7.845000000000001], [10.65, 7.845000000000001], [10.7, 7.855], [10.75, 7.94],
            [10.7, 8.040000000000001], [10.64, 8.23], [10.32, 8.180000000000001],
            [10.425, 7.9350000000000005], [10.32, 8.040000000000001], [10.15, 7.960000000000001],
            [10.15, 7.800000000000001], [10.15, 7.800000000000001]
        ]
        self._samples_002 = [
            [9.5, 8.450000000000001], [9.66, 8.450000000000001], [9.74, 8.620000000000001],
            [9.635, 8.725000000000001], [9.88, 8.620000000000001], [9.93, 8.940000000000001], [9.74, 9.0],
            [9.64, 9.05], [9.555, 9.0], [9.545, 8.950000000000001], [9.545, 9.040000000000001], [9.58, 9.09],
            [9.63, 9.14], [9.37, 9.14], [9.42, 9.09], [9.455, 9.040000000000001], [9.455, 8.950000000000001],
            [9.445, 9.0], [9.36, 9.05], [9.26, 9.0], [9.07, 8.940000000000001], [9.12, 8.620000000000001],
            [9.365, 8.725000000000001], [9.26, 8.620000000000001], [9.34, 8.450000000000001],
            [9.5, 8.450000000000001], [9.5, 8.450000000000001]
        ]
        self._samples_003 = [
            [7.85, 9.8], [7.85, 9.96], [7.68, 10.040000000000001], [7.575, 9.935], [7.68, 10.180000000000001],
            [7.36, 10.23], [7.3, 10.040000000000001], [7.25, 9.940000000000001], [7.3, 9.855], [7.35, 9.845],
            [7.26, 9.845], [7.21, 9.88], [7.16, 9.930000000000001], [7.16, 9.67], [7.21, 9.72], [7.26, 9.755],
            [7.35, 9.755], [7.3, 9.745000000000001], [7.25, 9.66], [7.3, 9.56], [7.36, 9.370000000000001],
            [7.68, 9.42], [7.575, 9.665000000000001], [7.68, 9.56], [7.85, 9.64], [7.85, 9.8], [7.85, 9.8]
        ]
        self._samples_004 = [[x + -2.0, y + 2.0] for x, y in self._samples_001]
        self._samples_005 = [[x + -9.5, y + -5.2] for x, y in self._samples_001]
        self._samples_006 = [
            [2.0, 3.9499999999999997], [1.84, 3.9499999999999997], [1.76, 3.78], [1.865, 3.675], [1.62, 3.78],
            [1.57, 3.4599999999999995], [1.76, 3.3999999999999995], [1.8599999999999999, 3.3499999999999996],
            [1.945, 3.3999999999999995], [1.955, 3.4499999999999997], [1.955, 3.3599999999999994],
            [1.92, 3.3099999999999996], [1.87, 3.26], [2.13, 3.26], [2.08, 3.3099999999999996],
            [2.045, 3.3599999999999994], [2.045, 3.4499999999999997], [2.055, 3.3999999999999995],
            [2.14, 3.3499999999999996], [2.24, 3.3999999999999995], [2.43, 3.4599999999999995], [2.38, 3.78],
            [2.135, 3.675], [2.24, 3.78], [2.16, 3.9499999999999997], [2.0, 3.9499999999999997],
            [2.0, 3.9499999999999997]
        ]
        self._samples_007 = [[x + -6.0, y + -5.2] for x, y in self._samples_001]
        self._samples_008 = [[x + 3.5, y + -1.0] for x, y in self._samples_006]
        self._samples_009 = [[x + 3.5, y + 0.0] for x, y in self._samples_006]
        self._samples_010 = [[x + -2.5, y + -4.2] for x, y in self._samples_001]
        self._samples_011 = [[x + 7.0, y + 0.0] for x, y in self._samples_006]
        self._samples_012 = [[x + 2.0, y + -6.2] for x, y in self._samples_002]
        self._samples_013 = [[x + 10.5, y + 0.0] for x, y in self._samples_006]
        self._samples_014 = [[x + 4.5, y + -5.2] for x, y in self._samples_001]
        self._samples_015 = [[x + 14.0, y + 0.0] for x, y in self._samples_006]
        self._samples_016 = [
            [6.15, 7.800000000000001], [6.27, 7.700000000000001], [6.42, 7.490000000000001],
            [6.58, 7.490000000000001], [6.79, 7.490000000000001], [6.81, 7.700000000000001],
            [6.66, 7.745000000000001], [6.75, 7.745000000000001], [6.8, 7.710000000000001],
            [6.84, 7.680000000000001], [6.84, 7.920000000000001], [6.8, 7.890000000000001], [6.75, 7.855],
            [6.66, 7.855], [6.81, 7.9], [6.79, 8.110000000000001], [6.58, 8.110000000000001],
            [6.42, 8.110000000000001], [6.27, 7.9], [6.15, 7.800000000000001], [6.15, 7.800000000000001]
        ]
        self._samples_017 = [
            [7.5, 7.450000000000001], [7.588167787843871, 7.6786474508437585],
            [7.832869780703303, 7.691844051968769], [7.642658477444273, 7.846352549156243],
            [7.705724838302365, 8.083155948031232], [7.5, 7.950000000000001],
            [7.294275161697635, 8.083155948031232], [7.357341522555727, 7.846352549156243],
            [7.167130219296697, 7.691844051968769], [7.411832212156129, 7.6786474508437585],
            [7.5, 7.450000000000001]
        ]
        self._samples_018 = [
            [9.5, 7.450000000000001], [9.6, 7.57], [9.81, 7.720000000000001], [9.81, 7.880000000000001],
            [9.81, 8.09], [9.6, 8.110000000000001], [9.555, 7.960000000000001], [9.555, 8.05],
            [9.59, 8.100000000000001], [9.62, 8.14], [9.38, 8.14], [9.41, 8.100000000000001], [9.445, 8.05],
            [9.445, 7.960000000000001], [9.4, 8.110000000000001], [9.19, 8.09], [9.19, 7.880000000000001],
            [9.19, 7.720000000000001], [9.4, 7.57], [9.5, 7.450000000000001], [9.5, 7.450000000000001]
        ]
        self._samples_019 = [[x + -1.0, y + 1.0] for x, y in self._samples_017]
        self._samples_020 = [
            [7.85, 8.8], [7.73, 8.9], [7.58, 9.110000000000001], [7.42, 9.110000000000001],
            [7.21, 9.110000000000001], [7.19, 8.9], [7.34, 8.855], [7.25, 8.855], [7.2, 8.89], [7.16, 8.92],
            [7.16, 8.680000000000001], [7.2, 8.71], [7.25, 8.745000000000001], [7.34, 8.745000000000001],
            [7.19, 8.700000000000001], [7.21, 8.49], [7.42, 8.49], [7.58, 8.49], [7.73, 8.700000000000001],
            [7.85, 8.8], [7.85, 8.8]
        ]
        self._samples_021 = [
            [6.15, 9.8], [6.378647450843758, 9.71183221215613], [6.391844051968769, 9.467130219296697],
            [6.546352549156242, 9.657341522555727], [6.783155948031231, 9.594275161697635], [6.65, 9.8],
            [6.783155948031232, 10.005724838302367], [6.546352549156242, 9.942658477444274],
            [6.391844051968769, 10.132869780703304], [6.378647450843758, 9.888167787843871], [6.15, 9.8]
        ]
        self._samples_022 = [[x + 3.0, y + 0.0] for x, y in self._samples_021]
        self._samples_023 = [
            [8.5, 11.15], [8.4, 11.030000000000001], [8.19, 10.88], [8.19, 10.72], [8.19, 10.510000000000002],
            [8.4, 10.49], [8.445, 10.64], [8.445, 10.55], [8.41, 10.5], [8.38, 10.46], [8.62, 10.46],
            [8.59, 10.5], [8.555, 10.55], [8.555, 10.64], [8.6, 10.49], [8.81, 10.510000000000002],
            [8.81, 10.72], [8.81, 10.88], [8.6, 11.030000000000001], [8.5, 11.15], [8.5, 11.15]
        ]
        self._samples_024 = [[x + -4.5, y + -7.2] for x, y in self._samples_021]
        self._samples_025 = [
            [1.34, 3.5999999999999996], [1.25, 3.4999999999999996], [1.05, 3.26], [0.88, 3.26],
            [0.6599999999999999, 3.26], [0.5700000000000001, 3.4899999999999998], [0.8, 3.5999999999999996],
            [0.5700000000000001, 3.7099999999999995], [0.6599999999999999, 3.9399999999999995],
            [0.88, 3.9399999999999995], [1.05, 3.9399999999999995], [1.25, 3.6999999999999997],
            [1.34, 3.5999999999999996], [1.34, 3.5999999999999996]
        ]
        self._samples_026 = [[x + 3.5, y + 0.0] for x, y in self._samples_025]
        self._samples_027 = [[x + 7.0, y + -1.0] for x, y in self._samples_025]
        self._samples_028 = [
            [9.0, 2.9499999999999997], [8.91183221215613, 2.721352549156242],
            [8.667130219296697, 2.7081559480312314], [8.857341522555727, 2.5536474508437577],
            [8.794275161697634, 2.316844051968768], [9.0, 2.4499999999999997],
            [9.205724838302366, 2.316844051968768], [9.142658477444273, 2.5536474508437577],
            [9.332869780703303, 2.708155948031231], [9.08816778784387, 2.721352549156242],
            [9.0, 2.9499999999999997]
        ]
        self._samples_029 = [[x + 6.0, y + -7.2] for x, y in self._samples_021]
        self._samples_030 = [[x + 10.5, y + 0.0] for x, y in self._samples_025]
        self._samples_031 = [[x + 7.0, y + 0.0] for x, y in self._samples_028]
        self._samples_032 = [[x + 14.0, y + 0.0] for x, y in self._samples_025]
        self._geometry_01 = [
            ('template_grid_edge_00', [[7.5, 12.1], [7.5, 13.1]]),
            ('template_grid_edge_01', [[7.5, 12.1], [8.5, 12.1]]),
            ('template_grid_edge_02', [[7.5, 13.1], [7.5, 14.1]]),
            ('template_grid_edge_03', [[7.5, 13.1], [8.5, 13.1]]),
            ('template_grid_edge_04', [[7.5, 14.1], [8.5, 14.1]]),
            ('template_grid_edge_05', [[8.5, 12.1], [8.5, 13.1]]),
            ('template_grid_edge_06', [[8.5, 12.1], [9.5, 12.1]]),
            ('template_grid_edge_07', [[8.5, 13.1], [8.5, 14.1]]),
            ('template_grid_edge_08', [[8.5, 13.1], [9.5, 13.1]]),
            ('template_grid_edge_09', [[8.5, 14.1], [9.5, 14.1]]),
            ('template_grid_edge_10', [[9.5, 12.1], [9.5, 13.1]]),
            ('template_grid_edge_11', [[9.5, 13.1], [9.5, 14.1]]),
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
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_017, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_017, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[8.5, 8.14], [8.6, 8.05], [8.84, 7.8500000000000005], [8.84, 7.680000000000001], [8.84, 7.460000000000001], [8.61, 7.370000000000001], [8.5, 7.6000000000000005], [8.39, 7.370000000000001], [8.16, 7.460000000000001], [8.16, 7.680000000000001], [8.16, 7.8500000000000005], [8.4, 8.05], [8.5, 8.14], [8.5, 8.14]], [1] + [4] * 12 + [79], id='board_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.5, 8.14], [8.6, 8.05], [8.84, 7.8500000000000005], [8.84, 7.680000000000001], [8.84, 7.460000000000001], [8.61, 7.370000000000001], [8.5, 7.6000000000000005], [8.39, 7.370000000000001], [8.16, 7.460000000000001], [8.16, 7.680000000000001], [8.16, 7.8500000000000005], [8.4, 8.05], [8.5, 8.14], [8.5, 8.14]], [1] + [4] * 12 + [79], id='board_cell_2_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_001, self._geometry_03, id='board_cell_4_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_001, self._geometry_03, id='board_cell_4_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_019, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_019, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[8.5, 9.14], [8.6, 9.05], [8.84, 8.850000000000001], [8.84, 8.680000000000001], [8.84, 8.46], [8.61, 8.370000000000001], [8.5, 8.600000000000001], [8.39, 8.370000000000001], [8.16, 8.46], [8.16, 8.680000000000001], [8.16, 8.850000000000001], [8.4, 9.05], [8.5, 9.14], [8.5, 9.14]], [1] + [4] * 12 + [79], id='board_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.5, 9.14], [8.6, 9.05], [8.84, 8.850000000000001], [8.84, 8.680000000000001], [8.84, 8.46], [8.61, 8.370000000000001], [8.5, 8.600000000000001], [8.39, 8.370000000000001], [8.16, 8.46], [8.16, 8.680000000000001], [8.16, 8.850000000000001], [8.4, 9.05], [8.5, 9.14], [8.5, 9.14]], [1] + [4] * 12 + [79], id='board_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_1_mark', capstyle='butt', joinstyle='round')
        c.path([[10.15, 8.8], [10.5, 9.040000000000001], [10.85, 8.8], [10.5, 8.56], [10.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_4_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.15, 8.8], [10.5, 9.040000000000001], [10.85, 8.8], [10.5, 8.56], [10.15, 8.8]], [1, 2, 2, 2, 79], id='board_cell_4_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_021, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_021, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_0_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_004, self._geometry_03, id='board_cell_2_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_004, self._geometry_03, id='board_cell_2_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_022, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_2_mark', capstyle='butt', joinstyle='round')
        c.path([[10.5, 10.15], [10.74, 9.8], [10.5, 9.450000000000001], [10.26, 9.8], [10.5, 10.15]], [1, 2, 2, 2, 79], id='board_cell_4_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.5, 10.15], [10.74, 9.8], [10.5, 9.450000000000001], [10.26, 9.8], [10.5, 10.15]], [1, 2, 2, 2, 79], id='board_cell_4_2_mark', capstyle='butt', joinstyle='round')
        c.path([[6.5, 11.15], [6.74, 10.8], [6.5, 10.450000000000001], [6.26, 10.8], [6.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_0_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.5, 11.15], [6.74, 10.8], [6.5, 10.450000000000001], [6.26, 10.8], [6.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_0_3_mark', capstyle='butt', joinstyle='round')
        c.path([[7.16, 10.8], [7.25, 10.9], [7.45, 11.14], [7.62, 11.14], [7.84, 11.14], [7.93, 10.91], [7.7, 10.8], [7.93, 10.690000000000001], [7.84, 10.46], [7.62, 10.46], [7.45, 10.46], [7.25, 10.700000000000001], [7.16, 10.8], [7.16, 10.8]], [1] + [4] * 12 + [79], id='board_cell_1_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.16, 10.8], [7.25, 10.9], [7.45, 11.14], [7.62, 11.14], [7.84, 11.14], [7.93, 10.91], [7.7, 10.8], [7.93, 10.690000000000001], [7.84, 10.46], [7.62, 10.46], [7.45, 10.46], [7.25, 10.700000000000001], [7.16, 10.8], [7.16, 10.8]], [1] + [4] * 12 + [79], id='board_cell_1_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_023, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_2_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_023, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_2_3_mark', capstyle='butt', joinstyle='round')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.5, 11.15], [9.74, 10.8], [9.5, 10.450000000000001], [9.26, 10.8], [9.5, 11.15]], [1, 2, 2, 2, 79], id='board_cell_3_3_mark', capstyle='butt', joinstyle='round')
        c.path([[10.5, 11.14], [10.6, 11.05], [10.84, 10.850000000000001], [10.84, 10.680000000000001], [10.84, 10.46], [10.61, 10.370000000000001], [10.5, 10.600000000000001], [10.39, 10.370000000000001], [10.16, 10.46], [10.16, 10.680000000000001], [10.16, 10.850000000000001], [10.4, 11.05], [10.5, 11.14], [10.5, 11.14]], [1] + [4] * 12 + [79], id='board_cell_4_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[10.5, 11.14], [10.6, 11.05], [10.84, 10.850000000000001], [10.84, 10.680000000000001], [10.84, 10.46], [10.61, 10.370000000000001], [10.5, 10.600000000000001], [10.39, 10.370000000000001], [10.16, 10.46], [10.16, 10.680000000000001], [10.16, 10.850000000000001], [10.4, 11.05], [10.5, 11.14], [10.5, 11.14]], [1] + [4] * 12 + [79], id='board_cell_4_3_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(41, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_A_grid_edge_00', [[0.5, 2.0999999999999996], [0.5, 3.0999999999999996]]), ('option_A_grid_edge_01', [[0.5, 2.0999999999999996], [1.5, 2.0999999999999996]]), ('option_A_grid_edge_02', [[0.5, 3.0999999999999996], [0.5, 4.1]]), ('option_A_grid_edge_03', [[0.5, 3.0999999999999996], [1.5, 3.0999999999999996]]), ('option_A_grid_edge_04', [[0.5, 4.1], [1.5, 4.1]]), ('option_A_grid_edge_05', [[1.5, 2.0999999999999996], [1.5, 3.0999999999999996]]), ('option_A_grid_edge_06', [[1.5, 2.0999999999999996], [2.5, 2.0999999999999996]]), ('option_A_grid_edge_07', [[1.5, 3.0999999999999996], [1.5, 4.1]]), ('option_A_grid_edge_08', [[1.5, 3.0999999999999996], [2.5, 3.0999999999999996]]), ('option_A_grid_edge_09', [[1.5, 4.1], [2.5, 4.1]]), ('option_A_grid_edge_10', [[2.5, 2.0999999999999996], [2.5, 3.0999999999999996]]), ('option_A_grid_edge_11', [[2.5, 3.0999999999999996], [2.5, 4.1]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_024, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_A_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_024, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_A_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_A_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_025, [1] + [4] * 12 + [79], id='option_A_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_006, self._geometry_03, id='option_A_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_006, self._geometry_03, id='option_A_cell_1_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_B_grid_edge_00', [[4.0, 2.0999999999999996], [4.0, 3.0999999999999996]]), ('option_B_grid_edge_01', [[4.0, 2.0999999999999996], [5.0, 2.0999999999999996]]), ('option_B_grid_edge_02', [[4.0, 3.0999999999999996], [4.0, 4.1]]), ('option_B_grid_edge_03', [[4.0, 3.0999999999999996], [5.0, 3.0999999999999996]]), ('option_B_grid_edge_04', [[4.0, 4.1], [5.0, 4.1]]), ('option_B_grid_edge_05', [[5.0, 2.0999999999999996], [5.0, 3.0999999999999996]]), ('option_B_grid_edge_06', [[5.0, 2.0999999999999996], [6.0, 2.0999999999999996]]), ('option_B_grid_edge_07', [[5.0, 3.0999999999999996], [5.0, 4.1]]), ('option_B_grid_edge_08', [[5.0, 3.0999999999999996], [6.0, 3.0999999999999996]]), ('option_B_grid_edge_09', [[5.0, 4.1], [6.0, 4.1]]), ('option_B_grid_edge_10', [[6.0, 2.0999999999999996], [6.0, 3.0999999999999996]]), ('option_B_grid_edge_11', [[6.0, 3.0999999999999996], [6.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_007, self._geometry_03, id='option_B_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_007, self._geometry_03, id='option_B_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_008, self._geometry_03, id='option_B_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_008, self._geometry_03, id='option_B_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_026, [1] + [4] * 12 + [79], id='option_B_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_026, [1] + [4] * 12 + [79], id='option_B_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_009, self._geometry_03, id='option_B_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_009, self._geometry_03, id='option_B_cell_1_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_C_grid_edge_00', [[7.5, 2.0999999999999996], [7.5, 3.0999999999999996]]), ('option_C_grid_edge_01', [[7.5, 2.0999999999999996], [8.5, 2.0999999999999996]]), ('option_C_grid_edge_02', [[7.5, 3.0999999999999996], [7.5, 4.1]]), ('option_C_grid_edge_03', [[7.5, 3.0999999999999996], [8.5, 3.0999999999999996]]), ('option_C_grid_edge_04', [[7.5, 4.1], [8.5, 4.1]]), ('option_C_grid_edge_05', [[8.5, 2.0999999999999996], [8.5, 3.0999999999999996]]), ('option_C_grid_edge_06', [[8.5, 2.0999999999999996], [9.5, 2.0999999999999996]]), ('option_C_grid_edge_07', [[8.5, 3.0999999999999996], [8.5, 4.1]]), ('option_C_grid_edge_08', [[8.5, 3.0999999999999996], [9.5, 3.0999999999999996]]), ('option_C_grid_edge_09', [[8.5, 4.1], [9.5, 4.1]]), ('option_C_grid_edge_10', [[9.5, 2.0999999999999996], [9.5, 3.0999999999999996]]), ('option_C_grid_edge_11', [[9.5, 3.0999999999999996], [9.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_027, [1] + [4] * 12 + [79], id='option_C_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_027, [1] + [4] * 12 + [79], id='option_C_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_028, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_028, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_010, self._geometry_03, id='option_C_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_010, self._geometry_03, id='option_C_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_011, self._geometry_03, id='option_C_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_011, self._geometry_03, id='option_C_cell_1_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_D_grid_edge_00', [[11.0, 2.0999999999999996], [11.0, 3.0999999999999996]]), ('option_D_grid_edge_01', [[11.0, 2.0999999999999996], [12.0, 2.0999999999999996]]), ('option_D_grid_edge_02', [[11.0, 3.0999999999999996], [11.0, 4.1]]), ('option_D_grid_edge_03', [[11.0, 3.0999999999999996], [12.0, 3.0999999999999996]]), ('option_D_grid_edge_04', [[11.0, 4.1], [12.0, 4.1]]), ('option_D_grid_edge_05', [[12.0, 2.0999999999999996], [12.0, 3.0999999999999996]]), ('option_D_grid_edge_06', [[12.0, 2.0999999999999996], [13.0, 2.0999999999999996]]), ('option_D_grid_edge_07', [[12.0, 3.0999999999999996], [12.0, 4.1]]), ('option_D_grid_edge_08', [[12.0, 3.0999999999999996], [13.0, 3.0999999999999996]]), ('option_D_grid_edge_09', [[12.0, 4.1], [13.0, 4.1]]), ('option_D_grid_edge_10', [[13.0, 2.0999999999999996], [13.0, 3.0999999999999996]]), ('option_D_grid_edge_11', [[13.0, 3.0999999999999996], [13.0, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_012, self._geometry_03, id='option_D_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_012, self._geometry_03, id='option_D_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_029, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_D_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_029, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_D_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_030, [1] + [4] * 12 + [79], id='option_D_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_030, [1] + [4] * 12 + [79], id='option_D_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_013, self._geometry_03, id='option_D_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_013, self._geometry_03, id='option_D_cell_1_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_E_grid_edge_00', [[14.5, 2.0999999999999996], [14.5, 3.0999999999999996]]), ('option_E_grid_edge_01', [[14.5, 2.0999999999999996], [15.5, 2.0999999999999996]]), ('option_E_grid_edge_02', [[14.5, 3.0999999999999996], [14.5, 4.1]]), ('option_E_grid_edge_03', [[14.5, 3.0999999999999996], [15.5, 3.0999999999999996]]), ('option_E_grid_edge_04', [[14.5, 4.1], [15.5, 4.1]]), ('option_E_grid_edge_05', [[15.5, 2.0999999999999996], [15.5, 3.0999999999999996]]), ('option_E_grid_edge_06', [[15.5, 2.0999999999999996], [16.5, 2.0999999999999996]]), ('option_E_grid_edge_07', [[15.5, 3.0999999999999996], [15.5, 4.1]]), ('option_E_grid_edge_08', [[15.5, 3.0999999999999996], [16.5, 3.0999999999999996]]), ('option_E_grid_edge_09', [[15.5, 4.1], [16.5, 4.1]]), ('option_E_grid_edge_10', [[16.5, 2.0999999999999996], [16.5, 3.0999999999999996]]), ('option_E_grid_edge_11', [[16.5, 3.0999999999999996], [16.5, 4.1]])]:
            c.line(points, id=object_id)
        c.path(self._samples_014, self._geometry_03, id='option_E_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_014, self._geometry_03, id='option_E_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_031, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_E_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_031, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_E_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_032, [1] + [4] * 12 + [79], id='option_E_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_032, [1] + [4] * 12 + [79], id='option_E_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_015, self._geometry_03, id='option_E_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_015, self._geometry_03, id='option_E_cell_1_1_mark', capstyle='butt', joinstyle='round')
        for object_id, text, anchor in [('option_A_label', '(A)', (1.5, 1.4999999999999996)), ('option_B_label', '(B)', (5.0, 1.4999999999999996)), ('option_C_label', '(C)', (8.5, 1.4999999999999996)), ('option_D_label', '(D)', (12.0, 1.4999999999999996)), ('option_E_label', '(E)', (15.5, 1.4999999999999996))]:
            c.text(text, anchor, id=object_id, zorder=3)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane552_C01.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({32, 33, 34, 35, 37, 41, 42, 43, 44, 46, 50, 52}, {'color': '#DC2626', 'linewidth': 1.5})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane552_C02.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({32, 33, 34, 35, 37, 41, 42, 43, 44, 46, 50, 52}, {'color': '#16A34A', 'linewidth': 1.5})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane552_C03.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({32, 33, 34, 35, 37, 41, 42, 43, 44, 46, 50, 52}, {'color': '#EA580C', 'linewidth': 2.0})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane552_C04.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({32, 33, 34, 35, 37, 41, 42, 43, 44, 46, 50, 52}, {'color': '#2563EB', 'linewidth': 2.0})], 41: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane552')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane552().draw(args.output, variant=args.variant))
