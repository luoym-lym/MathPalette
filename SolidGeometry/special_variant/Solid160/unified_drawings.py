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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid160_C01.png'
    with Canvas(SOLID, xlim=(-0.05852712257090298, 2.412085140981756), ylim=(-0.06208514098175533, 2.4085271225709035), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [1.0, 0.0]], id='slabe0', zorder=3, clip_on=False)
        c.line([[0.0, 1.0], [1.0, 1.0]], id='slabe1', zorder=3, clip_on=False, color='#2563EB')
        c.line([[0.0, 0.0], [0.0, 1.0]], id='slabe2', zorder=3, clip_on=False)
        c.line([[1.0, 0.0], [1.0, 1.0]], id='slabe3', zorder=3, clip_on=False, color='#2563EB')
        c.line([[0.0, 2.0], [1.0, 2.0]], id='slabe4', zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in [('slabe5', [[0.35, 2.35], [1.35, 2.35]]), ('slabe6', [[0.0, 2.0], [0.35, 2.35]]), ('slabe7', [[1.0, 2.0], [1.35, 2.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[0.0, 1.0], [0.0, 2.0]], id='slabe8', zorder=3, clip_on=False, color='#2563EB')
        for object_id, points in [('slabe9', [[1.0, 1.0], [1.0, 2.0]]), ('slabe10', [[1.0, 0.0], [2.0, 0.0]]), ('slabe11', [[1.0, 1.0], [2.0, 1.0]]), ('slabe12', [[2.0, 0.0], [2.35, 0.35]]), ('slabe13', [[2.0, 1.0], [2.35, 1.35]]), ('slabe14', [[2.0, 0.0], [2.0, 1.0]]), ('slabe15', [[2.35, 0.35], [2.35, 1.35]]), ('slabe16', [[1.0, 2.0], [2.0, 2.0]]), ('slabe17', [[1.35, 2.35], [2.35, 2.35]]), ('slabe18', [[2.0, 2.0], [2.35, 2.35]]), ('slabe19', [[2.0, 1.0], [2.0, 2.0]]), ('slabe20', [[2.35, 1.35], [2.35, 2.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        return c.save(output_path)
