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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana38.json'
_PROVENANCE_SHA256 = 'b2e6b2035c7cbdc7f0a0f2c3e4f090d6dd4deb03012179819a6aa069397d6352'
_SOURCE_COPY_PATH = 'originals/Ana38.png'
_SOURCE_COPY_SHA256 = '1384c2df76dab61aa3e783baf9f46e7a3b808946a697972d9ec75341df1094f9'

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

class Ana38:
    def __init__(self):
        _verify_helper()
        self.id='Ana38'; self.source_dataset='MathVerse'
        self.query='Estimate the point(s) at which the graph of odd function f  has a local maximum or a local minimum.'
        self.answer='\\[\\text { local maximum: }(-3,60) \\text {, local minimum: }(3, -60)\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=(1,8/250),x_ticks=range(-6,7),y_ticks=range(-250,251,50),x_grid_step=1,y_grid_step=50)
        x=np.linspace(-5.05,5.05,1000); y=x**3-27*x; plot_curve(ax,x,y*(8/250))
        curve=lambda z:z**3-27*z
        ax.annotate('',xy=(-5.55,curve(-5.55)*(8/250)),xytext=(-5.05,curve(-5.05)*(8/250)),arrowprops={'arrowstyle':'-|>','color':'#24588a','lw':1})
        ax.annotate('',xy=(5.55,curve(5.55)*(8/250)),xytext=(5.05,curve(5.05)*(8/250)),arrowprops={'arrowstyle':'-|>','color':'#24588a','lw':1})
        return _finish(fig,ax,_dest(self.id,output_path))
