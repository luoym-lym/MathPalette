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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane255_C01.png'
    with Canvas(PLANE, xlim=(-0.3090991525872955, 12.309099152587295), ylim=(-3.815876804671571, 8.80232150050302), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 5.0], [8.0, 5.0], [12.0, 0.0], [4.0, 0.0], [0.0, 5.0]], [1, 2, 2, 2, 79], id='o0', capstyle='butt')
        for object_id, points in [('o1', [[0.0, 5.0], [1.5, 3.9]]), ('o2', [[1.5, 3.9], [2.6, 4.5]]), ('o3', [[2.6, 4.5], [2.7, 3.2]]), ('o4', [[2.7, 3.2], [5.5, 2.95]]), ('o5', [[5.5, 2.95], [5.5, 1.2]]), ('o6', [[5.5, 1.2], [7.0, 1.95]]), ('o7', [[7.0, 1.95], [8.4, 0.85]]), ('o8', [[8.4, 0.85], [9.25, 1.45]]), ('o9', [[9.25, 1.45], [9.35, 0.7]]), ('o10', [[9.35, 0.7], [12.0, 0.0]])]:
            c.line(points, id=object_id)
        c.text('$P_1$', (4.5, 1.4), id='t0', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('$P_2$', (7.3, 3.5), id='t1', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[0, 5], [12, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
