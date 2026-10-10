"""Strict redraw for Ana25."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
from matplotlib.patches import Circle, Rectangle, Ellipse
_ROOT=Path(__file__).resolve().parents[1]
_DATASET_ROOT=_ROOT.parent
if str(_ROOT) not in sys.path: sys.path.insert(0,str(_ROOT))
from common_renderer import open_canvas, plot_curve, scatter_points, label, finalize, lock_view
def _finish(fig,ax,destination):
    result=finalize(fig,destination)
    if fig.number in __import__("matplotlib.pyplot",fromlist=["plt"]).get_fignums(): lock_view(ax)
    return result
def _dest(qid,output_path):
    return Path(output_path) if output_path is not None else _DATASET_ROOT/"image"/f"{qid}.png"
class Ana25:
    def __init__(self):
        self.id="Ana25"; self.source_dataset="MathVerse"
        self.query='Consider the circle on the graph. Find its equation in standard form.'; self.answer='$(x-1)^2+(y-2)^2=16$'; self.answer_type="string"; self.subject="analytic geometry" if 25<32 else "functions"; self.level="high school"
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        ax.add_patch(Circle((1,2),4,fill=False)); scatter_points(ax,1,2)
        return _finish(fig,ax,_dest(self.id,output_path))
