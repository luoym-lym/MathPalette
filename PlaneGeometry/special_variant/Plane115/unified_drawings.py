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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane115_C01.png'
    with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [3.0, 2.0]], id='PO')
        for object_id, points in [('A_dot', [[6.0, 4.0]]), ('B_dot', [[6.0, 2.7]]), ('C_dot', [[6.0, 5.3]])]:
            c.point(points, id=object_id)
        c.text('P', (0.0, 0.0), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-20, -17), annotation_clip=None)
        c.text('O', (3.0, 2.0), id='O_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -20), annotation_clip=None)
        for object_id, text, anchor in [('A_label', 'A', (6.0, 4.0)), ('B_label', 'B', (6.0, 2.7)), ('C_label', 'C', (6.0, 5.3))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
        c.line([[3.0, 2.0], [6.0, 2.7]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[2.941782804302842, 6.063618784990867], [2.978385416666666, -0.9128391315541187]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane115_C02.png'
    with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [3.0, 2.0]], id='PO')
        for object_id, points in [('A_dot', [[6.0, 4.0]]), ('B_dot', [[6.0, 2.7]]), ('C_dot', [[6.0, 5.3]])]:
            c.point(points, id=object_id)
        c.text('P', (0.0, 0.0), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-20, -17), annotation_clip=None)
        c.text('O', (3.0, 2.0), id='O_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -20), annotation_clip=None)
        for object_id, text, anchor in [('A_label', 'A', (6.0, 4.0)), ('B_label', 'B', (6.0, 2.7)), ('C_label', 'C', (6.0, 5.3))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
        c.line([[3.0, 2.0], [6.0, 5.3]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[1.594806669314093, 6.027016172627042], [1.6314092816779178, -0.7957107719898797]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[4.9256443944221395, 6.027016172627042], [4.991529096677024, -0.8542749517719992]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane115_C03.png'
    with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [3.0, 2.0]], id='PO')
        for object_id, points in [('A_dot', [[6.0, 4.0]]), ('B_dot', [[6.0, 2.7]]), ('C_dot', [[6.0, 5.3]])]:
            c.point(points, id=object_id)
        c.text('P', (0.0, 0.0), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-20, -17), annotation_clip=None)
        c.text('O', (3.0, 2.0), id='O_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -20), annotation_clip=None)
        for object_id, text, anchor in [('A_label', 'A', (6.0, 4.0)), ('B_label', 'B', (6.0, 2.7)), ('C_label', 'C', (6.0, 5.3))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
        c.line([[3.0, 2.0], [6.0, 2.7]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane115_C04.png'
    with Canvas(PLANE, xlim=(-0.6057423859990472, 6.562513219332381), ylim=(-1.0343598046020168, 6.133895800729411), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.line([[0.0, 0.0], [3.0, 2.0]], id='PO')
        for object_id, points in [('A_dot', [[6.0, 4.0]]), ('B_dot', [[6.0, 2.7]]), ('C_dot', [[6.0, 5.3]])]:
            c.point(points, id=object_id)
        c.text('P', (0.0, 0.0), id='P_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-20, -17), annotation_clip=None)
        c.text('O', (3.0, 2.0), id='O_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -20), annotation_clip=None)
        for object_id, text, anchor in [('A_label', 'A', (6.0, 4.0)), ('B_label', 'B', (6.0, 2.7)), ('C_label', 'C', (6.0, 5.3))]:
            c.text(text, anchor, id=object_id, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
        c.line([[3.0, 2.0], [6.0, 5.3]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
