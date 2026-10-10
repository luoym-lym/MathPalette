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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana31.json'
_PROVENANCE_SHA256 = '59450d23396d44b2c307d79d33cbe57be6695ab677f41ded6827f8aef379ba0d'
_SOURCE_COPY_PATH = 'originals/Ana31.png'
_SOURCE_COPY_SHA256 = 'ffec436582fb92736f1b00072bd5340250546cf2fff6a9c092c7834c27c4bd75'

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

class Ana31:
    def __init__(self):
        _verify_helper()
        self.id='Ana31'; self.source_dataset='MathVerse'
        self.query='A cake maker has rectangular boxes. She often receives orders for cakes in the shape of an ellipse, and wants to determine the largest possible cake that can be made to fit inside the rectangular box.\n\nState the coordinates of the center of the cake in the form $(a, b)$.'
        self.answer='Center $=(20,10)$'; self.answer_type='string'; self.subject='analytic geometry'; self.level='high school'
        self.center=(10,15); self.scale=16/70
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=self.center,scale=self.scale,x_ticks=range(-20,41,5),y_ticks=range(-10,41,5),x_label_step=10,y_label_step=10,x_grid_step=10,y_grid_step=10)
        rect=Rectangle(((0-self.center[0])*self.scale,(0-self.center[1])*self.scale),40*self.scale,20*self.scale,facecolor='#D0D0D0',edgecolor='#A0AAAA',linewidth=1,alpha=0.45,zorder=1)
        ax.add_patch(rect)
        ellipse=Ellipse(((20-self.center[0])*self.scale,(10-self.center[1])*self.scale),40*self.scale,20*self.scale,facecolor='white',edgecolor='black',linewidth=1,zorder=2)
        ax.add_patch(ellipse)
        return _finish(fig,ax,_dest(self.id,output_path))
