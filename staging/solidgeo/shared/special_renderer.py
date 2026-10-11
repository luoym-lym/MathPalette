"""Frozen preview-only renderer; not a SolidGeometry contract validator."""
"""Protocol-style frozen geometric renderer; construction never runs on reproduction."""
from pathlib import Path
import json,math,io,hashlib,platform,shutil,os
os.environ.setdefault("MPLCONFIGDIR","/tmp/mpl-solidgeo")
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
def sha(x):return hashlib.sha256(x if isinstance(x,bytes) else Path(x).read_bytes()).hexdigest()
def plain(x):return np.asarray(x,float).tolist()
def render(s,vector=False):
 with matplotlib.rc_context({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'solidgeo-frozen-special','lines.antialiased':True}):
  f=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white');ax=f.add_axes([.05,.05,.9,.9]);ax.set_aspect('equal');ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_autoscale_on(False);ax.axis('off')
  M=np.array(s['projection']['matrix']);o=np.array(s['projection']['origin']);offset=np.array(s['projection']['offset']);project=lambda p:(np.asarray(p)-o)@M.T+offset
  lines=[];texts=[]
  for obj in s['objects']:
   xy=project(obj['world_points'])
   if obj['type']=='fill':ax.add_patch(Polygon(xy,closed=True,facecolor='#E6E6E6',edgecolor='none',zorder=0))
   elif obj['type']=='point': ax.plot(*xy[0],'o',color='black',markersize=6,zorder=4)
   else:
    a,=ax.plot(xy[:,0],xy[:,1],color='black',lw=1,ls=(0,(4,3)) if obj['visibility']=='hidden' or obj.get('linestyle')=='dashed' else '-',solid_capstyle='round',dash_capstyle='butt',zorder=2 if obj['visibility']=='hidden' else 3);lines.append((obj['id'],a))
  for lab in s['labels']:
   a=ax.annotate(lab['text'],project(lab['world_anchor']),xytext=lab['offset_pt'],textcoords='offset points',ha=lab.get('ha','center'),va=lab.get('va','center'),fontsize=18 if lab['type']=='vertex' else 16,fontstyle='italic' if lab['type']=='vertex' else 'normal',color='black',annotation_clip=False,zorder=5);texts.append((lab['id'],a))
  f.canvas.draw();ren=f.canvas.get_renderer();coll=[];boxes=[]
  for id,a in texts:
   b=a.get_window_extent(ren)
   for oid,ob in boxes:
    if b.overlaps(ob):coll.append([id,oid,'text'])
   for oid,l in lines:
    if l.get_path().transformed(l.get_transform()).intersects_bbox(b.padded(-1),filled=False):coll.append([id,oid,'line'])
   boxes.append((id,b))
  b=io.BytesIO();f.savefig(b,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,metadata={'Date':None} if vector else {'Software':'SOLIDGEO protocol redraw'});plt.close(f);return b.getvalue(),coll

