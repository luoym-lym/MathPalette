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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane462_C01.png'
    _geometry_01 = [('p00', [[0.0, 0.0]]),
     ('p01', [[0.0, 1.0]]),
     ('p02', [[0.0, 2.0]]),
     ('p03', [[0.0, 3.0]]),
     ('p04', [[0.0, 4.0]]),
     ('p10', [[1.0, 0.0]]),
     ('p11', [[1.0, 1.0]]),
     ('p12', [[1.0, 2.0]]),
     ('p13', [[1.0, 3.0]]),
     ('p14', [[1.0, 4.0]]),
     ('p20', [[2.0, 0.0]]),
     ('p21', [[2.0, 1.0]]),
     ('p22', [[2.0, 2.0]]),
     ('p23', [[2.0, 3.0]]),
     ('p24', [[2.0, 4.0]]),
     ('p30', [[3.0, 0.0]]),
     ('p31', [[3.0, 1.0]]),
     ('p32', [[3.0, 2.0]]),
     ('p33', [[3.0, 3.0]]),
     ('p34', [[3.0, 4.0]]),
     ('p40', [[4.0, 0.0]]),
     ('p41', [[4.0, 1.0]]),
     ('p42', [[4.0, 2.0]]),
     ('p43', [[4.0, 3.0]]),
     ('p44', [[4.0, 4.0]])]
    with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-0.13358223919293732, 4.126917456665674), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.point(points, id=object_id)
        c.path([[0.0, 4.0], [1.0, 3.0], [1.0, 2.0], [0.0, 3.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='I', capstyle='butt')
        c.path([[2.0, 1.0], [4.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='II', capstyle='butt')
        c.text('I', (0.55, 2.95), id='nameI', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('II', (2.65, 0.95), id='nameII', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        for object_id, points in [(None, [[2, 2], [4, 2]]), (None, [[4, 2], [4, 0]]), (None, [[4, 0], [2, 0]]), (None, [[2, 0], [2, 2]])]:
            c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane462_C02.png'
    _geometry_01 = [('p00', [[0.0, 0.0]]),
     ('p01', [[0.0, 1.0]]),
     ('p02', [[0.0, 2.0]]),
     ('p03', [[0.0, 3.0]]),
     ('p04', [[0.0, 4.0]]),
     ('p10', [[1.0, 0.0]]),
     ('p11', [[1.0, 1.0]]),
     ('p12', [[1.0, 2.0]]),
     ('p13', [[1.0, 3.0]]),
     ('p14', [[1.0, 4.0]]),
     ('p20', [[2.0, 0.0]]),
     ('p21', [[2.0, 1.0]]),
     ('p22', [[2.0, 2.0]]),
     ('p23', [[2.0, 3.0]]),
     ('p24', [[2.0, 4.0]]),
     ('p30', [[3.0, 0.0]]),
     ('p31', [[3.0, 1.0]]),
     ('p32', [[3.0, 2.0]]),
     ('p33', [[3.0, 3.0]]),
     ('p34', [[3.0, 4.0]]),
     ('p40', [[4.0, 0.0]]),
     ('p41', [[4.0, 1.0]]),
     ('p42', [[4.0, 2.0]]),
     ('p43', [[4.0, 3.0]]),
     ('p44', [[4.0, 4.0]])]
    with Canvas(PLANE, xlim=(-0.12691745666567344, 4.133582239192938), ylim=(-0.13358223919293732, 4.126917456665674), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in _geometry_01:
            c.point(points, id=object_id)
        c.path([[0.0, 4.0], [1.0, 3.0], [1.0, 2.0], [0.0, 3.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='I', capstyle='butt')
        c.path([[2.0, 1.0], [4.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='II', capstyle='butt')
        c.text('I', (0.55, 2.95), id='nameI', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.text('II', (2.65, 0.95), id='nameII', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[2, 2], [4, 2]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[2, 2], [2, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
