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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana41.json'
_PROVENANCE_SHA256 = '81c8ac751a81daf260871ef84434fad897ed0f62bc1c4c7b24aa3010e96d95df'
_SOURCE_COPY_PATH = 'originals/Ana41.png'
_SOURCE_COPY_SHA256 = '7223bff79d6685f66bc0c09adc8b271b7e0a0a828798f016235b81058c844f4d'

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

class Ana41:
    def __init__(self):
        _verify_helper()
        self.id='Ana41'; self.source_dataset='MathVerse'
        self.query='Find the absolute maximum of the cubic function.'
        self.answer='(-1.8,10)'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=(8/6,8/15),x_ticks=range(-6,7),y_ticks=range(-14,15,2),x_grid_step=1,y_grid_step=2)
        x=np.linspace(-3.3,3.3,900); y=(10/3.8888888889)*(x**3/3-3.24*x); plot_curve(ax,x*(8/6),y*(8/15))
        ax.annotate('',xy=(-3.3*8/6,y[0]*8/15),xytext=(-3.0*8/6,(10/3.8888888889)*(-9+9.72)*8/15),arrowprops={'arrowstyle':'-|>','color':'black','lw':1})
        ax.annotate('',xy=(3.3*8/6,y[-1]*8/15),xytext=(3.0*8/6,(10/3.8888888889)*(9-9.72)*8/15),arrowprops={'arrowstyle':'-|>','color':'black','lw':1})
        return _finish(fig,ax,_dest(self.id,output_path))
