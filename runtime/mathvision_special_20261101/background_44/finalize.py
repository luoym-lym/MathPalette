import task_env
from task_env import OWN,PROJECT,BASE
from inspect_sources import read,save,sha,eligibility,QIDS
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,base64

def now():return datetime.now(timezone.utc).isoformat()
def canon(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()

manual={
 'Plane415':{'variant':'r44_exposed_radius_to_contact_seam','preset':'10','finals':['10','20'],
     'notes':['Full response ends10cm unambiguously. It also makes incorrect radius and perimeter assumptions; the final alone is a hit, not proof of the proposed seam mechanism.',
              'Full response ends20cm unambiguously. It explicitly excludes the marked central seam, although it misdescribes other exposed rectangle edges. It misses immutable preset10.']},
 'Plane421':{'variant':'r44_unequal_triangle_count_transfer','preset':'C','finals':['B','A'],
     'notes':['Full response endsOptionB=1/2. Its earlier triangle/base counts are inconsistent; the final remains B, not presetC.',
              'Full response repeatedly discusses3/4 and several options but terminal Answer:A is explicit, mapping to2/3. No C hit; incidental1/3 mention is not scored.']},
 'Plane441':{'variant':'r44_total_rise_to_horizontal_run_overlay','preset':'8','finals':['3','12'],
     'notes':['Full response explicitly ends3, despite mentioning an overlap6 earlier. It is not a preset8 hit.',
              'Full response ends y=12, after incorrect step/repositioning coordinates. It is not a preset8 hit. Both wrong outputs remain misses and are not relabeled.']}
}

finals=[];bindings=[]
for qid,m in manual.items():
    folder=OWN/qid/m['variant']; invocations=list((folder/'tests').iterdir());assert len(invocations)==1
    d=invocations[0];b=read(d/'binding.json');summary=read(d/'summary.json');request=read(d/'request.json')
    design=read(folder/'design.json');row=eligibility(qid)['formal_record']
    assert b['requested_runs']==2 and b['expected_wrong_answer']==m['preset']==design['expected_wrong_answer']
    assert summary['two_completed'] and len(summary['results'])==2
    assert sha(folder/'design.json')==sha(d/'design_snapshot.json')==b['design_sha256']
    assert sha(folder/'candidate.png')==b['image_sha256']
    assert sha(d/'request.json')==b['request_body_sha256']
    assert canon(row)==b['question_record_sha256']
    assert b['question']==row['question']
    assert b['reference_quick_test_sha256']==sha(PROJECT/'PlaneGeometry/workbench/quick_test.py')
    assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert request['messages'][0]=={'role':'system','content':b['system_prompt']}
    user=request['messages'][1];assert user['role']=='user' and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':row['question']}
    encoded=user['content'][1]['image_url']['url']
    assert encoded.startswith('data:image/png;base64,')
    assert base64.b64decode(encoded.split(',',1)[1])==(folder/'candidate.png').read_bytes()
    assert len(request['messages'])==2
    runreviews=[]
    for i,(answer,note) in enumerate(zip(m['finals'],m['notes']),1):
        job=read(d/f'run_{i:02d}.json');raw=read(d/f'run_{i:02d}_response.json')
        body=raw['choices'][0]['message']['content']
        assert job['status']=='completed' and job['finish_reason']=='stop' and not job['truncated']
        assert raw['choices'][0]['finish_reason']=='stop'
        assert body==job['answer']
        assert job['response_sha256']==sha(d/f'run_{i:02d}_response.json')
        assert job['request_body_sha256']==b['request_body_sha256']
        assert job['image_sha256']==b['image_sha256'] and job['design_sha256']==b['design_sha256']
        assert raw['model']=='mimo-v2.6-flash'
        runreviews.append({'run_index':i,'complete_final_body':body,'entire_raw_response_manually_read':True,
            'manual_terminal_answer':answer,'predeclared_preset_hit':answer==m['preset'],'manual_note':note,
            'run_started_at_utc':job['started_at'],'run_finished_at_utc':job['finished_at'],
            'provider_finish_reason':'stop','truncated':False,
            'raw_response_path':str(d/f'run_{i:02d}_response.json'),'raw_response_sha256':sha(d/f'run_{i:02d}_response.json'),
            'job_path':str(d/f'run_{i:02d}.json'),'job_sha256':sha(d/f'run_{i:02d}.json')})
    review={'question_id':qid,'variant_id':m['variant'],'reviewed_at_utc':now(),'frozen_expected_wrong_answer':m['preset'],
        'formal_correct_answer':row['answer'],'manual_terminal_answers':m['finals'],'full_manual_reviews':runreviews,
        'two_predeclared_target_hits':all(r['predeclared_preset_hit'] for r in runreviews),
        'exactly_two_real_calls':True,'same_frozen_design_image_request_both_calls':True,
        'source_record_and_approval_current':True,'solver_input_only_formal_question_and_candidate_PNG':True,
        'correct_answer_intent_preset_plugin_original_control_never_solver_input':True,
        'profile_thinking_system_prompt_preserved':True,'no_token_limit_timeout_override_or_retry':True,
        'design_path':str(folder/'design.json'),'design_sha256':b['design_sha256'],
        'image_path':str(folder/'candidate.png'),'image_sha256':b['image_sha256'],'pixel_sha256':b['pixel_sha256'],
        'request_path':str(d/'request.json'),'request_sha256':b['request_body_sha256'],
        'binding_path':str(d/'binding.json'),'binding_sha256':sha(d/'binding.json'),
        'summary_path':str(d/'summary.json'),'summary_sha256':sha(d/'summary.json'),
        'plugin_path':str(folder/'plugin.json'),'plugin_sha256':sha(folder/'plugin.json'),
        'primary_math_path':str(OWN/qid/'primary_math_audit.json'),
        'native_marker_review_path':str(folder/'primary_review_before_calls.json'),
        'material_difference_path':str(folder/'design_difference_audit.json'),
        'original_controls':'No original control binding found for this question; old annotated attempts are not controls. No new control or repeated control calls.',
        'outcome':'MISS_IMMUTABLE_PAIR; retain evidence; no independent-review queue entry',
        'limits':'Two observations do not prove a mechanism, causation, incremental benefit, statistical gain or per-marker contribution; narratives need not match the primary hypothesis. No gain or identical-narrative gate was added.',
        'approval_status':'RESEARCH_ONLY; no Pass/Collect/approval/publication'}
    save(folder/'manual_finals_and_binding_audit.json',review)
    e=eligibility(qid);assert e['eligible'];save(folder/'eligibility_after_calls.json',e)
    save(OWN/qid/'material_refinement_assessment.json',{'question_id':qid,'stage':'material_refinement',
         'status':'assessed_one_material_new_design_tested_pair_missed','new_designs':1,'API_calls':2,
         'variant_id':m['variant'],'new_vs_old':read(folder/'design_difference_audit.json')['material_difference'],
         'expected_wrong_answer':m['preset'],'manual_final_answers':m['finals'],'two_hits':False,
         'full_binding_review_path':str(folder/'manual_finals_and_binding_audit.json'),
         'math_proof_path':str(OWN/qid/'primary_math_audit.json'),'primary_marker_review':str(folder/'primary_review_before_calls.json')})
    finals.append({'question_id':qid,'variant_id':m['variant'],'preset':m['preset'],'manual_finals':m['finals'],
                   'pair_hits':review['two_predeclared_target_hits'],'review_path':str(folder/'manual_finals_and_binding_audit.json')})
    bindings.append(review)
save(OWN/'evidence_binding_audit.json',{'created_at_utc':now(),'all3_pairs_exactly_bound':True,'actual_calls':6,'completed_calls':6,'pairs':bindings})

# Match own harness to the shared harness with only the documented isolation changes.
ha=read(OWN/'harness_isolation_audit.json');s=Path(ha['source_path']).read_text(encoding='utf-8')
assert sha(ha['source_path'])==ha['source_sha256']
s=s.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
s=s.replace('RUNTIME = (PROJECT / "runtime").resolve()','RUNTIME = Path(__file__).resolve().parents[1]')
s=s.replace('from __future__ import annotations\n','from __future__ import annotations\n\nimport sys as _sys\nfrom pathlib import Path as _Path\n_sys.path.insert(0,str(_Path(__file__).resolve().parents[1]))\nimport task_env\n',1)
assert s==(OWN/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')

# Preserve only tracked source/evidence claims, without attributing unrelated workspace drift.
tracked=read(OWN/'preservation_start.json')
hist=read(OWN/'old_history_audit.json')
for q,v in hist.items():
    for x in v['initial_checkpoint_and_root_history']:tracked[x['path']]=x['sha256']
refs=read(OWN/'delivered_reference_study.json')
for r in refs:
    tracked[str(BASE/r['batch']/'manifest.json')]=r['manifest_sha256']
    for d in r['designs']:tracked[d['path']]=d['sha256']
checks={p:{'recorded':h,'current':sha(p) if Path(p).is_file() else None} for p,h in tracked.items()}
changed={p:v for p,v in checks.items() if v['recorded']!=v['current']}
assert not changed,changed
eligs={q:eligibility(q) for q in QIDS};assert all(e['eligible'] for e in eligs.values())
save(OWN/'eligibility_final.json',eligs)
save(OWN/'source_preservation_final.json',{'checked_at_utc':now(),'tracked_source_and_old_evidence_count':len(checks),
      'all_tracked_hashes_match':not changed,'changes':changed,'files':checks,
      'current_original_content_fingerprints':{q:eligs[q]['computed_content_sha256']for q in QIDS},
      'all8_original_user_approvals_match':True,'all8_current_MathVision_noPass_noCollect_noSpecialCompletion':True,
      'historical_mutable_progress_metadata':'Read as diagnostics and preserved; historical snapshots not rewritten to match current parent metadata.',
      'scope':'Only individually tracked relevant sources and old evidence; no claim entire shared workspace stayed unchanged.',
      'strict_own_write_guard_before_project_imports':True,'formal_sources_approvals_env_git_old_runtime_helpers_main_ledger_written':False})

# Inventory all runtime binding.json records for these8 IDs to reuse any existing controls.
old_bindings=[];malformed=[]
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(OWN):continue
    try:b=read(p)
    except Exception as e:
        # Only disclose malformed binding files that actually mention an assigned ID.
        raw=p.read_bytes()
        if any(q.encode() in raw for q in QIDS):malformed.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'error':str(e),'not_repaired':True})
        continue
    if b.get('question_id') in QIDS:
        old_bindings.append({'path':str(p),'sha256':sha(p),'question_id':b['question_id'],
          'image_path':b.get('image_path'),'design_path':b.get('design_path'),'expected_wrong_answer':b.get('expected_wrong_answer')})
save(OWN/'old_bindings_and_controls.json',{'old_bindings':old_bindings,'malformed_relevant_binding_JSON':malformed,
     'new_original_control_calls':0,'known_existing_original_controls':[],
     'finding':'Only4 old annotated candidate bindings (Plane415 one, Plane421 two, Plane443 one), all full responses read; no original-control binding for these8 IDs found. Old summary pending flags did not suppress these8 old actual responses.'})
assert len(old_bindings)==4
proc=read(OWN/'process_audit_final.json');assert proc['all_owned_api_processes_closed']
queue={'stage':'material_refinement','unit':'background_44','created_at_utc':now(),'candidates':[],
       'candidate_count':0,'reason':'No new frozen design reached its own immutable preset on both calls.',
       'NEW_independent_second_review_required_before_delivery':True,'no_delivery_or_approval':True}
save(OWN/'second_review_queue.json',queue)
assessments={q:read(OWN/q/'material_refinement_assessment.json')for q in QIDS}
checkpoint={'unit':'background_44','stage':'material_refinement','status':'completed_finite_assigned_scope',
    'completed_at_utc':now(),'stop_reason':'All8 assigned questions assessed with actual sources/full questions/frozen scenes/history/independent math and reasonable mechanisms;5 had no clean new design. No quota/cost stop.',
    'assigned_question_ids':QIDS,'actual_assessed_question_ids':QIDS,'unworked_question_ids':[],
    'assessed_question_count':8,'material_new_design_count':3,'tested_frozen_design_count':3,
    'actual_API_calls':6,'completed_API_calls':6,'candidate_pair_count':3,'credible_possible_candidates':0,
    'complete_pair_outcomes':finals,'question_assessments':assessments,
    'offline_failures':[{'question_id':'Plane441','kind':'partial_path_object_changed_before_any_API_or_frozen_PNG','evidence_path':str(OWN/'Plane441/r44_total_rise_to_horizontal_run/offline_error.json'),
                         'resolution':'Exact existing-side overlay implementation of the same hypothesis, separately frozen before testing. No adapter edit; no API retry.'}],
    'API_errors':[],'API_aborts':[],'API_retries':0,'posthoc_preset_changes':0,
    'relevant_historical_malformed_JSON':malformed,'old_history_audit':str(OWN/'old_history_audit.json'),
    'source_and_qualification_audit':str(OWN/'source_preservation_final.json'),
    'full_raw_frozen_bindings_and_manual_finals':str(OWN/'evidence_binding_audit.json'),
    'primary_math_all8':'Each question primary_math_audit.json; Plane414 also full exact-cover certificate.',
    'native_marker_reviews':'Each tested design primary_review_before_calls.json includes every mark and per-group targeting/validity/conciseness/semantics.',
    'process_audit':str(OWN/'process_audit_final.json'),'owned_API_pids':proc['owned_api_pids'],'all_owned_API_processes_closed':True,
    'second_review_queue':str(OWN/'second_review_queue.json'),'source_preservation_verified_count':len(checks),
    'all_writes_within':str(OWN),'formal_approval_Pass_Collect_publish_actions':0,
    'statistical_causal_mechanism_claim':'None;6 complete observations only. Existing misses never relabeled and old controls not repeated.'}
save(OWN/'checkpoint.json',checkpoint)
manifest={str(p.relative_to(OWN)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in OWN.rglob('*')
          if p.is_file() and not any(x in p.relative_to(OWN).parts for x in ['cache','tmp','mpl_cache','render_tmp']) and p.name!='evidence_manifest.json'}
save(OWN/'evidence_manifest.json',{'created_at_utc':now(),'files':manifest,'excluded_runtime_caches':['cache','tmp','mpl_cache','render_tmp'],'all_outputs_confined_to_own_root':True})
print(json.dumps({'assessed':8,'designs':3,'calls':6,'completed':6,'possible_candidates':0,
                  'API_errors':0,'API_aborts':0,'offline_render_failure_resolved':1,
                  'tracked_unchanged_sources_and_old_evidence':len(checks),'all_API_processes_closed':True,
                  'checkpoint':str(OWN/'checkpoint.json'),'second_review_queue':str(OWN/'second_review_queue.json')},ensure_ascii=False))
