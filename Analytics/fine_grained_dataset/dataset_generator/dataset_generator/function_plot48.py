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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana48.json'
_PROVENANCE_SHA256 = 'cbb2cabb21f1a2742f067683eac684c0c5448080572553a9af55e39f9fe3a62d'
_SOURCE_COPY_PATH = 'originals/Ana48.png'
_SOURCE_COPY_SHA256 = '398b09855c73d61f808521d98164876d8d9e7451cd1acaeceeabb2c545206c93'

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

class Ana48:
    def __init__(self):
        _verify_helper()
        self.id='Ana48'; self.source_dataset='MathVerse'
        self.query='Below is the graph of a trigonometric function. What is the period of the function? Give an exact value.'
        self.answer='\\[4 \\pi\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,7.5),scale=(16/18,16/16),x_ticks=range(-8,11),y_ticks=range(0,16),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-8,10,900); y=7.7+5.3*np.cos((x-3*np.pi/2)/2)
        plot_curve(ax,x*16/18,(y-7.5)*1.0)
        for px,py,txt in [(-np.pi/2,2.4,'(−π/2, 2.4)'),(3*np.pi/2,13,'(3π/2, 13)')]:
            xx=px*16/18; yy=(py-7.5); scatter_points(ax,xx,yy); label(ax,xx,yy+.55,txt)
        return _finish(fig,ax,_dest(self.id,output_path))
