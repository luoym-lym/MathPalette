from review_bootstrap import *
import json, hashlib, io, math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from dataset_tools.mathvision_workbench import build_scene, png_bytes
from drawing_board import describe_captured_scene
from partial_style import describe_paths
from mathvision_plugins import PluginRenderer
from workbench_io import load_config, pixel_hash, environment_versions

CAND=BASE/'background_23/Plane192/r23_maximal_run_unit_binding'
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(name,v): (OWN/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record=read(OWN/'eligibility_current.json')['record']
formal=read(ROOT/'PlaneGeometry'/record['scene'])
plugin=read(CAND/'plugin.json')
config=load_config()
config['runtime_dir']=str(OWN/'state');config['output_dir']=str(OWN/'output')
class ReviewReadAdapter:
    def is_native(self,qid): return qid=='Plane192'
    def scene(self,qid):
        assert qid=='Plane192'
        return build_scene(ROOT/'PlaneGeometry',record)
adapter=ReviewReadAdapter()
scene=adapter.scene('Plane192')
try:
    original_data=png_bytes(scene)
    (OWN/'independent_noop.png').write_bytes(original_data)
    scene.fig.canvas.draw()
    meta={'original_pixel_sha256':pixel_hash(original_data),'objects':scene.objects,
          'snap_points':scene.snap_points,'canvas':describe_captured_scene(scene,'Plane192')}
    paths={a['target']:describe_paths(scene,a['target']) for a in plugin['params']['actions']}
    pxsegments=[]; actual=[]
    for a in plugin['params']['actions']:
        artists=scene.artists[a['target']]
        assert len(artists)==1
        art=artists[0]
        xy=art.get_xydata().tolist()
        px=scene.ax.transData.transform(xy)
        px[:,1]=768-px[:,1]
        pxsegments.append(px)
        actual.append({'target':a['target'],'xy':xy,'pixel_endpoints_top_origin':px.tolist(),
            'pixel_length':float(np.linalg.norm(px[1]-px[0])), 'original_color':art.get_color(),
            'original_linewidth_pt':art.get_linewidth(),'original_linestyle':art.get_linestyle(),
            'frozen_object':next(o for o in formal['objects'] if o['id']==a['target'])})
    grid_unit_px=float(np.linalg.norm(scene.ax.transData.transform([1,1])-scene.ax.transData.transform([0,1])))
finally:
    scene.close()
write('fresh_native_context.json',meta)
write('fresh_native_paths.json',paths)
renderer=PluginRenderer(config,adapter,{'Plane192':meta})
norm,data,pixels=renderer.render(plugin,frozen=True)
(OWN/'independent_replay_1.png').write_bytes(data)
norm2,data2,pixels2=renderer.render(plugin,frozen=True)
(OWN/'independent_replay_2.png').write_bytes(data2)
def arr(data):
    with Image.open(io.BytesIO(data)) as im: return np.array(im.convert('RGBA'))
original=arr(original_data); candidate=arr((CAND/'candidate.png').read_bytes())
changed=np.any(original!=candidate,axis=2)
ys,xs=np.where(changed)
centers=np.column_stack([xs+.5,ys+.5]); distances=[]
for p in pxsegments:
    v=p[1]-p[0]
    t=np.clip((centers-p[0])@v/(v@v),0,1)
    distances.append(np.linalg.norm(centers-(p[0]+t[:,None]*v),axis=1))
all_distances=np.column_stack(distances)
nearest=np.argmin(all_distances,axis=1)
groups=[]
for i,a in enumerate(actual):
    owned=nearest==i
    a.update({'changed_pixels':int(owned.sum()),
        'changed_bbox_xyxy_exclusive':[int(xs[owned].min()),int(ys[owned].min()),int(xs[owned].max()+1),int(ys[owned].max()+1)],
        'actual_style_override':plugin['params']['actions'][i],
        'changed_pixels_max_distance_from_selected_centerline':float(all_distances[owned,i].max())})
    groups.append(a)
math_routes={}
for i,letter in enumerate('ABCD'):
    segments=[o for o in formal['objects'] if o['id'].startswith(f'route{i}_')]
    segments.sort(key=lambda o:int(o['id'].split('_')[1]))
    widths=[]; coordinates=[]
    for j,o in enumerate(segments):
        p,q=o['points'];dx=q[0]-p[0];dy=q[1]-p[1]
        assert dx>0 and dx==abs(dy)
        if j: assert segments[j-1]['points'][1]==p
        widths.append(dx);coordinates.append(o['points'])
    assert sum(widths)==8
    math_routes[letter]={'segments':coordinates,'horizontal_unit_lengths':widths,'maximal_run_count':len(widths),
       'unit_diagonals':sum(widths),'metric_length_exact':'8*sqrt(2)', 'first_rising_maximal_run_length_exact':str(widths[0])+'*sqrt(2)'}
audit={'checked_at_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),
    'method':'Fresh isolated capture + actual frozen PluginRenderer normalize/schema/render twice; no solver.',
    'adapter_scope':'A review-only adapter delegates scene() to unchanged shared build_scene for this one formal record; avoids scanning unrelated questions.',
    'isolation':ISOLATION,'environment':environment_versions(),
    'checks':{'schema_and_actual_normalization':norm==plugin==norm2,
       'noop_formal_rgba_equal':bool(np.array_equal(original,arr((ROOT/'PlaneGeometry/image/Plane192.png').read_bytes()))),
       'no_op_existing_runtime_rgba_equal':bool(np.array_equal(original,arr((BASE/'background_23/Plane192/noop.png').read_bytes()))),
       'two_replays_byte_equal':data==data2,'replays_equal_frozen_tested_png':data==data2==(CAND/'candidate.png').read_bytes(),
       'pixel_hash_equals_frozen':pixels==pixels2==read(CAND/'design.json')['pixel_sha256'],
       'fresh_paths_equal_pre_call_paths':paths==read(CAND/'path_fingerprints.json'),
       'fresh_native_context_equals_pre_call':meta==read(CAND/'fresh_context.json'),
       'changes_only_selected_stroke_neighborhoods':bool((all_distances.min(axis=1)<=4.1).all()),
       'opaque_768_canvas':candidate.shape==(768,768,4) and bool((candidate[:,:,3]==255).all()),
       'all_figures_closed':not plt.get_fignums()},
    'changed_pixels':int(changed.sum()),'maximum_diff_distance_selected_centerline_px':float(all_distances.min(axis=1).max()),
    'grid_unit_px':grid_unit_px,'override_stroke_width_px':2*100/72,'original_stroke_width_px':100/72,
    'per_marker_native_evidence':groups,'independent_exact_math':math_routes,
    'replay_png_sha256':hashlib.sha256(data).hexdigest(),'replay_pixel_sha256':pixels}
write('native_render_audit.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
