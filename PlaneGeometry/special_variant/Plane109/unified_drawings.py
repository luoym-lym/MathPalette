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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C01.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C02.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C03.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C04.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C05.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[1.5996950765959597, 0.9235843830939964]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C06.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[1.65, 1.3279056191361391]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C07(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C07.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[-3.031000827889699e-16, -0.3220943808638608]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C08(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane109_C08.png'
    with Canvas(PLANE, xlim=(-2.9302325581395348, 2.9302325581395348), ylim=(-2.5982561533555, 3.2622089629235695), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('top', [0.0, 1.3279056191361391], 1.65), ('left', [-1.15, -0.6639528095680696], 1.65), ('right', [1.15, -0.6639528095680696], 1.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[-1.5996950765959597, 0.9235843830939964]]), (None, [[-0.44969507659595975, -0.2596315735259268]]), (None, [[0.0, -1.8471687661879928]]), (None, [[0.0, 0.5192631470518536]]), (None, [[0.44969507659595975, -0.2596315735259268]]), (None, [[1.5996950765959597, 0.9235843830939964]]), (None, [[0.5, -0.6639528095680696]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
