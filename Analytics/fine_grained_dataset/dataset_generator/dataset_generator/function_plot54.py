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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana54.json'
_PROVENANCE_SHA256 = '35a40774fb07b6fc2a177dc1ce873ea898d66b2a2f9d3fb44293de9b8ff9cc89'
_SOURCE_COPY_PATH = 'originals/Ana54.png'
_SOURCE_COPY_SHA256 = 'a75bf6743c5f5ca05b02fbc8008715241a6349a2e4c19be9bd58ba7187a0f749'

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

class Ana54:
    def __init__(self):
        _verify_helper()
        self.id='Ana54'; self.source_dataset='MathVerse'
        self.query='f(x)=x^2+x-6. How many roots do the functions have in common, f(x) and g(x)?\nChoices:\nA:$f$ and $g$ share the same root(s).\nB:$f$ and $g$ share one root in common but each have another root that is not shared.\nC:$f$ and $g$ share no roots in common.'
        self.answer='B'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=.95,x_ticks=range(-8,9),y_ticks=range(-8,9),x_label_step=2,y_label_step=2,x_grid_step=1,y_grid_step=1)
        x=np.linspace(-4,4,500); y=(x-.5)**2-2.25; plot_curve(ax,x*.95,y*.95); label(ax,5,5,'y = g(x)',ha='left')
        return _finish(fig,ax,_dest(self.id,output_path))
