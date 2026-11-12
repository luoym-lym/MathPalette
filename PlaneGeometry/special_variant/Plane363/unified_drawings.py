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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane363_C01.png'
    with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dotP00', [[0.0, 0.0]]), ('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
            c.point(points, id=object_id)
        for object_id, points in [(None, [[0, 2], [2, 2]]), (None, [[2, 2], [2, 0]]), (None, [[2, 0], [0, 0]]), (None, [[0, 0], [0, 2]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        for object_id, points in [(None, [[1.0, 2.0]]), (None, [[0.0, 1.0]]), (None, [[1.0, 0.0]]), (None, [[2.0, 1.0]]), (None, [[1.0, 1.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane363_C02.png'
    with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dotP00', [[0.0, 0.0]]), ('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
            c.point(points, id=object_id)
        c.line([[0, 2], [2, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1, 0], [1, 2]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane363_C03.png'
    with Canvas(PLANE, xlim=(-0.06345872833283672, 2.066791119596469), ylim=(-0.06679111959646866, 2.063458728332837), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('dotP00', [[0.0, 0.0]]), ('dotP01', [[0.0, 1.0]]), ('dotP02', [[0.0, 2.0]]), ('dotP10', [[1.0, 0.0]]), ('dotP11', [[1.0, 1.0]]), ('dotP12', [[1.0, 2.0]]), ('dotP20', [[2.0, 0.0]]), ('dotP21', [[2.0, 1.0]]), ('dotP22', [[2.0, 2.0]])]:
            c.point(points, id=object_id)
        for object_id, points in [(None, [[0.0, 1.0]]), (None, [[1.0, 2.0]]), (None, [[2.0, 1.0]]), (None, [[1.0, 0.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        for object_id, points in [(None, [[0, 2], [2, 2]]), (None, [[2, 2], [2, 0]]), (None, [[2, 0], [0, 0]]), (None, [[0, 0], [0, 2]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
