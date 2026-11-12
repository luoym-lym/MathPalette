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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane248_C01.png'
    with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[6, 1], [9, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[6, 1], [9, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane248_C02.png'
    with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        c.path([[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
        c.path([[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option4', capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[13, 1], [15, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane248_C03.png'
    with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('source0', [[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('source1', [[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79]), ('option0', [[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option1', [[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='option2', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        c.path([[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option3', capstyle='butt')
        c.path([[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option4', capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[13, 1], [15, 2]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[13, 2], [15, 1]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane248_C04.png'
    with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source0', capstyle='butt')
        c.path([[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source1', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[7, 2], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane248_C05.png'
    with Canvas(PLANE, xlim=(-1.3532246852867402, 27.67854144687496), ylim=(-11.02219427296967, 18.00957185919203), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[8.0, 6.0], [9.0, 7.0], [10.0, 6.0], [10.0, 5.0], [9.0, 5.0], [9.0, 6.0], [8.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source0', capstyle='butt')
        c.path([[11.0, 6.0], [12.0, 7.0], [13.0, 6.0], [13.0, 5.0], [12.0, 5.0], [12.0, 6.0], [11.0, 6.0]], [1, 2, 2, 2, 2, 2, 79], id='source1', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 1.0], [2.0, 2.0], [3.0, 1.0], [3.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79], id='option0', capstyle='butt')
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 2.0], [9.0, 1.0], [8.0, 0.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 2, 2, 79], id='option1', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
        for object_id, vertices, codes in [('option2', [[12.0, 1.0], [13.0, 2.0], [15.0, 2.0], [15.0, 3.0], [16.0, 2.0], [15.0, 1.0], [13.0, 1.0], [13.0, 0.0], [12.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 79]), ('option3', [[18.0, 0.0], [19.0, 0.0], [21.0, 2.0], [21.0, 3.0], [20.0, 3.0], [20.0, 2.0], [19.0, 2.0], [19.0, 1.0], [18.0, 1.0], [18.0, 0.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 79]), ('option4', [[24.0, 1.0], [25.0, 1.0], [26.0, 0.0], [26.0, 1.0], [27.0, 1.0], [27.0, 2.0], [26.0, 2.0], [25.0, 3.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        for object_id, text, anchor in [('label0', 'A', (-0.4, 3.3)), ('label1', 'B', (5.6, 3.3)), ('label2', 'C', (11.6, 3.3)), ('label3', 'D', (17.6, 3.3)), ('label4', 'E', (23.6, 3.3))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[7.0, 2.0], [7.5, 1.0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
