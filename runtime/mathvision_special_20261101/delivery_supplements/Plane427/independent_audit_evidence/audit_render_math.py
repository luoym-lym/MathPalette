from review_bootstrap import *
ROUTING = route_runtime()
sys.path.insert(0, str(PROJECT/'PlaneGeometry/workbench'))
import copy
import io
import itertools
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Patch
from workbench_io import load_config, pixel_hash, environment_versions, canonical_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths, apply_partial_styles
from dataset_tools.mathvision_workbench import png_bytes
from dataset_tools.catalog import content, digest

cfg=load_config()
cfg['runtime_dir']=str(OWN/'temp/state')
cfg['output_dir']=str(OWN/'temp/output')
adapter=RendererAdapter(cfg)
qid='Plane427'
row=adapter.records[qid]
formal_scene=read(PROJECT/'PlaneGeometry'/row['scene'])
points={k:np.array(v) for k,v in formal_scene['points'].items()}

def angle(a,b,c):
    u,v=points[a]-points[b],points[c]-points[b]
    return math.degrees(math.atan2(abs(float(np.linalg.det(np.vstack([u,v])))),float(u@v)))

def direction(a,b):
    v=points[b]-points[a]
    return math.degrees(math.atan2(float(v[1]),float(v[0])))%360

rotations=[]
for images in [('U','V'),('V','U')]:
    u,v=points['R']-points['T'],points[images[0]]-points['T']
    theta=math.atan2(float(np.linalg.det(np.vstack([u,v]))),float(u@v))
    m=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    errors={src:float(np.linalg.norm(points['T']+m@(points[src]-points['T'])-points[dest])) for src,dest in zip(['R','S'],images)}
    rotations.append({'mapping':dict(zip(['R','S','T'],[*images,'T'])),'signed_degrees':math.degrees(theta),'errors':errors})

math_audit={'coordinate_source':str(PROJECT/'PlaneGeometry'/row['scene']),'coordinate_source_sha256':sha(PROJECT/'PlaneGeometry'/row['scene']),
 'points':formal_scene['points'],'angles_deg':{name:angle(*name) for name in ['RST','RTS','TRS','TUV','UVT','VTU','RTV','STV','TSV','TVS','RSV']},
 'distances':{name:float(np.linalg.norm(points[name[1]]-points[name[0]])) for name in ['RS','ST','TR','TU','UV','VT','SV']},
 'directions_at_T_deg':{x:direction('T',x) for x in ['S','R','V','U']},'directions_at_S_deg':{x:direction('S',x) for x in ['T','V','R']},
 'rotation_correspondence_enumeration':rotations,
 'independent_exact_proof':['The image places TR strictly between TS and TV in the nonreflex angle STV. RST is equilateral; rotating about T preserves lengths, hence TS=TV.',
 'Angle STV=angle STR+angle RTV=60+70=130 degrees. In the isosceles triangle STV, TSV=TVS=(180-130)/2=25 degrees.',
 'At S, ray SV lies strictly inside the 60-degree angle RST (as seen in both the source and frozen diagram). Thus RSV=RST-TSV=60-25=35 degrees. Only choice D equals 35.',
 'As a separate proof, TR=TS=TV, so R,S,V lie on a proof-only circle centered at T. S is on the major RV arc. The inscribed angle RSV intercepts the minor RV arc of 70 degrees, giving 35 degrees. No circle is added to the candidate.'],
 'unique_correct_letter':'D','unique_correct_degrees':35,'wrong_preset_letter':'B','wrong_preset_degrees':25,
 'layout_dependence':'The ray order is part of the actual supplied diagram. Placing TV on a different side of TR would be a different diagram; a reflex reinterpretation conflicts with the original minor arcs.',
 'three_dimensional_geometry_projection_visibility':'Not applicable; frozen 2D coordinates, all native paths, labels, transforms and view audited below.'}
assert abs(angle('R','S','V')-35)<1e-7
assert max(rotations[0]['errors'].values())<1e-8 and max(rotations[1]['errors'].values())>1
write('independent_math.json',math_audit)

frozen_context=read(CAND.parent/'context.json')
fresh=adapter.inspect_question(qid)
write('fresh_native_context.json',fresh)
assert fresh==frozen_context
frozen_manifest=read(CAND.parent/'adapter_input_hashes.json')
fresh_path_hashes={str(p.relative_to(PROJECT)):sha(p) for p in adapter.input_files.values()}
manifest_matches=fresh_path_hashes==frozen_manifest
assert manifest_matches
write('fresh_adapter_input_hashes.json',adapter.manifest)

plugin=read(CAND/'plugin.json')
renderer=PluginRenderer(cfg,adapter,{qid:fresh})
normalized=renderer.normalize(copy.deepcopy(plugin))
assert normalized==plugin

def texts(scene):
    return [{'text':t.get_text(),'position':list(t.get_position()),'font':t.get_fontfamily(),'size':t.get_fontsize(),
             'style':t.get_fontstyle(),'color':t.get_color(),'transform':t.get_transform().get_matrix().tolist(),
             'bbox':list(t.get_window_extent(scene.fig.canvas.get_renderer()).bounds),'zorder':t.get_zorder(),'visible':t.get_visible()}
            for t in scene.ax.texts]+[{'figure_text':t.get_text(),'position':list(t.get_position())} for t in scene.fig.texts]

def path_snapshot(scene):
    out={}
    for target in scene.artists:
        out[target]=[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],
                      'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(scene,target)]
    return out

def fill_snapshot(scene):
    return [{'fill':a.get_fill(),'facecolor':list(a.get_facecolor()),'vertices':a.get_path().vertices.tolist(),
             'transform':a.get_transform().get_matrix().tolist(),'zorder':a.get_zorder()}
            for a in scene.ax.patches if a.get_fill()]

scene=adapter.scene(qid)
try:
    noop=png_bytes(scene)
    (OWN/'independent_noop.png').write_bytes(noop)
    before_paths=path_snapshot(scene)
    before_text=texts(scene)
    before_fill=fill_snapshot(scene)
    before_view={'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'aspect':scene.ax.get_aspect(),
                 'axes':list(scene.ax.get_position().bounds),'size':list(scene.fig.canvas.get_width_height()),'dpi':scene.fig.dpi,'points':copy.deepcopy(scene.snap_points)}
    bindings=[]
    for index,action in enumerate(plugin['params']['actions']):
        target=action['target']; interval=action['interval']
        p=next(p for p in object_paths(scene,target) if p['id']==interval['path_id'])
        controls=[s['control'].tolist() for s in p['segments']]
        assert p['sha256']==interval['path_sha256']==canonical_hash(controls)
        count=len(controls)
        endpoints=[]
        for t in [interval['start'],interval['end']]:
            i=min(math.floor(t*count),count-1); local=t*count-i
            control=np.array(controls[i]); endpoints.append(((1-local)*control[0]+local*control[-1]).tolist())
        bindings.append({'action_index':index,'target':target,'interval':interval,'actual_path_sha256':p['sha256'],
                         'all_exact_controls':controls,'selected_exact_endpoints':endpoints,'source_segment_styles':[s['style'] for s in p['segments']]})
    apply_partial_styles(scene,plugin['params']['actions'])
    after_paths=path_snapshot(scene)
    after_text=texts(scene)
    after_fill=fill_snapshot(scene)
    direct=png_bytes(scene)
    (OWN/'independent_direct_replay.png').write_bytes(direct)
    assert before_text==after_text
    assert before_fill==after_fill
    assert before_paths['o3']==after_paths['o3'] and before_paths['o4']==after_paths['o4']
    for key in ['xlim','ylim']:
        assert before_view[key]==list(getattr(scene.ax,'get_'+key)())
    write('native_artist_audit.json',{'runtime_routing':ROUTING,'before_paths':before_paths,'after_paths':after_paths,
          'bindings':bindings,'before_texts':before_text,'after_texts':after_text,'before_fills':before_fill,'after_fills':after_fill,
          'view':before_view,'texts_exactly_preserved':True,'fills_exactly_preserved':True,'original_angle_arcs_exactly_preserved':True})
finally:
    scene.close()

replays=[]
for index in [1,2]:
    norm,data,dig=renderer.render(copy.deepcopy(plugin),frozen=True)
    (OWN/f'independent_replay_{index}.png').write_bytes(data)
    replays.append({'sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':dig,'byte_equal_to_frozen':data==(CAND/'candidate.png').read_bytes()})
    assert norm==plugin and data==(CAND/'candidate.png').read_bytes()
assert direct==(CAND/'candidate.png').read_bytes()
assert pixel_hash(noop)==pixel_hash(PROJECT/'PlaneGeometry/image/Plane427.png')

def arr(path):
    with Image.open(path) as im:
        return np.array(im.convert('RGBA'))

original=arr(OWN/'independent_noop.png')
candidate=arr(CAND/'candidate.png')
changed=np.any(candidate!=original,axis=2)
ys,xs=np.where(changed); pixels=np.column_stack([xs+.5,ys+.5])
matrix=np.array(fresh['canvas']['data_to_pixel'])
def px(name): return (matrix@np.array([*points[name],1.]))[:2]
def distances_to_segment(p,a,b):
    d=b-a;t=np.clip(((p-a)@d)/(d@d),0,1)
    return np.linalg.norm(p-a-t[:,None]*d,axis=1)
minimum=np.minimum.reduce([distances_to_segment(pixels,px(a),px(b)) for a,b in [('S','T'),('V','T'),('S','V')]])
outside=minimum>4
outside_pixels=[{'x':int(x),'y':int(y),'before':original[y,x].tolist(),'after':candidate[y,x].tolist(),'distance_to_marked_segments':float(d)}
                for x,y,d in zip(xs[outside],ys[outside],minimum[outside])]
text_pixel_checks=[]
for t in before_text:
    if 'bbox' not in t:continue
    x,y,w,h=t['bbox'];x0=max(0,math.floor(x)-1);x1=min(768,math.ceil(x+w)+1)
    y0=max(0,768-math.ceil(y+h)-1);y1=min(768,768-math.floor(y)+1)
    text_pixel_checks.append({'text':t['text'],'box':[x0,y0,x1,y1],'changed_pixels':int(changed[y0:y1,x0:x1].sum())})
rgba_hashes={name:pixel_hash(path) for name,path in [('formal',PROJECT/'PlaneGeometry/image/Plane427.png'),('candidate',CAND/'candidate.png'),('noop',OWN/'independent_noop.png')]}
audit={'environment':environment_versions(),'fresh_context_equals_frozen':fresh==frozen_context,'adapter_manifest_all_entries_equal':manifest_matches,
       'manifest_file_count':len(adapter.manifest['files']),'normalized_plugin_identical':normalized==plugin,
       'no_op_formal_pixel_equal':rgba_hashes['noop']==rgba_hashes['formal'],'direct_replay_byte_equal':direct==(CAND/'candidate.png').read_bytes(),
       'replays':replays,'pixel_hashes':rgba_hashes,'candidate_size':list(candidate.shape),'fully_opaque':bool((candidate[:,:,3]==255).all()),
       'changed_pixel_count':int(changed.sum()),'changed_bbox_xyxy':[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())],
       'changed_pixels_outside_4px_marked_segment_tubes':outside_pixels,'text_boxes_pixel_comparison':text_pixel_checks,
       'native_bindings':bindings,'all_figures_closed':not plt.get_fignums(),'pid':os.getpid()}
write('native_render_audit.json',audit)
write('render_write_audit.json',{'pid':os.getpid(),'write_paths':sorted(set(WRITE_EVENTS)),'all_inside_own_root':True})
print(json.dumps({'math':math_audit,'render':audit},ensure_ascii=False,indent=2))
