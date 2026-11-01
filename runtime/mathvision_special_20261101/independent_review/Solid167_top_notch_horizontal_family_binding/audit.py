"""Read-only evidence audit; all writes restricted to this new review directory."""
from pathlib import Path
import os, sys, json, hashlib, base64, io, math
from datetime import datetime, timezone

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
SESSION = ROOT / 'runtime/mathvision_special_20261101'
SOURCE = SESSION / 'background_07/solid_worker/Solid167'
CAND = SOURCE / 'top_notch_horizontal_family_binding'
EVID = CAND / 'tests/quicktest3_20261101T150754_53f9ec4b468e'
for key, sub in {'TEMP':'tmp', 'TMP':'tmp', 'MPLCONFIGDIR':'mpl', 'XDG_CACHE_HOME':'cache', 'PYTHONPYCACHEPREFIX':'pycache'}.items():
    directory = HERE / sub
    directory.mkdir(exist_ok=True)
    os.environ[key] = str(directory)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def check_write(path):
    if path is None or isinstance(path, int):
        return
    target = Path(os.fsdecode(path)).resolve()
    if not target.is_relative_to(HERE):
        raise PermissionError('Review write outside assigned directory: ' + str(target))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
sys.addaudithook(guard)
sys.path.insert(0, str(SESSION))
from runtime_isolation import install
isolation = install(HERE / 'render_tmp')
sys.path.insert(0, str(ROOT / 'SolidGeometry/workbench'))
sys.path.insert(0, str(ROOT))
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from dataset_tools.catalog import content, digest
from dataset_tools import mathvision_workbench as bridge
from workbench_io import load_config, pixel_hash, environment_versions
from renderer_adapter import scene_png
from render_plugins import PluginRenderer
from partial_style import object_paths

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def rows(path):
    return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def rel(path):
    return str(Path(path).relative_to(ROOT)).replace('\\','/')

def write(path, value):
    with Path(path).open('x', encoding='utf-8') as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')

frozen = read(SOURCE / 'frozen_inputs.json')
record = next(r for r in rows(ROOT / 'SolidGeometry/dataset.jsonl') if r['id'] == 'Solid167')
design = read(CAND / 'design.json')
plugin = read(CAND / 'plugin.json')
context = read(CAND / 'context.json')
binding = read(EVID / 'binding.json')
snapshot = read(EVID / 'design_snapshot.json')
request = read(EVID / 'request.json')
summary = read(EVID / 'summary.json')
source_paths = [p for p in SOURCE.rglob('*') if p.is_file()]
tracked = set(source_paths) | {ROOT / p for p in frozen['files']}
tracked |= {ROOT / p for p in ['AGENTS.md','SolidGeometry/dataset.jsonl','provenance/approvals.json','provenance/source_notes.json','SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl','SolidGeometry/workbench/quick_test.py']}
tracked |= {SESSION / 'runtime_isolation.py', SESSION / 'harness/quicktest3_isolated.py'}
before = {rel(p):sha(p) for p in sorted(tracked) if p.is_file()}
checks = {}
def verify(name, condition):
    checks[name] = bool(condition)

verify('formal_record_exact', record == read(SOURCE / 'formal_record.json'))
verify('formal_canonical_sha', digest(record) == binding['question_record_sha256'] == frozen['question_record_sha256'])
frozen_current = {p:{'expected':v, 'actual':sha(ROOT/p), 'match':sha(ROOT/p)==v} for p,v in frozen['files'].items()}
verify('all_frozen_files_match', all(v['match'] for v in frozen_current.values()))
verify('record_snapshot_file_sha', sha(SOURCE/'formal_record.json') == digest(record))
verify('design_snapshot_bytes', (CAND/'design.json').read_bytes() == (EVID/'design_snapshot.json').read_bytes())
verify('design_sha_bound', sha(CAND/'design.json') == binding['design_sha256'])
verify('preset_D_everywhere', design['expected_wrong_answer'] == snapshot['expected_wrong_answer'] == binding['expected_wrong_answer'] == summary['expected_wrong_answer'] == 'D')
verify('preset_predates_both_calls', design['created_at'] < binding['created_at'] < read(EVID/'run_01_started.json')['started_at'])
verify('candidate_sha_bound', sha(CAND/'candidate.png') == binding['image_sha256'] == design['candidate_png_sha256'])
verify('candidate_pixels_bound', pixel_hash(CAND/'candidate.png') == binding['pixel_sha256'])
verify('context_sha_bound', sha(CAND/'context.json') == design['context_sha256'])
verify('marker_bindings_sha_bound', sha(CAND/'marker_path_bindings.json') == design['marker_path_bindings_sha256'])
verify('request_body_sha', sha(EVID/'request.json') == binding['request_body_sha256'])
verify('dataset_sha_at_call_still_current', sha(ROOT/'SolidGeometry/dataset.jsonl') == binding['dataset_sha256'])
verify('reference_quicktest_sha', sha(ROOT/'SolidGeometry/workbench/quick_test.py') == binding['reference_quick_test_sha256'])
verify('request_top_level_exact', set(request) == {'model','stream','thinking','messages'})
verify('actual_quicktest3_disabled', request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False and binding['profile']=='quicktest3')
verify('only_system_and_one_user_message', len(request['messages'])==2 and [m['role'] for m in request['messages']]==['system','user'])
verify('system_matches_reference', request['messages'][0]['content'] == binding['system_prompt'])
user = request['messages'][1]['content']
verify('only_formal_text_plus_image', len(user)==2 and user[0]=={'type':'text','text':record['question']} and set(user[1])=={'type','image_url'} and set(user[1]['image_url'])=={'url'})
encoded = user[1]['image_url']['url']
image_bytes = base64.b64decode(encoded.split(',',1)[1], validate=True)
verify('embedded_png_exact', encoded.startswith('data:image/png;base64,') and image_bytes==(CAND/'candidate.png').read_bytes())
verify('no_answer_preset_intent_parameters_in_messages', request['messages'][0]['content']==binding['system_prompt'] and user[0]['text']==record['question'] and len(user)==2)
verify('summary_binding_exact', all(summary.get(k)==v for k,v in binding.items()))
runs = []
for index in (1,2):
    run = read(EVID/f'run_{index:02d}.json')
    start = read(EVID/f'run_{index:02d}_started.json')
    raw = read(EVID/f'run_{index:02d}_response.json')
    choice = raw['choices'][0]
    verify(f'run{index}_raw_hash', sha(EVID/f'run_{index:02d}_response.json')==run['response_sha256'])
    verify(f'run{index}_complete_exact_content', run['answer']==choice['message']['content'] and run['thinking']=='' and run['finish_reason']==choice['finish_reason']=='stop' and run['status']=='completed' and run['http_status']==200 and run['truncated'] is False)
    verify(f'run{index}_start_binding_exact', all(run.get(k)==v for k,v in start.items()) and run['image_sha256']==binding['image_sha256'] and run['design_sha256']==binding['design_sha256'] and run['request_body_sha256']==binding['request_body_sha256'])
    verify(f'run{index}_response_profile', raw['model']==run['response_model']=='mimo-v2.6-flash' and run['usage']['completion_tokens_details']['reasoning_tokens']==0)
    verify(f'run{index}_summary_exact', summary['results'][index-1]==run)
    runs.append({'index':index,'run':run,'raw_response_id':raw['id'],'provider_created_utc':datetime.fromtimestamp(raw['created'],timezone.utc).isoformat(),'full_raw_message':choice['message']['content']})
verify('exactly_two_starts_and_records', len(list(EVID.glob('run_*_started.json')))==2 and len([p for p in EVID.glob('run_*.json') if p.stem in ('run_01','run_02')])==2)
verify('only_one_invocation_for_this_candidate', len(list((CAND/'tests').iterdir()))==1)
verify('sequential_completed_pair', runs[0]['run']['finished_at'] < runs[1]['run']['started_at'] < runs[1]['run']['finished_at'])

approval = read(ROOT/'provenance/approvals.json')['approvals']['Solid167']
approval_content = content(ROOT,'SolidGeometry',record)
accepted = [r for r in rows(ROOT/'SolidGeometry/special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))=='Solid167']
collected = [r for r in rows(ROOT/'SolidGeometry/special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))=='Solid167']
formal_folder = ROOT/'SolidGeometry/special_variant/Solid167'
folder_files = [rel(p) for p in formal_folder.rglob('*') if p.is_file()] if formal_folder.exists() else []
eligibility = {'checked_at':datetime.now(timezone.utc).isoformat(),'source_dataset':record['source_dataset'],'source_key':record['source_key'],'approval':approval,'computed_approval_content_sha256':digest(approval_content),'accepted_entries':accepted,'collected_entries':collected,'formal_special_directory_exists':formal_folder.exists(),'formal_special_files':folder_files,'checks_sha256':{p:before[p] for p in ('SolidGeometry/dataset.jsonl','provenance/approvals.json','SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl')}}
verify('currently_formal_MathVision', record['source_dataset']=='MathVision')
verify('current_original_user_approval', approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(approval_content)==approval['content_sha256'])
verify('current_noPass_notCollected_noSpecialCompletion', not accepted and not collected and not folder_files)
eligibility['eligible'] = all(checks[k] for k in ('currently_formal_MathVision','current_original_user_approval','current_noPass_notCollected_noSpecialCompletion'))
diagnostics = {}
for filename in ('remaining_questions.jsonl','exploration_report.json'):
    path = SESSION/filename
    data = rows(path) if filename.endswith('jsonl') else read(path)
    relevant = [r for r in data if r.get('question_id',r.get('id'))=='Solid167'] if isinstance(data,list) else {k:[r for r in v if isinstance(r,dict) and r.get('question_id',r.get('id'))=='Solid167'] for k,v in data.items() if isinstance(v,list)}
    diagnostics[filename] = {'current_sha256':sha(path),'relevant_progress':relevant,'authoritative_for_math_or_eligibility':False}
preservation = read(SESSION/'background_07/source_preservation_classification_final.json')
diagnostics['unit07_preservation'] = {k:preservation[k] for k in ('checked_at','full_workspace_unchanged','drift_actor','no_restore_or_rewrite_of_concurrent_changes')}
diagnostics['unit07_preservation']['Solid167'] = next(r for r in preservation['questions'] if r['question_id']=='Solid167')

class AuditAdapter:
    def __init__(self):
        self.config=load_config()
        self.config.update(runtime_dir=str(HERE/'state'),output_dir=str(HERE/'output'))
        self.records={'Solid167':record}
        self.original_paths={'Solid167':ROOT/'SolidGeometry'/record['image']}
    def scene(self,qid):
        return bridge.build_scene(ROOT/'SolidGeometry',self.records[qid])

adapter=AuditAdapter()
capture=adapter.scene('Solid167')
try:
    baseline_bytes,baseline_pixels=scene_png(capture)
    verify('independent_noop_formal_pixels', baseline_pixels==pixel_hash(adapter.original_paths['Solid167']))
    with matplotlib.rc_context(capture.settings):
        capture.fig.canvas.draw()
    width,height=capture.fig.canvas.get_width_height()
    transform=np.array([[1,0,0],[0,-1,height],[0,0,1]])@capture.ax.transData.get_affine().get_matrix()
    metadata={'original_pixel_sha256':baseline_pixels,'objects':capture.objects,'snap_points':capture.snap_points,'xlim':list(capture.ax.get_xlim()),'ylim':list(capture.ax.get_ylim()),'canvas':{'width':width,'height':height,'data_to_pixel':transform.tolist(),'pixel_to_data':np.linalg.inv(transform).tolist(),'coordinate_system':'frozen_projected_2d'}}
    for key in ('objects','snap_points','canvas','xlim','ylim','original_pixel_sha256'):
        verify('fresh_context_'+key,metadata[key]==context[key])
    paths={target:object_paths(capture,target) for target in ('line14','line42','line43','line44','line45')}
    stored_paths=read(CAND/'marker_path_bindings.json')
    path_summary={target:[{**{k:path[k] for k in ('id','sha256','closed')},'controls':[s['control'].tolist() for s in path['segments']]} for path in pp] for target,pp in paths.items()}
    verify('every_exact_marker_path_regenerated',path_summary==stored_paths)
finally:
    capture.close()
renderer=PluginRenderer(adapter.config,adapter,{'Solid167':metadata})
normalized,replay,replay_pixels=renderer.render(plugin,frozen=True)
normalized2,replay2,replay_pixels2=renderer.render(plugin,frozen=True)
verify('plugin_schema_and_interval_validation',normalized==normalized2==plugin)
verify('independent_replay_exact_png',replay==(CAND/'candidate.png').read_bytes())
verify('independent_replay_exact_pixels',replay_pixels==replay_pixels2==binding['pixel_sha256'])
verify('independent_repeat_deterministic',replay==replay2)
(HERE/'replayed_candidate.png').write_bytes(replay)

scene=read(ROOT/'SolidGeometry/dataset_generator/scenes/Solid167.json')
p=scene['points']
math_result={}
for name,ids,axis,fold,other,second in [('top',['p49','p50','p51'],1,p['p49'][1],0,p['p52'][0]),('left',['p52','p53','p54'],0,p['p52'][0],1,p['p49'][1])]:
    tri=np.array([p[i][:2] for i in ids])
    lens=[float(np.linalg.norm(tri[i]-tri[(i+1)%3])) for i in range(3)]
    mirrored=tri.copy();mirrored[:,axis]=2*fold-mirrored[:,axis]
    diamond=np.unique(np.vstack([tri,mirrored]),axis=0)
    mate=diamond.copy();mate[:,other]=2*second-mate[:,other]
    ext=np.ptp(diamond,axis=0)
    verify('triangle_'+name+'_equilateral',max(lens)-min(lens)<1e-12)
    math_result[name]={'triangle_point_ids':ids,'flat_triangle':tri.tolist(),'side_lengths':lens,'fold_axis_coordinate':fold,'diamond_vertices':diamond.tolist(),'reflection_mate_vertices':mate.tolist(),'diamond_extents':ext.tolist(),'diamond_centres':[diamond.mean(0).tolist(),mate.mean(0).tolist()]}
option_holes={}
for oid in range(21,53):
    obj=next((o for o in scene['objects'] if o['id']==f'line{oid}'),None)
    if not obj or obj.get('role')!='cut_boundary':
        continue
    xy=np.array([p[v][:2] for v in obj['points']])
    xx=np.ptp(xy,axis=0)
    pts=transform@np.column_stack([xy,np.ones(len(xy))]).T
    option_holes[obj['id']]={'points':xy.tolist(),'extent_xy':xx.tolist(),'width_height_ratio':float(xx[0]/xx[1]),'pixel_bbox_extents':np.ptp(pts[:2],axis=1).tolist()}

with Image.open(CAND/'candidate.png') as im:
    a=np.array(im.convert('RGBA'))
with Image.open(ROOT/'SolidGeometry/image/Solid167.png') as im:
    b=np.array(im.convert('RGBA'))
delta=np.any(a!=b,axis=2)
yy,xx=np.where(delta)
component_boxes=[]
pending=set(zip(xx.tolist(),yy.tolist()))
while pending:
    todo=[pending.pop()];component=[]
    while todo:
        x,y=todo.pop();component.append((x,y))
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                q=(x+dx,y+dy)
                if q in pending:
                    pending.remove(q);todo.append(q)
    cx,cy=zip(*component)
    component_boxes.append({'bbox_inclusive':[min(cx),min(cy),max(cx),max(cy)],'changed_pixels':len(component)})
verify('exactly_six_local_pixel_change_components',len(component_boxes)==6)
verify('opaque_768_canvas',a.shape==(768,768,4) and bool(np.all(a[:,:,3]==255)))
for alternative, box in {'A':(50,470,165,620),'B':(185,470,305,620),'C':(325,470,440,620),'E':(602,470,718,620),'fold_labels':(180,145,450,190)}.items():
    x0,y0,x1,y1=box
    verify('unchanged_pixels_'+alternative,bool(np.array_equal(a[y0:y1,x0:x1],b[y0:y1,x0:x1])))

after={rel(p):sha(p) for p in sorted(tracked) if p.is_file()}
verify('tracked_existing_sources_evidence_and_eligibility_unchanged_during_audit',before==after)
verify('no_open_matplotlib_figures',not plt.get_fignums())
result={'checked_at':datetime.now(timezone.utc).isoformat(),'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],'evidence_files':{rel(p):{'sha256':sha(p),'length':p.stat().st_size,'modified_utc':datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()} for p in sorted(tracked) if p.is_file()},'frozen_input_verification':frozen_current,'eligibility':eligibility,'diagnostic_runtime_progress':diagnostics,'request_without_base64':{**request,'messages':[request['messages'][0],{'role':'user','content':[user[0],{'type':'image_url','image_url':{'url':'<exact frozen PNG data; decoded bytes independently matched>'}}]}]},'runs':runs,'fresh_marker_paths':path_summary,'replay':{'png_sha256':hashlib.sha256(replay).hexdigest(),'pixel_sha256':replay_pixels,'environment':environment_versions(),'appearance_changes':renderer.appearance_changes(plugin),'shared_isolation':isolation,'stricter_write_guard_root':str(HERE)},'independent_math_calculation':math_result,'option_hole_geometry':option_holes,'pixel_difference':{'changed_pixels':int(delta.sum()),'components':sorted(component_boxes,key=lambda v:v['bbox_inclusive'][1]),'overall_bbox':[int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())]}}
write(HERE/'audit_results.json',result)
print(json.dumps({'failed_checks':result['failed_checks'],'eligibility':eligibility,'request':result['request_without_base64'],'math':math_result,'option_holes':option_holes,'pixel_difference':result['pixel_difference'],'evidence_sha256':{Path(k).name:v['sha256'] for k,v in result['evidence_files'].items() if k.startswith(rel(EVID)) or k in [rel(CAND/'plugin.json'),rel(CAND/'design.json')]},'environment':result['replay']['environment']},ensure_ascii=False,indent=2))
