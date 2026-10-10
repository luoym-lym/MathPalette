"""Strict redraw for Ana33."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana33:
    def __init__(self):
        self.id='Ana33'; self.source_dataset='MathVerse'; self.query='Write an equation for the graphed function f.'; self.answer='When x<=-3 $f(x) = -x-5$, when x>3, $f(x)=x+1$'; self.answer_type='string'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-8,8,1000); plot_curve(ax,x,np.abs(x+3)-2); label(ax,4.2,5.6,'f',ha='left')
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
