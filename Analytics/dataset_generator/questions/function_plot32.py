"""Strict redraw for Ana32."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana32:
    def __init__(self):
        self.id='Ana32'; self.source_dataset='MathVerse'; self.query='Estimate the intervals on which the function is increasing or decreasing.'; self.answer='\\[The function is increasing on (-\\infty,-2.5) \\cup(1, \\infty), and decreasing on (-2.5,1)\\]'; self.answer_type='expression'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-4.4,3.15,1000); plot_curve(ax,x,x**3/3+0.75*x**2-2.5*x)
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
