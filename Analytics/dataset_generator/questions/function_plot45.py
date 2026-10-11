"""Strict MathVerse redraw using the Analytics protocol coordinate plane."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

_ROOT=Path(__file__).resolve().parents[1]
_DATASET_ROOT=_ROOT.parent
if str(_ROOT) not in sys.path: sys.path.insert(0,str(_ROOT))
from common_renderer import open_canvas, plot_curve, scatter_points, label, aux_hline, finalize

def _finish(fig, ax, destination):
    return finalize(fig, destination)

def _dest(qid, output_path):
    return Path(output_path) if output_path is not None else _DATASET_ROOT/'image'/f'{qid}.png'

class Ana45:
    def __init__(self):
        self.id='Ana45'; self.source_dataset='MathVerse'
        self.query = 'Let $f$ be the function given by the following graph. What is the domain of $f$?'
        self.answer = '$[-5,-3) \\cup(-3,5]$'; self.answer_type='expression'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        parts=[([-5,1],[-3,2]),([-3,2],[-1,4]),([-1,5],[3,3],[5,1])]
        for pts in parts:
         p=np.array(pts,float); plot_curve(ax,p[:,0],p[:,1])
        scatter_points(ax,[-5],[1]); scatter_points(ax,[-3],[2],open_marker=True); scatter_points(ax,[-1],[4],open_marker=True); scatter_points(ax,[-1],[5]); scatter_points(ax,[5],[1])
        return _finish(fig,ax,_dest(self.id,output_path))
