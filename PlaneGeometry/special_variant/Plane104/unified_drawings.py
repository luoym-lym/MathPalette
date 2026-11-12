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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane104_C01.png'
    with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane104_C02.png'
    with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', capstyle='butt')
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane104_C03.png'
    with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane104_C04.png'
    with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt')
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt')
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', linewidth=0.5, linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', linewidth=0.5, linestyle=(0, [3.7, 1.6]), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane104_C05.png'
    with Canvas(PLANE, xlim=(-6.981103617740445, 6.981103617740446), ylim=(-7.651935963581318, 6.310271271899573), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[-6.5, 2.0], [-3.5, 2.0], [-1.5, 4.0], [-3.5, 6.0], [-6.5, 6.0], [-5.0, 4.5], [-6.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_R', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[1.5, 2.0], [4.5, 2.0], [6.5, 4.0], [4.5, 6.0], [1.5, 6.0], [2.25, 4.5], [1.5, 2.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_A', capstyle='butt')
        c.path([[-2.0, -1.5], [-2.0, -4.5], [-4.0, -6.5], [-6.0, -4.5], [-6.0, -1.4999999999999998], [-4.5, -3.0], [-2.0, -1.5]], [1, 2, 2, 2, 2, 2, 79], id='outline_B', capstyle='butt')
        c.path([[1.5, -6.0], [4.5, -6.0], [6.5, -3.0], [4.5, -2.0], [1.5, -2.0], [3.0, -3.5], [1.5, -6.0]], [1, 2, 2, 2, 2, 2, 79], id='outline_C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (-4.0, 2.0)), ('name_A', 'A', (4.0, 2.0)), ('name_B', 'B', (-4.0, -6.5)), ('name_C', 'C', (4.0, -6.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)
