from tools33 import *
from itertools import combinations
from fractions import Fraction
R='#DC2626';B='#2563EB';G='#16A34A';O='#EA580C'
cfg,ad=adapter()
plans=[]
def ctx(q):return read(HERE/q/'context.json')
def target(q,oid):return next(t for t in ctx(q)['canvas']['targets'] if t['id']==oid)
def style(q,oid,color,start=None,end=None,width=2):
    a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width}
    if start is not None:
        p=target(q,oid)['partial_paths'][0]
        a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
    return a
def line(q,a,b,color,index):
    pts={p['id']:p['xy'] for p in ctx(q)['snap_points']}
    return {'type':'add_line','id':'r33_aux_'+str(index),'endpoints':[pts[a],pts[b]],'color':color,'linestyle':'solid'}
def add(q,vid,preset,actions,roles,hypothesis,difference,semantics,certificate=None):
    plans.append({'question_id':q,'variant_id':vid,'expected_wrong_answer':preset,'actions':actions,'per_marker_roles':roles,'hypothesis':hypothesis,'material_difference':difference,'human_semantics_precheck':semantics,'extra_certificate':certificate})

q='Plane249';intervals=[(0,1/16),(3/16,5/16),(7/16,9/16),(11/16,13/16),(15/16,1)]
actions=[style(q,'boundary',R,a,b) for a,b in intervals]
roles=['One part of four identical red exterior corner L marks: marks the actual four corner cells as a correspondence group, where the two right corner cells already form a horizontal reflected pair. This complete four-corner footprint is invariant under every possible grid reflection; no internal boundary or fill is added. Interval '+str(iv) for iv in intervals]
add(q,'r33_dihedral_corner_pair_group','3',actions,roles,
    'Four symmetry-preserving corner L marks group the two shaded right corners as an already matched horizontal pair. Predicted error commits to the horizontal completion requiring 3 additions and misses the falling-diagonal completion requiring only 2.',
    'Old prescreen rejected potentially asymmetric cell-border pairings. New marks use only original exterior boundary segments and their complete D4 orbit, whose color/width pattern preserves all four candidate axes even under literal ink-as-design reading. A geometric corner-occupancy correspondence, rather than a cosmetic retry; no old candidate or calls exist.',
    'The four red L marks are themselves invariant under all original candidate reflections. Whether treated as annotation or design content, they impose no extra reflection restriction. Black/white fills and literal grid edges are unchanged.',
    {'annotation_D4_invariance':'The footprint is all exterior boundary points within distance 1 along either side of each of the four corners; the same red and 2 pt width at every corner. Reflection permutes the four congruent Ls. Each admissible symmetry of the shaded grid therefore remains admissible with these fixed marks.'})

q='Plane325';orbit=[(3,1),(5,1),(3,7),(5,7),(1,3),(1,5),(7,3),(7,5)]
actions=[style(q,f'cell{x}_{y}',R,0,1,1.5) for x,y in orbit]
roles=[f'Original cell ({x},{y}) is one member of the full 8-cell D4 orbit of (3,1). Matching outlines group the off-axis near-arm cells, including the existing horizontal shaded pair (3,1)/(3,7) and the unmatched (1,3); all original gray/white fills remain. This member is required for reflection-invariant orbit coverage.' for x,y in orbit]
add(q,'r33_dihedral_arm_orbit_local_completion','1',actions,roles,
    'Eight symmetry-invariant off-axis arm-cell outlines bind an existing horizontal gray pair and its local missing mate. Predicted error completes only the highlighted orbit by adding cell (1,5), answering 1 while ignoring the other shaded-cell orbits.',
    'No old design/test exists. Old border-color concern is addressed by marking the complete D4 orbit rather than an asymmetric proposed pairing. The new information hypothesis is local orbit completion mistaken for global completion; the original minimum remains 3 for the rising diagonal.',
    'Every candidate original reflection permutes these eight identical outlines. Even a literal colored-picture interpretation retains the same four possible axes and the same fill-completion minimum. No gray cell is recolored and no square added.',
    {'orbit':orbit,'D4_invariance':'All eight images of the cell (3,1) under the square D4 group at center (4.5,4.5) are present with identical stroke. Local horizontal completion adds (1,5); the other original shaded cells still require 3 more additions for that axis.'})

q='Plane328';actions=[line(q,'P00','P22',R,0),line(q,'P02','P20',B,1)]
add(q,'r33_shared_center_diagonal_constraints','1',actions,
    ['The actual full P00-P11-P22 diagonal is one non-axis collinearity constraint. Its intersection with the blue line is the already marked P11, not a new point.',
     'The actual full P02-P11-P20 diagonal supplies the second constraint sharing P11. Together these support the local one-center deletion misconception while the three disjoint row constraints still force 3.'],
    'Two true diagonal 3-point constraints share the original center. Predicted error deletes just their shared center, answering 1 and overlooking the remaining full outer rows/columns.',
    'Old assessment incorrectly said 8 perimeter points and dismissed arbitrary triples. Current source/formal contain all 9 points. This design targets the structurally distinguished pair of non-axis 3-point lines and their existing shared center; no deletion marker or point recoloring, no arbitrary triple nomination.',
    'The target is removal of marked dots to avoid any three collinear points; solid auxiliary segments do not change collinearity or the nine-dot inventory. Both added lines meet only at existing P11 and do not mark any dot as removed.')

q='Plane363';pairs=[('P00','P20',R),('P20','P22',B),('P22','P02',G),('P02','P00',O)]
actions=[line(q,a,b,color,i) for i,(a,b,color) in enumerate(pairs)]
add(q,'r33_overlapping_boundary_constraint_groups','4',actions,
    [f'Boundary constraint {a}-{b} passes through its original side midpoint and has exactly three existing points. Its color identifies one of four real perimeter constraints; each corner belongs to two adjacent constraints. Predicted error adds one removal per color and ignores that overlap.' for a,b,color in pairs],
    'Four differently colored perimeter collinear triples appear as separate constraint groups. Predicted error sums one deletion per side to give 4, overlooking shared-corner coverage and the actual three-deletion main-diagonal solution.',
    'No prior saved design/calls. Replaces old proposed removed-point salience with full actual collinearity-group boundaries and their overlap. Every endpoint and intermediate point is original; all segment meetings are existing corners. Target misconception is overlap double-counting, distinct from Plane328 shared-center local-only undercount.',
    'The question counts removed points, not drawn sides or regions. The rectangle is only the existing perimeter-point constraint cycle, introduces no point, cross-out, false equality or cut condition; all 9 marked dots remain relevant.')

q='Plane368';actions=[style(q,'v0',B,5/22,9/22,1),line(q,'P2','P0',R,1),line(q,'P3','P0',G,2),line(q,'P2','P1',R,3),line(q,'P3','P1',G,4)]
roles=['The exact existing v0 interval from original marked P3=(0,1) to P2=(0,2) is the shared true unit base of two possible triangles; no extra grid edge.']
roles += ['P2-P0 is the first apex leg of the actual minimum triangle, paired red with P2-P1.','P3-P0 is its second apex leg, paired green with P3-P1.','P2-P1 is the first corresponding leg of the other same-base triangle; its apex is four grid units from the base rather than one.','P3-P1 closes the corresponding larger triangle. Same colors map leg roles; they are not equality symbols.']
add(q,'r33_common_base_apex_distance_binding','E',actions,roles,
    'A red/green same-base correspondence pairs triangles P2-P3-P0 and P2-P3-P1. Predicted error uses the conspicuous four-unit apex distance to report area 2 (E), overlooking the one-unit apex distance that gives 1/2.',
    'Old prescreen had no saved design and rejected generic rectangle/height formula emphasis. This new hypothesis binds the exact two realizable triangles sharing the only vertical unit pair, with matched side roles and an explicit one-versus-four apex distance. Both minima comparison features remain visible.',
    'The original says six marked points; all six black dots remain and no point marker is added. Thin auxiliary triangle sides do not add eligible vertices. Their one unmarked crossing is visibly not a seventh black dot. Both outlined triangles are genuine triples; original lattice, labels, and unit meaning are unchanged.')

q='Plane448';actions=[style(q,'band',R,0,.25,1),style(q,'band',B,.25,.5,1),style(q,'band',R,.5,.75,1),style(q,'band',B,.75,1,1),line(q,'p01','p41',G,4)]
roles=['Upper triangle left side p01-p13 is red, matched to lower triangle right side after exchanging common-base endpoints.','Upper triangle right side p13-p41 is blue, matched to the lower left side.','Lower triangle right side p41-p30 is red, the proposed half-turn counterpart of the upper left side.','Lower triangle left side p30-p01 is blue, counterpart of the upper right side.','The existing four peg intervals between p01 and p41 form a legitimate common diagonal base, splitting actual band area into 4+2. It passes through original p11,p21,p31 and adds no peg.']
add(q,'r33_common_diagonal_halfturn_part_binding','8',actions,roles,
    'Red/blue side-role pairing matches the two common-base triangular parts under a half-turn, encouraging a false congruence and doubling upper area 4 to answer 8; lower height is actually 1 versus upper height 2.',
    'Old prescreen saved no design and objected to arbitrary peg salience and added bounding boxes. New correspondence uses the four original rubber-band sides and one actual internal diagonal, with no outside region or box. The error is concrete mismatched triangular part correspondence, not a formula-only highlight.',
    'Original quadrilateral vertices and all 20 black pegs remain. The thin green line is an internal area-decomposition auxiliary, not a second rubber band or a cut into extra physical pieces. Color matches side roles without equality/parallel glyphs; unequal apex distances remain plainly visible.')

q='Plane486';proof=read(HERE/q/'math_proof.json');lift=proof['integer_lift'];actions=[];roles=[];selected=[]
for obj in proof['canonical_line_point_sets']:
    aa,bb,cc=obj['ABC']
    if (aa,bb) not in [(0,1),(1,1),(1,-1)]:continue
    ids=sorted(obj['point_ids'],key=lambda k:lift[k]);a,b=ids[0],ids[-1];color={(0,1):R,(1,1):B,(1,-1):G}[(aa,bb)]
    actions.append(line(q,a,b,color,len(actions)));selected.append(obj)
    roles.append(f'Maximal principal-direction line {obj["ABC"]} contains exactly original points {ids} ({len(ids)} >=3). This real excluded collinear group belongs to one of three parallel families. Together the fifteen groups account for 84 pair incidences; the other nine 3-point lines are not drawn, motivating the incomplete-subtraction error 171-84=87.')
assert len(actions)==15
add(q,'r33_principal_direction_exclusion_families','87',actions,roles,
    'Three colored principal-direction families identify all fifteen ordinary hexagonal rows. Predicted error subtracts only their 84 pair incidences from C(19,2)=171 to get 87 and misses nine further nonprincipal 3-point lines, whose 27 pairs reduce the true answer to 60.',
    'No old design/calls. Resolves the old arbitrary-segment concern by showing complete maximal >=3-point exclusion families, rather than nominating eligible two-point segments or recoloring/excluding dots. All new segment intersections within the hexagon are original dot centers. This is an explicit incomplete degeneracy classification hypothesis.',
    'Only marked-point incidence defines the requested line count. These fifteen drawn segments each contain >=3 original dots and cannot themselves become new exactly-two-point lines. No dots are added/removed/recolored; their center crossings are existing points. No equality or parallel-arrow glyph is asserted.',
    {'selected_principal_lines':selected,'principal_pair_incidences':84,'other_three_point_lines':9,'other_pair_incidences':27,'predicted_incomplete_count':87})

q='Plane487';actions=[style(q,'l1_2_0',R,width=2),style(q,'l1_4_0',R,width=2),style(q,'l0_2_0',B,width=2),style(q,'l0_4_0',B,width=2)]
add(q,'r33_intact_border_strip_union','217',actions,
    ['Existing complete y=2 row is the inner boundary of the bottom 6x2 intact strip. Paired red with y=4; retains exact grid-edge set.','Existing complete y=4 row is the inner boundary of the top 6x2 strip, red pair groups the two equal intact horizontal subgrids.','Existing complete x=2 column bounds the left 2x6 strip. Paired blue with x=4 and meets red only at original grid intersections.','Existing complete x=4 column bounds the right 2x6 strip. All four styles frame the actual central unsplit 2x2 cell; the x=3 and y=3 missing segments remain absent.'],
    'Red horizontal and blue vertical inner boundaries group four complete 6x2 border strips and the central large cell. Predicted error counts their union 4*63-4*9+1=217 and misses 80 valid rectangles spanning those local subgrids.',
    'Old prescreen rejected added completion edges and arbitrary rectangle salience. New styles change exactly four existing complete grid lines that delimit the maximal intact border subgrids; not a single new grid segment is introduced. This targets locally exhaustive strip enumeration mistaken for global enumeration.',
    'The target depends solely on which grid edges exist; all existing edges remain continuous and exactly the same, with original central omissions preserved. Colors identify real subgrid boundaries and do not forbid spanning rectangles or imply physical cuts.')

write(HERE/'design_difference_audit.json',{'unit':'background_33','stage':'material_refinement','created_at':now(),'old_history_audit_sha256':file_hash(HERE/'previous_history_audit.json'),'pre_call':True,'designs':plans,'old_variants_retested':False,'posthoc_presets':False,'semantic_lesson':'Explicitly read actual Plane295/Plane342 reject reports. None of these tasks transform colored printed content; the two symmetry cases additionally require complete D4-invariant annotation footprints even under literal ink-as-design reading.'})
for plan in plans:
    q=plan['question_id'];out=HERE/q/plan['variant_id'];assert eligibility(q)['eligible']
    fresh=ad.inspect_question(q);write(out/'fresh_context.json',fresh)
    assert fresh==ctx(q)
    write(out/'eligibility_design.json',eligibility(q))
    write(out/'design_difference_audit.json',{'created_at':now(),'stage':'material_refinement','pre_call':True,**plan})
    scene=ad.scene(q)
    try:
        from dataset_tools.mathvision_workbench import png_bytes
        baseline=png_bytes(scene)
    finally:scene.close()
    assert pixel_hash(baseline)==pixel_hash(ad.original_paths[q]);(out/'no_op.png').write_bytes(baseline)
    pr=PluginRenderer(cfg,ad,{q:fresh})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':plan['hypothesis'],'intent':plan['hypothesis'],'params':{'actions':plan['actions']}}
    write(out/'plugin_submitted.json',plugin)
    normalized,png,digest=pr.render(plugin);again,png2,digest2=pr.render(normalized,frozen=True)
    assert normalized==again==pr.normalize(normalized) and png==png2 and digest==digest2
    write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png);(out/'repeat.png').write_bytes(png2)
    targets={t['id']:t for t in fresh['canvas']['targets']};snaps={p['id']:p['xy'] for p in fresh['snap_points']}
    bindings=[]
    for i,a in enumerate(normalized['params']['actions']):
        binds={'action_index':i,'action':a,'useful_role':plan['per_marker_roles'][i]}
        if a['type']=='set_object_style':binds['actual_original_target']=targets[a['target']]
        else:
            binds['endpoint_exact_snap_ids']=[[k for k,v in snaps.items() if v==p] for p in a['endpoints']]
            assert all(binds['endpoint_exact_snap_ids'])
        bindings.append(binds)
    write(out/'marker_bindings.json',bindings)
    design={'question_id':q,'variant_id':plan['variant_id'],'stage':'material_refinement','created_at':now(),'expected_wrong_answer':plan['expected_wrong_answer'],'correct_answer':ad.records[q]['answer'],'hypothesis':plan['hypothesis'],'material_difference':plan['material_difference'],'primary_math_proof_path':str(HERE/q/'math_proof.json'),'primary_math_proof_sha256':file_hash(HERE/q/'math_proof.json'),'per_marker_roles':plan['per_marker_roles'],'human_semantics_precheck':plan['human_semantics_precheck'],'extra_certificate':plan['extra_certificate'],'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':digest,'plugin_sha256':file_hash(out/'plugin.json'),'design_difference_audit_sha256':file_hash(out/'design_difference_audit.json'),'source_inputs_sha256':file_hash(HERE/q/'input_fingerprints.json'),'baseline_pixel_equal_formal':True,'two_draws_byte_identical':True,'new_parent_independent_review_required':True,'approval_status':'PRIMARY_ONLY; no Pass/Collect/publication'}
    write(out/'design.json',design)
    write(out/'render_check.json',{'schema_and_actual_default_normalization_passed':True,'normalization_idempotent':True,'frozen_draw_passed':True,'no_op_pixel_equal_formal':True,'twice_byte_identical':True,'fresh_context_identical':True,'native_image_view_pending':True,'candidate_sha256':design['image_sha256'],'pixel_sha256':digest,'plugin_sha256':design['plugin_sha256'],'schema_sha256':file_hash(ROOT/'PlaneGeometry/workbench/plugin.schema.json'),'source_scene_unchanged':file_hash(ROOT/'PlaneGeometry'/ad.records[q]['scene'])==file_hash(HERE/q/'source_scene_snapshot.json')})
    print(q,plan['variant_id'],'preset',plan['expected_wrong_answer'],'actions',len(normalized['params']['actions']),flush=True)
