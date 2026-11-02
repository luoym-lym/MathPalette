from tools60 import *
R='#DC2626';B='#2563EB'

def interval(qid,oid,start,end,color=R,width=1.5):
    p=read(HERE/qid/'exact_paths.json')[oid][0]
    return dict(type='set_object_style',target=oid,color=color,linewidth_pt=width,interval=dict(path_id=p['id'],path_sha256=p['sha256'],start=start,end=end,wrap=False))

def edge(qid,oid,a,b,color=R,width=1.5):
    p=read(HERE/qid/'exact_paths.json')[oid][0];n=len(p['controls'])
    for i,control in enumerate(p['controls']):
        if len(control)!=2:continue
        u,v=control;dx=v[0]-u[0];dy=v[1]-u[1];norm=dx*dx+dy*dy
        def param(w):
            t=((w[0]-u[0])*dx+(w[1]-u[1])*dy)/norm
            return t if -1e-10<=t<=1+1e-10 and abs((w[0]-u[0])*dy-(w[1]-u[1])*dx)<1e-9 else None
        ta,tb=param(a),param(b)
        if ta is not None and tb is not None:
            lo,hi=sorted((ta,tb));lo=max(0,lo);hi=min(1,hi)
            return interval(qid,oid,(i+lo)/n,(i+hi)/n,color,width)
    raise ValueError((qid,oid,a,b))

def prepare(qid,variant,preset,mechanism,proof,actions,roles,difference,semantics,math_paths):
    d=HERE/qid/variant;d.mkdir(exist_ok=True)
    e=eligibility(qid);write(d/'eligibility_before_design.json',e);assert e['eligible']
    adapter,Renderer,cfg=setup();context=adapter.inspect_question(qid)
    write(d/'fresh_context.json',context)
    renderer=Renderer(cfg,adapter,{qid:context})
    submitted=dict(plugin_schema_version='1.0.0',question_id=qid,category='C',operation='C_manual',description=mechanism,intent='',params={'actions':actions})
    write(d/'plugin_submitted.json',submitted)
    plugin=renderer.normalize(submitted);write(d/'plugin.json',plugin)
    _,data,pix=renderer.render(plugin,frozen=True);(d/'candidate.png').write_bytes(data)
    _,again,pix2=renderer.render(plugin,frozen=True);(d/'repeat.png').write_bytes(again)
    assert data==again and pix==pix2
    old_hashes=read(HERE/'old_evidence_hashes_initial.json')
    old_images={p:h for p,h in old_hashes.items() if qid in p and p.endswith('.png')}
    assert sha(d/'candidate.png') not in old_images.values()
    design=dict(question_id=qid,variant_id=variant,created_at=now(),expected_wrong_answer=preset,formal_correct_answer=e['record']['answer'],mechanism=mechanism,primary_unique_math_proof=proof,marker_roles=[dict(action_indices=indices,role=role) for indices,role in roles],human_semantics=semantics,source_context=str(d/'fresh_context.json'),plugin_path=str(d/'plugin.json'),candidate_path=str(d/'candidate.png'),plugin_sha256=sha(d/'plugin.json'),candidate_sha256=sha(d/'candidate.png'),pixel_sha256=pix,mathematical_evidence=math_paths,approval_status='PRIMARY EXPLORATION ONLY; no user approval, no independent review, no delivery')
    write(d/'design.json',design)
    write(d/'design_difference_audit.json',dict(question_id=qid,variant_id=variant,frozen_before_any_API=True,old_immutable_pngs=old_images,old_history_materials=str(HERE/'old_history'/qid/'materials.json'),old_full_raw_responses=str(HERE/'old_history'/qid/'full_raw_responses.json'),substantive_difference=difference,new_wrong_hypothesis=preset,not_recolor_width_crop_rename_retest=True,candidate_sha256=sha(d/'candidate.png'),plugin_sha256=sha(d/'plugin.json'),design_sha256=sha(d/'design.json')))
    write(d/'render_check.json',dict(schema_and_defaults=plugin,normalized_frozen_roundtrip=True,no_op_formal_pixel_equal=True,repeat_bytes_equal=data==again,repeat_pixel_equal=pix==pix2,candidate_sha256=sha(d/'candidate.png'),repeat_sha256=sha(d/'repeat.png'),pixel_sha256=pix,fresh_context_sha256=sha(d/'fresh_context.json'),baseline_evidence=str(HERE/qid/'baseline_check.json')))
    import matplotlib.pyplot as plt
    plt.close('all');del adapter,renderer,context,data,again;gc.collect()
    print(qid,variant,'frozen; native visual gate still pending',flush=True)

def main(qid):
    if qid=='Plane271':
        prepare(qid,'r60_exposed_radius_to_buried_seam','D',
            'Match the small quarter-circle radius exposed on the left to the same material radius buried beside the rectangle on the right. The intended error cancels this 5 cm edge in the perimeter difference despite its change of boundary membership, producing 15 cm.',
            'The rectangle is 10 by5. Both large radii are10 and small radii5. Arc total in either arrangement is 2*(pi*10/2)+2*(pi*5/2)=15pi. The left exterior straight edges are 10+10+5+5=30; the right exterior straight edge is only the rectangle bottom10. Thus perimeters 15pi+30 and15pi+10 differ by20, uniquely E. The marked radius (-5,0)-(0,0) maps under a 90-degree rotation and translation to (30,-5)-(30,0), the same real small piece edge. The latter is an internal seam between the quarter circle and rectangle, not exterior.',
            [interval(qid,'left_small_left',.5,.75,width=2),interval(qid,'right_small_left',.5,.75,width=2)],
            [([0],'Source: actual exposed 5 cm straight radius of the small left piece.'),([1],'Receiver: the same 5 cm radius after the quarter-turn, now internal; source/receiver equal material edge but different perimeter membership.')],
            'Old v01 recolored whole rectangles and whole large sectors, preset C=10. This design uses neither old target family. It encodes exposed-versus-buried membership of a particular small-piece radius, with preset D=15 from one erroneous five-unit cancellation. This is not a line-strength variant of the old missed-factor-two hypothesis.',
            'Only two existing open straight radii are styled. All five piece contours, arcs, seams and joins stay fixed. The same physical radius can retain its ink in both arrangements, so physical-piece identity also remains consistent. No new cut, piece, dimensional equality symbol or fill is introduced.',[])
    elif qid=='Plane367':
        actions=[edge(qid,'shape0',[1,2],[2,2]),edge(qid,'shape0',[2,2],[2,1]),edge(qid,'h1',[3,1],[5,1]),edge(qid,'v4',[4,0],[4,1])]
        prepare(qid,'r60_square_unit_to_halfcell_corners','B',
            'Use an open red unit-square corner in A as source and the two existing unit-leg corners of the lower half-triangles in B as receivers. The intended error assigns each same-span receiver the full square area, overcounting B as 3 instead of2.',
            'Shoelace on the frozen original five polygons gives area2 for A,B,C,D,E. A consists of one unit square and two half-unit triangles. B consists of one unit square and two half-unit triangles. C does as well; D is half of a2by2 square; visual E is a diamond with diagonals2 and2. Therefore the choice E, all equal, is unique. The marked A corner has two unit legs bounding a full square. The B lower left and right corners each have unit horizontal and vertical legs, but each region is cut by its original diagonal, hence each area is1/2, not1.',
            actions,[([0,1],'Source open corner of the true unit square in A.'),([2],'Two horizontal unit legs of the two true lower half-triangles of B; a single interval supplies both nonduplicated receiver bases.'),([3],'Shared vertical unit leg of those two B half-triangles. It supplies both receiver heights exactly once, and combines with action2 into two open unit-leg corners.')],
            'Old solid_target/triangle_salience only favored D; zigzag_salience favored whole C vs D. New source A unit-square corner and B half-cell corners compare equal linear spans with unequal area weights. No whole wrong answer contour is emphasized. The new preset B arises from 1+1+1=3 versus the true1+1/2+1/2=2.',
            'The four operations restyle only preexisting shape/grid segments. They draw no new partition or filled cell, and close no colored region. All black diagonals, complete grid and all five silhouettes/letters stay visible. Color carries comparison grouping, with no explicit equal-area symbol or new numerical given.',[str(HERE/qid/'exact_area_audit.json')])
    elif qid=='Plane387':
        actions=[interval(qid,'edge0_5_1_0',0,1),interval(qid,'edge0_5_0_1',0,1),interval(qid,'edge3_1_1_0',0,2/3),interval(qid,'edge3_1_0_1',0,1),interval(qid,'edge3_2_1_0',0,1/3),interval(qid,'edge4_1_-1_1',.5,1)]
        prepare(qid,'r60_complementary_fragment_unit_transfer','12',
            'Match an open corner of a true unit triangle near the top to open corners of the actual 5/6 and1/6 shaded fragments along the right target boundary. The intended error counts each receiver fragment as a unit triangle, adding one to the true total and producing12.',
            'Use lattice coordinates with basis (1,0),(1/2,sqrt3/2). The shaded vertices are(0,1),(3,3),(4,0). Their determinant is abs(3*(-1)-2*4)=11 unit triangles, each1cm^2, so the unique area is11. Exact rational clipping of all36 cells independently sums to11. The up cell at(3,1) has a shaded5/6 fragment; the adjacent down cell at(3,1) has a shaded1/6 fragment. They sum to1, while the other shaded pieces sum10. Replacing both by1 gives12. The marking does not alter either fragment boundary or shade.',
            actions,[([0,1],'Source open two-edge corner of a genuine whole unit triangle P0_5,P1_5,P0_6, area1.'),([2,3],'Receiver open corner at P3_1 of the real5/6 shaded fragment, on existing lattice edges; horizontal segment ends at the exact target-boundary crossing.'),([4,5],'Receiver open corner at P3_2 of the real1/6 shaded fragment in the opposite triangle orientation; its horizontal and diagonal legs end at exact target crossings. No new crossing is drawn or snapped.')],
            'Old lattice_basis/diamond assigned the wrong global basis area5.5; old triangle_outline preset12 merely emphasized the whole target boundary. Here the full target outline stays black. A real whole unit is compared with two particular complementary5/6+1/6 fragments. Preset12 is derived before calls from a local object-count substitution1+1 for5/6+1/6, not adopted from old outputs or a cosmetic target-outline change.',
            'All six styled intervals lie exactly on existing grid edges. They form three open two-edge corners, never a new closed painted region. Target gray membership and boundary remain unchanged; all36 unit cells remain readable. The source whole triangle and two unequal fragments remain visually distinct. Colors do not label any area as1.',[str(HERE/qid/'exact_cell_clipping.json')])
    elif qid=='Plane449':
        prepare(qid,'r60_local_L_neighbor_star','D',
            'Bind the real D-bottom8 to C-top8 pair in red and D-right4 to A-left4 pair in blue. The intended error places the locally valid right-and-below star at I and stops before checking that A then needs a further right neighbor with left6.',
            'Fixed-orientation enumeration of all5!=120 permutations under all five seams yields only(I,II,III,IV,V)=(E,D,A,B,C). A right6 and C right5 cannot be followed by any left side. Hence the length-three top row is necessarily E-D-A; bottom edges0 and8 then force B,C below, with B-right3=C-left3. Unique I=E. The colored D-C vertical8 pair and D-A horizontal4 pair are both true source neighbor relationships and both appear consistently in this correct placement, centered at II. Putting this L-star at I instead would require II=A and III-left6, which is impossible. Thus local validity does not identify I.',
            [interval(qid,'D',0,.25,R,2),interval(qid,'C',.5,.75,R,2),interval(qid,'D',.25,.5,B,2),interval(qid,'A',.75,1,B,2)],
            [([0,1],'Real vertical adjacency: source D-bottom8 and receiver C-top8, with correct top/bottom side roles.'),([2,3],'Real horizontal adjacency: source D-right4 and receiver A-left4, with correct right/left side roles. Together the two pairs form a local L-neighbor star, rather than single-option salience.')],
            'Old designs color a3/5 top-row route and map a wrong top5 edge onto a right/left slot seam, preset B, with conflicting slot paint. This design removes ALL slot colors and uses only two true4/8 adjacencies that the global correct E arrangement also preserves. The new error is choosing a locally valid L-star root without enforcing the third top-row position. This explicitly resolves the prior colored-slot/number-conflict concern: even treating source edge colors as transported ink does not contradict the unique correct placement.',
            'Four existing source-card edges only; none of the slot diagram is styled. All20 integers, five source letters, Roman slots and all side orientations remain black/readable. Actual colored source sides match one another in the correct arrangement as well. No extra numerical equality, rotation or colored-slot matching requirement is introduced.',[str(HERE/qid/'exact_permutation_audit.json')])
if __name__=='__main__':
    for q in sys.argv[1:]:main(q)
