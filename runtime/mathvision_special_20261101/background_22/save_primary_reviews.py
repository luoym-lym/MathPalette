from unit_tools import *
for qid,name,findings in [
('Plane482','four_tile_single_window_binding',[
    'Viewed actual 768x768 candidate and source JPG individually. Four input diagonals remain identifiable by their original gray side; same colors on the four sides of the existing example diamond match all four orientations correctly.',
    'All 9 blank grid cells, 4 tile samples and 9 example cells remain visible. Eight 2pt existing diagonal styles do not add a cut or a region; the multicolor closed diamond exactly follows an existing gray boundary.',
    'Each of eight marks belongs to one of four genuine tile-to-example feature pairs. Local focus on this one event is the intended probability omission. This is information correspondence, not option salience; options are only in unchanged question text.'
]),
('Plane481','two_strip_overlap_binding',[
    'Viewed actual 768x768 candidate and source JPG individually. Red marks group NW and SE exposed arm portions; blue marks group NE and SW arm portions. Original gray union, all grid lines and both Math Team words remain clear.',
    'Twelve existing outer edges are 2pt color styles. Each edge identifies one exposed boundary of one true diagonal strip, including its two end caps. No central line has been added and no new inner cut or puzzle piece is suggested.',
    'A human can count four full central unit cells and twelve half-cells, area 10, or subtract area-2 overlap from two area-6 strips. The color grouping targets omission of the overlap; it does not explicitly state additivity.'
]),
('Solid201','two_yes_identity_edge_overlay',[
    'Viewed actual 768x768 candidate and source JPG individually. All three die views and nine no/YES/maybe words remain readable, with original within-face directions unchanged.',
    'Three red existing top-left edges group left YES observations; first top/front-right boundary and second top/rear boundary are blue. Open-edge marks provide the two intended cross-view identity groups and never frame an arbitrary answer option.',
    'Five declared add_line operations exactly coincide with current snap-endpoint projections of the named native edges. They are 1pt solid overlays, not 2pt object styles. This clarifies inherited general color/width wording in design semantic_review; actual normalized plugin and image are authoritative.',
    'Colors alone do not become permanent markings on the physical die or new face-identity givens. The problem stays solvable using original printed orientations; fresh enumeration of all 576 proper-rotation pairs proves exactly three YES faces. A second reviewer must independently judge whether this visual identity cue remains unambiguous for humans.'
])]:
    p=HERE/qid/name
    design=read(p/'design.json')
    actions=read(p/'plugin.json')['params']['actions']
    roles=[]
    for i,(a,r) in enumerate(zip(actions,design['marker_roles'])):
        roles.append({'index':i,'normalized_action':a,'role':r['information_role'],'primary_actual_image_check':'visible, follows intended original edge; no label or semantic fill obscured','not_an_extra_given':True})
    write(p/'primary_review.json',{'reviewer':'background_22 primary designer','independent_second_review':False,'reviewed_at':now(),'candidate_png_sha256':sha(p/'candidate.png'),'plugin_sha256':sha(p/'plugin.json'),'design_sha256':sha(p/'design.json'),'original_png_viewed':True,'source_jpg_viewed':True,'native_size_actual_candidate_viewed':True,'math_proof':str((HERE/qid/'primary_math.json').relative_to(HERE)),'primary_unique_answer_preserved':True,'visual_findings':findings,'per_marker_review':roles,'primary_test_admissible':True,'qualification_status':'Untested, unapproved; eventual possibility requires NEW independent parent reviewer.','controls':[],'limitations':['No human performance experiment or statistical marker ablation.','Any paired miss is retained; unchanged images will not be retried.']})
for qid in IDS:
    write(HERE/qid/'source_primary_audit.json',{'question_id':qid,'audited_at':now(),'formal_question_read_in_full':True,'formal_png_individually_viewed':True,'source_jpg_individually_viewed':True,'source_jpg_sha256':sha(HERE/qid/'source.jpg'),'formal_png_sha256':sha(HERE/qid/'original.png'),'fresh_context_saved':True,'exact_object_paths_saved':True,'no_op_pixel_equals_formal':read(HERE/qid/'baseline_check.json')['no_op_pixel_equal'],'original_approval_and_eligibility_checked':read(HERE/qid/'eligibility_initial.json')['eligible'],'geometry_text_semantic_fill_preserved':True,'three_dimensional_projection_visibility_immutable':qid.startswith('Solid'),'primary_only':True})
print('Saved actual-image and per-marker primary reviews before solver calls.')
