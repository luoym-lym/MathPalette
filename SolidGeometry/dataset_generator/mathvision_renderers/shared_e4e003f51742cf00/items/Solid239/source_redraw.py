"""Standalone native 3D frozen-scene renderer; no source raster is loaded.
The scene stores the paper/wood models in 3D, a single explicit parallel
projection, and edge visibility intervals bound to that projection.
"""
from pathlib import Path
import json,hashlib,io,platform,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch,Polygon
from PIL import Image
import PIL
HERE=Path(__file__).resolve().parent

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def project(s,xyz):
 p=s['projection'];return (np.asarray(xyz,float)-p['origin'])@np.asarray(p['matrix'],float).T+p['offset']
def validate(s):
 checks=[]; P=np.asarray(s['projection']['matrix']);v=np.asarray(s['projection']['toward_viewer']);assert P.shape==(2,3) and np.linalg.matrix_rank(P)==2 and np.linalg.norm(P@v)<1e-10
 assert s['visibility']['projection_sha256']==digest(s['projection'])
 if s['projection']['kind']=='orthographic': assert np.max(np.abs(P@P.T-np.eye(2)))<1e-10
 checks.append({'check':'projection_and_visibility_binding','passed':True})
 for k,p in s['points'].items():assert np.asarray(p).shape==(3,) and np.isfinite(p).all(),k
 for c in s['constraints']:
  ps=np.asarray([s['points'][p] for p in c.get('points',[])])
  if c['type']=='distance':result=float(np.linalg.norm(ps[1]-ps[0]));assert abs(result-c['value'])<1e-8
  elif c['type']=='coplanar':result=float(abs(np.linalg.det(np.stack((ps[1]-ps[0],ps[2]-ps[0],ps[3]-ps[0])))));assert result<1e-8
  elif c['type']=='perpendicular':result=float(np.dot(ps[1]-ps[0],ps[3]-ps[2]));assert abs(result)<1e-8
  elif c['type']=='angle':
   a,b=ps[0]-ps[1],ps[2]-ps[1];result=float(np.degrees(np.arccos(np.clip(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b),-1,1))));assert abs(result-c['degrees'])<1e-7
  else:raise ValueError(c['type'])
  checks.append({'id':c['id'],'type':c['type'],'basis':c['basis'],'actual':result,'passed':True})
 for o in s['objects']:
  assert o['type'] in ['face','polyline','arrow','text']
  if o['type']=='polyline':
   assert o['visibility'] in ['visible','hidden','occluded'];assert all(0<=a<b<=1 for a,b in o.get('intervals',[[0,1]]))
 return checks

def render_scene(s,vector=False):
 checks=validate(s)
 with matplotlib.rc_context({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','svg.hashsalt':'MathVisionTransformationNative3D','path.simplify':False}):
  fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white');ax=fig.add_axes([.05,.05,.9,.9]);ax.set_aspect('equal');ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_autoscale_on(False);ax.axis('off')
  for o in s['objects']:
   typ=o['type']
   if typ=='face':
    verts=[];codes=[]
    for ring_i,ring in enumerate([o['points']]+o.get('holes',[])):
     q=project(s,[s['points'][p] for p in ring]);area=sum(np.cross(q[(i+1)%len(q)]-q[i],q[(i+2)%len(q)]-q[(i+1)%len(q)]) for i in range(len(q))) if False else np.sum(q[:,0]*np.roll(q[:,1],-1)-q[:,1]*np.roll(q[:,0],-1))
     if (area>0)!=(ring_i==0):q=q[::-1]
     verts.extend(q.tolist()+[q[0].tolist()]);codes.extend([MPath.MOVETO]+[MPath.LINETO]*(len(q)-1)+[MPath.CLOSEPOLY])
    ax.add_patch(PathPatch(MPath(verts,codes),facecolor=o.get('fill','none'),edgecolor='none',linewidth=0,zorder=o.get('zorder',1),antialiased=True))
   elif typ=='polyline':
    if o['visibility']=='occluded':continue
    q=project(s,[s['points'][p] for p in o['points']]);style=(0,(4,3)) if o.get('linestyle')=='dashed' or o['visibility']=='hidden' else '-'
    ax.plot(q[:,0],q[:,1],color='black',lw=1,linestyle=style,solid_capstyle='round',dash_capstyle='butt',antialiased=True,zorder=o.get('zorder',5))
   elif typ=='arrow':
    q=project(s,[s['points'][p] for p in o['points']]);ax.plot(q[:,0],q[:,1],color='black',lw=1,solid_capstyle='round',zorder=6)
    # Arrow is a task-semantic motion symbol, not a dimension arrow.
    d=q[-1]-q[-2];d/=np.linalg.norm(d);n=np.array([-d[1],d[0]]);L=o.get('head_length',.12);w=L*.38;tri=np.array([q[-1],q[-1]-L*d+w*n,q[-1]-L*d-w*n]);ax.add_patch(Polygon(tri,facecolor='black',edgecolor='black',lw=1,zorder=6))
   else:
    q=project(s,[s['points'][o['point']]])[0];off=o.get('offset_pt',[0,0]);ax.annotate(o['text'],q,xytext=off,textcoords='offset points',ha=o.get('ha','center'),va=o.get('va','center'),fontsize=o.get('fontsize',16),fontstyle=o.get('fontstyle','normal'),color='black',annotation_clip=False,zorder=8)
  b=io.BytesIO();fig.savefig(b,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,metadata={'Date':None} if vector else {'Software':'MathVision native 3D frozen-scene renderer'});plt.close(fig)
 return b.getvalue(),checks

def render(vector=False):return render_scene(json.loads((HERE/'scene.json').read_text()),vector)
def image_bytes(s,vector=False):return render_scene(s,vector)
if __name__=='__main__':
 s=json.loads((HERE/'scene.json').read_text());a,c=render_scene(s);b,_=render_scene(s);ia=np.array(Image.open(io.BytesIO(a)).convert('RGBA'));ib=np.array(Image.open(io.BytesIO(b)).convert('RGBA'));assert np.array_equal(ia,ib) and ia.shape==(768,768,4) and ia[:,:,3].min()==255
 output=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'image.png';output.write_bytes(a)
 if len(sys.argv)==1:
  (HERE/'image.svg').write_bytes(render_scene(s,True)[0]);yy,xx=np.where((ia[:,:,:3]<245).any(2));box=[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
  report={'source_sha256':sha(HERE/'original.jpg'),'source_record_sha256':sha(HERE/'source.json'),'scene_sha256':sha(HERE/'scene.json'),'renderer_sha256':sha(__file__),'script_sha256':sha(__file__),'protocol_sha256':s['protocol_hashes'],'projection_sha256':digest(s['projection']),'output_sha256':sha(output),'two_render_pixels_equal':True,'opaque_768_square':True,'content_bbox_px':box,'constraints':c,'native_model':True,'renderer_kind':'standalone native 3D geometry + frozen parallel projection + explicit edge visibility; never reads original.jpg','dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'visual_check':'pending'}
  (HERE/'redraw_report.json').write_text(json.dumps(report,indent=2)+'\n')
