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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana50.json'
_PROVENANCE_SHA256 = 'f05ea6cc101ab5f246742f9e45fa9820103b071a267dc2ea76716790a3bb8b07'
_SOURCE_COPY_PATH = 'originals/Ana50.png'
_SOURCE_COPY_SHA256 = '84de7b1fcd4c9e5b7cc6e9e9d1384b501b13c3b4d637eea1f136075aef73fe55'

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

class Ana50:
    def __init__(self):
        _verify_helper()
        self.id='Ana50'; self.source_dataset='MathVerse'
        self.query='Evaluate the following expressions to the nearest hundredth or as an exact ratio.'
        self.answer='-4.9\n-4.9'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=7.5,x_ticks=[-1,0,1],y_ticks=[-1,0,1],x_grid_step=1,y_grid_step=1)
        ax.add_patch(Circle((0,0),7.5,fill=False,edgecolor='black',linewidth=1,zorder=2))
        ax.plot([0,.2*7.5],[0,.98*7.5],color='black',linewidth=1,zorder=2)
        scatter_points(ax,.2*7.5,.98*7.5); label(ax,1.65,7.9,'(0.2, 0.98)',ha='left')
        ax.add_patch(Arc((0,0),2.8,2.8,theta1=0,theta2=np.degrees(np.arctan2(.98,.2)),edgecolor='black',linewidth=1,zorder=3))
        label(ax,1.1,.45,'θ')
        return _finish(fig,ax,_dest(self.id,output_path))
