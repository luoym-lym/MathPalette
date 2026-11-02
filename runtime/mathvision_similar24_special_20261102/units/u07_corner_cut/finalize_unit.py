from worker_env import *
import gc

checks=[]
def verify(path,expected,kind):
    p=Path(path);actual=sha(p)
    checks.append({'path':str(p),'expected_sha256':expected,'actual_sha256':actual,'unchanged':actual==expected,'kind':kind})

initial=read(OWN/'initialization.json')
for name in ('brief','assignment'):
    verify(OWN/(name+'.txt' if name=='brief' else name+'.json'),initial[name+'_sha256'],'unit scope frozen bytes')
assignment=read(OWN/'assignment.json')
for q in assignment['questions']:
    for relative,expected in q['frozen_source_files_sha256'].items():verify(PROJECT/relative,expected,'formal source and frozen input')
for relative,expected in read(OWN/'protocol_fingerprints.json').items():verify(PROJECT/relative,expected,'protocol')
for h in read(OWN/'history_audit.json'):
    for f in h['actual_files_read']:verify(PROJECT/f['path'],f['sha256'],'old evidence')
for qid,entry in read(OWN/'references_read.json').items():
    for filename,value in entry.items():verify(TASK/'references'/qid/filename,value['sha256'],'current user reference')
for item in read(OWN/'supplementary_source_and_semantics_audit.json'):
    p=Path(item['path']);p=p if p.is_absolute() else PROJECT/p
    verify(p,item['sha256'],'supplementary source or old semantics evidence')
harness=read(OWN/'harness/copy_audit.json')
verify(OLD/'harness/quicktest3_isolated.py',harness['original_sha256'],'original quicktest3 harness')
verify(OWN/'harness/quicktest3_isolated.py',harness['copied_sha256'],'copied localized quicktest3 harness')
for qid in assignment['question_ids']:
    e=eligibility(qid);assert e['eligible'];write(OWN/qid/'eligibility_final.json',e,True)
assert all(c['unchanged'] for c in checks),'Real frozen source/evidence drift: preserve and hold'

# Recreate adapter manifest without rendering: strict exact JSON canonicalization,
# no tolerance and no modification of frozen input or renderer.
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from mathvision_adapter import RendererAdapter
baseline=read(OWN/'render_environment.json')
adapter=RendererAdapter(baseline['config'])
manifest_equal=json.loads(json.dumps(adapter.manifest))==baseline['adapter_manifest']
assert manifest_equal
write(OWN/'source_preservation_final.json',{'checked_at':now(),'all_checked_frozen_bytes_unchanged':True,
 'exact_adapter_manifest_unchanged':True,'files':checks,'no_parent_metadata_restored':True,
 'source_note':'Parent progress/brief append metadata is not treated as input drift. Only actual frozen source/reference/evidence bytes are compared.',
 'formal_edit_approval_Pass_Collect_actions':False,'env_git_dotruntime_modified':False,
 'write_isolation':'Every Python command imports worker_env first, sets four numerical thread counts to 1 before project/Pillow/numerical imports, installs original runtime_isolation and own_root-only audit guard. No Python bytecode. All localizations stay in memory or own_root.'},True)

questions={};all_candidates=[];all_runs=[];api_errors=[]
for qid in assignment['question_ids']:
    rows=[]
    for f in sorted((OWN/qid).glob('*/design.json')):
        folder=f.parent;design=read(f);review=read(folder/'manual_final_review.json')
        inv=Path(review['summary_path']).parent;summary=read(inv/'summary.json');binding=read(inv/'binding.json')
        assert summary['two_completed'] and len(summary['results'])==2
        assert binding['requested_runs']==2
        assert binding['image_sha256']==sha(folder/'candidate.png')==design['image_sha256']
        assert binding['design_sha256']==sha(f)==sha(inv/'design_snapshot.json')
        assert binding['request_body_sha256']==sha(inv/'request.json')
        assert sha(folder/'candidate.png')==sha(folder/'repeat.png')==sha(folder/'independent_process_replay.png')
        assert sha(folder/'plugin.json')==design['plugin_sha256']
        assert len(list(inv.glob('run_*_started.json')))==2
        assert read(folder/'api_process_finished.json')['actual_urllib_requests']==2
        records={}
        for path in inv.iterdir():
            if path.is_file():records[path.name]=sha(path)
        for index,result in enumerate(summary['results'],1):
            rawpath=inv/f'run_{index:02d}_response.json';raw=read(rawpath)
            assert sha(rawpath)==result['response_sha256']
            assert result['status']=='completed' and not result['truncated']
            assert raw['choices'][0]['finish_reason']=='stop'
            assert raw['choices'][0]['message']['content']==result['answer']
            eligibility_at_request=read(folder/f'eligibility_at_actual_request_{index:02d}.json')
            assert eligibility_at_request['eligibility']['eligible']
            assert eligibility_at_request['request_body_sha256']==binding['request_body_sha256']
            all_runs.append({'question_id':qid,'variant_id':design['variant_id'],'run_index':index,
              'status':result['status'],'raw_response_path':str(rawpath),'raw_response_sha256':sha(rawpath),
              'manual_final_letter':review['manual_finals'][index-1]['manual_final_letter'],
              'preset':design['expected_wrong_answer']})
        write(folder/'permanent_evidence_hashes.json',{'checked_at':now(),'files':records,'all_bindings_verified':True},True)
        rows.append({'variant_id':design['variant_id'],'directory':str(folder),'frozen_preset':design['expected_wrong_answer'],
           'actual_final_letters':[x['manual_final_letter'] for x in review['manual_finals']],
           'two_complete':True,'two_hit':review['both_match_frozen_preset'],'manual_review_path':str(folder/'manual_final_review.json'),
           'summary_path':str(inv/'summary.json'),'design_sha256':sha(f),'plugin_sha256':sha(folder/'plugin.json'),
           'image_sha256':sha(folder/'candidate.png')})
        if review['both_match_frozen_preset']:all_candidates.append(rows[-1])
        gc.collect()
    questions[qid]={'status':'PRIMARY_candidate_requires_new_parent_independent_review' if any(r['two_hit'] for r in rows) else 'UNRESOLVED_no_two_hit_primary',
       'correct_answer':next(q['formal_record']['answer'] for q in assignment['questions'] if q['question_id']==qid),
       'new_designs':len(rows),'new_actual_API_calls':len(rows)*2,'trials':rows,
       'mathematical_proof_path':str(OWN/qid/'mathematical_audit.json'),
       'remaining_reason_path':str(OWN/qid/'further_hypotheses_review.json') if (OWN/qid/'further_hypotheses_review.json').exists() else None}
assert len(all_runs)==len(list(OWN.rglob('run_*_started.json')))
queue=read(OWN/'second_review_queue.json');assert len(queue)==len(all_candidates)
write(OWN/'research_report.json',{'finished_at':now(),'unit':'u07_corner_cut','scope':assignment['question_ids'],
 'status':'PRIMARY_RESEARCH_RECORDED; strict candidate goal remains incomplete for unresolved questions',
 'questions':questions,'primary_candidate_count':len(all_candidates),'new_actual_API_calls':len(all_runs),
 'complete_nontruncated_responses':len(all_runs),'API_errors_or_aborts':api_errors,
 'old_actual_API_calls_read_not_repeated':2,'local_offline_errors':read(OWN/'local_errors.json'),
 'all_original_requests_bindings_started_design_snapshots_raw_summaries_and_hashes_preserved':True,
 'all_runs':all_runs,'second_review_queue_path':str(OWN/'second_review_queue.json'),
 'source_preservation_path':str(OWN/'source_preservation_final.json'),
 'limitations':['All results are PRIMARY research only. No independent second review performed.',
 'No user Pass/Collect, formal approval, source modification, publication or delivery.',
 'Off-preset wrong answers and single hits do not meet the exact two-hit criterion.',
 'No old PNG retries, no third call, no selected pair, no changed presets, no model/provider changes.',
 'No overall success-rate or causal-effect claim. All assigned questions were assessed.',
 'No arbitrary three-candidate or quota-saving stop; remaining hypotheses were screened for information value and human uniqueness.'],
 'owned_process_termination_audit':'process_termination_audit.json (written after this process exits)'},True)
write(OWN/'checkpoint.json',{'updated_at':now(),'unit':'u07_corner_cut','status':'PRIMARY_RESEARCH_RECORDED_WITH_EXPLICIT_UNRESOLVED_ITEMS',
 'questions':questions,'new_API_calls':len(all_runs),'complete_nontruncated_responses':len(all_runs),
 'API_errors_or_aborts':[],'primary_candidate_count':len(all_candidates),'second_review_queue_path':str(OWN/'second_review_queue.json'),
 'report_path':str(OWN/'research_report.json'),'source_preserved':True,'formal_approval_Pass_Collect_or_delivery':False,
 'processes':'All API wrappers returned normally; final no-live-owned-Python snapshot follows after finalizer exit.'})
import matplotlib.pyplot as plt
plt.close('all')
print(json.dumps({'questions':{q:{'status':d['status'],'new_calls':d['new_actual_API_calls']} for q,d in questions.items()},
 'new_actual_calls':len(all_runs),'primary_candidates':len(all_candidates),'all_frozen_source_and_old_evidence_preserved':True},ensure_ascii=False))
