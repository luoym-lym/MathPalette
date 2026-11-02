from env70 import *
from design70 import NAMES,directory

MATH={
'Plane186':[
 'Use original rectangle A=(0,5),B=(50,5),C=(50,0),D=(0,0); M=(25,0),N=(25,5). The folds are reflections, so the B-to-M crease is the perpendicular bisector5x+y=190 and the D-to-N crease is5x+y=65.',
 'The first crease meets the bottom/top at(38,0),(37,5); the second meets them at(13,0),(12,5). The shown final exposed white region is the parallelogram(13,0),(25,0),(37,5),(25,5). The two flipped end panels are grey and cover the adjacent triangles.',
 'Its horizontal base is25-13=12cm, height5cm, hence60cm2 uniquelyB. Half of a half of250 would be62.5, but omits the oblique-crease offset. This derivation uses the given fold coincidences and panel layering, not a measured screenshot.'],
'Plane269':[
 'At each external mesh the number of teeth passing the contact is equal:30*t1=15*t2,15*t2=60*t3,60*t3=10*t4. Therefore t4/t1=30/10=3 uniquely. The signed ratio is-3 because three meshes reverse direction; the question asks the count of turns, not signed orientation.',
 'All four original tooth counts30,15,60,10 and three contacts are preserved. Middle tooth counts telescope; hubs and decorative reference circles encode no additional transmission stage.'],
'Plane273':[
 'Actual source/native clock shafts show departure minute hand down at6 and short hand at1.5:1:30pm. Arrival minute hand is down at6 and hour hand at3.5:3:30pm. Native departure shaft angle45deg from+x, arrival-15deg, minute shafts-90deg confirm their ownership.',
 'The constant-speed journey takes120min. One third takes40min, giving2:10pm; its minute hand points to2. The five original options show40,50,0,10,20 minutes respectively. ThusD is unique.'],
'Plane275':[
 'Exact exhaustive cyclotomic position-and-tangent exclusion forN=2..11; twoN12 closed words. See exact_track_proof.json.',
 'A12-piece construction at the original inner/outer radii2/3 is closed, and every nonadjacent material pair is disjoint by the saved centerline-distance lower bound>1. Adjacent sectors meet only at their common seam. See track_construction_clearance.json and actual viewed track_construction.png. Thus12 is both possible and minimal.'],
'Plane314':[
 'Smallest square perimeter80cm implies side20cm. Shared boundaries force the shown small/medium/large side lengths1,2,3 in that unit; the layout is7units wide and5units high.',
 'The original open black route from the snake head through successive turns has lengths[1,1,2,2,2,2,2,3,4,1,1], total21. Therefore length420cm uniquelyC. These are actual route strokes, not all grey tile perimeters.',
 'It has12 maximal-run endpoints/corners but21 unit edges. A22-node unit subdivision would require adding interior-of-straight-edge points and a point on the existing head/eye region; original grid corners are not a ready22-node chain.'],
'Plane326':[
 'The independent port-graph upper bound gives at most22 connected quarter arcs; a specific4x4 orientation construction achieves22. Every arc is5dm, so maximum110dm uniquelyD. See exact_tile_proof.json.',
 'The actual source/native picture contains just one tile with two disjoint arcs, no sixteen-tile receiver arrangement. The proof construction is an audit object only and is not drawn into a candidate.'],
'Plane378':[
 'Let small rectangles have long side a and short b. Below the top band, two vertical long sides occupy the same height as three horizontal-tile short sides:2a=3b. Full AD=b+2a=4b, DC=3a=9b/2, soAD/DC=8/9 uniquelyA.',
 'Actual12-tile incidence and A/B/C/D ownership agree in source and formal image. The marked full height includes the upper b strip. The central source tile has ratio b/a=2/3, but component congruence supplies no similarity to the outer frame.'],
'Plane394':[
 'Normalize strip width to3cm. The actual four congruent grey trapeziums have parallel bases9 and3 and altitude3; their45-degree shoulders are the two original corner folds of a U-turn. Opening those two folds restores a3-by9 rectangular material module (visible area18 plus two overlapped right triangles of area4.5 each, material area27). Each module therefore uses9cm of strip.',
 'The five exposed straight white runs between modules have lengths6,3,3,3,6, sum21. Four unfolded modules contribute36. Total strip length21+36=57cm uniquelyD. Equivalently total material area63+4*27=171cm2 divided by width3 gives57cm.',
 'The labelled6cm is the end white run, not the strip width;27cm is the full enclosing horizontal span. Dashed enclosing guides are not material edges. No original dimension, grey/white face or fold changes.']}

SKIPS={
'Plane186':('screened_no_clean_materially_new_hypothesis',
 'I examined width-to-final-edge and midpoint-to-exposed-area correspondences. The final slanted side is13, not the5cm width; making them explicit equal-length symbols is false. A62.5 target would need a half-of-half partition cue absent from the original, while added filled/closed region styling could change the visible-white target or imply a crease. I found no concise true source/receiver presentation that avoids those problems. No new design or call, not a global-impossibility claim.'),
'Plane269':('screened_no_clean_information_transfer',
 'A contact tooth-to-tooth correspondence is true but supports the telescoping answer3. The prospective15/60 cumulative-ratio error has no printed whole-turn receiver. Pairing intermediate full rims or selecting a small hub only makes one cog salient; styling one tooth against a complete rim would introduce a misleading unit boundary without a useful true receiver. No tooth, axle, arrow or relation is added, and no candidate is forced.'),
'Plane273':('screened_no_clean_distinct_time_interval_receiver',
 'The old hour/minute identity error is excluded. Both actual minute hands occupy the same30-minute phase, so rim/end-hand matching cannot show the120-minute winding interval. A true40-minute elapsed arc against an absolute40-minute option would require choosing a new zero reference or marking a derived arc not delimited by the given hands; just coloring optionA would be isolated answer salience. No clear new input/receiver pairing retained.'),
'Plane314':('screened_node_edge_hypothesis_not_retained',
 'The old80-perimeter-to-one-side design and related unit-to-long-run endpoint designs were fully read and viewed. The new endpoint-count proposal needs22 unit nodes, whereas the original has12 run endpoints and several long edges without unit vertices. Filling in a new unit-node chain is not an original endpoint correspondence; the head endpoint also overlaps the original black head/white eye footprint. Omitting that endpoint would merely build a chosen20-edge marked subpath while the requested route still starts at the head. No clean concise original-feature count transfer retained; original route stays untouched.'),
'Plane326':('screened_no_printed_composite_receiver',
 'The missing maximum proof has now been resolved independently. However the supplied image has only one tile; no receiver component from the16-tile assembly is printed. Styling the two disjoint arcs as one connected curve or adding a connecting path would be false; drawing a16-tile arrangement would add actual puzzle pieces. A whole-tile/arc color cue alone does not exhibit the proposed counting transfer. No candidate/API.'),
'Plane394':('screened_material_vs_enclosing_span_ambiguity',
 'Width/shoulder and overlap-owner alternatives were inspected against the real folds.27cm is a bounding-box span, not a continuous material edge; pairing dashed guides to material would reproduce the previous rejected54 direction. Marking grey panels as one selected total either changes the face/target emphasis without a true receiver or suppresses one of four identical modules to manufacture a chosen count. No new crease, paint, paper target or false route is introduced. No clean distinct candidate retained.')}

assignment=read(OWN/'read_snapshots/background_70_assignment.json')
checks=[]
for q in assignment['questions']:
    qid=q['question_id']; old=q['source_assignment_question']['source_inputs']; files={}
    for stem in ('formal_png','original','scene','script'):
        p=Path(old[stem+'_path']);digest=sha(p)
        files[stem]={'path':str(p),'sha256':digest,'matches_source_assignment':digest==old[stem+'_sha256']}
        assert files[stem]['matches_source_assignment']
    e=eligibility(qid);assert e['eligible']
    native=read(OWN/qid/'native_source_state.json')
    record={'question_id':qid,'assessed_at':now(),'source_files':files,
       'current_eligibility':e,'full_source_JPG_and_formal_PNG_actually_viewed':True,
       'native_context':str(OWN/qid/'context.json'),'native_scene_object_count':len(native['objects']),
       'native_noop_formal_pixel_equality':True,'unique_math_independently_checked':MATH[qid],
       'frozen_3D_projection_visibility':'No3D input exists for these native planar scenes; frozen2D geometry, view, layering, labels, original arrows/dashes/fills retained.',
       'old_full_history':str(OWN/'history_reads'/f'{qid}.json'),
       'formal_edits_approvals_Pass_Collect':False,'no_arbitrary_design_or_mark_quota':True}
    if qid in SKIPS:
        record.update(status=SKIPS[qid][0],reason=SKIPS[qid][1],new_designs=0,API_calls=0)
    else:
        record.update(status='new_candidate_primary_ready_for_first_pair',variant_id=NAMES[qid],
                      candidate_directory=str(directory(qid)),new_designs=1,API_calls=0)
    save(f'{qid}/assessment.json',record)
    checks.append({'question_id':qid,'eligibility':True,'source_hashes':True,'status':record['status']})

for qid in NAMES:
    d=directory(qid);design=read(d/'design.json');plugin=read(d/'plugin.json')
    if qid=='Plane275':
        visual='Actual native768 candidate opened. Two adjacent reference outer45-degree arcs are red then blue; two true S outer arcs are red and blue on opposite curvature sides. All8 reference seams, both given S pieces, sleepers, rails, join, names and black unstyled edges are visible. No route, segment, filled face or piece was added. Actual12-piece proof construction also opened and shows a simple closed non-overlapping track.'
        semantics='This is a numerical minimum-closure question, not a colored result-matching task. Even if the rail-edge colors were physical paint, no color-matching joint rule is given: pieces retain their shapes/connectors and the same minimum12. The marked curves are already-existing boundaries; no equality, angle or directional arrow is asserted. Both signs remain visible, and position closure remains a human requirement.'
    else:
        visual='Actual native768 candidate opened. Complete AD is red, INCLUDING its top short-width strip to D. Complete DC is blue. One actual middle tile has its horizontal long bottom edge blue and vertical short right edge red. All12 cells and A/B/C/D remain clear. No interior region is closed with new edges; all selected intervals lie on original boundaries.'
        semantics='Numerical geometric ratio with original congruence statement unchanged. Red/blue identify numerator/denominator comparison roles, not numerical equality. Actual lengths remain visibly unequal and the original tiling equation2a=3b is fully available. There is no physical transformed-answer picture or fixed partition condition. Original small rectangles remain12 congruent objects; their composite frame remains distinct.'
    per=[]
    for i,(action,role) in enumerate(zip(plugin['params']['actions'],design['marker_roles'])):
        per.append({'action_index':i,'action':action,'role':role,
           'usefulness':'Necessary member of the declared source/receiver pair or contiguous constituent of a full receiving side; no unrelated option is marked.',
           'legality':'Fresh normalized schema; actual native target/pathsha; original coordinates/fills/text remain.',
           'concision_readability':'Visible at actual768; no redundant free contour. Action count follows original object segmentation.',
           'human_unambiguity':'Comparison styling supplies no new numeric equality, cut, connector, target or dimension.'})
    save(d/'primary_review.json',{'question_id':qid,'variant_id':NAMES[qid],'reviewed_at':now(),
         'role':'Primary designer review only; NOT an independent second review',
         'candidate_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),
         'actual_source_formal_native_candidate_images_viewed':True,'native_visual_findings':visual,
         'human_semantics':semantics,'primary_math_proof':design['primary_math_proof'],
         'per_marker':per,'fresh_schema_noop_repeat_offline_replay_pass':True,'proceed_to_API':True,
         'limits':['Prospective mechanism only; model narratives cannot establish causal gain.',
                   'No new original-control correctness hard gate, human study or per-marker ablation imposed.',
                   'Any double preset hit remains PRIMARY and needs a NEW parent-launched independent review before delivery.'],
         'approval_Pass_Collect_delivery':False})

manual={'Plane273':{'preset':'C','finals':['D','D'],'hits':[False,False],
       'note':'Full raw finals read. Both clock narratives misread actual hands; literal D finals nevertheless miss C.'},
 'Plane378':{'preset':'D','finals':['E (9/8)','5/6 (B)'],'hits':[False,False],
       'note':'Run1 ends E despite earlier4/3. Run2 ends5/6 after a long sequence of incompatible layouts; incidental2/3 and E mentions do not count.'},
 'Plane258':{'preset':'B','finals':['E (1680)','C (420)'],'hits':[False,False]},
 'Plane412':{'preset':'A','finals':['180cm (no option)','180cm (no option)'],'hits':[False,False],
       'note':'Incidental400 in run1 is not terminal selection; both explicitly conclude180.'},
 'Plane436':{'preset':'B','finals':['B (3:4)','1:2 (no option)'],'hits':[True,False],
       'note':'Full35036-character first final read in contiguous chunks; second gives1:2 and no option.'}}
save('old_full_manual_final_review.json',{'reviewed_at':now(),'complete_unique_raw_responses_read':10,
     'manual':manual,'source58_no_new_frozen_candidate_for_exact_scope':True,
     'old_Plane275_and_Plane314_no_actual_API_artifacts_found_in_full_task_binding_scan':True,
     'absence_limit':'No claim about unrecorded external calls; immutable saved artifacts and old pending metadata retained.',
     'cited_independent_objections_read':['Plane295','Plane342','Plane242/r24','Plane233/two_U'],
     'no_old_miss_relabelled_or_failed_image_retested':True})
save('scope_assessment_before_calls.json',checks)
print(json.dumps(checks))
