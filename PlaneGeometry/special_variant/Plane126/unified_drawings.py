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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C01.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, capstyle='butt', fill=False)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
        c.path([[2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2, 2, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, capstyle='butt', fill=False)
        for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, joinstyle='round', fill=False)
        for object_id, points in [('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, joinstyle='round', fill=False)
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C02.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999]], [1, 2, 2, 2, 2, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2], id='shade', capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 0.9999999999999999]], [1, 2], id='grid_v0', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, joinstyle='round', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', joinstyle='round', fill=False)
        for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [0.9999999999999999, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=1.5, joinstyle='round', fill=False)
        c.path([[0.9999999999999999, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', joinstyle='round', fill=False)
        for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        return c.save(output_path)

def C03(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C03.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='shade', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
        c.path([[2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2, 2, 2], id='shade', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        for object_id, points in [('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        return c.save(output_path)

def C04(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C04.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0]], [1, 2, 2], id='shade', capstyle='butt', fill=False)
        c.path([[2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2, 2, 2], id='shade', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        for object_id, points in [('grid_v0', [[0.0, 0.0], [0.0, 4.0]]), ('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.0, -1.1102230246251565e-16], [5.0, 4.0]], [1, 2], id='grid_v5', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        for object_id, points in [('grid_h0', [[0.0, 0.0], [5.0, 0.0]]), ('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, 4.0], [5.0, 4.0]], [1, 2], id='grid_h4', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        return c.save(output_path)

def C05(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C05.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999]], [1, 2, 2, 2, 2, 2], id='shade', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2], id='shade', capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 0.9999999999999999]], [1, 2], id='grid_v0', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', joinstyle='round', fill=False)
        for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [0.9999999999999999, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.path([[0.9999999999999999, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', joinstyle='round', fill=False)
        for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        return c.save(output_path)

def C06(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane126_C06.png'
    with Canvas(PLANE, xlim=(-0.11627906976744207, 5.116279069767442), ylim=(-0.6162790697674421, 4.616279069767442), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[1.0, 0.0], [5.0, 0.0], [5.0, 2.0], [2.0, 4.0], [0.0, 4.0], [0.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], alpha=0.45, zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), capstyle='butt')
        c.path([[1.0, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16], [5.0, 2.0], [2.0, 4.0], [5.551115123125783e-17, 4.0], [5.551115123125783e-17, 0.9999999999999999]], [1, 2, 2, 2, 2, 2], id='shade', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=3.0, capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [1.0, -1.1102230246251565e-16]], [1, 2], id='shade', capstyle='butt', fill=False)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [5.551115123125783e-17, 0.9999999999999999]], [1, 2], id='grid_v0', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.path([[5.551115123125783e-17, 0.9999999999999999], [5.551115123125783e-17, 4.0]], [1, 2], id='grid_v0', joinstyle='round', fill=False)
        for object_id, points in [('grid_v1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_v2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_v3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_v4', [[4.0, 0.0], [4.0, 4.0]]), ('grid_v5', [[5.0, 0.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        c.path([[5.551115123125783e-17, -1.1102230246251565e-16], [0.9999999999999999, -1.1102230246251565e-16]], [1, 2], id='grid_h0', edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), linewidth=3.0, joinstyle='round', fill=False)
        c.path([[0.9999999999999999, -1.1102230246251565e-16], [5.0, -1.1102230246251565e-16]], [1, 2], id='grid_h0', joinstyle='round', fill=False)
        for object_id, points in [('grid_h1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_h2', [[0.0, 2.0], [5.0, 2.0]]), ('grid_h3', [[0.0, 3.0], [5.0, 3.0]]), ('grid_h4', [[0.0, 4.0], [5.0, 4.0]])]:
            c.line(points, id=object_id)
        return c.save(output_path)
