import tools_local as t
import base64
def read(p):return t.json.loads(p.read_text(encoding='utf-8-sig'))
manual={
'Plane171':(['D','D'],['Final D explicitly, despite hallucinated internal regions and dots. Preset C miss.','Final D explicitly; incorrect convexity/perimeter account. Preset C miss.']),
'Plane278':(['INCONSISTENT: verbal C, terminal A','D'],['Verbal conclusion selects C but final standalone A conflicts; neither is preset E. Do not infer a clean final from incidental letters.','Final D:D explicitly, preset E miss.']),
'Plane286':(['D','C'],['Final D explicitly, misses preset C.','Final C explicitly, one preset C hit; the pair fails. Narrative permits cutting that original gluing task does not permit.']),
'Plane289':(['19','6'],['Final19 from incorrectly counted6 and nonminimal side5; preset12 miss.','Final6 from misread3 supplied and side3; preset12 miss.']),
'Plane307':(['17','21'],['Final17 from a faulty orbit closure; preset9 miss.','Final21 with all three disjoint8-cell orbits; correct answer, preset9 miss.'])}
manifest=read(t.HERE/'old_history_corrected_manifest.json');preservation={};sources={};eligible={};candidates=[];queue=[];calls_started=0;calls_completed=0;aborts=[]
cfg,ad=t.adapter()
for q in t.ASSIGNED:
    eligible[q]=t.eligibility(q);assert eligible[q]['eligible'],eligible[q]
    t.write(t.HERE/q/'eligibility_finish.json',eligible[q])
    before=read(t.HERE/q/'input_fingerprints.json');after=t.inputs(ad,q)
    # Mutable dataset-wide manifest/progress hashes never substitute for question inputs.
    diff=[p for p,h in before['files'].items() if after['files'].get(p)!=h]
    assert not diff and before['question_record_sha256']==after['question_record_sha256']
    sources[q]={'source_files_checked':len(before['files']),'question_record_unchanged':True,'all_relevant_input_files_unchanged':True,'changed_files':diff,'original_approval_matches':True}
    old=manifest[q]['files'];changed=[p for p,h in old.items() if not(t.ROOT/p).is_file() or t.file_hash(t.ROOT/p)!=h];assert not changed
    pngs=[]
    for p in old:
        if p.endswith('.png'):
            pp=t.ROOT/p;digest=t.pixel_hash(pp)
            reps=[str(a.relative_to(t.ROOT)) for a in [t.HERE/q/'original.png',*list((t.BASE/'plane_explore'/q).glob('*/candidate.png')),*list(t.BASE.glob('background_*/'+q+'/*/candidate.png'))] if a.exists() and t.pixel_hash(a)==digest]
            pngs.append({'path':p,'png_sha256':old[p],'pixel_sha256':digest,'same_pixels_as_native_viewed_representative':reps})
    preservation[q]={'old_files_verified':len(old),'changed_or_missing':changed,'old_png_equivalence_audit':pngs,'old_independent_review_reports':manifest[q]['independent_review_reports'],'immutable_history_preserved':True}
    for des in (t.HERE/q).glob('r30_*/design.json'):
        out=des.parent;d=read(des);n=d['variant_id'];dirs=list((out/'tests').glob('quicktest3_*'));assert len(dirs)==1
        test=dirs[0];binding=read(test/'binding.json');request=read(test/'request.json')
        assert binding['requested_runs']==2 and binding['expected_wrong_answer']==d['expected_wrong_answer']
        assert binding['design_sha256']==t.file_hash(des)==t.file_hash(test/'design_snapshot.json')
        assert binding['image_sha256']==t.file_hash(out/'candidate.png')
        assert binding['request_body_sha256']==t.file_hash(test/'request.json')
        assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
        assert set(request)=={'model','stream','thinking','messages'} and len(request['messages'])==2
        user=request['messages'][1];assert user['role']=='user' and len(user['content'])==2
        assert user['content'][0]=={'type':'text','text':ad.records[q]['question']}
        assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
        starts=list(test.glob('run_*_started.json'));jobs=sorted(p for p in test.glob('run_*.json') if not p.name.endswith(('_started.json','_response.json')))
        completed=[read(p) for p in jobs if read(p).get('status')=='completed'];calls_started+=len(starts);calls_completed+=len(completed)
        summary=test/'summary.json';pair=summary.exists() and read(summary)['two_completed']
        finals=[];hit=False
        if pair:
            assert len(starts)==2 and len(completed)==2
            assert q in manual,'Read complete new replies and explicitly enter manual adjudication first.'
            values,notes=manual[q]
            for i in range(1,3):
                rawp=test/f'run_{i:02d}_response.json';raw=read(rawp);body=raw['choices'][0]['message']['content']
                assert raw['choices'][0]['finish_reason']=='stop'
                assert completed[i-1]['response_sha256']==t.file_hash(rawp)
                finals.append({'run_index':i,'full_model_final_body':body,'complete_final_manually_read':True,'manual_final':values[i-1],'matches_immutable_preset':values[i-1]==str(d['expected_wrong_answer']),'manual_note':notes[i-1],'raw_response_path':str(rawp),'raw_response_sha256':t.file_hash(rawp)})
            hit=all(f['matches_immutable_preset'] for f in finals)
            status='PRIMARY possible double hit pending NEW parent independent review' if hit else 'complete_pair_preset_missed'
        else:
            abort=out/'aborted_call.json';assert abort.exists(),'Pending API process prevents final checkpoint.'
            aborted=read(abort);aborts.append(aborted);status='aborted_incomplete_pair_no_credit'
        record={'question_id':q,'variant_id':n,'stage':'material_refinement','status':status,'correct_formal_answer':ad.records[q]['answer'],'expected_wrong_answer_predeclared':d['expected_wrong_answer'],'actual_completed_calls':len(completed),'actual_started_calls':len(starts),'full_manual_finals':finals,'exact_two_completed_same_frozen_png':pair,'pretest_difference_audit':str(out/'design_difference_audit.json'),'old_new_difference':read(out/'design_difference_audit.json')['substantive_old_new_difference'],'immutable_bindings':binding,'binding_file':str(test/'binding.json'),'request_file':str(test/'request.json'),'candidate_image':str(out/'candidate.png'),'plugin':str(out/'plugin.json'),'math_audit':str(t.HERE/q/'primary_math_audit.json'),'marker_audit':str(out/'per_marker_geometry_audit.json'),'native_visual_review':read(out/'primary_visual.json'),'render_check':read(out/'render_check.json'),'API_profile_or_timeout_overrides':False,'retries':0,'original_controls':[],'limits':['No original controls exist for these old attempts; none repeated.','No statistical/human/causal/per-marker study, no equal-narrative or correct-control hard gate.','Primary review only; parent NEW independent review required before any eventual delivery.']}
        t.write(out/'manual_final_review.json',record)
        t.write(out/'primary_review.json',{'review_level':'PRIMARY ONLY','question_id':q,'variant_id':n,'unique_math':read(t.HERE/q/'primary_math_audit.json'),'per_marker_geometry':read(out/'per_marker_geometry_audit.json'),'native_visual':record['native_visual_review'],'render':record['render_check'],'observed_disposition':status,'manual_final_review_path':str(out/'manual_final_review.json'),'new_independent_review_required_before_delivery':True,'approval_recorded':False})
        candidates.append(record)
        if hit:queue.append({'question_id':q,'variant_id':n,'candidate_path':str(out),'review_required':'NEW parent independent review; no old review reuse; no self approval','primary_review':str(out/'primary_review.json'),'manual_finals':str(out/'manual_final_review.json')})
        t.write(t.HERE/q/'refinement_assessment.json',{'stage':'material_refinement','question_id':q,'assessed_at':t.now(),'hypothesis_materially_distinct':True,'tested_variant':n,'status':status,'possible_primary_double_hit':hit,'remaining_hypothesis_assessment':'Other corner/notch/width pairings repeat the same mistaken binding class or require an internal forced partition, extra guide or asymmetric counting-target change. No clean further materially distinct concise hypothesis retained; do not change this preset or repeat this image.','not_quota_or_cost_limited':True})
t.write(t.HERE/'source_preservation_final.json',{'question_frozen_sources':sources,'old_same_question_evidence':preservation,'scope':'Relevant original source/dependencies and old same-question evidence only. Unrelated concurrent human workbench activity preserved, never restored. Historical mutable exploration_report/remaining_questions hashes are diagnostic, not frozen source.','writes_only_own_runtime_guard':True,'formal_approvals_Pass_Collect_or_publication_actions':0})
t.write(t.HERE/'evidence_binding_audit.json',{'stage':'material_refinement','all_new_candidate_bindings_verified':True,'candidates':candidates,'harness_byte_identical':t.file_hash(t.HERE/'quicktest3_isolated.py')==t.file_hash(t.BASE/'harness/quicktest3_isolated.py'),'started_calls':calls_started,'completed_calls':calls_completed,'aborts':aborts,'API_retries':0,'no_success_selection_from_larger_samples':True})
t.write(t.HERE/'second_review_queue.json',{'stage':'material_refinement','unit':'background_30','primary_only':True,'new_independent_parent_review_mandatory':True,'candidates':queue})
t.write(t.HERE/'checkpoint.json',{'unit':'background_30','stage':'material_refinement','status':'finite_checkpoint_complete','finished_at':t.now(),'assigned_question_ids':t.ASSIGNED,'actual_assessed_question_ids':t.ASSIGNED,'assessed_question_ids':t.ASSIGNED,'unworked_question_ids':[],'new_design_count':len(candidates),'actual_API_calls_started':calls_started,'completed_calls':calls_completed,'complete_pairs':sum(r['exact_two_completed_same_frozen_png'] for r in candidates),'aborted_call_count':len(aborts),'retries':0,'credible_primary_possible_double_hits':len(queue),'candidate_ids':[r['question_id']+'/'+r['variant_id'] for r in queue],'screened_without_calls':['Plane244','Plane349'],'stop_reason':'All eight assigned questions assessed with materially different hypotheses or explicit no-clean-hypothesis screening; own API lifecycle finalized.','evidence_binding_audit':str(t.HERE/'evidence_binding_audit.json'),'source_preservation':str(t.HERE/'source_preservation_final.json'),'second_review_queue':str(t.HERE/'second_review_queue.json'),'all_old_new_differences':{r['question_id']:r['old_new_difference'] for r in candidates},'failures_and_aborts':aborts,'local_proof_development_note':str(t.HERE/'proof_development_note.json'),'formal_changes':False,'approval_Pass_Collect_delivery_publication_actions':0,'new_independent_parent_review_required_before_delivery':True,'no_live_own_API_processes':'Confirmed separately in final_process_check.json; do not infer from this string.'})
print(t.json.dumps({'assessed':8,'designs':len(candidates),'started':calls_started,'completed':calls_completed,'pairs':sum(r['exact_two_completed_same_frozen_png'] for r in candidates),'aborts':len(aborts),'queue':len(queue)}))
