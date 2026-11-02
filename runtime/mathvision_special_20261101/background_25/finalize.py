from design_tools import *
import base64

# These are manual readings of BOTH COMPLETE finals, never regex hits or snippets.
FINAL_READINGS={
 'Solid95':(['0','0'],['Final0 after hallucinating25height4pillars on25basecells. Explicitly concludesnogaps; frozen55missed.','Final0 after treatingall25basepositions asfullheightpillars. Mentionsredtopandbluebottom, butdoesnotgive55.']),
 'Solid170':(['E','D'],['Fullconclusion selectsChoiceE after flatteningopenings intointerioroppositefaceholes. OnepresetEhit.','OpenswithcorrectnetD and consistentlyselectsD. Eonlyoccursasarejectedoption; noEfinal.']),
 'Solid111':(['D','C'],['UnambiguousAnswerD; incorrectcolor/vertex rules. OnepresetDhit.','Longself-revisions endwithConclusionOptionC. IncidentalDdiscussionisnotafinalDhit.']),
 'Solid228':(['D','D'],['UnambiguousD:D. CorrectformalD despitewrongnetnarrative; frozenwrongBmissed.','UnambiguousCorrectAnswerDandfinalD. Incorrect2x2claimdoesnotchangecorrectletter; frozenBmissed.']),
 'Solid119':(['C','D'],['FullanswerC. Incorrectsinglewhiteface/topcountreasoning butcorrectformalchoice. PresetEexplicitlyrejected.','EndsCubeDandAnswerD, explicitlyrejectingE oncaporientation. Ementionsarenothits.']),
 'Solid137':(['A','B'],['FullfinalOptionA. DoesnotselectB; firstcallmissesfrozenB.','FullfinalB aftermatchinglinepositions andhallucinatedbrickcolumns. ExactlyonepresetBhit.']),
 'Solid187':(['C','A'],['StartsandendsC. Misdescribedadjacentnotches butcorrectformalletter; targetAmissed.','FullfinalA afterthrough-tunnelinterpretation, exactlyonepresetAhit.'])
}

def sha(data):return hashlib.sha256(data).hexdigest()
def rel(p):return str(Path(p).relative_to(ROOT))
entries=[];binding_audits=[];all_manual=[];all_source_checks=[]
prior=json.loads((TASK/'all_prior_same_question_evidence.json').read_text(encoding='utf-8'))
for q in ASSIGNED:
    actual_eligibility=eligibility(q);assert actual_eligibility['eligible'],actual_eligibility
    write(TASK/q/'eligibility_at_checkpoint.json',actual_eligibility)
    candidates=sorted((TASK/q).glob('r25_*/design.json'))
    if not candidates:
        assert q=='Solid94'
        entries.append({'question_id':q,'stage':'material_refinement','status':'screened_no_materially_distinct_human_clear_hypothesis','new_designs':0,'completed_candidate_calls':0,'design_difference_audit_path':rel(TASK/q/'design_difference_audit.json'),'primary_math_proof_path':rel(TASK/q/'primary_math_proof.json'),'current_eligibility_path':rel(TASK/q/'eligibility_at_checkpoint.json')});continue
    assert len(candidates)==1
    f=candidates[0].parent;d=json.loads((f/'design.json').read_text(encoding='utf-8'));render=json.loads((f/'render_check.json').read_text(encoding='utf-8'))
    current_sources=AD.frozen_inputs(q);assert current_sources==render['frozen_inputs']
    assert d['variant_id'] not in [x['design'].get('variant_id') for x in prior[q]]
    assert all((ROOT/x['folder']/'candidate.png').read_bytes()!=(f/'candidate.png').read_bytes() for x in prior[q])
    invocations=list((f/'tests').glob('quicktest3_*'));assert len(invocations)==1
    inv=invocations[0];binding=json.loads((inv/'binding.json').read_text(encoding='utf-8'));summary=json.loads((inv/'summary.json').read_text(encoding='utf-8'));req=json.loads((inv/'request.json').read_text(encoding='utf-8'))
    design_hash=file_hash(f/'design.json');image_hash=file_hash(f/'candidate.png');request_hash=file_hash(inv/'request.json')
    assert binding['expected_wrong_answer']==d['expected_wrong_answer']
    assert binding['design_sha256']==design_hash==file_hash(inv/'design_snapshot.json')
    assert binding['image_sha256']==image_hash and binding['pixel_sha256']==pixel_hash(f/'candidate.png')
    assert binding['request_body_sha256']==request_hash
    assert binding['question_record_sha256']==canonical_hash(AD.records[q])
    assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False
    assert set(req)=={'model','stream','thinking','messages'}
    assert len(req['messages'])==2 and req['messages'][0]=={'role':'system','content':binding['system_prompt']}
    assert req['messages'][1]['role']=='user' and len(req['messages'][1]['content'])==2
    content=req['messages'][1]['content'];assert content[0]=={'type':'text','text':AD.records[q]['question']}
    assert sha(base64.b64decode(content[1]['image_url']['url'].split(',',1)[1]))==image_hash
    assert summary['two_completed'] and len(summary['results'])==2
    assert len(list(inv.glob('run_*_started.json')))==2 and len(list(inv.glob('run_*_response.json')))==2
    finals,notes=FINAL_READINGS[q];runs=[]
    for i in (1,2):
        path=inv/f'run_{i:02d}.json';raw=inv/f'run_{i:02d}_response.json';r=json.loads(path.read_text(encoding='utf-8'));response=json.loads(raw.read_text(encoding='utf-8'));choice=response['choices'][0]
        assert r['status']=='completed' and choice['finish_reason']=='stop'
        assert r['response_sha256']==file_hash(raw) and r['request_body_sha256']==request_hash
        assert r['design_sha256']==design_hash and r['image_sha256']==image_hash
        answer=choice['message']['content'];assert answer.strip()
        runs.append({'run_index':i,'status':'completed','finish_reason':'stop','complete_final_manually_read':True,'complete_final_text':answer,'manual_final_answer':finals[i-1],'manual_notes':notes[i-1],'matches_frozen_preset':finals[i-1]==str(d['expected_wrong_answer']),'final_letter_value_consistent':True,'response_path':rel(raw),'response_sha256':file_hash(raw),'run_path':rel(path),'run_sha256':file_hash(path),'request_sha256':request_hash,'design_sha256':design_hash,'image_sha256':image_hash})
    credible=all(r['matches_frozen_preset'] for r in runs);assert not credible
    manual={'question_id':q,'variant_id':d['variant_id'],'stage':'material_refinement','review_role':'PRIMARY_ONLY','frozen_expected_wrong_answer':d['expected_wrong_answer'],'formal_correct_answer':AD.records[q]['answer'],'manual_full_final_answers':finals,'runs':runs,'two_completed':True,'credible_two_target_hits':credible,'disposition':'complete_pair_missed_immutable_preset','original_controls':'No separateold samequestioncontrolbindings found; none repeated ornewlycalled.','no_posthoc_preset_relabel_no_retry_no_selected_subset':True,'binding_path':rel(inv/'binding.json'),'summary_path':rel(inv/'summary.json'),'design_path':rel(f/'design.json'),'plugin_path':rel(f/'plugin.json'),'candidate_path':rel(f/'candidate.png'),'design_difference_audit_path':rel(f/'design_difference_audit.json'),'primary_math_proof_path':rel(TASK/q/'primary_math_proof.json'),'primary_native_visual_marker_review_path':rel(f/'primary_review.json'),'native_scale_caveat':'Several netfigures are intrinsicallysmallin768canvas. FullsamePNG wasviewed; readability isprimaryassessment only. No humansurvey orcausal/permarker/statistical claim.'}
    write(f/'manual_full_final_review.json',manual);all_manual.append(manual)
    audit={'question_id':q,'variant_id':d['variant_id'],'all_bindings_valid':True,'exactly_two_real_completed_calls':True,'one_frozen_png_and_design_for_both':True,'request_only_unchanged_question_and_candidate_png':True,'model':'mimo-v2.6-flash','thinking':{'type':'disabled'},'no_profile_max_tokens_or_timeout_override':True,'request_sha256':request_hash,'design_sha256':design_hash,'png_sha256':image_hash,'pixel_sha256':binding['pixel_sha256'],'plugin_sha256':file_hash(f/'plugin.json'),'math_sha256':file_hash(TASK/q/'primary_math_proof.json'),'difference_audit_sha256':file_hash(f/'design_difference_audit.json'),'context_sha256':file_hash(f/'context.json'),'marker_path_bindings_sha256':file_hash(f/'marker_path_bindings.json'),'actual_no_op_formal_pixel_match':render['baseline_matches_formal'],'twice_byte_identical_renderer_output':render['deterministic'],'normalization_by_approved_PluginRenderer':True,'source_inputs_unchanged_after_calls':True,'source_frozen_files':current_sources['files'],'complete_finals_manually_read':True,'full_final_review_path':rel(f/'manual_full_final_review.json'),'api_process_finished':json.loads((f/'api_process_finished.json').read_text(encoding='utf-8'))}
    binding_audits.append(audit)
    entries.append({'question_id':q,'stage':'material_refinement','variant_id':d['variant_id'],'status':'complete_pair_preset_missed','new_designs':1,'completed_candidate_calls':2,'preset':d['expected_wrong_answer'],'manual_full_final_answers':finals,'correct_answer':AD.records[q]['answer'],'credible_candidate':False,'old_new_difference':json.loads((f/'design_difference_audit.json').read_text(encoding='utf-8')),'paths':{name:rel(f/name) for name in ('design.json','candidate.png','plugin.json','render_check.json','context.json','marker_path_bindings.json','primary_review.json','manual_full_final_review.json','design_difference_audit.json')},'evidence_directory':rel(inv),'current_eligibility_path':rel(TASK/q/'eligibility_at_checkpoint.json')})

write(TASK/'manual_full_final_answers.json',{'stage':'material_refinement','all_complete_finals_manually_read':True,'candidates':all_manual})
write(TASK/'evidence_binding_audit.json',{'stage':'material_refinement','all_valid':True,'candidates':binding_audits,'errors':[],'aborted':[],'retries':0})
base=json.loads((TASK/'source_preservation_baseline.json').read_text(encoding='utf-8'))
frozen_changes=[]
for group in ('formal_and_helpers','prior_evidence'):
    for p,h in base[group].items():
        actual=file_hash(ROOT/p) if (ROOT/p).is_file() else None
        if actual!=h:frozen_changes.append({'group':group,'path':p,'before':h,'after':actual})
for q,old in base['per_question_frozen_inputs'].items():
    if AD.frozen_inputs(q)!=old:frozen_changes.append({'group':'question_inputs','question_id':q})
diagnostic_changes=[]
for group in ('mutable_progress_diagnostic','workbench_state_diagnostic'):
    for p,h in base[group].items():
        actual=file_hash(ROOT/p) if (ROOT/p).is_file() else None
        if actual!=h:diagnostic_changes.append({'group':group,'path':p,'before':h,'after':actual,'classification':'Mutableexternalruntime diagnosticmetadata/state; preservewithoutrestoring. Neverformalinputorquestionapprovalevidence.'})
source_audit={'stage':'material_refinement','frozen_changes':frozen_changes,'frozen_preserved':not frozen_changes,'prior_candidate_evidence_files_checked':len(base['prior_evidence']),'all_assigned_original_approvals_current':True,'all_assigned_still_eligible':True,'mutable_progress_and_state_drift':diagnostic_changes,'scope_limit':'Perquestionrelevantformalinputs,approval,Specialindicesandpriorassignedcandidateevidence checked. No claimaboutentireworkspaceoractorofunrelatedconcurrentchanges. Ownstrictwriteguardallowedonlybackground_25; externalunrelatedworkbenchchangespreserved.','all_current_eligibility':{q:eligibility(q) for q in ASSIGNED},'no_formal_Pass_Collect_publication_review_API_actions':True,'no_old_history_modified':True}
write(TASK/'source_preservation_final.json',source_audit);assert not frozen_changes,frozen_changes

write(TASK/'refinement_exhaustion_assessment.json',{'stage':'material_refinement','all_assigned_ids_assessed':ASSIGNED,'unworked_question_ids':[],'reason_stop':'All8assignedrefinementquestionsassessedwithreasonablemeaningfulhypotheses; no3crediblecandidatecutofftriggered. Sevenmateriallynewhypothesestestedexactlytwice; Solid94screenedbeforecalls.','further_same_question_hypotheses_screened':{
 'Solid94':'See detailed design_difference_audit: cutdepth, vertex andface-remnant hypothesesalreadyattempted; othermarks eithercosmetic, isolatedsalience orfalsecut/labelrisk.',
 'Solid95':'Omittingbase alreadytested; overlapcountingnewlytested. Swappingrailpalette, targetingposthoc0, countingremaininginsteadremoved, ormarkingimaginedtopchannelgrid wouldbecosmetic/taskpolarity/falsegeometry, notanewclearfeaturebinding.',
 'Solid111':'Localcorner old; actualoppositepair sufficiencynew. ChoosinganothertruecolorpairinB/A wouldrepeatthesameonepairshortcut withdifferentpalette/receiver; nofreshhuman-clearrelationfound.',
 'Solid119':'Actualvalidlocaldomino old; diagonalcapconnectivitynew. Otherwrongoptionsprovidealreadytestedlocalwhite/graystockomissions orcosmeticorientationchanges. Do not retargettoobservedDaftercalls.',
 'Solid137':'Two valid2cell subsetsold; 3depthunitsas2new. Anotherdepthrail/color/option withsamecountmisread isnotmaterial. Moremarkingwouldobscuresmallsemanticfills withoutnewrelation.',
 'Solid170':'Opposite/adjacent old; bent/flattopologynew. Nativefigure matchesSolid187, whosepriorcapclosure andadjacenthole designsareknownfailed; do notregenerateidenticalknownfailedgeometryunderanotherformalID.',
 'Solid187':'Priorcapclosure andglobaladjacency plusnewhalf-to-whole identitycoverclearindependentbindings. FacewindowE isalsoalreadytestednewlyonidenticalnativeSolid170; no cross-IDretry. Otherrecoloringofsameholepairsnotmaterial.',
 'Solid228':'OldAendclosureandrepeatedface; newB/Dfoldrelationtransfer. Furtherterminalfaceframesorothervalidnetreceiverswouldreusefold-overlapshortcut, andtargetDwouldnotbeawronganswer. No newgiven orfalsecuttoforce.'},'quota_or_cost_stop':False,'external_failure':False,'all_calls_and_raw_history_preserved':True})
queue={'stage':'material_refinement','unit':'background_25','created_at':datetime.now(timezone.utc).isoformat(),'actual_assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'candidates':[],'credible_candidate_count':0,'reason_empty':'No newdesignmatchesitsownfrozenwrongpresetinbothcompletefinals; nooldunchangeddoublehiteligibleforpromotion.','all_designs_and_results':entries,'delivery_policy':'EveryeventualdeliveryrequiresparentNEWindependentsecondreview; noneauthorizedbythisprimary-onlycheckpoint.'}
write(TASK/'second_review_queue.json',queue)
checkpoint={'unit':'background_25','stage':'material_refinement','status':'COMPLETED_FINITE_REVIEW_CHECKPOINT','completed_at':datetime.now(timezone.utc).isoformat(),'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'counts':{'assigned':8,'assessed':8,'new_material_designs':7,'screened_before_calls':1,'completed_candidate_pairs':7,'completed_real_candidate_calls':14,'original_control_calls':0,'credible_primary_candidates':0,'errors':0,'aborts':0,'retries':0},'stop_reason':'All8assignedrefinementquestionsassessedandexhaustedreasonablemeaningfulhypotheses.','results':entries,'second_review_queue_path':rel(TASK/'second_review_queue.json'),'source_preservation_audit_path':rel(TASK/'source_preservation_final.json'),'raw_binding_audit_path':rel(TASK/'evidence_binding_audit.json'),'complete_manual_finals_path':rel(TASK/'manual_full_final_answers.json'),'prior_history_audit_path':rel(TASK/'prior_history_completion_audit.json'),'old_evidence_snapshot_path':rel(TASK/'all_prior_same_question_evidence.json'),'delivered_references_path':rel(TASK/'delivered_reference_audit.json'),'exhaustion_assessment_path':rel(TASK/'refinement_exhaustion_assessment.json'),'failures':{'transport_errors':[],'aborted_calls':[],'preset_missed_candidates':[e['question_id'] for e in entries if e['new_designs']]},'approval_status':'UNREVIEWED runtime research only; noPass/Collect/publication/formalreviewaction.','limitations':['Two-outputresultsarenotstatistics,nothumanperformanceandnotcausalestimates.','No separatepreviousoriginalcontrolbindingsforthesequestionsfound; no unchangedcontrolsrepeated.','Smallnetfeaturesremainatnativeformalscale; source/candidateactuallyviewed, but independentreviewwouldstillbe required fordelivery.','Solid119pre-callclarificationdistinguishes2Dfrontpatchcorneradjacencyfrom3Dcubeedgeadjacency; frozenpreset/image/designkept.','Mutableglobalprogresshashesarediagnostic; relevantformalapprovalandSpecialstatearerecheckedcurrently.'],'api_processes':'Allsevenrecordedapi_process.json have correspondingapi_process_finished.json withtwo_completed=true. FinalOSprocessinventorysavedseparatelyafterthisscriptends.','all_own_writes_below':str(TASK),'nested_agents_or_threads':0}
write(TASK/'checkpoint.json',checkpoint)
print(json.dumps({'checkpoint':str(TASK/'checkpoint.json'),'counts':checkpoint['counts'],'frozen_preserved':source_audit['frozen_preserved'],'diagnostic_drift_count':len(diagnostic_changes)},ensure_ascii=False))
