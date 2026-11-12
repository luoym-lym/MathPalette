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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid101_C01.png'
    with Canvas(SOLID, xlim=(-0.7664851963866655, 10.48268553553395), ylim=(-5.156434602436827, 6.092736129483789), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('die0e0', [[0.0, 0.0], [1.0, 0.18]]), ('die0e1', [[0.0, 1.0], [1.0, 1.18]]), ('die0e2', [[-0.5, 1.3], [0.5, 1.48]]), ('die0e3', [[0.0, 0.0], [-0.5, 0.3]]), ('die0e4', [[0.0, 1.0], [-0.5, 1.3]]), ('die0e5', [[1.0, 1.18], [0.5, 1.48]]), ('die0e6', [[0.0, 0.0], [0.0, 1.0]]), ('die0e7', [[-0.5, 0.3], [-0.5, 1.3]]), ('die0e8', [[1.0, 0.18], [1.0, 1.18]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('die0toppip0', [[-0.125, 1.27]]), ('die0toppip1', [[0.625, 1.21]]), ('die0frontpip0', [[0.5, 0.59]])]:
            c.line(points, id=object_id, zorder=4, linestyle='none', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black', simplify=False)
        for object_id, points in [('die1e0', [[2.3, 0.0], [3.3, 0.18]]), ('die1e1', [[2.3, 1.0], [3.3, 1.1800000000000002]]), ('die1e2', [[1.7999999999999998, 1.3], [2.8, 1.48]]), ('die1e3', [[2.3, 0.0], [1.7999999999999998, 0.3]]), ('die1e4', [[2.3, 1.0], [1.7999999999999998, 1.3]]), ('die1e5', [[3.3, 1.1800000000000002], [2.8, 1.48]]), ('die1e6', [[2.3, 0.0], [2.3, 1.0]]), ('die1e7', [[1.7999999999999998, 0.3], [1.7999999999999998, 1.3]]), ('die1e8', [[3.3, 0.18], [3.3, 1.1800000000000002]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('die1toppip0', [[2.55, 1.2400000000000002]]), ('die1leftpip0', [[2.05, 0.6499999999999999]]), ('die1frontpip0', [[2.8, 0.5900000000000001]])]:
            c.line(points, id=object_id, zorder=4, linestyle='none', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black', simplify=False)
        for object_id, points in [('die2e0', [[4.6, 0.0], [5.6, 0.18000000000000005]]), ('die2e1', [[4.6, 1.0], [5.6, 1.1800000000000002]]), ('die2e2', [[4.1, 1.2999999999999998], [5.1, 1.48]]), ('die2e3', [[4.6, 0.0], [4.1, 0.29999999999999993]]), ('die2e4', [[4.6, 1.0], [4.1, 1.2999999999999998]]), ('die2e5', [[5.6, 1.1800000000000002], [5.1, 1.48]]), ('die2e6', [[4.6, 0.0], [4.6, 1.0]]), ('die2e7', [[4.1, 0.29999999999999993], [4.1, 1.2999999999999998]]), ('die2e8', [[5.6, 0.18000000000000005], [5.6, 1.1800000000000002]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('die2toppip0', [[4.55, 1.186]]), ('die2toppip1', [[4.85, 1.2399999999999998]]), ('die2toppip2', [[5.1499999999999995, 1.294]]), ('die2leftpip0', [[4.35, 0.65]]), ('die2frontpip0', [[4.85, 0.29499999999999993]]), ('die2frontpip1', [[5.1, 0.59]]), ('die2frontpip2', [[5.35, 0.8849999999999999]])]:
            c.line(points, id=object_id, zorder=4, linestyle='none', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black', simplify=False)
        c.line([[6.8999999999999995, 0.0], [7.8999999999999995, 0.18000000000000016]], id='die3e0', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[6.8999999999999995, 1.0], [7.8999999999999995, 1.1800000000000002]], id='die3e1', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[6.3999999999999995, 1.3], [7.3999999999999995, 1.4800000000000002]], id='die3e2', zorder=3, clip_on=False, simplify=False)
        c.line([[6.8999999999999995, 0.0], [6.3999999999999995, 0.30000000000000004]], id='die3e3', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[6.8999999999999995, 1.0], [6.3999999999999995, 1.3]], id='die3e4', zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        c.line([[7.8999999999999995, 1.1800000000000002], [7.3999999999999995, 1.4800000000000002]], id='die3e5', zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('die3e6', [[6.8999999999999995, 0.0], [6.8999999999999995, 1.0]]), ('die3e7', [[6.3999999999999995, 0.30000000000000004], [6.3999999999999995, 1.3]]), ('die3e8', [[7.8999999999999995, 0.18000000000000016], [7.8999999999999995, 1.1800000000000002]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, color='#DC2626', linewidth=1.5, solid_capstyle='butt', simplify=False)
        for object_id, points in [('die3toppip0', [[6.85, 1.186]]), ('die3toppip1', [[7.1499999999999995, 1.24]]), ('die3toppip2', [[7.449999999999999, 1.294]]), ('die3leftpip0', [[6.7749999999999995, 0.825]]), ('die3leftpip1', [[6.5249999999999995, 0.47499999999999987]])]:
            c.line(points, id=object_id, zorder=4, linestyle='none', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black', simplify=False)
        for object_id, points in [('die4e0', [[9.2, 0.0], [10.2, 0.17999999999999994]]), ('die4e1', [[9.2, 1.0], [10.2, 1.18]]), ('die4e2', [[8.7, 1.3], [9.7, 1.4799999999999998]]), ('die4e3', [[9.2, 0.0], [8.7, 0.30000000000000004]]), ('die4e4', [[9.2, 1.0], [8.7, 1.3]]), ('die4e5', [[10.2, 1.18], [9.7, 1.4799999999999998]]), ('die4e6', [[9.2, 0.0], [9.2, 1.0]]), ('die4e7', [[8.7, 0.30000000000000004], [8.7, 1.3]]), ('die4e8', [[10.2, 0.17999999999999994], [10.2, 1.18]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False, simplify=False)
        for object_id, points in [('die4toppip0', [[9.45, 1.2399999999999998]]), ('die4leftpip0', [[9.075, 0.825]]), ('die4leftpip1', [[8.825, 0.47499999999999987]]), ('die0leftpip0', [[-0.125, 0.825]]), ('die0leftpip1', [[-0.25, 0.65]]), ('die0leftpip2', [[-0.375, 0.475]]), ('die3frontpip0', [[7.1499999999999995, 0.29500000000000015]]), ('die3frontpip1', [[7.6499999999999995, 0.885]]), ('die4frontpip0', [[9.45, 0.29499999999999993]]), ('die4frontpip1', [[9.95, 0.8849999999999998]])]:
            c.line(points, id=object_id, zorder=4, linestyle='none', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black', simplify=False)
        for object_id, text, anchor in [('option0', '(A)', (0.2, 0.036)), ('option1', '(B)', (2.5, 0.035999999999999976)), ('option2', '(C)', (4.8, 0.03600000000000003)), ('option3', '(D)', (7.1, 0.03600000000000003)), ('option4', '(E)', (9.399999999999999, 0.03599999999999981))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -20), annotation_clip=None)
        return c.save(output_path)
