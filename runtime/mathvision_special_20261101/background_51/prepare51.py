from tools51 import *
from fractions import Fraction
from collections import Counter
import math
import numpy as np

def partial(qid,target,start,end,color):
    path=read(HERE/qid/'exact_paths.json')[target][0]
    return dict(type='set_object_style',target=target,color=color,linewidth_pt=2,
        interval=dict(path_id=path['id'],path_sha256=path['sha256'],start=start,end=end,wrap=False))
def base(qid,name,description,mechanism,wrong,proof,diff):
    return dict(question_id=qid,name=name,branch=BRANCH,description=description,mechanism=mechanism,
        expected_wrong_answer=wrong,correct_answer=eligibility(qid)['record']['answer'],
        primary_math_proof=proof,difference_audit=diff,marker_roles=[],actions=[],
        limits=['Primary designer review only; parent must commission NEW independent review for any two-hit possibility.',
                'Two model calls do not establish causal gain, population reliability or mechanism confirmation.',
                'No original control is repeated; prior controls, if any, are retained as historical evidence.'])

def sphere_math(qid):
    e=eligibility(qid); assert e['eligible']
    points=[(a,b,c,7-a-b-c) for a in range(8) for b in range(8-a) for c in range(8-a-b)]
    inner=[p for p in points if min(p)>0]
    shifted=[tuple(x-1 for x in p) for p in inner]
    layer_counts=dict(sorted(Counter(p[3] for p in inner).items()))
    assert len(points)==120 and len(inner)==20 and set(sum(p) for p in shifted)=={3}
    assert list(layer_counts.values())==[10,6,3,1]
    write(HERE/qid/'primary_math.json',dict(question_id=qid,checked_at=now(),
        derivation='An n-pyramid is the integer tetrahedron a+b+c+d=n-1, coordinates nonnegative. The four surface faces are coordinate zero, including d=0 for the base. Removing all outside balls requires all four coordinates >=1. Subtracting (1,1,1,1) gives sum 3, exactly a 4-pyramid. Its layers contain 10,6,3,1 balls.',
        all_8_pyramid_balls=points,interior=inner,shifted=shifted,interior_layers=layer_counts,
        source_3_pyramid_has_interior=False,correct_answer='B' if qid=='Solid158' else '4',
        explicitly_not_an_image_of_8_pyramid=True))

for qid in ['Solid158','Solid194']: sphere_math(qid)

qid='Solid153';s=read(PROJECT/BRANCH/eligibility(qid)['record']['scene']);objs={o['id']:o for o in s['objects']}
profiles={}
for name in 'ACDE':
    p=np.asarray(objs[name+'left']['points']); center=np.asarray(objs[name+'top']['center'])[:2]
    r=np.linalg.norm(p[:,:2]-center,axis=1);z=p[:,2]
    volumes=np.concatenate([[0],np.cumsum((r[1:]**2+r[:-1]**2)*np.diff(z)*math.pi/2)])
    profiles[name]=dict(total_volume=float(volumes[-1]),half_volume_height=float(np.interp(volumes[-1]/2,volumes,z)),
        bottom_radius=float(r[0]),middle_radius=float(r[len(r)//2]),top_radius=float(r[-1]),
        symmetry_radius_max_difference=float(max(abs(r-r[::-1]))),radius_nondecreasing=bool(np.all(np.diff(r)>=-1e-12)),
        radius_nonincreasing=bool(np.all(np.diff(r)<=1e-12)))
write(HERE/qid/'independent_profile_diagnostic.json',dict(method='Independent integration of actual frozen world-coordinate meridian radii; not measured PNG widths and not a new given.',profiles=profiles,
    human_proof='With equal total capacity and equal height, A has strictly increasing section area, so its lower half contains < half capacity and its half-litre level is above H/2. B has constant section; C and E are symmetric about H/2, so those levels equal H/2. D has decreasing section and a level below H/2. Hence only A is highest.',
    scope='Source contours are schematic. Numeric world volumes/levels are reconstruction diagnostics, not claimed original litre measurements.'))
spec=base(qid,'r51_reversed_capacity_profile_binding','Pair wide and narrow ends of A and D in reversed vertical roles.',
    'Bind A wide upper walls to D wide lower walls (red) and A narrow lower walls to D narrow upper walls (blue). Test reversing the vertical direction of cumulative capacity: transfer the high half-volume rise of an upward-flaring vase to the high narrow end of the downward-tapering vase, effectively using empty headspace instead of filled-from-base volume. This predicts D, not a local E-waist minimum.',
    'D','A is uniquely above half height; B,C,E exactly half height by constant section or up/down profile symmetry; D below half height by decreasing section area. Equal capacity is given, so this comparison uses within-vase volume fractions, not absolute silhouette widths.',
    dict(old='background_17 local_neck_cumulative_volume_confusion paired only A lower stem with E waist; preset E, A/A MISS.',
         new='Two distributed wide/narrow endpoint correspondences between A and D reverse the vertical volume profile. No E styling, no waterline, no narrowest-local-waist ranking.',
         substantive_difference='Orientation of full vertical capacity distribution and filled-vs-empty cumulative role; two different receiving regions with opposite height order.',
         preset_rationale_before_calls='An erroneous integration from the opening downward treats D narrow upper quarter as the capacity-accumulation region and chooses D. This is inconsistent with water being poured into the base.',
         old_final_answers_not_retargeted=True))
for pair,color in [([('A',.75,1),('D',0,.25)],'#DC2626'),([('A',0,.25),('D',.75,1)],'#2563EB')]:
    for name,lo,hi in pair:
        for side in ['left','right']:
            act=partial(qid,name+side,lo,hi,color);spec['actions'].append(act)
            spec['marker_roles'].append(dict(index=len(spec['actions'])-1,target=name+side,range=[lo,hi],
                role=('Wide end, paired across reversed height roles.' if color=='#DC2626' else 'Narrow end, paired across reversed height roles.'),
                source_receiver_group='A upper -> D lower' if color=='#DC2626' else 'A lower -> D upper',
                reason_both_sides='Both walls define the actual width of that end; neither side alone encodes a cross-section.'))
write(HERE/qid/'spec_r51.json',spec)

qid='Solid183';e=eligibility(qid);s=read(PROJECT/BRANCH/e['record']['scene'])
times=sorted({Fraction(i,n) for n in [5,3,4] for i in range(1,n)})
assert len(times)==9
write(HERE/qid/'primary_math.json',dict(diagonal='(5t,3t,4t), t in [0,1]',crossing_times=[str(t) for t in times],
    proof='Internal planes x=1..4, y=1..2, z=1..3 are crossed once each. Pairwise coprime dimensions imply all 9 crossing times distinct, agreeing with the given no-edge condition. There is one starting cube, then one new cube at each crossing: 1+9=10.',
    visited_cells=[list(map(lambda a: math.floor(a[0]*a[1]),[(5,(a+b)/2),(3,(a+b)/2),(4,(a+b)/2)])) for a,b in zip([Fraction(0)]+times,times+[Fraction(1)])],
    correct_answer='10'))
spec=base(qid,'r51_internal_plane_trace_to_visit_binding','Group existing internal division traces by the nine actual coordinate planes.',
    'Each continuous same-color surface L trace identifies one actual internal coordinate plane crossed by PQ. Substitute the count of true plane transitions (4+2+3=9) for the count of cubes, omitting the starting cube. The query diagonal remains implicit; no diagonal or internal crossing point is drawn, and marks themselves are not counted as cubes.',
    '9','Parameterize PQ=(5t,3t,4t). The 9 distinct crossing times are 1/5,1/4,1/3,2/5,1/2,3/5,2/3,3/4,4/5. Nine transitions plus the initial cube give exactly 10. All three counts and P/Q remain visible.',
    dict(old='Own old projected_diagonal_count draws PQ, preset11, complete finals10/11 MISS. Related Solid155 old projected line10/10 MISS preset11; r40 boundary walk12 first-tested in46:10/11 MISS. All frozen failed PNGs excluded.',
         new='No PQ ink and no outer boundary walk. Existing internal seams are grouped into 9 real plane traces across adjacent visible faces; wrong unit is transition versus visited cube.',
         substantive_difference='Interior boundary ownership and missing initial cell, not 2D projected intervals or 12 unit edges.',
         preset_rationale_before_calls='9 genuine plane crossings are mistakenly used as cube count; no old final9 has been chased.',
         source_receiver='The two visible face traces of each same coordinate plane are bound into one crossing event of the diagonally queried path.'))
plane_groups={}
for o in s['objects']:
    if o['type']!='segment': continue
    pts=np.asarray([s['points'][p] if isinstance(p,str) else p for p in o['points']])
    groups=[]
    for axis,n,color in [(0,5,'#DC2626'),(1,3,'#16A34A'),(2,4,'#2563EB')]:
        if pts[0,axis]==pts[1,axis] and pts[0,axis] in range(1,n): groups.append((axis,int(pts[0,axis]),color))
    assert len(groups)<=1
    if not groups: continue
    axis,k,color=groups[0]; key='xyz'[axis]+'='+str(k)
    act=dict(type='set_object_style',target=o['id'],color=color,linewidth_pt=1.5)
    spec['actions'].append(act);path=read(HERE/qid/'exact_paths.json')[o['id']]
    spec['marker_roles'].append(dict(index=len(spec['actions'])-1,target=o['id'],plane=key,
        exact_world_endpoints=pts.tolist(),exact_paths=path,
        role='Visible unit portion of the true '+key+' plane trace; joins the other face trace of the same plane. Counts a boundary event, not an extra ball, point, block or ink object.'))
    plane_groups.setdefault(key,[]).append(o['id'])
assert len(plane_groups)==9 and len(spec['actions'])==70
spec['plane_groups']=plane_groups
spec['conciseness']='70 schema actions are the existing unit fragments of 9 continuous traces. All 70 pieces are needed to identify each whole boundary consistently across the two visible faces; outer rims stay black.'
write(HERE/qid/'spec_r51.json',spec)

qid='Solid202';e=eligibility(qid);s=read(PROJECT/BRANCH/e['record']['scene']);p=s['points']
angles={}
for a,b,c in [('W','X','Y'),('X','Y','Z'),('Y','Z','W'),('Z','W','X')]:
    u=np.asarray(p[a])-p[b];v=np.asarray(p[c])-p[b]
    angles[b]=dict(vectors=[u.tolist(),v.tolist()],dot=int(u@v),length_squared=[int(u@u),int(v@v)],
        angle=math.degrees(math.acos(float(u@v/np.linalg.norm(u)/np.linalg.norm(v)))))
assert abs(sum(x['angle'] for x in angles.values())-330)<1e-10
write(HERE/qid/'primary_math.json',dict(actual_points={k:p[k] for k in 'WXYZ'},angles=angles,sum_degrees=330,correct_answer='B',
    proof='W=(0,0,0), X=(1,1,0), Y=(1,1,1), Z=(0,1,1). At X,Y,Z the dot products are zero, giving90 each. At W the two face diagonals (1,1,0),(0,1,1) have dot1 and squared lengths2, hence cos=1/2 and angle60. Total330, unique B.',
    old_narrative_correction='Old raw run1 ended B but its 60-degree-at-Z story used a misidentified front-right X. Current scene and source have both face diagonals meeting at W; the 60-degree angle is W. Old raw file remains unmodified.'))
spec=base(qid,'r51_axis_pair_to_face_diagonal_angle_binding','Bind the two edge directions at Y to the two face-diagonal directions at W.',
    'Source Y is a genuine 90-degree corner on the back face: YZ and YX. Match short YZ/WX ray portions in red and YX/WZ in blue. This tests carrying orthogonality of two face axes to two face diagonals which share a positive depth component; treating W as90 makes all four90 and predicts D360. It does not mark a closed WXYZ polygon.',
    'D','Exact current 3D points give X=Y=Z=90 and W=60; sum330, unique B. The shared depth component makes dot(WX,WZ)=1 rather than0. Four original arcs, all vertex positions and hidden edges remain intact.',
    dict(old='red_quadrilateral highlighted all4 full sides in one red closed loop, presetD. Actual run1 B and run2 started then aborted, no complete pair; absent summary did not mean no calls.',
         new='Only four short rays, in two directional correspondence groups, at the separated Y and W corners. No full side, closed loop, extra arc or right-angle symbol.',
         substantive_difference='Transfer of orthogonality from same-face edge axes to adjacent-face diagonals; not coplanarity or planar polygon sum.',
         same_wrong_preset_has_new_geometric_rationale=True,
         preset_rationale_before_calls='90 atY transferred to actual60 atW makes90+90+90+90=360, D.',
         old_run1_B_wrong_vertex_reasoning_preserved_and_separately_corrected=True))
for target,start,end,color,role in [
    ('line_7',.82,1,'#DC2626','Y->Z source ray: back-face horizontal axis, red pair with W->X bottom-face diagonal.'),
    ('line_12',0,.18,'#DC2626','W->X receiving ray: face diagonal with positive shared depth component, not a pure x axis.'),
    ('line_11',.82,1,'#2563EB','Y->X source ray: vertical axis orthogonal to Y->Z in the same back face.'),
    ('line_13',0,.18,'#2563EB','W->Z receiving ray: other face diagonal with the same positive depth component as W->X.')]:
    spec['actions'].append(partial(qid,target,start,end,color));spec['marker_roles'].append(dict(index=len(spec['actions'])-1,target=target,role=role))
write(HERE/qid/'spec_r51.json',spec)
print('Prepared three distinct hypotheses, no API calls. Sphere math independently enumerated twice for distinct source audits.')
