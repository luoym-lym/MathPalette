"""Collected question Solid111; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid111:
    variants = ('C01',)

    def __init__(self):
        self._geometry_01 = [
            ('B_cell1_-1_hatch1_5', [[8.0, -0.8], [8.2, -1.0]]),
            ('B_cell1_-1_hatch1_6', [[8.0, -0.56], [8.44, -1.0]]),
            ('B_cell1_-1_hatch1_7', [[8.0, -0.31999999999999995], [8.68, -1.0]]),
            ('B_cell1_-1_hatch1_8', [[8.0, -0.07999999999999996], [8.92, -1.0]]),
            ('B_cell1_-1_hatch1_9', [[9.0, -0.84], [8.16, 0.0]]),
            ('B_cell1_-1_hatch1_10', [[9.0, -0.6], [8.4, 0.0]]),
            ('B_cell1_-1_hatch1_11', [[9.0, -0.36], [8.64, 0.0]]),
            ('B_cell1_-1_hatch1_12', [[9.0, -0.12], [8.88, 0.0]]),
            ('B_cell1_-1_hatch-1_1', [[9.0, -0.76], [8.76, -1.0]]),
            ('B_cell1_-1_hatch-1_2', [[9.0, -0.52], [8.52, -1.0]]),
            ('B_cell1_-1_hatch-1_3', [[9.0, -0.28], [8.28, -1.0]]),
            ('B_cell1_-1_hatch-1_4', [[9.0, -0.040000000000000036], [8.04, -1.0]]),
            ('B_cell1_-1_hatch-1_5', [[8.0, -0.8], [8.8, 0.0]]),
            ('B_cell1_-1_hatch-1_6', [[8.0, -0.56], [8.56, 0.0]]),
            ('B_cell1_-1_hatch-1_7', [[8.0, -0.31999999999999995], [8.32, 0.0]]),
            ('B_cell1_-1_hatch-1_8', [[8.0, -0.07999999999999996], [8.08, 0.0]]),
            ('B_netedge0', [[7.0, 0.0], [7.0, 1.0]]), ('B_netedge1', [[7.0, 0.0], [8.0, 0.0]]),
            ('B_netedge2', [[7.0, 1.0], [8.0, 1.0]]), ('B_netedge3', [[8.0, -1.0], [8.0, 0.0]]),
            ('B_netedge4', [[8.0, -1.0], [9.0, -1.0]]), ('B_netedge5', [[8.0, 0.0], [8.0, 1.0]]),
            ('B_netedge6', [[8.0, 0.0], [9.0, 0.0]]), ('B_netedge7', [[8.0, 1.0], [8.0, 2.0]]),
            ('B_netedge8', [[8.0, 1.0], [9.0, 1.0]]), ('B_netedge9', [[8.0, 2.0], [9.0, 2.0]]),
            ('B_netedge10', [[9.0, -1.0], [9.0, 0.0]]), ('B_netedge11', [[9.0, 0.0], [9.0, 1.0]]),
            ('B_netedge12', [[9.0, 0.0], [10.0, 0.0]]), ('B_netedge13', [[9.0, 1.0], [9.0, 2.0]]),
            ('B_netedge14', [[9.0, 1.0], [10.0, 1.0]]), ('B_netedge15', [[10.0, 0.0], [10.0, 1.0]]),
            ('B_netedge16', [[10.0, 0.0], [11.0, 0.0]]), ('B_netedge17', [[10.0, 1.0], [11.0, 1.0]]),
            ('B_netedge18', [[11.0, 0.0], [11.0, 1.0]])
        ]
        self._geometry_02 = [
            ('C_cell3_-1_hatch1_5', [[17.0, -0.8], [17.2, -1.0]]),
            ('C_cell3_-1_hatch1_6', [[17.0, -0.56], [17.44, -1.0]]),
            ('C_cell3_-1_hatch1_7', [[17.0, -0.31999999999999995], [17.68, -1.0]]),
            ('C_cell3_-1_hatch1_8', [[17.0, -0.07999999999999996], [17.92, -1.0]]),
            ('C_cell3_-1_hatch1_9', [[18.0, -0.84], [17.16, 0.0]]),
            ('C_cell3_-1_hatch1_10', [[18.0, -0.6], [17.4, 0.0]]),
            ('C_cell3_-1_hatch1_11', [[18.0, -0.36], [17.64, 0.0]]),
            ('C_cell3_-1_hatch1_12', [[18.0, -0.12], [17.88, 0.0]]),
            ('C_cell3_-1_hatch-1_1', [[18.0, -0.76], [17.76, -1.0]]),
            ('C_cell3_-1_hatch-1_2', [[18.0, -0.52], [17.52, -1.0]]),
            ('C_cell3_-1_hatch-1_3', [[18.0, -0.28], [17.28, -1.0]]),
            ('C_cell3_-1_hatch-1_4', [[18.0, -0.040000000000000036], [17.04, -1.0]]),
            ('C_cell3_-1_hatch-1_5', [[17.0, -0.8], [17.8, 0.0]]),
            ('C_cell3_-1_hatch-1_6', [[17.0, -0.56], [17.56, 0.0]]),
            ('C_cell3_-1_hatch-1_7', [[17.0, -0.31999999999999995], [17.32, 0.0]]),
            ('C_cell3_-1_hatch-1_8', [[17.0, -0.07999999999999996], [17.08, 0.0]]),
            ('C_netedge0', [[14.0, 0.0], [14.0, 1.0]]), ('C_netedge1', [[14.0, 0.0], [15.0, 0.0]]),
            ('C_netedge2', [[14.0, 1.0], [15.0, 1.0]]), ('C_netedge3', [[15.0, 0.0], [15.0, 1.0]]),
            ('C_netedge4', [[15.0, 0.0], [16.0, 0.0]]), ('C_netedge5', [[15.0, 1.0], [16.0, 1.0]]),
            ('C_netedge6', [[16.0, 0.0], [16.0, 1.0]]), ('C_netedge7', [[16.0, 0.0], [17.0, 0.0]]),
            ('C_netedge8', [[16.0, 1.0], [17.0, 1.0]]), ('C_netedge9', [[17.0, -1.0], [17.0, 0.0]]),
            ('C_netedge10', [[17.0, -1.0], [18.0, -1.0]]), ('C_netedge11', [[17.0, 0.0], [17.0, 1.0]]),
            ('C_netedge12', [[17.0, 0.0], [18.0, 0.0]]), ('C_netedge13', [[17.0, 1.0], [17.0, 2.0]]),
            ('C_netedge14', [[17.0, 1.0], [18.0, 1.0]]), ('C_netedge15', [[17.0, 2.0], [18.0, 2.0]]),
            ('C_netedge16', [[18.0, -1.0], [18.0, 0.0]]), ('C_netedge17', [[18.0, 0.0], [18.0, 1.0]]),
            ('C_netedge18', [[18.0, 1.0], [18.0, 2.0]])
        ]

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        c.path([[15.0, 6.0], [17.0, 6.0], [17.0, 8.0], [15.0, 8.0], [15.0, 6.0]], [1, 2, 2, 2, 79], id='givenfront_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('givenfront_hatch1_5', [[15.0, 6.4], [15.4, 6.0]]), ('givenfront_hatch1_6', [[15.0, 6.88], [15.88, 6.0]]), ('givenfront_hatch1_7', [[15.0, 7.36], [16.36, 6.0]]), ('givenfront_hatch1_8', [[15.0, 7.84], [16.84, 6.0]]), ('givenfront_hatch1_9', [[17.0, 6.32], [15.32, 8.0]]), ('givenfront_hatch1_10', [[17.0, 6.8], [15.8, 8.0]]), ('givenfront_hatch1_11', [[17.0, 7.28], [16.28, 8.0]]), ('givenfront_hatch1_12', [[17.0, 7.76], [16.76, 8.0]]), ('givenfront_hatch-1_1', [[17.0, 6.48], [16.52, 6.0]]), ('givenfront_hatch-1_2', [[17.0, 6.96], [16.04, 6.0]]), ('givenfront_hatch-1_3', [[17.0, 7.4399999999999995], [15.56, 6.0]]), ('givenfront_hatch-1_4', [[17.0, 7.92], [15.08, 6.0]]), ('givenfront_hatch-1_5', [[15.0, 6.4], [16.6, 8.0]]), ('givenfront_hatch-1_6', [[15.0, 6.88], [16.12, 8.0]]), ('givenfront_hatch-1_7', [[15.0, 7.36], [15.64, 8.0]]), ('givenfront_hatch-1_8', [[15.0, 7.84], [15.16, 8.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[15.0, 8.0], [17.0, 8.0], [17.7, 8.7], [15.7, 8.7], [15.0, 8.0]], [1, 2, 2, 2, 79], id='giventop_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[17.0, 6.0], [17.7, 6.7], [17.7, 8.7], [17.0, 8.0], [17.0, 6.0]], [1, 2, 2, 2, 79], id='givenright_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        _ov = {j: s for idxs, s in _hi.get(4, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('givenedge0', [[15.0, 6.0], [15.0, 8.0]]), ('givenedge1', [[15.0, 6.0], [17.0, 6.0]]), ('givenedge2', [[15.0, 8.0], [15.7, 8.7]]), ('givenedge3', [[15.0, 8.0], [17.0, 8.0]]), ('givenedge4', [[15.7, 8.7], [17.7, 8.7]]), ('givenedge5', [[17.0, 6.0], [17.0, 8.0]]), ('givenedge6', [[17.0, 6.0], [17.7, 6.7]]), ('givenedge7', [[17.0, 8.0], [17.7, 8.7]]), ('givenedge8', [[17.7, 6.7], [17.7, 8.7]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell0_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell1_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell2_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell3_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('A_cell3_0_hatch1_5', [[3.0, 0.2], [3.2, 0.0]]), ('A_cell3_0_hatch1_6', [[3.0, 0.44], [3.44, 0.0]]), ('A_cell3_0_hatch1_7', [[3.0, 0.68], [3.68, 0.0]]), ('A_cell3_0_hatch1_8', [[3.0, 0.92], [3.92, 0.0]]), ('A_cell3_0_hatch1_9', [[4.0, 0.16], [3.16, 1.0]]), ('A_cell3_0_hatch1_10', [[4.0, 0.4], [3.4, 1.0]]), ('A_cell3_0_hatch1_11', [[4.0, 0.64], [3.64, 1.0]]), ('A_cell3_0_hatch1_12', [[4.0, 0.88], [3.88, 1.0]]), ('A_cell3_0_hatch-1_1', [[4.0, 0.24], [3.76, 0.0]]), ('A_cell3_0_hatch-1_2', [[4.0, 0.48], [3.52, 0.0]]), ('A_cell3_0_hatch-1_3', [[4.0, 0.72], [3.2800000000000002, 0.0]]), ('A_cell3_0_hatch-1_4', [[4.0, 0.96], [3.04, 0.0]]), ('A_cell3_0_hatch-1_5', [[3.0, 0.2], [3.8, 1.0]]), ('A_cell3_0_hatch-1_6', [[3.0, 0.44], [3.56, 1.0]]), ('A_cell3_0_hatch-1_7', [[3.0, 0.68], [3.32, 1.0]]), ('A_cell3_0_hatch-1_8', [[3.0, 0.92], [3.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='A_cell1_1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('A_cell1_1_hatch1_5', [[1.0, 1.2], [1.2, 1.0]]), ('A_cell1_1_hatch1_6', [[1.0, 1.44], [1.44, 1.0]]), ('A_cell1_1_hatch1_7', [[1.0, 1.6800000000000002], [1.6800000000000002, 1.0]]), ('A_cell1_1_hatch1_8', [[1.0, 1.92], [1.92, 1.0]]), ('A_cell1_1_hatch1_9', [[2.0, 1.16], [1.16, 2.0]]), ('A_cell1_1_hatch1_10', [[2.0, 1.4], [1.4, 2.0]]), ('A_cell1_1_hatch1_11', [[2.0, 1.6400000000000001], [1.6400000000000001, 2.0]]), ('A_cell1_1_hatch1_12', [[2.0, 1.88], [1.88, 2.0]]), ('A_cell1_1_hatch-1_1', [[2.0, 1.24], [1.76, 1.0]]), ('A_cell1_1_hatch-1_2', [[2.0, 1.48], [1.52, 1.0]]), ('A_cell1_1_hatch-1_3', [[2.0, 1.72], [1.28, 1.0]]), ('A_cell1_1_hatch-1_4', [[2.0, 1.96], [1.04, 1.0]]), ('A_cell1_1_hatch-1_5', [[1.0, 1.2], [1.8, 2.0]]), ('A_cell1_1_hatch-1_6', [[1.0, 1.44], [1.56, 2.0]]), ('A_cell1_1_hatch-1_7', [[1.0, 1.6800000000000002], [1.32, 2.0]]), ('A_cell1_1_hatch-1_8', [[1.0, 1.92], [1.08, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[2.0, -1.0], [3.0, -1.0], [3.0, 0.0], [2.0, 0.0], [2.0, -1.0]], [1, 2, 2, 2, 79], id='A_cell2_-1_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        for object_id, points in [('A_netedge0', [[0.0, 0.0], [0.0, 1.0]]), ('A_netedge1', [[0.0, 0.0], [1.0, 0.0]]), ('A_netedge2', [[0.0, 1.0], [1.0, 1.0]]), ('A_netedge3', [[1.0, 0.0], [1.0, 1.0]]), ('A_netedge4', [[1.0, 0.0], [2.0, 0.0]]), ('A_netedge5', [[1.0, 1.0], [1.0, 2.0]]), ('A_netedge6', [[1.0, 1.0], [2.0, 1.0]]), ('A_netedge7', [[1.0, 2.0], [2.0, 2.0]]), ('A_netedge8', [[2.0, -1.0], [2.0, 0.0]]), ('A_netedge9', [[2.0, -1.0], [3.0, -1.0]]), ('A_netedge10', [[2.0, 0.0], [2.0, 1.0]]), ('A_netedge11', [[2.0, 0.0], [3.0, 0.0]]), ('A_netedge12', [[2.0, 1.0], [2.0, 2.0]]), ('A_netedge13', [[2.0, 1.0], [3.0, 1.0]]), ('A_netedge14', [[3.0, -1.0], [3.0, 0.0]]), ('A_netedge15', [[3.0, 0.0], [3.0, 1.0]]), ('A_netedge16', [[3.0, 0.0], [4.0, 0.0]]), ('A_netedge17', [[3.0, 1.0], [4.0, 1.0]]), ('A_netedge18', [[4.0, 0.0], [4.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell0_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell1_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell2_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('B_cell2_0_hatch1_5', [[9.0, 0.2], [9.2, 0.0]]), ('B_cell2_0_hatch1_6', [[9.0, 0.44], [9.44, 0.0]]), ('B_cell2_0_hatch1_7', [[9.0, 0.68], [9.68, 0.0]]), ('B_cell2_0_hatch1_8', [[9.0, 0.92], [9.92, 0.0]]), ('B_cell2_0_hatch1_9', [[10.0, 0.16], [9.16, 1.0]]), ('B_cell2_0_hatch1_10', [[10.0, 0.4], [9.4, 1.0]]), ('B_cell2_0_hatch1_11', [[10.0, 0.64], [9.64, 1.0]]), ('B_cell2_0_hatch1_12', [[10.0, 0.88], [9.88, 1.0]]), ('B_cell2_0_hatch-1_1', [[10.0, 0.24], [9.76, 0.0]]), ('B_cell2_0_hatch-1_2', [[10.0, 0.48], [9.52, 0.0]]), ('B_cell2_0_hatch-1_3', [[10.0, 0.72], [9.28, 0.0]]), ('B_cell2_0_hatch-1_4', [[10.0, 0.96], [9.04, 0.0]]), ('B_cell2_0_hatch-1_5', [[9.0, 0.2], [9.8, 1.0]]), ('B_cell2_0_hatch-1_6', [[9.0, 0.44], [9.56, 1.0]]), ('B_cell2_0_hatch-1_7', [[9.0, 0.68], [9.32, 1.0]]), ('B_cell2_0_hatch-1_8', [[9.0, 0.92], [9.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell3_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='B_cell1_1_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[8.0, -1.0], [9.0, -1.0], [9.0, 0.0], [8.0, 0.0], [8.0, -1.0]], [1, 2, 2, 2, 79], id='B_cell1_-1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in self._geometry_01:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [14.0, 1.0], [14.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell0_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell1_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell2_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('C_cell2_0_hatch1_5', [[16.0, 0.2], [16.2, 0.0]]), ('C_cell2_0_hatch1_6', [[16.0, 0.44], [16.44, 0.0]]), ('C_cell2_0_hatch1_7', [[16.0, 0.68], [16.68, 0.0]]), ('C_cell2_0_hatch1_8', [[16.0, 0.92], [16.92, 0.0]]), ('C_cell2_0_hatch1_9', [[17.0, 0.16], [16.16, 1.0]]), ('C_cell2_0_hatch1_10', [[17.0, 0.4], [16.4, 1.0]]), ('C_cell2_0_hatch1_11', [[17.0, 0.64], [16.64, 1.0]]), ('C_cell2_0_hatch1_12', [[17.0, 0.88], [16.88, 1.0]]), ('C_cell2_0_hatch-1_1', [[17.0, 0.24], [16.76, 0.0]]), ('C_cell2_0_hatch-1_2', [[17.0, 0.48], [16.52, 0.0]]), ('C_cell2_0_hatch-1_3', [[17.0, 0.72], [16.28, 0.0]]), ('C_cell2_0_hatch-1_4', [[17.0, 0.96], [16.04, 0.0]]), ('C_cell2_0_hatch-1_5', [[16.0, 0.2], [16.8, 1.0]]), ('C_cell2_0_hatch-1_6', [[16.0, 0.44], [16.56, 1.0]]), ('C_cell2_0_hatch-1_7', [[16.0, 0.68], [16.32, 1.0]]), ('C_cell2_0_hatch-1_8', [[16.0, 0.92], [16.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell3_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='C_cell3_1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[17.0, -1.0], [18.0, -1.0], [18.0, 0.0], [17.0, 0.0], [17.0, -1.0]], [1, 2, 2, 2, 79], id='C_cell3_-1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        _ov = {j: s for idxs, s in _hi.get(29, ()) for j in idxs}
        for i, (object_id, points) in enumerate(self._geometry_02):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell0_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('D_cell0_0_hatch1_5', [[21.0, 0.2], [21.2, 0.0]]), ('D_cell0_0_hatch1_6', [[21.0, 0.44], [21.44, 0.0]]), ('D_cell0_0_hatch1_7', [[21.0, 0.68], [21.68, 0.0]]), ('D_cell0_0_hatch1_8', [[21.0, 0.92], [21.92, 0.0]]), ('D_cell0_0_hatch1_9', [[22.0, 0.16], [21.16, 1.0]]), ('D_cell0_0_hatch1_10', [[22.0, 0.4], [21.4, 1.0]]), ('D_cell0_0_hatch1_11', [[22.0, 0.64], [21.64, 1.0]]), ('D_cell0_0_hatch1_12', [[22.0, 0.88], [21.88, 1.0]]), ('D_cell0_0_hatch-1_1', [[22.0, 0.24], [21.76, 0.0]]), ('D_cell0_0_hatch-1_2', [[22.0, 0.48], [21.52, 0.0]]), ('D_cell0_0_hatch-1_3', [[22.0, 0.72], [21.28, 0.0]]), ('D_cell0_0_hatch-1_4', [[22.0, 0.96], [21.04, 0.0]]), ('D_cell0_0_hatch-1_5', [[21.0, 0.2], [21.8, 1.0]]), ('D_cell0_0_hatch-1_6', [[21.0, 0.44], [21.56, 1.0]]), ('D_cell0_0_hatch-1_7', [[21.0, 0.68], [21.32, 1.0]]), ('D_cell0_0_hatch-1_8', [[21.0, 0.92], [21.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [22.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell1_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[23.0, 0.0], [24.0, 0.0], [24.0, 1.0], [23.0, 1.0], [23.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell2_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('D_cell2_0_hatch1_5', [[23.0, 0.2], [23.2, 0.0]]), ('D_cell2_0_hatch1_6', [[23.0, 0.44], [23.44, 0.0]]), ('D_cell2_0_hatch1_7', [[23.0, 0.68], [23.68, 0.0]]), ('D_cell2_0_hatch1_8', [[23.0, 0.92], [23.92, 0.0]]), ('D_cell2_0_hatch1_9', [[24.0, 0.16], [23.16, 1.0]]), ('D_cell2_0_hatch1_10', [[24.0, 0.4], [23.4, 1.0]]), ('D_cell2_0_hatch1_11', [[24.0, 0.64], [23.64, 1.0]]), ('D_cell2_0_hatch1_12', [[24.0, 0.88], [23.88, 1.0]]), ('D_cell2_0_hatch-1_1', [[24.0, 0.24], [23.76, 0.0]]), ('D_cell2_0_hatch-1_2', [[24.0, 0.48], [23.52, 0.0]]), ('D_cell2_0_hatch-1_3', [[24.0, 0.72], [23.28, 0.0]]), ('D_cell2_0_hatch-1_4', [[24.0, 0.96], [23.04, 0.0]]), ('D_cell2_0_hatch-1_5', [[23.0, 0.2], [23.8, 1.0]]), ('D_cell2_0_hatch-1_6', [[23.0, 0.44], [23.56, 1.0]]), ('D_cell2_0_hatch-1_7', [[23.0, 0.68], [23.32, 1.0]]), ('D_cell2_0_hatch-1_8', [[23.0, 0.92], [23.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[24.0, 0.0], [25.0, 0.0], [25.0, 1.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell3_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[24.0, 1.0], [25.0, 1.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 79], id='D_cell3_1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[22.0, -1.0], [23.0, -1.0], [23.0, 0.0], [22.0, 0.0], [22.0, -1.0]], [1, 2, 2, 2, 79], id='D_cell1_-1_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        for object_id, points in [('D_netedge0', [[21.0, 0.0], [21.0, 1.0]]), ('D_netedge1', [[21.0, 0.0], [22.0, 0.0]]), ('D_netedge2', [[21.0, 1.0], [22.0, 1.0]]), ('D_netedge3', [[22.0, -1.0], [22.0, 0.0]]), ('D_netedge4', [[22.0, -1.0], [23.0, -1.0]]), ('D_netedge5', [[22.0, 0.0], [22.0, 1.0]]), ('D_netedge6', [[22.0, 0.0], [23.0, 0.0]]), ('D_netedge7', [[22.0, 1.0], [23.0, 1.0]]), ('D_netedge8', [[23.0, -1.0], [23.0, 0.0]]), ('D_netedge9', [[23.0, 0.0], [23.0, 1.0]]), ('D_netedge10', [[23.0, 0.0], [24.0, 0.0]]), ('D_netedge11', [[23.0, 1.0], [24.0, 1.0]]), ('D_netedge12', [[24.0, 0.0], [24.0, 1.0]]), ('D_netedge13', [[24.0, 0.0], [25.0, 0.0]]), ('D_netedge14', [[24.0, 1.0], [24.0, 2.0]]), ('D_netedge15', [[24.0, 1.0], [25.0, 1.0]]), ('D_netedge16', [[24.0, 2.0], [25.0, 2.0]]), ('D_netedge17', [[25.0, 0.0], [25.0, 1.0]]), ('D_netedge18', [[25.0, 1.0], [25.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[28.0, 0.0], [29.0, 0.0], [29.0, 1.0], [28.0, 1.0], [28.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell0_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[29.0, 0.0], [30.0, 0.0], [30.0, 1.0], [29.0, 1.0], [29.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell1_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('E_cell1_0_hatch1_5', [[29.0, 0.2], [29.2, 0.0]]), ('E_cell1_0_hatch1_6', [[29.0, 0.44], [29.44, 0.0]]), ('E_cell1_0_hatch1_7', [[29.0, 0.68], [29.68, 0.0]]), ('E_cell1_0_hatch1_8', [[29.0, 0.92], [29.92, 0.0]]), ('E_cell1_0_hatch1_9', [[30.0, 0.16], [29.16, 1.0]]), ('E_cell1_0_hatch1_10', [[30.0, 0.4], [29.4, 1.0]]), ('E_cell1_0_hatch1_11', [[30.0, 0.64], [29.64, 1.0]]), ('E_cell1_0_hatch1_12', [[30.0, 0.88], [29.88, 1.0]]), ('E_cell1_0_hatch-1_1', [[30.0, 0.24], [29.76, 0.0]]), ('E_cell1_0_hatch-1_2', [[30.0, 0.48], [29.52, 0.0]]), ('E_cell1_0_hatch-1_3', [[30.0, 0.72], [29.28, 0.0]]), ('E_cell1_0_hatch-1_4', [[30.0, 0.96], [29.04, 0.0]]), ('E_cell1_0_hatch-1_5', [[29.0, 0.2], [29.8, 1.0]]), ('E_cell1_0_hatch-1_6', [[29.0, 0.44], [29.56, 1.0]]), ('E_cell1_0_hatch-1_7', [[29.0, 0.68], [29.32, 1.0]]), ('E_cell1_0_hatch-1_8', [[29.0, 0.92], [29.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell2_0_fill', zorder=1, edgecolor='none', facecolor='#CCCCCC', linewidth=0.0, capstyle='butt')
        c.path([[31.0, 0.0], [32.0, 0.0], [32.0, 1.0], [31.0, 1.0], [31.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell3_0_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('E_cell3_0_hatch1_5', [[31.0, 0.2], [31.2, 0.0]]), ('E_cell3_0_hatch1_6', [[31.0, 0.44], [31.44, 0.0]]), ('E_cell3_0_hatch1_7', [[31.0, 0.68], [31.68, 0.0]]), ('E_cell3_0_hatch1_8', [[31.0, 0.92], [31.92, 0.0]]), ('E_cell3_0_hatch1_9', [[32.0, 0.16], [31.16, 1.0]]), ('E_cell3_0_hatch1_10', [[32.0, 0.4], [31.4, 1.0]]), ('E_cell3_0_hatch1_11', [[32.0, 0.64], [31.64, 1.0]]), ('E_cell3_0_hatch1_12', [[32.0, 0.88], [31.88, 1.0]]), ('E_cell3_0_hatch-1_1', [[32.0, 0.24], [31.76, 0.0]]), ('E_cell3_0_hatch-1_2', [[32.0, 0.48], [31.52, 0.0]]), ('E_cell3_0_hatch-1_3', [[32.0, 0.72], [31.28, 0.0]]), ('E_cell3_0_hatch-1_4', [[32.0, 0.96], [31.04, 0.0]]), ('E_cell3_0_hatch-1_5', [[31.0, 0.2], [31.8, 1.0]]), ('E_cell3_0_hatch-1_6', [[31.0, 0.44], [31.56, 1.0]]), ('E_cell3_0_hatch-1_7', [[31.0, 0.68], [31.32, 1.0]]), ('E_cell3_0_hatch-1_8', [[31.0, 0.92], [31.08, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[29.0, 1.0], [30.0, 1.0], [30.0, 2.0], [29.0, 2.0], [29.0, 1.0]], [1, 2, 2, 2, 79], id='E_cell1_1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[31.0, -1.0], [32.0, -1.0], [32.0, 0.0], [31.0, 0.0], [31.0, -1.0]], [1, 2, 2, 2, 79], id='E_cell3_-1_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        for object_id, points in [('E_netedge0', [[28.0, 0.0], [28.0, 1.0]]), ('E_netedge1', [[28.0, 0.0], [29.0, 0.0]]), ('E_netedge2', [[28.0, 1.0], [29.0, 1.0]]), ('E_netedge3', [[29.0, 0.0], [29.0, 1.0]]), ('E_netedge4', [[29.0, 0.0], [30.0, 0.0]]), ('E_netedge5', [[29.0, 1.0], [29.0, 2.0]]), ('E_netedge6', [[29.0, 1.0], [30.0, 1.0]]), ('E_netedge7', [[29.0, 2.0], [30.0, 2.0]]), ('E_netedge8', [[30.0, 0.0], [30.0, 1.0]]), ('E_netedge9', [[30.0, 0.0], [31.0, 0.0]]), ('E_netedge10', [[30.0, 1.0], [30.0, 2.0]]), ('E_netedge11', [[30.0, 1.0], [31.0, 1.0]]), ('E_netedge12', [[31.0, -1.0], [31.0, 0.0]]), ('E_netedge13', [[31.0, -1.0], [32.0, -1.0]]), ('E_netedge14', [[31.0, 0.0], [31.0, 1.0]]), ('E_netedge15', [[31.0, 0.0], [32.0, 0.0]]), ('E_netedge16', [[31.0, 1.0], [32.0, 1.0]]), ('E_netedge17', [[32.0, -1.0], [32.0, 0.0]]), ('E_netedge18', [[32.0, 0.0], [32.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        for object_id, text, anchor in [('label0', 'A', (-1.0, 0.5)), ('label1', 'B', (6.0, 0.5)), ('label2', 'C', (13.0, 0.5)), ('label3', 'D', (20.0, 0.5)), ('label4', 'E', (27.0, 0.5))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-2.1790738420292772, 32.868123484180295), ylim=(-13.701984079771453, 21.345213246438117)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid111_C01.png'
        with Canvas(SOLID, xlim=(-2.1790738420292772, 32.868123484180295), ylim=(-13.701984079771453, 21.345213246438117)) as c:
            self._draw_base(c, hi={4: [({3}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({5}, {'color': '#16A34A', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({7}, {'color': '#2563EB', 'linewidth': 1.5, 'solid_capstyle': 'butt'})], 29: [({24}, {'color': '#DC2626', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({27}, {'color': '#16A34A', 'linewidth': 1.5, 'solid_capstyle': 'butt'}), ({30}, {'color': '#2563EB', 'linewidth': 1.5, 'solid_capstyle': 'butt'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid111')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid111().draw(args.output, variant=args.variant))
