from tools27 import *
reviews={
 'Plane159':'Native768px image: red lower edges form the nonwhite source union and E black union. Original nine positions and all white/grey/black broad fills remain distinct, including white gaps at2/4/7. No connectors or extra squares; A remains uniquely correct.',
 'Plane203':'Native768px: six open unit edges visibly bind bottom-source to top-target edges for a halfturn. All six grey cells and all A/B/C/D/E letters remain clear. Black crease atx3 is unchanged; red endpoint at(6,2) is an existing grid intersection. No fill or square was added.',
 'Plane292':'Native768px: orange next mirror remains dashed; every other dotted axis, source arrows, grey final triangle and three drawn kangaroos remain intact. The last shown ear/tail and A ear/tail are colored on existing tiny anatomical features. Silhouettes are distinguishable at native size; feature colors are small, so zoom/display sensitivity is disclosed.',
 'Plane362':'Native768px: 2008 source and8005D are readable. Red and green vertical pairs distinguish source2 handed sides from rightmost5 inD; blue8 bars reverse end position. Other digits and five labels retain original black strokes, with no added bar or fill.',
 'Plane371':'Native768px: K diagonal and both trailing O outer arcs correspond to D opposite word ends. All black glyph interiors, white counters and glass edges remain distinguishable. Visibility audit confirms each individual action changes55..96 pixels. Partial O arcs are small and display sensitivity is disclosed; six roles remain useful word-end correspondence.',
 'Plane444':'Native768px: source red origin edge and blue outer cap correspond to C red far-left edge and blue cap beside yaxis. The source origin crossing, all10-point contours and every axis/label remain clear. Colored intervals are short open original edges, with no relation symbols or new line.'
}
for q,review in reviews.items():
    folder=next((HERE/q).glob('r27_*'))
    d=json.loads((folder/'design.json').read_text(encoding='utf-8'))
    write(folder/'primary_visual_review.json',{'stage':'material_refinement','review_type':'PRIMARY ONLY, not independent',
        'reviewed_at':now(),'actual_candidate_png_viewed':True,'actual_original_png_viewed':True,
        'viewed_at_native_resolution':'768x768','review':review,'proceed_to_API':True,
        'all_marker_roles':d['marker_roles'],'question_answer_geometry_fill_text_projection_visibility_unchanged':True,
        'readable_original_distinctions_and_unique_original_answer_preserved':True,
        'schema_and_no_op_and_determinism':'render_check.json','image_sha256':file_hash(folder/'candidate.png'),
        'design_sha256':file_hash(folder/'design.json'),'difference_audit_sha256':file_hash(folder/'design_difference_audit.json'),
        'limits':['No original control evidence exists for these8 old question folders; no fresh controls will be called.','No human/statistical/causal or per-marker necessity claim.','A doublehit is only a primary possibility, requiring NEW parent independent review before delivery.']})
