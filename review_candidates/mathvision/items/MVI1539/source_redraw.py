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
 fig.axes[0].patches[0].set_linewidth(2.5)
 with matplotlib.rc_context({'svg.fonttype':'path','svg.hashsalt':'MathVisionNative'}):fig.savefig(b,format='svg' if vector else 'png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,metadata={'Date':None} if vector else {'Software':'MathVision scoped native renderer'})
 r.plt.close(fig);return b.getvalue(),checks
if __name__=='__main__':
 a,checks=render();b,_=render();ia=np.array(Image.open(io.BytesIO(a)));ib=np.array(Image.open(io.BytesIO(b)));assert np.array_equal(ia,ib);assert ia.shape[:2]==(768,768);assert np.all(ia[:,:,3]==255)
 (p/'image.png').write_bytes(a);(p/'image.svg').write_bytes(render(True)[0])
 yy,xx=np.where(np.any(ia[:,:,:3]<245,axis=2));bounds=[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())]
 sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
 report={'source_sha256':sha(p/'original.jpg'),'scene_sha256':sha(p/'scene.json'),'renderer_sha256':sha(r.__file__),'script_sha256':sha(__file__),'protocol_sha256':sha(r.PROTOCOL_PATH),'output_sha256':sha(p/'image.png'),'two_render_pixels_equal':True,'opaque_768_square':True,'content_bbox_px':bounds,'constraints':checks,'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'visual_check':'pending','semantic_fill_override':'black solid holes and arrowheads, as source'}
 (p/'redraw_report.json').write_text(json.dumps(report,indent=2)+'\n')
