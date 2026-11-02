from tools57 import *
from collections import Counter
import math
def native(q):
    docs=read(HERE/q/'source_documents_full.json')
    return next(v for k,v in docs.items() if k.endswith('/scene.json'))
proofs={}
proofs['Solid79']=read(HERE/'Solid79/spec_r57.json')['primary_math_proof']
proofs['Solid214']=dict(method='Eight coordinate-orthant tetrahedra; no stored answer used',geometry='Prism side lengths3,4,5. Translate center to origin: face centers(+-3/2,0,0),(0,+-4/2,0),(0,0,+-5/2).',calculation='In each orthant the tetrahedron has perpendicular intercepts3/2,4/2,5/2; volume(3/2)(4/2)(5/2)/6=60/48. Eight such tetrahedra give60/6=10.',unique_answer='B=10',native_finding='Original JPG and formal768PNG contain only12prism edges and3length labels. No face-center vertices or octahedron edges are displayed. Fresh context has12styleable edges, no editable center-to-center path.')
c=1.;a=c;b=c/math.sqrt(3)
proofs['Solid216']=dict(method='Independent vector proof with H as origin',coordinates=dict(H=[0,0,0],G=[a,0,0],D=[a,0,c],F=[0,b,0],B=[0,b,c]),derivation='cos45=a/sqrt(a²+c²) impliesa=c. cos60=b/sqrt(b²+c²) impliesc²=3b². HD·HB=c²; normproduct=sqrt(2)c*(2c/sqrt3). ThuscosBHD=sqrt6/4.',value=math.sqrt(6)/4,unique_answer='D',native_finding='Actual original/formal angle arcs are GHD45 andFHB60 on different perpendicular faces. GH andHF are true perpendicular edges, not a straight angle. Flattening them into180 is a false premise; actual source point registry confirmsHG=(1,0,0),HF=(0,1/sqrt3,0).')
solutions=[];rejected=[]
for n in range(10,12):
    pair_sum=2*n+5
    bad=[(x,y) for x,y in [(11,14),(11,15),(14,15)] if x+y==pair_sum]
    if bad: rejected.append(dict(first=n,pair_sum=pair_sum,opposite_but_actually_adjacent=bad))
    else: solutions.append(dict(numbers=list(range(n,n+6)),pair_sum=pair_sum,total=sum(range(n,n+6))))
assert len(solutions)==1 and solutions[0]['total']==81
proofs['Solid225']=dict(method='Exhaust all consecutive whole-number ranges containing visible11,14,15',admissible_minima=[10,11],rejected=rejected,solution=solutions[0],unique_answer='81',native_finding='Three visible labeled faces meet pairwise along original edges and at one corner; none are opposite. Text and face fills are frozen and not editable targets.')
for q in ['Solid232','Solid233']:
    s=native(q)
    cubes=[tuple(m['min']) for m in s['solid_models']]
    assert all(tuple(m['max'][i]-m['min'][i] for i in range(3))==(1,1,1) for m in s['solid_models'])
    degree={str(p):sum(sum(abs(p[i]-r[i]) for i in range(3))==1 for r in cubes) for p in cubes}
    hist=dict(Counter(degree.values()))
    edges=sum(degree.values())//2;surface=6*len(cubes)-2*edges
    proofs[q]=dict(method='Fresh face-adjacency enumeration from actual frozen3Dunit cells, checked against native sources',cells=cubes,degrees=degree,degree_histogram=hist,contact_pairs=edges,surface=surface,volume=len(cubes),native_finding='Original JPG and formal768PNG independently viewed; every unit count, white face, exposed seam, support and projected overlap retained.')
    if q=='Solid232':
        assert len(cubes)==14 and hist=={3:4,2:6,1:4}
        proofs[q].update(unique_answer='6',reason='A cube of contact degreed has6-dexposed faces. Complete surface includes underside, so exactly4painted iffdegree2; sixbase-ring cells have degree2. Fourbasecorners have3contacts and fourtopcornercubes have1.')
    else:
        assert len(cubes)==7 and edges==6 and surface==30
        proofs[q].update(unique_answer='D=7:30',reason='One central cube contacts six mutually nonadjacent arms. Sevenunitvolumes;42individualfaces minus2for each of6joins=30. Subtracting each join only once gives wrong36,B.')
proofs['Solid234']=read(HERE/'Solid234/spec_r57.json')['primary_math_proof']
proofs['Solid247']=dict(method='Independent oblique-coordinate plane equation and axial integration',coordinates='D=(0,0,0), E=12u, F=12v, C=16k, A=12u+16k, B=12v+16k; unitvectorsu·v=1/2,kperpendicularu,v.',plane='Writing position=su+tv+zk, the unique plane throughM(4,0,0),N(0,2,0),Q(8,0,16) is s/4+t/2-z/16=1. OnCB, s=0,z=16 =>t=4,soCP=4 and allMNPQarecoplanar.',areas='Atheightz, intercepts4(1+z/16),2(1+z/16) enclose angle60. Sectionarea=2sqrt3(1+z/16)^2.',integral='Integral0^16 2sqrt3(1+z/16)^2 dz=32sqrt3*(8-1)/3=224sqrt3/3.',unique_answer='224sqrt3/3',native_finding='Native original/formal preserveA-F,MNPQ, original12and16andallcutdashes. Source world pointP=(2,6.9282032302755105,16) givesCP=4, consistent with independently solvedplane;M,N,Qcoordinates and usergivenDM4/DN2/CQ8 agree.')
reasons={
'Solid214':dict(status='skipped_no_legal_visible_facecenter_receiver',new_direction_examined='Bind a full3/4/5prism span to a genuine half-span at its facecenter.',concrete_skip='Fresh native source/context has no displayed face centers or center-to-center edges. Recoloring only12boundaryedges has no receiver for the required octahedron half-span. New center dots, octahedron edges or perpendiculars would introduce derived solving geometry forbidden by this unit. Existing old no-design objection survives independent inspection.',old='background_17/Solid214/prescreen.json'),
'Solid216':dict(status='skipped_no_true_component_receiver',new_direction_examined='Bind commonH45-face and60-face rays to encourage angle sum/difference or cosine transfer.',concrete_skip='SourceGH/HF are perpendicular worlddirections and45/60livein differentfaces. Getting listedE=cos75requires an unjustified180degreecoplanar total; marking sharedH/rays does not create a true information donor/receiver that makes this reading coherent. Mapping cosine45to otherface only re-highlights wrongangle. No added coplanarity/straight-line/angle marks or screen-angle premise accepted.',old='background_18/Solid216/assessment.json'),
'Solid225':dict(status='skipped_no_visible_opposite_face_receiver',new_direction_examined='Use actual adjacentface boundaries to stand for threeoppositepair representatives, or duplicate onepair.',concrete_skip='Only three mutually adjacent numbered faces are shown. Each true oppositeface receiver is hidden and unnumbered. Marking oneface label/rim would be salience; pairing11and14asopposites contradicts their visible sharededge. No clean value-specific correspondence remains without inventing a relation or unknownnumber.',old='background_16/Solid225/prescreen.json'),
'Solid232':dict(status='skipped_black_style_has_no_complete_contact_count_transfer',new_direction_examined='One real contactseam and oneexteriorunitfaceedge with black-onlylocalwidth, to substitute visiblefacecount for6-degree.',concrete_skip='Avoids oldpaint ambiguity, but an isolated rim/width pair does not encode which unseenfaces are unpainted or transfer a consistent complete count of degree2cells. The long frozen lines merge/cross rims of differentcubes; width grouping either outlines a proposedcountedset or leaves contact/visibleface association ambiguous. No visibleface-only numericalpreset has a fully specified receiver. No red/colorpaint, extra point/face/cube, selecteddegree2set or newhiddenadjacency used.',old='background_14/Solid232/prescreen.json'),
'Solid233':dict(status='skipped_shared_seam_single_side_not_uniquely_bound',new_direction_examined='Compare a one-sided real contactfacerim with an exteriorunitface border, inviting42-6=36.',concrete_skip='Atprojectedcentralcorner the visible centralrimsegments each belong to2possible contactfaceperimeters; opposite3interfaces have no displayedrim. A singleLdoes not distinguish which singlecontactface is counted; adding a centraljunction or substituting outerarmcontours for invisiblejoins repeats prior ambiguity. Fresh3Dcontacts correct6but no clean source/receiver exemplar uniquely accounts for subtracting onefaceperjoin. No arbitrarycap onmarks imposed.',old='background_13/Solid233/checkpoint record; relatedbackground_37/Solid177 contactvisibility audit'),
'Solid247':dict(status='skipped_ratio_marking_only_encodes_true_correspondence',new_direction_examined='MatchDE/DFfull/subspans toCA/CBcutintercepts, or matchlinear2:1sizes tovolumeratio.',concrete_skip='True planar parallelbase sections forceCQ:DM=CP:DN=2. Markingtheseactualpartners communicates the correctCP4; cross-swapping would contradict angle/lengthmembership. Linearvolume or midpointarea misuse needs an undrawn area/volume receiver, so edge-onlystyling is formula salience rather than a new explicit partmatch. No midpointsection or falseparallel/equality introduced.',old='background_04/Solid247/primary_prescreen.json')}
for q in IDS:
    write(HERE/q/'primary_math_native_review.json',dict(question_id=q,review_kind='PRIMARY research only',reviewed_at=now(),actual_original_JPG_viewed=True,actual_formal_native_768_PNG_viewed=True,fresh_no_op_verified=read(HERE/q/'baseline_check.json')['no_op_pixel_equal'],unique_answer_proof=proofs[q],formal_original_not_reapproved=True))
    if q in reasons:
        write(HERE/q/'assessment.json',dict(question_id=q,assessed=True,**reasons[q],new_designs=0,API_calls=0,unworked=False,math_review=str(HERE/q/'primary_math_native_review.json'),hypothesis_not_forced=True))
    else:
        spec=read(HERE/q/'spec_r57.json')
        write(HERE/q/'assessment.json',dict(question_id=q,assessed=True,status='substantive_new_design_native_reviewed',variant_id=spec['variant_id'],expected_wrong_answer=spec['expected_wrong_answer'],unworked=False,old_history_preserved=True))
write(HERE/'math_calculation_audit.json',proofs)
print('All eight assessed; six concrete skips; two frozen designs. Primary review only.')
