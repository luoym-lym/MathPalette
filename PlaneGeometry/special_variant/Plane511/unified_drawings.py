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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane511_C01.png'
    with Canvas(PLANE, xlim=(-0.15128068303094988, 4.65128068303095), ylim=(-1.1022425773542919, 3.700318788707608), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dot01', [[0.0, 0.0]]), ('dot02', [[1.0, 0.0]]), ('dot03', [[2.0, 0.0]]), ('dot04', [[0.5, 0.8660254037844386]]), ('dot05', [[1.5, 0.8660254037844386]]), ('dot06', [[2.5, 0.8660254037844386]]), ('dot07', [[3.5, 0.8660254037844386]]), ('dot08', [[1.0, 1.7320508075688772]]), ('dot09', [[2.0, 1.7320508075688772]]), ('dot10', [[3.0, 1.7320508075688772]]), ('dot11', [[4.0, 1.7320508075688772]]), ('dot12', [[2.5, 2.598076211353316]]), ('dot13', [[3.5, 2.598076211353316]]), ('dot14', [[4.5, 2.598076211353316]])]:
            c.point(points, id=object_id)
        for object_id, points in [(None, [[-0.12, -0.15], [1.68, -0.15]]), (None, [[1.68, -0.15], [1.68, 1.9]]), (None, [[1.68, 1.9], [-0.12, 1.9]]), (None, [[-0.12, 1.9], [-0.12, -0.15]])]:
            c.line(points, id=object_id, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[1.82, -0.15], [4.62, -0.15]]), (None, [[4.62, -0.15], [4.62, 2.75]]), (None, [[4.62, 2.75], [1.82, 2.75]]), (None, [[1.82, 2.75], [1.82, -0.15]])]:
            c.line(points, id=object_id, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane511_C02.png'
    with Canvas(PLANE, xlim=(-0.15128068303094988, 4.65128068303095), ylim=(-1.1022425773542919, 3.700318788707608), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dot01', [[0.0, 0.0]]), ('dot02', [[1.0, 0.0]]), ('dot03', [[2.0, 0.0]]), ('dot04', [[0.5, 0.8660254037844386]]), ('dot05', [[1.5, 0.8660254037844386]]), ('dot06', [[2.5, 0.8660254037844386]]), ('dot07', [[3.5, 0.8660254037844386]]), ('dot08', [[1.0, 1.7320508075688772]]), ('dot09', [[2.0, 1.7320508075688772]]), ('dot10', [[3.0, 1.7320508075688772]]), ('dot11', [[4.0, 1.7320508075688772]]), ('dot12', [[2.5, 2.598076211353316]]), ('dot13', [[3.5, 2.598076211353316]]), ('dot14', [[4.5, 2.598076211353316]])]:
            c.point(points, id=object_id)
        for object_id, points in [(None, [[1.34, 0.7060254037844386], [1.66, 0.7060254037844386]]), (None, [[1.66, 0.7060254037844386], [1.66, 1.0260254037844385]]), (None, [[1.66, 1.0260254037844385], [1.34, 1.0260254037844385]]), (None, [[1.34, 1.0260254037844385], [1.34, 0.7060254037844386]]), (None, [[2.34, 0.7060254037844386], [2.66, 0.7060254037844386]]), (None, [[2.66, 0.7060254037844386], [2.66, 1.0260254037844385]]), (None, [[2.66, 1.0260254037844385], [2.34, 1.0260254037844385]]), (None, [[2.34, 1.0260254037844385], [2.34, 0.7060254037844386]]), (None, [[2.84, 1.5720508075688773], [3.16, 1.5720508075688773]]), (None, [[3.16, 1.5720508075688773], [3.16, 1.8920508075688771]]), (None, [[3.16, 1.8920508075688771], [2.84, 1.8920508075688771]]), (None, [[2.84, 1.8920508075688771], [2.84, 1.5720508075688773]])]:
            c.line(points, id=object_id, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
