"""Frozen, previously passed Special drawings on the unified protocol. No new Pass/Collect."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

def C01(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane178_C01.png'
    with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 5.0], [0.0, 5.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
        c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 4.0], [4.0, 4.0], [4.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
        c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 3.0], [4.0, 3.0], [4.0, 4.0], [1.0, 4.0], [1.0, 3.0]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[4.0, 2.0], [5.0, 2.0], [5.0, 5.0], [4.0, 5.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 3.0], [1.0, 3.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
        c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 1.0], [5.0, 1.0], [5.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
        c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 0.0], [5.0, 0.0], [5.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
        c.line([[0, 5], [1, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1, 3], [2, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
