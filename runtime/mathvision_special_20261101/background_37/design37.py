from tools37 import *
import numpy as np
import itertools, math

def scene(q):return read(TASK/q/'source_scene_snapshot.json')
def xyz(q,oid):
    s=scene(q);o=next(o for o in s['objects'] if o['id']==oid)
    return [s['points'].get(p,p) if isinstance(p,str) else p for p in o['points']]
def projected(q,p):
    p=np.array(p,float);pr=scene(q)['projection']
    return (np.array(pr['matrix'])@(p-np.array(pr['origin']))+np.array(pr['offset'])).tolist()
def styles(q,items):
    actions=[];roles=[]
    for oid,color,role in items:
        o=next(o for o in read(TASK/q/'context.json')['objects'] if o['id']==oid);assert o['styleable']
        a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2}
        actions.append(a);roles.append({'action':a,'role':role,'world_endpoints':xyz(q,oid),'projected_endpoints':[projected(q,p) for p in xyz(q,oid)],'partial_paths':o.get('partial_paths',[]),'source_object_geometry_sha256':canonical_hash(o['geometry']),'new_geometry':False})
    return actions,roles
def overlays(q,items):
    actions=[];roles=[]
    for i,(oid,a,b,c,role,contact) in enumerate(items):
        p=np.array(xyz(q,oid),float);a=np.array(a,float);b=np.array(b,float);v=p[1]-p[0]
        tt=[float((x-p[0])@v/(v@v)) for x in [a,b]]
        assert all(-1e-12<=t<=1+1e-12 for t in tt)
        assert max(np.linalg.norm(x-(p[0]+t*v)) for x,t in zip([a,b],tt))<1e-12
        action={'type':'add_line','id':f'contact_{i+1}','endpoints':[projected(q,a),projected(q,b)],'color':c,'linestyle':'solid','linewidth_pt':1}
        actions.append(action);roles.append({'action':action,'role':role,'existing_object':oid,'existing_object_full_world_endpoints':p.tolist(),'world_endpoints':[a.tolist(),b.tolist()],'affine_parameters_on_original_segment':tt,'contact_cube_pair':contact,'coordinate_basis':'Exact existing cube-contact edge in current source model, affine projection from frozen scene, not measured pixels. No hidden segment or new physical edge.','source_object_geometry_sha256':canonical_hash(next(o for o in read(TASK/q/'context.json')['objects'] if o['id']==oid)['geometry'])})
    return actions,roles
def union_area(boxes):
    axes=[sorted({b[k][d] for b in boxes for k in ['min','max']}) for d in range(3)]
    cells=set()
    for ix in itertools.product(*(range(len(a)-1) for a in axes)):
        m=[(axes[d][ix[d]]+axes[d][ix[d]+1])/2 for d in range(3)]
        if any(all(b['min'][d]<m[d]<b['max'][d] for d in range(3)) for b in boxes):cells.add(ix)
    area=ground=0
    for ix in cells:
        for d in range(3):
            for side in [-1,1]:
                other=list(ix);other[d]+=side
                if tuple(other) not in cells:
                    a=math.prod(axes[k][ix[k]+1]-axes[k][ix[k]] for k in range(3) if k!=d);area+=a
                    if d==2 and side==-1 and axes[2][ix[2]]==0:ground+=a
    return {'full_surface_area':area,'ground_area':ground,'painted_area':area-ground}
def contacts(boxes):
    out=[]
    for i,a in enumerate(boxes):
        for j,b in enumerate(boxes[i+1:],i+1):
            for d in range(3):
                if a['max'][d]!=b['min'][d] and b['max'][d]!=a['min'][d]:continue
                lengths=[min(a['max'][k],b['max'][k])-max(a['min'][k],b['min'][k]) for k in range(3) if k!=d]
                if all(v>0 for v in lengths):out.append({'pair':[i,j],'normal_axis':d,'area':math.prod(lengths)})
    return out
def model(q):return read(TASK/q/'source_geometry_notes.json').get('additional_model_evidence',{})

if sys.argv[1:]==['math']:
    proofs={}
    parts=model('Solid102')['solid_parts'];boxes=[];individual=[]
    for p in parts['unit_cubes']:
        boxes.append({'min':p,'max':[v+1 for v in p]});individual.append({'origin':p,'size':[1,1,1],'surface_area':6})
    for p in parts['cuboids']:
        a,b,c=p['size'];boxes.append({'min':p['origin'],'max':[x+y for x,y in zip(p['origin'],p['size'])]});individual.append({**p,'surface_area':2*(a*b+a*c+b*c)})
    proofs['Solid102']={'parts':individual,'union':union_area(boxes),'separate_area':sum(p['surface_area'] for p in individual),'paint_liters':18*union_area(boxes)['full_surface_area']/sum(p['surface_area'] for p in individual),'wrong_rule':'Only upper3x1x1block inherits whole6-face unit-cube area6 via two genuine unit short sides; lower3x1x2 remains22. Wrong denominator36+6+22=64, numerator46 unchanged.','frozen_wrong_liters':18*46/64}
    proofs['Solid126']={'original_dimensions':[12,6,8],'cut_dimensions':[9,6,3],'original_area':432,'remaining_area':378,'removed_top_replaced_by_floor_area_each':54,'removed_end_replaced_by_cut_side_area_each':18,'front_and_back_losses_each':27,'decrease':54/432,'unique_answer':'B','wrong_rule':'Extrapolate the two true cancellation pairs to all removal, omit both27front/back losses,0%=>A.'}
    for q in ['Solid160','Solid196']:
        proofs[q]={'unit_cube_area':24,'unit_face_area':4,'dimensions_in_small_cube_units':[2,1,2],'four_cube_origins':[[0,0,0],[1,0,0],[0,0,1],[1,0,1]],'contacts':[[0,1],[2,3],[0,2],[1,3]],'front_back_unit_faces':[4,4],'top_bottom_unit_faces':[2,2],'left_right_unit_faces':[2,2],'surface_area':64,'unique_answer':AD.records[q]['answer']}
    proofs['Solid160']['wrong_rule']='4red front,2blue top,2green right visible-face representatives omit opposite faces:8*4=32,D.'
    proofs['Solid196']['wrong_rule']='Four distinct unit contact traces each mapped to one hidden unit face instead of two:96-4*4=80.'
    proofs['Solid177']={'dice_count':7,'all_dots':147,'six_center_face_total':21,'matching_arm_face_total':21,'surface_dots':105,'hypothesis':'Count contact-pair total once gives126, but no clean six-interface visual encoding is available.','skip_geometry':'Left(x=0),rear(y=1),bottom(z=0) central contact faces have no positive-length visible perimeter segment in current edge registry; three front/up/right traces overlap at the same center corner. Encoding six would invent hidden edges or substitute unrelated arm contour.'}
    for q in ['Solid224','Solid231']:
        bs=model(q)['solid_models'];proofs[q]={'source_boxes':bs,'exact_union':union_area(bs),'all_pair_contacts':contacts(bs),'independent_area_formula':6*len(bs)-2*sum(c['area'] for c in contacts(bs))}
    proofs['Solid224'].update(layer_footprints=[9,4,1],interlayer_contact_areas=[4,1],area_from_merged_layers='30+16+6-2*(4+1)=42; minusground9=33',wrong_rule='Subtract every layer bottom from already-unioned42:42-(9+4+1)=28; upper5already internal, double excluded.',wrong_answer=28)
    proofs['Solid230']={'dice_count':3,'each_die_total_pips':21,'all_pips':63,'visible_faces':{'bottom_front':5,'bottom_right':1,'middle_front':4,'middle_right':6,'top_front':2,'top_right':3,'top_top':1},'visible_pips':22,'hidden_pips':41,'wrong_rule':'Treat equal-valued top1andbottom-right1 as one visible record:visible21,hidden63-21=42.','pip_modifications':False}
    proofs['Solid231'].update(wrong_rule='Five genuine contact records subtracted once each:36-5=31 instead of36-2*5=26.',wrong_answer=31)
    assert proofs['Solid102']['separate_area']==72 and proofs['Solid102']['union']['full_surface_area']==46
    assert proofs['Solid224']['exact_union']['painted_area']==33 and proofs['Solid231']['exact_union']['full_surface_area']==26
    write(TASK/'independent_primary_math_audit.json',{'kind':'Author primary derivation, not independent second review','created_at':now(),'proofs':proofs,'method':'Independently recompute axis-aligned box union on exact coordinate subdivision; contact areas from overlap products; no solver outputs used.'})
    print(json.dumps(proofs,ensure_ascii=False));sys.exit()

M=read(TASK/'independent_primary_math_audit.json')['proofs']
for q in sys.argv[1:]:
    if q=='Solid102':
        items=[('outlinee11',RED,'Source unit cube left-front vertical side length1'),('outlinee10',RED,'Source unit cube top depth side length1, forms open unit corner with source vertical'),('outlinee21',RED,'Target upper3x1x1block right-front height side length1'),('partseam6',RED,'Target upperblock true top depth edge length1, open corner transfers two unit dimensions but leaves actual length3black')]
        a,r=styles(q,items);render(q,'r37_unit_corner_to_upper_block',a,'12.9375','Match two genuine unit short sides of one small cube to upper rectangular block; target extrapolating unit height/depth to whole block surface6 while actual3length remains.',M[q],r,'No prior design/calls. New open two-side unit corner correspondence targets only the upper3x1x1block; does not falsely assert lower3x1x2block has a unit front side. Wrong ratio46/64 independently frozen; not a full contour or missing-corner completion.')
    elif q=='Solid126':
        a,r=styles(q,[('removed1',RED,'Removed top9x6: existing dashed9-unit rear rim'),('removed2',RED,'Removed top9x6: existing dashed6-unit depth rim forming open L'),('ring1e4part0',RED,'New floor9x6: existing9-unit rear rim corresponding to removed top'),('depth5part0',RED,'New floor9x6: existing6-unit depth rim completing matching open L'),('removed4',BLUE,'Original outer end side removed height3, full common depth6unchanged'),('ring0e3part0',BLUE,'New cut side height3 matching old end side, common depth6unchanged')])
        render(q,'r37_local_area_replacement',a,'A','Pair removed top with new floor and removed end with new cut side; target extending these true local cancellations to all surface loss and omitting front/back holes.',M[q],r,'Old3red verticalheight5=>3misbinding with presetC was a MISS(A/A). New6edges form a red9x6open-L area pair plus blue true3height end/cut-side pair; no5-height source mark. New presetA arises from this independently computed cancellation mechanism, never relabeling oldA/A.')
    elif q=='Solid160':
        a,r=styles(q,[('slabe0',RED,'Front lower-left unit face: its bottom edge'),('slabe10',RED,'Front lower-right unit face: its bottom edge'),('slabe8',RED,'Front upper-left unit face: its outer left edge'),('slabe19',RED,'Front upper-right unit face: its outer right edge'),('slabe5',BLUE,'Top left unit face: rear rim'),('slabe17',BLUE,'Top right unit face: rear rim'),('slabe12',GREEN,'Right lower unit face: bottom depth edge'),('slabe20',GREEN,'Right upper unit face: rear vertical edge')])
        render(q,'r37_visible_unit_face_representatives',a,'D','Use one actual unit edge per visible unit face grouped4front/2top/2right; target8visible faces counted as total surface32.',M[q],r,'Old6continuous contact-plane traces presetA(80) missed B/B. New8surface-cell representatives omit all old6targets, group actual external area owners in three directions, target missing opposite faces32(D), not contact-plane multiplicity.')
    elif q=='Solid196':
        a,r=styles(q,[('slabe3',RED,'Lower left/right cube contact atx1,z0..1: one front unit seam records interface[0,1]'),('slabe9',BLUE,'Upper left/right cube contact atx1,z1..2: one front unit seam records interface[2,3]'),('slabe1',GREEN,'Left lower/upper contact atz1,x0..1: one front unit seam records interface[0,2]'),('slabe11',ORANGE,'Right lower/upper contact atz1,x1..2: one front unit seam records interface[1,3]')])
        render(q,'r37_four_single_side_contact_records',a,'80','Four separately colored true unit-contact seams encode four one-sided records; target subtracting one4cm2face per contact instead of both faces.',M[q],r,'Old8face-centerpoints preset32 missed64/64. New4existingunitcontactedges, each different pair/owncolor, no points or visibleface-count grouping. Not oldSolid160two3-edgeplanetraces: every unit contact separately retained; intended error is single-vs-double sided subtraction80.')
    elif q=='Solid224':
        a,r=styles(q,[('line_0',RED,'Ground-contact front bottom rim of3x3base layer, actual length3'),('line_18',RED,'Middle2x2layer front bottom contact rim atz1,y0.5,length2'),('line_32',RED,'Top1x1layer front bottom contact rim atz2,y1,length1')])
        render(q,'r37_layer_bottom_ground_transfer',a,'28','Match actual front bottom rims of all three layers; target transferring ground exclusion from base9to upper4+1already-internal bottoms.',M[q],r,'Prior prescreen had no design/call and held a terrace/top telescoping scaffold supporting correct33. New correspondence uses only bottom/contact rims across levels and predicts extra5exclusion28. Exact half-offset cube contacts independently recomputed; no artificial full unit grid.')
    elif q=='Solid230':
        a,r=styles(q,[('line_10',RED,'Open rear rim of top die top face showing exactly1pip'),('line_2',RED,'Open bottom rim of bottom die right face showing exactly1pip; different normal and different die')])
        render(q,'r37_equal_value_face_identity',a,'42','Pair one existing open rim on each of the two1pipfaces; target equal pip value collapsing two distinct visible records into one,hidden42.',M[q],r,'No old designs or calls. New two-true-face value/identity correspondence selects only actual1faces, not all dots or generic contour salience. Dots remain originalblack positions and counts, normals clear, no joining line between faces.')
    elif q=='Solid231':
        items=[('line_1',[1,1,1],[2,1,1],RED,'Central bottom/middle contactz1 one unit seam',[0,1]),('line_7',[1,1,2],[2,1,2],RED,'Central middle/top contactz2 one unit seam',[1,2]),('line_4',[2,1,1],[2,1,2],BLUE,'Middle/right contactx2 one unit seam',[1,3]),('line_3',[1,1,0],[1,1,1],GREEN,'Bottom central/left rear contactx1 visiblefront boundary',[0,4]),('line_1',[0,1,1],[1,1,1],ORANGE,'Left front/rear cubes contacty1 visible top seam',[4,5])]
        a,r=overlays(q,items);render(q,'r37_unit_contact_single_subtraction',a,'31','Five existing unit-contact edge records target subtracting5faces once rather than10faces in pairs.',M[q],r,'No prior design/call. New exact5contactregistry mapped to5existingvisibleedgeintervals; no projectionvertex counted as contact and no hidden seam added. Different unit traces distinguish five pair contacts, not central/branch matching or shape completion.')
    else:raise ValueError(q)
