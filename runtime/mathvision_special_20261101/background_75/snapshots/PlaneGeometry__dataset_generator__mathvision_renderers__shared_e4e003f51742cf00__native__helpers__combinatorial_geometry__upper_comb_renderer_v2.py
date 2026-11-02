"""Scoped semantic-fill override; geometry and validation delegated unchanged."""
from pathlib import Path
import sys,copy,io
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'PlaneGeometry/dataset_generator'))
import common_renderer as base
from PIL import Image
PROTOCOL_PATH=base.PROTOCOL_PATH

def image_bytes(scene):
 protocol=base.read_json(PROTOCOL_PATH)
 style=scene.get('semantic_fill_style')
 if style:
  if style!={'semantic_facecolor':'#000000','semantic_alpha':1.0}:raise ValueError('Unsupported semantic fill override')
  protocol['fill'].update(style)
 fig,checks=base.render_scene(scene,protocol)
 # Source grid/foreground distinction is semantic, not decorative.
 for item in scene['objects']:
  if item.get('role')=='background_grid':
   if item['type']!='segment':raise ValueError('Background grid must be native segment')
   a,b=base.segment(scene,item['points'])
   for artist in fig.axes[0].lines:
    xy=artist.get_xydata()
    if xy.shape==(2,2) and base.np.allclose(xy,base.np.array([a,b]),rtol=0,atol=1e-12):artist.set_color('#999999');artist.set_zorder(0.5)
 for item in scene['objects']:
  if item.get('role')=='semantic_bold':
   if item['type']!='segment' or item.get('semantic_linewidth_pt')!=2.5:raise ValueError('Only native2.5pt semantic segments')
   a,b=base.segment(scene,item['points']); matched=0
   for artist in fig.axes[0].lines:
    xy=artist.get_xydata()
    if xy.shape==(2,2) and base.np.allclose(xy,base.np.array([a,b]),rtol=0,atol=1e-12):artist.set_linewidth(2.5);matched+=1
   if matched<1:raise ValueError('Missing bold binding')
 try:
  b=io.BytesIO();fig.savefig(b,format='png',dpi=100,facecolor='#FFFFFF',transparent=False,bbox_inches=None,pad_inches=0,metadata={'Software':'MathPalette scoped combinatorial renderer'})
  data=b.getvalue();im=Image.open(io.BytesIO(data));assert im.size==(768,768) and im.convert('RGBA').getextrema()[3]==(255,255)
  return data,checks
 finally:base.plt.close(fig)
def draw(scene_path,output_path):
 scene=base.read_json(scene_path);data,checks=image_bytes(scene);Path(output_path).write_bytes(data);return checks
