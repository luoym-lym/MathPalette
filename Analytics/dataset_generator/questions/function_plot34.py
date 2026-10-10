"""Strict redraw for Ana34."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana34:
    def __init__(self):
        self.id='Ana34'; self.source_dataset='MathVerse'; self.query='Find the absolute maximum of the graphed cubic on its displayed closed domain.'; self.answer='6'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-3.3,3.3,900); plot_curve(ax,x,(125/243)*(x**3-9.72*x)); scatter_points(ax,-3.3,(125/243)*((-3.3)**3-9.72*(-3.3))); scatter_points(ax,3.3,(125/243)*((3.3)**3-9.72*(3.3)))
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
