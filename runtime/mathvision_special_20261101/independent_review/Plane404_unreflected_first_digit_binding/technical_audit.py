import audit as a  # Sets all caches and both write guards before project imports.
from pathlib import Path
import base64
import copy
import hashlib
import io
import json
import sys
from datetime import datetime, timezone
from dataset_tools import catalog
from dataset_tools.mathvision_workbench import build_scene, png_bytes
from PIL import Image
import numpy as np

sys.path.insert(0, str(a.ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config, canonical_hash, pixel_hash, environment_versions
from mathvision_plugins import PluginRenderer, _set_linewidth_preserving_dashes
from drawing_board import describe_captured_scene
from matplotlib.patches import Patch
import matplotlib.pyplot as plt

rows = catalog.rows(a.ROOT/'PlaneGeometry/dataset.jsonl')
row = next(r for r in rows if r['id']=='Plane404')
formal = a.ROOT/'PlaneGeometry'
scene = a.read(formal/row['scene'])
obj = {o['id']:o for o in scene['objects']}
plugin = a.read(a.CAND/'plugin.json')
actions = plugin['params']['actions']
frozen = a.read(a.QUESTION/'input_fingerprints.json')

# Independently derive every displayed numeral from coverage of the seven slots.
def reflect(pt):
    x,y = pt
    return [x,6-y] if y>3 else [x,y]
slots = {'a':[[0,2.5],[1,2.5]],'b':[[1,1.5],[1,2.5]],
         'c':[[1,.5],[1,1.5]],'d':[[0,.5],[1,.5]],
         'e':[[0,.5],[0,1.5]],'f':[[0,1.5],[0,2.5]],
         'g':[[0,1.5],[1,1.5]]}
digits = {'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg',
          '5':'acdfg','6':'acdefg','7':'abc','8':'abcdefg','9':'abcdfg'}
def covers(seg,slot):
    x1,y1 = seg[0]; x2,y2 = seg[1]
    return all(min(x1,x2)<=x<=max(x1,x2) and min(y1,y2)<=y<=max(y1,y2)
               and abs((x-x1)*(y2-y1)-(y-y1)*(x2-x1))<1e-10 for x,y in slot)
inventory = []
for left in (0,3,6):
    entries = []
    for o in scene['objects']:
        if o.get('encoding_bar') and min(p[0] for p in o['points'])>=left and max(p[0] for p in o['points'])<=left+1:
            entries.append({'id':o['id'],'before':o['points'],'after':[reflect(p) for p in o['points']]})
    segments = [[[x-left,y] for x,y in e['after']] for e in entries]
    lit = ''.join(k for k,v in slots.items() if any(covers(s,v) for s in segments))
    recognized = [k for k,v in digits.items() if set(v)==set(lit)]
    assert len(recognized)==1
    inventory.append({'x_origin':left,'segments':entries,'lit_slots':lit,'unique_digit':int(recognized[0])})
assert [e['unique_digit'] for e in inventory]==[5,6,9]
dot_inventory = []
for o in scene['objects']:
    if o['type']=='polygon' and o.get('semantic_fill') and len(o['points'])>20:
        pts = np.array(o['points'])
        dot_inventory.append({'id':o['id'],'center':((pts.min(0)+pts.max(0))/2).tolist(),
                              'radius':float((pts[:,0].max()-pts[:,0].min())/2)})
math = {'axis':obj['o1'],'fold_map':'(x,y) -> (x,6-y) for y>3; lower half fixed',
        'derivation':'Reflection fixes every point on y=3 and reverses signed perpendicular distance; x is fixed. Transparent overlay takes the union of all strokes.',
        'slot_legend':{'a':'top','b':'upper right','c':'lower right','d':'bottom','e':'lower left','f':'upper left','g':'middle'},
        'digits':inventory,'dot_inventory':dot_inventory,'formal_labels':scene['labels'],
        'formal_ambiguities':scene['ambiguities'],'formal_constraints':scene['constraints'],
        'independently_derived_answer':'C = 5:6:9',
        'choice_uniqueness':'A/B/D start with 2; E requires upper-right segment of middle digit, which is absent. Only C matches all three exact segment sets.',
        'intended_local_error':'For the colored first group only, translating its upper-half bars by y-3 instead of reflecting yields upper-right plus lower-left and three horizontals: 2. Correctly folding other groups yields 6:9. Ignoring reflection globally would instead yield 2:9:6, so the proposed target is a local first-digit error.'}
a.save('independent_math.json',math)

# Read authoritative original approval and current Special records, without APIs.
approval = a.read(a.ROOT/'provenance/approvals.json')['approvals']['Plane404']
content = catalog.content(a.ROOT,'PlaneGeometry',row)
catalog.validate_formal_row(a.ROOT,'PlaneGeometry',row)
state = {}
for rel in ['special_variant/accepted_index.jsonl','special_variant/collected_index.jsonl']:
    path = formal/rel
    state[rel]={'sha256':a.sha(path), 'matching_rows':[r for r in catalog.rows(path) if r.get('question_id',r.get('id'))=='Plane404']}
for name in ['recipes.json','collection.json']:
    p = formal/'special_variant/Plane404'/name
    state['Plane404/'+name]={'exists':p.exists(),'data':a.read(p) if p.exists() else None}
manifests=[]
for p in sorted(a.BASE.glob('batch_*/manifest.json')):
    manifests.append({'path':str(p.relative_to(a.ROOT)), 'sha256':a.sha(p),'mentions_Plane404':'Plane404' in p.read_text(encoding='utf-8-sig')})
elig = {'checked_at':datetime.now(timezone.utc).isoformat(),'formal_MathVision':row['source_dataset']=='MathVision',
        'formal_record':row,'question_record_sha256':canonical_hash(row),'original_approval':approval,
        'current_content_sha256':catalog.digest(content),'approval_matches_current_content':catalog.digest(content)==approval['content_sha256'],
        'approved_files':content['files'],'source_notes':content['source_notes'],'authoritative_special':state,
        'existing_delivery_manifests':manifests,'special_directory_exists':(formal/'special_variant/Plane404').exists()}
elig['eligible'] = (elig['formal_MathVision'] and elig['approval_matches_current_content'] and
    approval['reviewer']=='user' and bool(approval['instruction']) and
    all(not v['matching_rows'] for k,v in state.items() if 'matching_rows' in v) and
    all(not v['exists'] for k,v in state.items() if 'exists' in v) and not any(x['mentions_Plane404'] for x in manifests))
a.save('current_eligibility.json',elig)

# Replay via production normalization/rendering, retaining all source files.
class ReadOnlyAdapter:
    def is_native(self,qid): return qid=='Plane404'
    def scene(self,qid):
        assert qid=='Plane404'
        return build_scene(formal,row)
cfg=load_config()
cfg['runtime_dir']=str(a.OUT/'render_state')
cfg['output_dir']=str(a.OUT/'render_output')
ad=ReadOnlyAdapter()
s=ad.scene('Plane404')
try:
    original=png_bytes(s)
    fresh={'original_pixel_sha256':pixel_hash(original),'objects':s.objects,'snap_points':s.snap_points,
           'canvas':describe_captured_scene(s,'Plane404')}
finally:s.close()
(a.OUT/'reproduced_original.png').write_bytes(original)
renderer=PluginRenderer(cfg,ad,{'Plane404':fresh})
normalized,data,digest=renderer.render(plugin,frozen=True)
(a.OUT/'reproduced_candidate.png').write_bytes(data)
normalized2,data2,digest2=renderer.render(plugin,frozen=True)
(a.OUT/'reproduced_candidate_repeat.png').write_bytes(data2)
paths=a.read(a.CAND/'path_fingerprints.json')['targets']
fresh_targets={x['id']:x for x in fresh['canvas']['targets']}
frozen_paths_match={k:v==fresh_targets[k] for k,v in paths.items()}

def snapshot(s):
    result=[]
    for artist in s.ax.get_children():
        entry={'class':type(artist).__name__,'gid':artist.get_gid(),'visible':artist.get_visible(),
               'zorder':artist.get_zorder(),'alpha':artist.get_alpha()}
        for method in ['get_xdata','get_ydata','get_facecolor','get_edgecolor','get_color','get_linewidth',
                       'get_linestyle','get_text','get_position','get_fill','get_xy']:
            if hasattr(artist,method):
                v=getattr(artist,method)()
                if isinstance(v,np.ndarray):v=v.tolist()
                if isinstance(v,tuple):v=list(v)
                entry[method]=v
        if hasattr(artist,'get_path'):
            entry['path_vertices']=artist.get_path().vertices.tolist()
        entry['transform']=artist.get_transform().get_matrix().tolist()
        result.append(entry)
    return result
s=ad.scene('Plane404')
try:
    before=snapshot(s)
    objects_before=copy.deepcopy(s.objects)
    for action in actions:
        for artist in s.artists[action['target']]:
            _set_linewidth_preserving_dashes(artist,action['linewidth_pt'])
            if isinstance(artist,Patch):artist.set_edgecolor(action['color'])
            else:artist.set_color(action['color'])
    after=snapshot(s)
    diff=[]
    for i,(x,y) in enumerate(zip(before,after)):
        changes={k:{'before':x.get(k),'after':y.get(k)} for k in x.keys()|y.keys() if x.get(k)!=y.get(k)}
        if changes:diff.append({'artist_index':i,'gid':x['gid'],'changes':changes})
    assert all(x['gid'] in {v['target'] for v in actions} and set(x['changes'])<={'get_color','get_edgecolor','get_linewidth'} for x in diff)
    assert s.objects==objects_before
    assert png_bytes(s)==data
finally:s.close()
orig=np.array(Image.open(io.BytesIO(original)).convert('RGBA'))
candidate=np.array(Image.open(io.BytesIO(data)).convert('RGBA'))
changed=np.any(orig!=candidate,axis=2)
allowed=np.zeros(changed.shape,dtype=bool)
marker_pixels=[]
for act in actions:
    coords=np.array(fresh_targets[act['target']]['paths'][0])
    xlo,ylo=np.floor(coords.min(0)-3).astype(int)
    xhi,yhi=np.ceil(coords.max(0)+3).astype(int)
    allowed[ylo:yhi+1,xlo:xhi+1]=True
    marker_pixels.append({'id':act['target'],'path_pixels':coords.tolist(),
                          'centerline_length_px':float(np.linalg.norm(coords[-1]-coords[0])),
                          'changed_pixels':int(changed[ylo:yhi+1,xlo:xhi+1].sum()),
                          'width_pt':act['linewidth_pt'],'width_nominal_px':act['linewidth_pt']*100/72})
render={'schema_normalization_unchanged':normalized==plugin,'fresh_context_equals_unit_context':fresh==a.read(a.QUESTION/'context.json'),
        'fresh_context_equals_candidate_context':fresh==a.read(a.CAND/'context.json'),
        'formal_scene_equals_snapshot':scene==a.read(a.QUESTION/'source_scene_snapshot.json'),
        'fresh_target_paths_match':frozen_paths_match,'original_byte_identical':original==(formal/row['image']).read_bytes(),
        'candidate_byte_identical':data==(a.CAND/'candidate.png').read_bytes(),'repeat_byte_identical':data==data2,
        'replay_pixel_sha256':digest,'original_pixel_sha256':pixel_hash(original),'image_sha256':hashlib.sha256(data).hexdigest(),
        'dimensions':list(Image.open(io.BytesIO(data)).size),'alpha_extrema':list(Image.open(io.BytesIO(data)).convert('RGBA').getextrema()[3]),
        'only_artist_changes':diff,'all_geometries_fill_text_visibility_and_transforms_unchanged':True,
        'changed_pixel_count':int(changed.sum()),'changed_pixels_outside_five_paths_plus_3px':int((changed & ~allowed).sum()),
        'markers':marker_pixels,'environment':environment_versions(),'all_figures_closed':not bool(plt.get_fignums())}
a.save('render_and_preservation_audit.json',render)

# Bind exact request bytes, images, design snapshots, starts, raw completions.
tests=[]
for folder,role in [(a.CAND,'candidate'),(a.QUESTION/'original_control','original_control')]:
    invocations=list((folder/'tests').glob('quicktest3_*'))
    assert len(invocations)==1
    inv=invocations[0];binding=a.read(inv/'binding.json');payload=a.read(inv/'request.json')
    uri=payload['messages'][1]['content'][1]['image_url']['url']
    decoded=base64.b64decode(uri.split(',',1)[1])
    assert decoded==(folder/'candidate.png').read_bytes()
    assert payload=={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[
        {'role':'system','content':binding['system_prompt']},{'role':'user','content':[
            {'type':'text','text':row['question']},{'type':'image_url','image_url':{'url':uri}}]}]}
    assert a.sha(inv/'request.json')==binding['request_body_sha256']
    assert a.sha(folder/'candidate.png')==binding['image_sha256']
    assert a.sha(folder/'design.json')==a.sha(inv/'design_snapshot.json')==binding['design_sha256']
    assert pixel_hash(decoded)==binding['pixel_sha256']
    assert canonical_hash(row)==binding['question_record_sha256']
    design=a.read(folder/'design.json')
    assert design['expected_wrong_answer']==binding['expected_wrong_answer']=='A'
    assert design['created_at'] < binding['created_at']
    assert a.sha(formal/'workbench/quick_test.py')==binding['reference_quick_test_sha256']
    records=[]
    for n in (1,2):
        stem=f'run_{n:02d}';r=a.read(inv/(stem+'.json'));start=a.read(inv/(stem+'_started.json'));raw=a.read(inv/(stem+'_response.json'))
        assert all(r[k]==v for k,v in start.items())
        for k in ('request_body_sha256','image_sha256','design_sha256'):assert r[k]==binding[k]
        assert r['response_sha256']==a.sha(inv/(stem+'_response.json'))
        assert r['answer']==raw['choices'][0]['message']['content']
        assert raw['model']==r['response_model']=='mimo-v2.6-flash'
        assert raw['choices'][0]['finish_reason']==r['finish_reason']=='stop'
        assert r['status']=='completed' and not r['truncated'] and r['http_status']==200 and r['thinking']==''
        assert raw['usage']['completion_tokens_details']['reasoning_tokens']==0
        records.append({'run':n,'run_id':r['run_id'],'response_id':raw['id'],'response_sha256':r['response_sha256'],
                        'started_at':r['started_at'],'finished_at':r['finished_at'],'http_status':r['http_status'],
                        'finish_reason':r['finish_reason'],'truncated':r['truncated'],
                        'complete_raw_answer_manually_read':True,'complete_answer_text':r['answer'],
                        'run_sha256':a.sha(inv/(stem+'.json')),'start_sha256':a.sha(inv/(stem+'_started.json'))})
    assert records[0]['finished_at']<records[1]['started_at']
    summary=a.read(inv/'summary.json')
    assert summary['two_completed'] and summary['results']==[a.read(inv/f'run_{n:02d}.json') for n in (1,2)]
    tests.append({'role':role,'directory':str(inv.relative_to(a.ROOT)),'binding':binding,'binding_sha256':a.sha(inv/'binding.json'),
                  'request_sha256':a.sha(inv/'request.json'),'request_text_is_current_formal_question':True,
                  'image_data_uri_decodes_to_exact_frozen_png':True,'no_preset_design_intent_answer_metadata_in_payload':True,
                  'pre_call_design_created_at':design['created_at'],'design_mtime_utc':a.pathinfo(folder/'design.json')['mtime_utc'],
                  'image_mtime_utc':a.pathinfo(folder/'candidate.png')['mtime_utc'],'runs':records,
                  'all_invocation_file_hashes':[a.pathinfo(p) for p in sorted(inv.iterdir()) if p.is_file()]})
all_bindings=[]
for p in a.BASE.rglob('binding.json'):
    if p.is_relative_to(a.OUT):continue
    b=a.read(p)
    if b.get('question_id')=='Plane404':
        all_bindings.append({'path':str(p.relative_to(a.ROOT)),'image_sha256':b.get('image_sha256'),'design_sha256':b.get('design_sha256'),'requested_runs':b.get('requested_runs')})
refs=[a.BASE/'harness/quicktest3_isolated.py',a.UNIT/'harness/quicktest3_isolated.py',a.UNIT/'run_pair.py',a.UNIT/'tools08.py',formal/'workbench/quick_test.py']
evidence={'tests':tests,'all_Plane404_bindings_in_current_experiment_tree':all_bindings,
          'harness_files':[a.pathinfo(p) for p in refs],
          'harness_copy_byte_identical':refs[0].read_bytes()==refs[1].read_bytes(),
          'candidate_test_invocations':len(list((a.CAND/'tests').iterdir())),
          'candidate_run_starts':len(list((a.CAND/'tests').rglob('run_*_started.json'))),
          'candidate_complete_raw_responses':len(list((a.CAND/'tests').rglob('run_*_response.json'))),
          'candidate_incomplete_response_files':[str(p) for p in (a.CAND/'tests').rglob('*incomplete*')],
          'candidate_new_solver_calls_by_reviewer':0,
          'current_dataset_full_hash_equal_to_historical_binding':a.sha(formal/'dataset.jsonl')==tests[0]['binding']['dataset_sha256']}
a.save('raw_bindings_and_full_responses.json',evidence)

# Distinguish this question's frozen inputs from unrelated/global mutable files.
relevant=set(content['files'])
checks=[]
for rel in relevant:
    p=(formal/rel).resolve()
    key=str(p.relative_to(a.ROOT))
    expected=frozen['files'].get(key)
    checks.append({'path':key,'expected':expected,'current':a.sha(p),'match':expected==a.sha(p)})
extra=['dataset_tools/mathvision_workbench.py','PlaneGeometry/workbench/mathvision_plugins.py',
       'PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/drawing_board.py',
       'MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md']
for key in extra:
    checks.append({'path':key,'expected':frozen['files'].get(key.replace('/','\\')),
                   'current':a.sha(a.ROOT/key),'match':frozen['files'].get(key.replace('/','\\'))==a.sha(a.ROOT/key)})
assert all(x['match'] for x in checks)
a.save('frozen_input_checks.json',{'relevant_files':checks,'question_record_matches':canonical_hash(row)==frozen['question_record_sha256'],
                                'all_relevant_files_match':True,
                                'runtime_progress_hashes_are_diagnostic_not_frozen_evidence':True})
a.emit({'eligible':elig['eligible'],'digits':[e['unique_digit'] for e in inventory],
        'render':{k:v for k,v in render.items() if k not in ['only_artist_changes','markers']},
        'exact_candidate_calls':evidence['candidate_run_starts'],'all_Plane404_bindings':all_bindings,
        'current_dataset_full_hash_equal_to_historical_binding':evidence['current_dataset_full_hash_equal_to_historical_binding'],
        'all_relevant_frozen_files_match':True})
