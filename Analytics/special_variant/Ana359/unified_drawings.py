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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana359_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.point([[-2.0, 3.0]], id='point_001')
        c.point([[3.0, 2.0]], id='point_002')
        for object_id, text, anchor in [('text_001', 'M', (-1.78, 3.25)), ('text_002', 'N', (3.22, 2.25)), ('text_003', 'l', (6.5, 0.35))]:
            c.text(text, anchor, id=object_id, ha='left', va='bottom', rotation_mode='default')
        for object_id, points in [(None, [[-2, 3], [-2, -3]]), (None, [[-2, -3], [3, 1]]), (None, [[-2.0, 3.0], [1.640082, -0.008016]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[-2.0, -3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
