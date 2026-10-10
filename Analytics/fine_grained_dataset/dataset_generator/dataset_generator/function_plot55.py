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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana55.json'
_PROVENANCE_SHA256 = 'ac804897806f259d2888f6bbe57d3759678094637411498fbdfcd810f9a702fa'
_SOURCE_COPY_PATH = 'originals/Ana55.png'
_SOURCE_COPY_SHA256 = '9bf6498534b35a913a4812ba5fffcf129be125cd9133910e625801cdca1bdc6e'

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

class Ana55:
    def __init__(self):
        _verify_helper()
        self.id='Ana55'; self.source_dataset='MathVerse'
        self.query='Write the equation for g(x).'
        self.answer='\\[g(x)=x^2-3\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1,x_ticks=range(-7,8),y_ticks=range(-8,9),x_label_step=1,y_label_step=1,x_grid_step=1,y_grid_step=1)
        x=np.linspace(-3,3,500); plot_curve(ax,x,x*x); ax.plot(x,x*x-3,color='black',linewidth=1,linestyle=(0,(4,2)),zorder=2)
        label(ax,4,5,'f'); label(ax,2,-1,'g')
        return _finish(fig,ax,_dest(self.id,output_path))
