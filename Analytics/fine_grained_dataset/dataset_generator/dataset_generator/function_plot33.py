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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana33.json'
_PROVENANCE_SHA256 = 'ec3e79fa384b75953102c47d043de000c24f46f1d5ce8e90012e5ce3807767e8'
_SOURCE_COPY_PATH = 'originals/Ana33.png'
_SOURCE_COPY_SHA256 = '2afd4c96b4fc5abc26c6b29504bc652174dfe01315fac2792629998713df9fde'

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

class Ana33:
    def __init__(self):
        _verify_helper()
        self.id='Ana33'; self.source_dataset='MathVerse'
        self.query='Find the domain and range of the function f using interval notation.'
        self.answer='domain: [-4, 0) and range: (-3, 1]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.25,x_ticks=range(-6,7),y_ticks=range(-6,3),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-3,1,500); y=-x**3-3*x**2
        plot_curve(ax,x*1.25,y*1.25)
        scatter_points(ax,-3*1.25,0,open_marker=True); scatter_points(ax,1.25,-4*1.25)
        label(ax,-2.25,-2.25,'f',ha='left')
        return _finish(fig,ax,_dest(self.id,output_path))
