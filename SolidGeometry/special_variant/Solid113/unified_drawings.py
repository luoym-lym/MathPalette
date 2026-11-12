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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid113_C01.png'
    with Canvas(SOLID, xlim=(-0.4508658920902806, 3.8069977961600476), ylim=(-0.8069977961600476, 3.4508658920902806), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('stairse0', [[0.0, 0.0], [1.0, 0.0]]), ('stairse1', [[0.0, 1.0], [1.0, 1.0]]), ('stairse2', [[-0.35, 1.35], [0.65, 1.35]]), ('stairse3', [[0.0, 0.0], [-0.35, 0.35]]), ('stairse4', [[0.0, 1.0], [-0.35, 1.35]]), ('stairse5', [[1.0, 1.0], [0.65, 1.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('stairse6', [[0.0, 0.0], [0.0, 1.0]]), ('stairse7', [[-0.35, 0.35], [-0.35, 1.35]]), ('stairse8', [[1.0, 0.0], [1.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('stairse9', [[1.35, -0.35], [2.35, -0.35]]), ('stairse10', [[1.35, 0.65], [2.35, 0.65]]), ('stairse11', [[1.0, 1.0], [2.0, 1.0]]), ('stairse12', [[1.35, -0.35], [1.0, 0.0]]), ('stairse13', [[1.35, 0.65], [1.0, 1.0]]), ('stairse14', [[2.35, 0.65], [2.0, 1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[1.35, -0.35], [1.35, 0.65]], id='stairse15', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[2.35, -0.35], [2.35, 0.65]], id='stairse16', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('stairse17', [[1.0, 2.0], [2.0, 2.0]]), ('stairse18', [[0.65, 2.35], [1.65, 2.35]]), ('stairse19', [[1.0, 2.0], [0.65, 2.35]]), ('stairse20', [[2.0, 2.0], [1.65, 2.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('stairse21', [[1.0, 1.0], [1.0, 2.0]]), ('stairse22', [[0.65, 1.35], [0.65, 2.35]]), ('stairse23', [[2.0, 1.0], [2.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('stairse24', [[2.7, -0.7], [3.7, -0.7]]), ('stairse25', [[2.7, 0.30000000000000004], [3.7, 0.30000000000000004]]), ('stairse26', [[2.35, 0.65], [3.35, 0.65]]), ('stairse27', [[2.7, -0.7], [2.35, -0.35]]), ('stairse28', [[2.7, 0.30000000000000004], [2.35, 0.65]]), ('stairse29', [[3.7, 0.30000000000000004], [3.35, 0.65]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[2.7, -0.7], [2.7, 0.30000000000000004]], id='stairse30', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.7, -0.7], [3.7, 0.30000000000000004]], id='stairse31', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('stairse32', [[2.35, 1.65], [3.35, 1.65]]), ('stairse33', [[2.0, 2.0], [3.0, 2.0]]), ('stairse34', [[2.35, 1.65], [2.0, 2.0]]), ('stairse35', [[3.35, 1.65], [3.0, 2.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        c.line([[2.35, 0.65], [2.35, 1.65]], id='stairse36', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[3.35, 0.65], [3.35, 1.65]], id='stairse37', zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('stairse38', [[2.0, 3.0], [3.0, 3.0]]), ('stairse39', [[1.65, 3.35], [2.65, 3.35]]), ('stairse40', [[2.0, 3.0], [1.65, 3.35]]), ('stairse41', [[3.0, 3.0], [2.65, 3.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('stairse42', [[2.0, 2.0], [2.0, 3.0]]), ('stairse43', [[1.65, 2.35], [1.65, 3.35]]), ('stairse44', [[3.0, 2.0], [3.0, 3.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#2563EB', linewidth=1.5, solid_capstyle='butt', simplify=False)
        return c.save(output_path)
