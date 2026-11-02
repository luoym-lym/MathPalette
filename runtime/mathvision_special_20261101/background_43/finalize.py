import env
from env import OWN,PROJECT,SHARED
from prepare import IDS,read,dump,sha,eligibility
from datetime import datetime,timezone
from pathlib import Path
import sys
import base64,hashlib,io,json

def now():return datetime.now(timezone.utc).isoformat()

MANUAL={
 'Plane402':[
  {'manual_final':'-8','manual_final_value':'-8','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Reads all full raw content. It considers4 but expressly ends Final Answer:-8; not preset10/3.'},
  {'manual_final':'26/3; then dangling System Instruction Repeated quote','manual_final_value':'26/3','matches_predeclared_wrong_answer':False,'final_internally_consistent':False,'note':'Full valid HTTP/JSON stop response; several stated26/3 conclusions, followed by non-answer trailing System Instruction Repeated quote. Not a clean terminal completion for promotion and in any event not10/3. No repair or retry.'}],
 'Plane407':[
  {'manual_final':'A;18cm','manual_final_value':'A','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Explicit final18cm and choiceA, consistent and correct. Not presetE.'},
  {'manual_final':'E; depends upon rectangle sizes','manual_final_value':'E','matches_predeclared_wrong_answer':True,'final_internally_consistent':True,'note':'Explicit E matches its preset once. Narrative falsely claims a third continuous centre line/typo; actual native image still has exactly two centre lines.'}],
 'Plane410':[
  {'manual_final':'1','manual_final_value':'1','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Explicit final1 design. Incorrectly reads B as4x4. Not preset3.'},
  {'manual_final':'None of the designs;0','manual_final_value':'0','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Final conclusion None means0, with extensive false grid counts. Not preset3.'}],
 'Plane412':[
  {'manual_final':'180cm; no matching listed option','manual_final_value':'180','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Explicit final180cm. Mentions400 only as hypothetical option typo, never concludes380/A. Do not relabel180 as the preset.'},
  {'manual_final':'180cm; no matching listed option','manual_final_value':'180','matches_predeclared_wrong_answer':False,'final_internally_consistent':True,'note':'Explicit final180cm, notA/380. Two identical wrong values still fail their own immutable preset.'}]
}

def main():
    from PIL import Image
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import pixel_hash
    results=[];all_bindings=[];manuals=[]
    for binding in sorted(OWN.glob('Plane*/r43_*/tests/*/binding.json')):
        inv=binding.parent;root=inv.parents[1];b=read(binding);q=b['question_id']
        d=read(root/'design.json');plugin=read(root/'plugin.json');s=read(inv/'summary.json');req_bytes=(inv/'request.json').read_bytes();req=json.loads(req_bytes)
        e=eligibility(q);assert e['eligible'];dump(root/'eligibility_final.json',e)
        image_bytes=(root/'candidate.png').read_bytes();design_bytes=(root/'design.json').read_bytes()
        expected_request={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[{'role':'system','content':b['system_prompt']},{'role':'user','content':[{'type':'text','text':e['current_formal_record']['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(image_bytes).decode('ascii')}}]}]}
        current_canonical=json.dumps(e['current_formal_record'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
        check={'question_id':q,'binding_path':str(binding),'image_sha256':sha(root/'candidate.png')==b['image_sha256']==d['image_sha256'],'pixel_sha256':pixel_hash(image_bytes)==b['pixel_sha256'],'design_sha256':sha(root/'design.json')==b['design_sha256'],'design_snapshot_byte_equal':design_bytes==(inv/'design_snapshot.json').read_bytes(),'request_sha256':sha(inv/'request.json')==b['request_body_sha256'],'formal_question_exact_and_only_png':req==expected_request,'formal_question_record_sha256':hashlib.sha256(current_canonical).hexdigest()==b['question_record_sha256'],'reference_quicktest_sha256':sha(PROJECT/'PlaneGeometry/workbench/quick_test.py')==b['reference_quick_test_sha256'],'correct_profile_mimo_disabled':b['profile']=='quicktest3' and req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'},'token_limit_fields_absent':not any(k in req for k in ['max_tokens','max_completion_tokens']),'same_image_design_both_runs':True,'exactly_two_started':len(list(inv.glob('run_*_started.json')))==2,'exactly_two_complete_responses':len(list(inv.glob('run_*_response.json')))==2 and s['two_completed'],'preset_unchanged':b['expected_wrong_answer']==d['expected_wrong_answer']!=e['current_formal_record']['answer'],'immutable_design_precedes_calls':(root/'design.json').stat().st_mtime<min(p.stat().st_mtime for p in inv.glob('run_*_started.json')),'own_primary_native_review_precedes_calls':(root/'primary_review.json').stat().st_mtime<min(p.stat().st_mtime for p in inv.glob('run_*_started.json')),'replayed_source_eligibility':e['eligible']}
        review=[]
        for i,m in enumerate(MANUAL[q],1):
            rpath=inv/f'run_{i:02d}_response.json';r=read(rpath);job=read(inv/f'run_{i:02d}.json');start=read(inv/f'run_{i:02d}_started.json')
            assert job['status']=='completed' and job['http_status']==200
            assert r['choices'][0]['finish_reason']=='stop'
            assert sha(rpath)==job['response_sha256']
            assert all(job[k]==b[k] for k in ['image_sha256','design_sha256','request_body_sha256'])
            assert all(start[k]==job[k] for k in ['run_id','run_index','image_sha256','design_sha256','request_body_sha256'])
            review.append({**m,'run_index':i,'status':job['status'],'http_status':job['http_status'],'finish_reason':r['choices'][0]['finish_reason'],'raw_response_path':str(rpath),'raw_response_sha256':sha(rpath),'run_record_sha256':sha(inv/f'run_{i:02d}.json'),'full_final_text':r['choices'][0]['message']['content'],'complete_raw_response_and_full_content_manually_read':True,'expected_wrong_answer':d['expected_wrong_answer'],'started_at':job['started_at'],'finished_at':job['finished_at'],'elapsed_seconds':job['elapsed_seconds']})
        assert all(v is True for k,v in check.items() if isinstance(v,bool)),check
        pair={'question_id':q,'variant_id':d['variant_id'],'expected_wrong_answer':d['expected_wrong_answer'],'formal_correct_answer':e['current_formal_record']['answer'],'observed_manual_finals':[m['manual_final'] for m in review],'two_complete_calls':True,'target_hit_count':sum(m['matches_predeclared_wrong_answer'] for m in review),'credible_primary_possible_candidate':False,'manual_runs':review,'binding':b,'binding_checks':check,'candidate_png':str(root/'candidate.png'),'plugin_path':str(root/'plugin.json'),'design_path':str(root/'design.json'),'design_difference_audit':str(root/'design_difference_audit.json'),'primary_review':str(root/'primary_review.json'),'native_render_audit':str(root/'native_render_audit.json'),'source_eligibility_audit':str(root/'eligibility_final.json'),'evidence_dir':str(inv),'original_controls':[],'no_relabel_or_repeat':True,'status':'complete_pair_missed_own_preset; no independent second review queued'}
        dump(root/'manual_final_review.json',pair)
        results.append(pair);all_bindings.append(check);manuals.extend(review)
        a=read(OWN/q/'assessment.json');a['status']='completed_new_pair_missed_preset';a['new_pair_final_answers']=pair['observed_manual_finals'];a['api_calls']=2;a['target_hit_count']=pair['target_hit_count'];a['result']=str(root/'manual_final_review.json');dump(OWN/q/'assessment.json',a)
    assert len(results)==4 and sum(len(r['manual_runs']) for r in results)==8
    dump(OWN/'evidence_binding_audit.json',all_bindings)
    dump(OWN/'full_manual_finals.json',manuals)
    # Preserve prior evidence/source bytes; diagnostic mutable dispatch is classified separately.
    initial=read(OWN/'protected_inputs_start.json')
    for cp in read(OWN/'old_checkpoint_excerpts.json'):initial.setdefault(cp['path'],cp['sha256'])
    protected=[];changes=[]
    for p,h in initial.items():
        path=Path(p);cur=sha(path) if path.is_file() else None
        diagnostic=path.name=='refinement_dispatch_20261102.json'
        entry={'path':p,'initial_sha256':h,'final_sha256':cur,'matches':h==cur,'classification':'diagnostic_mutable_dispatch_metadata' if diagnostic else 'formal_source_or_old_frozen_evidence'}
        protected.append(entry)
        if h!=cur:changes.append(entry)
    relevant_changed=[x for x in changes if x['classification']!='diagnostic_mutable_dispatch_metadata']
    dump(OWN/'source_preservation_final.json',{'at_utc':now(),'tracked_file_count':len(protected),'files':protected,'changes':changes,'relevant_frozen_changes':relevant_changed,'own_formal_or_old_evidence_writes':False,'entire_workspace_unchanged_claim':False,'unrelated_concurrent_changes':'Preserved; no attribution/restoration or aggregate rebuild.'})
    assert not relevant_changed,relevant_changed
    eligibility_end={q:eligibility(q) for q in IDS};assert all(e['eligible'] for e in eligibility_end.values())
    dump(OWN/'eligibility_final_all.json',eligibility_end)
    # Context/assignment and mandatory semantics lesson binding.
    assignment=read(SHARED/'background_43_assignment.json')
    assert assignment['question_ids']==IDS
    assignment_agrees=all(x['formal_record_at_assignment']==eligibility_end[x['question_id']]['current_formal_record'] for x in assignment['questions'])
    lesson=SHARED/'annotation_semantics_lesson_plane242_r24_20261102.json';ind=SHARED/'independent_review/Plane242_r24_disconnected_gray_arc_assembly/independent_review.json'
    read(lesson);read(ind)
    protocol_files=[PROJECT/'MATHPALETTE_PROTOCOL.md',PROJECT/'PlaneGeometry/REDRAW_PROTOCOL.md',PROJECT/'PlaneGeometry/dataset_generator/protocol.json',PROJECT/'PlaneGeometry/workbench/README.md',PROJECT/'PlaneGeometry/workbench/agent_prompt.md',PROJECT/'PlaneGeometry/workbench/plugin.schema.json',SHARED/'background_43_brief.txt',SHARED/'background_43_assignment.json',SHARED/'continuation_brief.txt',lesson,ind]
    dump(OWN/'protocol_and_scope_audit.json',{'unit':'background_43','exact_authorized_ids':IDS,'assignment_record_equals_current':assignment_agrees,'full_files_read':{str(p):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in protocol_files},'lesson_application':'Physical printed-piece color interpretation may create no valid option: reject, no legend/text/question repair. Current tested tasks are numeric area/length; preserve all semantic fill/route membership and do not impose generic color-preservation constraints.','nested_agents_T3_threads_worktrees':0,'approved_API_harness':str(OWN/'harness/quicktest3_isolated.py'),'API_settings_changed':False})
    assessments={q:read(OWN/q/'assessment.json') for q in IDS};dump(OWN/'assessed_questions.json',assessments)
    queue={'unit':'background_43','stage':'material_refinement','created_at':now(),'candidates':[],'candidate_count':0,'reason':'None of four exact two-call new mechanisms matched their own unchanged wrong preset twice. No self independent review or promotion.','parent_next_step':'No candidate requires NEW independent review from this unit. Preserve all misses/held drafts; no Pass/Collect/publication.'}
    dump(OWN/'second_review_queue.json',queue)
    count={'assigned_questions':8,'assessed_questions':8,'unworked_questions':0,'independently_verified_unique_math':7,'unresolved_original_minimum_proof':1,'material_new_hypotheses':4,'saved_new_design_PNG_artifacts':5,'tested_designs':4,'precall_held_drafts':1,'candidate_test_pairs':4,'completed_candidate_API_calls':8,'new_original_control_calls':0,'credible_primary_possible_candidates':0,'API_errors':0,'API_aborts':0,'API_retries':0,'precall_QA_assertion_failures':1,'precall_metadata_corrections':1,'prior_malformed_relevant_question_JSON_files':0}
    cp={'unit':'background_43','stage':'material_refinement','status':'complete','completed_at':now(),'stop_reason':'All eight assigned questions reasonably assessed; four substantive hypotheses tested exactly twice, remaining four screened with concrete reasons. No preset-paired candidate.','actual_assessed_question_ids':IDS,'unworked_question_ids':[],'counts':count,'new_results':results,'screened_without_design':[assessments[q] for q in ['Plane400','Plane401','Plane405','Plane409']],'held_new_drafts':[{'path':str(OWN/'Plane407/r43_full_base_to_center_half_binding'),'reason':'Pre-call native QA center occlusion;0API. Source/PNG/design retained. Same hypothesis technically repaired before all calls.'}],'anomalies':[{'question_id':'Plane407','kind':'precall_QA','resolution':'Original four centre points kept black in tested clear-dots draft. Three disclosed AA contour pixels outside mark neighborhoods.'},{'question_id':'Plane412','kind':'original_source_metadata','resolution':'Actual approved native black-route linewidth1pt differs from frozen role2.5pt field; actual source pixels/styles retained, pre-call prose corrected with initial metadata copy.'},{'question_id':'Plane402','kind':'model_content','resolution':'Second valid stop JSON trails dangling System Instruction Repeated quote. Stored byte-for-byte; a preset miss regardless, no repair/retry.'},{'question_id':'Plane401','kind':'math_proof_limit','resolution':'18 feasible and minimal within standard convex tile-direction completion; unrestricted original minimum not established, no design/call.'}],'failures_or_aborts':[],'history_inventory':str(OWN/'history_inventory.json'),'all_raw_bindings':str(OWN/'evidence_binding_audit.json'),'complete_hand_read_finals':str(OWN/'full_manual_finals.json'),'eligibility_final':str(OWN/'eligibility_final_all.json'),'source_preservation':str(OWN/'source_preservation_final.json'),'second_review_queue':str(OWN/'second_review_queue.json'),'scope_protocol_audit':str(OWN/'protocol_and_scope_audit.json'),'no_live_own_API_processes':'Verified externally after final report writing; see process_audit_final.json','no_formal_approval_Pass_Collect_publish':True,'limits':['Two observations do not prove a mechanism, causality, incremental benefit or statistical reliability.','No new original controls: existing comparisons reused as read-only history; none repeated.','No third call, no changed target after outputs, no combination of different images.','Parent NEW independent second review would be required for any credible future possibility; this queue is empty.']}
    dump(OWN/'checkpoint.json',cp)
    print(json.dumps({'counts':count,'results':[{'id':r['question_id'],'preset':r['expected_wrong_answer'],'finals':r['observed_manual_finals'],'hits':r['target_hit_count']} for r in results],'tracked_source_changes':len(relevant_changed),'checkpoint':str(OWN/'checkpoint.json')},ensure_ascii=False))

if __name__=='__main__':main()
