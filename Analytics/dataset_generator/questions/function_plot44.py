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

class Ana44:
    def __init__(self):
        self.id='Ana44'; self.source_dataset='MathVerse'
        self.query = 'Write an equation that represents the figure.\nUse exact numbers.'
        self.answer = '$y+3=\\frac{3}{4}(x-2)$'; self.answer_type='expression'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-4.5,8,400); y=.75*(x-2)-3; plot_curve(ax,x,y)
        return _finish(fig,ax,_dest(self.id,output_path))
