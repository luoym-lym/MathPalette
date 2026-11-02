from prepare import *

VISUAL = {
 'r32_ear_content_preserving_comparison':'Actually viewed the complete native 768x768 PNG. Given, B and C each show red left and blue right shoulders. B retains the sloping source shoulders; C has visibly lower/flatter shoulders. At 1 pt the white triangles remain open and identifiable, with no mark on the eye, nose, head, mouth or A-E labels. All six individual colored segments were inspected. Small source heads remain a genuine display limitation, not a claim of effortless comparison.',
 'r32_wedge_print_preserved_halfturn_alternative':'Actually viewed the complete native 768x768 PNG. Source red left V, B red right V, and D red bottom V are all identifiable. The required physical red print is present in B. Both existing downward and right motion references, the blank intermediate reverse, the question mark, all five labels and black fills remain clear. D has rising full diagonal, B and source descending full diagonal. No arrow was added or modified.',
 'r32_nose_extent_preserved_comparison':'Actually viewed the complete native 768x768 PNG. Given small downward nose and B same small downward nose have red sloping sides. A has an obviously taller red-sided downward nose. The black interiors and the tip/base distinction remain visible; red does not hide C inner-ear flattening, D upward nose or E circular nose. Every individual V was inspected; the narrow tip/eye contact in A and B is inherited geometry, not a new point.',
 'r32_diagonal_print_preserved_singleflip':'Actually viewed the complete native 768x768 PNG. Source and B have a full red descending diagonal; A has a full red rising diagonal. Both halves of every selected diagonal and its actual corner endpoints were inspected. Source/B wedge positions differ by the correct half-turn. All black fills, unselected wedge legs, card outlines, original flip references, blank reverse and labels remain visible. The red diagonal is an existing printed stroke, not an added cutting boundary.'
}

def preflight():
    for plan in PLANS:
        qid=plan['qid'];out=ROOT/qid/plan['variant']
        grounding=read(out/'per_marker_grounding.json')
        scene=read(ROOT/qid/'formal_scene_snapshot.json')
        obs={o['id']:o for o in scene['objects']}
        pairs=[(0,2,'given','B'),(1,3,'given','B')] if 'ear_' in plan['variant'] else [(0,1,'given','B')]
        if qid=='Plane295':
            for i,j,source,answer in pairs:
                aa=np.array(grounding[i]['selected_original_controls'])-np.array(obs['givenhead']['center'])
                bb=np.array(grounding[j]['selected_original_controls'])-np.array(obs['Bhead']['center'])
                assert np.allclose(aa,bb,atol=1e-12,rtol=0)
        else:
            def normalize(controls,frame):
                pts=np.array(obs[frame]['points']); lo=pts.min(axis=0);hi=pts.max(axis=0)
                return (np.array(controls)-lo)/(hi-lo)
            aa=1-normalize(grounding[0]['selected_original_controls'],'o1')
            bb=normalize(grounding[1]['selected_original_controls'],'o207')
            def vertices(x): return sorted(set(tuple(round(float(v),12) for v in p) for p in x.reshape((-1,2))))
            assert vertices(aa)==vertices(bb)
        render=read(out/'render_audit.json')
        assert render['schema_normalization_idempotent'] and render['fresh_no_op_pixel_equal_formal'] and render['candidate_and_repeat_byte_identical']
        assert render['candidate_sha256']==sha(out/'candidate.png')
        assert read(out/'design.json')['expected_wrong_answer']==plan['wrong']
        assert 'design_difference_audit.json' in [p.name for p in out.iterdir()]
        save(out/'primary_review.json',{'created_at':now(),'review_level':'PRIMARY ONLY; no independent self-review','question_id':qid,'variant_id':plan['variant'],'candidate_sha256':sha(out/'candidate.png'),'design_sha256':sha(out/'design.json'),'plugin_sha256':sha(out/'plugin.json'),'formal_native_and_actual_source_and_old_images_viewed':True,'actual_new_native_candidate_viewed':True,'native_visual_findings':VISUAL[plan['variant']],'per_marker_review':[dict(row,native_visual_status='Individually inspected; actual feature remains readable; no extra point, line, region, relation, text, piece or occluded diagnostic.',mathematical_role=plan['roles'][i]) for i,row in enumerate(grounding)],'primary_unique_original_math':str(ROOT/qid/'primary_original_math.json'),'unique_answer_preserved_under_intrinsic_color_reading':'B; selected source controls map exactly to the selected B controls under head translation or the required half-turn. Color, path and position all transported; no hue-exemption convention or legend required.','unique_answer_if_comparison_highlights_ignored':'B by unchanged anatomy or card geometry.','source_to_correct_colored_controls_verified':True,'schema_and_frozen_render_audit':str(out/'render_audit.json'),'source_mouth_caveat':read(ROOT/qid/'primary_original_math.json').get('source_wording_caveat'),'proceed_to_API':True,'limits':['Two calls cannot establish a causal effect, rate estimate, human performance or per-marker necessity.','No same-question original controls exist in the supplied old evidence; none repeated.','Parent must start a NEW independent review for EVERY eventual delivery, including these repaired rejected questions.']})
    save(ROOT/'additional_preparation_errors.json',[{'stage':'local view snapshot','error':"AttributeError: tuple bounds has no tolist",'resolution':'Converted bounds to list before serialization; no solver call made.'},{'stage':'local fill preservation check','error':'First audit compared the scene.artists mapping after edge replacement against the old mapping. Partial style intentionally maps targets to replacement edge patches, so that mapping is not the set of original fills.','resolution':'Captured actual original filled artist references before styling and compared those exact fill paths, facecolors, visibility and transforms after styling. All passed. No source change, renderer bypass or API retry.'}])
    print(json.dumps({'designs_native_viewed_and_primary_passed':len(PLANS),'solver_calls_so_far':0}))

if __name__=='__main__': preflight()
