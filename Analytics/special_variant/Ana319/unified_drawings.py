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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana319_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.point([[-2.0, 2.0]], id='point_001')
        c.point([[1.0, 3.0]], id='point_002')
        for object_id, text, anchor in [('text_001', 'A', (-1.78, 2.25)), ('text_002', 'B', (1.22, 3.25)), ('text_003', 'l', (6.5, 0.35))]:
            c.text(text, anchor, id=object_id, ha='left', va='bottom', rotation_mode='default')
        for object_id, points in [(None, [[-2, 2], [-2, -2]]), (None, [[-2, -2], [1, 2]]), (None, [[-2.0, 2.0], [-0.549287, 0.021026]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
