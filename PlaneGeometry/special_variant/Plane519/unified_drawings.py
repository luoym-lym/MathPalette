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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane519_C01.png'
    with Canvas(PLANE, xlim=(-0.1627906976744189, 7.162790697674419), ylim=(-0.1627906976744189, 7.162790697674419), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [(None, [[0.0, 6.0], [1.0, 6.0], [1.0, 7.0], [0.0, 7.0], [0.0, 6.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 6.0], [2.0, 6.0], [2.0, 7.0], [1.0, 7.0], [1.0, 6.0]], [1, 2, 2, 2, 79]), (None, [[5.0, 6.0], [6.0, 6.0], [6.0, 7.0], [5.0, 7.0], [5.0, 6.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79]), (None, [[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), capstyle='butt')
        for object_id, points in [('v0', [[0, 0], [0, 7]]), ('v1', [[1, 0], [1, 7]]), ('v2', [[2, 0], [2, 7]])]:
            c.line(points, id=object_id)
        c.line([[3, 0], [3, 7]], id='v3', color='#DC2626')
        c.line([[4, 0], [4, 7]], id='v4', color='#DC2626')
        for object_id, points in [('v5', [[5, 0], [5, 7]]), ('v6', [[6, 0], [6, 7]]), ('v7', [[7, 0], [7, 7]]), ('h0', [[0, 0], [7, 0]]), ('h1', [[0, 1], [7, 1]]), ('h2', [[0, 2], [7, 2]])]:
            c.line(points, id=object_id)
        c.line([[0, 3], [7, 3]], id='h3', color='#DC2626')
        c.line([[0, 4], [7, 4]], id='h4', color='#DC2626')
        for object_id, points in [('h5', [[0, 5], [7, 5]]), ('h6', [[0, 6], [7, 6]]), ('h7', [[0, 7], [7, 7]])]:
            c.line(points, id=object_id)
        return c.save(output_path)
