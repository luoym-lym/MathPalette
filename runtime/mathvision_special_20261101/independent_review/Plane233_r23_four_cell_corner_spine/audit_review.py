from review_env import *
from datetime import datetime, timezone
from itertools import combinations
from collections import Counter
import base64
import io
import math
import re

def rows(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []

def eligibility():
    from dataset_tools import catalog
    b=ROOT/'PlaneGeometry'
    rr=[r for r in rows(b/'dataset.jsonl') if r.get('id')=='Plane233']
    assert len(rr)==1
    r=rr[0]
    a=read(ROOT/'provenance/approvals.json')['approvals']['Plane233']
    content=catalog.content(ROOT,'PlaneGeometry',r)
    current=catalog.digest(content)
    accepted=[r for r in rows(b/'special_variant/accepted_index.jsonl') if r.get('question_id')=='Plane233']
    collected=[r for r in rows(b/'special_variant/collected_index.jsonl') if r.get('question_id')=='Plane233']
    sd=b/'special_variant/Plane233'
    special_files=[str(p.relative_to(ROOT)) for p in sd.rglob('*') if p.is_file()] if sd.exists() else []
    known=['PlaneGeometry/dataset.jsonl','provenance/approvals.json','provenance/source_notes.json',
           'PlaneGeometry/special_variant/accepted_index.jsonl','PlaneGeometry/special_variant/collected_index.jsonl']
    return {'checked_at':datetime.now(timezone.utc).isoformat(),'record':r,'record_sha256':digest(r),
            'approval':a,'recomputed_content_sha256':current,
            'approval_valid':a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and current==a['content_sha256'],
            'accepted_entries':accepted,'collected_entries':collected,'special_directory_exists':sd.exists(),
            'special_files':special_files,'eligible':r['source_dataset']=='MathVision' and current==a['content_sha256'] and not accepted and not collected and not special_files,
            'authoritative_state_hashes':{p:sha(ROOT/p) if (ROOT/p).is_file() else None for p in known},
            'content':content}

ELIG=eligibility()
assert ELIG['eligible'] and ELIG['approval_valid']
record=ELIG['record']
core=[ROOT/'PlaneGeometry'/p for p in ELIG['content']['files']]
core += [ROOT/p for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md',
    'PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json',
    'PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/mathvision_plugins.py',
    'PlaneGeometry/workbench/partial_style.py','PlaneGeometry/workbench/quick_test.py','dataset_tools/mathvision_workbench.py',
    'runtime/mathvision_special_20261101/runtime_isolation.py']]
prior_dirs=[BATCH/'background_06/plane_parts/Plane233',BATCH/'background_23/Plane233']
evidence_files=set(p for d in prior_dirs for p in d.rglob('*') if p.is_file())
for rel in ['Plane233_r23_four_cell_corner_spine_independent_review_brief.txt',
    'Plane233_r23_four_cell_corner_spine_pre_review_evidence_check.json','annotation_semantics_lessons_20261102.json',
    'background_23_assignment.json','background_23/second_review_queue.json','background_23/old_control_reuse.json',
    'harness/quicktest3_isolated.py','background_23/common23.py','background_23/prepare_corner23.py',
    'background_23/run23.py','background_23/review_corner23.py',
    'independent_review/Plane233_two_U_partial_partition_binding/independent_review.json',
    'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
    'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
    if (BATCH/rel).is_file():evidence_files.add(BATCH/rel)
baseline={str(p.resolve().relative_to(ROOT)):sha(p) for p in set(core)|evidence_files if p.is_file()}
save('baseline_hashes.json',baseline)

# Recover cells from the actual frozen segment inventory, without using primary cells.
source=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane233.json')
native_source=read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane233/scene.json')
original_source=read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane233/source.json')
assert source['objects']==native_source['objects'] and source['view']==native_source['view']
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def ce(c):
    x,y=c
    return {edge((x,y),(x+1,y)),edge((x+1,y),(x+1,y+1)),edge((x+1,y+1),(x,y+1)),edge((x,y+1),(x,y))}

objects={o['id']:o for o in source['objects']}
parts={}
origins={}
edges={}
for prefix in ['given','A','B','C','D','E']:
    es={edge(*o['points']) for o in source['objects'] if o['id'].startswith(prefix+'_')}
    points={p for e in es for p in e}
    x0=min(x for x,y in points); y0=min(y for x,y in points)
    origins[prefix]=(x0,y0)
    cs={(x,y) for x in range(x0,max(x for x,y in points)) for y in range(y0,max(y for x,y in points)) if ce((x,y))<=es}
    assert set.union(*(ce(c) for c in cs))==es
    parts[prefix]={(x-x0,y-y0) for x,y in cs}
    edges[prefix]=es
board=parts['given']
assert board=={(x,y) for x in range(4) for y in range(4)}-{(3,0)}
def norm(cs):
    x0=min(x for x,y in cs);y0=min(y for x,y in cs)
    return tuple(sorted((x-x0,y-y0) for x,y in cs))
def orientations(cs,flip=True):
    shapes=set()
    for f in ([1,-1] if flip else [1]):
        for k in range(4):
            ss=[]
            for x,y in cs:
                x=x*f
                for _ in range(k):x,y=-y,x
                ss.append((x,y))
            shapes.add(norm(ss))
    return sorted(shapes)
def enum(cs,flip=True):
    forms=orientations(cs,flip)
    places=set()
    for s in forms:
        w=max(x for x,y in s)+1;h=max(y for x,y in s)+1
        for dx in range(5-w):
            for dy in range(5-h):
                p=frozenset((x+dx,y+dy) for x,y in s)
                if p<=board:places.add(p)
    placements=sorted(places,key=lambda p:tuple(sorted(p)))
    covers=[]; disjoint_pairs=0
    for tri in combinations(range(len(placements)),3):
        p,q,r=[placements[i] for i in tri]
        if p.isdisjoint(q) and p.isdisjoint(r) and q.isdisjoint(r) and p|q|r==board:covers.append(tri)
    for a,b in combinations(placements,2):
        disjoint_pairs+=a.isdisjoint(b)
    # A separately structured first-uncovered-cell recursion cross-checks enumeration.
    dfs_covers=set();branches=[]
    def dfs(left,chosen):
        if not left:
            dfs_covers.add(tuple(sorted(chosen)));return
        first=min(left)
        candidates=[i for i,p in enumerate(placements) if first in p and p<=left]
        branches.append({'remaining':sorted(left),'chosen':chosen,'first':first,'candidates':candidates})
        for i in candidates:dfs(left-placements[i],chosen+[i])
    dfs(set(board),[])
    assert set(covers)==dfs_covers
    return {'orientation_count':len(forms),'orientations':forms,'placement_count':len(placements),
        'placements':[sorted(p) for p in placements],'unordered_triples_checked':math.comb(len(placements),3),
        'disjoint_pairs':disjoint_pairs,'cover_count':len(covers),'cover_placement_indices':covers,
        'covers':[[sorted(placements[i]) for i in c] for c in covers],
        'first_uncovered_recursion_certificate':branches}
results={k:enum(parts[k]) for k in 'ABCDE'}
rotations={k:enum(parts[k],False) for k in 'ABCDE'}
assert [results[k]['cover_count'] for k in 'ABCDE']==[2,0,0,0,0]
spine=frozenset({(0,0),(0,1),(0,2),(0,3),(1,0)})
assert spine<=board and norm(spine) in orientations(parts['C'])
remaining=board-spine
fit_after_spine=[(i,j) for i,p in enumerate(results['C']['placements']) for j,q in enumerate(results['C']['placements'])
                 if i<j and set(map(tuple,p)).isdisjoint(map(tuple,q)) and set(map(tuple,p))|set(map(tuple,q))==remaining]
math_audit={'convention':'Unit cells are identified by lower-left integer coordinates; x right/y up. Three equal pieces means congruent whole-cell polyominoes. Turning a cutout over is allowed: full D4, not an unmentioned same-face orientation restriction.',
    'source_origins':origins,'normalized_cell_inventories':{k:sorted(p) for k,p in parts.items()},
    'each_option_has_five_cells':all(len(parts[k])==5 for k in 'ABCDE'),
    'results':results,'rotation_only_diagnostic':{k:{s:v for s,v in x.items() if s in ('orientation_count','placement_count','cover_count','covers')} for k,x in rotations.items()},
    'unique_correct_answer':'A','C_corner_trial_cells':sorted(spine),'C_trial_complement':sorted(remaining),'C_trial_complement_two_copy_covers':fit_after_spine}
save('independent_math.json',math_audit)

# Frozen request and raw records are independently byte-bound.
design=read(CAND/'design.json');plugin=read(CAND/'plugin.json')
binding=read(TEST/'binding.json');snapshot=read(TEST/'design_snapshot.json');request=read(TEST/'request.json');summary=read(TEST/'summary.json')
request_image=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)
assert request_image==(CAND/'candidate.png').read_bytes()
assert sha(CAND/'design.json')==sha(TEST/'design_snapshot.json')==binding['design_sha256']
assert digest(record)==binding['question_record_sha256']
assert request=={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[
    {'role':'system','content':binding['system_prompt']},{'role':'user','content':[
    {'type':'text','text':record['question']},{'type':'image_url','image_url':{'url':request['messages'][1]['content'][1]['image_url']['url']}}]}]}
assert binding['expected_wrong_answer']==design['expected_wrong_answer']=='C'
assert sha(TEST/'request.json')==binding['request_body_sha256']
assert sha(CAND/'plugin.json')==design['plugin_sha256']
assert sha(CAND/'candidate.png')==binding['image_sha256']==design['image_sha256']
assert design['created_at']<binding['created_at']
raw_runs=[]
for i in [1,2]:
    rn=f'run_{i:02}'
    start=read(TEST/(rn+'_started.json'));run=read(TEST/(rn+'.json'));raw=read(TEST/(rn+'_response.json'))
    for k,v in start.items():assert run[k]==v
    for k in ['request_body_sha256','image_sha256','design_sha256']:assert run[k]==binding[k]
    assert run['response_sha256']==sha(TEST/(rn+'_response.json'))
    assert run['answer']==raw['choices'][0]['message']['content']
    assert summary['results'][i-1]==run
    assert run['status']=='completed' and run['http_status']==200 and run['finish_reason']=='stop' and run['truncated']==False
    assert raw['choices'][0]['finish_reason']=='stop' and raw['model']==run['response_model']=='mimo-v2.6-flash'
    assert raw['usage']['completion_tokens_details']['reasoning_tokens']==0
    assert raw['choices'][0]['message'].get('reasoning_content','')==''
    assert binding['created_at']<run['started_at']<run['finished_at']
    raw_runs.append({'record':run,'started_record':start,'raw_provider_id':raw['id'],'raw_created':raw['created'],
        'raw_response_sha256':sha(TEST/(rn+'_response.json')),'run_record_sha256':sha(TEST/(rn+'.json')),
        'started_record_sha256':sha(TEST/(rn+'_started.json')),
        'full_raw_assistant_content':raw['choices'][0]['message']['content'],
        'content_sha256':hashlib.sha256(raw['choices'][0]['message']['content'].encode()).hexdigest()})
assert raw_runs[0]['record']['finished_at']<raw_runs[1]['record']['started_at']
assert len(list(TEST.glob('run_*_started.json')))==len(list(TEST.glob('run_*_response.json')))==len(list(TEST.glob('run_??.json')))==2
assert not list(TEST.glob('*incomplete*'))
calls=[]
for p in (ROOT/'runtime').rglob('binding.json'):
    if p.is_relative_to(OUT):continue
    try:b=read(p)
    except (ValueError,OSError):continue
    if b.get('question_id')=='Plane233':
        calls.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'created_at':b.get('created_at'),
            'image_sha256':b.get('image_sha256'),'design_sha256':b.get('design_sha256'),
            'preset':b.get('expected_wrong_answer'),'requested_runs':b.get('requested_runs'),
            'runs':[{'path':str(r.relative_to(ROOT)),'status':read(r).get('status'),'final_answer':read(r).get('answer')} for r in sorted(p.parent.glob('run_??.json'))]})
matching=[b for b in calls if b['image_sha256']==binding['image_sha256']]
assert len(matching)==1 and matching[0]['path']==str((TEST/'binding.json').relative_to(ROOT))
save('raw_evidence_audit.json',{'binding':binding,'request_without_image_data':{**request,'messages':[request['messages'][0],
    {'role':'user','content':[request['messages'][1]['content'][0],{'type':'image_url','decoded_sha256':hashlib.sha256(request_image).hexdigest()}]}]},
    'request_body_sha256':sha(TEST/'request.json'),'binding_file_sha256':sha(TEST/'binding.json'),
    'design_snapshot_sha256':sha(TEST/'design_snapshot.json'),'raw_runs':raw_runs,
    'all_saved_Plane233_bindings':calls,'same_image_binding_count':len(matching),
    'new_solver_calls':0,'harness_sha256':sha(BATCH/'harness/quicktest3_isolated.py'),
    'caller_sha256':sha(BATCH/'background_23/run23.py')})

# Current off-line live scene capture and replay using the project executors.
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config, pixel_hash, environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import describe_paths
from dataset_tools.mathvision_workbench import png_bytes
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
config=load_config()
config['runtime_dir']=str(OUT/'state');config['output_dir']=str(OUT/'output')
adapter=RendererAdapter(config)
meta=adapter.inspect_question('Plane233')
save('live_context.json',meta)
assert meta==read(CAND/'fresh_context.json')
sc=adapter.scene('Plane233')
try:
    original_replay=png_bytes(sc)
    sc.fig.canvas.draw()
    live_paths={a['target']:describe_paths(sc,a['target']) for a in plugin['params']['actions']}
finally:sc.close()
assert pixel_hash(original_replay)==pixel_hash(ROOT/'PlaneGeometry/image/Plane233.png')
assert live_paths==read(CAND/'path_fingerprints.json')
renderer=PluginRenderer(config,adapter,{'Plane233':meta})
normalized,replay,px=renderer.render(plugin,frozen=True)
assert normalized==plugin and replay==(CAND/'candidate.png').read_bytes()
assert replay==(CAND/'repeat.png').read_bytes()
assert px==binding['pixel_sha256']==design['pixel_sha256']
(OUT/'replay.png').write_bytes(replay)
img=Image.open(io.BytesIO(replay)).convert('RGBA');arr=np.array(img)
original=Image.open(ROOT/'PlaneGeometry/image/Plane233.png').convert('RGBA');oa=np.array(original)
mask=np.any(arr!=oa,axis=2); yy,xx=np.where(mask);pixels=np.column_stack((xx+.5,yy+.5))
M=np.array(meta['canvas']['data_to_pixel'])
def mapped(p):return (M@np.array([*p,1]))[:2]
mins=np.full(len(pixels),np.inf)
segments=[]
for a in plugin['params']['actions']:
    p,q=map(mapped,objects[a['target']]['points']);v=q-p
    t=np.clip(((pixels-p)*v).sum(axis=1)/(v*v).sum(),0,1)
    mins=np.minimum(mins,np.linalg.norm(pixels-p-t[:,None]*v,axis=1))
    segments.append({'target':a['target'],'data_endpoints':objects[a['target']]['points'],'pixel_endpoints':[p.tolist(),q.tolist()]})
assert max(mins)<3.5

given_cells={(x+11,y+7) for x,y in board}
given_incidence=Counter(e for c in given_cells for e in ce(c))
outer={e for e,n in given_incidence.items() if n==1}
styled_source={edge(*objects[a['target']]['points']) for a in plugin['params']['actions'] if a['target'].startswith('given_')}
assert styled_source<=outer and len(styled_source)==6
def components(cells,barriers):
    pending=set(cells);out=[]
    while pending:
        todo=[pending.pop()];component=set(todo)
        while todo:
            x,y=todo.pop()
            for q in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if q in pending and not (ce((x,y))&ce(q)&barriers):
                    pending.remove(q);component.add(q);todo.append(q)
        out.append(sorted(component))
    return sorted(out)
after=components(given_cells,styled_source)
assert len(after)==1 and len(after[0])==15
marked_per=[]
for idx,a in enumerate(plugin['params']['actions']):
    o=objects[a['target']];e=edge(*o['points'])
    group='given' if a['target'].startswith('given_') else a['target'].split('_')[0]
    origin=origins[group];cells={(x+origin[0],y+origin[1]) for x,y in parts[group]}
    incidence=sum(e in ce(c) for c in cells)
    assert incidence==1
    assert a['type']=='set_object_style' and a['linewidth_pt']==2 and 'linestyle' not in a and 'interval' not in a
    assert a['color'] in ['#DC2626','#2563EB']
    marked_per.append({'action_index':idx,'target':a['target'],'edge':o['points'],'adjacent_occupied_cells':incidence,
        'is_exterior':True,'color':a['color'],'linewidth_pt':a['linewidth_pt'],
        'path_fingerprint':live_paths[a['target']]})
for src,dst in zip(['given_0','given_1','given_2','given_4','given_6','given_10'],
                   ['C_0','C_1','C_2','C_4','C_6','C_10']):
    assert {(x+1,y-7) for x,y in objects[src]['points']}==set(map(tuple,objects[dst]['points']))
render_audit={'isolation':ISOLATION,'environment':environment_versions(),'live_context_equals_frozen':True,
    'fresh_scene_paths_equal_frozen':True,'original_noop_pixels_match':True,'frozen_plugin_actual_schema_normalization':normalized==plugin,
    'replayed_bytes_equal_tested_candidate_and_repeat':True,'png_sha256':sha(OUT/'replay.png'),'pixel_sha256':px,
    'size':list(img.size),'alpha_extrema':img.getextrema()[3],
    'changed_pixel_count':int(mask.sum()),'changed_pixels_max_distance_to_target_stroke_px':float(max(mins)),
    'all_changes_confined_to_3_5px_target_neighborhoods':True,
    'unit_cell_size_px':float(M[0,0]),'native_spine_length_px':float(4*M[0,0]),'native_foot_length_px':float(2*M[0,0]),
    'stroke_width_px':2*100/72,'target_segments':segments,'per_action_geometry':marked_per,
    'source_outer_boundary_unit_edges':len(outer),'source_internal_unit_edges':sum(n==2 for n in given_incidence.values()),
    'marked_source_outer_edges':6,'marked_source_internal_edges':0,
    'source_cell_components_after_treating_all_styled_source_edges_as_cut_barriers':after,
    'new_proper_region_with_original_outer_boundary':False,
    'source_original_shapes_have_zero_fill_artists':all(o['type']=='segment' for o in source['objects']),
    'original_source_record':original_source,'source_scene_geometry_equals_native_source_scene':True}
save('render_geometry_audit.json',render_audit)
plt.close('all')
end_elig=eligibility()
after_hashes={p:sha(ROOT/p) for p in baseline}
changes=[{'path':p,'before':v,'after':after_hashes[p]} for p,v in baseline.items() if v!=after_hashes[p]]
assert not changes
save('preservation_audit.json',{'review_pid':os.getpid(),'baseline_file_count':len(baseline),'changed_scoped_sources_or_old_evidence':changes,
    'eligibility_start':ELIG,'eligibility_end':end_elig,'whole_workspace_unchanged_claim':False,
    'strict_own_directory_guard_before_project_imports':True,'network_subprocess_blocked':True,
    'all_figures_closed':not plt.get_fignums(),'new_solver_calls':0,'no_formal_review_or_Pass_Collect_calls':True})
emit({'math':{k:{s:x[s] for s in ['orientation_count','placement_count','unordered_triples_checked','cover_count']} for k,x in results.items()},
      'rotation_only':{k:x['cover_count'] for k,x in rotations.items()},'inventories':{k:sorted(p) for k,p in parts.items()},
      'eligible':end_elig['eligible'],'prior_binding_count':len(calls),'same_image_bindings':len(matching),
      'raw_response_hashes':[x['raw_response_sha256'] for x in raw_runs],
      'render':{k:render_audit[k] for k in ['changed_pixel_count','changed_pixels_max_distance_to_target_stroke_px',
          'unit_cell_size_px','native_spine_length_px','native_foot_length_px','marked_source_internal_edges']},
      'source_component_sizes':list(map(len,after)),'preserved_file_count':len(baseline),'changed_files':changes,'pid':os.getpid()})
