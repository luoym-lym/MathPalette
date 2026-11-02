from make28 import *
from partial_style import object_paths

q='Solid103';scene=AD.scene(q)
try:
    scene.fig.canvas.draw();m=[];path_record={}
    for target,start,end,role in [('edge3',0,3/8,'Front small-block3cm width, derived from75/(5*5), falsely transferred to rear strip depth.'),('edge8',0,2/7,'Rear strip2cm depth along left top boundary; marked counterpart of3cm front small-block width.')]:
        paths=object_paths(scene,target);assert len(paths)==1
        p=paths[0]
        path_record[target]={'id':p['id'],'sha256':p['sha256'],'controls':[s['control'].tolist() for s in p['segments']],'closed':p['closed']}
        obj=next(o for o in AD.scenes[q]['objects'] if o['id']==target)
        a,b=obj['points'];ends=[[a[i]+t*(b[i]-a[i]) for i in range(3)] for t in [start,end]]
        m.append(({'type':'set_object_style','target':target,'color':R,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}},
                  {'role':role,'original_world_full_edge':obj['points'],'world_selected_endpoints':ends,'projected_selected_endpoints':[project(q,v) for v in ends],'full_vector_path':path_record[target],'parameter_basis':'One original straight vector segment: exact affine parameter; endpoints correspond to existing block junctions.'}))
finally:scene.close()
make(q,'r28_small_width_to_rear_depth','D','Pair the front small-block width3cm with the rear question-strip depth2cm. Transfer the inferred3cm width to that depth, then use total width3+5=8to get8*3=24cm2, optionD.',
    'Old overall_top_envelope_binding styled four outer edges, targeting whole top56(E); old finalsA/Cmissed. The new design styles only two exact original partial intervals meeting real block junctions. It swaps two perpendicular DIFFERENT sub-block dimensions,3frontwidth versus2reardepth, and predeclaresD24; no old observed final is relabeled.',
    'Gray cube side5. The front small cuboid shares height5 and depth5, so width75/25=3; rear strip spans width8. Residual rear volume280-125-75=80 and height5 give rear top area80/5=16, optionA. Equivalently rear depth2timeswidth8. Same-color appearance does not add equality of3and2; both junctions, grayfill and?label remain.',m)

q='Solid109';m=[]
for a,b,role in [([0,0,4],[1,0,4],'One original x-direction unit shell span; intended width decrement1instead of2.'),([0,0,4],[0,1,4],'One original y-direction unit shell span; intended depth decrement1instead of2.'),([0,0,4],[0,0,3],'One original z-direction unit shell span; intended height decrement1instead of2.')]:m+=chain(q,a,b,O,role)
make(q,'r28_near_skin_only','36','Group the three one-unit skin thickness spokes at one near trihedral corner; subtract a skin only once per axis instead of from both ends:(5-1)*(4-1)*(4-1)=36.',
    'The earlier r28_interior_section_full_depth marked a3by2central section and full4depth, preset24; finals18/12missed. This does not keep that section or full-depth path. It marks three different one-unit near-corner spokes, targeting the distinct one-sided-shell subtraction on ALL3axes and preset36. No observed old final is chosen.',
    'A blue cube must have a red neighbor-shell removed from both ends of each of the three original axes. Source5by4by4 yields(5-2)*(4-2)*(4-2)=12. A legal orange1unit span is skin thickness, not the total2unit loss per axis; original topology and cube grid remain unchanged.',m)

q='Solid123';m=[]
m+=chain(q,[0,0,0],[0,0,3],R,'Full3-unit vertical exterior span of the L prototype bounding square; notch remains explicitly visible.')
m+=chain(q,[0,0,0],[3,0,0],R,'Full3-unit horizontal exterior span of the same L bounding square; together target bounding-area9instead of L area5.')
piece=[o for o in AD.scenes[q]['objects'] if o['type']=='segment' and o['id'].startswith('piece')]
ax=min(p[0] for o in piece for p in o['points']);az=min(p[2] for o in piece for p in o['points'])
m+=chain(q,[ax,0,az],[ax,0,az+3],R,'Assembled cube full3-unit front vertical span; counterpart for prototype bounding square.')
m+=chain(q,[ax,0,az],[ax+3,0,az],R,'Assembled cube full3-unit front horizontal span; actual9-unit square reference misbound to notched L5-unit footprint.')
make(q,'r28_L_bounding_square','3','Match two outer spans of the L prototype to the assembled3by3cube front square, replacing the L footprint5with its9unit bounding square. TwoLs plus two3unitbars are wrongly24cells, leaving27-24=3white.',
    'Earlier r28_L_leg_to_bar_span paired only a single3-unit L leg with the dark-bar3-unit span, preset15; finals1/5missed. New counterpart is the assembled complete3by3front-face frame, with a second orthogonal L span. This is a bounding-square versus notched-area substitution (9versus5), not a longest-leg versus bar-volume substitution (3versus5). The dark bar is no longer marked; the L notch is not filled or completed.',
    'Exact proper-rotation placement enumeration in primary_unique_math_enumeration.json yields one compatible cover:two5-cellLs,two3-cellbars,11white. The L occupies5of its9bounding-square cells; no added contour crosses its four-cell notch. The assembled3cube volume27and all three material classes remain intact.',m,['Small original assembly scale retained; colors do not equate material classes.'])
