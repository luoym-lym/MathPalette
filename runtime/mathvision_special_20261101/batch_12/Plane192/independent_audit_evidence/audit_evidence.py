from review_bootstrap import *
import json, hashlib, base64, io, re
from datetime import datetime, timezone
from PIL import Image
from dataset_tools import catalog

CAND = BASE / 'background_23/Plane192/r23_maximal_run_unit_binding'
BRANCH = ROOT / 'PlaneGeometry'
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(name, data): (OWN / name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def rows(p): return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def snap(p):
    p = Path(p)
    return {'path': str(p), 'sha256': sha(p), 'size': p.stat().st_size,
            'mtime_utc': datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).isoformat()}
record = next(x for x in rows(BRANCH/'dataset.jsonl') if x['id']=='Plane192')
content = catalog.content(ROOT, 'PlaneGeometry', record)
approval = read(ROOT/'provenance/approvals.json')['approvals']['Plane192']
accepted = [x for x in rows(BRANCH/'special_variant/accepted_index.jsonl') if x.get('question_id', x.get('id'))=='Plane192']
collected = [x for x in rows(BRANCH/'special_variant/collected_index.jsonl') if x.get('question_id', x.get('id'))=='Plane192']
formal_special_dir = BRANCH/'special_variant/Plane192'
special_files = [str(x) for x in formal_special_dir.rglob('*') if x.is_file()] if formal_special_dir.exists() else []
eligibility = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'record': record,
    'approval': approval, 'current_content_sha256': catalog.digest(content),
    'approval_matches': approval['content_sha256']==catalog.digest(content),
    'accepted_entries': accepted, 'collected_entries': collected,
    'formal_special_directory_exists': formal_special_dir.exists(), 'formal_special_files': special_files,
    'eligible': record['source_dataset']=='MathVision' and approval['reviewer']=='user' and bool(approval['instruction'])
        and approval['content_sha256']==catalog.digest(content) and not accepted and not collected and not special_files,
    'authoritative_inputs': [snap(BRANCH/'dataset.jsonl'), snap(ROOT/'provenance/approvals.json'),
        snap(BRANCH/'special_variant/accepted_index.jsonl'), snap(BRANCH/'special_variant/collected_index.jsonl')]}
write('eligibility_current.json', eligibility)
files = set(CAND.rglob('*')) | set((BASE/'background_23/Plane192').glob('*.json'))
for relative in content['files']:
    files.add((BRANCH/relative).resolve())
for relative in ['AGENTS.md', 'MATHPALETTE_PROTOCOL.md', 'PlaneGeometry/REDRAW_PROTOCOL.md',
    'PlaneGeometry/dataset_generator/protocol.json', 'PlaneGeometry/workbench/README.md',
    'PlaneGeometry/workbench/agent_prompt.md', 'PlaneGeometry/workbench/plugin.schema.json',
    'PlaneGeometry/workbench/quick_test.py', 'dataset_tools/catalog.py', 'dataset_tools/mathvision_workbench.py',
    'runtime/mathvision_special_20261101/runtime_isolation.py',
    'runtime/mathvision_special_20261101/annotation_semantics_lessons_20261102.json',
    'runtime/mathvision_special_20261101/Plane192_r23_maximal_run_unit_binding_independent_review_brief.txt',
    'runtime/mathvision_special_20261101/Plane192_r23_maximal_run_unit_binding_pre_review_evidence_check.json',
    'runtime/mathvision_special_20261101/background_23/second_review_queue.json',
    'runtime/mathvision_special_20261101/background_23/old_control_reuse.json',
    'runtime/mathvision_special_20261101/background_23/prepare23.py',
    'runtime/mathvision_special_20261101/background_23/run23.py',
    'runtime/mathvision_special_20261101/background_23/harness/quicktest3_isolated.py']:
    files.add(ROOT/relative)
prior_dirs = [BASE/f'plane_explore/Plane192/v{i:02d}' for i in (1,2,3)]
prior_reports = [BASE/'independent_review'/d/'independent_review.json' for d in
    ['Plane192_v03','Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane233_r19_double_u_partition']]
for d in prior_dirs:
    files.update(d.rglob('*'))
files.update(p for p in prior_reports if p.exists())
manifest = {str(p.relative_to(ROOT)):snap(p) for p in sorted(files) if p.is_file()}
write('read_only_baseline_manifest.json', manifest)
tests = list((CAND/'tests').glob('*'))
assert len(tests)==1 and tests[0].is_dir()
TEST=tests[0]
binding=read(TEST/'binding.json'); design=read(CAND/'design.json'); request=read(TEST/'request.json')
payload_png=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1], validate=True)
with Image.open(io.BytesIO(payload_png)) as im:
    rgba=im.convert('RGBA'); pixel_sha=hashlib.sha256(f'{rgba.width}x{rgba.height}:RGBA:'.encode()+rgba.tobytes()).hexdigest()
checks={
    'candidate_hash': sha(CAND/'candidate.png')==binding['image_sha256']==design['image_sha256'],
    'pixel_hash': pixel_sha==binding['pixel_sha256']==design['pixel_sha256'],
    'image_bytes_in_request': payload_png==(CAND/'candidate.png').read_bytes(),
    'design_hash': sha(CAND/'design.json')==binding['design_sha256'],
    'design_snapshot_bytes': (CAND/'design.json').read_bytes()==(TEST/'design_snapshot.json').read_bytes(),
    'plugin_hash': sha(CAND/'plugin.json')==design['plugin_sha256'],
    'fresh_context_hash': sha(CAND/'fresh_context.json')==design['fresh_context_sha256'],
    'difference_audit_hash': sha(CAND/'design_difference_audit.json')==design['difference_audit_sha256'],
    'request_hash': sha(TEST/'request.json')==binding['request_body_sha256'],
    'question_record_hash': catalog.digest(record)==binding['question_record_sha256'],
    'current_aggregate_dataset_hash_matches_historical': sha(BRANCH/'dataset.jsonl')==binding['dataset_sha256'],
    'reference_quick_test_hash': sha(BRANCH/'workbench/quick_test.py')==binding['reference_quick_test_sha256'],
    'exact_question': request['messages'][1]['content'][0]=={'type':'text','text':record['question']} and binding['question']==record['question'],
    'system_prompt_exact': request['messages'][0]=={'role':'system','content':binding['system_prompt']},
    'only_math_question_and_png': len(request['messages'])==2 and len(request['messages'][1]['content'])==2 and
        set(request)=={'model','stream','thinking','messages'},
    'quicktest3': binding['profile']=='quicktest3' and request['model']=='mimo-v2.6-flash' and
        request['thinking']=={'type':'disabled'} and request['stream'] is False,
    'preset_before_calls': design['expected_wrong_answer']==binding['expected_wrong_answer']=='A' and
        design['created_at']<binding['created_at'],
    'candidate_and_design_mtimes_before_binding': all(datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()<binding['created_at'] for p in [CAND/'candidate.png',CAND/'design.json',CAND/'plugin.json']),
}
runs=[]
for index in (1,2):
    run=read(TEST/f'run_{index:02d}.json'); raw=read(TEST/f'run_{index:02d}_response.json'); started=read(TEST/f'run_{index:02d}_started.json')
    final=raw['choices'][0]['message']['content']
    c={'raw_hash':sha(TEST/f'run_{index:02d}_response.json')==run['response_sha256'],
       'full_content_equals_saved_answer':final==run['answer'],
       'complete':run['status']=='completed' and run['http_status']==200 and run['finish_reason']=='stop' and not run['truncated'] and raw['choices'][0]['finish_reason']=='stop',
       'same_frozen_binding':all(run[k]==binding[k] for k in ['request_body_sha256','image_sha256','design_sha256']),
       'start_file_matches':all(run[k]==v for k,v in started.items()),
       'chronological':binding['created_at']<=run['started_at']<run['finished_at'],
       'response_model':raw['model']==run['response_model']=='mimo-v2.6-flash',
       'zero_reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens']==0 and run['thinking']==''}
    runs.append({'index':index,'checks':c,'run_id':run['run_id'],'provider_id':raw['id'],
       'started_at':run['started_at'],'finished_at':run['finished_at'],
       'raw':snap(TEST/f'run_{index:02d}_response.json'),'run_record':snap(TEST/f'run_{index:02d}.json'),
       'full_final':final, 'explicit_final_letter':'A', 'explicit_final_text':final.splitlines()[-1],
       'usage':raw['usage']})
matching=[]
for p in BASE.rglob('binding.json'):
    v=read(p)
    if v.get('image_sha256')==binding['image_sha256']:
        matching.append({'path':str(p), 'sha256':sha(p),'run_records':[str(x) for x in p.parent.glob('run_??.json')]})
checks['only_one_exact_png_invocation_in_existing_runtime_bindings']=len(matching)==1
checks['exactly_two_run_records_and_two_started_and_two_raw']=all(len(list(TEST.glob(g)))==2 for g in ['run_??.json','run_??_started.json','run_??_response.json'])
checks['no_incomplete_or_error_files']=not list(TEST.glob('*.bin')) and all(all(r['checks'].values()) for r in runs)
checks['sequential_nonoverlap']=runs[0]['finished_at']<runs[1]['started_at']
historic=read(CAND/'eligibility_before_calls.json')['frozen_source_files']
source_hash_checks={rel:{'expected':old,'current':sha(ROOT/rel),'matches':old==sha(ROOT/rel)} for rel,old in historic.items()}
audit={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'isolation':ISOLATION,
    'checks':checks,'binding':binding,'request_without_image':{**request,'messages':[request['messages'][0],{'role':'user','content':[request['messages'][1]['content'][0],{'type':'image_url','png_bytes':len(payload_png),'png_sha256':hashlib.sha256(payload_png).hexdigest()}]}]},
    'exact_files':{name:snap(CAND/name) for name in ['candidate.png','plugin.json','design.json','fresh_context.json','path_fingerprints.json','primary_review.json']},
    'raw_test_files':{p.name:snap(p) for p in TEST.iterdir() if p.is_file()},
    'runs':runs,'matching_exact_png_bindings':matching,'frozen_source_hash_checks':source_hash_checks,
    'formal_record':record, 'eligibility':eligibility}
write('evidence_audit.json',audit)
scene=read(BRANCH/record['scene'])
print(json.dumps({'checks':checks,'eligibility':{k:eligibility[k] for k in ['eligible','current_content_sha256','accepted_entries','collected_entries','formal_special_directory_exists']},
    'frozen_sources_all_match':all(x['matches'] for x in source_hash_checks.values()),
    'source_json':read(BRANCH/'dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane192/source.json'),
    'formal_scene_non_grid':{**scene,'objects':[o for o in scene['objects'] if not o['id'].startswith('grid')]},
    'context_keys':list(read(CAND/'fresh_context.json')),'prior_report_existence':{str(p):p.exists() for p in prior_reports}},ensure_ascii=False,indent=2))
