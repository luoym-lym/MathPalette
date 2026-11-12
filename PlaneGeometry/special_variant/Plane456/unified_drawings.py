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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane456_C01.png'
    with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='outerI', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='outerII', capstyle='butt')
        c.path([[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='outerIII', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
        c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
        c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
        c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', capstyle='butt')
        c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
        c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
        for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        c.line([[6, 1], [8, 1]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane456_C02.png'
    with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
        c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
        c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
        c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
        c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
        for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane456_C03.png'
    with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
        c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
        c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
        c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
        c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
        for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane456_C04.png'
    with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
        c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
        c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
        c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
        c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
        c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
        for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.point([[7.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        c.point([[7.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane456_C05.png'
    with Canvas(PLANE, xlim=(-0.1982668529167313, 8.211586609172755), ylim=(-3.026694478975208, 5.383158983114279), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        for object_id, vertices, codes in [('outerI', [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('outerII', [[3.0, 0.0], [5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('outerIII', [[6.0, 0.0], [8.0, 0.0], [8.0, 2.0], [6.0, 2.0], [6.0, 0.0]], [1, 2, 2, 2, 79])]:
            c.path(vertices, codes, id=object_id, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 0.0]], [1, 2, 2, 79], id='grayIbottom', capstyle='butt', fill=False)
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[1.0, 1.0], [1.0, 2.0], [2.0, 2.0], [1.0, 1.0]], [1, 2, 2, 79], id='grayItop', capstyle='butt', fill=False)
        c.line([[1.0, 0.0], [1.0, 2.0]], id='midI')
        c.line([[0.0, 0.0], [2.0, 2.0]], id='diagI')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[3.0, 1.0], [4.0, 1.0], [4.0, 2.0], [3.0, 2.0], [3.0, 1.0]], [1, 2, 2, 2, 79], id='grayII', capstyle='butt', fill=False)
        c.line([[4.0, 0.0], [4.0, 2.0]], id='vII')
        c.line([[3.0, 1.0], [5.0, 1.0]], id='hII')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[6.0, 1.0], [6.5, 1.5], [7.0, 1.0], [6.5, 0.5], [6.0, 1.0]], [1, 2, 2, 2, 79], id='leftdiamond', capstyle='butt', fill=False)
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
        c.path([[7.0, 1.0], [7.5, 1.5], [8.0, 1.0], [7.5, 0.5], [7.0, 1.0]], [1, 2, 2, 2, 79], id='rightdiamond', capstyle='butt', fill=False)
        c.path([[6.0, 1.0], [7.0, 2.0], [8.0, 1.0], [7.0, 0.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='midpointdiamond', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
        c.line([[6.0, 0.0], [8.0, 2.0]], id='diagIIIa')
        c.line([[6.0, 2.0], [8.0, 0.0]], id='diagIIIb')
        for object_id, text, anchor in [('labelI', 'I', (1.0, 2.25)), ('labelII', 'II', (4.0, 2.25)), ('labelIII', 'III', (7.0, 2.25))]:
            c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
        c.line([[0.013010102932330514, 1.006462369265419], [2.014129237600274, 0.980696886844802]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
        return c.save(output_path)
