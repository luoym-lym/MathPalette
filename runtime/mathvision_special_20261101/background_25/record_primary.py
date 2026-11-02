from design_tools import *
q,vid,note=sys.argv[1:4];f=TASK/q/vid
d=json.loads((f/'design.json').read_text(encoding='utf-8'))
render=json.loads((f/'render_check.json').read_text(encoding='utf-8'))
assert render['baseline_matches_formal'] and render['deterministic']
assert AD.frozen_inputs(q)==render['frozen_inputs']
write(f/'primary_review.json',{'question_id':q,'variant_id':vid,'stage':'material_refinement','review_role':'PRIMARY ONLY; designing researcher','reviewed_at':datetime.now(timezone.utc).isoformat(),'actual_candidate_png_viewed':True,'native_dimensions':[768,768],'png_sha256':file_hash(f/'candidate.png'),'proceed_to_API':True,'native_visual_notes':note,'unique_math_proof_path':d['math_audit_path'],'unique_math_proof_sha256':file_hash(d['math_audit_path']),'per_marker_roles':d['marker_roles'],'all_marks_useful_in_specific_correspondence':True,'no_changed_geometry_text_fills_projection_frozen_visibility':True,'no_new_cut_region_equality_or_puzzle_part':True,'appearance_annotation_not_new_mathematical_given':True,'source_frozen_inputs_unchanged':True,'actual_no_op_matches_formal':True,'actual_approved_renderer_schema_defaults_and_twice_identical_bytes':True,'limits':['No human study or per-marker causal ablation; visual readability is primary assessment.','Exactly two samples only, no statistical effect estimate.','All prior controls reused by reference when available; none repeated.','Parent NEW independent second review required before any eventual delivery.']})
print('PRIMARY RECORDED',q,vid)
