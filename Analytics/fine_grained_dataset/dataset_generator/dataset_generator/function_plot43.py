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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana43.json'
_PROVENANCE_SHA256 = 'fe58284f442fbd7c0555ab6439851b710daa72227d2e0dd2410796db6be4a159'
_SOURCE_COPY_PATH = 'originals/Ana43.png'
_SOURCE_COPY_SHA256 = 'bd8eda21a2ec18f0a1e19fa45ca06cc4361c73c79c4a593be9ffe19226e5c16d'

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

class Ana43:
    def __init__(self):
        _verify_helper()
        self.id='Ana43'; self.source_dataset='MathVerse'
        self.query='$f$ and $g$ can model the heights (in meters) of two airplanes. $t$ is the number of minutes that have passed since noon at a local airport. Which statements represent the meaning of the intersection points of the graphs?\nChoices:\nA.They mean that one airplane was initially higher than the other airplane.\nB.They mean that the airplanes reached the same height when they were both at 10,000 meters.\nC.They give the solutions to the equation $f(t)=0$.\nD.They give the solutions to the equation $f(t)=g(t)$.'
        self.answer='(B)'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(60,6000),scale=(16/120,16/12000),x_ticks=range(0,121,20),y_ticks=range(0,12001,1000),xlabel='t',ylabel='y',x_grid_step=20,y_grid_step=1000)
        f=np.array([[0,500],[10,11000],[50,11000],[60,10000],[100,10000],[110,0]])
        g=np.array([[0,10000],[35,10000],[40,9000],[80,9000],[100,11000],[120,11000]])
        ax.plot((f[:,0]-60)*(16/120),(f[:,1]-6000)*(16/12000),color='black',linewidth=1,zorder=3)
        ax.plot((g[:,0]-60)*(16/120),(g[:,1]-6000)*(16/12000),color='black',linewidth=1,linestyle=(0,(4,2)),zorder=3)
        label(ax,(112-60)*(16/120),(2000-6000)*(16/12000),'f',ha='left')
        label(ax,(102-60)*(16/120),(11000-6000)*(16/12000),'g',ha='left')
        return _finish(fig,ax,_dest(self.id,output_path))
