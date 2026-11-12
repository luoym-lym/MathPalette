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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane25_C01.png'
    with Canvas(PLANE, xlim=(-0.5734572248750054, 2.5776993434716937), ylim=(-0.0776993434716935, 3.073457224875005), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('o1', [[0.0, 0.0], [0.0, 3.0]]), ('o2', [[1.0, 0.0], [1.0, 3.0]]), ('o3', [[2.0, 0.0], [2.0, 3.0]]), ('o4', [[0.0, 0.0], [2.0, 0.0]]), ('o5', [[0.0, 1.0], [2.0, 1.0]]), ('o6', [[0.0, 2.0], [2.0, 2.0]]), ('o7', [[0.0, 3.0], [2.0, 3.0]])]:
            c.line(points, id=object_id)
        c.line([[0.00451226008727712, 1.4817884761982516], [1.9997298585094105, 1.4785703832975705]], zorder=9, color='#2563EB', solid_capstyle='butt')
        return c.save(output_path)
