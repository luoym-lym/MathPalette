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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane370_C01.png'
    with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
            c.line(points, id=object_id)
        c.point([[0.0, 2.0]], id='start')
        c.point([[4.0, 0.0]], id='end')
        c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
        c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
        c.line([[0, 2], [4, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane370_C02.png'
    with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
            c.line(points, id=object_id)
        c.point([[0.0, 2.0]], id='start')
        c.point([[4.0, 0.0]], id='end')
        c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
        c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
        c.line([[0.0, 2.0], [4.0, 0.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0.0, 2.0], [1.0, 1.0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane370_C03.png'
    with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-1.1269223016330092, 3.1335773942256018), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('gv0', [[0.0, 0.0], [0.0, 2.0]]), ('gv1', [[1.0, 0.0], [1.0, 2.0]]), ('gv2', [[2.0, 0.0], [2.0, 2.0]]), ('gv3', [[3.0, 0.0], [3.0, 2.0]]), ('gv4', [[4.0, 0.0], [4.0, 2.0]]), ('gh0', [[0.0, 0.0], [4.0, 0.0]]), ('gh1', [[0.0, 1.0], [4.0, 1.0]]), ('gh2', [[0.0, 2.0], [4.0, 2.0]])]:
            c.line(points, id=object_id)
        c.point([[0.0, 2.0]], id='start')
        c.point([[4.0, 0.0]], id='end')
        c.text('Start', (0.0, 2.0), id='startname', rotation_mode='default', offset_pt=(17, 18), annotation_clip=None)
        c.text('Ziel', (4.0, 0.0), id='zielname', rotation_mode='default', offset_pt=(-10, -20), annotation_clip=None)
        c.line([[0, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[2, 1], [4, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
