from pathlib import Path
import sys
source=Path(__file__).with_name('prepare.py').read_text(encoding='utf-8').split('\nfor qid in sys.argv[1:]')[0]
exec(compile(source,str(Path(__file__).with_name('prepare.py')),'exec'))
for qid in sys.argv[1:]:
    targets=['tick0_6','tick1_7','tick2_6'] if qid=='Solid120' else ['tick0_6','tick1_7','tick2_7','tick3_6']
    wrong='50' if qid=='Solid120' else '72'
    check=eligibility(qid)
    if not check['eligible']:raise ValueError('Became ineligible '+qid)
    context=adapter.inspect_question(qid);scene=json.loads((TASK/qid/'source_scene_snapshot.json').read_text(encoding='utf-8'));objects={o['id']:o for o in scene['objects']}
    endpoints=[];bindings=[];actions=[]
    for i,target in enumerate(targets):
        world=objects[target]['points'][1]
        snaps=[p for p in context['snap_points'] if p.get('world_xyz')==world]
        if not snaps:raise ValueError('No exact lower snap '+target)
        p=snaps[0];endpoints.append(p['xy']);bindings.append({'target':target,'source_world_endpoint':world,'snap_point_id':p['id'],'exact_context_xy':p['xy']})
        actions.append({'type':'add_point','id':'tick_node_'+str(i),'xy':p['xy'],'color':'#DC2626'})
    for i,(a,b) in enumerate(zip(endpoints,endpoints[1:])):actions.append({'type':'add_line','id':'tick_correspondence_'+str(i),'endpoints':[a,b],'color':'#DC2626','linestyle':'dashed'})
    description='Discrete filled nodes at exact existing tick lower tips and dashed node-to-node guides encode false6-to28 one-revolution correspondence and continuation to the question. '+('A blank intermediate turn has its own node, making three additions of22 from6.' if qid=='Solid138' else 'Two additions of22 from6 suggest50.')+' Original ticks remain black: each point identifies one specific tick and each guide specifies a proposed relation; no redundant original-edge recoloring.'
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':description,'intent':'Predeclared wrong '+wrong,'params':{'actions':actions}}
    dst=TASK/qid/'false_tick_nodes_v3';adapter.render_candidate(plugin,dst)
    write(dst/'eligibility_before_design.json',check)
    write(dst/'design.json',{'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':description,'meaningful_redesign_from':'v2 red tick styles replaced with filled discrete endpoint nodes; guides moved to lower tips to bind the nodes without duplicate highlighting. The full v1/v2 evidence remains immutable.','marker_endpoint_bindings':bindings,'second_review_status':'pending; no independent second review','approval_status':'unreviewed runtime research only; no Pass/Collect'})
    print(json.dumps({'question_id':qid,'png_sha256':sha(dst/'candidate.png'),'preset':wrong}),flush=True)
