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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana47.json'
_PROVENANCE_SHA256 = 'e9bd0f7b944006171cbdd4ae833a0477084e394e6665cc6aa77e3dd8ccebf5de'
_SOURCE_COPY_PATH = 'originals/Ana47.png'
_SOURCE_COPY_SHA256 = '4a490d742dc160cc072dcf12c5b64a0e91eb0c8283a8ee778043eb9f72d720e7'

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

class Ana47:
    def __init__(self):
        _verify_helper()
        self.id='Ana47'; self.source_dataset='MathVerse'
        self.query='Below is the graph of a trigonometric function. What is the period of the function? Give an exact value.'
        self.answer='\\[{8}{5} \\pi\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        T=8*np.pi/5; x0=3*np.pi/5
        fig,ax=open_canvas(); set_view(ax,center=(4.5,5.5),scale=(16/14,16/14),x_ticks=range(-2,12),y_ticks=range(-2,14),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-2,12,1000); y=8-2*np.sin(2*np.pi*(x-x0)/T)
        plot_curve(ax,(x-4.5)*16/14,(y-5.5)*16/14)
        for px,txt,offset in [(3*np.pi/5,r'$(\frac{3\pi}{5},8)$',(0,-22)),(7*np.pi/5,r'$(\frac{7\pi}{5},8)$',(0,12))]:
            ax.scatter((px-4.5)*16/14,(8-5.5)*16/14,s=22,c='#d69a55',zorder=4)
            ax.annotate(txt,((px-4.5)*16/14,(8-5.5)*16/14),xytext=offset,textcoords='offset points',ha='center',va='top' if offset[1]<0 else 'bottom',fontsize=12,zorder=5)
        return _finish(fig,ax,_dest(self.id,output_path))
