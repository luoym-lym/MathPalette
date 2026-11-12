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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana550_C01.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-6.0, 4.0], [-4.0, 0.0], [-2.0, -4.0], [0.0, 0.0], [2.0, 4.0], [4.0, 0.0], [6.0, -4.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-6.0, 4.0], [6.0, -4.0]], id='point_001')
        c.text('$f$', (6.5, -4.2), id='text_001', rotation_mode='default')
        c.line([[-8, 2], [8, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[-5.0, 2.0]]), (None, [[1.0, 2.0]]), (None, [[3.0, 2.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[-8, -2], [2, -2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[-3.0, -2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[-1.0, -2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / 'Ana550_C02.png'
    with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
        c.line([[-6.0, 4.0], [-4.0, 0.0], [-2.0, -4.0], [0.0, 0.0], [2.0, 4.0], [4.0, 0.0], [6.0, -4.0]], id='curve_001', solid_capstyle='butt')
        c.point([[-6.0, 4.0], [6.0, -4.0]], id='point_001')
        c.text('$f$', (6.5, -4.2), id='text_001', rotation_mode='default')
        c.line([[-8, 2], [2, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[-8, -3], [8, -3]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[-5.0, 2.0]]), (None, [[1.0, 2.0]]), (None, [[-2.502582, -2.988995]]), (None, [[-1.489674, -2.989504]]), (None, [[5.513383, -2.968274]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
