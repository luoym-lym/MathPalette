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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana60.json'
_PROVENANCE_SHA256 = '9b04b7ea6e34f2f4cd3caaad53e8960bb9b6c36e144aa3d0c26a7b4f75a70578'
_SOURCE_COPY_PATH = 'originals/Ana60.png'
_SOURCE_COPY_SHA256 = '76365ff3dd77ec1cba4e727035a4c870123c6b28b48e62a2008f6721fac8e6e5'

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

class Ana60:
    def __init__(self):
        _verify_helper()
        self.id='Ana60'; self.source_dataset='MathVerse'
        self.query='What is the slope of the figure?'
        self.answer='\\[=\\frac{7}{4}\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.25,x_ticks=range(-5,6),y_ticks=range(-6,7),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-5,5,200); plot_curve(ax,x*1.25,(7*x/4-1)*1.25)
        return _finish(fig,ax,_dest(self.id,output_path))
