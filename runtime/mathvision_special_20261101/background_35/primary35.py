from tools35 import *
import itertools
from fractions import Fraction
from PIL import Image
import numpy as np
proofs={}
proofs['Plane423']={'correct':'E','independent_witnesses':{
 'parallelogram':'P3=(1,3),P1=(3,5),P4=(5,3),P5=(3,1); opposite vectors(2,2) and(2,-2) match.',
 'trapezium_exclusive':'P3=(1,3),P1=(3,5),P2=(7,5),P5=(3,1) in cyclic order. P3P1 parallel P5P2, but P1P2 horizontal and P3P5 slope-1 are not parallel. Thus a proper trapezium exists under either common definition.',
 'right_triangle':'P3,P1,P4: vectors from P1 are(-2,-2),(2,-2), dot product0.',
 'obtuse_triangle':'P3,P1,P2: vectors from P1 are(-2,-2),(4,0), dot product-8.'},
 'hypotheses_considered':['Color selected existing points into convex-hull/subset groups.','Draw actual examples to bias the search to axis-aligned shapes.'],
 'screen_reason':'All four shape types have exact witnesses. A complete constructive cue supplies the correct answer; an incomplete subset can make impossibility seem plausible only by arbitrarily excluding unmarked points. No source-to-target correspondence creates a specific different answer without that arbitrary exclusion. Extra source dots or hiding a point would change the target. No new legal meaningful design retained; this is a finite assessment, not impossibility of every legal variant.'}
proofs['Plane426']={'correct':'3','lower_bound':'Let a,b be the two P angles; c=PQT,d=TQS; e=PRQ; f=RSP,g=PSQ; h=QTS,i=PTQ. We have a+e=g, b+c=h, d+g+h=180, f+g=180, h+i=180. Therefore f=d+h>h and i=d+g>g. With only two distinct positive values x<y, these inequalities force f=i=y and h=g=x. Then x+y=180 and d=y-x must equal x, so x=60,y=120,d=60. But b+c=h=60 and both b,c>=60, contradiction. One value is also impossible. Thus at least three.',
 'upper_bound':'Choose P=(0,0),Q=(1,0),R=(1,sqrt3),S=(1,1/sqrt3),T=(1/2,1/(2sqrt3)). All points lie in the required open segments. The nine marked angles are a=b=c=e=30,d=g=h=60,f=i=120. Exactly three values, so minimum3.',
 'hypotheses_considered':['Match the two pairs of supplementary angles by edge color.','Group the small triangles by colored existing angle dots.','Style selected rays to induce a two-value symmetry shortcut.'],
 'screen_reason':'The essential distinctions concern free placement, not measured frozen layout. Colored black angle dots/rays suggesting just two equal classes would function as unsupported equality information; a marked triangle identity would need unprovided symmetry. No new false angle/equality glyph or counted dot is allowed, and there is no second representation requiring a genuine feature match. Existing objection still applies; no forced call.'}
proofs['Plane447']={'correct':'A','independent_general_proof':'Let original lower-right corner be C=(6,0), crease endpoints Q=(q,0),R=(6,H), reflected corner A=(0,a), and d=6-q. Theta is the actual angle QRC. Thus d=L sin(theta),H=L cos(theta), so d/H=tan(theta). The crease preserves distances: AQ=CQ=d and AR=CR=H. AQ^2=q^2+a^2=d^2 gives a^2=12d-36. AR^2=36+(H-a)^2=H^2 gives2aH=36+a^2=12d, hence a=6d/H=6tan(theta). Therefore36tan^2(theta)=12d-36, so d=3sec^2(theta), L=3sec^2(theta)csc(theta), answer A. No measured renderer angle is used.',
 'hypotheses_considered':['Bind the actual crease to the reflected long edge.','Use the source full-width versus retained bottom subsegment as a whole/part cue.','Bind the left lower height a=6tan(theta) to L, targeting B.'],
 'screen_reason':'The last proposal is only a false length association between unrelated segments, already implicated by the earlier flap-side prescreen; it does not encode a material new fold correspondence. Exact fold partners/width bindings reinforce the true derivation. Forcing a new theta equality or crease would violate the semantic constraints. No informative simple new hypothesis retained; no calls.'}
cells=[x for x in itertools.product(range(3),repeat=3) if sum(x)<=2]
def area(cells):
    c=set(cells);return sum(tuple(x[j]+(sign if j==axis else 0) for j in range(3)) not in c for x in c for axis in range(3) for sign in (-1,1))
assert len(cells)==10 and area(cells)==36
proofs['Solid113']={'correct':'36','independent_enumeration':{'canonical_cells':cells,'interpretation':'The source triangular stair pile has bottom6,middle3,top1, equivalent up to axis/sign placement to i+j+k<=2.','contact_pairs':(6*len(cells)-area(cells))//2,'exterior_faces':area(cells)},
 'hypotheses_considered':['Match visible stair joins to the contact count along each axis.','Group six visible cap cubes as a substitute for the ten-cube pile.','Pair front/top/side face families and double the visible-face tally.'],
 'screen_reason':'The six exposed cap cubes are pairwise only edge-adjacent; treating them as isolated gives6*6=36, coincidentally the correct total. The three monotone direction face families each have6faces; doubling18also gives36. An incorrect target would require arbitrarily suppressing bottom/back contacts or adding cube boundaries; no useful new incorrect correspondence retained.'}
full=set(itertools.product(range(3),repeat=3));cut={(x,y,z) for x in [1,2] for y in [0,1] for z in [1,2]};rest=full-cut
assert len(rest)==19 and area(rest)==54 and area(full)==54
proofs['Solid186']={'correct':'A','independent_enumeration':{'original_cube_cells':27,'removed_corner_cells':sorted(cut),'remaining_cells':19,'surface_before':area(full),'surface_after':area(rest),'paint_litres':9,'reason':'Three old2x2outer face patches totaling12unit faces are replaced by three2x2cut face patches totaling12.'},
 'hypotheses_considered':['Match source missing outer patches to new recessed patches.','Use the three remaining wall slabs as a volume-for-area transfer.','Group surviving outer rims separately from cut surfaces.'],
 'screen_reason':'The useful exact patch correspondence proves unchanged surface. Volume19/27would give6+1/3litres, not any exact listed answer; choosing nearest6would add an unsupported rounding hypothesis. Omitting new cut faces gives7litres, also absent from choices. Rim painting can imply a material subset, and no clean exact alternative among listed values follows from a genuine source feature. No forced test.'}
for q,p in proofs.items():
    write(HERE/q/'material_refinement_assessment.json',{'question_id':q,'stage':'material_refinement','assessed_at':now(),'actual_source_and_formal_native_images_viewed':True,'fresh_no_op_pixel_equal':True,'prior_same_question_history_read':True,'eligibility':eligibility(q),'primary_math_and_prescreen':p,'status':'assessed_no_material_new_design','calls':0,'not_a_universal_impossibility_claim':True})
candidates=[('Solid156','r35_axis_unit_to_whole_direct_count/frozen_final'),('Solid128','r35_corner_ownership_mixed_rims'),('Solid192','r35_five_visible_faces_opposite_exhaustion')]
visual={
 'Solid156':'Final native PNG viewed after pretest duplicate-owner correction. Six distinct intended marks are now visible: local red width, local blue depth, local green height, and corresponding whole red rear width, blue right-top depth, green rear vertical height. The 3width columns, 2depth strips and6height intervals remain sharp. No extra dot/brick, new seam, text or relation glyph. All three local colored edges refer to the SAME upper-left-front brick. Full edge marks denote whole-axis correspondence, not length equality.',
 'Solid128':'Native PNG actually viewed. Exactly two original open paths are red: complete front outside upper edge and the inward-offset return upper edge. Their genuine meeting at the front subdivision is visible, as are black outer return, transverse unit edges, thickness and continuation stubs. No closed new square or counted cube boundary. The red crossing on the wall top is a preexisting projection crossing, no new spatial intersection is introduced.',
 'Solid192':'Native PNG actually viewed. All15original black pips are distinctly visible:1,2 on left;4,6,2 on right. Two red open top frames, two blue open front frames and one green open side frame follow only original edges. Shared top/seam edges remain the original geometry. Uncolored edges still separate the faces. No spot or hidden side is added, deleted, obscured or recolored.'}
for q,v in candidates:
    out=HERE/q/v;d=json.loads((out/'design.json').read_text());m=json.loads((out/'context.json').read_text())
    math={}
    if q=='Solid156':
        counts=(3,2,6);answers={'A':(4,6,12),'B':(4,6,16),'C':(4,8,12),'D':(4,8,16),'E':(4,12,16)}
        fits={k:[p for p in itertools.permutations(dims) if len({n*x for n,x in zip(counts,p)})==1] for k,dims in answers.items()}
        assert [k for k,vv in fits.items() if vv]==['C']
        math={'counts_width_depth_height':counts,'exact_all_permutation_equal_cube_edge_check':fits,'unique_choice':'C','cube_edge_cm':24,'dimensions_width_depth_height_cm':[8,12,4]}
    elif q=='Solid128':
        fits=[n for n in range(3,100) if 4*n-4==36]
        assert fits==[10];math={'outer_side_cubes':10,'inner_side_cubes':8,'border_count':36,'fill_count':64,'partial_drawing_not_measured':True}
    else:
        scene=json.loads((HERE/q/'scene_snapshot.json').read_text());pips=[o for o in scene['objects'] if o['type']=='point'];assert len(pips)==15
        im1=Image.open(HERE/q/'original.png').convert('RGBA');im2=Image.open(out/'candidate.png').convert('RGBA')
        matrix=np.array(scene['projection']['matrix']);offset=np.array(scene['projection']['offset']);origin=np.array(scene['projection']['origin']);canvas=np.array(m['canvas']['data_to_pixel'])
        crops=[]
        for o in pips:
            xy=matrix@(np.array(o['point'])-origin)+offset;px=canvas@np.r_[xy,1];x,y=map(lambda a:int(round(a)),px[:2]);box=(x-6,y-6,x+7,y+7)
            same=im1.crop(box).tobytes()==im2.crop(box).tobytes();assert same
            crops.append({'id':o['id'],'world':o['point'],'projected_xy':xy.tolist(),'native_pixel_center':px[:2].tolist(),'13_by_13_pixel_crop_unchanged':same})
        math={'total_ordinary_dice_spots':42,'visible_face_counts':[1,2,4,6,2],'visible_spots':len(pips),'unseen_spots':27,'all_original_pip_pixel_crops_unchanged':crops,'target_misconception_only_five_opposites':20,'omitted_unseen_left_side_pair_spots':7}
    write(out/'primary_review.json',{'question_id':q,'variant_id':d['variant_id'],'stage':'material_refinement','review_kind':'primary_only_NOT_independent','created_at':now(),'actual_native_candidate_png_viewed':True,'original_source_jpg_and_formal_png_viewed':True,'native_size':[768,768],'visual_findings':visual[q],'each_marker_role':d['marker_roles'],'primary_unique_answer_proof':d['primary_unique_math_proof'],'exact_math_audit':math,'expected_wrong_answer_frozen':d['expected_wrong_answer'],'human_semantics':'Original question asks a numerical size/count, not preservation of drawing ink during a picture transformation. Colored existing edges can be intrinsic paint or annotation without changing brick dimensions, wall occupancy, or pip totals. No competing mathematical answer results from retaining the ink. No new equality/angle/parallel glyph, cut, piece, region, spot or obscured diagnostic distinction is present. Color grouping is not an additional mathematical relation.','image_sha256':file_hash(out/'candidate.png'),'design_sha256':file_hash(out/'design.json'),'plugin_sha256':file_hash(out/'plugin.json'),'difference_audit_sha256':file_hash(out/'design_difference_audit.json'),'proceed_to_exactly_two_calls':True,'original_controls_reused':[],'original_controls_note':'No old original-control calls exist for these assigned designs; none added as an extra gate.','limits':['Primary visual/mathematical inspection only; no self independent review.','No human study, statistical/causal/per-marker study or incremental-effect claim.','One fixed PNG, one fixed wrong preset and exactly two calls; no retry or selected successes.'],'required_next_step_if_pair_hits':'Parent must create a NEW independent review before any eventual delivery.'})
    write(HERE/q/'material_refinement_assessment.json',{'question_id':q,'stage':'material_refinement','status':'assessed_material_new_design_ready','assessed_at':now(),'old_new_difference':d['material_difference_from_old'],'candidate':str(out),'primary_review':str(out/'primary_review.json'),'eligible':eligibility(q)})
    print(q,'primary math/marker/native/semantic review ready',flush=True)
