"""Write the independent reviewer's conclusions; no external evidence is edited."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

assert sys.dont_write_bytecode
ROOT=Path(__file__).resolve().parents[4]
TASK=ROOT/'runtime/mathvision_special_20261101'
OWN=TASK/'independent_review'

def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def fh(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(own,d):
    path=own/'independent_review.json'
    path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(d['question_id'],d['decision'],str(path))

common_limits=[
    'Two candidate calls and two separate original controls per case are descriptive observations only. No statistical improvement, population rate, human performance effect or marker-level causal necessity is established.',
    'Complete narratives were read, but the final-letter records do not establish identical internal reasoning or a correct mathematical derivation by the solver. Correct original controls and identical narratives were not imposed as extra gates.',
    'No new solver/API call, renderer invocation, subagent/delegate, Pass, Collect, submission or publication was performed. All own scripts, caches and reports are confined to the two designated independent_review folders; Python -B was used. No project module was imported and no render cache was created outside those folders.',
    'Parent portable replay reports were inspected instead of rerunning a renderer. Their retained exact reproduced PNGs were independently byte-compared and hashed. Primary no-op baseline and repeated-render records were checked against current formal inputs.',
    'Human readability and interpretation are independent visual judgments of the actual source/formal/candidate images, not results of a human study.',
    'Historical exploration_report.json and remaining_questions.jsonl hashes differ from current progress metadata. The original diagnostics remain unchanged; current eligibility was independently established from formal datasets, user approval content hashes and actual Special accepted/collected records.'
]

for q,worker,v in [('Solid142','solid_worker','orthogonal_cut_feature_swap'),('Plane233','plane_parts','two_U_partial_partition_binding')]:
    own=OWN/f'{q}_{v}'
    e=read(own/'evidence_audit.json');m=read(own/'independent_math.json')
    c=TASK/'background_06'/worker/q/v
    source_branch='SolidGeometry' if q.startswith('Solid') else 'PlaneGeometry'
    candidate=e['candidate'];control=e['original_controls']
    checks={
        'brief_and_protocols': {'status':'verified','read_in_full':'review_batch_06_brief.txt',
            'read':['MATHPALETTE_PROTOCOL.md',source_branch+'/REDRAW_PROTOCOL.md',source_branch+'/workbench/README.md',source_branch+'/workbench/agent_prompt.md',source_branch+'/dataset_generator/protocol.json',source_branch+'/workbench/plugin.schema.json'],
            'authority':'Explicit user review-only instructions override designer CLI/context/submit workflow; no live workbench was contacted.'},
        'authoritative_current_eligibility': {'status':'verified','source_dataset':'MathVision','source_key':e['formal_source_key'],
            'formal_record_sha256':e['formal_record_sha256'],'approval_content_sha256':e['recomputed_approval_content_sha256'],
            'user_original_approval_time':e['original_approval']['approved_at_utc'],
            'user_approval_instruction':e['original_approval']['instruction'],
            'approval_fingerprint_recomputed_matches':True,'no_existing_special_pass_or_collect':True},
        'source_question_and_label_ownership': {'status':'verified', **e['source_record'],
            'finding':'Actual source and formal images were viewed; options A through E belong to the displayed shapes, with no moved/rebound labels. The formal question is unchanged in the actual solver request.'},
        'schema_path_and_style': {'status':'verified','actual_schema_validated':True,'schema_validation_errors':e['schema_validation_errors'],
            'style_actions_bind_original_geometry':True,'new_points_lines_text_cells_or_fills':False,
            'exact_vector_path_sha256_recomputed':True,'partial_interval_checks':'See independent_math.json and evidence_audit.json.'},
        'unchanged_frozen_inputs': {'status':'verified','fingerprinted_file_count':e['frozen_fingerprint_file_count'],
            'mismatches':e['frozen_fingerprint_mismatches'],'world_projection_visibility_fills_labels_dimensions_and_view_unchanged':True,
            'actual_rgba_difference_scope':e['pixel_difference_scope']},
        'render_reproducibility': {'status':'verified_existing_artifacts','no_op_formal_baseline':e['no_op_baseline'],
            'primary_repeat':e['primary_repeated_bytes'],'parent_two_portable_replays':e['parent_portable_replay_report'],
            'retained_reproduced_png_matches_current_tested_bytes':True},
        'two_complete_predeclared_candidate_calls': {'status':'verified','same_frozen_png':True,
            'png_sha256':candidate['png_sha256'],'pixel_sha256':candidate['pixel_sha256'],
            'design_snapshot_sha256':candidate['design_snapshot_sha256'],'request_sha256':candidate['request_body_sha256'],
            'design_declared_at':candidate['created_at'],'preset_before_each_start':True,
            'profile':'quicktest3 / mimo-v2.6-flash / thinking.type=disabled',
            'solver_input':'Unchanged existing system prompt + exact formal question + candidate PNG only. No answer, preset, intent, original image or drawing parameters.',
            'stateless':'Two separate two-message requests with distinct local run IDs and provider completion IDs; no previous assistant response in either request. Provider prompt caching is recorded and does not add conversation history.',
            'runs':candidate['runs'],'all_http200_stop_completed_not_truncated':True},
        'original_controls_kept_separate': {'status':'verified','png_is_exact_formal_original':True,
            'request_sha256':control['request_body_sha256'],'runs':control['runs'],
            'candidate_and_control_records_not_mixed':True},
        'math':{'status':'verified','correct_answer':m['unique_correct_answer'],'proof_artifact':'independent_math.json'},
        'visual_and_information':{},
        'review_evidence_artifacts':{'evidence_audit.json':fh(own/'evidence_audit.json'),'independent_math.json':fh(own/'independent_math.json')},
    }
    report={
        'decision':'recommended' if q=='Solid142' else 'reject',
        'question_id':q,'candidate_directory':c.relative_to(TASK).as_posix(),
        'candidate_path':str((c/'candidate.png').resolve()).replace('\\','/'),
        'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
        'reviewer':'New independent second reviewer; performed both case reviews personally; not a designer.',
        'scope':'Exactly the two named primary possibilities, with their separate original controls; no other candidate assessed.',
        'recommendation_status':'Independent recommendation only; never user Pass/Collect or formal approval.',
        'formal_correct_answer':e['formal_answer'],'preset_wrong_answer':'A' if q=='Solid142' else 'B',
        'candidate_png_sha256':candidate['png_sha256'],'checks':checks,'issues':[],
        'rationale':[],'marker_necessity':{},'limitations':list(common_limits),
        'manually_read_candidate_finals':['A','A'] if q=='Solid142' else ['B','B'],
        'manually_read_control_finals':['C','C'],
        'all_eight_full_raw_responses_read_personally':True,
        'actual_images_viewed':[source_branch+'/originals/'+q+'.jpg',source_branch+'/image/'+q+'.png',(c/'candidate.png').relative_to(ROOT).as_posix()],
    }
    if q=='Solid142':
        checks['visual_and_information']={
            'status':'satisfies_gate','actually_viewed_native_768_candidate':True,
            'givens':'Both real V notches, the partly opened folded stack and all A-E panels remain readable. Gray material regions, white hole interiors, outlines, labels and canvas remain intact.',
            'independent_reflection':'Use orthonormal axes (p2-p1)/2 and (p7-p1)/2. Upper notch endpoints (0.83,2),(1.17,2), apex (1,1.7055513627) reflect in v=2 to a rhombus of width .34 and height .5888972746; its duplicate occupies left/right positions. Left notch endpoints (0,1.17),(0,.83), apex (.2944486373,1) reflect in u=0 to horizontal rhombi at top/bottom. C alone has these four orientations and no central hole.',
            'notch_binding':'line16 has 10 ordered segments. [.3,.5] is exactly p14-p15-p16, [.7,.9] is exactly p18-p19-p20. The front packet is congruent to the rear square in world 3D. The exact stored path controls and 7ec1c604af8d1cb5cd032e04e6ea2b509d729ab335ea2f691bd6d0adb824edeb were independently verified.',
            'human_information_assessment':'Two colors distinguish two actual cut features and propose correspondence to two actual spatial hole families in A. The optional correspondence can be geometrically checked and rejected by reflection; no new fold, new cut, color legend, equality sign, connecting assertion or changed hole is supplied. All four colored A contours describe the target features rather than its outer box or answer label. I find no material ambiguity in the underlying unfolding problem for this exact image.',
            'conciseness':'Six style actions express two source features and four output holes. No unrelated contour or empty visual accent was found.'}
        report['rationale']=[
            'Recommend the exact frozen Solid142 candidate: independent world-coordinate reflection establishes unique C, while the predeclared wrong A is the unambiguous final answer of both complete calls against the same PNG.',
            'The red/blue marks encode a specific mistaken notch-to-hole-family correspondence, with a concrete role for every action and without concealing the geometry needed to disprove it.',
            'Formal MathVision approval, absence of Special Pass/Collect, current frozen inputs, schema, path fingerprint, request/design/response binding and portable deterministic replay evidence all check out.'
        ]
        roles=[
            'Trace the two real sides of the upper notch; distinguish the source feature from the perpendicular left notch.',
            'Trace the two real sides of the left notch; supply the second source feature needed for orthogonal unfolding correspondence.',
            'Trace the top A hole as one red member of the proposed upper-notch destination family.',
            'Trace the bottom A hole as the reflected red partner; completes that proposed family.',
            'Trace the left A hole as one blue member of the proposed left-notch destination family.',
            'Trace the right A hole as its reflected blue partner; completes that proposed family.'
        ]
        plugin=read(c/'plugin.json')
        report['marker_necessity']={'geometric_roles_verified':True,'actions':[{'action_index':i,'action':a,'role':roles[i]} for i,a in enumerate(plugin['params']['actions'])],
            'pair_truth':'Red upper notch is paired in A with top/bottom; blue left notch is paired with left/right. True reflection gives the reverse positional family and the required orthogonal orientations. The mark is a proposed misleading correspondence, not a correct derivation.',
            'necessity_meaning':'Each action carries one concrete feature or family member. This is a structural relevance judgment, not a claim that deleting any one action would change the model outcome.'}
        report['manual_final_reading']={
            'candidate':[{'run':1,'final':'Therefore, the correct unfolded pattern is shown in Option A.','notes':'Explicitly uses red/blue correspondence; wrongly infers diagonal folding and color retention.'},
                         {'run':2,'final':'The unfolded napkin matches the pattern in **Choice A**.','notes':'Explicitly selects the two colored hole families; misdescribes triangular notches as rectangular/square and treats color as decisive.'}],
            'controls':[{'run':1,'final':'**Correct Answer:** **C**','notes':'Correct letter, speculative generic pattern matching and erroneous fold/layer descriptions.'},
                        {'run':2,'final':'**Final Answer:** Option C','notes':'Correct letter, false center-corner cut and touching-hole explanation. Actual C holes are separated.'}]}
        report['limitations'] += [
            'Original C/C controls have incorrect narratives. The observed C/C versus A/A letter difference is not evidence of a correct reasoning process becoming incorrect, nor a causal effect estimate.',
            'The original uses a schematic partly opened zero-thickness stack; the independent proof follows its frozen two-perpendicular-fold geometry. Construction coordinates and chosen notch dimensions are not added as numerical givens.',
            'Direct image comparison found 19 changed grayscale antialias/join pixels on unchanged black parts of line16 beyond the two colored intervals (maximum channel delta 27). All differences remain on the original styled object strokes; no coordinate, fill, label or frozen visibility change was found.'
        ]
    else:
        checks['visual_and_information']={
            'status':'fails_unambiguous_original_givens_gate','actually_viewed_native_768_candidate':True,
            'readability':'All 15 board cells, the missing lower-right corner, original black grid, five option shapes and their labels remain legible. Two red U silhouettes can be traced despite their common color and two shared unit boundary segments. No extraneous or duplicate edge is present.',
            'independent_enumeration':{k:{key:v2 for key,v2 in val.items() if key in ['orientation_count','placement_count','solution_count','unordered_triples_exhausted']} for k,val in m['options'].items()},
            'highlighted_patches':m['marked_patches'],'complement':m['complement'],'complement_components':m['complement_components'],
            'literal_red_cut_reading_areas':m['if_red_edges_are_given_cuts_areas'],
            'text':'The formal question says the grid "was divided into three equal pieces" and asks which figure represents "one of these pieces".',
            'human_information_assessment':'At native size, thicker red closed contours visibly separate the two five-cell U regions from the finer black unit grid. The matching closed red B boundary reinforces reading these source contours as the already-given division, rather than as optional trial placements. No wording/visual convention in the solver input marks them as hypothetical. This is a reasonable concrete reading of this exact text+PNG, even though another reader may ignore the contours and solve the original tiling problem.',
            'consequence':'Taking the red contours as given cuts yields four connected regions of areas 5,5,3,2, not three equal pieces. The five leftover cells form separate 2- and 3-cell components. Under the optional-trial reading A is uniquely correct; under the given-division reading the pictured conditions are incompatible. Visible leftovers expose the inconsistency but do not disambiguate which status the red contours have.',
            'primary_review_objection':'The primary statement that styling does not force cuts is insufficient: preserving the scene coordinates and maintaining black-grid visibility does not establish unambiguous human semantics.'}
        report['issues']=[{
            'severity':'blocking','code':'closed_source_contours_reasonably_read_as_given_incompatible_division',
            'evidence':'Original past-tense division wording + two full thick red board U boundaries + same-color complete B boundary; literal highlighted-cut graph has regions 5,5,3,2.',
            'impact':'The exact candidate does not preserve an unambiguous statement of the original givens. This is a candidate presentation failure, not a formal-source/approval/hash failure.'}]
        report['rationale']=[
            'Reject this exact frozen Plane233 presentation for the human/information gate. The two closed highlighted source boundaries can reasonably be taken as the fixed division named by the question, and that division cannot satisfy the original three-equal-pieces condition.',
            'Independent full enumeration verifies the unchanged abstract tiling problem: A has two covers; B,C,D,E have zero. Both marked U patches are real, disjoint and congruent to B, but their complement is disconnected. Mathematical uniqueness under an optional-highlight convention does not resolve the convention ambiguity in the actual image.',
            'The technical evidence and both predeclared B final hits are valid. Rejection is not based on 34 unit actions, failed controls, narrative differences, missing human studies or absent ablation. Every styled edge has a real contour role; their combined semantic presentation causes the failure.'
        ]
        report['marker_necessity']={'geometric_roles_verified':True,'actions':m['all_34_exact_roles'],
            'counts':{'unique_board_unit_segments':22,'B_boundary_unit_segments':12,'each_U_perimeter':12,'shared_board_unit_segments':2,'total_unique_actions':34},
            'shared_edges':m['shared_board_boundary_edges'],
            'structural_finding':'The 22 source actions are exactly the union of two complete real U boundaries; the 12 B actions are exactly its U perimeter. No duplicate, isolated, unrelated or additional cell/line/text action was found. Black internal unit edges and the five-cell complement remain visible.',
            'necessity_meaning':'Each segment closes a specified contour. These roles justify the fine-grained action count and establish relevance; they do not cure the incompatible-given-division reading and are not a statistical deletion experiment.'}
        report['manual_final_reading']={
            'candidate':[{'run':1,'final':'B','notes':'Unambiguous final B; falsely counts A/D as four cells and invents 3x5 rectangles inside the board.'},
                         {'run':2,'final':'Answer: **B**','notes':'Unambiguous final B; explicitly treats red lines as cuts and matches the red source U to B. Miscounts C/D and never checks the remaining five cells.'}],
            'controls':[{'run':1,'final':'Therefore, the figure that represents one of the pieces is (C).','notes':'Wrong C; invalid L/rectangle argument and inconsistent cell placement.'},
                        {'run':2,'final':'**C**','notes':'Wrong C; proposed pieces have inconsistent areas and do not cover the board with three congruent pentominoes.'}]}
        report['limitations'] += [
            'Original controls are also wrong (C/C). This is an observed C/C-to-B/B change in output letters, not an observed increase from correct to incorrect responses; correct controls were not an additional gate.',
            'The original puzzle convention interprets equal pieces as congruent grid pieces and permits rotation/reflection. This standard interpretation yields the formal unique A; no new condition was introduced in the independent enumeration.',
            'The human ambiguity finding is about this exact closed-contour presentation and the actual past-tense question. It does not assert that all colored grid boundaries add mathematical conditions, or that numerous useful marks are categorically unacceptable.'
        ]
    save(own,report)

    # Final readback of exact existing inputs; no source/evidence file is rewritten.
    assert fh(c/'candidate.png')==report['candidate_png_sha256']
    for key in ['candidate','original_controls']:
        for run in e[key]['runs']:
            assert fh(ROOT/run['response_path'])==run['response_sha256']
