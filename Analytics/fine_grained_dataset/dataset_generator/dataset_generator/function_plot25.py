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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana25.json'
_PROVENANCE_SHA256 = '5d7a8bb3cafc34454f8f59af1b7dbe46b0f961e4652c0a7fbf24f3b28f1b67d6'
_SOURCE_COPY_PATH = 'originals/Ana25.png'
_SOURCE_COPY_SHA256 = '77e5936d996fcba958100ffdae2823c981b1243cae8de9f05b3077b17281c319'

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

class Ana25:
    def __init__(self):
        _verify_helper()
        self.id='Ana25'; self.source_dataset='MathVerse'
        self.query='Consider the circle on the graph.\n\nFind the equation of the circle in standard form.'
        self.answer='$(x-1)^{2}+(y-3)^{2}=36$'; self.answer_type='string'; self.subject='analytic geometry'; self.level='high school'
        self.center=(0,0); self.scale=2/3
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=self.center,scale=self.scale,x_ticks=range(-12,13),y_ticks=range(-12,13))
        h,k=1,3; r=6
        ax.add_patch(Circle(((h-self.center[0])*self.scale,(k-self.center[1])*self.scale),r*self.scale,fill=False,edgecolor='black',linewidth=1,zorder=2))
        scatter_points(ax,(h-self.center[0])*self.scale,(k-self.center[1])*self.scale)
        return _finish(fig,ax,_dest(self.id,output_path))
