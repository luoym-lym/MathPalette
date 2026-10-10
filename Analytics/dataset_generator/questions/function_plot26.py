"""Strict redraw for Ana26."""
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
class Ana26:
    def __init__(self):
        self.id="Ana26"; self.source_dataset="MathVerse"
        self.query='Write the equation of the figure.'; self.answer='\\[(x+3)^2+(y+3)^2=9\\]'; self.answer_type="string"; self.subject="analytic geometry" if 27<32 else "functions"; self.level="high school"
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        ax.add_patch(Circle((-3,-3),3,fill=False)); scatter_points(ax,-3,-3)
        return _finish(fig,ax,_dest(self.id,output_path))
