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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid69_C01.png'
    with Canvas(SOLID, xlim=(-5.23008677450906, 4.230086774509061), ylim=(-0.9288456473620674, 8.531327901656054), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-2.5, 1.5], [2.0, 0.675], [2.0, 4.675], [-2.5, 5.5], [-2.5, 1.5]], [1, 2, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        for object_id, points in [('edge_BC', [[0.0, 8.0], [-5.0, 3.0]]), ('edge_AB', [[0.0, 0.0], [0.0, 8.0]]), ('edge_AC', [[0.0, 0.0], [-5.0, 3.0]]), ('edge_BD', [[0.0, 8.0], [4.0, 1.35]]), ('edge_AD', [[0.0, 0.0], [4.0, 1.35]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-5.0, 3.0], [4.0, 1.35]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[-2.5, 1.5], [2.0, 0.675]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.0, 0.675], [2.0, 4.675]], id='section_NP', zorder=3, clip_on=False)
        c.line([[2.0, 4.675], [-2.5, 5.5]], id='section_PQ', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[-2.5, 5.5], [-2.5, 1.5]], id='section_QM', zorder=3, clip_on=False)
        c.line([[-2.5, 1.5]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.0, 0.675]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.0, 4.675]], id='midpoint_P', zorder=4, color=(0.17254901960784313, 0.6274509803921569, 0.17254901960784313), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[-2.5, 5.5]], id='midpoint_Q', zorder=4, color=(0.8392156862745098, 0.15294117647058825, 0.1568627450980392), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[0.03136187213643371, 3.7142910026155764]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
