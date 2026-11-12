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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid78_C01.png'
    with Canvas(SOLID, xlim=(-1.0690872749445486, 2.6044840987074416), ylim=(-1.0909815619277845, 2.5825898117242057), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v00_v01', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v01_v02', [[1.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v00_v02', [[0.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v01_v03', [[1.0, 0.0], [1.6666666666666665, 0.7453559924999298]]), ('edge_v02_v03', [[0.5, 1.118033988749895], [1.6666666666666665, 0.7453559924999298]]), ('edge_v03_v04', [[1.6666666666666665, 0.7453559924999298], [1.5555555555555556, 1.7391639824998364]]), ('edge_v02_v04', [[0.5, 1.118033988749895], [1.5555555555555556, 1.7391639824998364]]), ('edge_v04_v05', [[1.5555555555555556, 1.7391639824998364], [0.7407407407407409, 2.3188853099997817]]), ('edge_v02_v05', [[0.5, 1.118033988749895], [0.7407407407407409, 2.3188853099997817]]), ('edge_v01_v06', [[1.0, 0.0], [1.0, -1.0]]), ('edge_v06_v07', [[1.0, -1.0], [0.0, -1.0]]), ('edge_v00_v07', [[0.0, 0.0], [0.0, -1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.625578163355026, 3.548260240480185), annotation_clip=None)
        c.text('B', (1.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.880930102366165, -6.065975526142535), annotation_clip=None)
        c.text('C', (0.7407407407407409, 2.3188853099997817), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-6.262662537244549, 15.80439995522113), annotation_clip=None)
        c.text('D', (1.5555555555555556, 1.7391639824998364), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14.651577535536417, 8.621558775544282), annotation_clip=None)
        c.text('E', (0.5, 1.118033988749895), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.193848855066566, 5.172935265326576), annotation_clip=None)
        c.point([[0.0, 0.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.point([[1.0, 0.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
        c.point([[0.7407407407407409, 2.3188853099997817]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
        c.point([[0.5, 1.118033988749895]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[1.5555555555555556, 1.7391639824998364]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
        c.line([[0.0, 0.0], [1.5555555555555556, 1.7391639824998364]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / 'Solid78_C02.png'
    with Canvas(SOLID, xlim=(-1.0690872749445486, 2.6044840987074416), ylim=(-1.0909815619277845, 2.5825898117242057), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, points in [('edge_v00_v01', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v01_v02', [[1.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v00_v02', [[0.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v01_v03', [[1.0, 0.0], [1.6666666666666665, 0.7453559924999298]]), ('edge_v02_v03', [[0.5, 1.118033988749895], [1.6666666666666665, 0.7453559924999298]]), ('edge_v03_v04', [[1.6666666666666665, 0.7453559924999298], [1.5555555555555556, 1.7391639824998364]]), ('edge_v02_v04', [[0.5, 1.118033988749895], [1.5555555555555556, 1.7391639824998364]]), ('edge_v04_v05', [[1.5555555555555556, 1.7391639824998364], [0.7407407407407409, 2.3188853099997817]]), ('edge_v02_v05', [[0.5, 1.118033988749895], [0.7407407407407409, 2.3188853099997817]]), ('edge_v01_v06', [[1.0, 0.0], [1.0, -1.0]]), ('edge_v06_v07', [[1.0, -1.0], [0.0, -1.0]]), ('edge_v00_v07', [[0.0, 0.0], [0.0, -1.0]])]:
            c.line(points, id=object_id, zorder=3, clip_on=False)
        c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.625578163355026, 3.548260240480185), annotation_clip=None)
        c.text('B', (1.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.880930102366165, -6.065975526142535), annotation_clip=None)
        c.text('C', (0.7407407407407409, 2.3188853099997817), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-6.262662537244549, 15.80439995522113), annotation_clip=None)
        c.text('D', (1.5555555555555556, 1.7391639824998364), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14.651577535536417, 8.621558775544282), annotation_clip=None)
        c.text('E', (0.5, 1.118033988749895), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.193848855066566, 5.172935265326576), annotation_clip=None)
        for object_id, points in [(None, [[0.5, 1.118033988749895]]), (None, [[1.5555555555555556, 1.7391639824998364]]), (None, [[0.0, 0.0]]), (None, [[1.0, 0.0]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.line([[1.5555555555555556, 1.7391639824998364], [0.0, 0.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
