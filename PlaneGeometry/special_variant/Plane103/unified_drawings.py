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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane103_C01.png'
    with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
        c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane103_C02.png'
    with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
        c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
        c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', linestyle=(0, [3.7, 1.6]), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane103_C03.png'
    with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linestyle=(0, [3.7, 1.6]), capstyle='butt')
        c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane103_C04.png'
    with Canvas(PLANE, xlim=(-0.41, 11.41), ylim=(-1.005, 10.815), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 7.0], [4.0, 7.0], [4.0, 8.0], [1.0, 8.0], [1.0, 10.0], [0.0, 10.0], [0.0, 7.0]], [1, 2, 2, 2, 2, 2, 79], id='R', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt')
        c.path([[7.0, 6.5], [10.0, 6.5], [10.0, 10.5], [9.0, 10.5], [9.0, 7.5], [7.0, 7.5], [7.0, 6.5]], [1, 2, 2, 2, 2, 2, 79], id='A', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
        c.path([[0.0, 0.0], [4.0, 0.0], [4.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='B', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=2.0, capstyle='butt')
        c.path([[7.0, 0.0], [11.0, 0.0], [11.0, 1.0], [9.0, 1.0], [9.0, 3.0], [7.0, 3.0], [7.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='C', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        for object_id, text, anchor in [('name_R', 'R', (2.0, 7.0)), ('name_A', 'A', (8.5, 6.5)), ('name_B', 'B', (2.0, 0.0)), ('name_C', 'C', (9.0, 0.0))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, -22), annotation_clip=None)
        return c.save(output_path)
