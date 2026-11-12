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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane114_C01.png'
    with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
        for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane114_C02.png'
    with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
        for object_id, points in [(None, [[-1.5, -0.9013878188659974]]), (None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane114_C03.png'
    with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
        for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane114_C04.png'
    with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
        for object_id, points in [(None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane114_C05.png'
    with Canvas(PLANE, xlim=(-1.8313953488372092, 1.8313953488372092), ylim=(-1.8313953488372092, 1.8313953488372092), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.path([[-1.5, -1.5], [1.5, -1.5], [1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='square', capstyle='butt')
        for object_id, points in [(None, [[-1.5, -0.9013878188659974]]), (None, [[-1.5, 0.9013878188659974]]), (None, [[-0.9013878188659974, -1.5]]), (None, [[-0.9013878188659974, 1.5]]), (None, [[0.9013878188659974, -1.5]]), (None, [[0.9013878188659974, 1.5]]), (None, [[1.5, -0.9013878188659974]]), (None, [[1.5, 0.9013878188659974]]), (None, [[1.75, 0.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
