"""Collected question Plane325; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane325:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c):
        c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='cell4_0', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='cell4_0', capstyle='butt', fill=False)
        c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='cell3_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79], id='cell3_4', capstyle='butt', fill=False)
        c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='cell4_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 3.0], [5.0, 3.0], [5.0, 4.0], [4.0, 4.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='cell4_3', capstyle='butt', fill=False)
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell3_1', capstyle='butt', fill=False)
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell3_7', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 7.0], [4.0, 7.0], [4.0, 8.0], [3.0, 8.0], [3.0, 7.0]], [1, 2, 2, 2, 79], id='cell3_7', capstyle='butt', fill=False)
        c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='cell5_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 4.0], [6.0, 4.0], [6.0, 5.0], [5.0, 5.0], [5.0, 4.0]], [1, 2, 2, 2, 79], id='cell5_4', capstyle='butt', fill=False)
        c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[4.0, 6.0], [5.0, 6.0], [5.0, 7.0], [4.0, 7.0], [4.0, 6.0]], [1, 2, 2, 2, 79], id='cell4_6', capstyle='butt', fill=False)
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell5_1', capstyle='butt', fill=False)
        c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 7.0], [6.0, 7.0], [6.0, 8.0], [5.0, 8.0], [5.0, 7.0]], [1, 2, 2, 2, 79], id='cell5_7', capstyle='butt', fill=False)
        c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell2_2', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='cell2_5', capstyle='butt', fill=False)
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell1_3', capstyle='butt', fill=False)
        c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79], id='cell7_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[7.0, 4.0], [8.0, 4.0], [8.0, 5.0], [7.0, 5.0], [7.0, 4.0]], [1, 2, 2, 2, 79], id='cell7_4', capstyle='butt', fill=False)
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell6_2', capstyle='butt', fill=False)
        c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[6.0, 5.0], [7.0, 5.0], [7.0, 6.0], [6.0, 6.0], [6.0, 5.0]], [1, 2, 2, 2, 79], id='cell6_5', capstyle='butt', fill=False)
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='cell4_2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 3.0], [4.0, 3.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='cell4_2', capstyle='butt', fill=False)
        c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79], id='cell4_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 5.0], [5.0, 5.0], [5.0, 6.0], [4.0, 6.0], [4.0, 5.0]], [1, 2, 2, 2, 79], id='cell4_5', capstyle='butt', fill=False)
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell3_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell3_3', capstyle='butt', fill=False)
        c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79], id='cell5_6', capstyle='butt', fill=False)
        c.path([[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79], id='cell4_8', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 8.0], [5.0, 8.0], [5.0, 9.0], [4.0, 9.0], [4.0, 8.0]], [1, 2, 2, 2, 79], id='cell4_8', capstyle='butt', fill=False)
        c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 6.0], [4.0, 6.0], [4.0, 7.0], [3.0, 7.0], [3.0, 6.0]], [1, 2, 2, 2, 79], id='cell3_6', capstyle='butt', fill=False)
        c.path([[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79], id='cell5_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 3.0], [6.0, 3.0], [6.0, 4.0], [5.0, 4.0], [5.0, 3.0]], [1, 2, 2, 2, 79], id='cell5_3', capstyle='butt', fill=False)
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell2_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='cell2_4', capstyle='butt', fill=False)
        c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='cell0_4', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='cell1_5', capstyle='butt', fill=False)
        c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 4.0], [7.0, 4.0], [7.0, 5.0], [6.0, 5.0], [6.0, 4.0]], [1, 2, 2, 2, 79], id='cell6_4', capstyle='butt', fill=False)
        c.path([[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79], id='cell7_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[7.0, 3.0], [8.0, 3.0], [8.0, 4.0], [7.0, 4.0], [7.0, 3.0]], [1, 2, 2, 2, 79], id='cell7_3', capstyle='butt', fill=False)
        c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell3_2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell3_2', capstyle='butt', fill=False)
        c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='cell4_1', capstyle='butt', fill=False)
        c.path([[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='cell4_7', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 7.0], [5.0, 7.0], [5.0, 8.0], [4.0, 8.0], [4.0, 7.0]], [1, 2, 2, 2, 79], id='cell4_7', capstyle='butt', fill=False)
        c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell3_5', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79], id='cell3_5', capstyle='butt', fill=False)
        c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='cell5_2', capstyle='butt', fill=False)
        c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='cell4_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[4.0, 4.0], [5.0, 4.0], [5.0, 5.0], [4.0, 5.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='cell4_4', capstyle='butt', fill=False)
        c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[5.0, 5.0], [6.0, 5.0], [6.0, 6.0], [5.0, 6.0], [5.0, 5.0]], [1, 2, 2, 2, 79], id='cell5_5', capstyle='butt', fill=False)
        c.path([[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79], id='cell8_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[8.0, 4.0], [9.0, 4.0], [9.0, 5.0], [8.0, 5.0], [8.0, 4.0]], [1, 2, 2, 2, 79], id='cell8_4', capstyle='butt', fill=False)
        c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='cell1_4', capstyle='butt', fill=False)
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell2_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell2_3', capstyle='butt', fill=False)
        c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79], id='cell2_6', capstyle='butt', fill=False)
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell6_6', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 6.0], [7.0, 6.0], [7.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79], id='cell6_6', capstyle='butt', fill=False)
        c.path([[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79], id='cell7_5', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[7.0, 5.0], [8.0, 5.0], [8.0, 6.0], [7.0, 6.0], [7.0, 5.0]], [1, 2, 2, 2, 79], id='cell7_5', capstyle='butt', fill=False)
        c.path([[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='cell6_3', zorder=1, edgecolor='none', facecolor='white', linewidth=0.0, capstyle='butt')
        c.path([[6.0, 3.0], [7.0, 3.0], [7.0, 4.0], [6.0, 4.0], [6.0, 3.0]], [1, 2, 2, 2, 79], id='cell6_3', capstyle='butt', fill=False)

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.22437711759410206, 9.240158404748396), ylim=(-0.24077445742880865, 9.223761064913688)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane325_C01.png'
        with Canvas(PLANE, xlim=(-0.22437711759410206, 9.240158404748396), ylim=(-0.24077445742880865, 9.223761064913688)) as c:
            self._draw_base(c)
            c.point([[5.513110919642935, 3.486273027676651]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            c.point([[4.498225063999591, 2.4327248537230846]], zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane325_C02.png'
        with Canvas(PLANE, xlim=(-0.22437711759410206, 9.240158404748396), ylim=(-0.24077445742880865, 9.223761064913688)) as c:
            self._draw_base(c)
            c.line([[2, 7], [7, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane325_C03.png'
        with Canvas(PLANE, xlim=(-0.22437711759410206, 9.240158404748396), ylim=(-0.24077445742880865, 9.223761064913688)) as c:
            self._draw_base(c)
            for object_id, points in [(None, [[5.484114180910268, 3.4669418685215403]]), (None, [[4.47889390484448, 2.461721592455752]]), (None, [[7.552548210507178, 3.4476107093664288]]), (None, [[2.458787773135348, 2.461721592455752]])]:
                c.point(points, id=object_id, zorder=10, s=50, facecolors='#DC2626', edgecolors='#DC2626')
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane325_C04.png'
        with Canvas(PLANE, xlim=(-0.22437711759410206, 9.240158404748396), ylim=(-0.24077445742880865, 9.223761064913688)) as c:
            self._draw_base(c)
            c.line([[2, 7], [7, 2]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane325')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Plane325().draw(args.output, variant=args.variant))
