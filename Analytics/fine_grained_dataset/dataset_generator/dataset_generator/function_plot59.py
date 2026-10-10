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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana59.json'
_PROVENANCE_SHA256 = '2efe0b3da59307a4ea96d5165244d1a6073cbf73ad22e0e184cf88ec91c96f42'
_SOURCE_COPY_PATH = 'originals/Ana59.png'
_SOURCE_COPY_SHA256 = '3c433c2edb8940abc63e9c63b70121759c704d49a5ebce7ade23d0e935c7debd'

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

class Ana59:
    def __init__(self):
        _verify_helper()
        self.id='Ana59'; self.source_dataset='MathVerse'
        self.query='For function graphed below, determine if it has an inverse function.\nChoices:\nA:Yes\nB:No'
        self.answer='A'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=.65,x_ticks=range(-10,11,5),y_ticks=range(-10,11,5),x_label_step=5,y_label_step=5,x_grid_step=5,y_grid_step=5)
        left=np.linspace(-12,3.96,900); right=np.linspace(4.04,12,900)
        plot_curve(ax,left*.65,(1/(left-4))*.65); plot_curve(ax,right*.65,(1/(right-4))*.65)
        ax.axvline(4*.65,color='#82999a',linewidth=1,linestyle=(0,(3,3)),zorder=1)
        ax.axhline(0,color='#82999a',linewidth=1,linestyle=(0,(3,3)),zorder=1)
        ax.plot([-8,8],[0,0],color='#82999a',linewidth=1,linestyle=(0,(3,3)),zorder=3)
        return _finish(fig,ax,_dest(self.id,output_path))
