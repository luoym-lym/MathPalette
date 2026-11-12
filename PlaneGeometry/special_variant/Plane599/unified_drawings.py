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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane599_C01.png'
    with Canvas(PLANE, xlim=(-0.57, 8.57), ylim=(-3.392, 5.748), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.6666666666666666, 0.0], [2.0, 0.6666666666666666], [1.3333333333333333, 2.0], [0.6666666666666666, 0.0]], [1, 2, 2, 79], id='I_shade_4', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('I_cut_1', [[0.6666666666666666, 0.0], [2.0, 0.6666666666666666]]), ('I_cut_2', [[2.0, 0.6666666666666666], [1.3333333333333333, 2.0]]), ('I_cut_3', [[1.3333333333333333, 2.0], [0.0, 1.3333333333333333]]), ('I_cut_4', [[0.0, 1.3333333333333333], [0.6666666666666666, 0.0]])]:
            c.line(points, id=object_id, color='#DC2626')
        c.line([[0.6666666666666666, 0.0], [1.3333333333333333, 2.0]], id='I_cut_5')
        c.path([[3.0, 1.3333333333333333], [4.333333333333333, 2.0], [3.0, 2.0], [3.0, 1.3333333333333333]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[3.6666666666666665, 0.0], [5.0, 0.0], [5.0, 0.6666666666666666], [3.6666666666666665, 0.0]], [1, 2, 2, 79], id='II_shade_3', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]])]:
            c.line(points, id=object_id)
        for object_id, points in [('II_cut_1', [[3.6666666666666665, 0.0], [5.0, 0.6666666666666666]]), ('II_cut_2', [[5.0, 0.6666666666666666], [4.333333333333333, 2.0]]), ('II_cut_3', [[4.333333333333333, 2.0], [3.0, 1.3333333333333333]]), ('II_cut_4', [[3.0, 1.3333333333333333], [3.6666666666666665, 0.0]])]:
            c.line(points, id=object_id, color='#DC2626')
        c.path([[6.666666666666667, 0.0], [8.0, 0.0], [8.0, 1.3333333333333333], [6.666666666666667, 0.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]])]:
            c.line(points, id=object_id, color='#DC2626')
        c.line([[6.666666666666667, 0.0], [8.0, 1.3333333333333333]], id='III_cut_1')
        c.text('I', (1.0, 2.58), id='I_panel_label', clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        c.text('P', (0.6666666666666666, 0.0), id='I_label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=False)
        c.text('Q', (2.0, 0.6666666666666666), id='I_label_Q', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=False)
        c.text('R', (1.3333333333333333, 2.0), id='I_label_R', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 15), annotation_clip=False)
        c.text('S', (0.0, 1.3333333333333333), id='I_label_S', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 0), annotation_clip=False)
        c.text('II', (4.0, 2.58), id='II_panel_label', clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        c.text('P', (3.6666666666666665, 0.0), id='II_label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=False)
        c.text('Q', (5.0, 0.6666666666666666), id='II_label_Q', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=False)
        c.text('R', (4.333333333333333, 2.0), id='II_label_R', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 15), annotation_clip=False)
        c.text('S', (3.0, 1.3333333333333333), id='II_label_S', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-13, 0), annotation_clip=False)
        c.text('III', (7.0, 2.58), id='III_panel_label', clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        c.text('U', (6.666666666666667, 0.0), id='III_label_U', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -15), annotation_clip=False)
        c.text('V', (8.0, 1.3333333333333333), id='III_label_V', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(13, 0), annotation_clip=False)
        c.line([[6.666666666666667, 0.0], [8.0, 2.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
