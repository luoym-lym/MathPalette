from pathlib import Path
import sys
source=Path(__file__).with_name('prepare.py').read_text(encoding='utf-8').split('\nfor qid in sys.argv[1:]')[0]
exec(compile(source,str(Path(__file__).with_name('prepare.py')),'exec'))
R='#DC2626'
for qid,targets,wrong in [('Solid120',['tick0_6','tick1_7','tick2_6'],'50'),('Solid138',['tick0_6','tick1_7','tick2_7','tick3_6'],'72')]:
    check=eligibility(qid)
    if not check['eligible']:raise ValueError('Became ineligible '+qid)
    context=adapter.inspect_question(qid)
    scene=json.loads((TASK/qid/'source_scene_snapshot.json').read_text(encoding='utf-8'))
    objects={o['id']:o for o in scene['objects']}
    endpoints=[];bindings=[];actions=[]
    for target in targets:
        world=objects[target]['points'][0]
        snaps=[p for p in context['snap_points'] if p.get('world_xyz')==world]
        if not snaps:raise ValueError('No exact snap endpoint '+target)
        p=snaps[0];endpoints.append(p['xy']);bindings.append({'target':target,'source_world_endpoint':world,'snap_point_id':p['id'],'exact_context_xy':p['xy']})
        actions.append({'type':'set_object_style','target':target,'color':R,'linewidth_pt':2})
    for i,(a,b) in enumerate(zip(endpoints,endpoints[1:])):
        actions.append({'type':'add_line','id':'false_correspondence_'+str(i),'endpoints':[a,b],'color':R,'linestyle':'dashed'})
    description='Exact-context dashed guides chain tick6 to tick28 to the requested tick, encoding a false22-unit turn. '+('An explicit intermediate blank-turn tick is included so the question position is three turns above6.' if qid=='Solid138' else 'The requested position is two turns above6.')+' Guides are visual correspondence annotations, not measured paths or new conditions. All original tape ticks, labels and boundaries stay unchanged.'
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':description,'intent':'Predeclared wrong '+wrong,'params':{'actions':actions}}
    dst=TASK/qid/'false_tick_chain_v2'
    report=adapter.render_candidate(plugin,dst)
    write(dst/'eligibility_before_design.json',check)
    write(dst/'design.json',{'question_id':qid,'branch':'SolidGeometry','expected_wrong_answer':wrong,'correct_answer':adapter.records[qid]['answer'],'mechanism':description,'meaningful_redesign_from':'false_tick_correspondence: added exact endpoint-to-endpoint relational guides; Solid138 also marks a previously unmarked intermediate blank turn. Prior image/test history retained.','marker_endpoint_bindings':bindings,'mathematical_answer_unchanged':True,'second_review_status':'pending; no independent second review','approval_status':'unreviewed runtime research; no Pass/Collect'})
    print(json.dumps({'question_id':qid,'candidate':str(dst),'preset':wrong,'png_sha256':sha(dst/'candidate.png')}),flush=True)
