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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane222_C01.png'
    with Canvas(PLANE, xlim=(-0.3529121469228489, 14.357558491926058), ylim=(-2.8562693387459355, 11.854201300102972), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 9.0], [2.0, 9.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='square', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 9.0], [2.0, 9.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='square', capstyle='butt', fill=False)
        c.line([[3.0, 7.0], [3.0, 9.0]], id='squaregrid0_1_0')
        c.line([[2.0, 8.0], [4.0, 8.0]], id='squaregrid1_1_0')
        c.path([[6.0, 7.0], [12.0, 7.0], [10.0, 9.0], [8.0, 9.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='trapezoid', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[6.0, 7.0], [12.0, 7.0], [10.0, 9.0], [8.0, 9.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='trapezoid', capstyle='butt', fill=False)
        for object_id, points in [('trapezoidgrid0_1_0', [[7.0, 7.0], [7.0, 8.0]]), ('trapezoidgrid0_2_0', [[8.0, 7.0], [8.0, 9.0]]), ('trapezoidgrid0_3_0', [[9.0, 7.0], [9.0, 9.0]]), ('trapezoidgrid0_4_0', [[10.0, 7.0], [10.0, 9.0]]), ('trapezoidgrid0_5_0', [[11.0, 7.0], [11.0, 8.0]]), ('trapezoidgrid1_1_0', [[7.0, 8.0], [11.0, 8.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 2.0], [4.0, 2.0], [4.0, 4.0], [10.0, 4.0], [10.0, 2.0], [14.0, 2.0], [12.0, 0.0], [2.0, 0.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='boat', capstyle='butt')
        for object_id, points in [('boatgrid0_1_0', [[1.0, 1.0], [1.0, 2.0]]), ('boatgrid0_2_0', [[2.0, 0.0], [2.0, 2.0]]), ('boatgrid0_3_0', [[3.0, 0.0], [3.0, 2.0]]), ('boatgrid0_4_0', [[4.0, 0.0], [4.0, 4.0]]), ('boatgrid0_5_0', [[5.0, 0.0], [5.0, 4.0]]), ('boatgrid0_6_0', [[6.0, 0.0], [6.0, 4.0]]), ('boatgrid0_7_0', [[7.0, 0.0], [7.0, 4.0]]), ('boatgrid0_8_0', [[8.0, 0.0], [8.0, 4.0]]), ('boatgrid0_9_0', [[9.0, 0.0], [9.0, 4.0]]), ('boatgrid0_10_0', [[10.0, 0.0], [10.0, 2.0]]), ('boatgrid0_11_0', [[11.0, 0.0], [11.0, 2.0]]), ('boatgrid0_12_0', [[12.0, 0.0], [12.0, 2.0]]), ('boatgrid0_13_0', [[13.0, 1.0], [13.0, 2.0]]), ('boatgrid1_1_0', [[1.0, 1.0], [13.0, 1.0]]), ('boatgrid1_2_0', [[4.0, 2.0], [10.0, 2.0]]), ('boatgrid1_3_0', [[4.0, 3.0], [10.0, 3.0]])]:
            c.line(points, id=object_id)
        c.text('and', (5.2, 7.6), id='label0', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        for object_id, points in [(None, [[5.019294042264619, 2.9966711850444376]]), (None, [[9.00037525069493, 3.0116941330007787]]), (None, [[7.017346120457944, 2.9966711850444376]]), (None, [[3.006219016114953, 0.9986191068511108]]), (None, [[10.998427328888255, 1.0286650027637947]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane222_C02.png'
    with Canvas(PLANE, xlim=(-0.3529121469228489, 14.357558491926058), ylim=(-2.8562693387459355, 11.854201300102972), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 9.0], [2.0, 9.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='square', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[2.0, 7.0], [4.0, 7.0], [4.0, 9.0], [2.0, 9.0], [2.0, 7.0]], [1, 2, 2, 2, 79], id='square', capstyle='butt', fill=False)
        c.line([[3.0, 7.0], [3.0, 9.0]], id='squaregrid0_1_0')
        c.line([[2.0, 8.0], [4.0, 8.0]], id='squaregrid1_1_0')
        c.path([[6.0, 7.0], [12.0, 7.0], [10.0, 9.0], [8.0, 9.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='trapezoid', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        c.path([[6.0, 7.0], [12.0, 7.0], [10.0, 9.0], [8.0, 9.0], [6.0, 7.0]], [1, 2, 2, 2, 79], id='trapezoid', capstyle='butt', fill=False)
        for object_id, points in [('trapezoidgrid0_1_0', [[7.0, 7.0], [7.0, 8.0]]), ('trapezoidgrid0_2_0', [[8.0, 7.0], [8.0, 9.0]]), ('trapezoidgrid0_3_0', [[9.0, 7.0], [9.0, 9.0]]), ('trapezoidgrid0_4_0', [[10.0, 7.0], [10.0, 9.0]]), ('trapezoidgrid0_5_0', [[11.0, 7.0], [11.0, 8.0]]), ('trapezoidgrid1_1_0', [[7.0, 8.0], [11.0, 8.0]])]:
            c.line(points, id=object_id)
        c.path([[0.0, 2.0], [4.0, 2.0], [4.0, 4.0], [10.0, 4.0], [10.0, 2.0], [14.0, 2.0], [12.0, 0.0], [2.0, 0.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='boat', capstyle='butt')
        for object_id, points in [('boatgrid0_1_0', [[1.0, 1.0], [1.0, 2.0]]), ('boatgrid0_2_0', [[2.0, 0.0], [2.0, 2.0]]), ('boatgrid0_3_0', [[3.0, 0.0], [3.0, 2.0]]), ('boatgrid0_4_0', [[4.0, 0.0], [4.0, 4.0]]), ('boatgrid0_5_0', [[5.0, 0.0], [5.0, 4.0]]), ('boatgrid0_6_0', [[6.0, 0.0], [6.0, 4.0]]), ('boatgrid0_7_0', [[7.0, 0.0], [7.0, 4.0]]), ('boatgrid0_8_0', [[8.0, 0.0], [8.0, 4.0]]), ('boatgrid0_9_0', [[9.0, 0.0], [9.0, 4.0]]), ('boatgrid0_10_0', [[10.0, 0.0], [10.0, 2.0]]), ('boatgrid0_11_0', [[11.0, 0.0], [11.0, 2.0]]), ('boatgrid0_12_0', [[12.0, 0.0], [12.0, 2.0]]), ('boatgrid0_13_0', [[13.0, 1.0], [13.0, 2.0]]), ('boatgrid1_1_0', [[1.0, 1.0], [13.0, 1.0]]), ('boatgrid1_2_0', [[4.0, 2.0], [10.0, 2.0]]), ('boatgrid1_3_0', [[4.0, 3.0], [10.0, 3.0]])]:
            c.line(points, id=object_id)
        c.text('and', (5.2, 7.6), id='label0', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        for object_id, points in [(None, [[5.019294042264619, 3.0116941330007787]]), (None, [[7.032369068414285, 3.0116941330007787]]), (None, [[9.015398198651269, 2.9816482370880966]]), (None, [[2.044750346909142, 0.9986191068511108]]), (None, [[12.019987789919428, 0.9835961588947715]]), (None, [[3.997733581233445, 1.058710898676475]]), (None, [[7.017346120457944, 1.0136420548074536]]), (None, [[10.006912763769762, 0.9685732109384304]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
