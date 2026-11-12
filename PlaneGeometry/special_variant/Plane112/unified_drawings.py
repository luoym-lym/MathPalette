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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C01.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C02.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C03.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C04.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C05.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C06.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C07(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C07.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]]), (None, [[0.7000000000000001, 0.25]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C08(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane112_C08.png'
    with Canvas(PLANE, xlim=(-3.1395348837209305, 3.1395348837209305), ylim=(-2.9395348837209303, 3.3395348837209307), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([-0.9, 0.25], 1.6, id='left_circle', fill=False)
        c.circle([1.0, 0.05], 1.5, id='right_circle', fill=False)
        c.line([[-3.0, -1.08], [3.0, -0.12]], id='line')
        for object_id, points in [(None, [[-1.9926368849521967, -0.9188219015923516]]), (None, [[-0.3255463966993375, -0.6520874234718941]]), (None, [[0.0030760337958954387, -1.0707776789389936]]), (None, [[0.25829382921780325, 1.3537913775691304]]), (None, [[0.5027772905684218, -0.5195556335090525]]), (None, [[2.4784325121439554, -0.20345079805696709]]), (None, [[-0.8999999999999999, 1.85]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)
