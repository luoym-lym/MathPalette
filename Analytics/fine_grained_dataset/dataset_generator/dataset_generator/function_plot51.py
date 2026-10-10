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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana51.json'
_PROVENANCE_SHA256 = '4874867f26d0d07bcd8021582596d42be6d78ee659e404ddfdb91bb26791a894'
_SOURCE_COPY_PATH = 'originals/Ana51.png'
_SOURCE_COPY_SHA256 = 'c51cc05671f48fa78e3a344f8cf5a0b7b169452c22561b86495cf0692d7a0a3d'

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

class Ana51:
    def __init__(self):
        _verify_helper()
        self.id='Ana51'; self.source_dataset='MathVerse'
        self.query='\\[10 \\cdot f(7) + 9 \\cdot g(-1) =\\]'
        self.answer='-1'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=.8,x_ticks=range(-10,11),y_ticks=range(-10,11),x_label_step=2,y_label_step=2,x_grid_step=1,y_grid_step=2)
        f=np.array([[-10,0],[-9,-1],[-7,-1],[-6,1],[-5,-1],[-3,-1],[-2,0],[-1,-2],[0,-2],[1,0],[2,-1],[3,-2],[5,-2],[6,-3],[7,-1],[8,-2],[9,-3],[10,-5]])
        g=np.array([[-10,-2],[-9,-2],[-8,0],[-6,0],[-5,-1],[-2,-1],[-1,1],[0,3],[2,5],[3,3],[4,4],[5,3],[6,5],[7,5],[8,6],[9,6],[10,5]])
        ax.plot(f[:,0]*.8,f[:,1]*.8,color='black',linewidth=1,zorder=3)
        ax.plot(g[:,0]*.8,g[:,1]*.8,color='black',linewidth=1,linestyle=(0,(4,2)),zorder=3)
        label(ax,4.8*.8,-2.0*.8,'f'); label(ax,8.2*.8,6*.8,'g')
        return _finish(fig,ax,_dest(self.id,output_path))
