from tools10 import *
R='#DC2626';B='#2563EB';G='#16A34A';O='#EA580C'
def make(qid,vid,preset,actions,hypothesis,proof,roles):
    out=HERE/qid/vid;assert eligibility(qid)['eligible'];cfg,ad=adapter();before=inputs(ad,qid);ctx=ad.inspect_question(qid)
    write(out/'fresh_context.json',ctx);write(out/'eligibility_design.json',eligibility(qid));write(out/'source_inputs.json',before)
    p={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:ctx});normalized,data,digest=pr.render(p);n2,data2,digest2=pr.render(normalized,frozen=True)
    assert normalized==n2 and data==data2 and digest==digest2 and before==inputs(ad,qid)
    (out/'candidate.png').write_bytes(data);(out/'repeat.png').write_bytes(data2);write(out/'plugin.json',normalized)
    targets={x['id']:x for x in ctx['canvas']['targets']}
    actionbindings=[]
    for i,a in enumerate(normalized['params']['actions']):
        actionbindings.append({'action_index':i,'action':a,'role':roles[i],'original_target':targets.get(a.get('target'))})
    design={'question_id':qid,'candidate_id':qid+'/'+vid,'created_at':now(),'expected_wrong_answer':preset,'correct_answer':ad.records[qid]['answer'],'hypothesis':hypothesis,'primary_math_proof':proof,'per_marker_roles':roles,'mathematics_and_count_targets_preserved':True,'pretest_immutable':True,'source_inputs_sha256':file_hash(out/'source_inputs.json'),'plugin_sha256':file_hash(out/'plugin.json'),'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':digest,'baseline_pixel_equality':True,'twice_byte_identical':True,'approval_status':'unreviewed; parent must launch NEW independent second review'}
    write(out/'design.json',design);write(out/'marker_bindings.json',actionbindings)
    print(json.dumps({'candidate':design['candidate_id'],'preset':preset,'actions':len(actions),'image_sha256':design['image_sha256']}),flush=True)
if __name__=='__main__':
    q='Plane159';ctx=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'));targets={x['id']:x for x in ctx['canvas']['targets']};acts=[];roles=[]
    classes=['black','white','grey','white','grey','black','white','black','grey'];colors={'black':R,'white':B,'grey':G}
    for prefix in ['source','B']:
        for i,c in enumerate(classes):
            oid=prefix+str(i);p=targets[oid]['partial_paths'][0]
            acts.append({'type':'set_object_style','target':oid,'color':colors[c],'linewidth_pt':3,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':0.5,'end':0.75,'wrap':False}})
            roles.append(f'{oid} top edge identifies position {i+1} of the {c} origin class; same-color source/B pair encourages simultaneous one-step replacement rather than sequential replacement.')
    make(q,'simultaneous_class_binding','B',acts,'Top-edge class correspondence pairs each original cell with its simultaneous-replacement image in B; predicted error ignores that newly white cells also become grey in the final step.','Let initial classes be b,w,g. Step1 maps b->w; step2 g->b; step3 all current w->g. Thus original b,w both end g and original g ends b. Sequence g,g,b,g,b,g,g,g,b matches A alone. Borders do not change the original white/grey/black fills or add cells.',roles)
    q='Plane373';acts=[];roles=[]
    for origin,target,c,meaning in [('o4','o23',R,'white/black upper-right boundary'),('o5','o24',B,'white/grey upper-left boundary'),('o6','o25',G,'grey/black downward boundary')]:
        for oid in [origin,target]:
            acts.append({'type':'set_object_style','target':oid,'color':c,'linewidth_pt':3});roles.append(f'{oid} binds the {meaning} between source and B, encouraging preservation of initial orientation after discarding half a revolution.')
    make(q,'initial_spoke_orientation_binding','B',acts,'Three radial boundary color pairs match the original orientation to B; predicted error drops the last half revolution after five whole turns.','Circumference is 2pi; travel11pi yields clockwise rotation11pi=5.5 turns, equivalent to 180 degrees. Initial white top rotates to bottom; grey lower-left rotates upper-right; black lower-right rotates upper-left. E alone has this orientation and chirality. Only existing radial boundaries change stroke; sectors, arrow, distance, labels and circle geometry are untouched.',roles)
    q='Plane385';m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'));pts={p['id']:p['xy'] for p in m['snap_points']};acts=[];roles=[];seen=set()
    for label,ids in [('upper_left',['P01','P11','P12','P02']),('upper_right',['P11','P21','P22','P12']),('lower_right',['P10','P20','P21','P11'])]:
        for j in range(4):
            a,b=ids[j],ids[(j+1)%4];key=tuple(sorted([a,b]))
            if key in seen:continue
            seen.add(key);acts.append({'type':'add_line','id':'squareedge'+str(len(acts)),'endpoints':[pts[a],pts[b]],'color':R,'linestyle':'solid'})
            roles.append(f'Connects existing dots {a} and {b}, an edge of the valid axis-aligned {label} unit square. The connected lattice alignment encourages counting only the three axis-aligned squares, overlooking the diagonal one; no new dots or conditions.')
    make(q,'axis_aligned_square_subset','3',acts,'Draw the existing three axis-aligned unit squares as one connected edge family; predicted error misses the fourth tilted square.','The eight points are the 3x3 lattice minus(0,0). Axis-aligned squares: three unit squares; the side2 square is impossible since(0,0) is absent. Tilted squares in this 2x2 extent can only have side vector(1,1) or(1,-1); their common diamond has vertices(0,1),(1,0),(2,1),(1,2). Thus exactly4. Added lines join original dots, introduce no dots and do not restrict the requested total of squares that can be drawn.',roles)
