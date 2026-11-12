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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana269_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-7.5, -6.5], [6.5, 7.5]], id='curve_001', color='#2563EB', linewidth=0.5, linestyle=(0.0, [1.85, 0.8]), solid_capstyle='butt')
        c.line([[-7.5, -3.5], [3.5, 7.5]], id='curve_002', color='#EA580C', linewidth=3.0, solid_capstyle='butt')
        for object_id, points in [('point_001', [[-5.0, -4.0]]), ('point_002', [[1.0, 2.0]]), ('point_003', [[-4.0, 0.0]]), ('point_004', [[2.0, 6.0]])]:
            c.point(points, id=object_id)
        for object_id, text, anchor in [('text_001', 'A', (-5.25, -3.63)), ('text_002', 'B', (0.75, 2.37)), ('text_003', 'C', (-4.25, 0.37)), ('text_004', 'D', (1.75, 6.37))]:
            c.text(text, anchor, id=object_id, ha='right', va='bottom', rotation_mode='default')
        return c.save(output_path)
