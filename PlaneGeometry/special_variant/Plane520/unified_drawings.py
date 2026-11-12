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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane520_C01.png'
    with Canvas(PLANE, xlim=(-0.1860465116279073, 8.186046511627907), ylim=(-0.1860465116279073, 8.186046511627907), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [(None, [[0.0, 7.0], [1.0, 7.0], [1.0, 8.0], [0.0, 8.0], [0.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[6.0, 7.0], [7.0, 7.0], [7.0, 8.0], [6.0, 8.0], [6.0, 7.0]], [1, 2, 2, 2, 79]), (None, [[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79]), (None, [[3.0, 5.0], [4.0, 5.0], [4.0, 6.0], [3.0, 6.0], [3.0, 5.0]], [1, 2, 2, 2, 79]), (None, [[3.0, 4.0], [4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), capstyle='butt')
        c.line([[0, 0], [0, 8]], id='v0')
        c.path([[1.0, 1.1102230246251565e-16], [1.0, 1.0]], [1, 2], id='v1', joinstyle='round', fill=False)
        c.path([[1.0, 1.0], [1.0, 7.0]], [1, 2], id='v1', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), joinstyle='round', fill=False)
        c.path([[1.0, 7.0], [1.0, 8.0]], [1, 2], id='v1', joinstyle='round', fill=False)
        c.line([[2, 0], [2, 8]], id='v2')
        c.line([[3, 0], [3, 8]], id='v3')
        c.line([[4, 0], [4, 8]], id='v4', color='#16A34A')
        c.line([[5, 0], [5, 8]], id='v5')
        c.line([[6, 0], [6, 8]], id='v6')
        c.path([[7.0, 1.1102230246251565e-16], [7.0, 1.0]], [1, 2], id='v7', joinstyle='round', fill=False)
        c.path([[7.0, 1.0], [7.0, 7.0]], [1, 2], id='v7', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), joinstyle='round', fill=False)
        c.path([[7.0, 7.0], [7.0, 8.0]], [1, 2], id='v7', joinstyle='round', fill=False)
        c.line([[8, 0], [8, 8]], id='v8')
        c.line([[0, 0], [8, 0]], id='h0')
        c.path([[1.1102230246251565e-16, 1.0], [1.0, 1.0]], [1, 2], id='h1', joinstyle='round', fill=False)
        c.path([[1.0, 1.0], [7.0, 1.0]], [1, 2], id='h1', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), joinstyle='round', fill=False)
        c.path([[7.0, 1.0], [8.0, 1.0]], [1, 2], id='h1', joinstyle='round', fill=False)
        c.line([[0, 2], [8, 2]], id='h2')
        c.line([[0, 3], [8, 3]], id='h3')
        c.line([[0, 4], [8, 4]], id='h4', color='#16A34A')
        c.line([[0, 5], [8, 5]], id='h5')
        c.line([[0, 6], [8, 6]], id='h6')
        c.path([[1.1102230246251565e-16, 7.0], [1.0, 7.0]], [1, 2], id='h7', joinstyle='round', fill=False)
        c.path([[1.0, 7.0], [7.0, 7.0]], [1, 2], id='h7', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), joinstyle='round', fill=False)
        c.path([[7.0, 7.0], [8.0, 7.0]], [1, 2], id='h7', joinstyle='round', fill=False)
        c.line([[0, 8], [8, 8]], id='h8')
        for object_id, points in [(None, [[0, 0], [2, 2]]), (None, [[8, 8], [6, 6]]), (None, [[0, 8], [2, 6]]), (None, [[8, 0], [6, 2]])]:
            c.line(points, id=object_id, zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
