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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana547_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-6.0, -3.0], [-2.0, 1.0], [1.0, 4.0], [4.0, 1.0], [6.0, 3.0]], id='curve_001', solid_capstyle='butt')
        c.line([[-6.0, 5.0], [-2.0, 3.0], [0.0, -1.0], [2.0, 1.0], [4.0, -3.0], [6.0, -1.0]], id='curve_002', solid_capstyle='butt')
        c.point([[-6.0, -3.0], [6.0, 3.0], [-6.0, 5.0], [6.0, -1.0]], id='point_001')
        c.text('$f$', (6.5, 3.3), id='text_001', rotation_mode='default')
        c.text('$g$', (6.5, -1.2), id='text_002', rotation_mode='default')
        c.point([[-2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        for object_id, points in [(None, [[-2, 1], [4, 1]]), (None, [[-2, 1], [-2, 0]]), (None, [[4, 1], [4, 0]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[4.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana547_C02.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-6.0, -3.0], [-2.0, 1.0], [1.0, 4.0], [4.0, 1.0], [6.0, 3.0]], id='curve_001', solid_capstyle='butt')
        c.line([[-6.0, 5.0], [-2.0, 3.0], [0.0, -1.0], [2.0, 1.0], [4.0, -3.0], [6.0, -1.0]], id='curve_002', solid_capstyle='butt')
        c.point([[-6.0, -3.0], [6.0, 3.0], [-6.0, 5.0], [6.0, -1.0]], id='point_001')
        c.text('$f$', (6.5, 3.3), id='text_001', rotation_mode='default')
        c.text('$g$', (6.5, -1.2), id='text_002', rotation_mode='default')
        c.point([[-2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[8, 8], [-8, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[1.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        for object_id, points in [(None, [[-2, 1], [1, 1]]), (None, [[-2, 1], [-2, 0]]), (None, [[1, 1], [1, 0]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
