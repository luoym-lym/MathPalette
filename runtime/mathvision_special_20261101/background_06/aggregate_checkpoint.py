from pathlib import Path
import os,sys,json,hashlib,base64,io
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for key,name in {'TEMP':'aggregate_tmp','TMP':'aggregate_tmp','MPLCONFIGDIR':'aggregate_mpl','XDG_CACHE_HOME':'aggregate_cache'}.items():
    target=HERE/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.dont_write_bytecode=True;sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(HERE/'aggregate_render_tmp')
from PIL import Image
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def write(p,v):
    with Path(p).open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
workers={n:read(HERE/n/'checkpoint.json') for n in ['solid_worker','plane_fold','plane_parts']}
assignment=read(BASE/'background_06_assignment.json')['question_ids']
assessed=[q for d in workers.values() for q in d['assessed_question_ids']]
assert len(assessed)==len(set(assessed))==20 and set(assessed)==set(assignment)
queues=[c for n in workers for c in read(HERE/n/'second_review_queue.json')['candidates']]
assert {c['question_id'] for c in queues}=={'Solid142','Plane233'}
records=workers['solid_worker']['designs']+workers['plane_fold']['entries']+workers['plane_parts']['candidate_records']
assert len(records)==16
audits=[];complete_calls=0;aborted_calls=0;control_calls=0;seen=set();paircount=0
for binding_path in sorted(HERE.rglob('binding.json')):
    b=read(binding_path);folder=binding_path.parents[2];inv=binding_path.parent
    image_path=Path(b['image_path']);design_path=Path(b['design_path'])
    assert sha(image_path)==b['image_sha256'] and sha(design_path)==b['design_sha256']
    assert (inv/'design_snapshot.json').read_bytes()==design_path.read_bytes()
    assert sha(inv/'request.json')==b['request_body_sha256']
    request=read(inv/'request.json');d=read(design_path)
    assert set(request)=={'model','stream','thinking','messages'} and request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert len(request['messages'])==2 and request['messages'][0]['role']=='system' and request['messages'][1]['role']=='user'
    content=request['messages'][1]['content'];assert len(content)==2 and set(content[0])=={'type','text'} and content[0]['type']=='text'
    rows=[json.loads(s) for s in (ROOT/b['branch']/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    row=next(r for r in rows if r['id']==b['question_id'])
    assert content[0]['text']==row['question'] and canonical(row)==b['question_record_sha256']
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==image_path.read_bytes()
    assert d.get('expected_wrong_answer',d.get('predicted_wrong_answer'))==b['expected_wrong_answer']
    assert str(b['expected_wrong_answer'])!=str(row['answer'])
    rgba=Image.open(io.BytesIO(image_path.read_bytes())).convert('RGBA')
    assert rgba.size==(768,768) and rgba.getextrema()[3]==(255,255)
    assert hashlib.sha256(b'768x768:RGBA:'+rgba.tobytes()).hexdigest()==b['pixel_sha256']
    key=(b['question_id'],b['image_sha256'],str(b['expected_wrong_answer']));assert key not in seen;seen.add(key)
    jobs=[]
    for p in sorted(inv.glob('run_??.json')):
        r=read(p);assert r['status']=='completed' and not r.get('truncated')
        assert r['image_sha256']==b['image_sha256'] and r['design_sha256']==b['design_sha256'] and r['request_body_sha256']==b['request_body_sha256']
        response_path=inv/f"run_{r['run_index']:02d}_response.json"
        assert sha(response_path)==r['response_sha256']
        raw=read(response_path);assert raw['choices'][0]['message']['content']==r['answer']
        jobs.append(r)
    is_control=folder.name in ['original_control','original_controls']
    if len(jobs)==2:
        if is_control:control_calls+=2
        else:paircount+=1;complete_calls+=2
        status='two_complete_original_controls' if is_control else 'two_complete_candidate_calls'
    else:
        assert len(jobs)==0 and (folder/'aborted_process_evidence.json').is_file()
        assert (inv/'run_01_started.json').is_file() and not (inv/'run_02_started.json').exists()
        aborted_calls+=1;status='aborted_first_call_no_completed_result_no_retry'
    audits.append({'question_id':b['question_id'],'variant_id':folder.name,'raw_binding_path':str(binding_path),'image_sha256':b['image_sha256'],'design_sha256':b['design_sha256'],'request_body_sha256':b['request_body_sha256'],'expected_wrong_answer':b['expected_wrong_answer'],'status':status,'completed_calls':len(jobs),'exact_bytes_and_formal_only_solver_input_verified':True})
assert paircount==15 and complete_calls==30 and control_calls==4 and aborted_calls==1
write(HERE/'evidence_binding_audit.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'invocation_count':len(audits),'candidate_complete_pairs':paircount,'candidate_completed_calls':complete_calls,'original_control_completed_calls':control_calls,'aborted_first_calls':aborted_calls,'duplicate_unchanged_question_image_preset_invocations':0,'audits':audits,'auth_headers_stored':False,'no_additional_solver_calls_in_audit':True})
preservation=read(HERE/'source_preservation_final.json');assert preservation['no_formal_or_prior_delivery_changes']
processes=read(HERE/'no_live_processes.json');assert processes['matching_python_processes']==[]
write(HERE/'second_review_queue.json',{'unit':'background_06','created_at':datetime.now(timezone.utc).isoformat(),'candidate_count':2,'question_ids':['Solid142','Plane233'],'candidates':queues,'status':'TWO_POSSIBILITIES_PENDING_NEW_PARENT_INDEPENDENT_REVIEW','not_approved_or_delivered':True,'required_next_action':'Parent starts a NEW independent mathematical/visual/evidence review task for these exact frozen variants. Research authors must not act as their own independent reviewers.','hard_gates':['Unique unchanged mathematics and complete readable original givens.','Every marker has a concrete geometric input-feature/part/edge/transform role; no generic wrong-option salience, false explicit relation, hidden condition or changed target.','Frozen exact question+PNG and predeclared preset match both complete manually read final answers.','Schema/default normalization, no-op formalPNG equality, deterministic rendering and exact evidence hashes.'],'limits':['Solid142 candidateA/A, correctC, separate originalcontrolsC/C with flawed narratives.','Plane233 candidateB/B, correctA, separate originalcontrolsC/C are also wrong; narratives contain geometry/count errors.','Only two candidate calls and two original controls per possible candidate. No human performance study, statistical per-marker ablation or population success-rate claim.','Correct controls and identical model narratives are not additional hard gates; report observed outcomes honestly.'],'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'source_preservation_path':str(HERE/'source_preservation_final.json')})
write(HERE/'checkpoint.json',{'unit':'background_06','completed_at':datetime.now(timezone.utc).isoformat(),'stop_reason':'All20assigned questions assessed and the selected purposeful finite designs completed;2credible possibilities, below3stop threshold.','assigned_question_ids':assignment,'assessed_question_ids':assignment,'actual_assessed_question_count':20,'saved_design_count':16,'complete_paired_evidence_candidate_count':15,'completed_candidate_API_call_count':30,'original_control_completed_call_count':4,'all_completed_API_call_count':34,'aborted_first_call_count':1,'error_call_count':0,'all_started_API_call_count':35,'credible_twohit_possibility_count':2,'credible_question_ids':['Solid142','Plane233'],'independently_second_reviewed_in_this_unit':0,'delivered_or_approved_count':0,'designs':records,'prescreen_only_question_ids':['Plane194','Plane195','Plane204','Plane218','Plane227','Solid121','Solid130'],'prescreen_records_by_worker':{'solid_worker':workers['solid_worker']['prescreen_only'],'plane_fold':workers['plane_fold']['prescreens'],'plane_parts':workers['plane_parts']['prescreen_only_questions']},'untested_saved_candidates':[],'unworked_assignments':[],'worker_checkpoints':{n:{'path':str(HERE/n/'checkpoint.json'),'sha256':sha(HERE/n/'checkpoint.json')} for n in workers},'worker_source_and_evidence_audits':{'solid_worker':str(HERE/'solid_worker/source_and_evidence_audit.json'),'plane_fold':str(HERE/'plane_fold/source_preservation_audit.json'),'plane_parts':str(HERE/'plane_parts/source_and_evidence_audit.json')},'second_review_queue_path':str(HERE/'second_review_queue.json'),'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'source_preservation_final_path':str(HERE/'source_preservation_final.json'),'no_live_processes_path':str(HERE/'no_live_processes.json'),'all_local_API_and_renderer_processes_ended':True,'both_native_children_finished':True,'aborted_remote_processing_limit':'Verified ownPID26960was stopped after an unreturned first call; remote provider processing cannot be observed or guaranteed cancelled. No local request process remains; no second call or retry was made.','controls_and_limits':{'Solid142':{'candidate_finals':['A','A'],'correct':'C','original_control_finals':['C','C'],'limits':'Control narratives flawed; no per-marker causal or human study.'},'Plane233':{'candidate_finals':['B','B'],'correct':'A','original_control_finals':['C','C'],'limits':'Original controls also wrong; candidate and control narratives contain shape/count errors. Marked partial-placement hypothesis remains pending independent information/necessity and human-clarity review.'}},'next_recommendations':['Parent launches NEW independent review for Solid142 and Plane233 using exact frozen bytes, no research-author self-review.','Only independently recommended exact variants may enter a later immutable batch and byte-identical packaged replay verification.','Do not rerun any failed/aborted unchanged question+image+preset; do not alter delivered batches.','Parent may separately aggregate mutable progress metadata, preserving historical snapshots and keeping approvals/Special state untouched.'],'authorization_and_isolation':'All writes remain under fresh background_06 or permitted runtime helper/cache paths; no formal/workbench/.env/.runtime/.git changes, no Pass/Collect/review API.'})
print(json.dumps({'assessed':20,'designs':16,'complete_candidate_pairs':15,'completed_candidate_calls':30,'original_control_calls':4,'aborted_first_calls':1,'credible_possibilities':2,'checkpoint':str(HERE/'checkpoint.json'),'second_review_queue':str(HERE/'second_review_queue.json')}))
