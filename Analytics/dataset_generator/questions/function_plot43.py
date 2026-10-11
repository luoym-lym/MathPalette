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

class Ana43:
    def __init__(self):
        self.id='Ana43'; self.source_dataset='MathVerse'
        self.query = 'What is the slope of the figure?'
        self.answer = '\\[=\\frac{7}{4}\\]'; self.answer_type='number'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-4,5,300); plot_curve(ax,x,7*x/4-1)
        return _finish(fig,ax,_dest(self.id,output_path))
