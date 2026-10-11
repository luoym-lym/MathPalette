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

class Ana41:
    def __init__(self):
        self.id='Ana41'; self.source_dataset='MathVerse'
        self.query = 'f(x)=x^2+x-6. How many roots do the functions have in common, f(x) and g(x)?\nChoices:\nA:$f$ and $g$ share the same root(s).\nB:$f$ and $g$ share one root in common but each have another root that is not shared.\nC:$f$ and $g$ share no roots in common.'
        self.answer = 'B'; self.answer_type='choice'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-4,4,500); y=(x-.5)**2-2.25
        plot_curve(ax,x,y); label(ax,3,4,'y = g(x)',ha='left')
        return _finish(fig,ax,_dest(self.id,output_path))
