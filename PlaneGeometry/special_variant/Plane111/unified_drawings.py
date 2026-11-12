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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C01.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C02.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C03.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C04.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.7478381048599623, -0.08695952621499062]]), (None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C05.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C06.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[1.3851042190181628, -1.0695729533127138]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C07(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C07.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.5831322225070208, 0.7457830556267552]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C08(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane111_C08.png'
    with Canvas(PLANE, xlim=(-2.8255813953488373, 2.8255813953488373), ylim=(-2.9255813953488374, 2.7255813953488373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.circle([0.0, 0.0], 1.75, id='circle', fill=False)
        c.line([[-2.7, -0.32500000000000007], [2.7, 1.025]], id='line_a')
        c.line([[-2.7, 1.7899999999999998], [2.7, -1.99]], id='line_b')
        for object_id, points in [(None, [[-1.4790639505617877, 0.9353447653932512]]), (None, [[-0.47368421052631593, 0.231578947368421]]), (None, [[1.3851042190181628, -1.0695729533127138]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
