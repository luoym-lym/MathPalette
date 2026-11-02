from tools27 import *
import base64
from PIL import Image

FINALS={
 'Plane159':(['B','B'],[True,True],[None,None],['FinalB matches the simultaneous-replacement B sequence, not presetE. It miscounts8cells.','FinalB and full nine-cell B sequence are consistent, but frozen preset isE. B/B cannot be relabeled.']),
 'Plane203':(['E','C'],[True,True],[None,None],['FinalE correctly identifies the only uncovered letter.','FinalC follows misread grey cells; does not equal presetD.']),
 'Plane292':(['E','E'],[True,True],[None,None],['FinalE is correct despite false third-reflection narrative; presetA missed.','FinalE is correct despite treating reflections as halfturns; presetA missed.']),
 'Plane362':(['C','B'],[False,True],['8005','5008'],['FinalC is paired with8005 while drawnC is8002, so inconsistent and not a hit; presetD also missed.','FinalB=5008 is consistent and correct, not presetD.']),
 'Plane371':(['B','E'],[False,True],[None,None],['FinalB misdescribes B as reversed-order upright; regardless it misses presetD.','FinalE matches the correct final image; narrative glyph transliterations have errors, but no extra narrative gate is imposed. PresetD missed.']),
 'Plane444':(['A','C'],[True,True],[None,None],['FinalA explicitly claims original upright orientation; wrong but not presetC.','FinalC and its step-up colored-feature description agree with drawnC, so this one call hits presetC. Pair fails.'])
}
EXHAUST={
 'Plane159':['Old simultaneous3class rule and old first-stage-only mapping were already tested. New merged-dark grouping omits firststage and failed its own E preset.','B/B is not a new candidate: B was not the new immutable preset. Retargeting toB or changing stripe intensity would violate the task.','All-grey C would require an unsupported extra iteration or source-fill change; no simple new geometric information binding retained.'],
 'Plane203':['Old lower-L translations were exhausted and new lower-L halfturn reverses row order with a distinct D prediction. New E/C pair misses.','Other displaced crease/horizontal reflection choices leave several letters uncovered and do not supply a clean unique targeted alternative.','Recoloring the same edge pairs or retargeting observedC would repeat an old translation family or be posthoc.'],
 'Plane292':['Old initial-source single-axis shortcut failed its own B preset. New last-state/next-axis intermediate stopping rule failed its A preset.','Selecting another intermediate stage is the same stage-truncation family without a new correspondence; changes of feature width or ear color are cosmetic.','The exact five-axis computation uniquely givesE. No additional simple, human-clear mechanism retained without force.'],
 'Plane318':['Only answer glyphs are drawn; the input y is textual. A source-output feature pairing cannot be created with allowed actions without inventing a glyph.','Answer-arm styling alone amounts to answer salience. See primary_math_correction.json for corrected composed matrix; formalA unchanged.'],
 'Plane353':['The +5 modulo10 relation resides in text digits, which allowed styling cannot change.','A+4 off-by-one hypothesis, reversed wheel order and invented wheel ticks were considered; box-only marks do not express these mechanisms and new ticks invent information.'],
 'Plane362':['Old identityA, reversed-order unchanged2C, and new actual horizontal-mirrorD cover distinct available incorrect transformation families.','New C(value8005)/B pair fails. No unchanged rerun or posthoc switch toC is permitted.','E2005 is not a rigid whole-image transformation of2008: it replaces the8 identity, requiring unsupported semantic editing rather than a meaningful new geometry mapping.'],
 'Plane371':['Old internalN/G handedness pairing and new leadingK/trailingOO word-order grouping are distinct; new B/E pair failsD preset.','Changing to another internal letter to repeat local-handedness emphasis supplies no new operation, grouping or semantic repair.','No clean additional source-to-output mechanism retained; no new option may be selected merely from observedB.'],
 'Plane444':['Old uniform full-contour C and new fixed-origin-versus-shape-extreme C mechanisms were examined separately. New A/C pair fails.','A different whole-outline wrong answer would chiefly reintroduce old answer salience; source/target color swaps or short-edge intensity changes are cosmetic.','Using the observedA as a new preset without a distinct pretest geometric rationale is forbidden. No further concise targeted hypothesis retained.']
}

records=[];binding_reports=[]
for q in FINALS:
    folder=next((HERE/q).glob('r27_*'));evs=list((folder/'tests').glob('quicktest3_*'));assert len(evs)==1;ev=evs[0]
    d=json.loads((folder/'design.json').read_text(encoding='utf-8'));binding=json.loads((ev/'binding.json').read_text(encoding='utf-8'))
    summary=json.loads((ev/'summary.json').read_text(encoding='utf-8'));assert summary['two_completed']
    frozen=d['expected_wrong_answer'];finals,consistent,values,notes=FINALS[q];manual=[]
    for n in [1,2]:
        raw=ev/f'run_{n:02d}_response.json';rawdata=json.loads(raw.read_text(encoding='utf-8-sig'));job=json.loads((ev/f'run_{n:02d}.json').read_text(encoding='utf-8'))
        assert rawdata['choices'][0]['finish_reason']=='stop' and job['status']=='completed'
        content=rawdata['choices'][0]['message']['content']
        manual.append({'run_index':n,'full_complete_final_answer':content,'explicit_manual_final':finals[n-1],
            'explicit_final_value':values[n-1],'letter_value_or_qualitative_option_consistency':consistent[n-1],
            'preset_hit':finals[n-1]==frozen and consistent[n-1],'manual_notes':notes[n-1],
            'raw_path':str(raw),'raw_sha256':file_hash(raw),'run_record_path':str(ev/f'run_{n:02d}.json')})
    review={'stage':'material_refinement','question_id':q,'variant_id':d['variant_id'],'reviewed_at':now(),
        'review_type':'PRIMARY manual complete-final reading only','complete_both_model_finals_manually_read':True,
        'immutable_expected_wrong_answer':frozen,'design_sha256':file_hash(folder/'design.json'),'image_sha256':file_hash(folder/'candidate.png'),
        'evidence_dir':str(ev),'records':manual,'both_preset_hits':all(x['preset_hit'] for x in manual),
        'status':'complete_pair_preset_miss','no_posthoc_relabel_no_retries_no_combining_images':True,
        'parent_NEW_independent_review_mandatory_before_any_eventual_delivery':True}
    assert not review['both_preset_hits'];write(folder/'manual_final_review.json',review)
    payload=json.loads((ev/'request.json').read_text(encoding='utf-8'))
    current=eligibility(q);assert current['eligible']
    image_bytes=(folder/'candidate.png').read_bytes();design_bytes=(folder/'design.json').read_bytes()
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    assert set(payload)=={'model','stream','thinking','messages'}
    assert len(payload['messages'])==2
    user=payload['messages'][1];assert user['role']=='user' and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':current['formal_record']['question']}
    assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==image_bytes
    assert file_hash(ev/'request.json')==binding['request_body_sha256']
    assert file_hash(folder/'candidate.png')==binding['image_sha256']
    assert file_hash(folder/'design.json')==binding['design_sha256']
    assert (ev/'design_snapshot.json').read_bytes()==design_bytes
    assert (folder/'repeat.png').read_bytes()==image_bytes
    assert binding['expected_wrong_answer']==frozen and binding['requested_runs']==2
    assert file_hash(HERE/'harness/quicktest3_isolated.py')==file_hash(BASE/'harness/quicktest3_isolated.py')
    for n in [1,2]:
        job=json.loads((ev/f'run_{n:02d}.json').read_text(encoding='utf-8'))
        assert job['request_body_sha256']==binding['request_body_sha256'] and job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256']
        assert job['response_sha256']==file_hash(ev/f'run_{n:02d}_response.json')
    audit={'question_id':q,'variant_id':d['variant_id'],'stage':'material_refinement','checked_at':now(),
        'exactly_two_actual_completed_calls_same_frozen_PNG_and_preset':True,'actual_full_complete_finals':finals,
        'only_formal_question_plus_PNG_user_input':True,'exact_reference_system_prompt':payload['messages'][0]['content']==binding['system_prompt'],
        'exact_unchanged_harness_bytes':True,'no_model_profile_token_timeout_override_retry':True,
        'image_design_request_raw_bindings_verified':True,'native_actual_candidate_view_record':str(folder/'primary_visual_review.json'),
        'pretest_difference_audit':str(folder/'design_difference_audit.json'),'current_eligibility':current,
        'hashes':{str(p.relative_to(HERE)):file_hash(p) for p in folder.rglob('*') if p.is_file()},
        'primary_only':True,'both_preset_hits':False}
    write(folder/'evidence_binding_audit.json',audit);binding_reports.append(audit)
    records.append({'question_id':q,'variant_id':d['variant_id'],'candidate_path':str(folder),'expected_wrong_answer':frozen,
        'actual_finals':finals,'full_manual_final_review':str(folder/'manual_final_review.json'),'status':'complete_pair_preset_miss',
        'old_new_difference':json.loads((folder/'design_difference_audit.json').read_text(encoding='utf-8'))['substantive_new_information'],
        'proofs':[str(p) for p in [folder/'primary_math_audit.json',HERE/q/'fresh_transform_math.json',HERE/q/'fresh_discrete_math.json'] if p.exists()],
        'immutable_evidence':str(ev),'evidence_binding_audit':str(folder/'evidence_binding_audit.json')})

for q in ASSIGNED:
    write(HERE/q/'refinement_exhaustion.json',{'stage':'material_refinement','question_id':q,'assessed_at':now(),
        'reasonable_materially_distinct_hypotheses_exhausted_for_this_finite_unit':True,
        'retained_and_rejected_hypothesis_rationale':EXHAUST[q],'current_eligibility':eligibility(q),
        'not_a_global_impossibility_claim':True,'no_further_calls_or_unchanged_retests':True})

cfg,ad=adapter();source_reports=[]
old=json.loads((HERE/'old_evidence_index.json').read_text(encoding='utf-8'));old_changes=[];duplicate_pngs=[]
for q,item in old.items():
    for name,h in item['files'].items():
        p=ROOT/name
        if not p.is_file() or file_hash(p)!=h:old_changes.append(name)
    groups={}
    for name in item['pngs']:
        p=ROOT/name;groups.setdefault(file_hash(p),[]).append(name)
    duplicate_pngs.append({'question_id':q,'byte_identical_PNG_groups':list(groups.values()),'distinct_pixels_natively_viewed':True})
    start=json.loads((HERE/q/'input_fingerprints.json').read_text(encoding='utf-8'));end=inputs(ad,q)
    frozen_changes=[];aggregate=[]
    for name,h in start['files'].items():
        nh=end['files'].get(name)
        if nh!=h:
            entry={'path':name,'before':h,'after':nh}
            (aggregate if name in ['PlaneGeometry\\dataset.jsonl','provenance\\approvals.json'] else frozen_changes).append(entry)
    record_ok=start['question_record_sha256']==end['question_record_sha256'];check=eligibility(q)
    assert not frozen_changes and record_ok and check['eligible']
    assert (HERE/q/'original.png').read_bytes()==ad.original_paths[q].read_bytes()
    source_reports.append({'question_id':q,'current_eligible':check['eligible'],'current_original_approval_valid':check['current_content_sha256']==check['approval']['content_sha256'],
        'formal_record_hash_unchanged':record_ok,'individual_frozen_source_changes':frozen_changes,'aggregate_external_state_drift_diagnostic':aggregate,
        'original_PNG_bytes_unchanged':True,'current_record_and_approval':check})
assert not old_changes
write(HERE/'source_preservation_final.json',{'stage':'material_refinement','checked_at':now(),'all_eight_frozen_sources_and_current_approvals_valid':True,
    'per_question':source_reports,'old_same_question_evidence_changes':old_changes,'old_PNG_duplicate_hash_equivalence':duplicate_pngs,
    'write_guard':'tools27.py installs own-root filesystem audit guard before runtime_isolation/project imports; all Python commands use-Xutf8-B and caches under own unit.',
    'scope_of_claim':'Only assigned question inputs, original approvals and indexed old same-question evidence verified. Unrelated concurrent human workbench activity was not restored or attributed. Mutable global progress hashes are diagnostic metadata.'})

write(HERE/'second_review_queue.json',{'stage':'material_refinement','unit':'background_27','created_at':now(),'candidates':[],
    'credible_possible_doublehits':0,'reason':'All6 new exact pairs miss their own frozen presets. Plane159B/B cannot be relabeled from presetE; Plane362C/8005 is inconsistent.',
    'parent_NEW_independent_review_required_before_any_eventual_delivery':True,'no_self_approval_no_formal_Pass_Collect_publication':True})
write(HERE/'checkpoint.json',{'stage':'material_refinement','unit':'background_27','status':'terminal_all8_assessed_reasonable_material_hypotheses_exhausted',
    'completed_at':now(),'assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':ASSIGNED,'unworked_question_ids':[],
    'new_design_count':6,'actual_new_candidate_calls':12,'complete_two_call_pairs':6,'credible_possible_doublehits':0,
    'candidate_ids':[],'tested_candidates':records,'screened_question_ids':['Plane318','Plane353'],
    'screening_math_correction':'Plane318/primary_math_correction.json (composition=(y,x), formal answerA unchanged)',
    'old_doublehits_promoted':[],'all_old_evidence_preserved':True,'old_evidence_index':'old_evidence_index.json',
    'source_current_eligibility_audit':'source_preservation_final.json','second_review_queue':'second_review_queue.json',
    'failure_and_abort_audit':{'candidate_preset_misses':6,'API_errors':0,'API_aborts':0,'API_retries':0,
       'non_API_diagnostics':[{'file':'inspect_features27.py','issue':'Initial compact exploration assumed contiguous oIDs; o3 absent inPlane203. KeyError occurred before any calls and was fixed to skip absent IDs. All actual style targets were taken from fresh context.'},
                              {'file':'Plane318/primary_math_correction.json','issue':'Corrected displayed screening matrix in separate own-unit audit; original assessment preserved. No candidate/call/formal data affected.'}]},
    'API_processes':'All six run_pair.py processes returned exit0 and api_process_finished.json; external OS check saved separately in process_audit.json.',
    'controls':{'existing_original_control_evidence_for_assigned8':'None found in all old same-question evidence folders.','new_control_calls':0,'causal_or_statistical_claim':False},
    'preservation':'Own runtime root writes only; no formal, state, approval, workbench API, .env, .runtime, .git, shared helper or global progress writes.',
    'primary_only':True,'parent_NEW_independent_review_before_any_eventual_delivery':True})
print(json.dumps({'assessed':ASSIGNED,'new_designs':6,'calls':12,'complete_pairs':6,'credible_candidates':0,'finals':{q:FINALS[q][0] for q in FINALS}},ensure_ascii=False))
