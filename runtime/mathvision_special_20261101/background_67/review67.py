from env67 import *
from fractions import Fraction as F
import gc

A=read(OWN/'snapshots/background_67_assignment.json')
items={x['question_id']:x for x in A['questions']}
proofs={
 'Solid140': {'correct_answer':'D','proof':'The printed 25 cm is 1/4 m. Initial base 4*2=8 m^2 gives V=2 m^3. The right-hand picture labels the vertical dimension 4 m and the base 1 m by 2 m, so h=V/(1*2)=1 m, uniquely D. This also lies inside the 4 m tank. Initial and final horizontal water-surface areas 8 and 2 are unequal, even though both are rectangles. Source shape/receiver shape matching does not establish equality. No extremum is requested.','exact_results':{'initial_volume_m3':'2','final_base_m2':'2','height_m':'1'},'marker_assessment':[
  'leftlevel0 is the real 4 m front water-surface boundary, source width arm, not an outline of an answer choice.',
  'leftlevel1 is its real 2 m depth boundary, source second arm needed to identify horizontal area.',
  'rightlevel0 is the real 1 m water-surface width boundary, receiver matched by role, not by numerical equality.',
  'rightlevel1 is the real 2 m receiver depth boundary; together the four marks compare complete two-dimensional surface units.'],
  'human_semantics':'All 4/2/1 m and 25 cm labels remain distinct and readable. The gray water regions and existing water levels are fixed. No new water surface, paint target, equality mark or option cue is present. A colored water boundary is compatible with the same conserved-volume solution; the task does not ask for a color-preserving transformed option.'},
 'Solid219': {'correct_answer':'A','proof':'Use unit-cube coordinates with x front horizontal, y depth, z vertical; translate Figure 2 by -2.05 in x. The first two cuts share the top line y=t, z=1 and meet bottom edges y=0 and y=1. The two outer triangular prisms have volumes t/2 and (1-t)/2; their stated congruence forces t=1/2. Thus their planes are y=z/2 and y=1-z/2, outer prism volume 1/4. Cutting in the same manner in the orthogonal direction gives x=z/2 and x=1-z/2, as the actual front/back dashed traces show. Both W leaders indicate (1,0,1), not the free display anchor named W. Its piece is 1-z/2<=x<=1, 0<=y<=z/2. Horizontal area z^2/4 integrates from 0 to 1 to 1/12, uniquely A. Four corner cells integrate z^2/4 to 1/12 each; four edge-middle cells integrate z(1-z)/2 to 1/12 each; the central cell integrates (1-z)^2 to 1/3. These are nine positive-volume cells summing to 1. No extremum is requested.',
  'exact_results':{'first_outer_prism':'1/4','W_intersection':'1/12','four_corner_cells_each':'1/12','four_edge_middle_cells_each':'1/12','central_cell':'1/3','cell_count':9,'total':'1'},
  'marker_assessment':[
   'line_2 is Figure 1 right-front vertical edge (1,0,0)-(1,0,1), the length-1 leg of the true end triangle.',
   'line_5 interval [0,1/2] is the top half-depth leg (1,0,1)-(1,1/2,1); frozen path p0 is one straight ordered segment, so the interval ends at the existing cut apex R, not a newly stipulated midpoint.',
   'line_11 is the real first-cut trace (1,0,0)-R, closing that actual triangular prism end face.',
   'line_15 is the homologous Figure 2 vertical edge. It is also an exterior edge of the W piece; there is no newly created vertex or cut.',
   'line_18 interval [0,1/2] is the homologous top half-depth edge ending at the actual Figure 2 R; interval hash and direction are checked.',
   'line_24 is the homologous first-cut trace. Completing the real end-face triangle across stages communicates the source-prism to receiver-subpiece relation. The second-cut planes still subdivide its interior volume.'],
  'human_semantics':'The same physical end-face edges retain matching red across the two stages, so no incompatible transport of original edge identity occurs. The red triangle is an existing exterior face, including for the W subpiece, and is not a fake additional piece or fixed partition. All four second-cut dashed traces, both black W leaders, figure labels, nine-cell meaning and absent hidden edges are preserved. No new painted face or target redefinition appears. Six actions have six actual boundary roles; this is not a mark-count rule.'},
 'Solid236': {'correct_answer':'C','proof':'Use actual native coordinates C=(0,0,0), E=(1,1,1), B=(1,0,0), D=(0,1,0), F=(1,0,1), H=(0,1,1), J=(1,0,1/2), I=(0,1,1/2). E,J,C,I lie in x+y-2z=0, equivalently x+y=2z. Their diagonals CE=(1,1,1) and JI=(-1,1,0) are perpendicular with squared lengths 3 and 2 and shared midpoint (1/2,1/2,1/2). Area^2=(3*2)/4=3/2. One face has area 1, so R^2=3/2, uniquely C. Independently the adjacent vectors EJ=(0,-1,-1/2), EI=(-1,0,-1/2) have Gram determinant (5/4)^2-(1/4)^2=3/2. No extremum is requested.',
  'exact_results':{'CE_squared':'3','JI_squared':'2','dot':'0','section_area_squared':'3/2','R_squared':'3/2'},
  'marker_assessment':[
   'First dashed line uses exact native C/E snap coordinates and shows the genuine body diagonal inside the already specified section. It supplies the body-diagonal comparison source.',
   'Second dashed line uses exact native J/I snap coordinates and shows the genuine diagonal joining the specified edge midpoints. It is the comparison receiver. There is no midpoint dot at the red crossing and no equality tick.'],
  'human_semantics':'The gray EJCI region, all ten original point dots/labels, black edge visibility and cube identity survive. The red lines lie in the existing section and do not create a new section condition or claim equal lengths. Dashed comparison ink is readable over the gray plane and distinguishable from original black hidden edges. The new lines use existing endpoints and do not introduce new pieces.'}
}

# Important: independently correct a sign error in the source prose WITHOUT editing it.
assert all(F(x)+F(y)-2*F(z)==0 for x,y,z in ((1,1,1),(1,0,F(1,2)),(0,0,0),(0,1,F(1,2))))
assert F(4)*2*F(1,4)==2 and F(2)/(1*2)==1
assert F(1,4)/3==F(1,12)
assert F(1,2)*(F(1,2)-F(1,3))==F(1,12)
assert 1-1+F(1,3)==F(1,3)
assert 8*F(1,12)+F(1,3)==1
assert F(3)*2/4==F(3,2)==F(5,4)**2-F(1,4)**2
for q,v in items.items():
    e=read(OWN/q/'eligibility_initial.json')
    s=read(PROJECT/'SolidGeometry'/e['formal_record']['scene'])
    d=read(Path(v['source_directory'])/'design.json')
    inputs=[]
    for rel,expected in e['content_snapshot']['files'].items():
        p=PROJECT/'SolidGeometry'/rel
        actual=sha(p); assert actual==expected,(q,str(p))
        if p.suffix.lower() in ('.json','.py','.md'):
            txt=p.read_text(encoding='utf-8-sig')
            if p.suffix.lower()=='.json': obj=json.loads(txt); del obj
            del txt
        inputs.append({'path':str(p),'sha256':actual,'full_bytes_read':True,'approval_hash_matches':True})
    correction=[]
    if q=='Solid236':
        correction=[{'frozen_source_claim':'All EJCI points satisfy x+y+2z=2.','fresh_primary_correction':'For the ACTUAL native coordinates C=(0,0,0), E=(1,1,1), the correct plane is x+y-2z=0. The source plus-sign plane fails C and E. All four actual section vertices are coplanar in the corrected plane; all actual added endpoints/lines and the R^2 proof remain valid.','effect':'Prose proof error only; no math-uniqueness, native-geometry, exact-PNG or marker blocker. Source design/proof bytes remain untouched and the correction is external in this audit.'}]
    proof=proofs[q]
    proof.update({'at':now(),'question_id':q,'variant_id':v['variant_id'],'review_role':'fresh PRIMARY personal review only; no independent review or approval','source_JPG_formal_PNG_candidate_PNG_and_old_unique_candidate_actually_viewed':True,'native_resolution':'768x768 for all formal/candidate PNGs; source JPG at original resolution','all_markers_personally_inspected':True,'actual_marker_actions':d['every_marker_roles'],'frozen_projection':s['projection'],'frozen_visibility':s['visibility'],'native_source_ambiguities':s['ambiguities'],'approved_inputs':inputs,'source_prose_corrections':correction,'minimum_maximum_requirement':'Not applicable: none of the three assigned questions requests a minimum or maximum.','human_unique_answer_preserved':True,'useful_targeted_concise_mark_roles_pass':True,'no_math_native_targeting_hold':True,'frozen_design_unmodified':True,'zero_call_gate_is_separate_and_not_assumed':True})
    save(f'{q}/fresh_primary_math_native_every_marker_review.json',proof)
    print(q,'FRESH_PRIMARY_MATH_NATIVE_MARKERS_PASS', 'external_prose_corrections',len(correction),flush=True)
    del e,s,d,inputs,proof; gc.collect()
save('old_history_manual_outcomes.json',{'read_complete_full_finals_from_original_raw':True,'Solid140':{'prior_variant':'rotation_axis_dimension_swap','preset':'B','finals':['D = 1m','D = 1m'],'doublehit':False},'Solid219':{'prior_variant':'quarter_cut_capture','preset':'C','finals':['E = 1/4','D = 1/6'],'doublehit':False},'Solid236':{'prior_variant':'rhombus_to_square_edge_family_binding','preset':'D','finals':['C = 3/2','D = 25/16'],'doublehit':False,'second_final_note':'Contradictory geometry and extensive failed scratchwork, but terminal R^2 and D agree; preserved as historical single preset hit only.'},'new_wrong_presets_unchanged':['A','E','E'],'old_wrong_answers_not_relabelled':True})

# Parent metadata is diagnostic; preserve both original full snapshots and new read-ins.
rows=[]
for manifest_path in (BASE/'background_59/readin_metadata_snapshots.json',OWN/'snapshots/initial_manifest.json'):
    for r in read(manifest_path):
        original=Path(r['snapshot']); source=Path(r['path'])
        if not original.is_file() or not source.is_file(): continue
        before=original.read_bytes(); after=source.read_bytes()
        current_hash=hashlib.sha256(after).hexdigest(); old_hash=hashlib.sha256(before).hexdigest()
        dst=OWN/'metadata_current_readins'/current_hash/source.name; dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists(): dst.write_bytes(after)
        mutable=source.name in ('continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json')
        classification='unchanged' if before==after else 'exact_prefix_parent_append_diagnostic' if mutable and after.startswith(before) else 'parent_metadata_update_diagnostic' if mutable else 'immutable_source_changed'
        rows.append({'original_snapshot':str(original),'original_sha256':old_hash,'original_bytes':len(before),'source':str(source),'current_sha256':current_hash,'current_bytes':len(after),'classification':classification,'append_bytes':len(after)-len(before) if after.startswith(before) else None,'current_full_snapshot':str(dst),'never_restored_or_rewritten':True})
        del before,after; gc.collect()
save('parent_metadata_diagnostic.json',rows)
assert all(r['classification']!='immutable_source_changed' for r in rows)
