from pathlib import Path
import sys,json,hashlib,io,platform
import numpy as np
from PIL import Image
import PIL,matplotlib
p=Path(__file__).resolve().parent; repo=p.parents[3]
sys.path.insert(0,str(repo/'PlaneGeometry/dataset_generator'))
import common_renderer as r
s=json.loads((p/'scene.json').read_text()); protocol=r.read_json(r.PROTOCOL_PATH)
# Explicit task-semantic black holes/arrowheads, not decorative fill.
protocol['fill']['semantic_facecolor']='#000000';protocol['fill']['semantic_alpha']=1
def render(vector=False):
 fig,checks=r.render_scene(s,protocol); b=io.BytesIO()
 from matplotlib.path import Path as MP
 pi=li=0
 for ob in s['objects']:
  artists=[]
  if ob['type']=='polygon':
   if ob.get('semantic_fill'):
    artists=[fig.axes[0].patches[pi],fig.axes[0].patches[pi+1]]
    if ob.get('fill_color'):artists[0].set_facecolor(ob['fill_color'])
    if ob.get('no_outline'):
     for art in artists:art.set_edgecolor('none')
    pi+=2
   else:artists=[fig.axes[0].patches[pi]];pi+=1
  elif ob['type']=='segment':
   artists=[fig.axes[0].lines[li]]
   if ob.get('stroke_color'):artists[0].set_color(ob['stroke_color']);artists[0].set_linewidth(1.0)
   li+=1
  elif ob['type'] in ('circle','arc','angle_arc'):pi+=1
  if ob.get('clip_polygon'):
   for art in artists:art.set_clip_path(MP(ob['clip_polygon']+[ob['clip_polygon'][0]]),fig.axes[0].transData)
 with matplotlib.rc_context({'svg.fonttype':'path','svg.hashsalt':'MathVisionNative'}):fig.savefig(b,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,metadata={'Date':None} if vector else {'Software':'MathVision scoped native renderer'})
 r.plt.close(fig);return b.getvalue(),checks
if __name__=='__main__':
 a,checks=render();b,_=render();ia=np.array(Image.open(io.BytesIO(a)));ib=np.array(Image.open(io.BytesIO(b)));assert np.array_equal(ia,ib);assert ia.shape[:2]==(768,768);assert np.all(ia[:,:,3]==255)
 (p/'image.png').write_bytes(a);(p/'image.svg').write_bytes(render(True)[0])
 yy,xx=np.where(np.any(ia[:,:,:3]<245,axis=2));bounds=[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())]
 sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
 report={'source_sha256':sha(p/'source.jpg'),'scene_sha256':sha(p/'scene.json'),'renderer_sha256':sha(r.__file__),'script_sha256':sha(__file__),'protocol_sha256':sha(r.PROTOCOL_PATH),'output_sha256':sha(p/'image.png'),'two_render_pixels_equal':True,'opaque_768_square':True,'content_bbox_px':bounds,'constraints':checks,'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'visual_check':'pending','semantic_fill_override':'black solid holes and arrowheads, as source'}
 (p/'redraw_report.json').write_text(json.dumps(report,indent=2)+'\n')
