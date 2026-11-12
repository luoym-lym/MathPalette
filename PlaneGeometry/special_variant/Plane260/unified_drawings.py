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
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane260_C01.png'
    with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
        for object_id, points in [(None, [[2.50732973761175, 4.528298269615471]]), (None, [[4.558263856072971, 3.4598797105217973]]), (None, [[3.527427859359478, 2.5256845885001935]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)

def C02(output_path=None):
    if output_path is None:
        output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / 'Plane260_C02.png'
    with Canvas(PLANE, xlim=(-0.12667099149054195, 5.130592591748275), ylim=(-0.12979189053362905, 5.127471692705188), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', zorder=1, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.0, 0.0], [5.0, 0.0], [5.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='box', capstyle='butt', fill=False)
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.045, 4.045], [3.955, 4.045], [3.955, 4.955], [1.045, 4.955], [1.045, 4.045]], [1, 2, 2, 2, 79], id='block0', capstyle='butt', fill=False)
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[4.045, 2.045], [4.955, 2.045], [4.955, 4.955], [4.045, 4.955], [4.045, 2.045]], [1, 2, 2, 2, 79], id='block1', capstyle='butt', fill=False)
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.045, 3.045], [2.955, 3.045], [2.955, 3.955], [0.045, 3.955], [0.045, 3.045]], [1, 2, 2, 2, 79], id='block2', capstyle='butt', fill=False)
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[3.045, 1.045], [3.955, 1.045], [3.955, 3.955], [3.045, 3.955], [3.045, 1.045]], [1, 2, 2, 2, 79], id='block3', capstyle='butt', fill=False)
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[0.045, 0.045], [0.955, 0.045], [0.955, 2.955], [0.045, 2.955], [0.045, 0.045]], [1, 2, 2, 2, 79], id='block4', capstyle='butt', fill=False)
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[1.045, 0.045], [1.955, 0.045], [1.955, 2.955], [1.045, 2.955], [1.045, 0.045]], [1, 2, 2, 2, 79], id='block5', capstyle='butt', fill=False)
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', zorder=1, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
        c.path([[2.045, 0.045], [4.955, 0.045], [4.955, 0.955], [2.045, 0.955], [2.045, 0.045]], [1, 2, 2, 2, 79], id='block6', capstyle='butt', fill=False)
        for object_id, points in [(None, [[3.575748296705422, 0.4854883450047369]]), (None, [[3.548903609291009, 2.4451505262569517]]), (None, [[2.6683978620982325, 4.528298269615471]])]:
            c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
        return c.save(output_path)
