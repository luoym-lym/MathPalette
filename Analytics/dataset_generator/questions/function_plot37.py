"""Strict redraw for Ana37."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana37:
    def __init__(self):
        self.id='Ana37'; self.source_dataset='MathVerse'; self.query='The trigonometric function shown has an integer angular frequency. What is its period?'; self.answer = r'$\pi$'; self.answer_type='number'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-8,8,1200); plot_curve(ax,x,3*np.cos(2*(x-np.pi/4)))
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
