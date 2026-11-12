"""Collected question Plane337; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane337:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane337'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1096'
        self.question = 'A square piece of paper has a $4 \\times 4$ grid. Shapes matching the pictured shape or its mirror image are cut out along the gridlines. How many squares remain if as many shapes as possible are cut out?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-2.2115773933553307, 6.198276068734156), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane337_C01.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-2.2115773933553307, 6.198276068734156), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', capstyle='butt', fill=False)
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', capstyle='butt', fill=False)
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', capstyle='butt', fill=False)
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', capstyle='butt', fill=False)
            c.line([[0, 2], [4, 2]], zorder=9, color='#DC2626', solid_capstyle='butt')
            c.line([[2, 4], [2, 0]], zorder=9, color='#DC2626', solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane337_C02.png'
        with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-2.2115773933553307, 6.198276068734156), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='cell0', capstyle='butt', fill=False)
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='cell1', capstyle='butt', fill=False)
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='cell2', capstyle='butt', fill=False)
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 3.0], [1.0, 3.0], [1.0, 4.0], [0.0, 4.0], [0.0, 3.0]], [1, 2, 2, 2, 79], id='cell3', capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='cell4', capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='cell5', capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='cell6', capstyle='butt', fill=False)
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 3.0], [2.0, 3.0], [2.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='cell7', capstyle='butt', fill=False)
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='cell8', capstyle='butt', fill=False)
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='cell9', capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='cell10', capstyle='butt', fill=False)
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 3.0], [3.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]], [1, 2, 2, 2, 79], id='cell11', capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='cell12', capstyle='butt', fill=False)
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='cell13', capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='cell14', capstyle='butt', fill=False)
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 3.0], [4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0]], [1, 2, 2, 2, 79], id='cell15', capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='cell16', capstyle='butt', fill=False)
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='cell17', capstyle='butt', fill=False)
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79], id='cell18', capstyle='butt', fill=False)
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='cell19', capstyle='butt', fill=False)
            c.line([[2, 4], [2, 0]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[2, 4], [2, 0]], zorder=9, color='#16A34A', solid_capstyle='butt')
            c.line([[4, 2], [0, 2]], zorder=9, color='#16A34A', solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane337')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane337().draw(args.output, variant=args.variant))
