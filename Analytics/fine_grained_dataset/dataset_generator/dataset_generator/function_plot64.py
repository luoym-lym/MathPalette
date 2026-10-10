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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana64.json'
_PROVENANCE_SHA256 = 'bd4e669777665feb18d5e6a395bf4faa6092d50ee6b92f68c10b9618fb217073'
_SOURCE_COPY_PATH = 'originals/Ana64.png'
_SOURCE_COPY_SHA256 = 'f5f7d73cebf11517a78c8d5dd7ec725d512a91a06e953b5289496671967e902a'

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

class Ana64:
    def __init__(self):
        _verify_helper()
        self.id='Ana64'; self.source_dataset='MathVerse'
        self.query='What is the average rate of change in the graph?'
        self.answer='$\\frac{1}{2000}$'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(11,13.5),scale=(16/22,16/27),x_ticks=range(0,23),y_ticks=range(0,28),x_label_step=5,y_label_step=5,x_grid_step=5,y_grid_step=5,xlabel='quantity (thousand units)',ylabel='price',xlabel_position=(.91,.18),xlabel_rotation=90)
        x=np.linspace(0,22,300); y=14+.5*x
        plot_curve(ax,(x-11)*16/22,(y-13.5)*16/27)
        for p in [(6,17),(16,22)]: scatter_points(ax,(p[0]-11)*16/22,(p[1]-13.5)*16/27)
        return _finish(fig,ax,_dest(self.id,output_path))
