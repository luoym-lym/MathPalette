import review_bootstrap as b
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
from dataset_tools import catalog

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

BASE=b.PROJECT/'runtime/mathvision_special_20261101'
UNIT=BASE/'background_16'
QROOT=UNIT/'Solid197'
CAND=QROOT/'crease_side_binding'
audit=read(b.ROOT/'audit_bindings.json')
render=read(b.ROOT/'render_and_geometry_audit.json')
history=read(b.ROOT/'history_and_manifest_audit.json')
primary=read(CAND/'primary_review.json')
selected=read(b.ROOT/'selected_primary_and_history.json')
record=next(r for r in catalog.rows(b.PROJECT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid197')
approval=read(b.PROJECT/'provenance/approvals.json')['approvals']['Solid197']
current_digest=catalog.digest(catalog.content(b.PROJECT,'SolidGeometry',record))
special=b.PROJECT/'SolidGeometry/special_variant'
current_eligibility={
    'checked_at':datetime.now(timezone.utc).isoformat(),
    'formal_record':record,'formal_question_utf8_sha256':hashlib.sha256(record['question'].encode()).hexdigest(),
    'formal_record_canonical_sha256':catalog.digest(record),
    'formal_MathVision':record['source_dataset']=='MathVision',
    'approval':approval,'current_approval_content_sha256':current_digest,
    'original_approval_valid':approval['reviewer']=='user' and bool(approval['instruction']) and bool(approval['approved_at_utc']) and current_digest==approval['content_sha256'],
    'accepted_index_matches':[r for r in catalog.rows(special/'accepted_index.jsonl') if r.get('question_id',r.get('id'))=='Solid197'],
    'collected_index_matches':[r for r in catalog.rows(special/'collected_index.jsonl') if r.get('question_id',r.get('id'))=='Solid197'],
    'recipes_exists':(special/'Solid197/recipes.json').exists(),
    'collection_exists':(special/'Solid197/collection.json').exists(),
    'question_special_directory_exists':(special/'Solid197').exists(),
}
current_eligibility['noPass']=not current_eligibility['accepted_index_matches'] and not current_eligibility['recipes_exists']
current_eligibility['notCollected']=not current_eligibility['collected_index_matches']
current_eligibility['noSpecialCompletion']=not current_eligibility['collection_exists']
current_eligibility['current_eligible']=all(current_eligibility[k] for k in ['formal_MathVision','original_approval_valid','noPass','notCollected','noSpecialCompletion'])
current_eligibility['authoritative_file_hashes']={p:sha(b.PROJECT/p) if (b.PROJECT/p).exists() else None
    for p in audit['current_eligibility']['authoritative_hashes']}
assert current_eligibility['current_eligible']
assert approval==audit['current_eligibility']['approval'] and record==audit['current_eligibility']['formal_record']

protected_changes=[]
for p,expected in audit['read_only_baseline'].items():
    actual=sha(p) if Path(p).is_file() else None
    if actual!=expected:protected_changes.append({'path':p,'expected':expected,'actual':actual})
assert not protected_changes,protected_changes

protocol_paths=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md',
                'SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md',
                'SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
file_bindings={p:sha(b.PROJECT/p) for p in protocol_paths}
for p in [*QROOT.rglob('*'), UNIT/'primary_math_proofs.json',UNIT/'source_preservation_final.json',
          UNIT/'quicktest3_isolated.py',UNIT/'run_pair.py',UNIT/'errors_and_aborts.json',UNIT/'second_review_queue.json',
          BASE/'Solid197_firstpass_independent_review_brief.txt',BASE/'Solid197_pre_review_evidence_check.json']:
    if p.is_file():file_bindings[p.relative_to(b.PROJECT).as_posix()]=sha(p)

def reviewed_runs(kind):
    answer=[]
    for entry in audit['evidence'][kind]:
        for run in entry['runs']:
            r=run['record']
            text=run['raw_response']['choices'][0]['message']['content']
            if kind=='crease_side_binding':
                final='Final Answer: 450' if r['run_index']==1 else 'Answer: The total area of the stickers used is $450 \\mathrm{~cm}^{2}$.'
                error=('Uses s/2 for the axial reach of a rotated square whose true reach is s/sqrt(2); solves for 5 as if it were a side. It briefly counts 30 face incidences, then explicitly resolves to 18 physical stickers. Final 18*25=450 is unambiguous.'
                       if r['run_index']==1 else
                       'Hallucinates the central diamond vertices at cube-face side midpoints, obtains area 50, then contradicts identical-sticker areas and inconsistently assigns edge areas. The final 300+150=450 is explicit. This is not a coherent execution of the proposed side/diagonal substitution.')
            else:
                final=('The total area of the stickers used is **$450 \\mathrm{~cm}^{2}$**.' if r['run_index']==1 else
                       'The total area of the stickers used is **450 cm$^2$**.')
                error='Assumes a sticker side is 5 cm and multiplies 18*25. It misdescribes the unannotated diamond/edge arrangement; the wrong final 450 is explicit.'
            assert text.endswith(final),final
            answer.append({'run_index':r['run_index'],'run_id':r['run_id'],
                           'raw_response_id':run['raw_response']['id'],
                           'started_at':r['started_at'],'finished_at':r['finished_at'],
                           'raw_path':run['raw_path'],'raw_response_sha256':run['raw_sha256'],
                           'run_record_path':run['run_path'],'run_record_sha256':run['run_sha256'],
                           'started_record_sha256':run['started_sha256'],
                           'full_final_body_sha256':run['complete_body_sha256'],
                           'full_final_body_manually_read':text,'exact_terminal_final':final,
                           'manual_final_value':'450','pre_call_preset':'450','manual_preset_hit':True,
                           'is_wrong_against_independent_unique_answer_225':True,
                           'contradictory_terminal_letter_or_value':False,
                           'not_counted_from_incidental_mentions':True,
                           'finish_reason':r['finish_reason'],'status':r['status'],
                           'response_model':r['response_model'],'truncated':r['truncated'],'usage':r['usage'],
                           'binding_checks':run['checks'],'narrative_disposition':error,
                           'explicit_color_as_given_claim':'Neither candidate response explicitly mentions red or treats equal color as a stated equality; no such mechanism can be inferred from silence.'})
    return answer

candidate_entry=audit['evidence']['crease_side_binding'][0]
control_entry=audit['evidence']['control_original'][0]
with Image.open(CAND/'candidate.png') as im:
    png_metadata=dict(im.info)
assert set(png_metadata).issubset({'Software','dpi'})
design=read(CAND/'design.json')
marker1={
    'id':'central_side','legality':'legal','normalized_action':read(CAND/'plugin.json')['params']['actions'][0],
    'target':'frontsticker0 vertex 0 to vertex 1: lower-right gray/white boundary of the central front-face sticker',
    'world_endpoints_unit':[[.5,0,.25],[.75,0,.5]],
    'world_endpoints_cm':[[5,0,2.5],[7.5,0,5]],
    'projected_endpoints':[[.5,.25],[.75,.5]],
    'exact_snap_ids':['vertex_4b5ba3372ae697f9','vertex_1ab5fc0c26b10ce6'],
    'path_semantics':'An existing visible semantic-fill boundary; the face is not a styleable stroke. add_line legitimately traces its exact two displayed vertices. No path_id/interval/hash is required by add_line; none is fabricated.',
    'physical_role':'A true material side of a single central square sticker; not its diagonal.',
    'true_length_cm':'5/sqrt(2)','native_length_px':render['marker_geometry'][0]['length_px'],
    'information_role':'Identifies the actual square side for comparison with the longer fold diagonal. This is specific length-feature targeting, not whole-choice or whole-object salience.',
    'human_clarity':'At native 768 pixels the complete central diamond remains recognizable, all four corner contacts remain visible, and the thin red segment lies on exactly one existing side. It adds no chord, internal division, corner dot, text, or equality symbol.',
    'preservation':'Original gray fill remains on its original side of the same boundary; no original artist or world coordinate changes.',
    'disposition':'satisfied'}
marker2={
    'id':'fold_crease','legality':'legal','normalized_action':read(CAND/'plugin.json')['params']['actions'][1],
    'target':'frontsticker2 vertex 0 to vertex 1, shared in reverse by rightsticker4; central half of visible cube100_cube101',
    'world_endpoints_unit':[[1,0,.25],[1,0,.75]],'world_endpoints_cm':[[10,0,2.5],[10,0,7.5]],
    'projected_endpoints':[[1,.25],[1,.75]],
    'exact_snap_ids':['vertex_d75e4c84dbefc149','vertex_d743ced46a57648f'],
    'coincident_existing_cube_path':{'target':'cube100_cube101','path_id':'p0',
        'path_sha256':'ee9ee9f2375aebe85632f42691a8796ae4fed4b6f1dd0411a4b1e25f81decff3',
        'parameter_interval':[.25,.75],'closed':False,
        'note':'Describes independently checked correspondence; the actual normalized operation is add_line, not set_object_style.'},
    'physical_role':'Internal fold crease/diagonal of ONE square sticker spanning the two adjacent cube faces. It bounds the front triangular representation, but is NOT a material outer side or a cut between two stickers.',
    'true_length_cm':'5','native_length_px':render['marker_geometry'][1]['length_px'],
    'information_role':'Localizes exactly the crease length that can be confused with the side selected by central_side. Endpoints are genuine square corners on the cube edge.',
    'human_clarity':'The red segment overlays an already visible solid cube edge. Both triangular gray halves and their shared endpoints remain visible. It does not introduce a new line through a formerly continuous face, a new closed contour, a separate triangular sticker, or an extra given.',
    'preservation':'Original front/right polygons, solid edge geometry, camera and visibility remain unchanged; only the color of the overlaid visible stroke pixels differs.',
    'disposition':'satisfied'}

report={
    'question_id':'Solid197','variant_id':'crease_side_binding','branch':'SolidGeometry',
    'decision':'recommended','reviewer_role':'NEW independent second reviewer; task performed directly without child agents',
    'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Recommendation on mathematical rigor, actual human picture semantics, legal concise feature-targeted annotation, frozen two-hit evidence and current eligibility. No user approval, Pass, Collect, or publication.',
    'recommendation_reasons':[
        'The text plus actual source/candidate geometry gives the unique answer 225 cm^2; the crease and true sticker side are distinguished correctly.',
        'Both exact 1 pt red add_line marks target existing visible features, use exact displayed source vertices, and preserve the original scene, fill, text, projection and visibility.',
        'Native-size inspection finds no new relation, cut, closed region or plausible alternative physical sticker partition. Equal color is a comparison cue here; it is not an equality notation.',
        'Both complete raw candidate responses end unambiguously in the pre-call preset 450 on the same frozen PNG under the exact quicktest3 nonthinking profile.',
        'The current formal MathVision record and original user approval are valid; no Pass, collection or special completion exists.'
    ],
    'protocol_and_evidence_file_sha256':file_bindings,
    'actual_images_inspected':[
        {'path':str(b.PROJECT/'SolidGeometry/originals/Solid197.jpg'),'sha256':sha(b.PROJECT/'SolidGeometry/originals/Solid197.jpg'),'view':'actual source JPG at original resolution; three faces each show a central diamond and four corner-contact edge triangles'},
        {'path':str(b.PROJECT/'SolidGeometry/image/Solid197.png'),'sha256':sha(b.PROJECT/'SolidGeometry/image/Solid197.png'),'view':'actual formal 768x768 PNG at native resolution'},
        {'path':str(CAND/'candidate.png'),'sha256':sha(CAND/'candidate.png'),'pixel_sha256':render['candidate_pixel_sha256'],'view':'actual frozen candidate 768x768 PNG at native resolution'},
        {'path':str(b.ROOT/'candidate_reproduced_01.png'),'sha256':sha(b.ROOT/'candidate_reproduced_01.png'),'view':'independent isolated byte-identical reproduction inspected; original candidate inspection remains the primary native readability evidence'}
    ],
    'independent_unique_answer_proof':{
        'basis':'Formal question and actual source JPG/formal PNG/native candidate. The following derivation does not use the stored answer, source solution, or primary proof as a premise.',
        'diagram_facts':[
            'The central sticker is a square turned 45 degrees in the front face, with diagonals along the face horizontal and vertical midlines.',
            'Each edge sticker crosses a cube edge along a diagonal: its two congruent right-isosceles triangular halves lie on the two adjacent faces, with their common hypotenuse along that edge. This is visible directly at the marked front/right edge.',
            'The apex of each half-sticker touches a central-square corner; no positive area overlaps occur. These contact and orientation facts come from the diagram included by the question phrase as shown.'
        ],
        'contact_equation':'Let r be the distance from the centre of a square sticker to one vertex, i.e. half its diagonal. Along the front face vertical midline, the lower edge half-sticker extends r upward, the central square extends 2r, and the upper edge half-sticker extends r downward. Their corner contacts give r+2r+r=10, hence r=2.5 cm. Equivalently the face-centre to edge-midpoint distance is 5=2r.',
        'diagonal_side_area':'Every identical square has diagonal d=2r=5 cm, side s=d/sqrt(2)=5/sqrt(2) cm, area d^2/2=25/2 cm^2.',
        'explicit_unfolding':'In a 10 cm front-face coordinate chart the marked edge has crease endpoints (10,2.5) and (10,7.5), front apex (7.5,5), and the adjacent right-face apex unfolds to (12.5,5). These four vertices form one square with both diagonals 5. Its crease is an internal diagonal, not one of its four material sides. The marked central side runs (5,2.5) to (7.5,5) and has length sqrt(2.5^2+2.5^2)=5/sqrt(2).',
        'physical_count_including_unseen':'A cube has 6 faces and 12 edges. The instruction uses 6 whole central stickers plus 12 whole edge stickers, totaling 18 physical squares, including the invisible faces and edges. The 24 face incidences of edge half-stickers pair into 12 whole stickers; do not count those halves as additional stickers.',
        'total':'18*(25/2)=225 cm^2',
        'independent_world_area_crosscheck':'Computed 3D polygon cross-product areas from the actual frozen vertices: each displayed face has a central area 1/8 plus four half-sticker areas 1/16 each, i.e. 3/8 of its 100 cm^2. All six faces give 6*100*3/8=225 cm^2.',
        'uniqueness':'The included diagonal-fold/contact arrangement fixes r by 4r=10. No red annotation supplies a size or equality. Interpreting the 5 cm crease as a square side would conflict with the visible square and its corner contacts. There is no second total consistent with the unchanged question and pictured arrangement.',
        'derived_answer':'225','matches_formal_answer_after_independent_derivation':record['answer']=='225'
    },
    'markers':[marker1,marker2],
    'human_semantics':{
        'disposition':'satisfied','schema_legality_alone_used_as_semantic_proof':False,
        'matching_color_assessed_on_actual_picture':'Both red segments are thin, open, disjoint and exactly feature-aligned. There are no matching ticks, dimension labels, arrows, equal signs or legend giving color a metric meaning. The front face is undistorted, so their unequal displayed lengths (about 172 and 244 px, ratio sqrt(2)) are directly visible. Same-color pairing highlights side versus crease for comparison without making them equal.',
        'crease_boundary_objection':'The crease separates two rendered face patches but passes through the interior of a whole physical sticker. Calling both marked segments material boundaries is factually imprecise. The native picture nevertheless retains both gray halves and the pre-existing cube edge, while the question expressly says one sticker across each edge. A triangular-sticker or new-cut reading contradicts those retained cues.',
        'no_new_partition':'The central line follows a pre-existing gray/white boundary, and the fold line follows an existing solid cube edge. Neither crosses an unpartitioned face or closes a new loop. The gray regions are unchanged; the candidate does not introduce a new shaded unit or source contour that forces incompatible partitions.',
        'normal_size_readability':'At the native 768x768 size both 1 pt red strokes are visible and endpoint precise; the central diamond, four corner contacts, front/right folded halves and cube silhouette remain clear. There are no embedded text labels to occlude. This is actual reviewer visual judgment, not a measured human-study result.',
        'comparison_annotation_not_automatically_new_given':True,
        'specific_targeting_and_concision':'Each of the two marks has a distinct, necessary role in the intended side-versus-diagonal comparison. No numeric mark cap is assumed.',
        'human_wrong_answer_rate_established':False
    },
    'preservation_and_reproduction':render,
    'frozen_source_current_binding':{
        'all_initial_frozen_files_rehashed_match':not audit['frozen_input_mismatches'],
        'file_hash_pairs':audit['frozen_inputs'],
        'formal_record_matches_pretest_snapshot':audit['record_matches_snapshot'],
        'source_notes_caveat':'The frozen scene contains an unrelated legacy sentence mentioning source 1352/glass. The actual formal question/source key here is test:1877 and does not mention glass. This stale metadata does not enter the solver request or geometry and was preserved, not repaired.'
    },
    'two_hit_evidence':{
        'disposition':'satisfied','predeclared_wrong_answer':'450','independent_correct_answer':'225',
        'design_created_at':design['created_at'],'design_sha256':sha(CAND/'design.json'),
        'plugin_sha256':sha(CAND/'plugin.json'),'candidate_png_sha256':sha(CAND/'candidate.png'),
        'binding':candidate_entry['binding'],'binding_sha256':candidate_entry['binding_sha256'],
        'request_sha256':candidate_entry['request_sha256'],'design_snapshot_sha256':candidate_entry['design_snapshot_sha256'],
        'request_inspection':candidate_entry['request_sanitized'],'exact_binding_checks':candidate_entry['checks'],
        'png_metadata':png_metadata,
        'no_leak':'Exact decoded image bytes match the candidate. The only textual messages are the reference system prompt and exact formal question. No stored answer, wrong preset, intent, design, plugin, source image, added instruction, previous response, filename, token cap or reasoning override is supplied. PNG metadata contains only software and DPI.',
        'profile_source_sha256':audit['profile_source_sha256'],'harness_sha256':audit['harness_sha256'],
        'profile_verified_without_loading_credentials':'Parsed literal TEST_PROFILES, SYSTEM_PROMPT and MIMO_API_BASE from the current quick_test.py; exact binding match and unchanged referenced source hash. No .env read or new solver call.',
        'complete_manually_read_runs':reviewed_runs('crease_side_binding'),
        'same_frozen_png_two_completed_calls':True,
        'no_retries_selection_or_fishing_found':True,
        'history_archive_audit':history,
        'mechanism_limit':'The two erroneous explanations differ and do not prove the intended perceptual mechanism. Run 2 is internally incoherent despite its unambiguous terminal 450. No narrative is accepted as geometry evidence.'
    },
    'original_controls':{
        'original_png_byte_identical_to_formal':(QROOT/'control_original/candidate.png').read_bytes()==(b.PROJECT/'SolidGeometry/image/Solid197.png').read_bytes(),
        'binding':control_entry['binding'],'binding_sha256':control_entry['binding_sha256'],
        'request_sha256':control_entry['request_sha256'],'exact_binding_checks':control_entry['checks'],
        'complete_manually_read_runs':reviewed_runs('control_original'),
        'manual_finals':['450','450'],
        'disposition':'Original controls also produce 450/450, exactly the candidate final values. No incremental annotation effect, causal gain, reliability gain, or superiority over the original is established.',
        'not_extra_hard_gates':'Correct controls, identical narratives, a new human study, statistical significance, causal attribution and per-marker ablations were not required and are not imposed.'
    },
    'current_authoritative_eligibility':current_eligibility,
    'concrete_objections_and_dispositions':[
        {'objection':'Primary design and visual wording calls both marks material boundaries.','disposition':'Nonblocking factual wording correction recorded here only: central_side is a material side; fold_crease is an internal crease/diagonal, also a patch boundary and cube edge. The frozen design was not changed.'},
        {'objection':'Same red color might invite an unsupported equality inference.','disposition':'Examined on actual image, not waved away by schema. No equality convention is present, unequal lengths are visible, no new geometry is drawn, and the original square/contact arrangement remains readable. Acceptable comparison annotation with a perceptual risk, not an added condition.'},
        {'objection':'Candidate repeated wrong finals might be presented as an induced improvement.','disposition':'Not supported: both original controls are already 450. Recommendation is limited to the requested observed two-hit and rigorous readable-variant criteria.'},
        {'objection':'Run 2 does not follow the primary proposed error mechanism.','disposition':'Recorded as an erroneous narrative with an explicit wrong final. It is neither mathematical proof nor a causal attribution; divergent narratives are not an extra failure gate.'}
    ],
    'blocking_objections':[],
    'limitations':[
        'Only the two existing completed candidate calls and two separate original controls were audited; no new solver calls were made.',
        'Two wrong answers are observations, not a statistical reliability estimate or proof of the proposed visual mechanism.',
        'Original controls also 450/450: no incremental effect has been established.',
        'Native-size readability and unique human interpretation are independent reviewer judgments, not new participant-study results.',
        'No causal or per-marker ablation evidence; none is invented or made an extra gate.',
        'Hashes and timestamps verify consistency of the available immutable evidence archive; they do not provide external provider attestation or rule out undisclosed/deleted files.',
        'Mutable exploration_report/remaining_questions snapshots can drift during concurrent work. Such metadata is diagnostic and is not treated as frozen scene or raw-response corruption.'
    ],
    'workspace_and_process_scope':{
        'assigned_new_output_root':str(b.ROOT),'isolation':b.ISOLATION,
        'preexisting_protected_files_rechecked':len(audit['read_only_baseline']),
        'protected_file_changes_during_review':protected_changes,
        'whole_workspace_unchanged_claim':False,
        'unrelated_concurrent_workbench_changes':'Preserved; no restore, mutation or author attribution. Only scoped current question and frozen inputs are certified.',
        'historical_progress_snapshots_modified':False,
        'formal_state_changes':False,'helper_source_changes':False,'prior_evidence_changes':False,
        'env_or_git_changes':False,'pass_collect_approval_or_publication_api_calls':0,
        'new_solver_calls':0,'nested_agents_or_delegates_or_threads_or_worktrees':0,
        'background_processes_started':0,'render_figures_closed':render['all_figures_closed']
    },
    'supporting_new_audits':{p.name:sha(p) for p in [b.ROOT/'audit_bindings.json',b.ROOT/'selected_primary_and_history.json',
                                                    b.ROOT/'render_and_geometry_audit.json',b.ROOT/'history_and_manifest_audit.json']},
    'approval_status':'Recommendation only; no user Pass/Collect/publication/approval recorded by this reviewer.'
}
assert report['decision'] in ('recommended','hold','reject')
dump(b.ROOT/'independent_review.json',report)
print(json.dumps({'decision':report['decision'],'report':str(b.ROOT/'independent_review.json'),
                  'report_sha256':sha(b.ROOT/'independent_review.json'),
                  'blocking_objections':report['blocking_objections'],'current_eligible':current_eligibility['current_eligible'],
                  'protected_files_unchanged':len(audit['read_only_baseline'])},indent=2))

def omit_repeated_bodies(x):
    if isinstance(x,dict):return {k:omit_repeated_bodies(v) for k,v in x.items() if k!='full_final_body'}
    if isinstance(x,list):return [omit_repeated_bodies(v) for v in x]
    return x
dump(b.ROOT/'primary_review_nonduplicated.json',omit_repeated_bodies(primary))
