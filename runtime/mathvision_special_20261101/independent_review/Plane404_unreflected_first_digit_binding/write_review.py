import audit as a
from datetime import datetime, timezone
from pathlib import Path
from dataset_tools import catalog

math=a.read(a.OUT/'independent_math.json')
render=a.read(a.OUT/'render_and_preservation_audit.json')
evidence=a.read(a.OUT/'raw_bindings_and_full_responses.json')
elig=a.read(a.OUT/'current_eligibility.json')
history=a.read(a.OUT/'history_and_queue_audit.json')
chronology=a.read(a.OUT/'chronology_audit.json')
serialization=a.read(a.OUT/'original_png_serialization_audit.json')
frozen=a.read(a.OUT/'frozen_input_checks.json')
start=a.read(a.OUT/'evidence_manifest_start.json')

# Final recheck of current authority and all preserved files actually inventoried.
current_row=next(x for x in catalog.rows(a.ROOT/'PlaneGeometry/dataset.jsonl') if x['id']=='Plane404')
current_approval=a.read(a.ROOT/'provenance/approvals.json')['approvals']['Plane404']
assert current_row==elig['formal_record']
assert current_approval==elig['original_approval']
assert catalog.digest(catalog.content(a.ROOT,'PlaneGeometry',current_row))==current_approval['content_sha256']
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    p=a.ROOT/'PlaneGeometry/special_variant'/name
    assert not any(x.get('question_id',x.get('id'))=='Plane404' for x in catalog.rows(p))
assert not (a.ROOT/'PlaneGeometry/special_variant/Plane404/recipes.json').exists()
assert not (a.ROOT/'PlaneGeometry/special_variant/Plane404/collection.json').exists()
end=[]
for old in start:
    p=a.ROOT/old['path']
    end.append({'path':old['path'],'start_sha256':old['sha256'],
                'end_sha256':a.sha(p) if p.is_file() else None,
                'same':p.is_file() and a.sha(p)==old['sha256']})
preservation={'checked_at':datetime.now(timezone.utc).isoformat(),'scoped_file_count':len(end),
              'files':end,'all_scoped_source_and_evidence_hashes_unchanged':all(x['same'] for x in end),
              'workspace_claim':'Scoped source/evidence verification only. No claim that the entire shared workspace is unchanged or who authored unrelated concurrent changes.',
              'unrelated_concurrent_changes_preserved':True,
              'mutable_runtime_progress':'exploration_report/remaining_questions are diagnostic progress metadata; historical snapshots remain unmodified. Drift is not evidence or frozen-geometry corruption.'}
a.save('final_preservation_check.json',preservation)
assert preservation['all_scoped_source_and_evidence_hashes_unchanged']

markers=[]
roles={
 'o2':{'position':'upper-right moving bar','before':[[1,4.5],[1,5.5]],'after':[[1,1.5],[1,.5]],
       'role':'Supplies the lower-right leg of the true 5. Red binds it to the other moving bar. Its reversal is one of the two decisive differences between 5 and a locally unreflected 2.',
       'necessity':'Completes the moving pair and the lower-right leg; no duplicate mark. Empirical necessity of its red styling is not claimed.'},
 'o3':{'position':'lower-left moving bar','before':[[0,3.5],[0,4.5]],'after':[[0,2.5],[0,1.5]],
       'role':'Supplies the upper-left leg of the true 5. Red marks the complementary handed feature whose top/bottom order must reverse.',
       'necessity':'Completes the moving pair and upper-left leg. Marking only o2 would omit the other defining handed feature; empirical necessity is untested.'},
 'o18':{'position':'bottom stationary horizontal','before':[[0,.5],[1,.5]],'after':[[0,.5],[1,.5]],
        'role':'Bottom completion bar of the same first digit; blue distinguishes the stationary scaffold from the red moving pair.',
        'necessity':'One of the three actual horizontal digit strokes. Gives the colored scaffold its bottom, without an extra cue or duplicate line; no per-marker effect claim.'},
 'o19':{'position':'middle stationary horizontal','before':[[0,1.5],[1,1.5]],'after':[[0,1.5],[1,1.5]],
        'role':'Central crossbar where the two reflected red legs join opposite ends. Blue completes the stationary scaffold.',
        'necessity':'Encodes the central stroke common to 2 and 5 and links their two levels. It is information-bearing, not an independent answer highlight; no ablation claim.'},
 'o20':{'position':'top stationary horizontal','before':[[0,2.5],[1,2.5]],'after':[[0,2.5],[1,2.5]],
        'role':'Top completion bar of the first digit; blue makes all and only the stationary first-digit bars one group.',
        'necessity':'Completes the colored three-bar scaffold at its top. Omitting this style would leave that scaffold only partly grouped; empirical indispensability is untested.'}}
plugin=a.read(a.CAND/'plugin.json')
for action in plugin['params']['actions']:
    oid=action['target'];px=next(x for x in render['markers'] if x['id']==oid)
    markers.append({'target':oid,**roles[oid], 'actual_action':action,
                    'legality':'Existing styleable original solid segment; legal object hue and 1.5 pt whitelist width; no interval, new point, new line, text or fill action.',
                    'native_size_clarity':{'observed_visible':True,'centerline_length_px':px['centerline_length_px'],
                       'nominal_width_px':px['width_nominal_px'],'changed_pixels':px['changed_pixels'],
                       'judgment':'Clear against white at native 768x768. Distinct from nearby dots, fold dashes and neighboring digit; endpoints remain in the same positions.'},
                    'semantics':'Original numeral ink remains part of the transparent overlay. Hue groups existing ink and introduces no extra fold, missing bar, cut, equality or color-dependent encoding.'})

candidate=evidence['tests'][0]
control=evidence['tests'][1]
candidate_finals=[
 {'run':1,'complete_final_conclusion':'Therefore, the visible result after folding is the sequence **2: 6: 9**.',
  'letter_in_response':'Option A is **2: 6: 9**. This matches our count of 2 lines, 6 lines, and 9 lines.',
  'final_letter':'A','final_value':'2:6:9','letter_is_explicit_last_sentence':False,
  'interpretation':'Last sentence gives the numeric value, uniquely A; preceding selection explicitly identifies A. No contradictory final letter/value.',
  'narrative_objections':['Incorrectly counts upper vertical bars as 2, 6 and 9; actual unsplit upper segment counts are 2,2,2.',
                          'Hallucinates color-coded answer options A/B; formal choices are uncolored text and provide no hue mapping.'],
  'counts_as_preset_hit':True},
 {'run':2,'complete_final_conclusion':'This corresponds to the pattern **2 : 6 : 9**.\n\nA: 2: 6: 9\nB: 2: 6: 6\nC: 5: 6: 9\nD: 2: 8: 6\nE: 5: 8: 9\n\nThe correct choice is A.',
  'final_letter':'A','final_value':'2:6:9','letter_is_explicit_last_sentence':True,
  'interpretation':'Earlier second "8" is an incorrect intermediate statement. Final pattern and final A agree unambiguously; listing all options is not a competing final.',
  'narrative_objections':['Invents six numbered spatial columns and covered-dot reasoning inconsistent with the actual transparent segment union.',
                         'Mentions a second "8" before the conclusion; does not finish at 8.'],
  'counts_as_preset_hit':True}]
for r,final in zip(candidate['runs'],candidate_finals):
    final.update({'response_sha256':r['response_sha256'],'run_sha256':r['run_sha256'],
                  'complete_response_manually_read':True,'complete_response_text':r['complete_answer_text'],
                  'started_at':r['started_at'],'finished_at':r['finished_at'],'finish_reason':r['finish_reason'],
                  'truncated':r['truncated'],'response_id':r['response_id']})
control_finals=[]
for r,letter,value in zip(control['runs'],['B','C'],['2:6:6','5:6:9']):
    control_finals.append({**r,'final_letter':letter,'final_value':value,'correct_final':letter=='C',
                           'note':'Full narrative is inaccurate; final letter/value interpretation is independent of that narrative.'})

hashfiles=[a.CAND/x for x in ['candidate.png','plugin.json','design.json','context.json','path_fingerprints.json',
             'primary_review.json','primary_visual_review.json','source_image_visual_audit.json','fold_segment_math_audit.json',
             'render_check.json','replay_final_audit.json','replay_final.png','repeat.png','harness_isolation_audit.json']]
hashfiles += [a.ROOT/'PlaneGeometry'/row for row in [current_row['original_image'],current_row['image'],current_row['scene'],current_row['script']]]
hashfiles += [a.UNIT/'second_review_queue.json',a.UNIT/'checkpoint.json',a.BASE/'Plane404_unit08_independent_review_brief.txt']
report={
 'schema_version':'1.0.0','question_id':'Plane404','variant_id':'unreflected_first_digit_binding',
 'decision':'recommended','reviewed_at':datetime.now(timezone.utc).isoformat(),
 'review_role':'NEW independent second reviewer; worked alone; independent recomputation from actual source/formal geometry and native diagrams.',
 'decision_scope':'Review recommendation only. No original approval, Special Pass, Collect, publication or formal-state change.',
 'reasons':[
   'Exact reflection and overlay independently give the unique numeric result C=5:6:9 for all three digits.',
   'All five legal styles have concrete first-digit segment roles. Actual native-size diagrams and diagnostic overlay remain clear, with no new mathematical given or color-code ambiguity.',
   'Exactly two retained candidate calls on the same predeclared A design and frozen PNG complete with final A/2:6:9; full raw response bindings and nonthinking profile verified.',
   'Original approval and all Plane404 source dependencies still match; authoritative records show MathVision/no Pass/not collected/no special completion.'],
 'required_reading':[str(p.relative_to(a.ROOT)) for p in [a.BASE/'Plane404_unit08_independent_review_brief.txt',a.ROOT/'AGENTS.md',
    a.ROOT/'MATHPALETTE_PROTOCOL.md',a.ROOT/'PlaneGeometry/REDRAW_PROTOCOL.md',a.ROOT/'PlaneGeometry/dataset_generator/protocol.json',
    a.ROOT/'PlaneGeometry/workbench/README.md',a.ROOT/'PlaneGeometry/workbench/agent_prompt.md',a.ROOT/'PlaneGeometry/workbench/plugin.schema.json',
    a.UNIT/'second_review_queue.json',a.UNIT/'checkpoint.json']],
 'independent_unique_answer_proof':{
   **math,
   'first_digit_explanation':'o2 (1,4.5)-(1,5.5) becomes (1,1.5)-(1,0.5), the lower-right leg. o3 (0,3.5)-(0,4.5) becomes (0,2.5)-(0,1.5), the upper-left leg. Fixed horizontals at y=0.5,1.5,2.5 yield top/middle/bottom + upper-left + lower-right = 5. Neither upper-right nor lower-left vertical exists.',
   'middle_digit_explanation':'o4 x=3,y=3.5..5.5 becomes the complete left vertical y=0.5..2.5. o5 x=4,y=4.5..5.5 becomes lower-right y=0.5..1.5. o21..o23 give the three fixed horizontals. This is 6; an 8 would require a missing upper-right segment, which a lone endpoint dot does not supply.',
   'right_digit_explanation':'o6 x=6,y=3.5..4.5 becomes upper-left y=1.5..2.5. o7 x=7,y=3.5..5.5 becomes complete right vertical y=0.5..2.5. o24..o26 give the fixed horizontals. This is 9; a 6 would need lower-left and lack upper-right, opposite to the actual segment set.',
   'dots_and_separators':'Ten upper dot objects and six lower separator dot objects are retained. Reflected unused endpoint dots coincide with horizontal-bar endpoints. The x=2 and x=5 dot columns remain separators, with three dot positions per column as in the source. Dots do not span a unit vertical interval and cannot turn 5 into 2, 6 into 8, or 9 into 6.',
   'source_check':'Actual source JPG at native size visibly has the same upper-right/lower-left first pair, full-left plus upper-right middle pair, full-right plus lower-left right pair, and three lower horizontals per digit. The coordinate proof agrees with those pixels; the stored answer/primary proof was not used as a premise.'},
 'marker_reviews':markers,
 'marker_set_assessment':{
   'all_five_have_specific_informational_roles':True,'no_redundant_overlapping_mark_or_option_salience':True,
   'conciseness':'Styles all and only the five information-bearing first-digit strokes: complete moving pair versus complete stationary three-bar scaffold. No marks on choices, unrelated dots, other digits or fold apparatus.',
   'necessity_limit':'The five styles are purposeful as a complete feature grouping. Neither mathematical need for color nor causal/per-marker empirical indispensability is claimed. No arbitrary numeric mark cap or ablation hard gate is imposed.'},
 'actual_image_and_human_semantics':{
   'images_actually_viewed_at_native_size':[{'path':'PlaneGeometry/originals/Plane404.jpg','size_px':[238,173]},
       {'path':'PlaneGeometry/image/Plane404.png','size_px':[768,768]},
       {'path':str((a.CAND/'candidate.png').relative_to(a.ROOT)),'size_px':[768,768]},
       {'path':str((a.OUT/'diagnostic_exact_fold_overlay.png').relative_to(a.ROOT)),'size_px':[768,768],
        'role':'Reviewer diagnostic from exact frozen geometry at the original display scale, not a solver input or replacement source.'}],
   'human_numeric_interpretation':'Colored first digit folds into a clearly connected 5, followed by black 6 and 9. Every colored bar is about 63.55 px long and 2.08 px wide nominally at 100 dpi; missing vertical slots remain about 63.55 px gaps. A different hue at a joined endpoint does not erase connectivity or create another digit.',
   'hue_semantics':'The stem asks what the transparent paper shows and the choices specify numeric triplets. It supplies no hue legend, color-count rule, color exclusion, opaque mask, transfer/cancellation rule or matching colored answer option. Red and blue remain visible numeral ink under the same reflection. The two hues honestly distinguish moving verticals from stationary horizontals. Treating hue as extra answer data or discarding a hue is unsupported by the actual task.',
   'actual_new_relations_examined':'There is no newly drawn stroke, point, contour, region, cut or purported partition. Existing bars are recolored and mildly thickened in place. The original paper outline, dashed fold, curved downward arrow and its filled arrowhead remain black. No appearance can reasonably be read as an extra fold or fixed piece partition.',
   'preserved_information':'All original dot disks, separators, coordinates, line endpoints, horizontal/vertical bar inventories, fills, fold line/dashes, arrow geometry/arrowhead, visibility, transforms and text are unchanged. This formal PNG has no option text embedded; the question/choices remain exact external text.',
   'source_background':'Upstream JPG has gray paper background; the already-approved formal redraw has white paper. Candidate does not change either file or introduce/remove any semantic fill.',
   'reviewer_judgment_limit':'Normal-size readability and semantic unambiguity are expert inspection judgments, not a new human-performance study.'},
 'legality_and_render_verification':{
   **render,'new_objects':0,'selected_object_count':5,
   'schema_colors':['#DC2626','#2563EB'],'actual_width_pt':1.5,'allowed_object_widths_pt':[0.5,1,1.5,2,3],
   'linestyle':'No linestyle field supplied; all five original solid styles retained.',
   'original_no_op_serialization_note':'No-op replay has identical decoded pixels and IDAT, IHDR and pHYs chunks; only the Software text chunk differs between formal renderer and workbench serializer. Candidate replays are byte-identical to the exact tested PNG.',
   'original_serialization_audit':'original_png_serialization_audit.json'},
 'frozen_evidence_and_profile':{
   'preset':{'letter':'A','value':'2:6:9','design_sha256':candidate['binding']['design_sha256'],
             'design_snapshot_byte_identical':True,'immutable_pre_call_preset_confirmed':True},
   'correct_answer_independently_proved':{'letter':'C','value':'5:6:9'},
   'exact_file_hashes':[a.pathinfo(p) for p in hashfiles],
   'question_record_sha256':candidate['binding']['question_record_sha256'],
   'request_sha256':candidate['request_sha256'],'binding_sha256':candidate['binding_sha256'],
   'image_sha256':candidate['binding']['image_sha256'],'image_pixel_sha256':candidate['binding']['pixel_sha256'],
   'settings':candidate['binding']['settings'],'system_prompt':candidate['binding']['system_prompt'],
   'payload_examination':'Exact request JSON has only model=mimo-v2.6-flash, stream=false, thinking.type=disabled, standard system prompt, exact formal question/choices and one data:image/png whose decoded bytes equal the frozen candidate. No answer metadata, design, preset, intent, original image, prior response, max_tokens or max_completion_tokens field.',
   'response_profile':'Both provider model fields agree, HTTP 200, finish_reason=stop, no truncation, empty separate thinking, reasoning_tokens=0.',
   'chronology':chronology,'harness_copy_byte_identical':evidence['harness_copy_byte_identical'],
   'harness_examination':'Read run_pair.py and both byte-identical isolated harnesses. Only PROJECT/RUNTIME filesystem constants restored in memory. Standard Quick Test 3 settings/system prompt remain unchanged; no retry loop or response-selection loop.',
   'full_raw_bindings':'raw_bindings_and_full_responses.json','all_invocation_hashes':candidate['all_invocation_file_hashes']},
 'candidate_full_final_review':candidate_finals,
 'observed_two_hit_evidence':{'candidate_invocations':1,'candidate_completed_calls':2,'preset_hits':2,
   'same_exact_png_question_design_preset_profile':True,'contradictory_final_letter_or_value':False,
   'interpretation':'Two observed, complete preset-A finals. Neither incidental mentions nor unfinished responses are counted.',
   'mechanism_limit':'Responses do not demonstrate the predeclared local no-reflection mechanism: run 1 uses false counting and imagined option colors; run 2 uses false coverage reasoning. Different/error-filled narratives do not annul the unambiguous matching finals, but prohibit strong mechanism attribution.'},
 'original_control_review':{'binding_sha256':control['binding_sha256'],'image_sha256':control['binding']['image_sha256'],
   'request_sha256':control['request_sha256'],'settings':control['binding']['settings'],'complete_finals':control_finals,
   'conclusion':'B/2:6:6 then C/5:6:9, with false reasoning in both. Controls are not consistently correct and were run after the candidate. No causal improvement, general success rate or statistical effect is established.'},
 'no_retries_or_fishing_audit':{
   'candidate_designs_for_Plane404':1,'separate_original_control_designs':1,
   'candidate_invocations':evidence['candidate_test_invocations'],'candidate_run_starts':evidence['candidate_run_starts'],
   'candidate_complete_responses':evidence['candidate_complete_raw_responses'],
   'incomplete_candidate_files':evidence['candidate_incomplete_response_files'],
   'all_binding_records':evidence['all_Plane404_bindings_in_current_experiment_tree'],
   'checkpoint_candidate_design_count_for_question':len(history['checkpoint_Plane404_design_records']),
   'global_progress_candidate_attempt_count_for_question':len(history['global_report_Plane404_attempts']),
   'no_recorded_retries_selection_or_duplicate_candidate_calls':True,
   'scope_limit':history['scope_limit'],'details':'history_and_queue_audit.json'},
 'current_authoritative_eligibility':{
   'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':elig['eligible'],
   'MathVision':True,'noPass':True,'notCollected':True,'noSpecialCompletion':True,
   'source_key':current_row['source_key'],'original_approval':current_approval,
   'current_content_sha256':elig['current_content_sha256'],'approval_matches_current_content':True,
   'authoritative_special_records':elig['authoritative_special'],'delivery_manifests':elig['existing_delivery_manifests'],
   'all_relevant_approved_source_dependencies_match_test_freeze':frozen['all_relevant_files_match'],
   'details':'current_eligibility.json and frozen_input_checks.json'},
 'specific_objections_and_disposition':[
   {'objection':'Run 1 treats annotation colors as an answer-option code and invents segment counts.',
    'disposition':'Substantive model reasoning error, disclosed. Actual formal choices contain no colors; does not create a new human mathematical given or invalidate its clear final A value.'},
   {'objection':'Run 2 contains an intermediate erroneous 8 and a different narrative.',
    'disposition':'Final pattern is 2:6:9 and final letter is A. No conflicting final exists; count as the second observed preset hit, without interpreting the narrative as proof of mechanism.'},
   {'objection':'Ignoring fold reversal everywhere would give a different triplet.',
    'disposition':'The declared candidate is a local first-digit binding intervention. Its red/blue grouping is restricted to that digit; proof explicitly distinguishes local from global no-reflection errors.'},
   {'objection':'Original controls are B/C, not both correct.',
    'disposition':'Prevents causal or success-rate claims; consistently correct controls are not an additional eligibility gate under the assignment.'},
   {'objection':'Initial no-op replay differs in file bytes from the formal PNG.',
    'disposition':'Independently isolated to the Software text metadata chunk. Decoded pixels and compressed pixel data match, while candidate replay itself is byte-exact. Not frozen-image corruption.'},
   {'objection':'Primary visual-review boilerplate mentions visible letters/options, though this PNG contains none.',
    'disposition':'Minor primary wording mismatch, recorded without editing frozen evidence. Independent inspection verifies the actual text-free PNG and exact external question/choices.'}],
 'blocking_objections':[],
 'limitations':[
   'Exactly two retained candidate calls; a descriptive observed pair, not a confidence interval, robustness rate, or proof of stochastic independence.',
   'No causal/statistical attribution, no consistently correct original control, and no model-mechanism confirmation from the error-filled narratives.',
   'No new human studies, causal experiments or per-marker ablations were required or performed. Readability is direct native-image inspection.',
   'Local timestamps and hashes establish internal consistency of retained records, not cryptographic provider attestation or proof against unrecorded external activity.',
   'Unrelated concurrent workspace edits and naturally drifting runtime progress metadata are preserved and excluded from frozen candidate corruption claims.'],
 'isolation_and_preservation':{
   'strict_guard_and_all_cache_TEMP_root':str(a.OUT),'guard_installed_before_project_or_rendering_imports':True,
   'shared_runtime_isolation_installed':True,'new_solver_calls':0,'children_delegates_threads_worktrees':0,
   'source_evidence_helper_formal_env_runtime_git_edits':0,'Pass_Collect_publication_approval_API_calls':0,
   'all_scoped_source_and_existing_evidence_hashes_unchanged':True,
   'scoped_file_count':len(end),'unrelated_concurrent_changes_preserved':True,
   'all_rendering_figures_closed':render['all_figures_closed'],'no_background_processes_started':True,
   'process_check':'no_live_processes.json','preservation_check':'final_preservation_check.json'},
 'supporting_review_files':['independent_math.json','render_and_preservation_audit.json','raw_bindings_and_full_responses.json',
    'chronology_audit.json','history_and_queue_audit.json','current_eligibility.json','frozen_input_checks.json',
    'original_png_serialization_audit.json','evidence_manifest_start.json','final_preservation_check.json','isolation.json','no_live_processes.json']
}
assert report['decision'] in ('recommended','hold','reject')
assert len(report['marker_reviews'])==5
assert all(x['counts_as_preset_hit'] for x in candidate_finals)
assert all(x in report for x in ['independent_unique_answer_proof','current_authoritative_eligibility'])
a.save('independent_review.json',report)
loaded=a.read(a.OUT/'independent_review.json')
assert loaded==report
a.emit({'decision':report['decision'],'report':str(a.OUT/'independent_review.json'),
        'report_sha256':a.sha(a.OUT/'independent_review.json'),'checked_files_unchanged':len(end),
        'current_eligible':elig['eligible'],'blocking_objections':[]})
