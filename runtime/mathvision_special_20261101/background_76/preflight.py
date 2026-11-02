import bootstrap
from bootstrap import OWNROOT,PROJECT,BASE
import json,hashlib,sys,difflib,subprocess
from pathlib import Path
from datetime import datetime,timezone
from dataset_tools.catalog import content,digest,read,rows

IDS=['Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')

reads=[]
docs=['AGENTS.md','MATHPALETTE_PROTOCOL.md']
for branch in ['PlaneGeometry','SolidGeometry']:
    docs += [branch+'/'+p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/README.md','workbench/agent_prompt.md','workbench/plugin.schema.json']]
docs += ['runtime/mathvision_special_20261101/'+p for p in ['background_76_brief.txt','background_76_assignment.json','background_66_brief.txt','background_66_assignment.json','background_65_brief.txt','background_65_assignment.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json','independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']]
for rel in docs:
    p=PROJECT/rel;txt=p.read_text(encoding='utf-8-sig')
    if p.suffix=='.json':json.loads(txt)
    reads.append({'path':str(p),'sha256':sha(p),'characters_complete_utf8_read':len(txt)})
    del txt
save(OWNROOT/'audit/prerequisite_complete_file_read_manifest.json',reads)
records={r['id']:r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl')};approvals=read(PROJECT/'provenance/approvals.json')['approvals']
index_paths=[PROJECT/'SolidGeometry/special_variant'/n for n in ['accepted_index.jsonl','collected_index.jsonl']]
index_hits={str(p):[r for r in rows(p) if r['question_id'] in IDS] for p in index_paths}
assert not any(index_hits.values())
elig={}
for q in IDS:
    r=records[q];c=content(PROJECT,'SolidGeometry',r);a=approvals[q];start=read(OWNROOT/q/'eligibility_start.json')
    sp=PROJECT/'SolidGeometry/special_variant'/q
    ok=r['source_dataset']=='MathVision' and digest(c)==a['content_sha256'] and c==start['content'] and a['reviewer']=='user' and bool(a['instruction']) and not (sp/'recipes.json').exists() and not (sp/'collection.json').exists()
    assert ok,q
    elig[q]={'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':ok,'source_dataset':'MathVision','approval_fingerprint_matches_current':True,'current_content_sha256':digest(c),'original_approval':a,'frozen_source_files':c['files'],'record_sha256':digest(r),'source_inputs_match_initial':True,'no_passed_variant':True,'not_collected':True,'no_special_completion':True,'accepted_and_collected_index_hits':[]}
save(OWNROOT/'audit/eligibility_before_first_call.json',{'questions':elig,'indexes':{str(p):sha(p) for p in index_paths},'index_hits':index_hits})

reasons={
'Solid83':('Visible-unit count gives8 for A and10 for each of B/C/D/E. Dropping hidden supports therefore produces a four-way wrong tie, not a uniquely predeclarable wrong receiver. Marking just one tied option would be arbitrary salience; marking fake support cells would change the represented object. No clean new source/receiver binding survived.','primary_count_audit.json','A has an attaining10-die support completion; other diagrams require at least12,11,11,11. Adding any additional hidden dice cannot lower these bounds. Ordinary supported stacks are used, not source pixels as extra givens.'),
'Solid85':('The proposed one-face-per-contact subtraction is monotone in contact count and still selects B: 24-e is minimized by B just as24-2e is. Thus that concrete misconception has no wrong unique answer. Visible-face count uses a different projection-dependent quantity; no nonarbitrary cross-option unit/contact binding was found that selects one wrong option while preserving the all-surface paint target. No extra painted area or arbitrary contour retained.','primary_surface_audit.json','Contacts3,4,3,3,3 give external areas18,16,18,18,18; unique minimum B.'),
'Solid121':('The proposed footprint substitution counts the four-cube white piece as3, leaving8 gray, which no option has. Counting an extra exposed face as another white cube instead leaves6 and ties A/C/D. Selecting one would need arbitrary option salience or a misleading omitted/added cube. No distinct clean feature transfer survives the actual seven-gray-cube invariant; the old U-outline objection remains unresolved.','primary_complement_audit.json','Independent24-rotation placement witness verifies18-4-7=7 and E; A/C/D6, B5.'),
'Solid130':('A real visible GG subspan exists in several choices and does not determine a complete GGW rod. Using it as a whole rod either repeats the earlier rejected partial-pair shortcut without a new information role or implies a fixed/fictitious rod decomposition. Black-width grouping can still imply a physical block boundary; colored block-edge identity has an additional source-to-composed-piece interpretation risk. No closed or false decomposition was drawn; no new human-clear substantive binding retained.','primary_exact_cover_audit.json','Independent full3D exact cover searches all54 possible oriented colored rods before exposed-color pruning. Only A has a nine-rod witness; B/C/D/E exhaust infeasible.'),
'Solid132':('After merging actual shared 3D cubies, A already has9 light,9 dark,1 white and can fill8 hidden white. B/D expose10 white, C11 white, E10 light. Pure face-patch counting rejects the valid A but does not create a unique consistent wrong choice. A single nine-cell-face highlight would again ignore the other exposed faces and repeat the old salience objection. No safe additional paint/color/cube identity was introduced.','primary_inventory_audit.json','The19 unique exposed cubies leave8 hidden; class-deficit test plus explicit A completion proves A only.'),
'Solid211':('All nine hinge cases were freshly folded, preserving the original offset L-like four-square polyomino. A correct hinge-axis correspondence reinforces six. To reject a valid remote flap by matching an already occupied face repeats the old opposite-face-to-same-face false-collision mechanism (preset5 missed), even if a different edge is chosen. No independent useful new mismatch avoiding that repetition and preserving fold semantics was retained.','primary_folding_audit.json','Valid4,5,6,7,8,9;1 and3 overlap an existing face,2 has inconsistent hinge cycle; exactly6.'),
'Solid221':('The four unlettered cells are the actual sideways T, distinct from all eight lettered candidates. New T-hinge highlighting would mainly clarify that original membership and preserve six. The only concise false planar-collision grouping found focuses C/G and repeats the prior invalid-position/complement2 design; another arbitrary receiver or a fabricated fold/face would not repair it. No copied cross-ID PNG or added face/fold was made.','primary_folding_audit.json','Independently folded all8: A,B,D,E,F,H valid; C/G have inconsistent2x2 hinge cycles. Exactly6, without copying Solid211 geometry.')}
for q,(reason,proof,mathtext) in reasons.items():
    save(OWNROOT/q/'assessment.json',{'question_id':q,'stage':'material_refinement','status':'reasoned_skip_no_new_distinct_human_clear_binding','eligible':True,'actual_original_and_formal_native_images_viewed':True,'fresh_formal_noop_pixels_match':True,'independent_math_audit':str(OWNROOT/q/proof),'independent_math_summary':mathtext,'substantive_direction_assessed':reason,'new_candidate_saved':False,'new_api_calls':0,'marker_review':{'proposed_roles_examined_before_calls':True,'no_marks_retained':True,'why_no_marker_actions':reason},'not_global_impossibility_claim':True,'not_a_quota_saving_skip':True,'original_65_66_directions_are_not_presets_proofs_or_approvals':True})

out=OWNROOT/'Solid151/face_center_inventory_to_core_confusion'
save(out/'primary_native_visual_review.json',{'reviewer_role':'primary researcher only; not independent second review','actual_native_candidate_viewed':True,'dimensions':[768,768],'all_ten_patterns_and_labels_readable':True,'findings':'The10 short colored intervals locate exactly four given black face centers and E black center. Each top/bottom pair remains an open locator; no new cell, face, painted region, corner template, equality symbol or fold appears. All black/white interiors and the distinguishing A-white/E-black center remain clear.','semantics':'The task is an inventory of uniformly black/white unit cubes, not transport of printed cards or colored edging. Thin styles on existing unit-grid spans leave those two cube-material classes intact. Same-color spans cue a position class, not physical identity of different face centers or an added equality given.','each_marker_review_path':str(out/'marker_path_bindings.json'),'unique_answer_after_marks':'A','independent_math_audit_path':str(OWNROOT/'Solid151/primary_cube_identity_audit.json'),'critical_error_exposed':'E forces16 exterior black cubes; a fully hidden interior can add0or1 black, never subtract1.','limits':['No causal ablation or human study.','Primary review only; any doublehit requires parent NEW independent delegate before delivery.'],'candidate_png_sha256':sha(out/'candidate.png')})

# Local-only relocation: exactly one PROJECT resolution line changes; payload/profile code is untouched.
original=BASE/'harness/quicktest3_isolated.py';data=original.read_bytes();old=b'PROJECT = Path(__file__).resolve().parents[3]';new=b"PROJECT = next(p for p in Path(__file__).resolve().parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())"
assert data.count(old)==1
relocated=data.replace(old,new);h=OWNROOT/'harness/quicktest3_isolated.py';h.parent.mkdir(exist_ok=True);h.write_bytes(relocated)
save(OWNROOT/'audit/harness_relocation_byte_diff_audit.json',{'source':str(original),'source_sha256':sha(original),'relocated':str(h),'relocated_sha256':sha(h),'allowed_change_only':'PROJECT local root resolution; HARNESS naturally resolves beneath OWNROOT. No payload/model/thinking/systemprompt/API/privatecredential/token/timeout/profile/retry code changed.','exact_bytes_inverse_restore_original':relocated.replace(new,old)==data,'unified_diff':''.join(difflib.unified_diff(data.decode().splitlines(True),relocated.decode().splitlines(True),fromfile='original',tofile='ownroot_relocation')),'solver_profile':'mimo-v2.6-flash thinking.disabled','runs':2,'no_connectivity_ping':True})

png_hash=sha(out/'candidate.png');binding_matches=[];png_matches=[];binding_count=0;png_count=0
listing=subprocess.check_output(['rg','--files',str(BASE)],text=True,encoding='utf-8').splitlines()
for n in listing:
    p=Path(n)
    if p.is_relative_to(OWNROOT):continue
    if p.name=='binding.json':
        j=read(p);binding_count+=1
        if j.get('image_sha256')==png_hash:binding_matches.append(str(p))
        del j
    elif p.name=='candidate.png':
        png_count+=1
        if sha(p)==png_hash:png_matches.append(str(p))
assert not binding_matches and not png_matches
save(out/'global_zero_prior_call_audit.json',{'before_any_own_api_call':True,'candidate_png_sha256':png_hash,'all_existing_binding_records_scanned_one_at_a_time':binding_count,'all_existing_candidate_PNGs_hashed_one_at_a_time':png_count,'prior_exact_image_bindings':binding_matches,'prior_exact_candidate_PNG_matches':png_matches,'own_started_request_count':len(list(OWNROOT.rglob('run_*_started.json'))),'new_image_not_copied_from_failed_or_aborted_other_ID':True})
save(OWNROOT/'checkpoint_pre_api.json',{'unit':'background_76','stage':'material_refinement','assessed_question_ids':IDS,'unworked_question_ids':[],'reasoned_skips':list(reasons),'new_frozen_candidate':'Solid151/face_center_inventory_to_core_confusion','immutable_wrong_preset':'E','actual_new_api_calls':0,'owned_live_requests':0,'fresh_eligibility_all8_pass':True,'local_math_parser_assertion_corrected_before_any_API':'First Solid130 extractor assumed generic face IDs, stopped at assertion before API; corrected to actual *_front/right/top_*_fill IDs and all full exact-cover checks passed. No allocation/import/render error occurred.','source_model_configuration_override':False,'independent_second_review_pending_only_if_candidate_doublehit':True})
print(json.dumps({'assessed':8,'reasoned_skips':7,'candidate':'Solid151','preset':'E','prior_bindings':binding_count,'prior_pngs':png_count,'prior_exact_matches':0,'new_api_calls':0}))
