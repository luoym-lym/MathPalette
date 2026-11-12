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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana554_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        for object_id, points in [('curve_001', [[0.0, 0.0], [2.0, 1.0]]), ('curve_002', [[0.0, 0.0], [-1.0, 2.0]]), ('curve_003', [[0.0, 0.0], [3.0, 4.0]])]:
            c.line(points, id=object_id, solid_capstyle='butt')
        for object_id, points in [('point_001', [[2.0, 1.0]]), ('point_002', [[-1.0, 2.0]]), ('point_003', [[3.0, 4.0]])]:
            c.point(points, id=object_id)
        for object_id, text, anchor in [('text_001', 'U', (2.45, 0.8)), ('text_002', 'V', (-1.45, 2.2)), ('text_003', 'P', (3.4, 4.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[3, 4], [3, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 4], [0, 4]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[0.0, 4.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
