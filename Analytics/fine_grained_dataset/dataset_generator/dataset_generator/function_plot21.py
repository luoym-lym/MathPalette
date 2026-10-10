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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana21.json'
_PROVENANCE_SHA256 = 'efb09d7657958bb47a2280f909a448b0f38df11e934c30bbdbe17efbcbfabdab'
_SOURCE_COPY_PATH = 'originals/Ana21.png'
_SOURCE_COPY_SHA256 = '6d88e6d1823e2a53e9c7a7586cb1d9ee90bbdc70d0c5195b92f1654bec473bdd'

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

class Ana21:
    def __init__(self):
        _verify_helper()
        self.id='Ana21'; self.source_dataset='MathVerse'
        self.query='Find the coordinates of the midpoint for each diagonal.'
        self.answer='(2,-2)'; self.answer_type='string'; self.subject='analytic geometry'; self.level='high school'
        self.center=(2,2); self.scale=8/9
    def draw(self, num=0, output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=self.center,scale=self.scale,x_ticks=range(-7,12),y_ticks=range(-3,8))
        x,y=map_point(-6,-1,self.center,self.scale); w,h=16*self.scale,6*self.scale
        ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor='black',linewidth=1,zorder=2))
        for a,b in [((-6,5),(10,-1)),((-6,-1),(10,5))]:
            p=map_point(*a,self.center,self.scale); q=map_point(*b,self.center,self.scale)
            ax.plot([p[0],q[0]],[p[1],q[1]],color='black',linewidth=1,linestyle=(0,(5,3)),zorder=2)
        for p in [(-6,5),(10,5),(-6,-1),(10,-1)]:
            q=map_point(*p,self.center,self.scale); scatter_points(ax,*q)
        for p,t,ha,va in [((-6,5),'(-6, 5)','right','bottom'),((10,5),'(10, 5)','left','bottom'),((-6,-1),'(-6, -1)','right','top'),((10,-1),'(10, -1)','left','top')]:
            q=map_point(*p,self.center,self.scale); label(ax,q[0],q[1],t,ha=ha,va=va)
        return _finish(fig,ax,_dest(self.id,output_path))
