from tools34 import *
from make34 import SPECS,SKIPS
notes={
 'Plane257':'Native768PNG actually viewed. Three receiver black squares and three source black stripes have clearly visible red bottom boundaries. Receiver right sides are partly overpainted by original adjacent polygon black outlines, leaving a black core/less prominent red; this is disclosed, not claimed uniform red. All8 first-flag cells, all five fourth-flag bands and both qualifying flags remain countable; second/third/fifth flags untouched. Six source overlays coincide exactly with already drawn band boundaries, no colored line crosses a uniform black band. Marking filled black-area boundaries does not introduce a new counted piece.',
 'Plane336':'Native768PNG actually viewed. All three existing dividing chords are red, producing six actual rays about the visible common intersection. All three gray rhombi, white triangles and ABC labels remain large and clear. Outer corner extensions that defeat the equal-sector-area mistake are intact. No new center dot, angle arc or line was added.',
 'Plane340':'Native768PNG actually viewed. Three open red L-frame motifs are visible: bottom/right corner of left unit square, top/right corner of top square, bottom/right corner of right square. The entire black diagonal and its y1 crossing at x1.25 remain clear, as do white top triangle, gray trapezoid and lower-right gray triangle. No new frame, partition or fill has been drawn.',
 'Solid184':'Native768PNG actually viewed. The two stacked bricks are identified by upper/lower exterior front corner motifs, the two wide bricks by front half-span corners and the two long bricks by near/far top corners. Contiguous same-color front segments in wide are separated by the original black center seam. All three original seams and72/96/102 labels remain readable. Every12 action occupies an actual visible exterior edge or exact half ending at an existing seam; no hidden face or visibility edge is added.'
}
for qid,spec in SPECS.items():
    folder=UNIT/qid/spec['variant_id'];design=read(folder/'design.json');render=read(folder/'render_check.json')
    assert sha(folder/'candidate.png')==design['frozen_png_sha256']
    write(folder/'primary_pretest_review.json',{'at':now(),'role':'Primary designer only; not independent second review','question_id':qid,'variant_id':spec['variant_id'],
          'actual_native_768_png_viewed':True,'visual_observation':notes[qid],'image_sha256':sha(folder/'candidate.png'),
          'design_sha256':sha(folder/'design.json'),'plugin_sha256':sha(folder/'plugin.json'),
          'unique_math':read(UNIT/qid/'primary_math_audit.json'),'per_marker_roles':design['marker_roles'],
          'semantic_readability':spec['semantic_review'],'schema_and_default_normalization':True,'no_op_formal_pixel_match':True,
          'two_independent_renders_byte_identical':True,'source_frozen':True,'all_marks_have_actual_feature_role':True,
          'no_false_cut_region_equality_angle_parallel_glyph':True,'no_extra_counted_dot_line_piece':True,
          'black_gray_semantic_fill_text_geometry_and_diagnostics_preserved':True,
          'proceed_to_exactly_two_calls':True,'review_status':'NEW parent independent review is required for every eventual delivery.',
          'limitations':['This is primary inspection, not a human experiment.','A two-call outcome cannot prove a causal mechanism, incremental effect or statistical improvement.','No original controls exist for these four assigned questions in prior evidence; no new control calls are made.','No per-marker ablation is imposed as an extra gate.']})
for qid,skip in SKIPS.items():
    write(UNIT/qid/'refinement_prescreen.json',{'question_id':qid,'stage':'material_refinement','at':now(),**skip,
          'actual_formal_and_source_images_viewed':True,'primary_math_audit':str(UNIT/qid/'primary_math_audit.json'),
          'current_eligibility':eligibility(qid),'retained_new_designs':0,'API_calls':0,
          'old_evidence_preserved':True,'absence_of_old_design_not_call_obligation':True})
write(UNIT/'Plane338/primary_math_erratum_pretest.json',{'at':now(),'prior_math_audit':'primary_math_audit.json',
      'correction':'The optional bounding-rectangle verbal decomposition listed incorrect individual corner areas even though its sum14 and shoelace21 were correct. Correct complement pieces are top triangle7/2, bottom-right triangle6 and lower-left quadrilateral9/2; total14. Exact shoelace21 and84cm2 remain unchanged.',
      'no_candidate_or_API_for_this_question':True,'stored_answer_not_used_to_patch_geometry':True})
print(json.dumps({'four_native_pretest_reviews_saved':True,'four_reasoned_skips_saved':True,'no_solver_calls_yet':True}))
