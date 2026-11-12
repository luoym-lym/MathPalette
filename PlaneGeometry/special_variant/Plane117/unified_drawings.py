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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane117_C01.png'
    with Canvas(PLANE, xlim=(0.047923313001905665, 6.768743353664762), ylim=(-0.13818779810920567, 6.58263224255365), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.5, 4.2], [3.0, 5.45]], id='PQ', color='#16A34A', linewidth=3.0)
        c.line([[6.3, 1.0], [6.3, 4.6]], id='OA', color='#16A34A', linewidth=3.0)
        c.line([[6.3, 1.0], [3.754415587728429, 3.545584412271571]], id='OB')
        c.line([[6.3, 1.0], [4.690031056200151, 4.219937887599697]], id='OC')
        for object_id, points in [('P_dot', [[0.5, 4.2]]), ('Q_dot', [[3.0, 5.45]]), ('O_dot', [[6.3, 1.0]]), ('A_dot', [[6.3, 4.6]]), ('B_dot', [[3.754415587728429, 3.545584412271571]]), ('C_dot', [[4.690031056200151, 4.219937887599697]])]:
            c.point(points, id=object_id)
        c.text('P', (0.5, 4.2), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-12, -13), annotation_clip=None)
        c.text('Q', (3.0, 5.45), id='Q_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, 10), annotation_clip=None)
        c.text('O', (6.3, 1.0), id='O_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, -14), annotation_clip=None)
        c.text('A', (6.3, 4.6), id='A_label', fontsize=18.0, fontstyle='italic', va='bottom', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
        c.text('B', (3.754415587728429, 3.545584412271571), id='B_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-12, 9), annotation_clip=None)
        c.text('C', (4.690031056200151, 4.219937887599697), id='C_label', fontsize=18.0, fontstyle='italic', va='bottom', rotation_mode='default', offset_pt=(3, 13), annotation_clip=None)
        return c.save(output_path)
