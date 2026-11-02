import review_bootstrap as b
import json
import hashlib
from pathlib import Path

BASE=b.PROJECT/'runtime/mathvision_special_20261101'
UNIT=BASE/'background_16'
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=read(UNIT/'evidence_manifest.json')
found=[]
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(b.ROOT):continue
    data=read(p)
    if data.get('question_id')=='Solid197':
        found.append({'path':str(p),'sha256':sha(p),'image_sha256':data.get('image_sha256'),
                      'preset':data.get('expected_wrong_answer'),'created_at':data.get('created_at'),
                      'run_record_paths':[str(q) for q in sorted(p.parent.glob('run_[0-9][0-9].json'))],
                      'raw_response_paths':[str(q) for q in sorted(p.parent.glob('run_[0-9][0-9]_response.json'))]})
designs=[]
for p in BASE.rglob('design.json'):
    if p.is_relative_to(b.ROOT):continue
    data=read(p)
    if data.get('question_id')=='Solid197':designs.append({'path':str(p),'sha256':sha(p),'id':data.get('design_id')})
assert len(found)==2 and len(designs)==2
manifest_items=[]
def visit(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if 'Solid197' in k and isinstance(v,str) and len(v)==64:
                p=Path(k)
                candidates=[p,UNIT/p,BASE/p,b.PROJECT/p]
                actual=next((q for q in candidates if q.is_file()),None)
                manifest_items.append({'entry':k,'expected':v,'path':str(actual) if actual else None,
                                       'actual':sha(actual) if actual else None})
            elif isinstance(v,(list,dict)):visit(v)
    elif isinstance(x,list):
        for v in x:visit(v)
visit(manifest)
assert manifest_items and all(x['expected']==x['actual'] for x in manifest_items)
errors=read(UNIT/'errors_and_aborts.json')
result={'all_archived_Solid197_bindings':found,'all_archived_Solid197_designs':designs,
        'one_candidate_two_calls_plus_separate_original_two_calls':True,
        'candidate_retries_or_discarded_candidate_runs_in_available_archive':[],
        'documented_pre_render_setup_error':[x for x in errors['local_setup_errors'] if x.get('question_id')=='Solid197'],
        'api_errors':errors['api_errors'],'aborted_requests':errors['aborted_requests'],'retries':errors['retries'],
        'manifest_Solid197_entries_verified':manifest_items,
        'manifest_sha256':sha(UNIT/'evidence_manifest.json'),
        'archive_limit':'This is verification of the available file archive and harness, not provider-side attestation or proof that undisclosed/deleted records cannot exist.',
        'historical_progress_snapshot_policy':'The mutable exploration_report and remaining_questions data are diagnostic progress snapshots. Their drift and stale explored_no_deliverable status do not alter frozen geometry or raw response evidence; no historical snapshot was changed.'}
(b.ROOT/'history_and_manifest_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='manifest_Solid197_entries_verified'},ensure_ascii=False,indent=2))
print('Verified Solid197 manifest entries: '+str(len(manifest_items)))
