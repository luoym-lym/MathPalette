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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane307_C01.png'
    with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 6.0]], id='v1')
        c.line([[2.0, 0.0], [2.0, 6.0]], id='v2')
        c.line([[3.0, 0.0], [3.0, 6.0]], id='v3', color='#DC2626')
        for object_id, points in [('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]])]:
            c.line(points, id=object_id)
        c.line([[0.0, 3.0], [6.0, 3.0]], id='h3', color='#DC2626')
        c.line([[0.0, 4.0], [6.0, 4.0]], id='h4')
        c.line([[0.0, 5.0], [6.0, 5.0]], id='h5')
        c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane307_C02.png'
    with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
        for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
        c.line([[0, 6], [6, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[6, 6], [0, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane307_C03.png'
    with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
        for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
        c.line([[6, 6], [0, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0, 6], [6, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane307_C04.png'
    with Canvas(PLANE, xlim=(-0.14824620141445033, 6.15721078160753), ylim=(-0.15797195779922157, 6.147485025222759), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 4.0], [3.0, 4.0], [3.0, 5.0], [2.0, 5.0], [2.0, 4.0]], [1, 2, 2, 2, 79], id='green24', capstyle='butt', fill=False)
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79], id='green25', capstyle='butt', fill=False)
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79], id='green15', capstyle='butt', fill=False)
        for object_id, points in [('v1', [[1.0, 0.0], [1.0, 6.0]]), ('v2', [[2.0, 0.0], [2.0, 6.0]]), ('v3', [[3.0, 0.0], [3.0, 6.0]]), ('v4', [[4.0, 0.0], [4.0, 6.0]]), ('v5', [[5.0, 0.0], [5.0, 6.0]]), ('h1', [[0.0, 1.0], [6.0, 1.0]]), ('h2', [[0.0, 2.0], [6.0, 2.0]]), ('h3', [[0.0, 3.0], [6.0, 3.0]]), ('h4', [[0.0, 4.0], [6.0, 4.0]]), ('h5', [[0.0, 5.0], [6.0, 5.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 6.0], [0.0, 6.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outer', capstyle='butt')
        c.line([[0, 3], [6, 3]], zorder=9, color='#16A34A', solid_capstyle='butt')
        c.line([[3, 6], [3, 0]], zorder=9, color='#16A34A', solid_capstyle='butt')
        return c.save(output_path)
