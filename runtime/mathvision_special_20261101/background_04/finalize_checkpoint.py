from research import *
ROOT_IDS=['Plane224','Plane280','Solid206','Solid247']
ASSIGNED_PLANE=['Plane197','Plane258','Plane225','Plane238','Plane240','Plane314','Plane332','Plane322']
ASSIGNED_SOLID=['Solid170','Solid188','Solid169','Solid185','Solid106','Solid152','Solid204','Solid199']
def relative(path):return Path(path).relative_to(ROOT).as_posix()
def main():
    plane=json.loads((HERE/'plane_worker/checkpoint.json').read_text(encoding='utf-8-sig'))
    solid=json.loads((HERE/'solid_worker/checkpoint.json').read_text(encoding='utf-8-sig'))
    local=json.loads((HERE/'root_results.json').read_text(encoding='utf-8-sig'))
    audit=json.loads((HERE/'evidence_binding_audit.json').read_text(encoding='utf-8-sig'))
    preservation=json.loads((HERE/'source_preservation_audit.json').read_text(encoding='utf-8-sig'))
    process=json.loads((HERE/'no_live_processes.json').read_text(encoding='utf-8-sig'))
    if isinstance(process,dict):process=process.get('processes',process.get('matching_processes',[]))
    assert not process,'Own background_04 Python processes remain'
    assert audit['all_checks_pass']
    assert not preservation['formal_changed'] and not preservation['formal_added'] and not preservation['formal_deleted'] and not preservation['previous_evidence_changed_or_deleted']
    qids=ROOT_IDS+ASSIGNED_PLANE+ASSIGNED_SOLID
    if 'assessed_question_ids' in plane:assert set(plane['assessed_question_ids'])==set(ASSIGNED_PLANE)
    if 'assessed_questions' in plane:assert {r['question_id'] for r in plane['assessed_questions']}==set(ASSIGNED_PLANE)
    assert set(solid['assessed_question_ids'])==set(ASSIGNED_SOLID)
    assert len(qids)==len(set(qids))==20
    checks=[eligible('PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry',q) for q in qids]
    write(HERE/'eligibility_at_checkpoint.json',checks)
    candidates=[]
    for worker in ['plane_worker','solid_worker']:
        queue=json.loads((HERE/worker/'second_review_queue.json').read_text(encoding='utf-8-sig'))
        items=queue if isinstance(queue,list) else queue.get('candidates',queue.get('queue',[]))
        candidates.extend(items)
    assert len(candidates)<=3
    write(HERE/'second_review_queue.json',{'created_at':datetime.now(timezone.utc).isoformat(),'candidate_count':len(candidates),'candidates':candidates,'status':'FOR_NEW_PARENT_INDEPENDENT_SECOND_REVIEW_ONLY','independent_second_reviews_performed_by_this_unit':0,'qualified_or_published_candidates':0,'no_Pass_Collect':True,'worker_queues':[relative(HERE/w/'second_review_queue.json') for w in ['plane_worker','solid_worker']]})
    runs=[r for inv in audit['invocations'] for r in inv['runs']]
    completed=[r for r in runs if r['status']=='completed' and not r.get('truncated') and r.get('finish_reason')!='length']
    invocation_folders=[Path(r['binding_path']).parent for r in audit['invocations']]
    two_complete=sum(len(r['runs'])==2 and all(j['status']=='completed' and not j.get('truncated') and j.get('finish_reason')!='length' for j in r['runs']) for r in audit['invocations'])
    designs=sorted(HERE.rglob('design.json'))
    bound={json.loads((p/'binding.json').read_text(encoding='utf-8-sig'))['design_path'] for p in invocation_folders}
    untested=[relative(p) for p in designs if str(p) not in bound]
    files={relative(p):digest(p) for p in HERE.rglob('*') if p.is_file() and p.name not in ['checkpoint.json','evidence_manifest.json']}
    write(HERE/'evidence_manifest.json',{'created_at':datetime.now(timezone.utc).isoformat(),'files':files})
    value={
        'created_at':datetime.now(timezone.utc).isoformat(),'status':'FINITE_BACKGROUND_04_COMPLETE',
        'stop_reason':'Twenty new assigned questions assessed. Final Plane238 intermediate-fold request stalled and was explicitly aborted after exact own PID/command verification; no response is counted and its second call never started. Earlier pairs and pre-API rejections are preserved. No repeated failed identical-image requests.',
        'all_outputs_under':relative(HERE),'assessed_question_count':20,'new_question_ids':qids,
        'root_assessment':local,'plane_worker_checkpoint':relative(HERE/'plane_worker/checkpoint.json'),'plane_worker_results':plane,
        'solid_worker_checkpoint':relative(HERE/'solid_worker/checkpoint.json'),'solid_worker_results':solid,
        'saved_candidate_designs':len(designs),'test_invocations_including_controls':len(audit['invocations']),
        'two_complete_call_invocations':two_complete,'completed_calls_including_controls':len(completed),
        'failed_calls':sum(r['status']!='completed' for r in runs),'aborted_calls':sum(1 for folder in invocation_folders for p in folder.glob('run_??_aborted.json')),'aborted_evidence_files':[relative(p) for folder in invocation_folders for p in folder.glob('*aborted*.json')],
        'all_untested_design_paths':untested,'credible_two_hit_candidate_count':len(candidates),'possible_candidates_for_parent_new_independent_second_review':candidates,
        'new_qualified_deliveries':0,'independent_second_reviews_performed_by_this_unit':0,
        'evidence_binding_audit':relative(HERE/'evidence_binding_audit.json'),'evidence_manifest':relative(HERE/'evidence_manifest.json'),
        'source_preservation_audit':relative(HERE/'source_preservation_audit.json'),'all_binding_checks_pass':audit['all_checks_pass'],
        'eligibility_rechecked_at_checkpoint':relative(HERE/'eligibility_at_checkpoint.json'),
        'formal_library_workbench_env_protocol_approval_recipe_index_edits':False,'previous_exploration_evidence_mutations':False,'Pass_Collect_review_APIs_used':False,
        'no_live_process_confirmation':relative(HERE/'no_live_processes.json'),'native_workers_finished':True,
        'root_rejected_candidate_disclosure':'Plane280 was rendered but rejected before API after actual frozen artist widths proved1pt for both target/grid. Its immutable pretest design incorrectly assumed the source semantic2.5pt width; primary_visual_review.json explicitly corrects the metadata and rejects target-membership ambiguity. All failed serialization partials retained.',
        'original_controls':'No original controls required for failed pairs; any controls actually run are preserved in worker evidence and disclosed there.',
        'next_recommendations':['Do not retest any identical failed image from this unit.','If a future unit is authorized, select only NEW remaining not_yet_explored formal MathVision records after parent aggregation and fresh eligibility checks.','All possible future deliveries require a NEW independent second-review task; this unit publishes no candidate or Pass/Collect.']}
    write(HERE/'checkpoint.json',value)
    print(json.dumps({'assessed':20,'saved_designs':len(designs),'invocations':len(audit['invocations']),'complete_pairs':two_complete,'completed_calls':len(completed),'second_review_candidates':len(candidates),'checkpoint':str(HERE/'checkpoint.json')},ensure_ascii=False))
if __name__=='__main__':main()
