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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana560_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True, xlabel='Re', ylabel='Im') as c:
        c.line([[0.0, 0.0], [2.0, 1.0]], id='curve_001', solid_capstyle='butt', simplify=False)
        c.line([[0.0, 0.0], [-1.0, 2.0]], id='curve_002', solid_capstyle='butt', simplify=False)
        c.point([[2.0, 1.0]], id='point_001')
        c.point([[-1.0, 2.0]], id='point_002')
        c.text('z', (2.45, 0.9), id='text_001', rotation_mode='default')
        c.text('w', (-1.45, 2.3), id='text_002', rotation_mode='default')
        for object_id, points in [(None, [[2.0, 1.0], [1.0, 3.0]]), (None, [[-1.0, 2.0], [1.0, 3.0]]), (None, [[0.0, 0.0], [1.0, 3.0]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt', simplify=False)
        c.point([[1.0, 3.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
