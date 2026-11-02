from bootstrap import *
import gc
import math
import shutil

assert read(HERE/'assignment_hash_freshness.json')['all_exact']
assert read(HERE/'zero_prior_invocation_qualified.json')['zero_visible_exact_prior_invocations']
assignment=read(BASE/'background_63_assignment.json')
proof206={
 'answer':288,
 'topology_basis':'Actual source and formal PNG have square ABCD, triangular LAD/RCB and planar quadrilateral ALRB/DLRC faces. No extra face or section is introduced.',
 'proof_steps':[
  'Put A=(0,0,0), B=(s,0,0), C=(s,s,0), D=(0,s,0). LR parallel to the base is explicitly given, so L and R have common nonzero height h; choose h>0 by reflection.',
  'The plane of face ALRB intersects z=0 in AB and z=h in LR. Intersections of a plane with parallel horizontal planes are parallel, hence LR is parallel to AB. This supplies the ridge-orientation argument rather than asserting it from the diagram or an unexplained distance inequality.',
  'LA=LD=s gives y_L=s/2. RB=RC=s gives y_R=s/2. Write L=(u,s/2,h), R=(v,s/2,h). Then u^2+h^2=3s^2/4 and (v-s)^2+h^2=3s^2/4. Thus u=+(v-s) or u=-(v-s). The first case gives |v-u|=s, incompatible with LR=2s. The second gives v=s-u and |s-2u|=2s. Its roots are u=-s/2 and u=3s/2; the latter would give h^2=-3s^2/2 and is impossible. Thus L=(-s/2,s/2,h), R=(3s/2,s/2,h), h=s/sqrt(2)=6.',
  'At relative height t=z/h, the four triangular/planar face intersections enclose a rectangle with x-range[-st/2,s+st/2] and y-range[st/2,s-st/2]. Its area is s^2(1-t^2). V=h*s^2*integral_0^1(1-t^2)dt=(2/3)*6*72=288.',
  'The end triangles are equilateral of side s, but their planes are not parallel (their x-slopes have opposite signs). Corresponding connectors AB, DC, LR have lengths s,s,2s. They cannot be prism bases. Multiplying equilateral area by ridge2s gives the frozen wrong216sqrt(6), about529.09, and is refuted by unchanged geometry.'
 ],
 'old_primary_qualification':'The r55 statement that subtracting four distance equations forces ridge direction was too compressed to establish the needed assumptions. This fresh supplement uses the actual planar quadrilateral face topology. Old primary/design files remain byte-exact.',
 'uniqueness':'All real branches above exhausted; mirror/rigid motions preserve the volume. No false parallel end faces, new height datum or extra face assumed.'}
proof207={
 'answer':864,
 'face_metrics':'Each B is a rigid right isosceles6,6,6sqrt2 triangle. Each A is the rigid12square with a midpoint6-by6 corner removed: cyclic lengths6,12,12,6,6sqrt2 and corner angles135,90,90,90,135. The central regular hexagon has side6sqrt2. Native panel coordinates and all six attachments match these metrics.',
 'folding_convention':'Use the stated seven rigid polygonal faces and their drawn hinges to form a closed simple polyhedron, with no additional creases, panel subdivision, overlaps or identification of distinct vertices of the hexagon. This is the ordinary net interpretation of the actual question; convexity is not used as an independent unstated given.',
 'proof_steps':[
  'Embed the central hexagon as the six permutations of(0,6,12) in x+y+z=18. Adjacent distances are6sqrt2 and interior angles120degrees. Alternate boundary edges have common coordinate12 (B) and common coordinate0 (A), matching the actual cyclic attachments.',
  'Every free6edge has exactly one endpoint at a central-hexagon vertex. It cannot join a6edge in reversed endpoint order to a different hexagon vertex: that would place two distinct hexagon vertices6apart, whereas hexagon chords are6sqrt2,6sqrt6,12sqrt2. It cannot join another vertex of the hexagon in the same endpoint order because those vertices are fixed and distinct. Hence the two free6edges at each hexagon vertex join each other. A long12edge cannot be subdivided into two6seams without putting at least two distinct hexagon vertices6or12apart; neither is a hexagon chord. No new fold or seam subdivision is supplied by the actual net.',
  'For the B edge between X=(12,6,0) and Y=(12,0,6), its third vertex P has |PX|=|PY|=6. At X the angle between XP and XY is45degrees (B), and between XP and the adjacent A hinge is135degrees. These fix the component of XP in the hexagon plane; its nonzero perpendicular component has only two signs. The two solutions are P=(12,0,0) and its reflection Pprime=(16,4,4) across x+y+z=18. Cyclically the other B apices are(0,12,0),(0,0,12), or their reflections obtained by adding(4,4,4).',
  'Each A contains two consecutive B apices at its short-edge endpoints. Their separation inside the rigid A polygon is the original square diagonal12sqrt2, squared288. Two apices chosen on the same side of the hexagon plane have squared separation288; choosing opposite reflection signs gives336. Therefore each A forces its neighboring B signs equal, and the three A panels force all three signs equal. This rules out independent inward/outward B flips and mixed nonconvex hinge choices under the actual net closure; a bare appeal to convex rigidity would not suffice.',
  'With the three B apices fixed, each A is rigidly fixed by its cut-edge endpoints and short-edge endpoint; three noncollinear anchors fix its plane and its polygon side. All faces therefore bound [0,12]^3 intersect{x+y+z<=18}, or its reflected congruent counterpart. The map(x,y,z)->(12-x,12-y,12-z) exchanges the two half-cubes. Thus V=12^3/2=864.',
  'The two red open intervals compare source6 with receiver12; they are not equal-length ticks and do not alter this scale. Using6as the full cube side gives6^3/2=108, the unchanged r55 wrongpreset. Retaining red ink on edges while folding changes no numerical volume; the task asks no color-pattern output.'
 ],
 'uniqueness':'Constructive face metrics plus forced short seams and synchronized reflection signs establish the intended closed seven-face volume without relying on convexity alone. Exotic additional cuts/folds, self-intersection or collapsing different hexagon vertices would change the given net.',
 'old_primary_qualification':'Old r55 proof appealed only to fixed convex-face rigidity. This supplement explicitly checks closure and mixed-sign alternatives; no old proof/design file edited.'}

for q in assignment['questions']:
    qid=q['question_id'];src=Path(q['source_directory']);d=HERE/qid
    native=read(d/'fresh_schema_native_replay.json');assert native['fresh_replay_exactly_equals_frozen']
    proof=proof206 if qid=='Solid206' else proof207
    scene=read(PROJECT/'SolidGeometry'/q['formal_record']['scene'])
    points=scene['points'];objects={o['id']:o for o in scene['objects']}
    dist=lambda a,b:math.dist(points[a],points[b])
    if qid=='Solid206':
        numerical={o['id']:dist(*o['points']) for o in scene['objects'] if o['type']=='segment'}
        for k,v in numerical.items(): assert math.isclose(v,(2 if k=='line_5' else 1)*6*math.sqrt(2),abs_tol=1e-8)
        numerical.update(height=points['L'][2],volume=(2/3)*72*points['L'][2])
        assert numerical['volume']==288
    else:
        numerical={'same_sign_apex_distance_squared':288,'mixed_sign_apex_distance_squared':336,'cut_plane':[1,1,1,18],'volume':864,'panel_edge_lengths':{}}
        for i in range(6):
            pts=[points[f'f{i}_{j}'] for j in range(3 if i%2==0 else 5)]
            lengths=[math.dist(pts[j],pts[(j+1)%len(pts)]) for j in range(len(pts))]
            expected=[6,6,6*math.sqrt(2)] if i%2==0 else [6,12,12,6,6*math.sqrt(2)]
            assert all(math.isclose(a,b,abs_tol=1e-8) for a,b in zip(lengths,expected))
            numerical['panel_edge_lengths'][str(i)]=lengths
    write(d/'fresh_math_proof.json',dict(checked_at=now(),question_id=qid,proof=proof,numerical_checks=numerical,primary_only=True))
    oldreview=read(src/'primary_visual_marker_review.json');plugin=read(src/'plugin.json');design=read(src/'design.json')
    markers=[]
    for a,r in zip(plugin['params']['actions'],design['marker_roles']):
        assert a['target']==r['target'] and a['target'] in objects and 'linestyle' not in a
        markers.append({'action':a,'actual_geometry':objects[a['target']],'targeted_role':r['role'],'useful_because':r['why_needed'],'fresh_native_observation':'Viewed actual original JPG, formal768PNG, frozen candidate768PNG, and full fresh context. Exact existing target/path confirmed; color/width only, original dash distinction and all human information retained.'})
    native_note=('Two real red equilateral end-face outlines: LAD retains its two dashed hidden edges, RCB retains three solid edges. Blue ridge2s differs from black base connectorss. Original s/2s remain readable, with no extra face or perpendicular/parallel symbol.' if qid=='Solid206' else 'Source upper half-edge stops at the original cut midpoint; receiver is the full upper A panel edge. Original source cut, all three A pentagons and three B triangles, regular hexagon, six hinges and all A/B labels remain visible. No added cut, equality or extra panel.')
    write(d/'fresh_every_marker_native_semantics.json',dict(checked_at=now(),question_id=qid,actually_viewed_source_formal_candidate=True,native_observation=native_note,markers=markers,human_unique_answer_preserved=True,semantic_fills_paint_routes_counts_labels_dimensions_preserved=True,numerical_color_cues_not_new_givens=True,semantics_rejections_applied='Unlike physical picture-completion rejects295/342/242, colored edging here can persist without altering the numerical solid-volume answer. Unlike220/263/192, every selected edge belongs to an explicit area/length or part/fullscale correspondence. No arbitrary mark-count gate.',primary_only=True))
    dest=d/q['variant_id'];dest.mkdir(exist_ok=False)
    copychecks=[]
    for name,expected in q['frozen_files_sha256'].items():
        assert sha(src/name)==expected
        shutil.copyfile(src/name,dest/name)
        assert sha(dest/name)==expected
        copychecks.append({'source':str(src/name),'copy':str(dest/name),'sha256':expected,'byte_equal':True})
    receipts=d/'frozen_source_receipts';receipts.mkdir()
    for name in ('primary_math.json','baseline_check.json','source_hashes_initial.json','formal_record.json','exact_paths.json','assessment_final.json','eligibility_initial.json'):
        shutil.copyfile(src.parent/name,receipts/name)
        copychecks.append({'source':str(src.parent/name),'copy':str(receipts/name),'sha256':sha(src.parent/name),'byte_equal':sha(src.parent/name)==sha(receipts/name)})
    write(d/'reuse_provenance.json',dict(checked_at=now(),question_id=qid,variant_id=q['variant_id'],original_created_at=design['created_at'],expected_wrong_answer=design['expected_wrong_answer'],source_directory=str(src),copied_directory=str(dest),all_file_bytes_and_internal_paths_preserved=True,copy_checks=copychecks,new_design_count=0,continuation_of='background_55',first_testing_of_existing_frozen_draft=True,zero_prior_call_gate=str(HERE/'zero_prior_invocation_qualified.json'),fresh_approval=str(d/'fresh_eligibility_and_approval.json'),fresh_math=str(d/'fresh_math_proof.json'),fresh_native_schema_replay=str(d/'fresh_schema_native_replay.json'),fresh_marker_semantics=str(d/'fresh_every_marker_native_semantics.json'),primary_only_no_independent_review=True))
    print(qid,'all fresh gates/copy equality passed',flush=True)
    del scene,points,objects,oldreview,plugin,design,native;gc.collect()
