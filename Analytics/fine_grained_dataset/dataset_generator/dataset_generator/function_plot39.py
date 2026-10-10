"""Frozen MathVerse analytic graph question."""
from __future__ import annotations
import sys
import hashlib
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Ellipse, Arc

_ROOT = Path(__file__).resolve().parents[1]
_DATASET_ROOT = _ROOT.parent
for _path in (_ROOT, _ROOT / "dataset_generator"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
from mathverse_renderer import open_canvas, plot_curve, scatter_points, label, set_view, map_point, finalize, lock_view

_HELPER_SHA256 = "630627b21686e59f5ca376ed8a56b2c25806b38defb672ab4f692ed4c5e7db13"

_PROVENANCE_PATH = 'provenance/MathVerse/Ana39.json'
_PROVENANCE_SHA256 = '70de07c44643941406712d63174514d2c9af4a7f48196d9df9e4aefd97b4b722'
_SOURCE_COPY_PATH = 'originals/Ana39.png'
_SOURCE_COPY_SHA256 = '8cd44bbbac50a19492b4c3fcc720a7ea770bf0fcfe9f5fa5c8db520da3b6c672'

def _verify_helper():
    helper = _ROOT / "mathverse_renderer.py"
    actual = hashlib.sha256(helper.read_bytes()).hexdigest()
    if actual != _HELPER_SHA256:
        raise RuntimeError(f"Frozen renderer helper changed: {actual} != {_HELPER_SHA256}")
    for relative, expected in ((_PROVENANCE_PATH, _PROVENANCE_SHA256),(_SOURCE_COPY_PATH, _SOURCE_COPY_SHA256)):
        actual = hashlib.sha256((_DATASET_ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Frozen MathVerse dependency changed: {relative}")


def _finish(fig, ax, destination):
    result = finalize(fig, destination)
    if plt.fignum_exists(fig.number):
        lock_view(ax)
    return result

def _dest(qid, output_path):
    return Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{qid}.png"

class Ana39:
    def __init__(self):
        _verify_helper()
        self.id='Ana39'; self.source_dataset='MathVerse'
        self.query='Estimate the point(s) at which the graph of odd function f  has a local maximum or a local minimum.'
        self.answer='\\[\\text { Local minimum at }(-2,-2) \\text {, decreasing on }(-3,-2) \\text {, increasing on }(-2, \\infty)\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=(1,8/250),x_ticks=range(-8,9),y_ticks=range(-250,251,50),x_grid_step=1,y_grid_step=50)
        # A frozen smooth interpolation through the visible source landmarks; domain is [-8,7].
        knots=np.array([-8,-5,-3,0,3,5,7],dtype=float)
        vals=np.array([-225,0,50,0,-50,0,150],dtype=float)
        # Piecewise cubic Hermite interpolation, with horizontal tangents at extrema.
        slopes=np.gradient(vals,knots); slopes[2]=0.0; slopes[4]=0.0
        x=np.linspace(-8,7,1000); idx=np.clip(np.searchsorted(knots,x)-1,0,len(knots)-2)
        h=knots[idx+1]-knots[idx]; t=(x-knots[idx])/h
        y=(2*t**3-3*t**2+1)*vals[idx]+(t**3-2*t**2+t)*h*slopes[idx]+(-2*t**3+3*t**2)*vals[idx+1]+(t**3-t**2)*h*slopes[idx+1]
        plot_curve(ax,x,y*(8/250))
        scatter_points(ax,-8, -225*(8/250)); scatter_points(ax,7,150*(8/250))
        return _finish(fig,ax,_dest(self.id,output_path))
