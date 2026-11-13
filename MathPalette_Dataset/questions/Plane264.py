"""Collected question Plane264; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane264:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07')

    def __init__(self):
        self._geometry_01 = [
            ('board_0', [[9.0, 7.0], [9.0, 8.0]]), ('board_1', [[9.0, 7.0], [10.0, 7.0]]),
            ('board_2', [[9.0, 8.0], [9.0, 9.0]]), ('board_3', [[9.0, 8.0], [10.0, 8.0]]),
            ('board_4', [[9.0, 9.0], [9.0, 10.0]]), ('board_5', [[9.0, 9.0], [10.0, 9.0]]),
            ('board_6', [[9.0, 10.0], [9.0, 11.0]]), ('board_7', [[9.0, 10.0], [10.0, 10.0]]),
            ('board_8', [[9.0, 11.0], [9.0, 12.0]]), ('board_9', [[9.0, 11.0], [10.0, 11.0]]),
            ('board_10', [[9.0, 12.0], [10.0, 12.0]]), ('board_11', [[10.0, 7.0], [10.0, 8.0]]),
            ('board_12', [[10.0, 7.0], [11.0, 7.0]]), ('board_13', [[10.0, 8.0], [10.0, 9.0]]),
            ('board_14', [[10.0, 8.0], [11.0, 8.0]]), ('board_15', [[10.0, 9.0], [10.0, 10.0]]),
            ('board_16', [[10.0, 9.0], [11.0, 9.0]]), ('board_17', [[10.0, 10.0], [10.0, 11.0]]),
            ('board_18', [[10.0, 10.0], [11.0, 10.0]]), ('board_19', [[10.0, 11.0], [10.0, 12.0]]),
            ('board_20', [[10.0, 11.0], [11.0, 11.0]]), ('board_21', [[10.0, 12.0], [11.0, 12.0]]),
            ('board_22', [[11.0, 7.0], [11.0, 8.0]]), ('board_23', [[11.0, 7.0], [12.0, 7.0]]),
            ('board_24', [[11.0, 8.0], [11.0, 9.0]]), ('board_25', [[11.0, 8.0], [12.0, 8.0]]),
            ('board_26', [[11.0, 9.0], [11.0, 10.0]]), ('board_27', [[11.0, 9.0], [12.0, 9.0]]),
            ('board_28', [[11.0, 10.0], [11.0, 11.0]]), ('board_29', [[11.0, 10.0], [12.0, 10.0]]),
            ('board_30', [[11.0, 11.0], [11.0, 12.0]]), ('board_31', [[11.0, 11.0], [12.0, 11.0]]),
            ('board_32', [[11.0, 12.0], [12.0, 12.0]]), ('board_33', [[12.0, 7.0], [12.0, 8.0]]),
            ('board_34', [[12.0, 7.0], [13.0, 7.0]]), ('board_35', [[12.0, 8.0], [12.0, 9.0]]),
            ('board_36', [[12.0, 8.0], [13.0, 8.0]]), ('board_37', [[12.0, 9.0], [12.0, 10.0]]),
            ('board_38', [[12.0, 9.0], [13.0, 9.0]]), ('board_39', [[12.0, 10.0], [12.0, 11.0]]),
            ('board_40', [[12.0, 10.0], [13.0, 10.0]]), ('board_41', [[12.0, 11.0], [12.0, 12.0]]),
            ('board_42', [[12.0, 11.0], [13.0, 11.0]]), ('board_43', [[12.0, 12.0], [13.0, 12.0]]),
            ('board_44', [[13.0, 7.0], [13.0, 8.0]]), ('board_45', [[13.0, 7.0], [14.0, 7.0]]),
            ('board_46', [[13.0, 8.0], [13.0, 9.0]]), ('board_47', [[13.0, 8.0], [14.0, 8.0]]),
            ('board_48', [[13.0, 9.0], [13.0, 10.0]]), ('board_49', [[13.0, 9.0], [14.0, 9.0]]),
            ('board_50', [[13.0, 10.0], [13.0, 11.0]]), ('board_51', [[13.0, 10.0], [14.0, 10.0]]),
            ('board_52', [[13.0, 11.0], [13.0, 12.0]]), ('board_53', [[13.0, 11.0], [14.0, 11.0]]),
            ('board_54', [[13.0, 12.0], [14.0, 12.0]]), ('board_55', [[14.0, 7.0], [14.0, 8.0]]),
            ('board_56', [[14.0, 8.0], [14.0, 9.0]]), ('board_57', [[14.0, 9.0], [14.0, 10.0]]),
            ('board_58', [[14.0, 10.0], [14.0, 11.0]]), ('board_59', [[14.0, 11.0], [14.0, 12.0]])
        ]

    def _draw_base(self, c, kw=None):
        _kw = kw or {}
        c.path([[13.0, 11.0], [14.0, 11.0], [14.0, 12.0], [13.0, 12.0], [13.0, 11.0]], [1, 2, 2, 2, 79], id='given44', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[13.0, 11.0], [14.0, 11.0], [14.0, 12.0], [13.0, 12.0], [13.0, 11.0]], [1, 2, 2, 2, 79], id='given44', capstyle='butt', fill=False)
        c.path([[11.0, 11.0], [12.0, 11.0], [12.0, 12.0], [11.0, 12.0], [11.0, 11.0]], [1, 2, 2, 2, 79], id='given24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[11.0, 11.0], [12.0, 11.0], [12.0, 12.0], [11.0, 12.0], [11.0, 11.0]], [1, 2, 2, 2, 79], id='given24', capstyle='butt', fill=False)
        c.path([[9.0, 11.0], [10.0, 11.0], [10.0, 12.0], [9.0, 12.0], [9.0, 11.0]], [1, 2, 2, 2, 79], id='given04', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[9.0, 11.0], [10.0, 11.0], [10.0, 12.0], [9.0, 12.0], [9.0, 11.0]], [1, 2, 2, 2, 79], id='given04', capstyle='butt', fill=False)
        c.path([[13.0, 10.0], [14.0, 10.0], [14.0, 11.0], [13.0, 11.0], [13.0, 10.0]], [1, 2, 2, 2, 79], id='given43', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[13.0, 10.0], [14.0, 10.0], [14.0, 11.0], [13.0, 11.0], [13.0, 10.0]], [1, 2, 2, 2, 79], id='given43', capstyle='butt', fill=False)
        c.path([[12.0, 8.0], [13.0, 8.0], [13.0, 9.0], [12.0, 9.0], [12.0, 8.0]], [1, 2, 2, 2, 79], id='given31', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[12.0, 8.0], [13.0, 8.0], [13.0, 9.0], [12.0, 9.0], [12.0, 8.0]], [1, 2, 2, 2, 79], id='given31', capstyle='butt', fill=False)
        c.path([[9.0, 10.0], [10.0, 10.0], [10.0, 11.0], [9.0, 11.0], [9.0, 10.0]], [1, 2, 2, 2, 79], id='given03', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[9.0, 10.0], [10.0, 10.0], [10.0, 11.0], [9.0, 11.0], [9.0, 10.0]], [1, 2, 2, 2, 79], id='given03', capstyle='butt', fill=False)
        c.path([[10.0, 11.0], [11.0, 11.0], [11.0, 12.0], [10.0, 12.0], [10.0, 11.0]], [1, 2, 2, 2, 79], id='given14', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 11.0], [11.0, 11.0], [11.0, 12.0], [10.0, 12.0], [10.0, 11.0]], [1, 2, 2, 2, 79], id='given14', capstyle='butt', fill=False)
        c.path([[13.0, 9.0], [14.0, 9.0], [14.0, 10.0], [13.0, 10.0], [13.0, 9.0]], [1, 2, 2, 2, 79], id='given42', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[13.0, 9.0], [14.0, 9.0], [14.0, 10.0], [13.0, 10.0], [13.0, 9.0]], [1, 2, 2, 2, 79], id='given42', capstyle='butt', fill=False)
        c.path([[9.0, 9.0], [10.0, 9.0], [10.0, 10.0], [9.0, 10.0], [9.0, 9.0]], [1, 2, 2, 2, 79], id='given02', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[9.0, 9.0], [10.0, 9.0], [10.0, 10.0], [9.0, 10.0], [9.0, 9.0]], [1, 2, 2, 2, 79], id='given02', capstyle='butt', fill=False)
        c.path([[13.0, 8.0], [14.0, 8.0], [14.0, 9.0], [13.0, 9.0], [13.0, 8.0]], [1, 2, 2, 2, 79], id='given41', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[13.0, 8.0], [14.0, 8.0], [14.0, 9.0], [13.0, 9.0], [13.0, 8.0]], [1, 2, 2, 2, 79], id='given41', capstyle='butt', fill=False)
        for object_id, points in self._geometry_01:
            c.line(points, id=object_id)
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='option0_0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='option0_0', capstyle='butt', fill=False, **_kw.get(22, {}))
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='option0_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='option0_1', capstyle='butt', fill=False, **_kw.get(24, {}))
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0_2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='option0_2', capstyle='butt', fill=False, **_kw.get(26, {}))
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='option0_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='option0_3', capstyle='butt', fill=False, **_kw.get(28, {}))
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='option0_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='option0_4', capstyle='butt', fill=False, **_kw.get(30, {}))
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='option1_0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='option1_0', capstyle='butt', fill=False)
        c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='option1_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='option1_1', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='option1_2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='option1_2', capstyle='butt', fill=False)
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='option1_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='option1_3', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='option1_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79], id='option1_4', capstyle='butt', fill=False)
        c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='option2_0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='option2_0', capstyle='butt', fill=False, **_kw.get(42, {}))
        c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='option2_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79], id='option2_1', capstyle='butt', fill=False)
        c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='option2_2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79], id='option2_2', capstyle='butt', fill=False)
        c.path([[10.0, 3.0], [11.0, 3.0], [11.0, 4.0], [10.0, 4.0], [10.0, 3.0]], [1, 2, 2, 2, 79], id='option2_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 3.0], [11.0, 3.0], [11.0, 4.0], [10.0, 4.0], [10.0, 3.0]], [1, 2, 2, 2, 79], id='option2_3', capstyle='butt', fill=False)
        c.path([[10.0, 4.0], [11.0, 4.0], [11.0, 5.0], [10.0, 5.0], [10.0, 4.0]], [1, 2, 2, 2, 79], id='option2_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[10.0, 4.0], [11.0, 4.0], [11.0, 5.0], [10.0, 5.0], [10.0, 4.0]], [1, 2, 2, 2, 79], id='option2_4', capstyle='butt', fill=False, **_kw.get(50, {}))
        c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='option3_0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='option3_0', capstyle='butt', fill=False)
        c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='option3_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='option3_1', capstyle='butt', fill=False)
        c.path([[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79], id='option3_2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79], id='option3_2', capstyle='butt', fill=False)
        c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='option3_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='option3_3', capstyle='butt', fill=False)
        c.path([[17.0, 2.0], [18.0, 2.0], [18.0, 3.0], [17.0, 3.0], [17.0, 2.0]], [1, 2, 2, 2, 79], id='option3_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[17.0, 2.0], [18.0, 2.0], [18.0, 3.0], [17.0, 3.0], [17.0, 2.0]], [1, 2, 2, 2, 79], id='option3_4', capstyle='butt', fill=False)
        c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4_0', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[20.0, 0.0], [21.0, 0.0], [21.0, 1.0], [20.0, 1.0], [20.0, 0.0]], [1, 2, 2, 2, 79], id='option4_0', capstyle='butt', fill=False, **_kw.get(62, {}))
        c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='option4_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='option4_1', capstyle='butt', fill=False, **_kw.get(64, {}))
        c.path([[20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0]], [1, 2, 2, 2, 79], id='option4_2', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[20.0, 1.0], [21.0, 1.0], [21.0, 2.0], [20.0, 2.0], [20.0, 1.0]], [1, 2, 2, 2, 79], id='option4_2', capstyle='butt', fill=False, **_kw.get(66, {}))
        c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='option4_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 1.0], [22.0, 1.0], [22.0, 2.0], [21.0, 2.0], [21.0, 1.0]], [1, 2, 2, 2, 79], id='option4_3', capstyle='butt', fill=False, **_kw.get(68, {}))
        c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='option4_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[21.0, 2.0], [22.0, 2.0], [22.0, 3.0], [21.0, 3.0], [21.0, 2.0]], [1, 2, 2, 2, 79], id='option4_4', capstyle='butt', fill=False, **_kw.get(70, {}))
        for object_id, text, anchor in [('label0', 'A)', (-1.0, 1.5)), ('label1', 'B)', (4.0, 1.5)), ('label2', 'C)', (9.0, 1.5)), ('label3', 'D)', (14.0, 1.5)), ('label4', 'E)', (19.0, 1.5))]:
            c.text(text, anchor, id=object_id)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C01.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={22: {'edgecolor': '#DC2626', 'linewidth': 1.5}, 24: {'edgecolor': '#DC2626', 'linewidth': 1.5}})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C02.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={22: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 26: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 28: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C03.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={24: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 30: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C04.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={28: {'edgecolor': '#EA580C', 'linewidth': 2.0}, 30: {'edgecolor': '#EA580C', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C05.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={42: {'edgecolor': '#DC2626', 'linewidth': 2.0}, 50: {'edgecolor': '#DC2626', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C06.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={64: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 68: {'edgecolor': '#2563EB', 'linewidth': 2.0}, 70: {'edgecolor': '#2563EB', 'linewidth': 2.0}})
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane264_C07.png'
        with Canvas(PLANE, xlim=(-1.9647747619226656, 22.613642698354337), ylim=(-6.309172695588561, 18.26924476468844)) as c:
            self._draw_base(c, kw={62: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 64: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 66: {'edgecolor': '#EA580C', 'linewidth': 1.5}, 68: {'edgecolor': '#EA580C', 'linewidth': 1.5}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane264')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07'))
    args = parser.parse_args()
    print(Plane264().draw(args.output, variant=args.variant))
