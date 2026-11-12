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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane510_C01.png'
    with Canvas(PLANE, xlim=(-0.13447171824973303, 4.134471718249733), ylim=(-1.2684463144652944, 3.0004971220341714), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dot01', [[0.0, 0.0]]), ('dot02', [[1.0, 0.0]]), ('dot03', [[2.0, 0.0]]), ('dot04', [[3.0, 0.0]]), ('dot05', [[0.5, 0.8660254037844386]]), ('dot06', [[1.5, 0.8660254037844386]]), ('dot07', [[2.5, 0.8660254037844386]]), ('dot08', [[3.5, 0.8660254037844386]]), ('dot09', [[1.0, 1.7320508075688772]]), ('dot10', [[2.0, 1.7320508075688772]]), ('dot11', [[3.0, 1.7320508075688772]]), ('dot12', [[4.0, 1.7320508075688772]])]:
            c.point(points, id=object_id)
        for object_id, points in [(None, [[0.0, 0.0], [1.0, 0.0]]), (None, [[0.0, 0.0], [0.5, 0.8660254037844386]]), (None, [[1.0, 0.0], [0.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[2.0, 0.0], [1.5, 0.8660254037844386]]), (None, [[2.0, 0.0], [2.5, 0.8660254037844386]]), (None, [[1.5, 0.8660254037844386], [2.5, 0.8660254037844386]])]:
            c.line(points, id=object_id, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[3.0, 0.0], [2.0, 1.7320508075688772]]), (None, [[3.0, 0.0], [4.0, 1.7320508075688772]]), (None, [[2.0, 1.7320508075688772], [4.0, 1.7320508075688772]])]:
            c.line(points, id=object_id, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
