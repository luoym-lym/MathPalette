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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana63.json'
_PROVENANCE_SHA256 = 'bf2b2623cff34d621f49aeefd5e34a40e1cf81d0376133240d6af34c1e989fdd'
_SOURCE_COPY_PATH = 'originals/Ana63.png'
_SOURCE_COPY_SHA256 = 'ad7fc8c69703af2a43b2f6a234320cfd3313cbc71312f33bdd1cd363b6f2625b'

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

class Ana63:
    def __init__(self):
        _verify_helper()
        self.id='Ana63'; self.source_dataset='MathVerse'
        self.query='Let $f$ be the function given by the following graph. What is the domain of $f$?'
        self.answer='$[-5,-3) \\cup(-3,5]$'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.2,x_ticks=range(-6,7),y_ticks=range(-1,6),x_grid_step=1,y_grid_step=1)
        for p,open_first,open_last in [([(-5,1),(-3,2)],False,True),([(-3,2),(-1,4)],True,True),([(-1,5),(3,3),(5,1)],False,False)]:
            ar=np.array(p); plot_curve(ax,ar[:,0]*1.2,ar[:,1]*1.2)
            if len(p)==2:
                if open_first: scatter_points(ax,p[0][0]*1.2,p[0][1]*1.2,open_marker=True)
                else: scatter_points(ax,p[0][0]*1.2,p[0][1]*1.2)
                if open_last: scatter_points(ax,p[-1][0]*1.2,p[-1][1]*1.2,open_marker=True)
                else: scatter_points(ax,p[-1][0]*1.2,p[-1][1]*1.2)
            else:
                scatter_points(ax,p[0][0]*1.2,p[0][1]*1.2); scatter_points(ax,p[-1][0]*1.2,p[-1][1]*1.2)
        return _finish(fig,ax,_dest(self.id,output_path))
