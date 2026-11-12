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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane522_C01.png'
    with Canvas(PLANE, xlim=(-0.075, 1.075), ylim=(-0.071, 1.079), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_AB', [[0, 0], [1, 0]]), ('edge_BC', [[1, 0], [1, 1]]), ('edge_CD', [[1, 1], [0, 1]]), ('edge_DA', [[0, 1], [0, 0]])]:
            c.line(points, id=object_id)
        c.path([[0.33333333333333326, -2.7755575615628914e-17], [0.33333333333333326, 0.3333333333333333]], [1, 2], id='cut_1', linestyle=(0.0, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[0.33333333333333326, 0.3333333333333333], [0.33333333333333326, 1.0]], [1, 2], id='cut_1', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(144.25043478260872, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[-2.7755575615628914e-17, 0.33333333333333326], [0.3333333333333333, 0.33333333333333326]], [1, 2], id='cut_2', linestyle=(0.0, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[0.3333333333333333, 0.33333333333333326], [1.0, 0.33333333333333326]], [1, 2], id='cut_2', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(144.25043478260872, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.text('A', (0, 0), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='top', rotation_mode='default', offset_pt=(-8, -8), annotation_clip=None)
        c.text('B', (1, 0), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(8, -8), annotation_clip=None)
        c.text('C', (1, 1), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 8), annotation_clip=None)
        c.text('D', (0, 1), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-8, 8), annotation_clip=None)
        c.point([[0.09, 0.11]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[0.23, 0.22]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[0.48, 0.48]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[0.78, 0.78]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane522_C02.png'
    with Canvas(PLANE, xlim=(-0.075, 1.075), ylim=(-0.071, 1.079), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_AB', [[0, 0], [1, 0]]), ('edge_BC', [[1, 0], [1, 1]]), ('edge_CD', [[1, 1], [0, 1]])]:
            c.line(points, id=object_id)
        c.path([[-2.7755575615628914e-17, 1.0], [-2.7755575615628914e-17, 0.33333333333333337]], [1, 2], id='edge_DA', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), joinstyle='round', fill=False)
        c.path([[-2.7755575615628914e-17, 0.33333333333333337], [-2.7755575615628914e-17, -2.7755575615628914e-17]], [1, 2], id='edge_DA', joinstyle='round', fill=False)
        c.path([[0.33333333333333326, -2.7755575615628914e-17], [0.33333333333333326, 0.3333333333333333]], [1, 2], id='cut_1', linestyle=(0.0, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[0.33333333333333326, 0.3333333333333333], [0.33333333333333326, 1.0]], [1, 2], id='cut_1', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(144.25043478260872, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[-2.7755575615628914e-17, 0.33333333333333326], [0.3333333333333333, 0.33333333333333326]], [1, 2], id='cut_2', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(0.0, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.path([[0.3333333333333333, 0.33333333333333326], [1.0, 0.33333333333333326]], [1, 2], id='cut_2', linestyle=(144.25043478260872, (4.0, 3.0)), capstyle='butt', joinstyle='round', fill=False)
        c.text('A', (0, 0), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='top', rotation_mode='default', offset_pt=(-8, -8), annotation_clip=None)
        c.text('B', (1, 0), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=(8, -8), annotation_clip=None)
        c.text('C', (1, 1), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=(8, 8), annotation_clip=None)
        c.text('D', (0, 1), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=(-8, 8), annotation_clip=None)
        c.point([[0.09, 0.11]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[0.23, 0.22]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[0.09, 0.46]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[0.23, 0.78]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        return c.save(output_path)
