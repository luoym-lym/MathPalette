from audit_io import install,OWN,PROJECT,load,save,sha,IDS
install()
import json
from datetime import datetime,timezone

h=load(OWN/'host_memory_failure.json')
h.pop('observed_at_utc',None)
h['observed_by_clock_utc']='2026-11-01T20:35:40Z'
h['timestamp_limit']='Error preceded the actual20:35:40 UTC clock-tool reading; no exact per-command trusted timestamp was captured.'
save(OWN/'host_memory_failure.json',h)

c=load(OWN/'checkpoint.json');queue=load(OWN/'second_review_queue.json')
assert c['stage']=='material_refinement' and c['calls_started']==c['calls_completed']==6 and c['complete_two_call_pairs']==3
assert c['calls_aborted']==0 and c['new_credible_possible_candidate_count']==queue['count']==0
assert c['untested_frozen_design_question_ids']==['Plane482','Plane488']
assert c['actual_assessed_question_ids']==IDS and not c['unworked_question_ids']
assert load(OWN/'process_closure.json')['all_own_API_processes_closed']
checks=[]
for case in c['cases']:
    qid=case['question_id']
    assert load(OWN/qid/'eligibility_final.json')['eligible']
    assert load(OWN/qid/'baseline_check.json')['pixel_equal']
    for d in case['designs']:
        f=OWN/qid/d['variant_id']
        assert sha(f/'design.json')==d['design_sha256']==load(f/'primary_review_before_calls.json')['design_sha256']
        assert sha(f/'candidate.png')==sha(f/'repeat.png')==d['image_sha256']
        assert load(f/'post_test_offline_replay.json')['replay_sha256']==d['image_sha256']
        assert load(f/'native_preservation_audit.json')['original_geometry_facecolors_texts_object_metadata_snap_points_view_canvas_exact_equal']
        assert sha(f/'plugin.json')==d['plugin_sha256']
        for b in (f/'tests').glob('*/binding.json') if (f/'tests').exists() else []:
            binding=load(b)
            assert binding['design_sha256']==d['design_sha256'] and binding['image_sha256']==d['image_sha256']
            assert binding['expected_wrong_answer']==d['wrong_preset_unchanged']
            summary=load(b.parent/'summary.json');assert summary['two_completed'] and len(summary['results'])==2
        checks.append({'qid':qid,'variant_id':d['variant_id'],'frozen_design_plugin_PNG_repeats_bindings_exact':True,'status':d['status']})
for f in (OWN/'reference_read').glob('*.json'):
    ref=load(f);assert sha(ref['source'])==ref['sha256']
assert all(x['unchanged'] for x in load(OWN/'old_evidence_preservation_final.json')['files'])

facts={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'source_qualification_noop_math_marker_native_and_hash_audits_saved':True,'exact_two_call_pairs':3,'completed_real_calls':6,'new_possible_candidates':0,'API_errors':0,'aborts':0,'retries':0,'host_memory_failure':str(OWN/'host_memory_failure.json'),'provider_anomaly':str(OWN/'provider_response_anomaly.json'),'no_actual_termination':True,'all_own_API_processes_closed':True,'old_scoped_files_unchanged':156,'exact_independent_reject_reports_unchanged':3,'formal_original_approvals_special_records_helpers_env_runtime_git_not_written':True,'all_own_outputs_below':str(OWN),'untested_frozen_designs_not_candidates':['Plane482','Plane488']}
save(OWN/'final_qa.json',facts)
c['process_closure']=str(OWN/'process_closure.json');c['all_own_API_processes_closed']=True;c['final_qa']=str(OWN/'final_qa.json');c['process_status']='All3 own API child processes exited0; exact PID/command closure check found no live own Python processes. Zero terminations/aborts/retries.'
c['external_stop_detail']='Host OpenBLAS memory initialization failed during reporting; no new solver call was started afterward. The already outstanding Plane483 second call completed normally before the exact-PID termination guard. Plane482/488 remain frozen and untested.'
save(OWN/'checkpoint.json',c)

excluded={'tmp','mpl','cache','render_tmp','harness'}
files=[]
for p in sorted(OWN.rglob('*')):
    if not p.is_file() or p.name=='artifact_manifest.json':continue
    rel=p.relative_to(OWN)
    if rel.parts[0] in excluded:
        if rel.as_posix()!='harness/quicktest3_isolated.py':continue
    files.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
save(OWN/'artifact_manifest.json',{'root':str(OWN),'artifacts':files,'runtime_caches_temporary_bridge_files_excluded':True,'final_qa':str(OWN/'final_qa.json'),'no_API_calls_from_this_QA':True})
print(json.dumps(facts,ensure_ascii=False))
