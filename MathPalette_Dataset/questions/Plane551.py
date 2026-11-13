"""Collected question Plane551; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane551:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self._samples_001 = [
            [8.35, 7.800000000000001], [8.35, 7.960000000000001], [8.18, 8.040000000000001],
            [8.075, 7.9350000000000005], [8.18, 8.180000000000001], [7.86, 8.23], [7.8, 8.040000000000001],
            [7.75, 7.94], [7.8, 7.855], [7.85, 7.845000000000001], [7.76, 7.845000000000001],
            [7.71, 7.880000000000001], [7.66, 7.930000000000001], [7.66, 7.670000000000001],
            [7.71, 7.720000000000001], [7.76, 7.755000000000001], [7.85, 7.755000000000001],
            [7.8, 7.745000000000001], [7.75, 7.660000000000001], [7.8, 7.5600000000000005],
            [7.86, 7.370000000000001], [8.18, 7.420000000000001], [8.075, 7.665000000000001],
            [8.18, 7.5600000000000005], [8.35, 7.640000000000001], [8.35, 7.800000000000001],
            [8.35, 7.800000000000001]
        ]
        self._samples_002 = [
            [10.0, 8.15], [9.84, 8.15], [9.76, 7.98], [9.865, 7.875000000000001], [9.62, 7.98],
            [9.57, 7.660000000000001], [9.76, 7.6000000000000005], [9.86, 7.550000000000001],
            [9.945, 7.6000000000000005], [9.955, 7.65], [9.955, 7.5600000000000005],
            [9.92, 7.510000000000001], [9.87, 7.460000000000001], [10.13, 7.460000000000001],
            [10.08, 7.510000000000001], [10.045, 7.5600000000000005], [10.045, 7.65],
            [10.055, 7.6000000000000005], [10.14, 7.550000000000001], [10.24, 7.6000000000000005],
            [10.43, 7.660000000000001], [10.38, 7.98], [10.135, 7.875000000000001], [10.24, 7.98],
            [10.16, 8.15], [10.0, 8.15], [10.0, 8.15]
        ]
        self._samples_003 = [
            [8.0, 8.450000000000001], [8.16, 8.450000000000001], [8.24, 8.620000000000001],
            [8.135, 8.725000000000001], [8.38, 8.620000000000001], [8.43, 8.940000000000001], [8.24, 9.0],
            [8.14, 9.05], [8.055, 9.0], [8.045, 8.950000000000001], [8.045, 9.040000000000001], [8.08, 9.09],
            [8.13, 9.14], [7.87, 9.14], [7.92, 9.09], [7.955, 9.040000000000001], [7.955, 8.950000000000001],
            [7.945, 9.0], [7.86, 9.05], [7.76, 9.0], [7.57, 8.940000000000001], [7.62, 8.620000000000001],
            [7.865, 8.725000000000001], [7.76, 8.620000000000001], [7.84, 8.450000000000001],
            [8.0, 8.450000000000001], [8.0, 8.450000000000001]
        ]
        self._samples_004 = [[x + 0.0, y + 3.0] for x, y in self._samples_001]
        self._samples_005 = [[x + -6.0, y + -5.2] for x, y in self._samples_001]
        self._samples_006 = [[x + -4.5, y + -5.2] for x, y in self._samples_002]
        self._samples_007 = [[x + 1.0, y + -5.2] for x, y in self._samples_001]
        self._samples_008 = [[x + 3.5, y + -5.2] for x, y in self._samples_001]
        self._samples_009 = [[x + 6.0, y + -5.2] for x, y in self._samples_002]
        self._samples_010 = [
            [9.65, 8.8], [9.77, 8.700000000000001], [9.92, 8.49], [10.08, 8.49], [10.29, 8.49],
            [10.31, 8.700000000000001], [10.16, 8.745000000000001], [10.25, 8.745000000000001], [10.3, 8.71],
            [10.34, 8.680000000000001], [10.34, 8.92], [10.3, 8.89], [10.25, 8.855], [10.16, 8.855],
            [10.31, 8.9], [10.29, 9.110000000000001], [10.08, 9.110000000000001], [9.92, 9.110000000000001],
            [9.77, 8.9], [9.65, 8.8], [9.65, 8.8]
        ]
        self._samples_011 = [[x + -3.0, y + 1.0] for x, y in self._samples_010]
        self._samples_012 = [
            [8.0, 10.15], [7.9, 10.030000000000001], [7.69, 9.88], [7.69, 9.72], [7.69, 9.510000000000002],
            [7.9, 9.49], [7.945, 9.64], [7.945, 9.55], [7.91, 9.5], [7.88, 9.46], [8.12, 9.46], [8.09, 9.5],
            [8.055, 9.55], [8.055, 9.64], [8.1, 9.49], [8.31, 9.510000000000002], [8.31, 9.72], [8.31, 9.88],
            [8.1, 10.030000000000001], [8.0, 10.15], [8.0, 10.15]
        ]
        self._samples_013 = [
            [9.65, 9.8], [9.878647450843758, 9.71183221215613], [9.891844051968768, 9.467130219296697],
            [10.046352549156243, 9.657341522555727], [10.283155948031231, 9.594275161697635], [10.15, 9.8],
            [10.283155948031231, 10.005724838302367], [10.046352549156243, 9.942658477444274],
            [9.891844051968768, 10.132869780703304], [9.878647450843758, 9.888167787843871], [9.65, 9.8]
        ]
        self._samples_014 = [
            [9.0, 11.15], [8.91183221215613, 10.921352549156243], [8.667130219296697, 10.908155948031233],
            [8.857341522555727, 10.753647450843758], [8.794275161697634, 10.51684405196877], [9.0, 10.65],
            [9.205724838302366, 10.51684405196877], [9.142658477444273, 10.753647450843758],
            [9.332869780703303, 10.908155948031233], [9.08816778784387, 10.921352549156243], [9.0, 11.15]
        ]
        self._samples_015 = [[x + 0.0, y + 1.0] for x, y in self._samples_013]
        self._samples_016 = [[x + -9.0, y + -6.2] for x, y in self._samples_010]
        self._samples_017 = [[x + -5.5, y + -6.2] for x, y in self._samples_010]
        self._samples_018 = [[x + -2.0, y + -6.2] for x, y in self._samples_010]
        self._samples_019 = [[x + -2.0, y + -6.2] for x, y in self._samples_013]
        self._samples_020 = [[x + 2.5, y + -6.2] for x, y in self._samples_010]
        self._samples_021 = [[x + 5.0, y + -6.2] for x, y in self._samples_010]
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
            ('template_grid_edge_09', [[9.5, 12.1], [9.5, 13.1]]),
            ('board_grid_edge_00', [[6.5, 7.300000000000001], [6.5, 8.3]]),
            ('board_grid_edge_01', [[6.5, 7.300000000000001], [7.5, 7.300000000000001]]),
            ('board_grid_edge_02', [[6.5, 8.3], [6.5, 9.3]]),
            ('board_grid_edge_03', [[6.5, 8.3], [7.5, 8.3]]),
            ('board_grid_edge_04', [[6.5, 9.3], [6.5, 10.3]]),
            ('board_grid_edge_05', [[6.5, 9.3], [7.5, 9.3]]),
            ('board_grid_edge_06', [[6.5, 10.3], [6.5, 11.3]]),
            ('board_grid_edge_07', [[6.5, 10.3], [7.5, 10.3]]),
            ('board_grid_edge_08', [[6.5, 11.3], [7.5, 11.3]]),
            ('board_grid_edge_09', [[7.5, 7.300000000000001], [7.5, 8.3]]),
            ('board_grid_edge_10', [[7.5, 7.300000000000001], [8.5, 7.300000000000001]]),
            ('board_grid_edge_11', [[7.5, 8.3], [7.5, 9.3]]),
            ('board_grid_edge_12', [[7.5, 8.3], [8.5, 8.3]]),
            ('board_grid_edge_13', [[7.5, 9.3], [7.5, 10.3]]),
            ('board_grid_edge_14', [[7.5, 9.3], [8.5, 9.3]]),
            ('board_grid_edge_15', [[7.5, 10.3], [7.5, 11.3]]),
            ('board_grid_edge_16', [[7.5, 10.3], [8.5, 10.3]]),
            ('board_grid_edge_17', [[7.5, 11.3], [8.5, 11.3]]),
            ('board_grid_edge_18', [[8.5, 7.300000000000001], [8.5, 8.3]]),
            ('board_grid_edge_19', [[8.5, 7.300000000000001], [9.5, 7.300000000000001]]),
            ('board_grid_edge_20', [[8.5, 8.3], [8.5, 9.3]]),
            ('board_grid_edge_21', [[8.5, 8.3], [9.5, 8.3]]),
            ('board_grid_edge_22', [[8.5, 9.3], [8.5, 10.3]]),
            ('board_grid_edge_23', [[8.5, 9.3], [9.5, 9.3]]),
            ('board_grid_edge_24', [[8.5, 10.3], [8.5, 11.3]]),
            ('board_grid_edge_25', [[8.5, 10.3], [9.5, 10.3]]),
            ('board_grid_edge_26', [[8.5, 11.3], [9.5, 11.3]]),
            ('board_grid_edge_27', [[9.5, 7.300000000000001], [9.5, 8.3]]),
            ('board_grid_edge_28', [[9.5, 7.300000000000001], [10.5, 7.300000000000001]]),
            ('board_grid_edge_29', [[9.5, 8.3], [9.5, 9.3]]),
            ('board_grid_edge_30', [[9.5, 8.3], [10.5, 8.3]]),
            ('board_grid_edge_31', [[9.5, 9.3], [9.5, 10.3]]),
            ('board_grid_edge_32', [[9.5, 9.3], [10.5, 9.3]]),
            ('board_grid_edge_33', [[9.5, 10.3], [9.5, 11.3]]),
            ('board_grid_edge_34', [[9.5, 10.3], [10.5, 10.3]]),
            ('board_grid_edge_35', [[9.5, 11.3], [10.5, 11.3]]),
            ('board_grid_edge_36', [[10.5, 7.300000000000001], [10.5, 8.3]]),
            ('board_grid_edge_37', [[10.5, 8.3], [10.5, 9.3]]),
            ('board_grid_edge_38', [[10.5, 9.3], [10.5, 10.3]]),
            ('board_grid_edge_39', [[10.5, 10.3], [10.5, 11.3]])
        ]
        self._geometry_03 = [1] + [4] * 12 + [2] + [4] * 12 + [79]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _defs = [
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
            {}, {}, {}, {}, {'color': '#EA580C', 'linewidth': 1.5}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
        ]
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_01):
            c.line(points, id=object_id, **_ov.get(i, _defs[i]))
        c.path([[7.0, 8.15], [7.24, 7.800000000000001], [7.0, 7.450000000000001], [6.76, 7.800000000000001], [7.0, 8.15]], [1, 2, 2, 2, 79], id='board_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[7.0, 8.15], [7.24, 7.800000000000001], [7.0, 7.450000000000001], [6.76, 7.800000000000001], [7.0, 8.15]], [1, 2, 2, 2, 79], id='board_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_001, self._geometry_03, id='board_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_001, self._geometry_03, id='board_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[8.66, 7.800000000000001], [8.75, 7.9], [8.95, 8.14], [9.12, 8.14], [9.34, 8.14], [9.43, 7.910000000000001], [9.2, 7.800000000000001], [9.43, 7.69], [9.34, 7.460000000000001], [9.12, 7.460000000000001], [8.95, 7.460000000000001], [8.75, 7.700000000000001], [8.66, 7.800000000000001], [8.66, 7.800000000000001]], [1] + [4] * 12 + [79], id='board_cell_2_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.66, 7.800000000000001], [8.75, 7.9], [8.95, 8.14], [9.12, 8.14], [9.34, 8.14], [9.43, 7.910000000000001], [9.2, 7.800000000000001], [9.43, 7.69], [9.34, 7.460000000000001], [9.12, 7.460000000000001], [8.95, 7.460000000000001], [8.75, 7.700000000000001], [8.66, 7.800000000000001], [8.66, 7.800000000000001]], [1] + [4] * 12 + [79], id='board_cell_2_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_002, self._geometry_03, id='board_cell_3_0_mark', capstyle='butt', joinstyle='round')
        c.path([[6.66, 8.8], [6.75, 8.9], [6.95, 9.14], [7.12, 9.14], [7.34, 9.14], [7.43, 8.91], [7.2, 8.8], [7.43, 8.690000000000001], [7.34, 8.46], [7.12, 8.46], [6.95, 8.46], [6.75, 8.700000000000001], [6.66, 8.8], [6.66, 8.8]], [1] + [4] * 12 + [79], id='board_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.66, 8.8], [6.75, 8.9], [6.95, 9.14], [7.12, 9.14], [7.34, 9.14], [7.43, 8.91], [7.2, 8.8], [7.43, 8.690000000000001], [7.34, 8.46], [7.12, 8.46], [6.95, 8.46], [6.75, 8.700000000000001], [6.66, 8.8], [6.66, 8.8]], [1] + [4] * 12 + [79], id='board_cell_0_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_003, self._geometry_03, id='board_cell_1_1_mark', capstyle='butt', joinstyle='round')
        c.path([[8.65, 8.8], [9.0, 9.040000000000001], [9.35, 8.8], [9.0, 8.56], [8.65, 8.8]], [1, 2, 2, 2, 79], id='board_cell_2_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[8.65, 8.8], [9.0, 9.040000000000001], [9.35, 8.8], [9.0, 8.56], [8.65, 8.8]], [1, 2, 2, 2, 79], id='board_cell_2_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_010, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_010, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_3_1_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_011, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_011, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_0_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_012, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_012, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='board_cell_1_2_mark', capstyle='butt', joinstyle='round')
        c.path([[9.0, 10.15], [9.24, 9.8], [9.0, 9.450000000000001], [8.76, 9.8], [9.0, 10.15]], [1, 2, 2, 2, 79], id='board_cell_2_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[9.0, 10.15], [9.24, 9.8], [9.0, 9.450000000000001], [8.76, 9.8], [9.0, 10.15]], [1, 2, 2, 2, 79], id='board_cell_2_2_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_013, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_2_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_013, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_2_mark', capstyle='butt', joinstyle='round')
        c.path([[6.66, 10.8], [6.75, 10.9], [6.95, 11.14], [7.12, 11.14], [7.34, 11.14], [7.43, 10.91], [7.2, 10.8], [7.43, 10.690000000000001], [7.34, 10.46], [7.12, 10.46], [6.95, 10.46], [6.75, 10.700000000000001], [6.66, 10.8], [6.66, 10.8]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[6.66, 10.8], [6.75, 10.9], [6.95, 11.14], [7.12, 11.14], [7.34, 11.14], [7.43, 10.91], [7.2, 10.8], [7.43, 10.690000000000001], [7.34, 10.46], [7.12, 10.46], [6.95, 10.46], [6.75, 10.700000000000001], [6.66, 10.8], [6.66, 10.8]], [1] + [4] * 12 + [79], id='board_cell_0_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_004, self._geometry_03, id='board_cell_1_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_004, self._geometry_03, id='board_cell_1_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_014, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_014, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_2_3_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_015, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_3_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_015, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='board_cell_3_3_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_A_grid_edge_00', [[0.5, 2.0999999999999996], [0.5, 3.0999999999999996]]), ('option_A_grid_edge_01', [[0.5, 2.0999999999999996], [1.5, 2.0999999999999996]]), ('option_A_grid_edge_02', [[0.5, 3.0999999999999996], [0.5, 4.1]]), ('option_A_grid_edge_03', [[0.5, 3.0999999999999996], [1.5, 3.0999999999999996]]), ('option_A_grid_edge_04', [[0.5, 4.1], [1.5, 4.1]]), ('option_A_grid_edge_05', [[1.5, 2.0999999999999996], [1.5, 3.0999999999999996]]), ('option_A_grid_edge_06', [[1.5, 2.0999999999999996], [2.5, 2.0999999999999996]]), ('option_A_grid_edge_07', [[1.5, 3.0999999999999996], [1.5, 4.1]]), ('option_A_grid_edge_08', [[1.5, 3.0999999999999996], [2.5, 3.0999999999999996]]), ('option_A_grid_edge_09', [[2.5, 2.0999999999999996], [2.5, 3.0999999999999996]])]:
            c.line(points, id=object_id)
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_A_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_016, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_A_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_005, self._geometry_03, id='option_A_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[0.65, 3.5999999999999996], [1.0, 3.84], [1.35, 3.5999999999999996], [1.0, 3.3599999999999994], [0.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[0.65, 3.5999999999999996], [1.0, 3.84], [1.35, 3.5999999999999996], [1.0, 3.3599999999999994], [0.65, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_A_cell_0_1_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(40, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_B_grid_edge_00', [[4.0, 2.0999999999999996], [4.0, 3.0999999999999996]]), ('option_B_grid_edge_01', [[4.0, 2.0999999999999996], [5.0, 2.0999999999999996]]), ('option_B_grid_edge_02', [[4.0, 3.0999999999999996], [4.0, 4.1]]), ('option_B_grid_edge_03', [[4.0, 3.0999999999999996], [5.0, 3.0999999999999996]]), ('option_B_grid_edge_04', [[4.0, 4.1], [5.0, 4.1]]), ('option_B_grid_edge_05', [[5.0, 2.0999999999999996], [5.0, 3.0999999999999996]]), ('option_B_grid_edge_06', [[5.0, 2.0999999999999996], [6.0, 2.0999999999999996]]), ('option_B_grid_edge_07', [[5.0, 3.0999999999999996], [5.0, 4.1]]), ('option_B_grid_edge_08', [[5.0, 3.0999999999999996], [6.0, 3.0999999999999996]]), ('option_B_grid_edge_09', [[6.0, 2.0999999999999996], [6.0, 3.0999999999999996]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_017, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_B_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_017, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_B_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_006, self._geometry_03, id='option_B_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_006, self._geometry_03, id='option_B_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[4.15, 3.5999999999999996], [4.5, 3.84], [4.85, 3.5999999999999996], [4.5, 3.3599999999999994], [4.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[4.15, 3.5999999999999996], [4.5, 3.84], [4.85, 3.5999999999999996], [4.5, 3.3599999999999994], [4.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_B_cell_0_1_mark', capstyle='butt', joinstyle='round')
        for object_id, points in [('option_C_grid_edge_00', [[7.5, 2.0999999999999996], [7.5, 3.0999999999999996]]), ('option_C_grid_edge_01', [[7.5, 2.0999999999999996], [8.5, 2.0999999999999996]]), ('option_C_grid_edge_02', [[7.5, 3.0999999999999996], [7.5, 4.1]]), ('option_C_grid_edge_03', [[7.5, 3.0999999999999996], [8.5, 3.0999999999999996]]), ('option_C_grid_edge_04', [[7.5, 4.1], [8.5, 4.1]]), ('option_C_grid_edge_05', [[8.5, 2.0999999999999996], [8.5, 3.0999999999999996]]), ('option_C_grid_edge_06', [[8.5, 2.0999999999999996], [9.5, 2.0999999999999996]]), ('option_C_grid_edge_07', [[8.5, 3.0999999999999996], [8.5, 4.1]]), ('option_C_grid_edge_08', [[8.5, 3.0999999999999996], [9.5, 3.0999999999999996]]), ('option_C_grid_edge_09', [[9.5, 2.0999999999999996], [9.5, 3.0999999999999996]])]:
            c.line(points, id=object_id)
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_C_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_018, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_C_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_007, self._geometry_03, id='option_C_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_007, self._geometry_03, id='option_C_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_019, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_019, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option_C_cell_0_1_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(54, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_D_grid_edge_00', [[11.0, 2.0999999999999996], [11.0, 3.0999999999999996]]), ('option_D_grid_edge_01', [[11.0, 2.0999999999999996], [12.0, 2.0999999999999996]]), ('option_D_grid_edge_02', [[11.0, 3.0999999999999996], [11.0, 4.1]]), ('option_D_grid_edge_03', [[11.0, 3.0999999999999996], [12.0, 3.0999999999999996]]), ('option_D_grid_edge_04', [[11.0, 4.1], [12.0, 4.1]]), ('option_D_grid_edge_05', [[12.0, 2.0999999999999996], [12.0, 3.0999999999999996]]), ('option_D_grid_edge_06', [[12.0, 2.0999999999999996], [13.0, 2.0999999999999996]]), ('option_D_grid_edge_07', [[12.0, 3.0999999999999996], [12.0, 4.1]]), ('option_D_grid_edge_08', [[12.0, 3.0999999999999996], [13.0, 3.0999999999999996]]), ('option_D_grid_edge_09', [[13.0, 2.0999999999999996], [13.0, 3.0999999999999996]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_008, self._geometry_03, id='option_D_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_008, self._geometry_03, id='option_D_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_D_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_020, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_D_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[11.15, 3.5999999999999996], [11.5, 3.84], [11.85, 3.5999999999999996], [11.5, 3.3599999999999994], [11.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[11.15, 3.5999999999999996], [11.5, 3.84], [11.85, 3.5999999999999996], [11.5, 3.3599999999999994], [11.15, 3.5999999999999996]], [1, 2, 2, 2, 79], id='option_D_cell_0_1_mark', capstyle='butt', joinstyle='round')
        _ov = {j: s for idxs, s in _hi.get(61, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('option_E_grid_edge_00', [[14.5, 2.0999999999999996], [14.5, 3.0999999999999996]]), ('option_E_grid_edge_01', [[14.5, 2.0999999999999996], [15.5, 2.0999999999999996]]), ('option_E_grid_edge_02', [[14.5, 3.0999999999999996], [14.5, 4.1]]), ('option_E_grid_edge_03', [[14.5, 3.0999999999999996], [15.5, 3.0999999999999996]]), ('option_E_grid_edge_04', [[14.5, 4.1], [15.5, 4.1]]), ('option_E_grid_edge_05', [[15.5, 2.0999999999999996], [15.5, 3.0999999999999996]]), ('option_E_grid_edge_06', [[15.5, 2.0999999999999996], [16.5, 2.0999999999999996]]), ('option_E_grid_edge_07', [[15.5, 3.0999999999999996], [15.5, 4.1]]), ('option_E_grid_edge_08', [[15.5, 3.0999999999999996], [16.5, 3.0999999999999996]]), ('option_E_grid_edge_09', [[16.5, 2.0999999999999996], [16.5, 3.0999999999999996]])]):
            c.line(points, id=object_id, **_ov[i]) if i in _ov else c.line(points, id=object_id)
        c.path(self._samples_021, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_E_cell_0_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_021, [1] + [4] * 9 + [2] + [4] * 9 + [79], id='option_E_cell_0_0_mark', capstyle='butt', joinstyle='round')
        c.path(self._samples_009, self._geometry_03, id='option_E_cell_1_0_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path(self._samples_009, self._geometry_03, id='option_E_cell_1_0_mark', capstyle='butt', joinstyle='round')
        c.path([[15.0, 3.9499999999999997], [15.24, 3.5999999999999996], [15.0, 3.2499999999999996], [14.76, 3.5999999999999996], [15.0, 3.9499999999999997]], [1, 2, 2, 2, 79], id='option_E_cell_0_1_mark__semantic_fill', zorder=1, edgecolor='none', facecolor='black', capstyle='butt')
        c.path([[15.0, 3.9499999999999997], [15.24, 3.5999999999999996], [15.0, 3.2499999999999996], [14.76, 3.5999999999999996], [15.0, 3.9499999999999997]], [1, 2, 2, 2, 79], id='option_E_cell_0_1_mark', capstyle='butt', joinstyle='round')
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
            self._draw_base(c, hi={0: [({28}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C01.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({10, 11, 12, 13, 15, 19, 20, 21, 22}, {'color': '#EA580C', 'linewidth': 1.5})], 54: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#EA580C'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C02.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({10, 11, 12, 13, 15, 19, 20, 21, 22, 28}, {'color': '#16A34A', 'linewidth': 1.5})], 54: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#16A34A'})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C03.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({29, 30, 31, 33, 37, 38, 39, 40, 46}, {'color': '#EA580C', 'linewidth': 1.5})], 40: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#EA580C'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C04.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({10, 11, 12, 13, 15, 19, 20, 21, 22}, {'color': '#EA580C', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C05.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({28, 29, 30, 31, 33, 37, 38, 39, 40, 46}, {'color': '#DC2626', 'linewidth': 1.5})], 61: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C06.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({28, 29, 30, 31, 33, 37, 38, 39, 40, 46}, {'color': '#2563EB', 'linewidth': 1.5})], 61: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C07.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({28, 29, 30, 31, 33, 37, 38, 39, 40, 46}, {'color': '#2563EB', 'linewidth': 2.0})], 61: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#2563EB', 'linewidth': 1.5})]})
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane551_C08.png'
        with Canvas(PLANE, xlim=(0.10247843518405908, 16.89752156481594), ylim=(-0.7332191815494271, 16.061823948082452)) as c:
            self._draw_base(c, hi={0: [({28, 29, 30, 31, 33, 37, 38, 39, 40, 46}, {'color': '#DC2626', 'linewidth': 2.0})], 61: [({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {'color': '#DC2626', 'linewidth': 1.5})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane551')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane551().draw(args.output, variant=args.variant))
