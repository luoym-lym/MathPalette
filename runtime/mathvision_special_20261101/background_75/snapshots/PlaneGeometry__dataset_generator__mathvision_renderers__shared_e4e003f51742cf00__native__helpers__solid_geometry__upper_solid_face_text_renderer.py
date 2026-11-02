"""Scoped native planar text for orientation-essential die faces; no shared edits."""
import numpy as np
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D
import common_renderer as R

def install():
 if getattr(R.render_scene,'_upper_face_text',False):return
 old=R.render_scene
 def render(scene,*args,**kwargs):
  fig,checks=old(scene,*args,**kwargs);ax=fig.axes[0];m=np.array(scene['projection']['matrix']);pt=(scene['view']['xlim'][1]-scene['view']['xlim'][0])/ax.bbox.width*fig.dpi/72;paths=[]
  for item in scene.get('face_text',[]):
   u=np.array(item['u'],float);v=np.array(item['v'],float);anchor=np.array(scene['points'][item['anchor']],float)
   assert abs(u@v)<1e-10 and abs(u@u-1)<1e-10 and abs(v@v-1)<1e-10
   tp=TextPath((0,0),item['text'],size=16,prop=FontProperties(family='DejaVu Sans',weight='normal'));bb=tp.get_extents();center=np.array([(bb.x0+bb.x1)/2,(bb.y0+bb.y1)/2]);verts=tp.vertices-center
   xyz=anchor+pt*(verts[:,0,None]*u+verts[:,1,None]*v);lo=np.array(item['host_min']);hi=np.array(item['host_max']);assert np.all(xyz>=lo-1e-8) and np.all(xyz<=hi+1e-8),'Face glyph extends outside native cube face'
   xy=R.project(scene,[anchor])[0];basis=m@np.column_stack((u,v))*pt;transform=Affine2D().translate(*(-center)).transform # only used through equivalent explicit matrix below
   affine=Affine2D.from_values(basis[0,0],basis[1,0],basis[0,1],basis[1,1],*(xy-basis@center));path=tp.transformed(affine);patch=PathPatch(path,facecolor='black',edgecolor='none',zorder=5);ax.add_patch(patch);paths.append((item['id'],patch))
  fig.canvas.draw()
  if kwargs.get('check_layout',True):
   renderer=fig.canvas.get_renderer();boxes=[]
   for name,patch in paths:
    box=patch.get_window_extent(renderer).padded(1)
    assert ax.bbox.contains(box.x0,box.y0) and ax.bbox.contains(box.x1,box.y1),'Face-text margin violation'
    assert not any(box.overlaps(b) for b in boxes),'Face texts overlap'
    for line in ax.lines:
     lp=line.get_path().transformed(line.get_transform());assert not lp.intersects_bbox(box,filled=False),'Face text overlaps diagram line'
    boxes.append(box)
   checks.append({'id':'native_face_text','type':'scoped_primitive','passed':True,'count':len(paths),'font':'DejaVu Sans','font_size_pt':16,'geometry':'orthonormal3Dplanar basis, glyph vertices contained in host cube','margin_and_line_overlap_checked':True})
  return fig,checks
 render._upper_face_text=True;R.render_scene=render
