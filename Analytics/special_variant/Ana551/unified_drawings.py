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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana551_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True, xlabel='t', ylabel='v') as c:
        c.line([[0.0, 0.0], [1.0, 4.0], [2.0, 0.0], [3.0, -2.0], [4.0, 0.0], [5.0, 2.0], [6.0, 0.0]], id='curve_001', solid_capstyle='butt', simplify=False)
        c.point([[0.0, 0.0], [6.0, 0.0]], id='point_001')
        c.text('$v(t)$', (1.5, 4.3), id='text_001', rotation_mode='default')
        for object_id, points in [(None, [[2.0, -2.7], [2.0, -0.9]]), (None, [[2.0, 0.3], [2.0, 4.7]]), (None, [[4.0, -2.7], [4.0, -0.9]]), (None, [[4.0, 0.3], [4.0, 4.7]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', simplify=False)
        for object_id, text, anchor in [(None, '$+$', (1, 1.3)), (None, '$-$', (3, -1.3)), (None, '$+$', (5, 0.6)), (None, '$\\int_0^6 v(t)\\,dt$', (4.5, 5.6))]:
            c.text(text, anchor, id=object_id, zorder=11, clip_on=True, color='#2563EB', rotation_mode='default')
        return c.save(output_path)
