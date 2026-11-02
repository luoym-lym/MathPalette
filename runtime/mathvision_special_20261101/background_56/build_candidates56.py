from env56 import *
import math
from fractions import Fraction
from dataset_tools import catalog
from workbench_io import load_config, pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.mathvision_workbench import png_bytes

config=load_config()
adapter=RendererAdapter(config)
PROOFS={
'Plane320': 'Let the common apex A be the origin and a radial leg have length r. In the displayed construction the consecutive triangles are T_n=conv{0,r u(theta+100n),r u(theta+100(n+1))}; the equal shared radial leg and identical 100-degree apex give fixed r and shape, not a growing logarithmic spiral. A full coincidence must preserve the unique 100-degree apex and both radial endpoints. The unswapped case requires 100n=0 mod360, first n=18 since gcd(100,360)=20. The swapped case requires simultaneously 100n=100 and 100n=-100 mod360, impossible because200 is not0 mod360. Thus neither parallel outer bases at n=9 nor equal shapes at n=2 give full coverage. Number18 is unique; counting the initial object gives19 objects, not index19.',
'Plane332': 'Translate the unrotated middle piece by (39,0) in frozen display coordinates. Its step endpoints become (50,26),(63,26), length13. The upper-left source triangle rotates90 degrees counterclockwise about its displayed dot: its x-long vertical side becomes the entire target horizontal seam from(50,26) to(87,26). Its other side11 becomes the target vertical11 from(50,26) to(50,37). The lower source triangle rotates180 degrees about its dot and its original bottom side, length11+13=24, becomes the target right horizontal seam (63,26)..(87,26). The full seam therefore has length13+24=37. These are rigid piece correspondences, not measurements from the unequal image silhouettes. Rotation compatibility uniquely fixes x=37.',
'Plane354': 'The five identical larger acute angles exhaust the full360 degrees around O, hence each is72 degrees. Each right triangle has remaining acute angle90-72=18 degrees. Using these smaller acute angles at the new common center requires N*18=360, hence N=20 uniquely. Five copies at the small angle leave270 degrees uncovered. Original and formal images contain exactly five right triangles; no new triangle or second star is needed for this proof.',
'Plane361': 'Write initial square vertices P=(0,0),R=(s,0),S=(s,s),T=(0,s), with s=10. Successive clockwise90-degree rolls pivot about R=(s,0), then S=(2s,0), then T=(3s,0). The tracked P positions after these turns are(s,s),(3s,s),(4s,0). Its successive distances to the actual pivots are s,s*sqrt(2),s. P stays above the line between its departure and the end of the third turn, so first return occurs then. The length is(pi/2)*(s+s*sqrt(2)+s)=10pi+5pi*sqrt(2), uniquely C. The subsequent turn about P contributes zero but is outside the first-return path. The native diagram deliberately shows only45-degree portions of the first/last arcs and compresses the intervening motion by an ellipsis; these are not the entire measured path. In all three displayed square poses the same material side P-R is respectively initial bottom edge, dashed tilted P-to-pivot edge, and terminal right edge. These correspondences preserve material identity.',
'Plane380': 'Use the 6-by5 array of30 identical squares. The grey cells are the unchanged semantic_fill=true polygons. Count a unit grid edge iff it is incident to exactly one grey cell (including the frame outside); an interface shared by two grey cells is not perimeter. Exact endpoint incidence enumeration gives30 unit exterior edges. Therefore30s=240, s=8cm and area30s^2=1920cm^2, uniquely D. Colours cannot change grey membership or edge incidence. Treating one longer collinear exterior run as one edge undercounts the perimeter, whereas the old40-edge attempt incorrectly added ten interior interfaces; these are different mistakes.',
'Plane390': 'In cell units P=(1,6),Q=(2,2),R=(5,1),S=(8,5). Shoelace sum P-Q-R-S is(1*2+2*1+5*5+8*6)-(6*2+2*5+1*8+5*1)=77-35=42, so area21 cells. Each cell area is2^2=4cm^2, giving84cm^2, uniquely B. Equivalently the7-by5 bounding rectangle35 loses top triangle7/2, right triangle6, lower-left two triangles2 and3/2 plus the1-by1 corner square1:35-14=21. Omitting just that outside corner square would give22 cells/88 (D), but marking that existing corner does not by itself establish a misleading part correspondence. No new internal grid or cut is permitted.',
'Plane397': 'Let the small square side be u. The subdivided quadrant contains a3-by3 array, hence its side3u. The other three unsubdivided squares share matching full quadrant sides and each have area9u^2. The whole outer square side6u, area36u^2. Seven of the nine unit squares and exactly one of the three larger squares are grey. Grey area=(7+9)u^2=16u^2, fraction16/36=4/9, uniquely D. Equal object counting would instead give(7+1)/(9+3)=8/12=2/3 (A). This is a square-count versus area-weight error: the actual side3-to1 distinction remains visible. The question asks a grey area fraction, not how many painted outlines or marks exist.',
'Plane445': 'Set A=(0,0),C=(4,0),B=(4,3). A fold carrying A to B is reflection in their perpendicular bisector8x+6y=25. It meets AB at M=(2,3/2), AC at N=(25/8,0), and BC only at y=-7/6 outside the triangle. Thus the entire crease in the paper is MN. Its length sqrt((9/8)^2+(3/2)^2)=sqrt225/64=15/8, uniquely D. The source has no actual crease or midpoint segment. Half the base is2 but the crease is not a base half; adding a false fold would contradict the given reflection.'
}

SKIPS={
'Plane320': {'old':'congruence_coincidence_binding preset2; complete finals16 and9, both misses. Related Plane382 independently screened no design.','considered':'Off-by-one19 by pairing successive shared radial edges with initial triangle0.','reason':'Existing geometry encodes transitions and labels0..3, but there is no actual receiver representing the final object count19. Recoloring shared rays cannot make the ordinal/cardinality conversion readable independently of an unstated counting instruction. A new endpoint or triangle would alter the scene; reemphasizing0/2 would repeat the old design. No clean new information transfer found.'},
'Plane332': {'old':'Unit04 prescreen only, no saved design or API; rejected direct13-to37 association.','considered':'Pair actual upper cut/source and rigidly rotated target cut; distinguish original13 step, rotated13 vertical, and target24 remainder.','reason':'The true material correspondences yield x=13+24=37 and preserve the11 vertical after rotation. A preset24 requires discarding a real13 segment; a preset13 requires assigning a part measurement to the whole seam. I found no visible receiver/intermediate that supports this error without reverting to the explicitly rejected full-span false measurement cue. No fake cut, equal-length mark, or invented join added.'},
'Plane380': {'old':'internal_external_edge_binding presetC1080, finalsD/D (first letter/value inconsistent2204); no hits.','considered':'Map one exterior unit edge to a complete longer collinear exposed exterior run, counting the longer run as a unit.','reason':'The correct perimeter is30 units. This undercount hypothesis produces an integer unit count m<30. Among the available larger-area alternatives only E=2430 is above1920, but it implies side9 and m=240/9=80/3, not an integer. None is a consistent exact prediction of the proposed grouping. Chasing a nearest option or reinserting interior edges would not be a new clean geometric hypothesis. No clone of the old40 red edges made.'},
'Plane390': {'old':'Unit20 prescreen only. Related Plane244 local_U_global_fit preset5 missed3/1; unit30 skipped.','considered':'Map the2cm unit-edge reference to clipped grey fragments, or omit the one-unit outside corner in bounding-box subtraction to targetD88.','reason':'A linear2-as-area factor predicts42, absent from the choices. The88 hypothesis needs the unchanged outside corner square omitted, but the existing grid and grey boundary show that corner as fully outside. An open-corner mark would point out the omitted square, while a coloured closed replacement or newly drawn grid beneath grey would create the very spurious partition the brief forbids. No concrete source/receiver transfer sufficiently independent of arbitrary cell salience was found.'},
'Plane445': {'old':'Unit21 screened without design/calls because a false crease conflicts with A landing onB.','considered':'Transfer a true base half2 or hypotenuse portion to the requested crease.','reason':'There is no crease or actual receiving edge in the source. Marking the base alone is isolated length salience. Drawing an incorrect crease changes the physical fold; drawing the correct solved perpendicular bisector and pairing it with2 would manufacture a new receiver rather than transfer an existing one. With no clean existing-edge receiver I skip; no fold/text/legend/false relation added.'}
}

for q,proof in PROOFS.items():
    e=eligibility(q)
    save(f'{q}/eligibility_before_design.json',e)
    assert e['eligible'],(q,e['reasons'])
    save(f'{q}/primary_math_and_native_review.json',{'question_id':q,'at':now(),'unique_original_proof':proof,'original_JPG_and_formal_768_PNG_actually_viewed':True,'formal_noop_pixel_match':True,'original_approval_matches':e['approval_matches'],'native_notes':{'Plane320':'Labels0/1/2/3 and shaded triangle0; all radial rays visible.','Plane332':'Three pieces and rotation arrows survive; target37 is full horizontal seam, not the13 vertical.','Plane354':'Five triangles, central incident rays and pointed18-degree tips distinguishable.','Plane361':'Small native diagram centered in768 canvas; two partial arcs and dots are readable; ellipsis must not be counted as physical contact points.','Plane380':'Grey/white cell incidence clear; formal grid lacks the thicker grey perimeter of the source but exact fill is preserved.','Plane390':'Grid is intentionally occluded under the grey quadrilateral; no internal construction grid is a given.','Plane397':'Seven small grey cells and one large grey quadrant;3-to1 side scale readily visible.','Plane445':'Original JPG grey interior vs approved formal no visible fill; both show only3/4/5 triangle, no crease. No formal alteration.'}[q],'marker_roles':[] if q in SKIPS else 'See each frozen design and pretest primary review.','review_role':'PRIMARY research review only; not independent second review/user approval'})
    if q in SKIPS:
        save(f'{q}/design_difference_audit.json',{'question_id':q,'stage':'material_refinement','at':now(),**SKIPS[q],'decision':'skip_no_clean_new_hypothesis','new_designs':0,'new_API_calls':0,'not_a_claim_of_impossibility':True})

def partial(paths,target,start,end,color='#DC2626',width=2):
    p=paths[target][0]
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}

prepared=[]
for q,vid,preset in [('Plane354','r56_central_angle_to_tip_role','5'),('Plane361','r56_material_edge_visible_motion_events','A'),('Plane397','r56_square_object_unit_across_scales','A')]:
    dest=OWN/q/vid
    dest.mkdir(parents=True,exist_ok=True)
    assert not (dest/'design.json').exists(), 'Never overwrite a frozen design'
    context=adapter.inspect_question(q)
    save(dest/'fresh_context.json',context)
    scene=adapter.scene(q)
    try:
        data=png_bytes(scene)
        paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],
                        'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]}
                       for p in object_paths(scene,o['id'])]
               for o in context['objects'] if o['styleable']}
    finally:scene.close()
    (dest/'no_op.png').write_bytes(data)
    assert pixel_hash(data)==context['original_pixel_sha256']
    save(dest/'frozen_paths.json',paths)
    roles=[]
    if q=='Plane354':
        actions=[partial(paths,'triangle0',0,1/12),partial(paths,'triangle0',11/12,1),partial(paths,'triangle0',1/4,1/3),partial(paths,'triangle0',1/3,5/12)]
        roles=['Source large acute angle at O: near-O portion of original hypotenuse OT0.','Source large acute angle at O: near-O portion of original leg F0O. Together the two red rays identify the72-degree angle carrying the displayed five-copy count.','Receiver small acute angle at T0: near-tip portion of the very same hypotenuse OT0. Its middle remains black, distinguishing the two angle locations.','Receiver small acute angle at T0: near-tip portion of original leg T0F0. Together these red rays match the source angular role without adding an equality arc or triangle.']
        mechanism='Match the two real side rays at the central72-degree angle to the two real side rays at the same triangle tip18-degree angle. The proposed error transfers the existing five-copy central angle role to the tip role, answering5 for the second star instead of complementing to18 degrees and using20. The pair of open ray frames is the information transfer; no second star is drawn.'
        difference='Unit12 had only a prescreen rejecting isolated tip highlighting or false angular equality markers. This design uses four actual partial paths to make both an explicit source pair and receiver pair at two distinct angles of one triangle. It contains no new angle arc, relation symbol, full triangle outline, or geometric given.'
        semantics='Although these are rearrangeable triangles, the requested number depends only on unchanged72/18/90-degree geometry. Paint on these two angle locations can remain on their material edges under motion; no result-picture option requires that paint disappear. There is no material ink mismatch that changes the count. The two acute angle sizes remain visibly different; same colour is not an equality mark.'
    elif q=='Plane361':
        actions=[partial(paths,'o0',0,1/4),{'type':'set_object_style','target':'o3','color':'#DC2626','linewidth_pt':2},{'type':'set_object_style','target':'o18','color':'#DC2626','linewidth_pt':2},{'type':'set_object_style','target':'o7','color':'#2563EB','linewidth_pt':2},{'type':'set_object_style','target':'o21','color':'#2563EB','linewidth_pt':2}]
        roles=['Source material side P-R, original bottom edge, joining P to the first true pivot.','The same material side P-R in the displayed45-degree intermediate pose; original dashed visibility retained. Its nonpivot endpoint is the original small open P-position circle.','The same material side P-R after three rolls, now terminal right vertical edge, ending at the displayed terminal P at its bottom. This is NOT the terminal bottom side.','True initial displayed P-trajectory arc, blue source event; unchanged45-degree illustrated portion.','True terminal displayed P-trajectory arc, blue receiver event; unchanged45-degree illustrated portion. Both blue end motions have side10 radius but do not include the hidden middle motion.']
        mechanism='Track the same physical P-R side through initial,45-degree and terminal poses, while matching the two actually displayed terminal trajectory fragments as an apparent two-event path. Target omission of the unpictured middle diagonal-radius quarter-turn, counting only two side-radius quarter-turns and returning10pi (A). The design does not transfer a diagonal radius and does not pretend the drawn45-degree fragments are complete measured quarter-arcs.'
        difference='Old diagonal_to_terminal_arc_radius_binding added two dashed diagonals and matched their long radii to red end arcs, presetD; full finalsB/C were misses. New design removes all new diagonals, uses three true poses of the SAME existing material side and two blue original trajectory arcs, and predeclaresA for a missing-motion-event hypothesis. It is geometrically different from a diagonal-radius substitution or relabelling the oldB/C outputs.'
        semantics='Material identity was explicitly checked: P-R maps from initial bottom to intermediate o3 and final right o18. Initial red bottom does NOT map to the final bottom o17. No paint disappears or migrates to a different material edge. Red is a material-side correspondence; blue is the existing path, not ink on the square. Original dashed pose edges keep their dash patterns. P endpoints, open circle, all ellipsis dots and line remain unchanged.'
    else:
        targets=['cell00']+[o['id'] for o in context['objects'] if o['id']!='cell00']
        actions=[partial(paths,t,1/8,3/8) for t in targets]
        for t in targets:
            ob=next(o for o in context['objects'] if o['id']==t)
            roles.append(('Source one small square object' if t=='cell00' else 'Receiver one '+('large3-by3' if t.startswith('big') else 'small unit')+' square object')+f' ({t}, '+('grey' if ob['geometry'].get('semantic_fill') else 'white')+'): open bottom/right corner, one half of each actual adjacent edge. Matching square-corner shape transfers one-object weight; no new seam or region. Its actual scale remains visible.')
        mechanism='Use one open square-corner frame on EVERY existing square object: nine unit cells and three3-by3 squares. cell00 supplies a small square object as the reference; the three much larger squares receive the same local square-corner role. Target treating each framed square as one equal count unit: seven small grey plus one large grey among twelve squares gives8/12=2/3 (A), instead of weighting large square area9 and obtaining4/9.'
        difference='Unit20 had no candidate or calls and rejected uniform grey-border emphasis without a genuine part match. New design frames all12 real square objects, including the four white ones, rather than uniformly emphasizing only grey. Cross-scale homologous bottom/right corners make the square-object unit reference/receiver explicit. Related Plane340 r34 used equal-size containing frames to replace PARTIAL grey regions with whole unit areas, preset2 and finals0.75/1: that is a different whole-frame-versus-part mechanism. Here every square is uniformly grey/white, and the error is COUNT weighting across1-to3 side scales. No prior PNG is copied or relabelled.'
        semantics='The wording defines grey by unchanged interior fill. Open red strokes stay on existing edges only, without enclosing any new region, adding cuts, painting faces, or turning a white cell grey. Each of12 marks corresponds to exactly one actual square object. Small/large dimensions and every original seam remain visible, so humans can reject equal-area weighting and uniquely obtain4/9. This numerical area task has no physical motion/picture-choice ink preservation issue.'
    assert len(actions)==len(roles)
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':vid,'intent':'','params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{q:context})
    normalized=renderer.normalize(plugin)
    save(dest/'plugin_submitted.json',plugin)
    save(dest/'plugin.json',normalized)
    _,first,px=renderer.render(normalized,frozen=True)
    _,second,px2=renderer.render(normalized,frozen=True)
    assert first==second and px==px2
    (dest/'candidate.png').write_bytes(first)
    (dest/'repeat.png').write_bytes(second)
    markers=[{'action_index':i,'action':a,'role':r,'actual_paths':paths[a['target']]} for i,(a,r) in enumerate(zip(normalized['params']['actions'],roles))]
    diff={'question_id':q,'variant_id':vid,'stage':'material_refinement','at':now(),'old_new_substantive_difference':difference,'new_geometric_information_hypothesis':mechanism,'cosmetic_retry':False,'failed_or_aborted_PNG_reused':False,'posthoc_preset':False,'related_history_manifest':str(OWN/'old_history_manifest.json'),'semantic_objections_assessed':semantics,'decision':'primary_new_hypothesis_freeze_before_exact_two_calls'}
    save(dest/'design_difference_audit.json',diff)
    design={'question_id':q,'variant_id':vid,'stage':'material_refinement','created_at':now(),'expected_wrong_answer':preset,'correct_answer':read(OWN/q/'formal_record.json')['answer'],'mechanism':mechanism,'old_new_difference':difference,'primary_unique_math_proof':PROOFS[q],'marker_roles':markers,'human_semantics':semantics,'candidate_sha256':sha(dest/'candidate.png'),'candidate_pixel_sha256':px,'normalized_plugin_sha256':sha(dest/'plugin.json'),'frozen_paths_sha256':sha(dest/'frozen_paths.json'),'review_status':'PRIMARY ONLY; parent must create a NEW independent second review; no approval/Pass/Collect/delivery'}
    save(dest/'design.json',design)
    save(dest/'render_check.json',{'fresh_inspect_question':True,'fresh_noop_formal_pixel_equal':True,'normalized_defaults_valid':True,'twice_byte_identical':first==second,'twice_pixel_identical':px==px2,'candidate_sha256':sha(dest/'candidate.png'),'repeat_sha256':sha(dest/'repeat.png'),'design_sha256':sha(dest/'design.json'),'plugin_sha256':sha(dest/'plugin.json'),'context_sha256':sha(dest/'fresh_context.json'),'paths_sha256':sha(dest/'frozen_paths.json'),'renderer_source_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py'),'actual_PNG_view_pending':True})
    prepared.append({'question_id':q,'variant_id':vid,'path':str(dest),'expected_wrong_answer':preset,'design_sha256':sha(dest/'design.json'),'image_sha256':sha(dest/'candidate.png')})
    print(q,vid,'FROZEN',preset,len(actions),'marks',flush=True)

save('prepared_candidates.json',prepared)

# Byte-for-byte reuse of the harness logic, with only its local environment bootstrap.
source=(BASE/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')
old='PROJECT = Path(__file__).resolve().parents[3]'
replacement='sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nimport env56\nPROJECT = env56.PROJECT'
assert source.count(old)==1
dest=OWN/'harness/quicktest3_isolated.py'
dest.parent.mkdir()
dest.write_text(source.replace(old,replacement),encoding='utf-8',newline='\n')
assert dest.read_text(encoding='utf-8').replace(replacement,old)==source
save('harness_isolation_audit.json',{'source':str(BASE/'harness/quicktest3_isolated.py'),'source_sha256':sha(BASE/'harness/quicktest3_isolated.py'),'copy':str(dest),'copy_sha256':sha(dest),'only_substitution':{'old':old,'new':replacement},'all_request_profile_credential_timeout_token_error_logic_byte_identical_after_bootstrap_reversal':True,'own_strict_write_guard_installed_before_project_imports':True,'all_caches_and_TEMP_own':True,'no_API_calls_yet':True})
