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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana52.json'
_PROVENANCE_SHA256 = '95371848486c0393cac0869cd79514216c28f6ecd5864f74b93e84af46ee78e1'
_SOURCE_COPY_PATH = 'originals/Ana52.png'
_SOURCE_COPY_SHA256 = 'dbb9ec91a196cfc13cf15d674d4d36532132ef9ea3ddec83cbbad540820cce4c'

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

class Ana52:
    def __init__(self):
        _verify_helper()
        self.id='Ana52'; self.source_dataset='MathVerse'
        self.query='\\[What is the domain of h?\nChoices:\nA:-5 \\leq x \\leq 7\nB:-5 \\leq x \\leq 4\nC:-5 \\leq x \\leq 5\nD:-5 \\leq x \\leq 6\\]'
        self.answer='C'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=.95,x_ticks=range(-8,9),y_ticks=range(-8,9),x_label_step=2,y_label_step=2,x_grid_step=1,y_grid_step=1)
        p=np.array([[-5,4],[-3,3],[-1,7],[2,1],[4,-5]])*.95
        plot_curve(ax,p[:,0],p[:,1]); scatter_points(ax,p[[0,-1],0],p[[0,-1],1])
        label(ax,2,2.3,'h')
        return _finish(fig,ax,_dest(self.id,output_path))
