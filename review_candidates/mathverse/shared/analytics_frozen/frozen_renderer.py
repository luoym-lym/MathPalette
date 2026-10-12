"""Deterministic frozen-scene adapter to the unchanged Analytics common renderer."""
from pathlib import Path
import sys,json,math
import numpy as np
from matplotlib.patches import Circle,Ellipse,Arc
import common_renderer as R

def validate_scene(s):
 if s['view']['xlim']!=R.PROTOCOL['axes']['xlim'] or s['view']['ylim']!=R.PROTOCOL['axes']['ylim'] or s['view']['aspect']!='equal':raise ValueError('Analytics requires the fixed equal-unit window')
 p=s['points'];ids=set()
 def point(x):
  if isinstance(x,str):
   if x not in p:raise ValueError('Missing point '+x)
   x=p[x]
  a=np.asarray(x,dtype=float)
  if a.shape!=(2,) or not np.isfinite(a).all():raise ValueError('Expected a finite coordinate pair')
  return a
 def positive(x):
  if not isinstance(x,(int,float)) or not math.isfinite(x) or x<=0:raise ValueError('Expected a positive finite size')
 for x in p.values():point(x)
 for o in s['objects']:
  if o['id'] in ids:raise ValueError('Duplicate object ID')
  ids.add(o['id']);t=o['type']
  if any(k in o for k in ['color','alpha','linewidth','linestyle','fill','facecolor']):raise ValueError('Scene cannot override protocol styles')
  if t in ['circle','ellipse','arc']:
   c=point(o['center'])
   if t=='circle':positive(o['radius']);r=np.repeat(o['radius'],2)
   else:
    positive(o['width']);positive(o['height']);r=np.array([o['width'],o['height']])/2
   if t!='arc' and (np.any(c-r < -8-1e-8) or np.any(c+r > 8+1e-8)):raise ValueError('Closed geometry must fit fixed window')
   if t=='arc' and not np.isfinite([o['theta1'],o['theta2']]).all():raise ValueError('Arc angles must be finite')
  elif t=='line':
   if len(o['points'])<2:raise ValueError('Line requires at least two points')
   for x in o['points']:point(x)
  elif t=='point':point(o['point'])
  elif t=='right_angle':
   a,b,c=[point(x) for x in o['points']];u=a-b;v=c-b
   if np.linalg.norm(u)*np.linalg.norm(v)<1e-12 or abs(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)))>1e-8:raise ValueError('Right-angle marker must bind perpendicular nonzero rays')
   positive(o.get('size',.23))
  else:raise ValueError('Unsupported object '+t)
 for l in s['labels']:
  point(l['point'] if 'point' in l else l['xy']);point(l.get('offset_pt',[0,0]))
  if not isinstance(l['text'],str):raise ValueError('Label must contain text')
 return {'finite_points':len(p),'objects':len(ids),'fixed_window':True,'equal_units':True,'protocol_style_locked':True}

def render_scene(s,include_labels=True):
 checks=validate_scene(s);fig,ax=R.open_canvas();p=s['points']
 def xy(x):return p[x] if isinstance(x,str) else x
 for o in s['objects']:
  typ=o['type']
  if typ=='circle':R.add_styled_patch(ax,Circle(xy(o['center']),o['radius']))
  elif typ=='ellipse':R.add_styled_patch(ax,Ellipse(xy(o['center']),o['width'],o['height']))
  elif typ=='arc':R.add_styled_patch(ax,Arc(xy(o['center']),o['width'],o['height'],theta1=o['theta1'],theta2=o['theta2']))
  elif typ=='line':
   pts=np.array([p[x] if isinstance(x,str) else x for x in o['points']]);R.plot_curve(ax,pts[:,0],pts[:,1])
  elif typ=='point':
   point_xy=xy(o['point']);R.scatter_points(ax,[point_xy[0]],[point_xy[1]])
  elif typ=='right_angle':
   a,b,c=[np.array(xy(x)) for x in o['points']];u=(a-b)/np.linalg.norm(a-b)*o.get('size',.23);v=(c-b)/np.linalg.norm(c-b)*o.get('size',.23);pts=np.array([b+u,b+u+v,b+v]);R.plot_curve(ax,pts[:,0],pts[:,1])
 if include_labels:
  for i,l in enumerate(s['labels']):
   label_xy=xy(l['point']) if 'point' in l else l['xy'];off=l.get('offset_pt',[0,0]);art=ax.annotate(l['text'],xy=label_xy,xytext=off,textcoords='offset points',ha=l.get('ha','center'),va=l.get('va','center'),fontsize=R.FONT_SIZE,color=R.CURVE_COLOR,fontfamily=R.FONT_FAMILY,clip_on=False,zorder=5);art.set_gid('scene_label_'+str(i))
 R.lock_view(ax);fig.canvas.draw();return fig,checks

def draw(scene_path,output_path):
 s=json.loads(Path(scene_path).read_text());fig,checks=render_scene(s);return R.finalize(fig,output_path)
if __name__=='__main__':draw(sys.argv[1],sys.argv[2])
