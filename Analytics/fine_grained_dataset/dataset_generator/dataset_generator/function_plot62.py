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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana62.json'
_PROVENANCE_SHA256 = '1013b9188f7ae45308ab546fb81ed1910526e77c4e4082d27477ea88b4a883b8'
_SOURCE_COPY_PATH = 'originals/Ana62.png'
_SOURCE_COPY_SHA256 = 'ef9b04739a16a96bef1fe5eadbd63487848b37b6ea6c6fa52e42ec3d888675fd'

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

class Ana62:
    def __init__(self):
        _verify_helper()
        self.id='Ana62'; self.source_dataset='MathVerse'
        self.query='Find the equation of the figure in point-slope form .'
        self.answer='$y-3=\\frac{2}{3}(x-8)$'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(5.5,2),scale=(16/13,16/6),x_ticks=range(-1,13),y_ticks=range(-1,6),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-1,11,400); y=3+(2/3)*(x-8); plot_curve(ax,(x-5.5)*16/13,(y-2)*16/6)
        return _finish(fig,ax,_dest(self.id,output_path))
