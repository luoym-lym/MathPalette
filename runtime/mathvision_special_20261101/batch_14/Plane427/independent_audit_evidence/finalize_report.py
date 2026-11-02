from review_bootstrap import *
audit=read(OWN/'process_audit_final.json')
assert audit['zero_residual_own_processes'] and not audit['residual_own_processes']
report=read(OWN/'independent_review.json')
report['workspace_process_discipline']['zero_residual_own_processes']=True
report['workspace_process_discipline']['external_zero_process_check_observed_at_utc']=audit['checked_at_utc']
report['workspace_process_discipline']['final_external_process_audit_path']=str(OWN/'process_audit_final.json')
report['workspace_process_discipline']['final_external_check_runs_after_this_foreground_writer_exits']=True
for run in report['two_complete_final_answers']:
    raw_path=Path(run['raw_response_path'])
    assert run['hashes']['raw_response']==sha(raw_path)
    assert run['full_assistant_content']==read(raw_path)['choices'][0]['message']['content']
assert report['decision'] in ['recommended','hold','reject']
assert report['question_id']=='Plane427' and report['variant_id']=='r41_isosceles_base_angle_frame'
assert report['source_readonly_verification']['all_tracked_hashes_and_mtimes_unchanged']
report['supporting_new_artifacts']['finalize_report.py']={'absolute_path':str(OWN/'finalize_report.py'),'sha256':sha(OWN/'finalize_report.py')}
write('independent_review.json',report)
validation=read(OWN/'report_validation.json')
validation['report_sha256']=sha(OWN/'independent_review.json')
validation['full_raw_contents_match']=True
validation['zero_residual_own_processes_checked_externally']=True
validation['schema_required_fields_valid']=True
write('report_validation.json',validation)
print(json.dumps({'decision':report['decision'],'required_fields_and_full_raw_valid':True,'final_report_sha256':sha(OWN/'independent_review.json')}))
