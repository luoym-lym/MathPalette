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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana27.json'
_PROVENANCE_SHA256 = '095d15fbc03068bf9aa8bdff7553599157cc81be5a401cf9fb372aa0c3ca820f'
_SOURCE_COPY_PATH = 'originals/Ana27.png'
_SOURCE_COPY_SHA256 = 'f772b9abaaa113dcc13d678330398eac35fd59c4b281f86374e8ccb53a8f31fc'

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

class Ana27:
    def __init__(self):
        _verify_helper()
        self.id='Ana27'; self.source_dataset='MathVerse'
        self.query='Write the equation of the figure.'
        self.answer='\\[(x+3)^2+(y+3)^2=9\\]'; self.answer_type='string'; self.subject='analytic geometry'; self.level='high school'
        self.center=(0,0); self.scale=2/3
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=self.center,scale=self.scale,x_ticks=range(-12,13),y_ticks=range(-12,13),x_label_step=5,y_label_step=5,x_grid_step=5,y_grid_step=5)
        ax.add_patch(Circle((-3*self.scale,-3*self.scale),3*self.scale,fill=False,edgecolor='black',linewidth=1,zorder=2))
        scatter_points(ax,-3*self.scale,-3*self.scale)
        return _finish(fig,ax,_dest(self.id,output_path))
