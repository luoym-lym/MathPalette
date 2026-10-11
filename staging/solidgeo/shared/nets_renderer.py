"""Frozen preview-only renderer; not a SolidGeometry contract validator."""
import json,io,hashlib
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','svg.hashsalt':'solidgeo-nets-v1','mathtext.fontset':'dejavusans'})
def image_bytes(s,fmt='png'):
 fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white'); ax=fig.add_axes([.05,.05,.9,.9]);ax.set_aspect('equal');ax.set_axis_off();ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_autoscale_on(False)
 for o in s['objects']:
  if o['type']=='polygon':
   from matplotlib.patches import Polygon
   ax.add_patch(Polygon([s['points'][p] for p in o['points']],closed=True,facecolor=o['fill'],edgecolor='none',zorder=1));continue
  if o['type']!='segment':raise ValueError(o['type'])
  a,b=[s['points'][p] for p in o['points']];ax.plot([a[0],b[0]],[a[1],b[1]],color='black',linewidth=1,linestyle=(0,(4,3)) if o.get('dashed') else '-',solid_capstyle='round',antialiased=True)
 for l in s['labels']:
  p=s['points'][l['anchor']]; ax.annotate(l['text'],p,xytext=l.get('offset_pt',[0,0]),textcoords='offset points',ha=l.get('ha','center'),va=l.get('va','center'),fontsize=18 if l.get('role')=='point' else 16,fontstyle='italic' if l.get('role')=='point' else 'normal',color='black',clip_on=False)
 b=io.BytesIO();fig.savefig(b,format=fmt,dpi=100,facecolor='white',transparent=False,metadata={'Date':None} if fmt=='svg' else {'Software':'MathPalette net renderer'});plt.close(fig);return b.getvalue()
