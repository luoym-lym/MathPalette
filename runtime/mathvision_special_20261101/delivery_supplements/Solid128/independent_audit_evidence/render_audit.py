from audit_bootstrap import *
import copy
import io
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from dataset_tools import mathvision_workbench as bridge
from renderer_adapter import scene_png
from render_plugins import PluginRenderer
from partial_style import object_paths, describe_paths
from workbench_io import load_config, pixel_hash, environment_versions

record=next(json.loads(s) for s in (ROOT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip() and json.loads(s).get('id')=='Solid128')
context=read(CANDIDATE/'context.json')
design=read(CANDIDATE/'design.json')
plugin=read(CANDIDATE/'plugin.json')
scene_record=read(ROOT/'SolidGeometry'/record['scene'])
checks={}
def check(name,value): checks[name]=bool(value)

class ReadOnlySingleAdapter:
    def scene(self,q):
        assert q=='Solid128'
        return bridge.build_scene(ROOT/'SolidGeometry',record)

config=load_config()
config['runtime_dir']=str(OWN/'tmp/state')
config['output_dir']=str(OWN/'tmp/output')
adapter=ReadOnlySingleAdapter()
renderer=PluginRenderer(config,adapter,{'Solid128':context})
normalized=renderer.normalize(plugin)
check('schema_and_target_validation_passed',normalized==plugin)
check('exactly_two_legal_existing_edge_styles_no_added_objects',len(plugin['params']['actions'])==2 and all(a['type']=='set_object_style' and a['linewidth_pt']==1.5 and a['color']=='#DC2626' and set(a)=={'type','target','color','linewidth_pt'} for a in plugin['params']['actions']))
check('reproduction_environment_equal_frozen',environment_versions()==read(QUESTION/'input_fingerprints.json')['environment'])

def inventory(scene):
    return {'objects':copy.deepcopy(scene.objects),'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'line_count':len(scene.ax.lines),'patch_count':len(scene.ax.patches),'text_count':len(scene.ax.texts),'collection_count':len(scene.ax.collections),'artists':{o:[{'xy':a.get_xydata().tolist(),'linewidth_pt':float(a.get_linewidth()),'color':matplotlib.colors.to_hex(a.get_color()),'linestyle':a.get_linestyle(),'visible':a.get_visible(),'zorder':a.get_zorder()} for a in artists] for o,artists in scene.artists.items()}}

native = adapter.scene('Solid128')
paths={}
try:
    with matplotlib.rc_context(native.settings): native.fig.canvas.draw()
    before=inventory(native)
    baseline_bytes, baseline_pixel=scene_png(native)
    (OWN/'reproduced_original.png').write_bytes(baseline_bytes)
    check('no_op_baseline_pixels_match_formal',baseline_pixel==pixel_hash(ROOT/'SolidGeometry'/record['image'])==context['original_pixel_sha256'])
    for role in design['marker_roles']:
        target=role['action']['target']
        p=object_paths(native,target)
        controls=[[seg['control'].tolist() for seg in path['segments']] for path in p]
        desc=describe_paths(native,target)
        obj=next(o for o in native.objects if o['id']==target)
        check(target+'_native_object_matches_frozen_design',obj==role['stable_source_object'])
        check(target+'_exact_control_path_hashes_match',len(p)==1 and p[0]['id']==role['frozen_path_id'] and p[0]['sha256']==role['frozen_path_sha256'] and not p[0]['closed'] and controls[0]==role['full_precision_frozen_projected_controls'] and desc==role['path_description'])
        paths[target]={'native_object':obj,'controls':controls,'path_description':desc,'baseline_style':before['artists'][target]}
    with matplotlib.rc_context(native.settings): renderer.apply_actions(native,normalized)
    after=inventory(native)
    candidate_bytes,candidate_pixel=scene_png(native)
    (OWN/'reproduced_candidate.png').write_bytes(candidate_bytes)
    check('full_candidate_reproduction_bytes_equal_frozen',candidate_bytes==(CANDIDATE/'candidate.png').read_bytes())
    check('full_candidate_pixels_equal_frozen',candidate_pixel==pixel_hash(CANDIDATE/'candidate.png')==design['pixel_sha256'])
    check('geometry_projection_visibility_labels_fill_artist_counts_unchanged',all(before[k]==after[k] for k in before if k!='artists'))
    target_names=set(paths)
    for target in before['artists']:
        b=before['artists'][target]; a=after['artists'][target]
        if target in target_names:
            check(target+'_only_color_and_width_changed',len(b)==len(a)==1 and all(b[0][k]==a[0][k] for k in b[0] if k not in ('color','linewidth_pt')) and a[0]['linewidth_pt']==1.5 and a[0]['color']=='#dc2626')
        else:
            check(target+'_entire_artist_unchanged',a==b)
    with Image.open(io.BytesIO(baseline_bytes)) as loaded: original=np.array(loaded.convert('RGBA'))
    with Image.open(io.BytesIO(candidate_bytes)) as loaded: candidate=np.array(loaded.convert('RGBA'))
    changed=np.any(original!=candidate,axis=2)
    yy,xx=np.nonzero(changed)
    pixels=np.column_stack((xx+0.5,yy+0.5))
    distances=[]
    for target,p in paths.items():
        ends=np.array(p['path_description'][0]['samples'])[:,:2]
        a,b=ends[0],ends[-1]; d=b-a
        t=np.clip((pixels-a)@d/(d@d),0,1)
        distances.append(np.linalg.norm(pixels-(a+t[:,None]*d),axis=1))
        p['projected_length_px']=float(np.linalg.norm(d))
        p['changed_stroke_style']=after['artists'][target]
    min_dist=np.min(np.array(distances),axis=0)
    check('all_changed_pixels_within_original_target_stroke_envelopes',min_dist.max()<2)
    ink=np.any(candidate[:,:,:3]!=255,axis=2)
    iy,ix=np.nonzero(ink)
    red=(candidate[:,:,0]>candidate[:,:,1]+30) & (candidate[:,:,0]>candidate[:,:,2]+30)
    check('opaque_native_768_square',candidate.shape==(768,768,4) and np.all(candidate[:,:,3]==255))
    raster={'changed_pixel_count':int(changed.sum()),'changed_pixel_bbox_inclusive':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())],'max_changed_pixel_center_distance_from_either_existing_target_px':float(min_dist.max()),'all_ink_bbox_inclusive':[int(ix.min()),int(iy.min()),int(ix.max()),int(iy.max())],'nominal_original_stroke_width_px':100/72,'nominal_marked_stroke_width_px':1.5*100/72,'target_marker_lengths_px':{t:p['projected_length_px'] for t,p in paths.items()}}
finally:
    native.close()

projection=np.array(scene_record['projection']['matrix'],dtype=float)
view=np.array(scene_record['projection']['toward_viewer'],dtype=float)
check('projection_toward_viewer_in_kernel',np.allclose(projection@view,[0,0],atol=1e-12))
check('visibility_projection_hash_binds_current_projection',canonical_hash(scene_record['projection'])==scene_record['visibility']['projection_sha256'])
check('actual_marked_edges_frozen_visible',all(next(o for o in scene_record['objects'] if o['id']==t)['visibility']=='visible' for t in paths))
top_intersections={'red_front_with_red_return':{'world_xyz':[1,0,1],'projected_xy':(projection@np.array([1,0,1])).tolist(),'front_parameter':0.2,'return_parameter':0.0,'classification':'True shared cube-seam/front-rim endpoint; red T junction, not an apparent depth crossing'},'red_return_with_black_front_rear_top':{'world_xyz':[1,1,1],'projected_xy':(projection@np.array([1,1,1])).tolist(),'return_parameter':1/2.7,'black_front_rear_parameter':1/4.1,'classification':'True coplanar top-seam crossing at the inner corner; all participating objects have z=1. Not a merely projected crossing.'}}
outer_n=10
boundary={(x,y) for x in range(outer_n) for y in range(outer_n) if x in (0,outer_n-1) or y in (0,outer_n-1)}
interior={(x,y) for x in range(1,outer_n-1) for y in range(1,outer_n-1)}
enumeration={'outer_side':outer_n,'boundary_cubes':len(boundary),'empty_interior_cubes':len(interior),'only_integer_outer_side_solution_from_formula':[n for n in range(2,100) if 4*n-4==36],'target_81_would_require_outer_side':11,'boundary_for_9_by_9_interior':4*11-4,'scope':'Arithmetic and finite lattice cross-check of the proof, no model or solver request.'}
write('render_and_geometry_audit.json',{'checked_at':now(),'checks':checks,'all_checks_passed':all(checks.values()),'failed_checks':[k for k,v in checks.items() if not v],'baseline_png_sha256':hashlib.sha256(baseline_bytes).hexdigest(),'baseline_pixel_sha256':baseline_pixel,'candidate_png_sha256':hashlib.sha256(candidate_bytes).hexdigest(),'candidate_pixel_sha256':candidate_pixel,'paths_and_styles':paths,'raster':raster,'independent_top_intersections':top_intersections,'independent_lattice_count':enumeration,'appearance_changes':renderer.appearance_changes(plugin),'figure_numbers_after_close':plt.get_fignums(),'environment':environment_versions(),'scope':'Exact original/candidate replay only. No API/control calls. Input geometry, projection and visibility are read-only.'})
print(json.dumps({'failed_checks':[k for k,v in checks.items() if not v],'checks_count':len(checks),'raster':raster,'paths':{t:{'id':p['path_description'][0]['id'],'sha256':p['path_description'][0]['sha256'],'closed':p['path_description'][0]['closed']} for t,p in paths.items()},'intersections':top_intersections,'enumeration':enumeration,'open_figures':plt.get_fignums()},ensure_ascii=False,indent=2))
