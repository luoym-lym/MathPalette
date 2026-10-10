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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana66.json'
_PROVENANCE_SHA256 = '3312dfad7c5322f59cc12a77d22749f382156608fd18fc2dbc688b707c3fbb75'
_SOURCE_COPY_PATH = 'originals/Ana66.png'
_SOURCE_COPY_SHA256 = '8bc3064df0e67ad534e60989366f306e35172e8cd98473c50e500ba4326ac3e9'

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

class Ana66:
    def __init__(self):
        _verify_helper()
        self.id='Ana66'; self.source_dataset='MathVerse'
        self.query='The linear function is graphed. Archimedes drained the water in his tub.\nThe amount of water left in the tub (in liters) as a function of time (in minutes) is graphed.\nHow much water was initially in the tub?'
        self.answer='Bugs Bunny'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(2.5,180),scale=(16/5,16/360),x_ticks=range(0,6),y_ticks=range(0,361,40),x_label_step=1,y_label_step=40,x_grid_step=1,y_grid_step=40,xlabel='Time (minutes)',ylabel='Water (liters)',xlabel_position=(.52,.035),xlabel_rotation=0)
        x=np.array([0,5]); y=np.array([360,0]); plot_curve(ax,(x-2.5)*16/5,(y-180)*16/360)
        return _finish(fig,ax,_dest(self.id,output_path))
