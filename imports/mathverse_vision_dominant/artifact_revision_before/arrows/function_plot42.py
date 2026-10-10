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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana42.json'
_PROVENANCE_SHA256 = 'd9bdec5a4b3677789ab5ecd9dfb244e9a29ae74952d8a56262f802aba57c25cc'
_SOURCE_COPY_PATH = 'originals/Ana42.png'
_SOURCE_COPY_SHA256 = '612cd7e173fe985fa5964bbab71598722342b0fd4ffd07d5eeff5b2c4ee31cb0'

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

class Ana42:
    def __init__(self):
        _verify_helper()
        self.id='Ana42'; self.source_dataset='MathVerse'
        self.query='Write an equation for the transformation of f(x)=|x| as shown in the figure.'
        self.answer='f(x)=-3|x-3|+3'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(2.5,1),scale=(16/10,16/10),x_ticks=range(-1,6),y_ticks=range(-2,5),x_grid_step=1,y_grid_step=1)
        x=np.linspace(1.8,4.2,500); y=-3*np.abs(x-3)+3; plot_curve(ax,(x-2.5)*1.6,(y-1)*1.6)
        ax.annotate('',xy=((1.55-2.5)*1.6,(-1.35-1)*1.6),xytext=((1.8-2.5)*1.6,(-.6-1)*1.6),arrowprops={'arrowstyle':'-|>','color':'#168ca3','lw':1})
        ax.annotate('',xy=((4.45-2.5)*1.6,(-1.35-1)*1.6),xytext=((4.2-2.5)*1.6,(-.6-1)*1.6),arrowprops={'arrowstyle':'-|>','color':'#168ca3','lw':1})
        return _finish(fig,ax,_dest(self.id,output_path))
