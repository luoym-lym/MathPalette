"""Collected question Plane388; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane388:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def _draw_base(self, c, kw=None):
        _kw = kw or {}
        c.path([[8.0, 7.0], [9.0, 7.0], [9.0, 8.0], [8.0, 8.0], [8.0, 7.0]], [1, 2, 2, 2, 79], id='board0', capstyle='butt')
        c.path([[8.0, 8.0], [9.0, 8.0], [9.0, 9.0], [8.0, 9.0], [8.0, 8.0]], [1, 2, 2, 2, 79], id='board1', capstyle='butt')
        c.path([[8.0, 9.0], [9.0, 9.0], [9.0, 10.0], [8.0, 10.0], [8.0, 9.0]], [1, 2, 2, 2, 79], id='board2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[8.0, 9.0], [9.0, 9.0], [9.0, 10.0], [8.0, 10.0], [8.0, 9.0]], [1, 2, 2, 2, 79], id='board2', capstyle='butt', fill=False)
        c.path([[8.0, 10.0], [9.0, 10.0], [9.0, 11.0], [8.0, 11.0], [8.0, 10.0]], [1, 2, 2, 2, 79], id='board3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[8.0, 10.0], [9.0, 10.0], [9.0, 11.0], [8.0, 11.0], [8.0, 10.0]], [1, 2, 2, 2, 79], id='board3', capstyle='butt', fill=False)
        c.path([[8.0, 11.0], [9.0, 11.0], [9.0, 12.0], [8.0, 12.0], [8.0, 11.0]], [1, 2, 2, 2, 79], id='board4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[8.0, 11.0], [9.0, 11.0], [9.0, 12.0], [8.0, 12.0], [8.0, 11.0]], [1, 2, 2, 2, 79], id='board4', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('board5', [[9.0, 7.0], [10.0, 7.0], [10.0, 8.0], [9.0, 8.0], [9.0, 7.0]], [1, 2, 2, 2, 79]), ('board6', [[9.0, 8.0], [10.0, 8.0], [10.0, 9.0], [9.0, 9.0], [9.0, 8.0]], [1, 2, 2, 2, 79]), ('board7', [[9.0, 9.0], [10.0, 9.0], [10.0, 10.0], [9.0, 10.0], [9.0, 9.0]], [1, 2, 2, 2, 79]), ('board8', [[9.0, 10.0], [10.0, 10.0], [10.0, 11.0], [9.0, 11.0], [9.0, 10.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[9.0, 11.0], [10.0, 11.0], [10.0, 12.0], [9.0, 12.0], [9.0, 11.0]], [1, 2, 2, 2, 79], id='board9', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[9.0, 11.0], [10.0, 11.0], [10.0, 12.0], [9.0, 12.0], [9.0, 11.0]], [1, 2, 2, 2, 79], id='board9', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('board10', [[10.0, 7.0], [11.0, 7.0], [11.0, 8.0], [10.0, 8.0], [10.0, 7.0]], [1, 2, 2, 2, 79]), ('board11', [[10.0, 8.0], [11.0, 8.0], [11.0, 9.0], [10.0, 9.0], [10.0, 8.0]], [1, 2, 2, 2, 79]), ('board12', [[10.0, 9.0], [11.0, 9.0], [11.0, 10.0], [10.0, 10.0], [10.0, 9.0]], [1, 2, 2, 2, 79]), ('board13', [[10.0, 10.0], [11.0, 10.0], [11.0, 11.0], [10.0, 11.0], [10.0, 10.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[10.0, 11.0], [11.0, 11.0], [11.0, 12.0], [10.0, 12.0], [10.0, 11.0]], [1, 2, 2, 2, 79], id='board14', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 11.0], [11.0, 11.0], [11.0, 12.0], [10.0, 12.0], [10.0, 11.0]], [1, 2, 2, 2, 79], id='board14', capstyle='butt', fill=False)
        c.path([[11.0, 7.0], [12.0, 7.0], [12.0, 8.0], [11.0, 8.0], [11.0, 7.0]], [1, 2, 2, 2, 79], id='board15', capstyle='butt')
        c.path([[11.0, 8.0], [12.0, 8.0], [12.0, 9.0], [11.0, 9.0], [11.0, 8.0]], [1, 2, 2, 2, 79], id='board16', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[11.0, 8.0], [12.0, 8.0], [12.0, 9.0], [11.0, 9.0], [11.0, 8.0]], [1, 2, 2, 2, 79], id='board16', capstyle='butt', fill=False)
        for object_id, vertices, codes in [('board17', [[11.0, 9.0], [12.0, 9.0], [12.0, 10.0], [11.0, 10.0], [11.0, 9.0]], [1, 2, 2, 2, 79]), ('board18', [[11.0, 10.0], [12.0, 10.0], [12.0, 11.0], [11.0, 11.0], [11.0, 10.0]], [1, 2, 2, 2, 79]), ('board19', [[11.0, 11.0], [12.0, 11.0], [12.0, 12.0], [11.0, 12.0], [11.0, 11.0]], [1, 2, 2, 2, 79]), ('board20', [[12.0, 7.0], [13.0, 7.0], [13.0, 8.0], [12.0, 8.0], [12.0, 7.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[12.0, 8.0], [13.0, 8.0], [13.0, 9.0], [12.0, 9.0], [12.0, 8.0]], [1, 2, 2, 2, 79], id='board21', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[12.0, 8.0], [13.0, 8.0], [13.0, 9.0], [12.0, 9.0], [12.0, 8.0]], [1, 2, 2, 2, 79], id='board21', capstyle='butt', fill=False)
        c.path([[12.0, 9.0], [13.0, 9.0], [13.0, 10.0], [12.0, 10.0], [12.0, 9.0]], [1, 2, 2, 2, 79], id='board22', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[12.0, 9.0], [13.0, 9.0], [13.0, 10.0], [12.0, 10.0], [12.0, 9.0]], [1, 2, 2, 2, 79], id='board22', capstyle='butt', fill=False)
        c.path([[12.0, 10.0], [13.0, 10.0], [13.0, 11.0], [12.0, 11.0], [12.0, 10.0]], [1, 2, 2, 2, 79], id='board23', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[12.0, 10.0], [13.0, 10.0], [13.0, 11.0], [12.0, 11.0], [12.0, 10.0]], [1, 2, 2, 2, 79], id='board23', capstyle='butt', fill=False)
        c.path([[12.0, 11.0], [13.0, 11.0], [13.0, 12.0], [12.0, 12.0], [12.0, 11.0]], [1, 2, 2, 2, 79], id='board24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[12.0, 11.0], [13.0, 11.0], [13.0, 12.0], [12.0, 12.0], [12.0, 11.0]], [1, 2, 2, 2, 79], id='board24', capstyle='butt', fill=False)
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='opt00', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='opt00', capstyle='butt', fill=False)
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='opt01', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='opt01', capstyle='butt', fill=False, **_kw.get(29, {}))
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='opt02', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='opt02', capstyle='butt', fill=False, **_kw.get(31, {}))
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='opt03', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='opt03', capstyle='butt', fill=False)
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='opt04', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='opt04', capstyle='butt', fill=False, **_kw.get(35, {}))
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='opt10', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='opt10', capstyle='butt', fill=False, **_kw.get(37, {}))
        c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='opt11', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='opt11', capstyle='butt', fill=False, **_kw.get(39, {}))
        c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='opt12', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='opt12', capstyle='butt', fill=False, **_kw.get(41, {}))
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='opt13', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='opt13', capstyle='butt', fill=False, **_kw.get(43, {}))
        c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='opt14', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='opt14', capstyle='butt', fill=False, **_kw.get(45, {}))
        c.path([[10.0, 4.0], [11.0, 4.0], [11.0, 5.0], [10.0, 5.0], [10.0, 4.0]], [1, 2, 2, 2, 79], id='opt20', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 4.0], [11.0, 4.0], [11.0, 5.0], [10.0, 5.0], [10.0, 4.0]], [1, 2, 2, 2, 79], id='opt20', capstyle='butt', fill=False)
        c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='opt21', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='opt21', capstyle='butt', fill=False)
        c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='opt22', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='opt22', capstyle='butt', fill=False)
        c.path([[10.0, 3.0], [11.0, 3.0], [11.0, 4.0], [10.0, 4.0], [10.0, 3.0]], [1, 2, 2, 2, 79], id='opt23', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 3.0], [11.0, 3.0], [11.0, 4.0], [10.0, 4.0], [10.0, 3.0]], [1, 2, 2, 2, 79], id='opt23', capstyle='butt', fill=False)
        c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='opt24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='opt24', capstyle='butt', fill=False)
        c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='opt30', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='opt30', capstyle='butt', fill=False)
        c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='opt31', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='opt31', capstyle='butt', fill=False)
        c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='opt32', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='opt32', capstyle='butt', fill=False)
        c.path([[17.0, 2.0], [18.0, 2.0], [18.0, 3.0], [17.0, 3.0], [17.0, 2.0]], [1, 2, 2, 2, 79], id='opt33', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 2.0], [18.0, 2.0], [18.0, 3.0], [17.0, 3.0], [17.0, 2.0]], [1, 2, 2, 2, 79], id='opt33', capstyle='butt', fill=False)
        c.path([[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79], id='opt34', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79], id='opt34', capstyle='butt', fill=False)
        c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='opt40', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='opt40', capstyle='butt', fill=False, **_kw.get(67, {}))
        c.path([[20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0]], [1, 2, 2, 2, 79], id='opt41', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0]], [1, 2, 2, 2, 79], id='opt41', capstyle='butt', fill=False, **_kw.get(69, {}))
        c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='opt42', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='opt42', capstyle='butt', fill=False, **_kw.get(71, {}))
        c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='opt43', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='opt43', capstyle='butt', fill=False, **_kw.get(73, {}))
        c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='opt44', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='opt44', capstyle='butt', fill=False, **_kw.get(75, {}))
        for object_id, text, anchor in [('label0', 'A', (1.0, -0.8)), ('label1', 'B', (6.0, -0.8)), ('label2', 'C', (11.0, -0.8)), ('label3', 'D', (16.0, -0.8)), ('label4', 'E', (21.0, -0.8))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C01.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={29: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 31: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 35: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C02.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={37: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 39: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 41: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 43: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 45: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C03.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={37: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 41: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 45: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C04.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={67: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 69: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 71: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 73: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 75: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C05.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={67: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 71: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 75: {'edgecolor': '#2563EB', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane388_C06.png'
        with Canvas(PLANE, xlim=(-0.5452338455210093, 22.58186317522508), ylim=(-6.055045858745472, 17.072051162000616)) as c:
            self._draw_base(c, kw={67: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 69: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 73: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 75: {'edgecolor': '#EA580C', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane388')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane388().draw(args.output, variant=args.variant))
