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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C01.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C02.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C03.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C04.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C05.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        c.point([[0.557108074225981, 1.303963766318224]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[1.9463356638562852, 0.8214801867465081]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C06.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        c.point([[0.15902991149963308, -1.0181588495854723]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[1.9463356638562852, 0.8214801867465081]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C07(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C07.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]]), (None, [[0.85, 0.35]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C08(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane110_C08.png'
    with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
            c.circle(center, radius, id=object_id, fill=False)
        for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]]), (None, [[-0.8499999999999999, 2.05]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        return c.save(output_path)
