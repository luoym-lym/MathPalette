import task_env
from task_env import OWN
from prepare import read,write,hashfile
from datetime import datetime,timezone

ids=['Plane468','Plane469','Plane472','Plane473','Plane475','Plane476','Plane477','Plane479']
entries=[];queue=[]
for q in ids:
    ds=[]
    for f in (OWN/q).glob('r48_*/design.json'):
        d=f.parent;design=read(f);manual=read(d/'manual_final_review.json') if (d/'manual_final_review.json').exists() else None
        evidence=list((d/'tests').glob('quicktest3_*'))
        calls=[]
        for t in evidence:
            for p in sorted(t.glob('run_*_started.json')):
                job=p.with_name(p.name.replace('_started',''))
                calls.append({'started_record':str(p),'started_sha256':hashfile(p),'status':read(job)['status'] if job.exists() else 'IN_FLIGHT_NO_FINAL','result_record':str(job) if job.exists() else None})
        ds.append({'variant_id':design['variant_id'],'design_path':str(f),'plugin_path':str(d/'plugin.json'),'candidate_png':str(d/'candidate.png'),'png_sha256':design['png_sha256'],'design_sha256':hashfile(f),'expected_wrong_answer':design['expected_wrong_answer'],'material_difference':design['material_difference'],'mathematical_proof':str(d/'math_proof.json'),'native_primary_review':str(d/'primary_review.json'),'render_check':str(d/'render_check.json'),'marker_audit':str(d/'marker_chroma_audit.json'),'frozen_bindings_audit':str(d/'frozen_evidence_audit.json') if (d/'frozen_evidence_audit.json').exists() else None,'manual_final_review':str(d/'manual_final_review.json') if manual else None,'manual_finals':[x['manual_terminal_answer'] for x in manual['manual_runs']] if manual else [],'two_hits':manual['two_hits'] if manual else False,'calls':calls,'status':manual['decision'] if manual else ('CALL_IN_PROGRESS' if calls else 'PREPARED_UNTESTED')})
        if manual and manual['two_hits']:queue.append(ds[-1])
    assessment=read(OWN/q/'assessment.json') if (OWN/q/'assessment.json').exists() else None
    entries.append({'question_id':q,'assessed':True,'designs':ds,'screened_without_calls':assessment,'eligibility_final_path':str(OWN/q/'eligibility_final.json'),'source_audit':str(OWN/q/'source_primary_audit.json')})
calls=[c for e in entries for d in e['designs'] for c in d['calls']]
pending=[c for c in calls if c['status']=='IN_FLIGHT_NO_FINAL']
complete=[c for c in calls if c['status']=='completed']
aborted=[c for c in calls if c['status']=='aborted']
errors=[c for c in calls if c['status']=='error']
terminal=not pending and all(not d['calls'] or d['manual_final_review'] for e in entries for d in e['designs'])
cp={'unit':'background_48','stage':'material_refinement','updated_at_utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE_ASSESSED_SCOPE' if terminal else 'IN_PROGRESS_PENDING_EXTERNAL_RESPONSE','stop_condition':'All eight assessed with finite substantive hypotheses; no clean scheme forced for two screened cases.' if terminal else 'No stop decision yet; waiting on exact own in-flight API, no retry.','actual_assessed_question_ids':ids,'unworked_question_ids':[],'counts':{'assessed_questions':8,'material_new_fully_rendered_designs':sum(len(e['designs']) for e in entries),'additional_pre_API_local_render_failure_drafts':1,'questions_screened_without_new_calls':2,'actual_API_starts':len(calls),'completed_calls':len(complete),'aborted_calls':len(aborted),'API_errors':len(errors),'in_flight_calls':len(pending),'credible_two_hit_possibilities':len(queue),'original_control_calls':0,'retries':0},'questions':entries,'pending_calls':pending,'second_review_queue_path':str(OWN/'second_review_queue.json'),'local_errors':str(OWN/'local_errors.json'),'source_preservation':str(OWN/'source_preservation_final.json'),'old_evidence_inventory':str(OWN/'old_history_inventory.json'),'delivered_references':str(OWN/'delivered_references_read.json'),'isolation':str(OWN/'isolation.json'),'harness_source_audit':str(OWN/'harness_source_audit.json'),'formal_approval_Pass_Collect_publication_actions':0,'nested_agents_threads_worktrees':0,'constraints_and_limits':['Original controls not repeated; none found for these eight in local binding scan.','No post-hoc preset changes, same-image retries or selection from more than two calls.','Historical raw bytes retained; no parse repair and no no-call inference from parse failure.','No observed pair proves intended mechanism, causal effect or statistical gain.','Only primary research; parent must commission NEW independent review before delivery.']}
write(OWN/'second_review_queue.json',{'unit':'background_48','stage':'material_refinement','primary_only':True,'candidates':queue,'new_parent_independent_review_required':True})
cp['process_audit_final_path']=str(OWN/'process_audit_final.json')
cp['primary_qualifications_path']=str(OWN/'primary_qualifications.json')
cp['evidence_binding_audit_path']=str(OWN/'evidence_binding_audit.json')
if (OWN/'process_audit_final.json').exists():
    cp['own_API_processes_remaining']=read(OWN/'process_audit_final.json')['own_API_processes_remaining']
write(OWN/'checkpoint.json',cp)
if pending:write(OWN/'checkpoint_pending_external_response.json',cp)
print(cp['status'],cp['counts'])
