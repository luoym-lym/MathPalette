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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana46.json'
_PROVENANCE_SHA256 = 'd709c0abf3fc62a4137f28917e65a309ccc68b3ea01e942e974fcbb4abe6270d'
_SOURCE_COPY_PATH = 'originals/Ana46.png'
_SOURCE_COPY_SHA256 = '539931bbdd002e0d7f312d2322acf7c45d05a6b8596236b30e77e4d5336d4b07'

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

class Ana46:
    def __init__(self):
        _verify_helper()
        self.id='Ana46'; self.source_dataset='MathVerse'
        self.query='Below is the graph of a trigonometric function. What is the period of the function? Give an exact value.'
        self.answer='\\[\\pi\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(1,-4.5),scale=16/9,x_ticks=range(-3,6),y_ticks=range(-9,1),x_grid_step=1,y_grid_step=1)
        x=np.linspace(-3,5,1000); y=-5.35+3.15*np.cos(2*(x-np.pi/4))
        plot_curve(ax,(x-1)*16/9,(y+4.5)*16/9)
        for px,py,txt,offset in [(np.pi/4,-2.2,r'$(\frac{\pi}{4},-2.2)$',(0,12)),(3*np.pi/4,-8.5,r'$(\frac{3\pi}{4},-8.5)$',(0,-26))]:
            ax.scatter((px-1)*16/9,(py+4.5)*16/9,s=22,c='#d69a55',zorder=4)
            ax.annotate(txt,((px-1)*16/9,(py+4.5)*16/9),xytext=offset,textcoords='offset points',ha='center',va='bottom' if offset[1]>0 else 'top',fontsize=12,zorder=5)
        return _finish(fig,ax,_dest(self.id,output_path))
