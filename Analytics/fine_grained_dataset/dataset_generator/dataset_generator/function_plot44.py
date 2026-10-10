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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana44.json'
_PROVENANCE_SHA256 = '3b8a7bd164c53ac4ec99970e08fa2f434e15e51fbc422b3439ffc07529bafc44'
_SOURCE_COPY_PATH = 'originals/Ana44.png'
_SOURCE_COPY_SHA256 = '5e450cc66c71ea4d4fa865a84871e791497e78e097e8a027b10cff1762694ba3'

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

class Ana44:
    def __init__(self):
        _verify_helper()
        self.id='Ana44'; self.source_dataset='MathVerse'
        self.query='Below is the graph of a trigonometric function. It has an amplitude of 1.8 . What is the midline equation of the function?'
        self.answer='0.2'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.45,x_ticks=range(-5,6),y_ticks=range(-5,6))
        x=np.linspace(-5,5,800); y=.2+1.8*np.cos((6/5)*(x+1)); plot_curve(ax,x*1.45,y*1.45)
        q=(-1*1.45,2*1.45); scatter_points(ax,*q); label(ax,q[0]-.2,q[1]+.65,'(−π/3, 2)',ha='right')
        return _finish(fig,ax,_dest(self.id,output_path))
