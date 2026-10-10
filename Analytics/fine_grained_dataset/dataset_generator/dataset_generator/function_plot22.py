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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana22.json'
_PROVENANCE_SHA256 = '70d60608b2c2fa25a2fc7be69d868e752d02b76ed644d65a52eca89e97990be4'
_SOURCE_COPY_PATH = 'originals/Ana22.png'
_SOURCE_COPY_SHA256 = '0102cfbb6314885d3029e8678d042d79b5407cf00cbf12df712204a12b35dae4'

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

class Ana22:
    def __init__(self):
        _verify_helper()
        self.id='Ana22'; self.source_dataset='MathVerse'
        self.query='Find the equation of the figure.\nUse exact numbers.\ny = _ x + _'
        self.answer='y=-2 x+5'; self.answer_type='string'; self.subject='analytic geometry'; self.level='high school'
        self.center=(0,0); self.scale=0.8
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=self.center,scale=self.scale,x_ticks=range(-10,11),y_ticks=range(-10,11))
        x=np.linspace(-10,10,500); plot_curve(ax,x*self.scale,(-2*x+5)*self.scale)
        return _finish(fig,ax,_dest(self.id,output_path))
