"""Frozen preview-only renderer; not a SolidGeometry contract validator."""
from pathlib import Path
import os,io,json,hashlib,math
os.environ.setdefault('MPLCONFIGDIR','/tmp/solidgeo-views-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','svg.hashsalt':'solidgeo-views-v1','lines.solid_capstyle':'round','lines.dash_capstyle':'butt'})
def render(s,vector=False):
 fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white');ax=fig.add_axes([.05,.05,.9,.9]);ax.set_aspect('equal');ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_autoscale_on(False);ax.axis('off')
 for o in s['objects']:
  p=np.array(o['xy']);style=(0,(4,3)) if o.get('linestyle')=='dashed' else '-'
  if o['type']=='polyline':ax.plot(p[:,0],p[:,1],color='black',lw=1,ls=style,antialiased=True)
  elif o['type']=='semantic_fill':ax.fill(p[:,0],p[:,1],facecolor=o.get('color','black'),edgecolor='black',lw=1)
  elif o['type']=='point':ax.scatter(p[:,0],p[:,1],s=36,c='black',edgecolors='black',linewidths=1,zorder=4)
  else:raise ValueError(o['type'])
 for l in s['labels']:
  ax.annotate(l['text'],l['xy'],xytext=l.get('offset_pt',[0,0]),textcoords='offset points',fontsize=18 if l.get('role')=='vertex' else 16,fontstyle='italic' if l.get('role')=='vertex' else 'normal',ha=l.get('ha','center'),va=l.get('va','center'),color='black',annotation_clip=False)
 b=io.BytesIO();fig.savefig(b,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,metadata={'Date':None} if vector else {'Software':'SolidGeo protocol redraw'});plt.close(fig);return b.getvalue()
