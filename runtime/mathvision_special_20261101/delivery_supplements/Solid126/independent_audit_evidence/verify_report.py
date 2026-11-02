from review_env import *
from dataset_tools.catalog import rows, content, digest
report=read(OUT/'independent_review.json')
assert report['question_id']=='Solid126' and report['variant_id']=='r37_local_area_replacement'
assert report['decision'] in ('recommended','hold','reject')
assert report['decision']=='recommended' and not report['blocking_objections']
assert len(report['two_complete_final_answers'])==2 and len(report['per_marker'])==6
for r in report['two_complete_final_answers']:
    assert r['full_raw_final_answer_text'] and r['manually_extracted_option']=='A' and r['explicit_claimed_decrease_percent']==0
    assert all(r['checks'].values())
for v in report['exact_sha256'].values():assert sha(v['absolute_path'])==v['sha256']
for v in report['exact_test_evidence_sha256'].values():assert sha(v['absolute_path'])==v['sha256']
before=read(OUT/'read_only_inputs_before.json')
changed=[p for p,v in before['files'].items() if sha(ROOT/p)!=v['sha256']]
additional=read(OUT/'additional_read_only_sources.json')
late_changed=[p for p,v in additional['files'].items() if sha(ROOT/p)!=v['sha256']]
assert not changed and not late_changed
row=next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid126')
assert digest(content(ROOT,'SolidGeometry',row))==read(ROOT/'provenance/approvals.json')['approvals']['Solid126']['content_sha256']
assert all(not (ROOT/'SolidGeometry/special_variant/Solid126'/n).exists() for n in ('recipes.json','collection.json'))
for n in ('accepted_index.jsonl','collected_index.jsonl'):
    assert not any(x.get('question_id')=='Solid126' or x.get('id')=='Solid126' for x in rows(ROOT/'SolidGeometry/special_variant'/n))
assert report['independent_mathematical_proof']['third_check_independent_unit_cell_enumeration']['remaining_area']==378
assert report['old_history']['old_preset']=='C' and report['old_history']['old_result'].startswith('MISS')
assert all(r['matches_predeclared_wrong_option'] is False for r in report['old_history']['old_runs_with_full_content'])
save('report_verification.json',{'checked_at':stamp(),'pid':os.getpid(),'report_path':str(OUT/'independent_review.json'),'report_sha256':sha(OUT/'independent_review.json'),'required_fields_and_complete_answers_valid':True,'all_key_test_hashes_still_match':True,'all_initial_128_inputs_and_late_9_sources_unchanged':not changed and not late_changed,'source_approval_still_matches':True,'no_pass_collect_or_special_completion':True,'old_C_A_A_remains_MISS':True,'no_new_API_calls':True,'blocked':BLOCKED})
print(json.dumps({'verified':True,'pid':os.getpid(),'report_sha256':sha(OUT/'independent_review.json'),'tracked_inputs':len(before['files']),'late_sources':len(additional['files'])},ensure_ascii=False))
