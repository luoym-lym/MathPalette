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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana559_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-5.0, -3.0], [-2.0, 1.0]], id='curve_001', solid_capstyle='butt')
        c.line([[1.0, -3.0], [3.0, -2.0]], id='curve_002', solid_capstyle='butt')
        for object_id, points in [('point_001', [[-5.0, -3.0]]), ('point_002', [[-2.0, 1.0]]), ('point_003', [[1.0, -3.0]]), ('point_004', [[3.0, -2.0]])]:
            c.point(points, id=object_id)
        for object_id, text, anchor in [('text_001', 'A', (-5.4, -3.4)), ('text_002', 'B', (-2.4, 1.4)), ('text_003', 'C', (0.7, -3.5)), ('text_004', 'D', (3.45, -2.1))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[-2, 1], [0, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[-5, -3], [0, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[0.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
