from tools26 import *
import base64
manual=read(HERE/'manual_new_finals.json')
process=read(HERE/'process_audit_verified.json');assert not process['live_own_python_processes']
cfg,ad=adapter();audits=[];queue=[];source_checks={};old_checks={};hash_cache={};total_calls=0
def current_hash(rel):
    if rel not in hash_cache:
        p=ROOT/rel;hash_cache[rel]=file_hash(p) if p.exists() else None
    return hash_cache[rel]
for q in ASSIGNED:
    ck=eligibility(q);assert ck['eligible'],ck
    write(HERE/q/'eligibility_final.json',ck)
    initial=read(HERE/q/'input_fingerprints.json');rec=ck['formal_record'];br=ROOT/'PlaneGeometry'
    relevant={str((br/rec[k]).relative_to(ROOT)) for k in ['image','original_image','scene','script'] if rec.get(k)}
    relevant.update(str((br/p).relative_to(ROOT)) for p in rec.get('runtime_dependencies',[]))
    relevant.update(str((ROOT/p).relative_to(ROOT)) for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','dataset_tools/mathvision_workbench.py','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/common_renderer.py','PlaneGeometry/dataset_generator/protocol.json'])
    relevant.update(rel for rel in initial['files'] if str(Path(rel)).replace('\\','/').startswith('PlaneGeometry/workbench/'))
    changed=[{'path':rel,'historical_start_sha256':sha,'current_sha256':current_hash(rel),'relevant_to_assigned_original_or_renderer':rel in relevant} for rel,sha in initial['files'].items() if current_hash(rel)!=sha]
    critical=[c for c in changed if c['relevant_to_assigned_original_or_renderer']]
    assert not critical,(q,critical)
    assert initial['question_record_sha256']==canonical_hash(rec)
    start=read(HERE/q/'eligibility_start.json')
    metadata=[{'path':rel,'historical_start_sha256':sha,'current_sha256':file_hash(ROOT/rel),'changed':sha!=file_hash(ROOT/rel),'classification':'mutable runtime progress metadata; diagnostic, not frozen original or approval'} for rel,sha in start['diagnostic_runtime_metadata_hashes'].items()]
    source_checks[q]={'formal_record_hash_unchanged':True,'current_approval_fingerprint_matches':ck['approval_fingerprint_matches'],'current_noPass_notCollected_noSpecialCompletion':ck['eligible'],'relevant_assigned_source_and_renderer_changed':critical,'other_full_adapter_manifest_drift_preserved':changed,'diagnostic_progress_drift':metadata,'no_restore_or_baseline_rewrite':True}
    old=read(HERE/q/'prior_history_audit.json');mismatches=[]
    for rel,sha in old['old_evidence_file_sha256'].items():
        if current_hash(rel)!=sha:mismatches.append({'path':rel,'old':sha,'current':current_hash(rel)})
    assert not mismatches
    old_checks[q]={'old_design_count':len(old['history']),'old_frozen_evidence_hashes_checked':len(old['old_evidence_file_sha256']),'changed':mismatches,'old_presets_not_relabelled':True}
    for dp in sorted((HERE/q).glob('r26_*/design.json')):
        out=dp.parent;d=read(dp);key=q+'/'+d['variant_id'];man=manual[key]
        assert len(man['final_answers'])==2 and man['both_complete_finals_manually_read']
        summaries=list(out.glob('tests/*/summary.json'));assert len(summaries)==1
        summary=read(summaries[0]);inv=summaries[0].parent;b=read(inv/'binding.json')
        assert summary['two_completed'] and len(summary['results'])==2
        assert (inv/'design_snapshot.json').read_bytes()==dp.read_bytes()
        assert b['design_sha256']==file_hash(dp) and b['image_sha256']==file_hash(out/'candidate.png')
        assert (out/'repeat.png').read_bytes()==(out/'candidate.png').read_bytes()
        req=read(inv/'request.json');assert b['request_body_sha256']==file_hash(inv/'request.json')
        assert set(req)=={'model','stream','thinking','messages'} and req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False
        assert len(req['messages'])==2 and req['messages'][0]['role']=='system' and req['messages'][1]['role']=='user'
        assert req['messages'][0]['content']==b['system_prompt']
        uc=req['messages'][1]['content'];assert len(uc)==2 and uc[0]=={'type':'text','text':rec['question']}
        assert base64.b64decode(uc[1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
        assert b['expected_wrong_answer']==d['expected_wrong_answer'] and b['question']==rec['question'] and b['question_record_sha256']==canonical_hash(rec)
        assert b['reference_quick_test_sha256']==file_hash(br/'workbench/quick_test.py')
        full=[]
        for i,job in enumerate(summary['results'],1):
            rp=inv/f'run_{i:02d}_response.json';raw=read(rp);assert job['status']=='completed' and job['response_sha256']==file_hash(rp)
            assert job['request_body_sha256']==b['request_body_sha256'] and job['image_sha256']==b['image_sha256'] and job['design_sha256']==b['design_sha256']
            assert raw['choices'][0]['finish_reason']=='stop';text_content=raw['choices'][0]['message']['content'];assert text_content.strip()
            full.append({'run_index':i,'manually_assessed_final_answer':man['final_answers'][i-1],'full_final_content':text_content,'raw_response_path':str(rp.relative_to(ROOT)),'raw_response_sha256':file_hash(rp),'finish_reason':'stop','request_body_sha256':job['request_body_sha256'],'image_sha256':job['image_sha256'],'design_sha256':job['design_sha256']})
        total_calls+=2;hits=[str(x)==str(d['expected_wrong_answer']) for x in man['final_answers']]
        pair=all(hits) and not man.get('inconsistent_final_letter_value_pair',False)
        review={'stage':'material_refinement','question_id':q,'variant_id':d['variant_id'],'review_role':'PRIMARY_AUTHOR_ONLY_NOT_INDEPENDENT','reviewed_at':now(),'frozen_expected_wrong_answer':d['expected_wrong_answer'],'correct_answer':d['correct_answer'],'manual_final_answers':man['final_answers'],'both_complete_finals_manually_read':True,'final_interpretation_notes':man['notes'],'hits_own_unchanged_preset':hits,'credible_primary_two_hit_candidate':pair,'raw_full_final_bindings':full,'evidence_binding_all_checks_passed':True,'pre_call_native_math_marker_review':str((out/'primary_review_before_calls.json').relative_to(ROOT)),'pre_call_native_math_marker_review_sha256':file_hash(out/'primary_review_before_calls.json'),'math_proof':str((out/'math_proof.json').relative_to(ROOT)),'math_proof_sha256':file_hash(out/'math_proof.json'),'marker_bindings':str((out/'marker_bindings.json').relative_to(ROOT)),'marker_bindings_sha256':file_hash(out/'marker_bindings.json'),'design_difference_audit':read(out/'design_difference_audit.json'),'frozen_binding':b,'exact_request_path':str((inv/'request.json').relative_to(ROOT)),'no_original_control_retests':True,'limits':['Finite two-call observation only; no causal, statistical, human-performance or per-marker effectiveness claim.','Native original small features remain a display limitation.','Any eventual delivery requires a NEW parent independent second-review task; this primary review is insufficient.'],'status':'QUEUE_FOR_NEW_PARENT_REVIEW' if pair else 'MISS_NO_RETEST_OR_POSTHOC_PRESET_CHANGE'}
        write(out/'primary_review.json',review)
        item={'question_id':q,'variant_id':d['variant_id'],'candidate':str(out.relative_to(ROOT)),'preset':d['expected_wrong_answer'],'final_answers':man['final_answers'],'credible_two_hit':pair,'design_difference':d['design_difference'],'binding':str((inv/'binding.json').relative_to(ROOT)),'exact_request':str((inv/'request.json').relative_to(ROOT)),'summary':str(summaries[0].relative_to(ROOT)),'primary_review':str((out/'primary_review.json').relative_to(ROOT)),'image_sha256':b['image_sha256'],'design_sha256':b['design_sha256']}
        audits.append(item)
        if pair:queue.append({**item,'stage':'material_refinement','parent_NEW_independent_second_review_required':True,'not_delivered_or_approved':True})
write(HERE/'source_preservation_audit.json',{'created_at':now(),'stage':'material_refinement','per_question':source_checks,'own_scope_write_guard':ISOLATION,'own_additional_guard_root':str(HERE),'formal_workbench_approvals_env_runtime_dotgit_readonly':True,'whole_workspace_unchanged_not_claimed':True,'concurrent_unrelated_changes_preserved':True})
write(HERE/'old_evidence_preservation_audit.json',{'created_at':now(),'per_question':old_checks,'all_checked_old_files_unchanged':True})
assessment_reasons={
'Plane175':'No new human-clear targeted correspondence beyond six old notch/contour variants; small-square-to-E approximate-size idea and D long-side idea rejected before rendering/calls. See material_refinement_prescreen.json.',
'Plane198':'Central three-cell identity-copy hypothesis tested after old compressed run mapping. Further selective complement-cell or run variants offer no clear new grouping beyond these; do not retarget its observed E/D outputs.',
'Plane223':'Upper three-solid-dot cluster was a new grouping beyond old large-dot/annulus metric pair. Further count-deficient options would require disregarding intact source spots, and ring/palette variants repeat existing partial correspondence; no additional concise clear hypothesis found.',
'Plane252':'Tested actual five-edge/six-joint metric error and current-direction orientation lock, after old incompatible-overlap sum and four-edge U. Further selected-arm/point recolorings repeat those hypotheses; do not set8 from repeated hallucinated8 responses.',
'Plane282':'Tested three actual row-strip open-frame grouping after old full-seam and short-shoulder hypotheses. Further row/edge color variants would repeat these or add artificial partitions; none is called.',
'Plane408':'Tested external-step total variation and internal-contact single-count errors after old conserved-ribbon-identity design. These independently cover endpoint omission, two-side cancellation, and identity conservation; no cosmetic retargeting to observed0/75.',
'Plane446':'Square skeleton and tail classes already tested; new asymmetric coloring would change the symmetry-count target and subset edges/added axes offer no clear new legal misconception. See prescreen.',
'Plane461':'Tested free-top-edge-as-fold alias after old left-fold-as-outer-edge punch mapping. Combining their cues into E repeats those fold-role errors without a new feature hypothesis; no extra calls.'}
for q in ASSIGNED:
    write(HERE/q/'refinement_assessment.json',{'stage':'material_refinement','question_id':q,'assessed':True,'new_design_count':sum(a['question_id']==q for a in audits),'new_completed_calls':2*sum(a['question_id']==q for a in audits),'credible_candidates':[a['variant_id'] for a in audits if a['question_id']==q and a['credible_two_hit']],'reasonable_meaningful_hypotheses_exhausted_for_this_checkpoint':True,'reason':assessment_reasons[q],'no_unfinished_questions_or_extra_ids_used':True})
write(HERE/'second_review_queue.json',{'stage':'material_refinement','unit':'background_26','created_at':now(),'candidates':queue,'candidate_count':len(queue),'parent_NEW_independent_review_required_for_every_eventual_delivery':True,'no_delivery_Pass_Collect_or_publication':True})
checkpoint={'stage':'material_refinement','unit':'background_26','status':'finite_review_checkpoint_complete','created_at':now(),'stop_reason':'All eight assigned refinement questions assessed; reasonable materially distinct human-clear hypotheses exhausted. No quota/cost stop.','assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'saved_new_designs':len(audits),'complete_candidate_pairs':len(audits),'actual_completed_api_calls':total_calls,'api_errors':0,'api_aborts':0,'api_retries':0,'new_original_control_calls':0,'credible_primary_candidate_count':len(queue),'candidates':audits,'all_old_new_differences_in_each_candidate_audit':True,'all_complete_finals_manually_read_and_saved':True,'old_design_count':sum(x['old_design_count'] for x in old_checks.values()),'old_already_double_hit_promotions':0,'old_all_presets_unchanged':True,'precall_rejections':['Plane175','Plane446'],'setup_failures':[{'stage':'initial_context_path_serialization','question_id':'Plane175','error':'TypeError ndarray; a second attempt reached TypeError Polygon artist. No API call involved. Partial diagnostics preserved at paths.json and paths_full.json. Serializable exact workbench path descriptions saved separately at paths_frozen.json.','diagnostic_artifacts_preserved':True}],'process_audit_path':str((HERE/'process_audit_verified.json').relative_to(ROOT)),'all_own_API_processes_finished':True,'live_own_API_processes':[],'source_preservation_audit':str((HERE/'source_preservation_audit.json').relative_to(ROOT)),'old_evidence_preservation_audit':str((HERE/'old_evidence_preservation_audit.json').relative_to(ROOT)),'second_review_queue':str((HERE/'second_review_queue.json').relative_to(ROOT)),'all_new_outputs_below_own_root':str(HERE),'no_formal_or_old_evidence_writes':True,'mutable_runtime_progress_hash_drift_classified_separately':True,'parent_NEW_independent_second_review_required_before_delivery':True,'limitations':['Two observations per frozen image do not establish causal/statistical effectiveness.','No human study, marker ablation or fresh original controls.','All history remains intact. Small native features/display limits disclosed in primary reviews.']}
write(HERE/'checkpoint.json',checkpoint)
write(HERE/'completion_manifest.json',{'stage':'material_refinement','created_at':now(),'checkpoint_sha256':file_hash(HERE/'checkpoint.json'),'second_review_queue_sha256':file_hash(HERE/'second_review_queue.json'),'new_designs':len(audits),'new_complete_calls':total_calls,'credible_candidates':len(queue),'all_own_processes_finished':True,'preservation_checks_passed':True})
print(json.dumps({'assessed':len(ASSIGNED),'new_designs':len(audits),'completed_calls':total_calls,'credible':len(queue),'unworked':[],'checkpoint':str(HERE/'checkpoint.json')}),flush=True)
