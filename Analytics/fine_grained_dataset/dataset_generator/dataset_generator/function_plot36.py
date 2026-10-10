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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana36.json'
_PROVENANCE_SHA256 = '917617a27ebb217ee4aede5d250da4259355a44f40f8646b8101cd2c761fbc6b'
_SOURCE_COPY_PATH = 'originals/Ana36.png'
_SOURCE_COPY_SHA256 = '0ab6dd2a10dc572c660593b9bd4cd95a0af40876ae810cf3f8485f36e83dfaa3'

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

class Ana36:
    def __init__(self):
        _verify_helper()
        self.id='Ana36'; self.source_dataset='MathVerse'
        self.query='Write the domain and range of the hyperbolic function using interval notation.'
        self.answer='\\[domain: [-6,-\\frac{1}{6}] \\cup[\\frac{1}{6}, 6] and range: [-6,-\\frac{1}{6}\\right] \\cup[\\frac{1}{6}, 6]\\]'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(0,0),scale=1.2,x_ticks=range(-6,7),y_ticks=range(-6,7),x_grid_step=1,y_grid_step=1)
        for lo,hi in [(-6,-1/6),(1/6,6)]:
            x=np.linspace(lo,hi,600); plot_curve(ax,x*1.2,(1/x)*1.2)
        for px,py in [(-6,-1/6),(-1/6,-6),(1/6,6),(6,1/6)]: scatter_points(ax,px*1.2,py*1.2)
        ax.axvline(0,color='#c62828',linewidth=1,linestyle=(0,(4,3)),zorder=1)
        ax.annotate(r'$(-6,-\frac{1}{6})$',(-7.2,-.2),xytext=(12,-36),textcoords='offset points',ha='left',va='top',fontsize=12)
        ax.annotate(r'$(-\frac{1}{6},-6)$',(-.2,-7.2),xytext=(-60,14),textcoords='offset points',ha='right',va='bottom',fontsize=12)
        ax.annotate(r'$(\frac{1}{6},6)$',(.2,7.2),xytext=(56,4),textcoords='offset points',ha='left',va='center',fontsize=12)
        ax.annotate(r'$(6,\frac{1}{6})$',(7.2,.2),xytext=(-4,48),textcoords='offset points',ha='right',va='bottom',fontsize=12)
        return _finish(fig,ax,_dest(self.id,output_path))
