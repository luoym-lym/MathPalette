from tools27 import *

OLD=json.loads((HERE/'old_evidence_index.json').read_text(encoding='utf-8'))
R='#DC2626';B='#2563EB';G='#16A34A';O='#EA580C'

def context(q):return json.loads((HERE/q/'context.json').read_text(encoding='utf-8'))
def part(q,oid,start,end,color,width=1.5):
    t=next(t for t in context(q)['canvas']['targets'] if t['id']==oid)
    p=t['partial_paths'][0]
    return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width,
            'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
def whole(oid,color):return {'type':'set_object_style','target':oid,'color':color}

def make(q,v,preset,old_summary,difference,mechanism,proof,actions,roles):
    assert v.startswith('r27_')
    folder=HERE/q/v
    write(folder/'design_difference_audit.json',{'stage':'material_refinement','question_id':q,'variant_id':v,
        'saved_at':now(),'saved_before_any_new_solver_call':True,'old_evidence':OLD[q],
        'all_old_distinct_pngs_natively_viewed':True,'byte_identical_repeat_PNGs_reviewed_by_hash_equivalence':True,
        'all_old_designs_plugins_primary_reviews_and_FULL_raw_model_replies_read':True,
        'prior_independent_objections':[], 'old_outcomes_honestly_preserved':old_summary,
        'substantive_new_information':difference,'new_mechanism':mechanism,'new_wrong_answer_frozen_before_calls':preset,
        'not_cosmetic_or_posthoc':True,'original_math_proof':proof,'planned_actions':actions,
        'marker_roles':roles,'human_semantics':'Appearance marks on existing edges only; no new condition, fill, text, cut or moved geometry. Native candidate QA still required before API.'})
    render(q,v,actions,preset,mechanism,proof,roles)
    ob={o['id']:o for o in context(q)['objects']}
    bindings=[]
    for i,a in enumerate(actions):
        target=next(t for t in context(q)['canvas']['targets'] if t['id']==a['target'])
        bindings.append({'action_index':i,'action':a,'frozen_source_object':ob[a['target']],
                         'full_precision_frozen_partial_paths':target.get('partial_paths'),
                         'role':roles[i] if len(roles)==len(actions) else roles})
    write(folder/'exact_marker_bindings.json',bindings)
    write(folder/'primary_math_audit.json',{'question_id':q,'variant_id':v,'proof':proof,'unique_original_answer':eligibility(q)['formal_record']['answer'],
        'all_marks_use_existing_paths':True,'no_added_endpoints_or_paths':True,'no_changes_to_question_answer_fill_labels_geometry_projection_visibility':True,
        'additional_numeric_audit':str(HERE/q/'fresh_transform_math.json') if (HERE/q/'fresh_transform_math.json').exists() else None,
        'primary_only':True,'requires_NEW_parent_independent_review':True})

q='Plane159';v='r27_dark_class_union_skip_first'
acts=[];roles=[]
for prefix in ['source','E']:
    for i in [0,2,4,5,7,8]:
        acts.append(part(q,f'{prefix}{i}',0,0.25,R))
        roles.append(f'{prefix} cell {i+1} bottom edge belongs to the union of ORIGINAL black and grey positions. The same red union in source and E binds retained-black and grey-to-black cells as one dark class, encouraging omission of the first replacement. White gaps and all broad fills remain unmarked and visible.')
make(q,v,'E','Old simultaneous_class_binding presetB finalsB/A; first_stage_black_transfer presetB finalsD/A. Both misses; no controls or independent review found.',
     'Old designs isolated ORIGINAL black->white or kept three original classes separate. New grouping deliberately MERGES original black AND grey into a single dark-origin class, mapping both to E black while leaving original white gaps grey. This changes the information partition and predicts omission of step1, rather than simultaneous three-class replacement.',
     'Group all nonwhite input cells with E black cells; tempt applying only grey->black and white->grey, forgetting initial black->white.',
     'Initial nine cells B,W,G,W,G,B,W,B,G. Sequential steps send original B->W->G, original W->G, original G->B. Final G,G,B,G,B,G,G,G,B equals A alone. E=B,G,B,G,B,B,G,B,B instead omits step1. Red bottom edges change no fill, number of cells, class distinction or ordering.',acts,roles)

q='Plane203';v='r27_lower_L_halfturn_row_swap'
acts=[part(q,'o18',0,0.25,R),part(q,'o9',5/6,1,R),
      part(q,'o16',0,0.25,B),part(q,'o8',5/6,1,B),
      part(q,'o17',0,0.25,G),part(q,'o8',4/6,5/6,G)]
roles=[
 'Red source lower-L bottom cell(0,0) BOTTOM edge is the first halfturn source member.',
 'Red target cell(5,1) TOP edge is its false halfturn destination, using (c,r)->(5-c,1-r).',
 'Blue source cell(0,1) BOTTOM edge identifies the common corner member of the lower L.',
 'Blue target C cell(5,0) TOP edge is its halfturn destination, reversing vertical order as well as horizontal order.',
 'Green source cell(1,1) BOTTOM edge identifies the upper-right arm member.',
 'Green target E cell(4,0) TOP edge maps that arm below C rather than to the true D row; thus the false lower L covers C/E and misses D.'
]
make(q,v,'D','Old lower_L_translation_binding presetC finalsB/E; three_unit_edge_translation presetC finalsB/None. Both misses; no controls found.',
     'Both old designs translated the lower L +4 columns with unchanged row order. New design uses an actual HALF TURN of that L about(3,1), reversing BOTH columns and rows and pairing bottom edges with top edges. The new wrong result uniquely leaves D, not old presetC. Upper-L reflection remains human-readable and unchanged.',
     'Bind the lower three grey cells to a halfturned L covering C and E; confuse a halfturn with the requested vertical reflection.',
     'Zero-based grey cells: (1,3),(2,3),(2,2),(0,1),(1,1),(0,0). True reflection x=3 gives (4,3),(3,3),(3,2),(5,1),(4,1),(5,0). Letters A=(3,3),B=(4,3),C=(5,0),D=(4,1),E=(4,0); E alone uncovered. False lower-L halfturn gives(5,1),(5,0),(4,0), with upper L correctly reflected, so A/B/C/E covered and D omitted. Six existing edge intervals change no grey fill, grid, crease or letter.',acts,roles)

q='Plane292';v='r27_next_fold_intermediate_stop'
n=369
acts=[whole('o8',O),part(q,'o23',0.6612466124661247,0.7262872628726287,R),
      part(q,'o27',0.6612466124661247,0.7262872628726287,R),whole('o25',B),whole('o29',B)]
roles=[
 'Orange third dotted mirror o8 identifies the NEXT reflection after the two already shown; original dash pattern and all five axes remain visible.',
 'Red short tail-bend interval on the LAST shown kangaroo identifies the current input state, rather than the initial kangaroo used in the old design.',
 'Red homologous tail-bend interval on A binds the one-next-reflection result to the wrong final answer.',
 'Blue existing ear stroke on last shown kangaroo adds a local head orientation feature.',
 'Blue corresponding ear stroke on A binds the next-stage head orientation; both tail and ear agree with the third reflection but not the required fifth.'
]
make(q,v,'A','Old initial-tail/ear-toB presetB finalsC/C; both missed own preset and cannot be relabeled. No controls found.',
     'Old initial-source anatomical pairing toB invited a single-axis shortcut from the first kangaroo. New pairing starts from the LAST shown state (after2 reflections), singles out the next existing dotted mirror, and maps to the EXACT intermediate after3 reflections (A). The misconception is terminating two stages early, not changing the old C/C observed answer into a preset.',
     'Focus on the next fold from the last drawn kangaroo and stop at intermediate A instead of continuing through the remaining two mirrors.',
     'Apply five exact reflection matrices along o2,o5,o8,o11,o14 to all369 ordered original contour vertices. E alone matches after5 (<4e-15; other options>0.42). A alone matches after3 (<2e-15). New ear/tail outlines and mirror color retain every original contour, grey target fill, black option fill, arrow and dotted axis. See fresh_transform_math.json.',acts,roles)

q='Plane362';v='r27_horizontal_mirror_side_order'
acts=[whole('o1',R),whole('o116',R),whole('o3',G),whole('o118',G),whole('o23',B),whole('o102',B)]
roles=[
 'Red original2 UPPER-RIGHT vertical segment is a handed input feature.',
 'Red D rightmost5 UPPER-LEFT segment is its horizontal-mirror image, rather than its true vertical-flip lower-right image.',
 'Green original2 LOWER-LEFT segment identifies the complementary handed feature separately.',
 'Green D rightmost5 LOWER-RIGHT segment is its horizontal-mirror partner, proving a side exchange, not unchanged2.',
 'Blue original rightmost8 middle bar anchors the opposite end of the four-digit word.',
 'Blue D leftmost8 middle bar creates a reversal of word order, combined with the reflected2->5 side pair.'
]
make(q,v,'D','Old unchanged-digit presetA finalsC/A; old reverse-order presetC finalsC(value2005 inconsistent with C8002)/A. Both misses; no controls found.',
     'Old A pairing kept both digit order and2 handedness, while old C pairing reversed order but retained2. New D pairing reverses order AND changes2 to5 by matching upper-right to upper-left and lower-left to lower-right as DISTINCT feature pairs. It targets a horizontal mirror alone (omitting the halfturn), not either old rule, and is derived from actual D8005 geometry.',
     'Apply horizontal mirror to the whole2008 word, producing8005=D, while omitting the upside-down halfturn.',
     'Halfturn R=-I followed by horizontal mirror M=diag(-1,1) gives M R=diag(1,-1). This preserves word order and vertically flips2 to5; 0,0,8 are invariant. Correct result5008=B. Horizontal mirror alone reverses order and flips2 to5, giving8005=D. All142 original segment endpoints are unchanged and every digit remains legible; no strokes or labels added.',acts,roles)

q='Plane371';v='r27_word_end_reversal_bundle'
# K diagonal arm edge and the two O outer half-contours are distinct word-end groups.
acts=[part(q,'o1',2/11,3/11,R),part(q,'o69',2/11,3/11,R),
      part(q,'o11',0,0.5,B),part(q,'o60',0,0.5,B),
      part(q,'o13',0,0.5,B),part(q,'o58',0,0.5,B)]
roles=[
 'Red source K upper diagonal edge identifies the asymmetric LEADING word end.',
 'Red D rightmost K corresponding vertically flipped diagonal puts that leading end at the opposite word end.',
 'Blue source first O outer half-contour is one member of the trailing OO bundle.',
 'Blue D second O outer half-contour binds it at the opposite end under reversed letter order.',
 'Blue source last O outer half-contour supplies the second member of the terminal repeated pair.',
 'Blue D first O outer half-contour finishes the reversed OO bundle, discriminating word-level order from local glyph handedness.'
]
make(q,v,'D','Old N/G handedness-toA presetA finalsD/B (both miss). No original controls found.',
     'Old design focused two INTERNAL glyph outlines N/G in fixed positions and wrongA handedness. New design binds the asymmetric LEADING K and terminal repeated OO as WORD-END groups to opposite ends ofD, while their individual glyphs are vertically flipped. It targets failure to cancel the two order reversals, not unchanged N/G geometry. Exact D glyph comparisons independently show vertical flips with reversed slot order.',
     'Preserve the vertical flip of individual glyphs but reverse the word order only once; match K and OO to opposite ends of D.',
     'Flip about the right edge reverses x and glyph order; the subsequent in-plane halfturn reverses x again and y once. Composition is(x,y)->(x,-y)+translation, so left-to-right slot order remains KANGAROO and every glyph vertically flips. All14 full contours including glass uniquely matchE (residual0; A-D differ). D has reversed glyph order although each K/N/G/O local contour is a vertical flip. The six partial outer edges leave black letters and white counters unchanged.',acts,roles)

q='Plane444';v='r27_origin_anchor_to_extreme'
acts=[part(q,'o2',0,0.1,R,2),part(q,'o11',0.1,0.2,R,2),
      part(q,'o2',0.7,0.8,B,2),part(q,'o11',0.8,0.9,B,2)]
roles=[
 'Red source F origin-adjacent short horizontal bottom edge identifies which end of the transformed stem must stay at the origin.',
 'Red C far-left short vertical edge is the shape-congruent partner under true orientation plus WRONG translation(-5,0). It moves the origin-adjacent end away from the origin.',
 'Blue source outer cap vertical edge identifies the other extremity of F, separate from the origin edge.',
 'Blue C high right horizontal cap is its matching partner; together the two pairs bind an entire local orientation while exposing the wrong axis anchoring.'
]
make(q,v,'C','Old whole-F source/C uniform outlines presetC finalsE/E (miss). No independent review or controls found.',
     'Old two uniform full outlines supplied no selective information and described left/right orientation. Fresh exact vertices showC actually has the TRUE transformed orientation translated5units to the left. New four partial edges encode the ORIGIN-adjacent end versus far cap correspondence, inviting bounding-shape matching while ignoring fixed-origin anchoring. This is a concrete semantic repair and a new geometric mistake, not merely reduced width/color on the old outlines.',
     'Match the two extreme F features by orientation but align the far cap to the origin, translating the correctly oriented shape left into C.',
     'In local coordinates source origin(15,19), clockwise90:(x,y)->(y,-x), y-mirror:(-y,-x), halfturn:(y,x). E with origin(18,-6) equals this map over all10 vertices. C with origin(40,9) equals the SAME swap(x,y) shape plus(-5,0), verified by cyclic point set; its red endpoint is5units left of the required fixed origin. A/B/D are distinct. Four existing open edge intervals add no cut, relation or fill, and both axes/origin crossings remain readable.',acts,roles)

for q,reason,alternatives,proof in [
 ('Plane318','No drawn input y exists. Coloring answer arms or constructing a source y would respectively be arbitrary option emphasis or introduce an unsupported glyph.',
  ['Pair answer-arm endpoints: lacks a source operand.','Draw source y: invents task information.','Color mirrored candidate edges only: answer salience.'],
  'Composition R180 Mx Rcw90 maps(x,y)->(-y,-x), selectingA for the textual y. Existing five option glyphs and choices remain unchanged.'),
 ('Plane353','The operative digits are text; wheel-box borders alone carry no distinct +4 versus+5 relation. No clean geometric correspondence survives without inventing positions or emphasizing a candidate row.',
  ['+4 off-by-one numeric mapping toA: border colors do not express the four-step mechanism.','Reverse wheel order toE: wheel order is fixed; marking boxes only would pick a row.','Add extra wheel positions or ticks: introduces unsupported count information.'],
  'Ten equally spaced wheel positions put180degrees exactly5positions away.6348+5mod10=1893, choiceB. Adjacent rows are also shifted+5.' )]:
    write(HERE/q/'refinement_assessment.json',{'stage':'material_refinement','question_id':q,'assessed_at':now(),
       'eligibility':eligibility(q),'all_old_evidence_read':OLD[q],'actual_original_PNG_natively_viewed':True,
       'old_screening_reconsidered':True,'reasonable_distinct_hypotheses_considered':alternatives,'new_calls':0,
       'status':'screened_no_clean_material_hypothesis','reason':reason,'primary_math':proof,
       'no_global_impossibility_claim':True,'no_formal_or_review_API_actions':True})
