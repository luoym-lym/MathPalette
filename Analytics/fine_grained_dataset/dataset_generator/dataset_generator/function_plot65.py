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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana65.json'
_PROVENANCE_SHA256 = '15e006470a2e316e27646cbd80f7483d75c5a2d6e3df358dc3a3431b62cf2b8a'
_SOURCE_COPY_PATH = 'originals/Ana65.jpg'
_SOURCE_COPY_SHA256 = '660b15d6336c98e1339c8f75c9501c0dc3319b0af7226c15ddab3cf29cdc3ad9'

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

class Ana65:
    def __init__(self):
        _verify_helper()
        self.id='Ana65'; self.source_dataset='MathVerse'
        self.query="The logarithm function and a line are graphed. A pharmaceutical scientist making a new medication wonders how much of the active ingredient to include in a dose. They are curious how long different amounts of the active ingredient will stay in someone's bloodstream.\n\nThe amount of time (in hours) the active ingredient remains in the bloodstream can be modeled by $f(x)$, where $x$ is the initial amount of the active ingredient (in milligrams). Here is the graph of $f$ and the graph of the line $y=4$.\n\nWhich statements represent the meaning of the intersection point of the graphs?\n\nChoose all answers that apply:\nChoices:\nA:It describes the amount of time the active ingredient stays in the bloodstream if the initial amount of the active ingredient is $4 \\mathrm{mg}$.\nB:\nC:It gives the solution to the equation $-1.25 \\cdot \\ln \\left(\\frac{1}{x}\\right)=4$.\nD:It describes the situation where the initial amount of the active ingredient is equal to how long it stays in the bloodstream.\nE:\nF:It gives the initial amount of the active ingredient such that the last of the active ingredient leaves the bloodstream after 4 hours."
        self.answer='C'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(32.5,3.5),scale=(16/65,16/7),x_ticks=range(0,66,10),y_ticks=range(0,8),x_label_step=10,y_label_step=1,x_grid_step=10,y_grid_step=1,xlabel='x',ylabel='y')
        x=np.linspace(.2,65,900); y=1.25*np.log(x)
        plot_curve(ax,(x-32.5)*16/65,(y-3.5)*16/7)
        ax.axhline((4-3.5)*16/7,color='black',linewidth=1,zorder=2)
        ax.annotate(r'$y=4$',((7-32.5)*16/65,(4.35-3.5)*16/7),fontsize=12,ha='left',va='bottom')
        ax.annotate(r'$f$',((57-32.5)*16/65,(6.2-3.5)*16/7),fontsize=12,ha='left',va='bottom')
        ax.annotate(r'$f(x)=-1.25\cdot\ln\left(\frac{1}{x}\right)$',((31-32.5)*16/65,(2.4-3.5)*16/7),fontsize=12,ha='center',va='center')
        return _finish(fig,ax,_dest(self.id,output_path))
