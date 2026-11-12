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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana273_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-7.5, -6.5], [6.5, 7.5]], id='curve_001', linewidth=3.0, solid_capstyle='butt')
        for object_id, points in [('point_001', [[-4.0, -3.0]]), ('point_002', [[2.0, 3.0]]), ('point_003', [[3.0, -2.0]])]:
            c.point(points, id=object_id)
        c.text('A', (-4.25, -2.63), id='text_001', ha='right', va='bottom', rotation_mode='default')
        c.text('B', (1.75, 3.37), id='text_002', ha='right', va='bottom', rotation_mode='default')
        c.text('P', (3.23, -1.63), id='text_003', ha='left', va='bottom', rotation_mode='default')
        c.line([[3.0, -2.0], [3.0, -0.9]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3.0, 0.5], [3.0, 4.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0.5, 4.0], [3.0, 4.0]], zorder=9, color='#EA580C', solid_capstyle='butt')
        c.point([[3.0, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
