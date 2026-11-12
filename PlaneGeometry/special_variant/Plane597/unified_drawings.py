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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane597_C01.png'
    with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [2.0, 0.0], [0.6666666666666666, 1.3333333333333333], [0.0, 0.0]], [1, 2, 2, 79], id='I_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[0.0, 0.0], [1.0, 2.0]]), ('I_cut_2', [[2.0, 0.0], [0.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[3.0, 0.0], [5.0, 0.0], [4.333333333333333, 0.6666666666666666], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [5.0, 1.0]]), ('II_cut_2', [[5.0, 0.0], [3.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, 0.0], [6.8, 0.4], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 79], id='III_shade_0', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 0.0], [8.0, 1.0]]), ('III_cut_2', [[6.0, 2.0], [7.0, 0.0]])]:
            c.line(points, id=object_id)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        for object_id, points in [(None, [[0.0, 1.3333333333333333], [2.0, 1.3333333333333333]]), (None, [[3.0, 0.6666666666666666], [5.0, 0.6666666666666666]]), (None, [[6.0, 0.4], [8.0, 0.4]])]:
            c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane597_C02.png'
    with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [2.0, 0.0], [0.6666666666666666, 1.3333333333333333], [0.0, 0.0]], [1, 2, 2, 79], id='I_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[0.0, 0.0], [1.0, 2.0]]), ('I_cut_2', [[2.0, 0.0], [0.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[3.0, 0.0], [5.0, 0.0], [4.333333333333333, 0.6666666666666666], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [5.0, 1.0]]), ('II_cut_2', [[5.0, 0.0], [3.0, 2.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, 0.0], [6.8, 0.4], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 79], id='III_shade_0', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[6.0, -4.440892098500626e-16], [7.0, -4.440892098500626e-16]], [1, 2], id='III_outer_AB', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), joinstyle='round', fill=False)
        c.path([[7.0, -4.440892098500626e-16], [8.0, -4.440892098500626e-16]], [1, 2], id='III_outer_AB', joinstyle='round', fill=False)
        for object_id, points in [('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, -4.440892098500626e-16], [6.8, 0.3999999999999996]], [1, 2], id='III_cut_1', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), joinstyle='round', fill=False)
        c.path([[6.8, 0.3999999999999996], [8.0, 0.9999999999999996]], [1, 2], id='III_cut_1', joinstyle='round', fill=False)
        c.path([[6.0, 1.9999999999999996], [6.800000000000001, 0.39999999999999947]], [1, 2], id='III_cut_2', joinstyle='round', fill=False)
        c.path([[6.800000000000001, 0.39999999999999947], [7.0, -4.440892098500626e-16]], [1, 2], id='III_cut_2', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), joinstyle='round', fill=False)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        return c.save(output_path)
