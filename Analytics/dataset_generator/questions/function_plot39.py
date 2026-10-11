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

class Ana39:
    def __init__(self):
        self.id='Ana39'; self.source_dataset='MathVerse'
        self.query = '\\[What is the domain of h?\nChoices:\nA:-5 \\leq x \\leq 7\nB:-5 \\leq x \\leq 4\nC:-5 \\leq x \\leq 5\nD:-5 \\leq x \\leq 6\\]'
        self.answer = 'B'; self.answer_type='choice'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        p=np.array([[-5,4],[-3,3],[0,7],[3,1],[4,-5]],float)
        plot_curve(ax,p[:,0],p[:,1]); scatter_points(ax,p[[0,-1],0],p[[0,-1],1])
        label(ax,2,1.8,'h')
        return _finish(fig,ax,_dest(self.id,output_path))
