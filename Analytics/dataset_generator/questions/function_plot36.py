"""Strict redraw for Ana36."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana36:
    def __init__(self):
        self.id='Ana36'; self.source_dataset='MathVerse'; self.query='Below is the graph of a trigonometric function. It has an amplitude of 1.8 . What is the midline equation of the function?'; self.answer='0.2'; self.answer_type='number'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-8,8,1000); x0=-np.pi/3; y=0.2+1.8*np.cos(2*np.pi*(x-x0)/5.2); plot_curve(ax,x,y)
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
