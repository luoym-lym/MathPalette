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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid185_C01.png'
    with Canvas(SOLID, xlim=(-2.0202808012156144, 26.306790067914356), ylim=(-2.2205354345649813, 26.10653543456499), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('cube000_cube100', [[0.0, 0.0], [18.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 18.0]]), ('cube001_cube101', [[0.0, 18.0], [18.0, 18.0]]), ('cube001_cube011', [[0.0, 18.0], [6.3, 24.3]]), ('cube011_cube111', [[6.3, 24.3], [24.3, 24.3]]), ('cube100_cube110', [[18.0, 0.0], [24.3, 6.3]]), ('cube100_cube101', [[18.0, 0.0], [18.0, 18.0]]), ('cube101_cube111', [[18.0, 18.0], [24.3, 24.3]]), ('cube110_cube111', [[24.3, 6.3], [24.3, 24.3]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.path([[18.0, 0.0], [24.3, 6.3], [24.3, 24.3], [18.0, 18.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='rightface', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        for object_id, points in [('route0', [[0.0, 18.0], [0.0, 0.0]]), ('arrow0wing0', [[0.0, 0.0], [-0.4139999999999999, 1.1700000000000002]]), ('arrow0wing1', [[0.0, 0.0], [0.41400000000000003, 1.17]]), ('route1', [[0.0, 0.0], [11.700000000000001, 0.0]]), ('arrow1wing0', [[11.700000000000001, 0.0], [10.530000000000001, -0.41400000000000003]]), ('arrow1wing1', [[11.700000000000001, 0.0], [10.530000000000001, 0.4139999999999999]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[11.700000000000001, 0.0], [11.700000000000001, 18.0]], id='route2', zorder=3, clip_on=False, color='#DC2626')
        for object_id, points in [('arrow2wing0', [[11.700000000000001, 18.0], [12.114000000000003, 16.830000000000002]]), ('arrow2wing1', [[11.700000000000001, 18.0], [11.286000000000001, 16.83]]), ('route3', [[11.700000000000001, 18.0], [18.0, 18.0]]), ('arrow3wing0', [[18.0, 18.0], [16.83, 17.586]]), ('arrow3wing1', [[18.0, 18.0], [16.830000000000002, 18.414]]), ('route4', [[18.0, 18.0], [24.3, 24.3]]), ('arrow4wing0', [[23.796, 23.796], [23.26142727342297, 22.67594285860051]]), ('arrow4wing1', [[23.796, 23.796], [22.67594285860051, 23.26142727342297]]), ('route5', [[24.3, 24.3], [24.3, 6.3]]), ('arrow5wing0', [[24.3, 6.3], [23.886, 7.47]]), ('arrow5wing1', [[24.3, 6.3], [24.714, 7.47]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('X', (0.0, 18.0), id='start', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18, 8), annotation_clip=None)
        c.text('Y', (24.3, 6.3), id='end', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(17, -4), annotation_clip=None)
        return c.save(output_path)
