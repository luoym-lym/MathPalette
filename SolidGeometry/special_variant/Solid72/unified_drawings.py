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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid72_C01.png'
    with Canvas(SOLID, xlim=(-7.6668456833941105, 6.0869105355540745), ylim=(-0.9189339495038924, 12.834822269444292), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 8.399999999999999], [-3.0, 1.25], [2.2, 0.8], [0.0, 8.399999999999999]], [1, 2, 2, 79], id='cut_fill', alpha=1.0, zorder=1, edgecolor='none', facecolor=(0.9019607843137255, 0.9019607843137255, 0.9019607843137255, 1.0), capstyle='butt')
        c.line([[-1.5999999999999996, 4.1], [4.4, 1.6]], id='edge_CD', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[-6.0, 2.5], [-1.5999999999999996, 4.1]], id='edge_BC', clip_on=False, linestyle=(0, [4, 3]))
        for object_id, points in [('edge_AB', [[0.0, 0.0], [-6.0, 2.5]]), ('edge_AD', [[0.0, 0.0], [4.4, 1.6]]), ('edge_TU', [[0.0, 8.399999999999999], [-6.0, 10.899999999999999]]), ('edge_UV', [[-6.0, 10.899999999999999], [-1.5999999999999996, 12.5]]), ('edge_VW', [[-1.5999999999999996, 12.5], [4.4, 10.0]]), ('edge_TW', [[0.0, 8.399999999999999], [4.4, 10.0]]), ('edge_BU', [[-6.0, 2.5], [-6.0, 10.899999999999999]]), ('edge_AT', [[0.0, 0.0], [0.0, 8.399999999999999]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.line([[-1.5999999999999996, 4.1], [-1.5999999999999996, 12.5]], id='edge_CV', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[4.4, 1.6], [4.4, 10.0]], id='edge_DW', zorder=3, clip_on=False)
        c.line([[0.0, 8.399999999999999], [-3.0, 1.25]], id='section_TM', zorder=3, clip_on=False)
        c.line([[-3.0, 1.25], [2.2, 0.8]], id='section_MN', clip_on=False, linestyle=(0, [4, 3]))
        c.line([[2.2, 0.8], [0.0, 8.399999999999999]], id='section_NT', zorder=3, clip_on=False)
        c.line([[-3.0, 1.25]], id='midpoint_M', zorder=4, color=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.line([[2.2, 0.8]], id='midpoint_N', zorder=4, color=(1.0, 0.4980392156862745, 0.054901960784313725), linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', va='top', rotation_mode='default', offset_pt=(0, -8), annotation_clip=None)
        c.point([[-3.0, 9.649999999999999]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
