from common38 import *
import math
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
M=read(TASK/'math_audit.json')
def style(t,c,start=None,end=None,w=2):
    a={'type':'set_object_style','target':t,'color':c,'linewidth_pt':w}
    if start is not None:
        p=PATHS[t][0];a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
    return a
def save(q,v,wrong,actions,roles,mechanism,difference):
    folder=TASK/q/v;folder.mkdir(exist_ok=False)
    check=eligibility(q);assert check['eligible'],check
    write(folder/'eligibility_before_design.json',check)
    write(folder/'design_difference_audit.json',dict(question_id=q,variant_id=v,created_at=now(),historical_evidence=str(TASK/q/'history_audit.json'),substantive_difference=difference,new_feature=mechanism,not_cosmetic=True,old_misses_not_relabelled=True,independently_computed_expected_wrong_answer=wrong,math=M[q]))
    c=AD.inspect_question(q);write(folder/'context.json',c)
    renderer=PluginRenderer(CONFIG,AD,{q:c})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    normalized,data,digest=renderer.render(plugin)
    norm2,again,dig2=renderer.render(normalized,frozen=True)
    assert norm2==normalized and data==again and digest==dig2
    write(folder/'plugin.json',normalized);(folder/'candidate.png').write_bytes(data);(folder/'repeat.png').write_bytes(again)
    bindings=paths(q,sorted({a['target'] for a in normalized['params']['actions'] if a['type']=='set_object_style'}))
    write(folder/'marker_path_bindings.json',bindings)
    objects={o['id']:o for o in c['objects']}
    write(folder/'design.json',dict(question_id=q,variant_id=v,created_at=now(),expected_wrong_answer=wrong,formal_correct_answer=AD.records[q]['answer'],mechanism=mechanism,mathematical_solution=M[q],marker_roles=[dict(action_index=i,action=a,role=r,source_object=objects.get(a.get('target'))) for i,(a,r) in enumerate(zip(normalized['params']['actions'],roles))],candidate_png_sha256=sha(folder/'candidate.png'),pixel_sha256=digest,context_sha256=sha(folder/'context.json'),path_bindings_sha256=sha(folder/'marker_path_bindings.json'),schema_valid=True,defaults_normalized=True,no_op_pixel_equality=c['original_pixel_sha256']==pixel_hash(AD.original_paths[q]),repeat_byte_identical=True,environment=environment_versions(),review_status='PRIMARY_ONLY; parent NEW independent second review required',solver_input='formal question and candidate image only; no intent, preset, proof or parameters'))
    write(folder/'render_check.json',dict(schema_valid=True,normalization_exact=norm2==normalized,baseline_pixel_sha256=c['original_pixel_sha256'],formal_pixel_sha256=pixel_hash(AD.original_paths[q]),repeat_byte_identical=True,png_sha256=sha(folder/'candidate.png'),repeat_png_sha256=sha(folder/'repeat.png'),plugin_sha256=sha(folder/'plugin.json'),frozen_input_hashes={k:AD.manifest['files'][k] for k in AD.dependencies(q)}))
    print(q,v,len(actions),wrong,flush=True)
q=sys.argv[1]
allids=[o['id'] for o in read(TASK/q/'context.json')['objects'] if o['styleable']]
PATHS=paths(q,allids)
if q=='Plane179':
    objects=read(TASK/q/'context.json')['objects']
    def cart(p):return [p[0]+p[1]/2,p[1]*math.sqrt(3)/2]
    def edge(a,b):
        a,b=cart(a),cart(b)
        def near(p,r):return all(abs(x-y)<1e-10 for x,y in zip(p,r))
        found=[o['id'] for o in objects if o['id'].startswith('grid') and ((near(o['geometry']['points'][0],a) and near(o['geometry']['points'][1],b)) or (near(o['geometry']['points'][0],b) and near(o['geometry']['points'][1],a)))]
        assert len(found)==1,(a,b,found)
        return found[0]
    specs=[((0,5),(1,5),RED,'Exemplar full unit-triangle base.'),((0,5),(0,6),BLUE,'Exemplar full unit-triangle second edge; open V, third existing black edge intact.'),((3,1),(4,1),RED,'First ABC-crossed cell base, only5/6 of this cell is gray.'),((3,1),(3,2),BLUE,'First crossed-cell second edge.'),((3,2),(4,2),RED,'Second ABC-crossed cell top base, only1/6 of this cell is gray.'),((4,1),(4,2),BLUE,'Second crossed-cell second edge, a rotated counterpart of the exemplar.')]
    actions=[style(edge(a,b),c) for a,b,c,r in specs]
    M[q]['wrong']='B';M[q]['wrong_derivation']='Exact clipping gives up_3_1 area5/6 and down_3_1 area1/6. Counting these two crossed unit cells as two instead of total1 while counting the rest exactly gives11-1+2=12, B. All marked edges are preexisting unit cell boundaries; no imaginary clipped triangle is closed.'
    save(q,'r38_unit_cell_partial_area_transfer','B',actions,[r for a,b,c,r in specs],'Pair an intact unit cell two-edge V with two ABC-crossed lattice cells of true shaded areas5/6 and1/6, targeting whole-cell counting in place of shaded area.','Old all-three-ABC-edges red outline targetedB but had completed final4 MISS and second transport failure. New untouched ABC boundary and six existing lattice edges bind a full unit cell to two partial cells with exact area-sum1; no whole-ABC emphasis, cosmetic repeat or borrowed old final4.')
elif q=='Plane188':
    actions=[style('Npart0',RED,.25,.5),style('Npart2',RED,.25,.5),style('Npart0',BLUE,0,.25),style('Npart2',BLUE,0,.25)]
    roles=['Vertical stem true height6 reference.','Diagonal side length2sqrt10 falsely substituted for perpendicular height6.','True stem base1 reference.','True diagonal parallelogram horizontal base1 matches reference.']
    save(q,'r38_oblique_height_unit_transfer','12+2*sqrt(10)',actions,roles,'Pair the actual1-unit horizontal bases and the6-unit stem height with the slant side of the diagonal parallelogram; target side-length versus perpendicular-height substitution.','No prior retained design/API. New two-feature base/height correspondence rather than whole-N emphasis; all three semantic gray strips and all grid fragments unchanged.')
elif q=='Plane224':
    actions=[style('square3',RED,0,.25),style('square2',RED,0,.25)]
    save(q,'r38_compound_span_unit_transfer','77/9',actions,['Actual smallest-square bottom side length1.','Existing middle-square bottom side spans all three labeled smallest squares, actual length3; false unit counterpart.'],'Bind the one-unit base of one labeled square to the three-unit base of the square immediately above the small row.','No prior retained design/API. Local true-unit-to-compound-span correspondence transfers length scale and area scale, rather than arbitrary largest-square salience; three1 labels and all seams remain intact.')
elif q=='Plane229':
    actions=[];roles=[]
    # two-cell open portions at each end of each outer side; same corner belongs to two side groups
    specs=[(RED,2,['frame8','frame10','frame22','frame31'],'top'),(BLUE,0,['frame0','frame9','frame21','frame23'],'bottom'),(GREEN,3,['frame0','frame1','frame7','frame8'],'left'),(ORANGE,1,['frame23','frame24','frame30','frame31'],'right')]
    for col,edge,ids,name in specs:
        for t in ids:
            actions.append(style(t,col,edge/4,(edge+1)/4));roles.append(f'{name} side membership of '+t+'; corner shares adjacent side colors on different preexisting edges, straight neighbor anchors group.')
    save(q,'r38_corner_double_membership','48',actions,roles,'Use four side color groups on short existing outer-edge runs, assigning each real corner to both adjacent sides and inviting duplicate corner counting.','No prior design/API. Four corner-to-side ownership relations; only two-cell runs at each end, central five-cell portions untouched. Not a uniformly recolored ring; no photograph artwork, tile fill, seam, count or inner boundary edited.')
elif q=='Plane250':
    ts=['path2_0','path2_1','path2_2','path3_2','path3_6']
    actions=[style(t,RED) for t in ts]
    roles=['Rin U-step upward3dm.','Rin U-step horizontal4dm.','Rin U-step downward3dm; combined U has total10 but horizontal span4.','Tin first horizontal4dm is falsely matched to total U10dm.','Tin second horizontal4dm is falsely matched to total U10dm.']
    save(q,'r38_U_journey_to_advance','47',actions,roles,'Match Rin single-column up-horizontal-down journey to Tin two single-column horizontal advances, targeting journey length versus horizontal span.','Old Fin diagonal-to-Tin-vertical5dm substitution targeted43 and finals21.5/31.25 both MISS. New source is Rin three-edge U total10 and new targets are Tin horizontals, deriving47 before calls; no old four marked objects or observed wrong-output retuning.')
elif q=='Plane254':
    actions=[style('o6',RED,w=1),style('o1',RED,w=1.5),style('o8',BLUE,w=1),style('o3',BLUE,w=1.5)]
    save(q,'r38_center_to_right_boundary','E',actions,['First left-center original black dot rim; center remains black-filled.','First rectangle right boundary, falsely bound to first left center.','Third rectangle center original black dot rim; center remains black-filled.','Third rectangle right boundary, falsely bound to second left center.'],'Pair the left center of each measured segment with its own rectangle right divider, targeting endpoint identity versus region boundary.','Old entire centerlines red/blue and central divider salience failed B/B. New center dots remain black-filled and centerlines black; two specific center-to-boundary identity substitutions derive variable (b+d)/2 and E. Same final hypothesis E has a distinct algebraic error and four newly bound objects; no cosmetic retest.')
elif q=='Plane256':
    actions=[style('ribbon0_2',RED,5/12,.5),style('ribbon1_0',RED,5/12,.5)]
    save(q,'r38_single_exposure_material_edge','25',actions,['S third-length ribbon right edge y50..75, currently touching longest ribbon.','Same actual material edge translated by(45,0) to T first ribbon right edge y50..75, now exposed.'],'Track one25cm material edge from an internal contact in S to exposed boundary in T, inviting a single-exposure count instead of the doubled net contact loss.','Old complete shortest/longest ribbon outlines targeted material-invariance0 and have no saved invocation. New only third-length ribbon local contact/exposure edge, not whole material contours. Red ink transport is physically consistent under translation(45,0); numeric union perimeter remains50 regardless of ink.')
elif q=='Plane258':
    actions=[];roles=[]
    for id,xy,c,role in [('unit_top',[1,7],RED,'Top of actual1-unit black vertical reference.'),('long_top',[2,6],RED,'Top of actual2-unit black vertical false counterpart.'),('unit_bottom',[1,6],BLUE,'Bottom of unit reference.'),('long_bottom',[2,4],BLUE,'Bottom of2-unit false counterpart.')]:
        actions.append(dict(type='add_point',id=id,xy=xy,color=c));roles.append(role)
    save(q,'r38_black_route_endpoint_unit_binding','B',actions,roles,'Pair the endpoints of a true smallest-square black side with the endpoints of a two-unit black vertical run, inviting one-unit undercount.','Prior assessment rejected gray-edge recoloring because black path membership would change. New exclusively colored endpoint nodes on the existing black route; every segment retains its original black stroke, all gray edges stay gray. Derive21-1=20 units=>400(B), not recoloring the target or a generic path salience change.')
else:raise ValueError(q)
