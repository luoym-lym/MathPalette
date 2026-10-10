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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana35.json'
_PROVENANCE_SHA256 = '7717a8f3d9b08066bd179bcaf2ed563a621689db5c40956fd252f267b6651faf'
_SOURCE_COPY_PATH = 'originals/Ana35.png'
_SOURCE_COPY_SHA256 = 'a41c9d6134507aebf1817590222f52260935475a66a8a35cc6a8baceb3bb226c'

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

class Ana35:
    def __init__(self):
        _verify_helper()
        self.id='Ana35'; self.source_dataset='MathVerse'
        self.query='Write the domain and range of the function using interval notation.'
        self.answer='\\[domain: (-\\infty, 1] and range: [0, \\infty)\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.2,x_ticks=range(-6,7),y_ticks=range(-6,7))
        x=np.linspace(-6,1,500); y=2*np.sqrt(np.maximum(0,1-x)); plot_curve(ax,x*1.2,y*1.2)
        scatter_points(ax,1.2,0)
        ax.annotate('',xy=(-4.8*1.2,2*np.sqrt(5.8)*1.2),xytext=(-4.0*1.2,2*np.sqrt(5)*1.2),arrowprops={'arrowstyle':'-|>','color':'black','lw':1})
        return _finish(fig,ax,_dest(self.id,output_path))
