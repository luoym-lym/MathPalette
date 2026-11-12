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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane595_C01.png'
    with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('I_shade_1', [[0.0, 1.0], [0.5, 0.5], [0.5, 1.5], [0.0, 1.0]], [1, 2, 2, 79]), ('I_shade_3', [[0.5, 0.5], [1.0, 0.0], [1.5, 0.5], [0.5, 0.5]], [1, 2, 2, 79]), ('I_shade_5', [[0.5, 1.5], [1.5, 1.5], [1.0, 2.0], [0.5, 1.5]], [1, 2, 2, 79]), ('I_shade_8', [[1.5, 0.5], [2.0, 1.0], [1.5, 1.5], [1.5, 0.5]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[1.0, 0.0], [2.0, 1.0]]), ('I_cut_2', [[2.0, 1.0], [1.0, 2.0]]), ('I_cut_3', [[1.0, 2.0], [0.0, 1.0]]), ('I_cut_4', [[0.0, 1.0], [1.0, 0.0]]), ('I_cut_5', [[1.5, 0.5], [1.5, 1.5]]), ('I_cut_6', [[1.5, 1.5], [0.5, 1.5]]), ('I_cut_7', [[0.5, 1.5], [0.5, 0.5]]), ('I_cut_8', [[0.5, 0.5], [1.5, 0.5]])]:
            c.line(points, id=object_id)
        c.path([[3.0, 0.0], [5.0, 1.0], [4.0, 2.0], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [4.0, 2.0]]), ('II_cut_2', [[4.0, 2.0], [5.0, 1.0]]), ('II_cut_3', [[5.0, 1.0], [3.0, 0.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, 2.0], [7.0, 0.0], [8.0, 2.0], [6.0, 2.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 2.0], [7.0, 0.0]]), ('III_cut_2', [[7.0, 0.0], [8.0, 2.0]])]:
            c.line(points, id=object_id)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        c.line([[0, 1], [2, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 1], [5, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane595_C02.png'
    with Canvas(PLANE, xlim=(-0.205, 8.205), ylim=(-3.027, 5.383), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('I_shade_1', [[0.0, 1.0], [0.5, 0.5], [0.5, 1.5], [0.0, 1.0]], [1, 2, 2, 79]), ('I_shade_3', [[0.5, 0.5], [1.0, 0.0], [1.5, 0.5], [0.5, 0.5]], [1, 2, 2, 79]), ('I_shade_5', [[0.5, 1.5], [1.5, 1.5], [1.0, 2.0], [0.5, 1.5]], [1, 2, 2, 79]), ('I_shade_8', [[1.5, 0.5], [2.0, 1.0], [1.5, 1.5], [1.5, 0.5]], [1, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('I_outer_AB', [[0.0, 0.0], [2.0, 0.0]]), ('I_outer_BC', [[2.0, 0.0], [2.0, 2.0]]), ('I_outer_CD', [[2.0, 2.0], [0.0, 2.0]]), ('I_outer_DA', [[0.0, 2.0], [0.0, 0.0]]), ('I_cut_1', [[1.0, 0.0], [2.0, 1.0]]), ('I_cut_2', [[2.0, 1.0], [1.0, 2.0]]), ('I_cut_3', [[1.0, 2.0], [0.0, 1.0]]), ('I_cut_4', [[0.0, 1.0], [1.0, 0.0]]), ('I_cut_5', [[1.5, 0.5], [1.5, 1.5]]), ('I_cut_6', [[1.5, 1.5], [0.5, 1.5]]), ('I_cut_7', [[0.5, 1.5], [0.5, 0.5]]), ('I_cut_8', [[0.5, 0.5], [1.5, 0.5]])]:
            c.line(points, id=object_id)
        c.path([[3.0, 0.0], [5.0, 1.0], [4.0, 2.0], [3.0, 0.0]], [1, 2, 2, 79], id='II_shade_2', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('II_outer_AB', [[3.0, 0.0], [5.0, 0.0]]), ('II_outer_BC', [[5.0, 0.0], [5.0, 2.0]]), ('II_outer_CD', [[5.0, 2.0], [3.0, 2.0]]), ('II_outer_DA', [[3.0, 2.0], [3.0, 0.0]]), ('II_cut_1', [[3.0, 0.0], [4.0, 2.0]]), ('II_cut_2', [[4.0, 2.0], [5.0, 1.0]]), ('II_cut_3', [[5.0, 1.0], [3.0, 0.0]])]:
            c.line(points, id=object_id)
        c.path([[6.0, 2.0], [7.0, 0.0], [8.0, 2.0], [6.0, 2.0]], [1, 2, 2, 79], id='III_shade_1', zorder=1, edgecolor='none', facecolor=(0.9098039215686274, 0.9098039215686274, 0.9098039215686274, 1.0), linewidth=0.0, capstyle='butt')
        for object_id, points in [('III_outer_AB', [[6.0, 0.0], [8.0, 0.0]]), ('III_outer_BC', [[8.0, 0.0], [8.0, 2.0]]), ('III_outer_CD', [[8.0, 2.0], [6.0, 2.0]]), ('III_outer_DA', [[6.0, 2.0], [6.0, 0.0]]), ('III_cut_1', [[6.0, 2.0], [7.0, 0.0]]), ('III_cut_2', [[7.0, 0.0], [8.0, 2.0]])]:
            c.line(points, id=object_id)
        for object_id, text, anchor in [('I_panel_label', 'I', (1.0, 2.25)), ('II_panel_label', 'II', (4.0, 2.25)), ('III_panel_label', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, clip_on=True, rotation_mode='default', offset_pt=(0, 0), annotation_clip=False)
        c.line([[0, 1], [2, 1]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[3, 1], [5, 1]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
