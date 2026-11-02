"""Low-memory final audit: stdlib and catalog only; no renderer/API imports."""
import os
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;PROJECT=HERE.parents[2]
sys.dont_write_bytecode=True
for key,name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    os.environ[key]=str(HERE/name)
def guard(event,args):
    def check(path):
        if path is None or isinstance(path,int):return
        if not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):raise PermissionError('Outside background57')
    if event=='open' and args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(guard)
import json
import hashlib
import base64
import re
from datetime import datetime,timezone
sys.path.insert(0,str(PROJECT))
from dataset_tools.catalog import content,digest
IDS=['Solid79','Solid214','Solid216','Solid225','Solid232','Solid233','Solid234','Solid247']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):return [json.loads(l) for l in Path(p).read_text(encoding='utf-8-sig').splitlines() if l.strip()] if Path(p).is_file() else []
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(65536):h.update(b)
    return h.hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():
        previous=read(p)
        if p.name=='eligibility_checkpoint.json':
            assert previous['current_content_sha256']==v['current_content_sha256'] and previous['eligible']==v['eligible']
            return
        assert previous==v,p
        return
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
branch=PROJECT/'SolidGeometry'
records={r['id']:r for r in rows(branch/'dataset.jsonl')}
notes={};active=None;parts=[]
with (PROJECT/'provenance/source_notes.json').open('r',encoding='utf-8-sig') as stream:
    for line in stream:
        match=re.match(r'^  "([^"\\]+)":',line)
        if match or line.strip()=='}' and line.startswith('}'):
            if active is not None:
                fragment=''.join(parts).rstrip().rstrip(',')
                notes.update(json.loads('{'+fragment+'}'))
            active=match.group(1) if match and match.group(1) in IDS else None
            parts=[]
        if active is not None:parts.append(line)
assert set(notes)==set(IDS)
approvals=read(PROJECT/'provenance/approvals.json')['approvals']
accepted=rows(branch/'special_variant/accepted_index.jsonl');collected=rows(branch/'special_variant/collected_index.jsonl')
elig={};source_changes=[]
for q in IDS:
    a=approvals[q];r=records[q];payload=content(PROJECT,'SolidGeometry',r,source_notes=notes)
    def belongs(x):return x.get('question_id',x.get('id'))==q
    ar=list(filter(belongs,accepted));cr=list(filter(belongs,collected));s=branch/'special_variant'/q
    files=[str(p) for p in s.rglob('*') if p.is_file()] if s.exists() else []
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(payload)==a['content_sha256']
    rootrow=next(x for x in rows(PROJECT/'question_bank.jsonl') if x['id']==q)
    eligible=valid and r['source_dataset']=='MathVision' and not ar and not cr and not files and not rootrow.get('special_plugins')
    assert eligible,q
    elig[q]=dict(checked_at=now(),MathVision=True,original_approval_current=valid,current_content_sha256=digest(payload),approval=a,accepted=ar,collected=cr,Special_files=files,eligible=eligible)
    write(HERE/q/'eligibility_checkpoint.json',elig[q])
    for p,h in read(HERE/q/'source_hashes_initial.json').items():
        actual=sha(PROJECT/p)
        if actual!=h:source_changes.append(dict(question_id=q,path=p,old=h,current=actual))
old=read(HERE/'old_evidence_inventory.json')['files'];old_changes=[]
for p,item in old.items():
    actual=sha(p)
    if actual!=item['sha256']:old_changes.append(dict(path=p,old=item['sha256'],current=actual))
assert not source_changes and not old_changes
write(HERE/'source_and_old_evidence_preservation_final.json',dict(checked_at=now(),source_changes=source_changes,old_evidence_changes=old_changes,old_files=len(old),source_hash_references=sum(len(read(HERE/q/'source_hashes_initial.json')) for q in IDS),all_current_eligible=True,own_writes_only=str(HERE),global_metadata_readonly=True,entire_workspace_unchanged_claim=False,unrelated_concurrent_changes_preserved=True))
# Validate each exact request/response/image/design binding and save full manual finals.
q='Solid79';spec=read(HERE/q/'spec_r57.json');d=HERE/q/spec['variant_id'];summaries=list((d/'tests').glob('*/summary.json'));assert len(summaries)==1
evidence=summaries[0].parent;summary=read(summaries[0]);binding=read(evidence/'binding.json');request=read(evidence/'request.json')
assert binding['image_sha256']==sha(d/'candidate.png') and binding['design_sha256']==sha(d/'design.json')
assert sha(evidence/'design_snapshot.json')==sha(d/'design.json')
assert summary['two_completed'] and len(summary['results'])==2
assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
u=request['messages'][1];assert u['role']=='user' and len(u['content'])==2
assert u['content'][0]=={'type':'text','text':records[q]['question']}
assert base64.b64decode(u['content'][1]['image_url']['url'].split(',',1)[1])==(d/'candidate.png').read_bytes()
assert not any(k in request for k in ['max_tokens','max_completion_tokens','timeout'])
manual=[]
for index in [1,2]:
    p=evidence/f'run_{index:02d}_response.json';raw=read(p);answer=raw['choices'][0]['message']['content']
    assert raw['choices'][0]['finish_reason']=='stop'
    assert re.search(r'(?:5 cubes were removed\.|\*\*Final Answer:\*\*\s*5)\s*$',answer),answer
    manual.append(dict(run_index=index,response_path=str(p),response_sha256=sha(p),full_final_manually_read=answer,final_answer='5',matches_unchanged_preset_11=False,finish_reason='stop',manual_reason='Both terminal answers explicitly5. Run1 invents fouruppercubes and13remaining; run2 uses12original and7remaining. Neither is11; incidental intermediate values cannot change grading.'))
write(d/'manual_full_final_review.json',dict(question_id=q,variant_id=spec['variant_id'],role='PRIMARY manual review only',expected_wrong_answer_frozen='11',formal_answer='7',full_final_answers_read=True,runs=manual,target_hits=0,two_target_hits=False,credible_candidate=False,history_or_preset_relabelled=False,no_new_control_calls=True))
binding_audit=dict(question_id=q,variant_id=spec['variant_id'],evidence_dir=str(evidence),design_path=str(d/'design.json'),design_sha256=sha(d/'design.json'),image_path=str(d/'candidate.png'),image_sha256=sha(d/'candidate.png'),plugin_sha256=sha(d/'plugin.json'),binding_sha256=sha(evidence/'binding.json'),request_sha256=sha(evidence/'request.json'),request_exact_question_and_candidate_only=True,model_profile_systemprompt_unchanged=True,both_actual_calls_completed=True,manual_finals=['5','5'],preset='11',hits=0)
write(d/'evidence_binding_audit.json',binding_audit)
# Local native-library startup failure, not a provider/API error and not two valid calls.
d234=HERE/'Solid234'/'r57_maximum_generator_to_cut_trace'
log=(d234/'api_stdout.log').read_text(encoding='utf-8',errors='strict')
assert 'OpenBLAS error: Memory allocation' in log
assert not list((d234/'tests').glob('**/binding.json')) and not list((d234/'tests').glob('**/request.json')) and not list((d234/'tests').glob('**/*started.json'))
finish=read(d234/'api_process_finished.json');assert finish['wait_reaped'] and finish['pid']==33376
local=dict(question_id='Solid234',variant_id='r57_maximum_generator_to_cut_trace',classification='local_startup_abort_before_API',pid=33376,returncode=finish['returncode'],complete_process_log=log,log_sha256=sha(d234/'api_stdout.log'),request_bindings=0,requests_started=0,actual_API_calls=0,valid_calls=0,not_graded=True,no_retry_of_frozen_image=True,no_process_killed_or_abandoned=True,old_generic_stop_file=str(HERE/'external_failure_stop.json'),qualification='Generic harness-no-summary stop filename is retained unchanged. Actual evidence identifies local OpenBLAS import/startup allocation failure, with no external API response/error. OpenBLAS allocator internal retry text is not API retry activity.')
write(d234/'local_startup_abort_review.json',local)
write(HERE/'offline_error_ledger_final.json',dict(previous=read(HERE/'offline_errors_initial.json'),additional=[dict(stage='rerun inspect after audit wrote source records',error='FileExistsError on own Solid216/formal_record.json',resolution='Preserved immutable existing record; inspect now compares exact value, reuses unchanged record and writes separate fresh eligibility.',API_calls=0),local],external_API_errors=0,API_retries=0,own_requests_abandoned=0))
write(HERE/'second_review_queue.json',dict(stage='material_refinement',unit='background_57',candidates=[],count=0,reason='Solid79 missed its immutable preset twice; Solid234 has zero actual calls after recorded local startup failure. No credible pair to submit. Parent must create a NEW independent review for any future credible candidate.'))
write(HERE/'checkpoint.json',dict(unit='background_57',stage='material_refinement',status='complete_finite_unit',finished_at=now(),stop_reason='All eight assigned questions assessed; local Solid234 startup abort preserved without retry.',assigned_question_ids=IDS,actual_assessed_question_ids=IDS,unworked_question_ids=[],question_outcomes={q:(dict(status='tested_pair_missed_preset',variant_id='r57_basal_footprint_retained_inventory',expected_wrong_answer='11',manual_finals=['5','5'],credible=False) if q=='Solid79' else dict(status='frozen_design_local_startup_abort_zero_API',variant_id='r57_maximum_generator_to_cut_trace',expected_wrong_answer='D',credible=False) if q=='Solid234' else read(HERE/q/'assessment.json')) for q in IDS},new_designs_frozen=2,complete_pairs=1,actual_completed_API_calls=2,actual_external_API_errors=0,local_harness_startup_aborts=1,API_request_aborts=0,API_retries=0,credible_candidate_pairs=0,all_current_eligible=elig,bindings=[binding_audit],untested_frozen_designs=[dict(question_id='Solid234',path=str(d234),reason='OpenBLAS allocation failure before any request; no retry.')],second_review_queue=str(HERE/'second_review_queue.json'),source_audit=str(HERE/'source_and_old_evidence_preservation_final.json'),old_evidence_manifest=str(HERE/'old_evidence_inventory.json'),primary_mathematical_native_reviews=[str(HERE/q/'primary_math_native_review.json') for q in IDS],processes=dict(all_own_API_children_waited_and_reaped=True,pids=[48164,33376],live_own_API_processes=0,external_PID_commandline_check='PowerShell CIM queried both exact PID33376 and allbackground57commands; no Python/API process remained. See own_process_inventory_final.json after final native snapshot.',termination_actions=0),authorization_actions=dict(formal_data_writes=False,approval_Pass_Collect=False,publication_delivery=False,independent_self_review=False,nested_agents_threads_worktrees_servers=False),limits=['No population or causal-gain claim. No original control repeated.','Six skips are concrete finite-unit design decisions, not impossibility claims.','Solid234 is not a two-hit candidate; do not silently rerun unchanged image.','No preset changed after responses; old failed or rejected evidence unchanged.']))
print('Checkpoint saved:8assessed;2frozen;1complete pair;2real calls;0credible;1localpre-APIstartupabort;noAPIretry.')
