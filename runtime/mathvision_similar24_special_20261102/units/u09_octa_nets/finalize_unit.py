from own_bootstrap import *
from unit_tools import eligibility,snapshot

def main():
    queue=load(OWN/'second_review_queue.json')
    cp=load(OWN/'checkpoint.json')
    own_processes=[load(p) for p in OWN.rglob('own_api_process.json')]
    assert all(p['ended_at'] and p['status']=='harness_returned' for p in own_processes)
    attempt_records=[];started_ids=[]
    for d in sorted((OWN/'Solid166').iterdir()):
        if not d.is_dir() or not (d/'design.json').is_file():continue
        design=load(d/'design.json')
        if not (d/'manual_final_review.json').is_file():
            attempt_records.append({'variant_id':design['variant_id'],'status':'unworked_prepared_only',
                 'reason':'No completed reviewed two-call evidence; no qualification claimed.','directory':str(d)})
            continue
        review=load(d/'manual_final_review.json')
        summaries=list((d/'tests').rglob('summary.json'));assert len(summaries)==1
        summary_path=summaries[0];summary=load(summary_path)
        binding=load(summary_path.parent/'binding.json')
        assert summary['requested_runs']==binding['requested_runs']==2
        assert summary['design_sha256']==sha(d/'design.json')==sha(summary_path.parent/'design_snapshot.json')
        assert summary['image_sha256']==sha(d/'candidate.png')==sha(d/'candidate_repeat.png')
        assert review['plugin_sha256']==sha(d/'plugin.json')
        assert len(summary['results'])==2 and summary['two_completed']
        assert len(list(summary_path.parent.glob('run_*_started.json')))==2
        assert len(list(summary_path.parent.glob('run_*_response.json')))==2
        assert hashlib.sha256((summary_path.parent/'request.json').read_bytes()).hexdigest()==summary['request_body_sha256']
        for i,r in enumerate(summary['results'],1):
            start=load(summary_path.parent/f'run_{i:02d}_started.json')
            assert start['run_id']==r['run_id'];started_ids.append(start['run_id'])
            assert r['status']=='completed' and not r['truncated'] and r['finish_reason']=='stop'
            assert r['response_sha256']==sha(summary_path.parent/f'run_{i:02d}_response.json')
            network=load(d/'tests'/f'pre_network_run_{i:02d}.json')
            assert network['eligibility']['eligible']
            assert network['request_body_sha256']==summary['request_body_sha256']
        fingerprints={str(f.relative_to(d)):sha(f) for f in d.rglob('*') if f.is_file() and f.name!='evidence_hashes.json'}
        save(d/'evidence_hashes.json',{'created_at':now(),'file_sha256':fingerprints,'all_original_request_binding_started_raw_parsed_summary_and_design_snapshot_preserved':True},exclusive=True)
        attempt_records.append({'question_id':'Solid166','variant_id':design['variant_id'],'directory':str(d),
             'frozen_wrong_preset':design['preset_semantics'],'final_values':[r['manual_final_value'] for r in review['reviews']],
             'two_completed':True,'double_hit':review['double_hit'],'actual_calls':2,
             'manual_review_path':str(d/'manual_final_review.json'),'evidence_hashes_path':str(d/'evidence_hashes.json')})
    assert len(started_ids)==len(set(started_ids))==sum(p['network_requests'] for p in own_processes)
    current={q:eligibility(q) for q in ('Solid166','Solid240')}
    save(OWN/'eligibility_final.json',current,exclusive=True)
    initial=load(OWN/'readonly_execution_source_initial.json')
    assert snapshot()==initial
    harness=load(OWN/'harness/copy_integrity.json')
    assert sha(OWN/'harness/quicktest3_isolated.py')==harness['copied_sha256']
    assert sha(OLD/'harness/quicktest3_isolated.py')==harness['original_sha256']
    copied=(OWN/'harness/quicktest3_isolated.py').read_bytes()
    assert copied.replace(harness['only_replacement']['after'].encode(),harness['only_replacement']['before'].encode())==(OLD/'harness/quicktest3_isolated.py').read_bytes()
    preservation={}
    for rel,v in load(OWN/'read_source_manifest.json').items():
        preservation[rel]={'before_sha256':v['sha256'],'after_sha256':sha(PROJECT/rel)}
        assert preservation[rel]['before_sha256']==preservation[rel]['after_sha256']
    assert sha(OWN/'assignment.json')==cp['assignment_sha256'] and sha(OWN/'brief.txt')==cp['brief_sha256']
    save(OWN/'source_preservation_final.json',{'checked_at':now(),'formal_approval_fingerprints_match':True,
        'formal_geometry_sources_and_execution_files_unchanged':True,'execution_file_hashes':snapshot(),
        'all_read_old_evidence_and_current_reference_files':preservation,'brief_assignment_unchanged':True,
        'harness_path_only_copy_and_reverse_byte_equality_preserved':True,
        'formal_special_state_records_unchanged_and_empty_for_assigned':True,
        'strict_writeguard_during_all_python_processes':str(OWN),'no_formal_approval_Pass_Collect_writes':True},exclusive=True)
    has_primary=any(e['question_id']=='Solid166' for e in queue)
    if not has_primary:
        assert (OWN/'Solid166/uncompleted_reason.json').is_file()
    final={'unit_id':'u09_octa_nets','finished_at':now(),'assigned':['Solid166','Solid240'],
        'PRIMARY_candidates':[{'question_id':e['question_id'],'variant_id':e['variant_id'],'directory':e['candidate_directory']} for e in queue],
        'attempts':attempt_records,'actual_new_call_count':len(started_ids),'complete_new_call_count':len(started_ids),
        'API_errors':[],'API_aborts':[],'retries':0,'third_calls':0,
        'holds':[{'question_id':'Solid240','reason':'Original visible face orientation not uniquely bound; proper rotations give right-neighbor1/2/6. Frozen internal assumption Q_apex_maps_to_T yields1 but is not a visible vertex correspondence.',
          'evidence':str(OWN/'Solid240/primary_math_and_orientation_hold.json'),'calls':0}],
        'unworked':[],'local_read_diagnostics_path':str(OWN/'local_read_diagnostics.json'),
        'source_preservation_path':str(OWN/'source_preservation_final.json'),
        'second_review_queue_path':str(OWN/'second_review_queue.json'),
        'question_outcomes':{
           'Solid166':{'status':'PRIMARY_PENDING_NEW_INDEPENDENT_REVIEW' if has_primary else 'UNCOMPLETED_NO_QUALIFYING_TWO_HIT_CANDIDATE',
               'reason_path':None if has_primary else str(OWN/'Solid166/uncompleted_reason.json'),
               'primary_candidate_count':sum(e['question_id']=='Solid166' for e in queue),'actual_calls':len(started_ids)},
           'Solid240':{'status':'HOLD_ORIGINAL_ORIENTATION_UNIQUENESS','actual_calls':0,
               'reason_path':str(OWN/'Solid240/hold_report.json')}},
        'unfinished_required_work':(['New independent second review of Solid166 PRIMARY candidate'] if has_primary else ['Solid166 still needs a separately justified design meeting the exact two-hit rule']) + ['Review the Solid240 original face-orientation uniqueness hold before any candidate calls'],
        'own_API_process_records':own_processes,'all_owned_API_harness_functions_returned':True,
        'process_cleanup_path':str(OWN/'process_cleanup.json'),
        'independent_second_review_performed':False,'user_approval_Pass_Collect_delivery':False,
        'limitations':['Only the frozen two-call observations are reported.','No population success rate or causal gain is established.','Parent must create a new independent reviewer before delivery.','Solid240 is a documented hold, not an answer correction or original approval invalidation.']}
    save(OWN/'primary_report.json',final,exclusive=True)
    cp.update(phase='PRIMARY_RESEARCH_FINISHED_PENDING_PARENT_REVIEW',updated_at=now(),new_actual_calls=len(started_ids),
       attempts=attempt_records,own_processes=own_processes,report_path=str(OWN/'primary_report.json'),
       holds=['Solid240'],errors=[],unworked=[],independent_second_review_performed=False,formal_writes_Pass_Collect=False)
    if not has_primary:
        cp['questions']['Solid166']={'status':'UNCOMPLETED_NO_QUALIFYING_TWO_HIT_CANDIDATE','reason_path':str(OWN/'Solid166/uncompleted_reason.json'),'actual_calls_total':len(started_ids)}
    save(OWN/'checkpoint.json',cp)
    print(json.dumps({'PRIMARY_candidates':final['PRIMARY_candidates'],'actual_new_calls':len(started_ids),'holds':['Solid240'],'report':str(OWN/'primary_report.json')},ensure_ascii=False))

if __name__=='__main__':main()
