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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane120_C01.png'
    with Canvas(PLANE, xlim=(-4.6457628047975135, 4.61567021220492), ylim=(-5.00564200460506, 4.255791012397373), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_00', [[-4.0, -2.0], [-2.8, -0.3]]), ('edge_01', [[-2.8, -0.3], [-0.8, -0.3]]), ('edge_02', [[-0.8, -0.3], [0.2, 1.6]]), ('edge_03', [[0.2, 1.6], [2.1, 1.6]]), ('edge_04', [[2.1, 1.6], [2.1, -0.9]]), ('edge_05', [[2.1, -0.9], [4.0, -0.9]])]:
            c.line(points, id=object_id)
        c.text('P', (-4.0, -2.0), id='label_P', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18.0, -16.0), annotation_clip=None)
        c.text('Q', (4.0, -0.9), id='label_Q', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.0, 13.0), annotation_clip=None)
        for object_id, points in [(None, [[-2.8, -0.3]]), (None, [[-0.8, -0.3]]), (None, [[0.2, 1.6]]), (None, [[2.1, 1.6]]), (None, [[2.1, -0.9]]), (None, [[1.1500000000000001, 1.6]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)
