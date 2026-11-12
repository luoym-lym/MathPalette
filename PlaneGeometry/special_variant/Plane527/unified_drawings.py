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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane527_C01.png'
    with Canvas(PLANE, xlim=(-0.08823529411764719, 3.088235294117647), ylim=(-0.5882352941176472, 2.588235294117647), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [(None, [[0.0, 0.0]]), (None, [[0.0, 1.0]]), (None, [[0.0, 2.0]]), (None, [[1.0, 0.0]]), (None, [[1.0, 1.0]]), (None, [[1.0, 2.0]]), (None, [[2.0, 0.0]]), (None, [[2.0, 1.0]]), (None, [[2.0, 2.0]]), (None, [[3.0, 0.0]]), (None, [[3.0, 1.0]]), (None, [[3.0, 2.0]])]:
            c.point(points, id=object_id)
        c.line([[1, 0], [3, 0]], color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 0], [3, 2]], color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 2], [1, 2]], color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1, 2], [1, 0]], color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1, 1], [3, 2]], color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0, 0], [1, 0]], color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0, 0], [0, 1]], color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
