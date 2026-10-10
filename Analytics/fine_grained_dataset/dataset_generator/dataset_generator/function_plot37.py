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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana37.json'
_PROVENANCE_SHA256 = '4b03e989fff1b52d5391015c828eb48d3ba5008d81cc02c01b384d5a4e78c14f'
_SOURCE_COPY_PATH = 'originals/Ana37.png'
_SOURCE_COPY_SHA256 = '6f771f3081c82650b860bd72ba840686f359f80fcd8d69be8161ccd662240e1d'

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

class Ana37:
    def __init__(self):
        _verify_helper()
        self.id='Ana37'; self.source_dataset='MathVerse'
        self.query='Estimate the intervals on which the function is increasing or decreasing.'
        self.answer='\\[The function is increasing on (-\\infty,-2.5) \\cup(1, \\infty), and decreasing on (-2.5,1)\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(-.75,1.5),scale=16/9,x_ticks=range(-5,5),y_ticks=range(-3,7),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-4.5,3,800); y=(x**3/3+0.75*x**2-2.5*x); plot_curve(ax,(x+.75)*(16/9),(y-1.5)*(16/9))
        color='black'
        ax.annotate('',xy=((-4.4+.75)*16/9,(((-4.4)**3/3)+.75*(-4.4)**2-2.5*(-4.4)-1.5)*16/9),xytext=((-4.05+.75)*16/9,(((-4.05)**3/3)+.75*(-4.05)**2-2.5*(-4.05)-1.5)*16/9),arrowprops={'arrowstyle':'-|>','color':color,'lw':1})
        ax.annotate('',xy=((2.63+.75)*16/9,((2.63**3/3)+.75*2.63**2-2.5*2.63-1.5)*16/9),xytext=((2.45+.75)*16/9,((2.45**3/3)+.75*2.45**2-2.5*2.45-1.5)*16/9),arrowprops={'arrowstyle':'-|>','color':color,'lw':1})
        return _finish(fig,ax,_dest(self.id,output_path))
