from tools13 import *
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
c=read(TASK/'checkpoint.json');q=read(TASK/'second_review_queue.json');a=read(TASK/'source_preservation_audit.json');p=read(TASK/'no_live_processes.json')
assert c['assessed_question_ids']==ASSIGNED and len(set(c['assessed_question_ids']))==20
assert c['saved_design_count']==12 and c['completed_paired_evidence_candidate_count']==9 and c['all_completed_API_call_count']==18
assert c['credible_twohit_possibility_count']==0 and q['candidates']==[]
assert a['all_assigned_source_inputs_unchanged'] and all(r['current_eligibility']['eligible'] for r in a['questions'])
assert a['own_harness_byte_identical_to_shared'] and a['own_adapter_byte_identical_to_shared']
assert p['all_own_api_processes_closed'] and p['launch_count']==p['completion_count']==9 and not p['live_own_api_processes']
for item in c['candidates']:
    for key,pathkey in [('image_sha256','image_path'),('design_sha256','design_path'),('plugin_sha256','plugin_path'),('render_check_sha256','render_check_path')]:
        assert file_hash(ROOT/item[pathkey])==item[key]
    if item['status']=='completed_pair_missed_preset':
        assert len(item['manual_finals'])==2 and not all(item['target_hits'])
        for r in item['manual_finals']:assert r['manually_read_complete_final']
files={str(x.relative_to(TASK)).replace('\\','/'):file_hash(x) for x in sorted(TASK.rglob('*')) if x.is_file() and x.name not in ['evidence_manifest.json','final_verification.json']}
write(TASK/'evidence_manifest.json',{'unit':'background_13','created_at':datetime.now(timezone.utc).isoformat(),'files':files,'note':'Hashes include all own evidence, reports, scripts and caches. The manifest and final_verification exclude themselves to avoid recursive self hashes.'})
write(TASK/'final_verification.json',{'unit':'background_13','verified_at':datetime.now(timezone.utc).isoformat(),'assessed20':True,'saved_designs12':True,'complete_pairs9':True,'complete_calls18':True,'credible_pairs0':True,'source_inputs_unchanged':True,'current_eligibility_all20':True,'same_frozen_PNG_and_pretest_preset_verified_for_all9pairs':True,'all18complete_finals_manually_read':True,'no_live_own_API_processes':True,'no_Pass_Collect_or_publication':True,'no_extra_questions':True,'own_evidence_file_count':len(files),'evidence_manifest_sha256':file_hash(TASK/'evidence_manifest.json'),'final_report_paths':['checkpoint.json','second_review_queue.json','report.txt','assessments.json','candidate_evidence_index.json','source_preservation_audit.json','no_live_processes.json']})
print(json.dumps({'unit':'background_13','assessed':20,'designs':12,'pairs':9,'calls':18,'credible':0,'own_evidence_files':len(files),'all_own_API_processes_closed':True}))
