from pathlib import Path
import os,sys,json,hashlib,base64,io
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for k,n in {'TEMP':'aggregate_tmp','TMP':'aggregate_tmp','MPLCONFIGDIR':'aggregate_mpl','XDG_CACHE_HOME':'aggregate_cache'}.items():
    p=HERE/n;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
sys.dont_write_bytecode=True;sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(HERE/'aggregate_render_tmp')
from PIL import Image
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def write(p,v):
    with Path(p).open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
names=['plane_transform','plane_worker','solid_worker']
workers={n:read(HERE/n/'checkpoint.json') for n in names}
assignment=read(BASE/'background_07_assignment.json')['question_ids']
assessed=[q for w in workers.values() for q in w['assessed_question_ids']]
assert len(assessed)==len(set(assessed)) and set(assessed)<=set(assignment)
queues=[c for n in names for c in read(HERE/n/'second_review_queue.json')['candidates']]
assert len(queues)<=3 and len({c['question_id'] for c in queues})==len(queues)
records=[]
for n,w in workers.items():
    entries=w.get('designs',w.get('candidate_records',w.get('entries',[])))
    records+=entries
audits=[];seen=set();paircount=0;complete_calls=0;errors=0;aborts=0
prior=[]
for p in BASE.rglob('binding.json'):
    if not p.is_relative_to(HERE):
        b=read(p);prior.append((b.get('question_id'),b.get('image_sha256'),str(b.get('expected_wrong_answer'))))
for bp in sorted(HERE.rglob('binding.json')):
    b=read(bp);inv=bp.parent;imagepath=Path(b['image_path']);designpath=Path(b['design_path']);folder=designpath.parent
    assert imagepath.resolve().is_relative_to(HERE) and designpath.resolve().is_relative_to(HERE)
    assert sha(imagepath)==b['image_sha256'] and sha(designpath)==b['design_sha256']
    assert (inv/'design_snapshot.json').read_bytes()==designpath.read_bytes()
    assert sha(inv/'request.json')==b['request_body_sha256']
    d=read(designpath);assert d.get('expected_wrong_answer',d.get('predicted_wrong_answer'))==b['expected_wrong_answer']
    request=read(inv/'request.json')
    assert set(request)=={'model','stream','thinking','messages'} and request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert len(request['messages'])==2 and request['messages'][0]['role']=='system' and request['messages'][1]['role']=='user'
    from importlib.util import spec_from_file_location,module_from_spec
    sys.path.insert(0,str(ROOT/b['branch']/'workbench'))
    spec=spec_from_file_location('_unit07_reference_'+b['branch'],ROOT/b['branch']/'workbench/quick_test.py');ref=module_from_spec(spec);spec.loader.exec_module(ref)
    assert request['messages'][0]['content']==ref.SYSTEM_PROMPT
    assert b['settings']['model']==ref.TEST_PROFILES['quicktest3']['model'] and b['settings']['thinking']==ref.TEST_PROFILES['quicktest3']['thinking']
    assert {k:v for k,v in b['settings'].items() if k!='api_base'}==ref.TEST_PROFILES['quicktest3']
    assert sha(ROOT/b['branch']/'workbench/quick_test.py')==b['reference_quick_test_sha256']
    contents=request['messages'][1]['content'];assert len(contents)==2 and set(contents[0])=={'type','text'} and contents[0]['type']=='text'
    rows=[json.loads(s) for s in (ROOT/b['branch']/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    row=next(r for r in rows if r['id']==b['question_id']);assert row['source_dataset']=='MathVision'
    assert sha(ROOT/b['branch']/'dataset.jsonl')==b['dataset_sha256']
    assert contents[0]['text']==row['question'] and canon(row)==b['question_record_sha256']
    assert str(b['expected_wrong_answer'])!=str(row['answer'])
    assert base64.b64decode(contents[1]['image_url']['url'].split(',',1)[1])==imagepath.read_bytes()
    rgba=Image.open(io.BytesIO(imagepath.read_bytes())).convert('RGBA');assert rgba.size==(768,768) and rgba.getextrema()[3]==(255,255)
    assert hashlib.sha256(b'768x768:RGBA:'+rgba.tobytes()).hexdigest()==b['pixel_sha256']
    key=(b['question_id'],b['image_sha256'],str(b['expected_wrong_answer']));assert key not in seen and key not in prior;seen.add(key)
    jobs=[]
    for p in sorted(inv.glob('run_??.json')):
        r=read(p)
        if r['status']=='completed':
            assert not r.get('truncated') and r['finish_reason']=='stop'
            assert r['image_sha256']==b['image_sha256'] and r['design_sha256']==b['design_sha256'] and r['request_body_sha256']==b['request_body_sha256']
            rp=inv/f"run_{r['run_index']:02d}_response.json";assert sha(rp)==r['response_sha256']
            assert read(rp)['choices'][0]['message']['content']==r['answer'];complete_calls+=1
        else:errors+=1
        jobs.append(r)
    started=list(inv.glob('run_??_started.json'))
    if len(jobs)==2 and all(r['status']=='completed' for r in jobs):paircount+=1;status='TWO_COMPLETE_CALLS'
    elif len(jobs)<len(started):aborts+=len(started)-len(jobs);status='ABORTED_INCOMPLETE'
    else:status='ERROR'
    manual=read(folder/'manual_final_review.json')
    finals=manual.get('manual_final_answers',manual.get('manual_full_final_answers',manual.get('run_final_answers',manual.get('finals'))))
    if finals is None and 'actual_manual_finals' in manual:finals=[f['choice'] for f in manual['actual_manual_finals']]
    assert isinstance(finals,list) and len(finals)==len(jobs)
    audits.append({'question_id':b['question_id'],'variant_id':folder.name,'raw_binding_path':str(bp),'binding_sha256':sha(bp),'image_sha256':b['image_sha256'],'design_sha256':b['design_sha256'],'request_body_sha256':b['request_body_sha256'],'expected_wrong_answer':b['expected_wrong_answer'],'status':status,'completed_calls':sum(r['status']=='completed' for r in jobs),'exact_bytes_formal_question_only_solver_inputs_verified':True,'manual_final_review_path':str(folder/'manual_final_review.json'),'manual_final_answers':finals,'no_duplicate_prior_or_current_invocation':True,'raw_run_paths':[str(inv/f'run_{i:02d}.json') for i in range(1,len(jobs)+1)]})
write(HERE/'evidence_binding_audit.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'invocation_count':len(audits),'candidate_complete_pairs':paircount,'completed_candidate_API_calls':complete_calls,'errors':errors,'aborts':aborts,'duplicate_unchanged_candidate_invocations':0,'auth_headers_stored':False,'no_additional_solver_calls_in_audit':True,'audits':audits})
preserve=read(HERE/'source_preservation_classification_final.json')
assert preserve['task_frozen_sources_unchanged'] and preserve['prior_runtime_evidence_unchanged'] and preserve['all_assigned_currently_eligible'] and not preserve['unclassified_drift']
procs=read(HERE/'no_live_processes.json');assert procs['matching_python_processes']==[]
for n in names:assert read(HERE/n/'no_live_processes.json')['matching_python_processes']==[] if n=='plane_transform' else True
write(HERE/'second_review_queue.json',{'unit':'background_07','created_at':datetime.now(timezone.utc).isoformat(),'candidate_count':len(queues),'question_ids':[c['question_id'] for c in queues],'candidates':queues,'status':'PENDING_NEW_PARENT_INDEPENDENT_REVIEW','not_approved_or_delivered':True,'required_next_action':'Parent must create a NEW independent mathematical, human-semantics, visual and raw-evidence review task before delivery. Primary authors must not self-approve. Any later publication additionally requires exact packaged replay.','review_focus':['Unique original mathematics and every original visual distinction remain readable.','Each mark is tied to an actual geometric feature/correspondence; no arbitrary wrong-option highlighting.','Check human semantics, especially whether apparent cutting boundaries become incompatible fixed partitions as in rejectedPlane233.','Verify both complete manually read final answers against the immutable preset and same frozenPNG.','Model narratives have errors and color-as-given assumptions; those are observations, not geometry proofs.'],'limits':['Two candidate calls per exactimage; no statistical causal attribution or human-performance claim.','No original controls performed in this unit unless explicitly listed in worker evidence.','No Pass,Collect,review API or publication performed.'],'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'source_preservation_path':str(HERE/'source_preservation_classification_final.json'),'concurrent_workbench_drift_preserved':preserve['observed_concurrent_unrelated_workbench_drift']})
prescreens={n:workers[n].get('prescreen_only_question_ids',workers[n].get('prescreen_only',workers[n].get('prescreens',workers[n].get('prescreen_only_questions',workers[n].get('prescreen_questions',[]))))) for n in names}
untested={n:workers[n].get('untested_saved_candidates',workers[n].get('failures_and_aborts',{}).get('untested_visual_rejections',[])) for n in names}
write(HERE/'checkpoint.json',{'unit':'background_07','completed_at':datetime.now(timezone.utc).isoformat(),'stop_reason':'Three credible new paired-hit possibilities reached.' if len(queues)==3 else 'Assigned20questions exhausted; selected finite purposeful designs complete.','assigned_question_ids':assignment,'assessed_question_ids':assessed,'actual_assessed_question_count':len(assessed),'unworked_assignments':sorted(set(assignment)-set(assessed)),'saved_design_count':len(records),'complete_paired_evidence_candidate_count':paircount,'completed_candidate_API_call_count':complete_calls,'original_control_completed_call_count':0,'all_completed_API_call_count':complete_calls,'error_call_count':errors,'aborted_call_count':aborts,'credible_twohit_possibility_count':len(queues),'credible_question_ids':[c['question_id'] for c in queues],'independent_second_review_count':0,'delivered_or_approved_count':0,'designs':records,'prescreens_by_worker':prescreens,'untested_saved_candidates_by_worker':untested,'assessment_only_no_candidate_question_ids':workers['plane_transform'].get('assessment_only_no_candidate_question_ids',[]),'worker_checkpoints':{n:{'path':str(HERE/n/'checkpoint.json'),'sha256':sha(HERE/n/'checkpoint.json')} for n in names},'worker_source_and_evidence_audits':{n:str(HERE/n/'source_and_evidence_audit.json') for n in names},'second_review_queue_path':str(HERE/'second_review_queue.json'),'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'source_preservation_final_path':str(HERE/'source_preservation_classification_final.json'),'original_full_workspace_observation_path':str(HERE/'source_preservation_final.json'),'concurrent_workbench_drift_preserved':preserve['observed_concurrent_unrelated_workbench_drift'],'no_live_processes_path':str(HERE/'no_live_processes.json'),'all_local_API_processes_ended':True,'both_native_children_finished':True,'no_retries_or_fishing':True,'next_recommendations':['Parent creates NEW independent secondreview for exact queued variants.','No primary author may self-approve or publish.','All failed or abandoned unchangedimages remain evidence and must not be retested.','Progress aggregation, if desired, belongs to parent; existing aggregate metadata was not rewritten.'],'authorization_and_isolation':'Only background_07files created/updated; all formal/workbench/approvals/.env/.runtime/.git/prior evidence/published batches preserved. Write guard and runtime caches selected before project imports.'})
print(json.dumps({'assessed':len(assessed),'saved_designs':len(records),'pairs':paircount,'calls':complete_calls,'credible':len(queues),'errors':errors,'aborts':aborts,'checkpoint':str(HERE/'checkpoint.json'),'queue':str(HERE/'second_review_queue.json')}))


