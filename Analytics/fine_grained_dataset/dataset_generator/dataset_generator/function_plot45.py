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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana45.json'
_PROVENANCE_SHA256 = 'f66c05e31fd3061edf6e8d2710de72c3c4dbd1fc15793333e1e7ee3f83b90e8a'
_SOURCE_COPY_PATH = 'originals/Ana45.png'
_SOURCE_COPY_SHA256 = 'c1b5f6ca197551097ed92bda0bb3856d86a10077749374bfb2a2a5e5cf3971b2'

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

class Ana45:
    def __init__(self):
        _verify_helper()
        self.id='Ana45'; self.source_dataset='MathVerse'
        self.query='Below is the graph of a trigonometric function. What is the amplitude of the function?'
        self.answer='4.6'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(2,3),scale=(16/14,16/14),x_ticks=range(-5,11),y_ticks=range(-4,11),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-5,9,800); y=1.2+4.6*np.cos(.75*x)
        plot_curve(ax,(x-2)*(16/14),(y-3)*(16/14))
        for px,py,txt in [(2*np.pi/3,1.2,'(2π/3, 1.2)'),(4*np.pi/3,-3.4,'(4π/3, −3.4)')]:
            xx=(px-2)*16/14; yy=(py-3)*16/14; scatter_points(ax,xx,yy); label(ax,xx+.25,yy+.4,txt,ha='left')
        ax.axhline((1.2-3)*16/14,color='black',linewidth=1,linestyle=(0,(4,3)),zorder=1)
        return _finish(fig,ax,_dest(self.id,output_path))
