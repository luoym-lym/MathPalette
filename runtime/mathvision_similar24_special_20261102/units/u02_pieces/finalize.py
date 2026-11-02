from worker import *
import base64

def finalize():
    halt=read(OWN/'host_api_halt.json')
    assert halt['question_id']=='Plane398'
    error_summary_path=Path(halt['summary_path'])
    invocation=error_summary_path.parent
    summary=read(error_summary_path);binding=read(invocation/'binding.json')
    request=read(invocation/'request.json')
    assert len(summary['results'])==1 and summary['results'][0]['status']=='error'
    assert not (invocation/'run_02_started.json').exists()
    assert filehash(invocation/'request.json')==binding['request_body_sha256']
    partial=invocation/'run_01_incomplete_response.bin'
    partial_bytes=partial.read_bytes()
    assert digest(partial_bytes)==summary['results'][0]['partial_response_sha256']
    assert binding['design_sha256']==filehash(binding['design_path'])==filehash(invocation/'design_snapshot.json')
    assert binding['image_sha256']==filehash(binding['image_path'])
    embedded=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    assert digest(embedded)==binding['image_sha256'];del embedded
    assert request['messages'][1]['content'][0]['text']==read(OWN/'Plane398/formal_record.json')['question']
    transport={'reviewed_at':now(),'actual_first_run_status':'incomplete_http_response',
      'elapsed_seconds':summary['results'][0]['elapsed_seconds'],
      'partial_path':str(partial),'partial_sha256':digest(partial_bytes),'partial_bytes':len(partial_bytes),
      'partial_byte_histogram':{str(b):partial_bytes.count(b) for b in sorted(set(partial_bytes))},
      'partial_has_complete_answer':False,'manual_final_answer':None,
      'original_summary_path':str(error_summary_path),'original_summary_sha256':filehash(error_summary_path),
      'original_binding_sha256':filehash(invocation/'binding.json'),'request_sha256':filehash(invocation/'request.json'),
      'second_call_not_started':True,'no_retry_no_relabel_no_resume':True,
      'harness_returned_naturally_no_manual_termination':True,
      'subsequent_API_invocations_stopped_for_entire_unit':True,
      'remote_failure_cause_unknown':True,
      'retained_request_binding_started_design_snapshot_partial_error_summary':True}
    write(OWN/'Plane398/p02_detached_two_piece_B_independent_rotations/transport_failure_review.json',transport)
    registry=[];byq={}
    for qid in ('Plane218','Plane398'):
        designs=[]
        for dp in sorted((OWN/qid).glob('*/design.json')):
            out=dp.parent;d=read(dp)
            entry={'question_id':qid,'variant_id':d['variant_id'],'candidate_directory':str(out),
              'correct_answer':d['correct_answer'],'wrong_preset':d['expected_wrong_answer'],
              'image_sha256':filehash(out/'candidate.png'),'plugin_sha256':filehash(out/'plugin.json'),
              'design_sha256':filehash(dp),'primary_math_proof_path':d['primary_mathematical_proof_path'],
              'reference_transfer_path':str(out/'reference_transfer.json'),
              'render_gates_path':str(out/'render_gates.json'),
              'new_process_exact_replay_path':str(out/'independent_process_exact_replay.json'),
              'primary_visual_review_path':str(out/'primary_visual_review_before_calls.json')}
            replay=read(out/'independent_process_exact_replay.json')
            assert replay['image_sha256']==entry['image_sha256'] and replay['design_sha256']==entry['design_sha256']
            if (out/'manual_full_final_review.json').exists():
                r=read(out/'manual_full_final_review.json')
                entry.update(status=r['decision'],manual_finals=[x['manual_final_letter'] for x in r['two_complete_finals']],
                             manual_review_path=str(out/'manual_full_final_review.json'))
            elif (out/'transport_failure_review.json').exists():
                entry.update(status='API_INCOMPLETE_FIRST_RESPONSE_NO_SECOND_CALL_DO_NOT_RETEST',manual_finals=[],
                             transport_review_path=str(out/'transport_failure_review.json'))
            else:
                assert not (out/'tests').exists()
                entry.update(status='UNTESTED_API_BATCH_HALTED',manual_finals=[],
                             unfinished_reason='Both required real calls unstarted because prior transport error ended this unit batch. Offline proof/schema/noop/repeat/new-process replay/native visual review passed; this is not a qualifying PRIMARY candidate.')
                assert d.get('material_color_proof_path')
                entry['material_color_proof_path']=d['material_color_proof_path']
                entry['material_color_proof_sha256']=d['material_color_proof_sha256']
            designs.append(entry);registry.append(entry)
        byq[qid]={'status':'UNFINISHED_API_BLOCKED_NO_TWO_HIT_PRIMARY',
          'independently_verified_unique_original_answer':'A' if qid=='Plane218' else 'E',
          'primary_mathematical_proof_path':str(OWN/qid/'primary_mathematical_proof.json'),
          'native_material_color_proof_path':str(OWN/qid/'p03_color_preserving_boundary_proof.json'),
          'current_eligibility_path':str(OWN/qid/'eligibility_current.json'),
          'designs':designs,'no_claim_of_unsolvability':True,
          'completion_reason':'Earlier complete pairs did not both hit their frozen preset. A genuinely different native-boundary scheme is prepared but its two calls remain unstarted after the unit transport failure.'}
    started=list(OWN.glob('Plane*/*/tests/*/run_*_started.json'))
    raw=list(OWN.glob('Plane*/*/tests/*/run_*_response.json'))
    assert len(started)==7 and len(raw)==6
    assert read(OWN/'second_review_queue.json')==[]
    report={'unit_id':'u02_pieces','finished_at':now(),'scope':['Plane218','Plane398'],
      'status':'RESEARCH_STOPPED_ON_ORIGINAL_HARNESS_TRANSPORT_FAILURE',
      'qualifying_PRIMARY_candidates':0,'independent_second_review_queue':[],
      'new_designs':len(registry),'tested_designs':4,'complete_two_call_pairs':3,
      'real_new_request_count':7,'complete_raw_responses':6,'partial_error_responses':1,
      'manually_aborted_requests':0,'third_calls_or_retries':0,'questions':byq,
      'transport_failure':transport,
      'unfinished_native_drafts':[e for e in registry if e['status']=='UNTESTED_API_BATCH_HALTED'],
      'source_and_evidence_preservation_path':str(OWN/'source_and_evidence_preservation.json'),
      'complete_read_audit_path':str(OWN/'complete_read_audit.json'),
      'own_offline_diagnostic_error_paths':[str(OWN/'offline_diagnostic_errors.json'),str(OWN/'native_path_inspection_correction.json')],
      'known_history_outside_new_counts':'Old Plane398 wrong_corner_L_transfer had two complete D/A finals against C; those are historical, preserved read-only and excluded from the seven new calls.',
      'constraints':{'all_new_writes_only_own_root':True,'strict_writeguard':True,
          'python_utf8_B_and_four_numeric_thread_limits_1':True,'runtime_isolation_installed':True,
          'original_harness_copy_byte_identical':True,'new_subagents_servers_worktrees':0,
          'formal_question_source_answer_or_approval_edits':0,'Pass_Collect_or_delivery_actions':0},
      'limitations':['No candidate met the required two-hit gate; none can enter independent second review or delivery.',
          'The native p03 schemes have mathematical and local-render evidence only, no solver observations.',
          'Six complete responses often fabricate cell counts or impose full coverage; no claimed causal mechanism or population success rate.',
          'The source/grid coverage wording in the preparation brief was corrected against the formal Plane218 text: two pentominoes leave two unused cells.',
          'A future authorized batch may assess the genuinely untested native p03 drafts after the API condition changes; the old incomplete/failing PNGs must not be retried.']}
    write(OWN/'candidate_registry.json',registry)
    write(OWN/'unit_report.json',report)
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint.update(updated_at=now(),status=report['status'],actual_new_API_calls=7,
      complete_raw_responses=6,partial_error_responses=1,primary_candidates=[],
      question_status={q:v['status'] for q,v in byq.items()},
      holds=[{'question_id':'Plane398','reason':'Original-harness incomplete HTTP response stopped this entire unit batch.'}],
      unworked=[{'question_id':e['question_id'],'variant_id':e['variant_id'],'remaining':'Exactly two original quicktest3 calls unstarted due prior transport failure.'} for e in report['unfinished_native_drafts']],
      all_assigned_accounted_for=True,report_path=str(OWN/'unit_report.json'),
      no_quota_or_three_candidate_early_stop=True,
      API_process_naturally_finished=True)
    checkpoint.setdefault('attempts',{})['Plane398/p02_detached_two_piece_B_independent_rotations']={'status':'API_INCOMPLETE_FIRST_RESPONSE_NO_SECOND_CALL_DO_NOT_RETEST','preset':'B','manual_finals':[],'review_path':str(OWN/'Plane398/p02_detached_two_piece_B_independent_rotations/transport_failure_review.json')}
    write(OWN/'checkpoint.json',checkpoint)
    print(json.dumps({'status':report['status'],'new_requests':7,'complete':6,'partial':1,
                      'PRIMARY_candidates':0,'unworked_new_native_drafts':2,'report':str(OWN/'unit_report.json')}))

if __name__=='__main__':finalize()
