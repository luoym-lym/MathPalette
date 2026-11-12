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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana556_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[0.0, 0.0], [2.0, 1.0]], id='curve_001', solid_capstyle='butt')
        for object_id, points in [('point_001', [[1.0, 0.0]]), ('point_002', [[0.0, 1.0]]), ('point_003', [[2.0, 1.0]]), ('point_004', [[-3.0, 2.0]])]:
            c.point(points, id=object_id)
        for object_id, text, anchor in [('text_001', 'E1=T(E1)', (2, -0.8)), ('text_002', 'E2', (-0.65, 1.35)), ('text_003', 'V=T(E2)', (3.3, 1.3)), ('text_004', 'P', (-3.45, 2.4))]:
            c.text(text, anchor, id=object_id, rotation_mode='default')
        c.line([[0, 1], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[-3, 2], [-1, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[-1.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[-1, 2], [-1, 0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
