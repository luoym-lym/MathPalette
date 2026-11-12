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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane598_C01.png'
    with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('I_shade_1', [[0.0, 0.6666666666666666], [0.6666666666666666, 0.6666666666666666], [0.6666666666666666, 1.3333333333333333], [0.0, 1.3333333333333333], [0.0, 0.6666666666666666]], [1, 2, 2, 2, 79]), ('I_shade_3', [[0.6666666666666666, 0.0], [1.3333333333333333, 0.0], [1.3333333333333333, 0.6666666666666666], [0.6666666666666666, 0.6666666666666666], [0.6666666666666666, 0.0]], [1, 2, 2, 2, 79]), ('I_shade_4', [[0.6666666666666666, 0.6666666666666666], [1.3333333333333333, 0.6666666666666666], [1.3333333333333333, 1.3333333333333333], [0.6666666666666666, 1.3333333333333333], [0.6666666666666666, 0.6666666666666666]], [1, 2, 2, 2, 79]), ('I_shade_5', [[0.6666666666666666, 1.3333333333333333], [1.3333333333333333, 1.3333333333333333], [1.3333333333333333, 2.0], [0.6666666666666666, 2.0], [0.6666666666666666, 1.3333333333333333]], [1, 2, 2, 2, 79]), ('I_shade_7', [[1.3333333333333333, 0.6666666666666666], [2.0, 0.6666666666666666], [2.0, 1.3333333333333333], [1.3333333333333333, 1.3333333333333333], [1.3333333333333333, 0.6666666666666666]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]])]:
            c.line(points, id=object_id)
        c.line([[0.6666666666666666, 0.0], [0.6666666666666666, 2.0]], id='I_cut_1', color='#DC2626')
        c.line([[1.3333333333333333, 0.0], [1.3333333333333333, 2.0]], id='I_cut_2', color='#DC2626')
        c.line([[0.0, 0.6666666666666666], [2.0, 0.6666666666666666]], id='I_cut_3', color='#2563EB')
        c.line([[0.0, 1.3333333333333333], [2.0, 1.3333333333333333]], id='I_cut_4', color='#2563EB')
        c.path([[3.0, 0.0], [3.6666666666666665, 0.0], [5.0, 1.3333333333333333], [5.0, 2.0], [4.333333333333333, 2.0], [3.0, 0.6666666666666666], [3.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='II_shade_0', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.6666666666666666], [4.333333333333333, 2.0]]), ('II_cut_2', [[3.6666666666666665, 0.0], [5.0, 1.3333333333333333]])]:
            c.line(points, id=object_id)
        c.path([[6.333333333333333, 1.0], [7.0, 0.3333333333333333], [7.666666666666667, 1.0], [7.0, 1.6666666666666667], [6.333333333333333, 1.0]], [1, 2, 2, 2, 79], id='III_shade_3', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 0.6666666666666666], [7.333333333333333, 2.0]]), ('III_cut_2', [[6.666666666666667, 0.0], [8.0, 1.3333333333333333]]), ('III_cut_3', [[6.666666666666667, 2.0], [8.0, 0.6666666666666666]]), ('III_cut_4', [[6.0, 1.3333333333333333], [7.333333333333333, 0.0]])]:
            c.line(points, id=object_id)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        for object_id, points in [(None, [[6, 1], [7, 2]]), (None, [[7, 2], [8, 1]]), (None, [[8, 1], [7, 0]]), (None, [[7, 0], [6, 1]])]:
            c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.point([[7.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[7.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[6, 1], [8, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
