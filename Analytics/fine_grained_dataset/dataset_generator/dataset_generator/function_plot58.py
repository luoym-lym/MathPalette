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

_PROVENANCE_PATH = 'provenance/MathVerse/Ana58.json'
_PROVENANCE_SHA256 = 'a217c9fff557294996e62a3e4163773c81ca48d3e45b18c79cb9dc8d758508fc'
_SOURCE_COPY_PATH = 'originals/Ana58.png'
_SOURCE_COPY_SHA256 = '128faac445143e883f47bf69e26f47c207fe4cd577f630259ea3b003be28bf4f'

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

class Ana58:
    def __init__(self):
        _verify_helper()
        self.id='Ana58'; self.source_dataset='MathVerse'
        self.query="In a memory study, subjects are asked to memorize some content and recall as much as they can remember each day thereafter. Each day, Maximilian finds that he has forgotten $15 \\%$ of what he could recount the day before. Lucy also took part in the study. The given graphs represent the percentage of content that Maximilian (gray) and Lucy (black) could remember after $t$ days.\n\nOn each day, what percentage of the previous day's content did Lucy forget?"
        self.answer='$13 \\%$'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas(); set_view(ax,center=(5,50),scale=(1.6,.16),x_ticks=range(0,11),y_ticks=range(0,101,20),xlabel='days',ylabel='recall percentage',x_label_step=100,y_label_step=100,grid=False)
        t=np.linspace(0,10,700); lucy=100*.87**t; maxm=100*.85**t
        ax.plot((t-5)*1.6,(lucy-50)*.16,color='black',linewidth=1,zorder=2)
        ax.plot((t-5)*1.6,(maxm-50)*.16,color='#888888',linewidth=1,zorder=2)
        return _finish(fig,ax,_dest(self.id,output_path))
