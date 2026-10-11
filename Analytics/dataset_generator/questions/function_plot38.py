"""Strict redraw for Ana38."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
_ROOT=Path(__file__).resolve().parents[1]
for _p in (_ROOT,_ROOT/"dataset_generator"):
    if str(_p) not in sys.path: sys.path.insert(0,str(_p))
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize
class Ana38:
    def __init__(self):
        self.id='Ana38'; self.source_dataset='MathVerse'; self.query='The trigonometric function shown has a non-integer angular frequency. What is its period?'; self.answer = r'$4\pi$'; self.answer_type='number'; self.subject='functions'; self.level='high school'
    def draw(self,num=0,output_path=None):
        fig,ax=open_canvas()
        x=np.linspace(-8,8,1400); plot_curve(ax,x,3*np.cos((x-3*np.pi/2)/2))
        dest=Path(output_path) if output_path is not None else _ROOT.parent/'image'/f'{self.id}.png'
        return finalize(fig,dest)
