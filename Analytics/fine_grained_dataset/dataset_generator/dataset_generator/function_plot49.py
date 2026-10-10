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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana49.json'
_PROVENANCE_SHA256 = 'd53e7e137d26af3942ee944677983d1a3fd3d3005a77c38c2615416f1c6141b0'
_SOURCE_COPY_PATH = 'originals/Ana49.png'
_SOURCE_COPY_SHA256 = '27fa375836d864afa7aa4bb6e8441eb4e62b6ca3f99bf0ed60b2be6f6c248ccc'

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

class Ana49:
    def __init__(self):
        _verify_helper()
        self.id='Ana49'; self.source_dataset='MathVerse'
        self.query="There is a function $h(t)$, where $t$ corresponds to the number of hours after 12:00 a.m. According to Takoda's research, approximately how much time passes between two consecutive high tides?"
        self.answer='12.5'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(24,2),scale=(16/48,16/6),x_ticks=range(0,49,4),y_ticks=range(-1,6),x_label_step=4,y_label_step=1,x_grid_step=4,y_grid_step=1,xlabel='t',ylabel='h')
        t=np.linspace(0,48,1200); h=1.8+2.3*np.cos(2*np.pi*(t-4)/12.5)
        plot_curve(ax,(t-24)*16/48,(h-2)*16/6)
        return _finish(fig,ax,_dest(self.id,output_path))
