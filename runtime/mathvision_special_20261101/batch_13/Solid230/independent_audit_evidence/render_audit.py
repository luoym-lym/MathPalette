from review_env import *
import io
import math
from collections import Counter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from delivery_bridge_adapter import RendererAdapter
from renderer_adapter import scene_png
from render_plugins import PluginRenderer, check_schema
from workbench_io import load_config, environment_versions

record = next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid230')
scene = read(ROOT/'SolidGeometry'/record['scene'])
plugin = read(CAND/'plugin.json')
design = read(CAND/'design.json')
schema = read(ROOT/'SolidGeometry/workbench/plugin.schema.json')
check_schema(plugin,schema,schema)
config=load_config()
config['runtime_dir']=str(OWN/'bridge_state')
config['output_dir']=str(OWN/'bridge_outputs')
adapter=RendererAdapter(config)
ctx=adapter.inspect_question('Solid230')
write('fresh_context.json',ctx)
captured=adapter.scene('Solid230')
try:
    noop,noop_pixel=scene_png(captured)
finally:
    captured.close()
(OWN/'independent_noop.png').write_bytes(noop)
renderer=PluginRenderer(config,adapter,{'Solid230':ctx})
normal,data,pixel=renderer.render(plugin)
normal2,data2,pixel2=renderer.render(plugin)
(OWN/'independent_replay_1.png').write_bytes(data)
(OWN/'independent_replay_2.png').write_bytes(data2)
formal=Image.open(ROOT/'SolidGeometry'/record['image']).convert('RGBA')
candidate=Image.open(CAND/'candidate.png').convert('RGBA')
source=Image.open(ROOT/'SolidGeometry'/record['original_image']).convert('RGBA')
a,b=np.array(formal),np.array(candidate)
diff=np.any(a!=b,axis=2)
changed_yx=np.argwhere(diff)
matrix=np.array(scene['projection']['matrix'],dtype=float)
origin=np.array(scene['projection']['origin'],dtype=float)
offset=np.array(scene['projection']['offset'],dtype=float)
transform=np.array(ctx['canvas']['data_to_pixel'],dtype=float)
def project(xyz):
    return matrix@(np.array(xyz,dtype=float)-origin)+offset
def px(xy):
    return (transform@np.array([*xy,1.0]))[:2]
objects={obj['id']:obj for obj in scene['objects']}
fresh_objects={obj['id']:obj for obj in ctx['objects']}
segments=[]
marker_rows=[]
for role in design['pretest_marker_roles']:
    action=role['action']; target=action['target']; obj=objects[target]
    xyz=[scene['points'][point] for point in obj['points']]
    xy=[project(p).tolist() for p in xyz]
    pix=[px(p).tolist() for p in xy]
    segments.append(np.array(pix))
    marker_rows.append({'target':target,'original_scene_object':obj,'world_endpoints':xyz,'projected_endpoints':xy,'pixel_endpoints':pix,
        'geometry_sha256':canonical(obj),'matches_pretest_geometry_sha256':canonical(obj)==role['source_object_geometry_sha256'],
        'matches_pretest_endpoints':xyz==role['world_endpoints'] and xy==role['projected_endpoints'],
        'action':action,'whole_object':True,'partial_paths':[],
        'original_visible':obj['visibility']=='visible','original_width_pt':1,'rendered_width_pt':2,'rendered_color':'#DC2626','rendered_linestyle':'solid retained'})

def point_segment_dist(points,segment):
    start,end=segment
    v=end-start
    t=np.clip(((points-start)@v)/(v@v),0,1)
    return np.linalg.norm(points-(start+t[:,None]*v),axis=1)
changed_xy=changed_yx[:,[1,0]].astype(float)
changed_dist=np.min(np.array([point_segment_dist(changed_xy,s) for s in segments]),axis=0)

pip_rows=[]
for obj in scene['objects']:
    if obj['type']!='point': continue
    xyz=scene['points'][obj['point']]
    xy=project(xyz); center=px(xy)
    x,y=[int(round(v)) for v in center]
    box=(x-9,y-9,x+10,y+10)
    p0=formal.crop(box).tobytes();p1=candidate.crop(box).tobytes()
    distance=float(np.min(np.linalg.norm(changed_xy-center,axis=1)))
    pip_rows.append({'id':obj['id'],'world_xyz':xyz,'projected_xy':xy.tolist(),'pixel_xy':center.tolist(),
        'patch_box_ltrb':box,'radius_pixels':9,'formal_patch_sha256':sha(p0),'candidate_patch_sha256':sha(p1),
        'exact_patch_equal':p0==p1,'distance_center_to_nearest_changed_pixel':distance})
old_pips=read(CAND/'pip_pixel_preservation.json')
old_byid={p['id']:p for p in old_pips['patches']}
for row in pip_rows:
    old=old_byid[row['id']]
    row['prior_pixel_centers_independently_match']=np.allclose(row['pixel_xy'],old['pixel_xy'],atol=1e-10,rtol=0)
    row['prior_patch_hash_match']=row['formal_patch_sha256']==old['patch_sha256']

# Independent connected components directly on actual raster; no scene pip count used.
def components(image):
    rgb=np.array(image)[:,:,:3]
    mask=np.max(rgb,axis=2)<64
    visited=np.zeros(mask.shape,dtype=bool)
    found=[]
    for yy,xx in np.argwhere(mask):
        if visited[yy,xx]:continue
        stack=[(int(yy),int(xx))];visited[yy,xx]=True;coords=[]
        while stack:
            cy,cx=stack.pop();coords.append((cx,cy))
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<mask.shape[0] and 0<=nx<mask.shape[1] and mask[ny,nx] and not visited[ny,nx]:
                        visited[ny,nx]=True;stack.append((ny,nx))
        cs=np.array(coords);lo=cs.min(axis=0);hi=cs.max(axis=0)
        found.append({'area_pixels':len(coords),'bbox_xyxy':[*lo.tolist(),*(hi+1).tolist()],'centroid_xy':cs.mean(axis=0).tolist()})
    return found
raster={}
for name,img,threshold,max_size in [('source_jpg',source,70,25),('formal_png',formal,25,15),('candidate_png',candidate,25,15)]:
    allc=components(img)
    dots=[c for c in allc if threshold<c['area_pixels']<500 and 3<c['bbox_xyxy'][2]-c['bbox_xyxy'][0]<=max_size and 3<c['bbox_xyxy'][3]-c['bbox_xyxy'][1]<=max_size]
    raster[name]={'size':img.size,'all_component_count':len(allc),'pip_component_count':len(dots),'pips':dots,'non_pip_components':[c for c in allc if c not in dots]}
    if name!='source_jpg':
        for row in pip_rows:
            nearest=min(dots,key=lambda c:math.dist(c['centroid_xy'],row['pixel_xy']))
            row[name+'_nearest_pip_component']=nearest
            row[name+'_center_match_distance']=math.dist(nearest['centroid_xy'],row['pixel_xy'])
counts={prefix:sum(row['id'].startswith(prefix) for row in pip_rows) for prefix in ['front0','front1','front2','right0','right1','right2','top3']}
face_values={'top_top':1,'top_front':2,'top_right':3,'middle_front':4,'middle_right':6,'bottom_front':5,'bottom_right':1}
proof={'basis':'Independent native-source/formal/candidate count, corroborated by raster components and frozen 3D face membership. Not a copy of primary proof.',
    'visible_face_values':face_values,'scene_pip_counts':counts,'number_of_dice':3,'faces_per_die':6,
    'sum_all_faces_of_one_die':sum(range(1,7)),'all_dots':3*sum(range(1,7)),
    'visible_dots':sum(face_values.values()),'hidden_dots':3*sum(range(1,7))-sum(face_values.values()),
    'hidden_per_die':{'top':21-1-2-3,'middle':21-4-6,'bottom':21-5-1},
    'hidden_faces_per_die':{'top':3,'middle':4,'bottom':4},
    'uniqueness':'Each die contains 1,2,3,4,5,6 once, so total 63 regardless of hidden orientation/opposite-face convention. Seven distinct visible faces carry 22 dots, so exactly the other eleven carry 41. Equal pip values on two different dice are two separate visible contributions. No hidden placement can alter this complement.',
    'preset_42_rule':'Deduplicating the two visible value-1 faces would drop exactly one dot: visible 21, hidden 42. This was frozen before calls but not observed in their text.',
    'response_actual_42_rule':'Both responses instead count both 1 faces and replace unmarked middle-right 6 with 5: 63-(6+9+6)=42.',
    'no_opposite_sum_needed':True}
write('independent_math_proof.json',proof)
checks={
    'fresh_context_exact_frozen_context':ctx==read(CAND/'context.json'),
    'current_environment_matches_frozen':environment_versions()==read(CAND/'render_check.json')['frozen_inputs']['environment'],
    'noop_pixels_exact_formal':np.array_equal(np.array(Image.open(io.BytesIO(noop)).convert('RGBA')),a),
    'noop_bytes_exact_formal':noop==(ROOT/'SolidGeometry'/record['image']).read_bytes(),
    'candidate_exact_tested_png_replay':data==(CAND/'candidate.png').read_bytes(),
    'candidate_two_replays_bytes_equal':data==data2,
    'plugin_normalization_unchanged':normal==normal2==plugin,
    'pixel_sha256_exact_bound':pixel==pixel2==read(TEST/'binding.json')['pixel_sha256'],
    'all_geometry_and_endpoints_match':all(r['matches_pretest_geometry_sha256'] and r['matches_pretest_endpoints'] for r in marker_rows),
    'all22_pip_patches_unchanged':len(pip_rows)==22 and all(r['exact_patch_equal'] for r in pip_rows),
    'all_prior_pip_patch_findings_independently_match':all(r['prior_pixel_centers_independently_match'] and r['prior_patch_hash_match'] for r in pip_rows),
    'all_three_images_have22_raster_dot_components':all(r['pip_component_count']==22 for r in raster.values()),
    'all_scene_pips_match_distinct_actual_dot_components':all(r['formal_png_center_match_distance']<2 and r['candidate_png_center_match_distance']<2 for r in pip_rows) and len({tuple(r['formal_png_nearest_pip_component']['bbox_xyxy']) for r in pip_rows})==22,
    'middle_right_six_preserved':counts['right1']==6 and all(r['exact_patch_equal'] for r in pip_rows if r['id'].startswith('right1')),
    'all_changed_pixels_local_to_two_existing_edges':bool(np.max(changed_dist)<3.0),
    'canvas_opaque768':formal.size==candidate.size==(768,768) and formal.getextrema()[3]==candidate.getextrema()[3]==(255,255),
    'no_added_text_dimensions_fills':scene['labels']==[] and scene['dimensions']==[] and not any(a['type']!='set_object_style' for a in normal['params']['actions']),
    'all_figures_closed':plt.get_fignums()==[],
}
write('native_render_pixel_audit.json',{'at':now(),'pid':os.getpid(),'checks':checks,'all_checks_pass':all(checks.values()),
    'images':{'source':{'path':str(ROOT/'SolidGeometry'/record['original_image']),'sha256':fh(ROOT/'SolidGeometry'/record['original_image']),'size':source.size},
    'formal':{'path':str(ROOT/'SolidGeometry'/record['image']),'sha256':fh(ROOT/'SolidGeometry'/record['image']),'pixel_sha256':noop_pixel},
    'candidate':{'path':str(CAND/'candidate.png'),'sha256':fh(CAND/'candidate.png'),'pixel_sha256':pixel}},
    'noop_sha256':sha(noop),'replay1_sha256':sha(data),'replay2_sha256':sha(data2),
    'scene_sha256':fh(ROOT/'SolidGeometry'/record['scene']),'projection_sha256':canonical(scene['projection']),
    'frozen_visibility':scene['visibility'],'matrix_kernel_check':(matrix@np.array(scene['projection']['toward_viewer'])).tolist(),
    'markers':marker_rows,'pip_patches':pip_rows,'raster_components':raster,'changed_pixels':len(changed_xy),
    'change_bbox_xyxy':[*changed_xy.min(axis=0).tolist(),*changed_xy.max(axis=0).tolist()],
    'maximum_changed_pixel_distance_to_selected_centerlines':float(np.max(changed_dist)),
    'minimum_pip_center_distance_to_any_change':min(r['distance_center_to_nearest_changed_pixel'] for r in pip_rows),
    'appearance_changes':renderer.appearance_changes(normal),'environment':environment_versions(),'all_scenes_closed':True})
print(json.dumps({'all_checks_pass':all(checks.values()),'failed':[k for k,v in checks.items() if not v],
    'source_formal_candidate_raster_dot_counts':{k:v['pip_component_count'] for k,v in raster.items()},
    'scene_face_counts':counts,'hidden_answer':proof['hidden_dots'],'changed_pixels':len(changed_xy),
    'max_change_distance':float(np.max(changed_dist)),'min_pip_change_distance':min(r['distance_center_to_nearest_changed_pixel'] for r in pip_rows),
    'pid':os.getpid(),'all_figures_closed':plt.get_fignums()==[]}))
