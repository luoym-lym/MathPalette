from env50 import *
from inspect50 import IDS,BRANCH,eligibility
from prepare50 import DEFS,PROOFS
from dataset_tools.catalog import read,digest
from datetime import datetime,timezone
import base64,importlib.util
manual={
'Plane176':{'finals':['2','2'],'narrative_notes':['Run1 miscounts original gray11 and perimeter28; explicitly treats only two marked notches as intended count. Final2 is not preset7.','Run2 counts original9/perimeter20 but only enumerates the two marked locations; terminal2. Trailing System Instruction string is preserved verbatim, not treated as a new request or parsefailure.']},
'Plane180':{'finals':['D','E'],'values':[110,100],'narrative_notes':['Run1 assumes two undocumented right-angle turns, gives110 and D. This is only one target hit; no new right-angle condition exists in the candidate.','Run2 uses inconsistent80/100 angle story, but terminal E corresponds100, no contradictory terminal letter/value. It misses presetD.']},
'Plane181':{'finals':['C','C'],'values':[32,32],'narrative_notes':['Run1 independently obtains exact crease, Dprime32/17,128/17 and triangle areas17+15=32; correctC.','Run2 uses vertically reversed coordinates consistently and calculates17+15=32; notation MDprimeC erroneously names original triangle MDC, but finalC32 is clear.']},
'Plane183':{'finals':['2.5','10'],'narrative_notes':['Run1 correctly finds hole144 but incorrectly calls it exterior turn and divides360/144, terminal2.5; not preset5.','Run2 meanders through fabricated usual options and incorrectly says full outer boundary has10edges; actual completed ring outer boundary has2edges per plate,20edges. Its final inner-hole calculation144=180-360/n and answer10 are correct. No option list was sent for this number question.']}
}
skip_reasons={q:PROOFS[q].get('skip',PROOFS[q].get('finding')) for q in IDS if q not in DEFS}
def now():return datetime.now(timezone.utc).isoformat()
def main():
    sys.path.insert(0,str(BRANCH/'workbench'))
    spec=importlib.util.spec_from_file_location('reference50',BRANCH/'workbench/quick_test.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    cases=[];bindings=[];queue=[]
    for q in IDS:
        e=eligibility(q);dump(OWN/q/'eligibility_end.json',e);assert e['eligible']
        if q not in DEFS:
            a={'question_id':q,'status':'SKIP_NO_CLEAN_NEW_CANDIDATE','reason':skip_reasons[q],'formal_answer_unchanged':e['record']['answer'],'primary_math':PROOFS[q],'API_calls':0,'candidate_designs':0,'actual_source_JPG_and_formal_PNG_and_old_PNGs_viewed':True,'exact_context_path':str(OWN/q/'context.json'),'eligibility_end':str(OWN/q/'eligibility_end.json'),'old_history_audit':str(OWN/'history_read_audit.json'),'not_a_global_impossibility_claim':True}
            dump(OWN/q/'assessment.json',a);cases.append(a);continue
        variant,preset,_,_=DEFS[q];d=OWN/q/variant
        summaries=list((d/'tests').glob('quicktest3_*/summary.json'));assert len(summaries)==1
        td=summaries[0].parent;s=read(summaries[0]);b=read(td/'binding.json');frozen=read(d/'frozen_before_API.json')
        assert s['two_completed'] and len(s['results'])==2 and b['requested_runs']==2
        assert not [n for n,h in frozen['hashes'].items() if sha(d/n)!=h]
        assert sha(d/'candidate.png')==b['image_sha256'] and sha(d/'design.json')==b['design_sha256']==sha(td/'design_snapshot.json')
        assert read(td/'design_snapshot.json')['expected_wrong_answer']==preset==b['expected_wrong_answer']
        payload=read(td/'request.json');assert set(payload)=={'model','stream','thinking','messages'}
        assert payload['model']==mod.TEST_PROFILES['quicktest3']['model']=='mimo-v2.6-flash' and payload['thinking']==mod.TEST_PROFILES['quicktest3']['thinking']=={'type':'disabled'}
        assert payload['stream'] is False and len(payload['messages'])==2 and payload['messages'][0]=={'role':'system','content':mod.SYSTEM_PROMPT}
        expected_user={'role':'user','content':[{'type':'text','text':e['record']['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((d/'candidate.png').read_bytes()).decode('ascii')}}]}
        assert payload['messages'][1]==expected_user
        assert sha(td/'request.json')==b['request_body_sha256'] and digest(e['record'])==b['question_record_sha256']
        finals=[]
        for k,answer in enumerate(manual[q]['finals'],1):
            rr=td/f'run_{k:02d}_response.json';raw=read(rr);job=read(td/f'run_{k:02d}.json');start=read(td/f'run_{k:02d}_started.json')
            assert raw['choices'][0]['finish_reason']=='stop' and job['status']=='completed' and sha(rr)==job['response_sha256']
            assert start['image_sha256']==b['image_sha256'] and start['design_sha256']==b['design_sha256'] and start['request_body_sha256']==b['request_body_sha256']
            finals.append({'run_index':k,'full_final_text':raw['choices'][0]['message']['content'],'full_raw_response_manually_read':True,'terminal_answer':answer,'terminal_value':manual[q].get('values',[None,None])[k-1],'matches_original_frozen_wrong_preset':answer==preset,'contradictory_terminal_letter_value':False,'narrative_notes':manual[q]['narrative_notes'][k-1],'raw_response_path':str(rr),'raw_response_sha256':sha(rr),'job_path':str(td/f'run_{k:02d}.json'),'finish_reason':'stop'})
        twohit=all(f['matches_original_frozen_wrong_preset'] for f in finals)
        manual_review={'question_id':q,'variant_id':variant,'reviewed_at':now(),'expected_wrong_answer_immutable':preset,'formal_correct_answer':e['record']['answer'],'full_manual_final_reviews':finals,'hits':sum(f['matches_original_frozen_wrong_preset'] for f in finals),'two_hit':twohit,'outcome':'PRIMARY_POSSIBLE_NEEDS_NEW_INDEPENDENT_REVIEW' if twohit else 'MISS','same_wrong_final_does_not_override_preset':True,'no_posthoc_relabel_or_retests':True,'actual_narratives_do_not_establish_causal_mechanism':True,'original_controls':'None located for these8originals; none newly called. No causal/statistical gain claim.'}
        dump(d/'manual_final_review.json',manual_review)
        binding={'question_id':q,'variant_id':variant,'formal_question_exact':True,'mimo_quicktest3_profile_exact':True,'system_prompt_exact':True,'no_correct_answer_preset_intent_history_or_plugin_in_solver_input':True,'same_frozen_PNG_for_exact_two_runs':True,'complete_raw_responses':True,'all_pre_API_frozen_hashes_unchanged':True,'design_snapshot_exact':True,'request_sha256':sha(td/'request.json'),'image_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),'plugin_sha256':sha(d/'plugin.json'),'raw_responses':[f['raw_response_sha256'] for f in finals],'evidence_directory':str(td),'manual_review_path':str(d/'manual_final_review.json')}
        dump(d/'evidence_binding_audit.json',binding);bindings.append(binding)
        a={'question_id':q,'variant_id':variant,'status':manual_review['outcome'],'candidate_designs':1,'API_calls':2,'expected_wrong_answer':preset,'actual_terminal_answers':manual[q]['finals'],'hits':manual_review['hits'],'candidate_directory':str(d),'difference_audit':str(d/'design_difference_audit.json'),'source_precision_paths':str(d/'path_fingerprints.json'),'primary_math_path':str(OWN/q/'math_proof.json'),'native_primary_review':str(d/'primary_native_review.json'),'binding_audit':str(d/'evidence_binding_audit.json'),'manual_review':str(d/'manual_final_review.json'),'eligibility_end':str(OWN/q/'eligibility_end.json'),'limitation':'Pair outcome alone does not prove mechanism, incremental effect or human acceptance. No preset change or failed-image repeat.'}
        dump(OWN/q/'assessment.json',a);cases.append(a)
        if twohit:queue.append(a)
    historical=[]
    for p in ROOT.rglob('binding.json'):
        if p.is_relative_to(OWN):continue
        try:v=read(p)
        except Exception:continue
        if v.get('question_id') in IDS:historical.append({'path':str(p),'sha256':sha(p),'question_id':v['question_id']})
    dump(OWN/'old_solver_binding_search.json',{'searched_all_historical_binding_json':True,'found_for_assigned_ids':historical,'new_calls_not_added_to_old_history':True})
    assert not historical,historical
    before=read(OWN/'source_hashes_before.json');changes=[{'path':p,'before':h,'after':sha(p) if Path(p).exists() else None} for p,h in before.items() if not Path(p).exists() or sha(p)!=h]
    old_changes=[];old_count=0
    for q in IDS:
        for x in read(OWN/q/'old_file_manifest.json'):
            old_count+=1;p=Path(x['path'])
            if not p.exists() or sha(p)!=x['sha256']:old_changes.append({'path':str(p),'old_sha256':x['sha256'],'current_sha256':sha(p) if p.exists() else None})
    preservation={'finished_at':now(),'scoped_source_hash_count':len(before),'scoped_source_hash_changes':changes,'old_evidence_files_checked':old_count,'old_evidence_hash_changes':old_changes,'strict_own_directory_guard_installed_before_project_imports':True,'own_writes_only':str(OWN),'whole_workspace_unchanged_claim':False,'mutable_global_metadata_not_rewritten':True,'approvals_formal_env_git_dotruntime_old_helpers_and_global_ledger_not_written':True,'historical_metadata_correction':'Old Plane177 car/Plane237 prose is retained and separately corrected in old_native_image_review.json.'}
    dump(OWN/'source_preservation_final.json',preservation)
    assert not changes and not old_changes
    dump(OWN/'local_anomalies.json',{'external_API_errors':[],'API_aborts':[],'API_retries':0,'local_only_errors':[{'script':'check_math50.py','error':'SyntaxError expected else after if expression; missing whitespace in else2/else1/else4','effect':'Only supplemental mathematical calculation script failed before execution. Corrected own script and calculation checks subsequently passed. No API call, frozen design, PNG or old evidence modified.'}],'old_metadata_errors_retained':[{'question_id':'Plane177','location':'background_07/plane_transform/Plane177/source_primary_audit.json','issue':'Unrelated Plane237/car-color boilerplate. Actual source/board inspected and correct specific proof recorded separately.'}]})
    processes=[]
    for q,(v,*_) in DEFS.items():
        d=OWN/q/v;start=read(d/'api_process.json');end=read(d/'api_process_finished.json');assert start['pid']==end['pid'] and end['process_reaped'] and end['exit_code']==0
        processes.append({'pid':start['pid'],'exact_command':start['command'],'finished':end})
    dump(OWN/'process_closure.json',{'own_API_processes':processes,'all4child_processes_waited_and_reaped':True,'final_GetCimInstance_exact_ownroot_python_filter_result':[],'no_live_own_API_processes':True,'no_abort_or_termination_used':True,'no_servers_threads_nested_agents_or_worktrees_started':True})
    dump(OWN/'second_review_queue.json',{'unit':'background_50','stage':'material_refinement','created_at':now(),'candidates':queue,'candidate_count':len(queue),'parent_must_launch_NEW_independent_second_review_before_delivery':True,'no_self_independent_review_Pass_Collect_or_publication':True})
    checkpoint={'unit':'background_50','stage':'material_refinement','status':'COMPLETE_ASSIGNED8_REASONABLE_HYPOTHESES_EXHAUSTED','finished_at':now(),'assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'unworked_question_ids':[],'candidate_designs_created':4,'actual_API_calls':8,'complete_API_calls':8,'complete_exact_two_call_pairs':4,'possible_two_hit_candidates':len(queue),'external_errors':0,'aborts':0,'retries':0,'live_own_API_processes':0,'no_original_control_calls':True,'actual_results':cases,'evidence_bindings':bindings,'source_preservation':str(OWN/'source_preservation_final.json'),'history_read_audit':str(OWN/'history_read_audit.json'),'full_old_solver_binding_search':str(OWN/'old_solver_binding_search.json'),'independent_semantic_lessons_read':str(OWN/'independent_lessons_read.json'),'math_calculation_checks':str(OWN/'mathematical_calculation_checks.json'),'second_review_queue':str(OWN/'second_review_queue.json'),'process_closure':str(OWN/'process_closure.json'),'local_anomalies':str(OWN/'local_anomalies.json'),'limits':['Plane170 actual source/formal shows only a2x1stone; no square path arrangement or clean source/receiver. Conditional12 calculation was not presented as a demonstrated unique arrangement proof. Formal source unchanged.','Plane176 maximal-fill interpretation explicitly stated; smaller additions are possible if the question is read nonmaximally. Marks preserved all original fill classes.','No original controls found for these8and no new control calls made, so no causal/statistical effect estimate.','All4new designs miss their original preregistered presets; identical wrong2/2onPlane176 remainsMISS, and D/EonPlane180 is only one target hit.','Primary native/mathematical reviews are designer checks, not independent second reviews or user approvals. No candidate was delivered.'],'all_writes_below_own_root':str(OWN),'formal_approval_Pass_Collect_publish_actions':False}
    dump(OWN/'checkpoint.json',checkpoint)
    evidence=[]
    for p in OWN.rglob('*'):
        if p.is_file() and not any(part in ['tmp','cache','mpl_cache','render_tmp','__pycache__'] for part in p.relative_to(OWN).parts) and p.name!='evidence_manifest.json':evidence.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
    dump(OWN/'evidence_manifest.json',{'created_at':now(),'files':evidence,'scope':'Own research/proof/raw API evidence; disposable caches excluded.'})
    print(json.dumps({'assessed':len(cases),'designs':4,'calls':8,'two_hit_candidates':len(queue),'results':[{k:v for k,v in a.items() if k in ['question_id','status','expected_wrong_answer','actual_terminal_answers','hits']} for a in cases],'source_hashes_verified':len(before),'old_files_verified':old_count,'source_changes':changes,'old_changes':old_changes},ensure_ascii=False))
if __name__=='__main__':main()
