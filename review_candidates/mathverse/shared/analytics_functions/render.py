"""Reproducible strict Analytics candidate renderer. No source pixels are read."""
from pathlib import Path
import os

import json
import numpy as np
from matplotlib.patches import Ellipse, Circle, Polygon, Rectangle
from common_renderer import open_canvas,plot_curve,scatter_points,label,finalize,add_styled_patch,fill_region,fill_polygon
ROOT=Path(__file__).resolve().parent
NAMES={'np':np,'pi':np.pi,'sin':np.sin,'cos':np.cos,'tan':np.tan,'exp':np.exp,'log':np.log,'sqrt':np.sqrt,'abs':np.abs,'cbrt':np.cbrt,'where':np.where,'minimum':np.minimum,'maximum':np.maximum}
def calc(expr,x):
 with np.errstate(all='ignore'):
  a=eval(expr,{'__builtins__':{}},{**NAMES,'x':x})
  return np.broadcast_to(a,np.shape(x)).astype(float)
def build(scene):
 fig,ax=open_canvas()
 for o in scene['objects']:
  t=o['kind']
  if t=='function':
   x=np.linspace(*o.get('domain',[-8,8]),o.get('samples',4001));plot_curve(ax,x,calc(o['expression'],x))
  elif t=='parametric':
   x=np.linspace(*o['domain'],o.get('samples',2001));plot_curve(ax,calc(o['x'],x),calc(o['y'],x))
  elif t=='polyline':
   a=np.array(o['points'],float);plot_curve(ax,a[:,0],a[:,1])
  elif t=='points':
   a=np.array(o['points'],float);scatter_points(ax,a[:,0],a[:,1],open_marker=o.get('open',False))
  elif t=='ellipse':add_styled_patch(ax,Ellipse(o['center'],o['width'],o['height'],angle=o.get('angle',0)))
  elif t=='polygon':add_styled_patch(ax,Polygon(o['points'],closed=True))
  elif t=='fill':
   x=np.linspace(*o.get('domain',[-8,8]),4001);fill_region(ax,x,calc(o['lower'],x),calc(o['upper'],x))
  elif t=='fill_polygon':
   a=np.array(o['points'],float);fill_polygon(ax,a[:,0],a[:,1])
  elif t=='label':label(ax,*o['xy'],o['text'],ha=o.get('ha','center'),va=o.get('va','center'))
  else:raise ValueError(t)
 return fig,ax

def draw(qid,output_path=None):
 scene=json.loads((ROOT/'scenes'/f'{qid}.json').read_text())
 fig,ax=build(scene)
 return finalize(fig,output_path or ROOT/'images'/f'{qid}.png')
if __name__=='__main__':
 import sys
 print(draw(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else None))
