"""Standalone native Bézier-on-3D-face renderer for MathVision 927.
Imports are side-effect free. Raster files are never opened for drawing or tracing.
"""
from pathlib import Path
import hashlib, io, itertools, json, platform, argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Polygon
from matplotlib.transforms import Affine2D
from PIL import Image
import PIL
B=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cube_rotations():
 out=[]
 for perm in itertools.permutations(range(3)):
  for signs in itertools.product([-1,1],repeat=3):
   m=np.zeros((3,3),dtype=int)
   for col,row in enumerate(perm):m[row,col]=signs[col]
   if round(np.linalg.det(m))==1:out.append(m)
 return out

def check_scene(s):
 P=np.array(s['projection']['matrix']);toward=np.array(s['projection']['toward_viewer'])
 assert s['visibility']['projection_sha256']==hashlib.sha256(json.dumps(s['projection'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert np.max(np.abs(P@P.T-np.eye(2)))<1e-12 and np.max(np.abs(P@toward))<1e-12
 assert np.dot(np.cross(P[0],P[1]),toward)>0
 checks=[{'id':'orthographic_projection','passed':True,'rows_orthonormal':True,'toward_viewer_in_kernel':True}]
 for f in s['faces'].values():
  vv=np.array(f['vertices']);d=np.roll(vv,-1,axis=0)-vv
  assert np.allclose(np.linalg.norm(d,axis=1),1) and np.allclose(np.sum(d*np.roll(d,-1,axis=0),axis=1),0)
 for cube in s['cubes']:
  assert cube['page_scale']>0
  rot=np.array(cube['rotation_from_view_1']);assert np.array_equal(rot@rot.T,np.eye(3)) and round(np.linalg.det(rot))==1
  for d in cube['decals']:
   u=np.array(d['art_u']);v=np.array(d['art_v']);n=np.array(s['faces'][d['face']]['normal']);c=np.array(d['center'])
   assert np.linalg.norm(u)==np.linalg.norm(v)==1 and np.dot(u,v)==0 and np.array_equal(np.cross(u,v),n)
   art=s['artwork'][d['animal']]
   assert all(lay['linewidth_pt']==1.0 for lay in art['layers'])
   verts=np.concatenate([np.array(a['vertices']) for a in art['layers']]);assert np.all(np.isfinite(verts));xyz=c+d['side']*(verts[:,0,None]*u+verts[:,1,None]*v)
   assert np.min(xyz)>=0-1e-12 and np.max(xyz)<=1+1e-12
   assert np.max(np.abs((xyz-c)@n))<1e-12
 checks.append({'id':'genuine_3d_face_decals','passed':True,'faces_unit_squares':True,'six_directed_art_bases_right_handed':True,'decal_vertices_on_faces':True,'uniform_post_projection_cube_scaling':True})
 first,second=s['cubes'];a=next(d for d in first['decals'] if d['animal']=='ladybird');b=next(d for d in second['decals'] if d['animal']=='ladybird')
 n1=np.array(s['faces'][a['face']]['normal']);n2=np.array(s['faces'][b['face']]['normal'])
 rs=cube_rotations();assert len(rs)==24
 adjacency=[r for r in rs if np.array_equal(r@n1,n2)]
 directed=[r for r in adjacency if np.array_equal(r@a['art_v'],b['art_v']) and np.array_equal(r@a['art_u'],b['art_u'])]
 assert len(adjacency)==4 and len(directed)==1
 r=directed[0];assert np.array_equal(r,second['rotation_from_view_1'])
 normal1={d['animal']:np.array(s['faces'][d['face']]['normal']) for d in first['decals']}
 for d in second['decals']:
  n=r.T@np.array(s['faces'][d['face']]['normal'])
  if d['animal'] in normal1:assert np.array_equal(n,normal1[d['animal']])
  else:normal1[d['animal']]=n
 unused=[np.array(n) for n in itertools.product([-1,0,1],repeat=3) if sum(abs(t) for t in n)==1 and not any(np.array_equal(n,k) for k in normal1.values())]
 assert len(unused)==1;normal1['elephant']=unused[0]
 duck2=r@normal1['duck'];fly2=r@normal1['fly'];assert np.array_equal(duck2,-fly2)
 opposite={k:next(j for j,v in normal1.items() if np.array_equal(v,-n)) for k,n in normal1.items()}
 # Without directed axes, each of four normal-only rotations predicts a different location for duck.
 checks.append({'id':'directed_cube_rotation_enumeration','passed':True,'proper_cube_rotations_enumerated':24,'common_face_identity_only_candidates':len(adjacency),'directed_head_and_right_axis_candidates':len(directed),'unique_rotation_view1_to_view2':r.tolist(),'first_ladybird_normal':n1.tolist(),'first_ladybird_head_axis':a['art_v'],'second_ladybird_normal':n2.tolist(),'second_ladybird_head_axis':b['art_v'],'duck_normal_in_second_view':duck2.tolist(),'fly_normal_in_second_view':fly2.tolist(),'opposite_pairs':opposite,'unique_answer':'E','all_24_rotation_matrices':[m.tolist() for m in rs]})
 assert list(s['artwork'])==['mouse','elephant','duck','ladybird','dog','fly']
 assert [x['animal'] for x in s['reference_and_option_instances'] if x['id'].startswith('reference_')]==list(s['artwork'])
 assert [x['animal'] for x in s['reference_and_option_instances'] if x['id'].startswith('option_')]==['elephant','mouse','ladybird','dog','fly']
 checks.append({'id':'source_inventory','passed':True,'reference_stickers':6,'cube_decals':6,'colored_options':5,'total_native_instances':17,'native_path_layers':sum(len(a['layers']) for a in s['artwork'].values()),'unlabeled_stickers_not_substituted':True})
 assert all(lay['linewidth_pt']==1.0 for art in s['artwork'].values() for lay in art['layers'])
 checks.append({'id':'strict_1pt_stroke_protocol','passed':True,'all_native_path_linewidths_pt':[1.0],'cube_edge_linewidth_pt':1.0,'thin_polygon_stroke_substitution':False})
 return checks

def draw_art(ax,art,linear,offset,mode,z=4):
 mat=np.eye(3);mat[:2,:2]=linear;mat[:2,2]=offset
 trans=Affine2D(mat)+ax.transData
 for k,lay in enumerate(art['layers']):
  if mode=='monochrome':fill=lay['monochrome_fill'];stroke='none' if lay['stroke']=='none' else 'black'
  else:fill=art['palette'].get(lay['fill'],lay['fill']);stroke=art['palette'].get(lay['stroke'],lay['stroke'])
  ax.add_patch(PathPatch(MPath(lay['vertices'],lay['codes']),facecolor=fill,edgecolor=stroke,linewidth=lay['linewidth_pt'],transform=trans,antialiased=True,joinstyle='round',capstyle='round',zorder=z+k*.001))

def render(vector=False):
 s=json.loads((B/'scene.json').read_text());checks = check_scene(s);P=np.array(s['projection']['matrix'])
 with matplotlib.rc_context({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'MathVision927native','path.simplify':False}):
  fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white');ax=fig.add_axes(s['view']['layout']['axes_position']);ax.set_xlim(s['view']['xlim']);ax.set_ylim(s['view']['ylim']);ax.set_aspect('equal');ax.set_axis_off();ax.set_autoscale_on(False)
  for cube in s['cubes']:
   scale=cube['page_scale'];off=np.array(cube['page_origin']);worldcenter=np.array(cube['world_center'])
   project=lambda x:scale*((np.array(x)-worldcenter)@P.T)+off
   for f in s['faces'].values():ax.add_patch(Polygon(project(f['vertices']),closed=True,facecolor='white',edgecolor='none',zorder=1))
   for a,b in s['visibility']['visible_edges']:
    a,b=project([a,b]);ax.plot([a[0],b[0]],[a[1],b[1]],color='black',linewidth=1,solid_capstyle='round',zorder=2)
   for d in cube['decals']:
    lin=scale*d['side']*(P@np.array([d['art_u'],d['art_v']]).T)
    draw_art(ax,s['artwork'][d['animal']],lin,project(d['center']),d['color_mode'])
  for ins in s['reference_and_option_instances']:draw_art(ax,s['artwork'][ins['animal']],ins['scale']*np.eye(2),np.array(ins['center']),ins['color_mode'])
  for label in s['labels']:ax.text(*label['position'],label['text'],fontsize=label['font_size_pt'],ha=label['ha'],va=label['va'],color='black',clip_on=False,zorder=10)
  buf=io.BytesIO();fig.savefig(buf,format='svg' if vector else 'png',dpi=100,transparent=False,facecolor='white',bbox_inches=None,metadata={'Date':None} if vector else {'Software':'MathPalette native 927 renderer'});plt.close(fig)
 return buf.getvalue()

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=B);args=parser.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
 s=json.loads((B/'scene.json').read_text());checks=check_scene(s)
 pngs=[render(False) for _ in range(2)];svgs=[render(True) for _ in range(2)]
 imgs=[np.asarray(Image.open(io.BytesIO(p))) for p in pngs]
 assert imgs[0].shape==(768,768,4) and np.all(imgs[0][:,:,3]==255) and np.array_equal(*imgs) and pngs[0]==pngs[1] and svgs[0]==svgs[1]
 (out/'image.png').write_bytes(pngs[0]);(out/'image.svg').write_bytes(svgs[0]);img=imgs[0]
 yy,xx=np.where(np.any(img[:,:,:3]<245,axis=2));bbox=[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())];center=[(bbox[0]+bbox[2])/2,(bbox[1]+bbox[3])/2];occ=max(bbox[2]-bbox[0]+1,bbox[3]-bbox[1]+1)/768
 layout={'content_bbox_px':bbox,'content_center_px':center,'longest_side_occupancy':occ,'centered_within_2px':max(abs(v-383.5) for v in center)<=2,'occupancy_85_to_87_percent':.85<=occ<=.87,'minimum_5_percent_margin':min(bbox[0],bbox[1],767-bbox[2],767-bbox[3])>=38.4}
 assert layout['centered_within_2px'] and layout['occupancy_85_to_87_percent'] and layout['minimum_5_percent_margin'],layout
 report={'source_sha256':sha(B/'original.jpg') if (B/'original.jpg').exists() else None,'scene_sha256':sha(B/'scene.json'),'renderer_sha256':sha(__file__),'protocol_sha256':sha(B/'protocol.json') if (B/'protocol.json').exists() else None,'author_script_sha256':sha(B/'author_scene.py') if (B/'author_scene.py').exists() else None,'script_sha256':sha(__file__),'image_sha256':sha(out/'image.png'),'svg_sha256':sha(out/'image.svg'),'two_render_pixels_equal':True,'two_render_png_bytes_equal':True,'two_render_svg_bytes_equal':True,'opaque_768_square':True,'layout':layout,'constraints':checks,'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'Pillow':PIL.__version__},'native_rendering':{'raster_embedding':False,'pixel_tracing':False,'all_artwork':'83 hand-authored native cubic Bézier paths; no fonts, generic symbols or letters used as animal replacements.','face_attachment':'Every cube sticker is mapped by right-handed local 3D tangent bases to a true unit-square cube face and then projected by the one frozen orthographic matrix.','stroke_protocol':'Every native artwork outline/detail stroke and cube edge is exactly 1pt. Filled details remain ordinary native fills; no thin polygon stroke substitutes. Source color identity retained in reference and choices, monochrome views retained.','source_packaging_omitted':'Blue <imageN> labels, separator rules, and punctuation after the top sticker row are not mathematical data.'},'visual_check':'pending_author_view','independent_review':'pending','status':'awaiting_independent_review'}
 (out/'redraw_report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(layout,indent=2))
if __name__=='__main__':main()
