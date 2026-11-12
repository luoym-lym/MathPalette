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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane425_C01.png'
    with Canvas(PLANE, xlim=(-0.14831072575800563, 6.159906313357347), ylim=(-0.8104426647939471, 5.497774374321405), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('o1', [[1.0, 0.2], [1.0, 4.4]]), ('o2', [[2.0, 0.2], [2.0, 4.4]]), ('o3', [[3.0, 0.2], [3.0, 4.4]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]])]:
            c.line(points, id=object_id, color='#AAAAAA')
        c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
        c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
        for object_id, points in [('o15', [[3.0, 4.0]]), ('o16', [[2.0, 3.0]]), ('o17', [[1.0, 1.0]]), ('o18', [[2.0, 1.0]])]:
            c.point(points, id=object_id)
        c.text('W', (3.0, 4.0), id='label_X0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, 31.54104465353544), annotation_clip=None)
        c.text('V', (2.0, 3.0), id='label_Y1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(27.598414071843493, 31.541044653535405), annotation_clip=None)
        c.text('T', (1.0, 1.0), id='label_Z2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-39.42630581691927, -43.3689363986112), annotation_clip=None)
        c.text('U', (2.0, 1.0), id='label_T3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, -43.3689363986112), annotation_clip=None)
        c.line([[1, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[2.0, 1.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane425_C02.png'
    with Canvas(PLANE, xlim=(-0.14831072575800563, 6.159906313357347), ylim=(-0.8104426647939471, 5.497774374321405), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('o1', [[1.0, 0.2], [1.0, 4.4]]), ('o2', [[2.0, 0.2], [2.0, 4.4]]), ('o3', [[3.0, 0.2], [3.0, 4.4]]), ('o8', [[0.0, 1.0], [6.0, 1.0]]), ('o9', [[0.0, 2.0], [6.0, 2.0]]), ('o10', [[0.0, 3.0], [6.0, 3.0]]), ('o11', [[0.0, 4.0], [6.0, 4.0]])]:
            c.line(points, id=object_id, color='#AAAAAA')
        c.line([[1.0, 2.0], [1.0, 4.0]], id='o13')
        c.line([[3.0, 2.0], [5.0, 2.0]], id='o14')
        for object_id, points in [('o15', [[3.0, 4.0]]), ('o16', [[2.0, 3.0]]), ('o17', [[1.0, 1.0]]), ('o18', [[2.0, 1.0]])]:
            c.point(points, id=object_id)
        c.text('W', (3.0, 4.0), id='label_X0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, 31.54104465353544), annotation_clip=None)
        c.text('V', (2.0, 3.0), id='label_Y1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(27.598414071843493, 31.541044653535405), annotation_clip=None)
        c.text('T', (1.0, 1.0), id='label_Z2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-39.42630581691927, -43.3689363986112), annotation_clip=None)
        c.text('U', (2.0, 1.0), id='label_T3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(31.541044653535405, -43.3689363986112), annotation_clip=None)
        c.line([[1, 4], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[5, 2], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
