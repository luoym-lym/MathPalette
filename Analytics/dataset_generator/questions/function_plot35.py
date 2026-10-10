"""Strict redraw for Ana35."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana35:
    def __init__(self):
        self.id='Ana35'; self.source_dataset='MathVerse'; self.query='Write an equation for the transformation of f(x)=|x| as shown in the figure.'; self.answer='f(x)=-3|x-3|+3'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-8,8,1000); plot_curve(ax,x,-3*np.abs(x-3)+3)
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
