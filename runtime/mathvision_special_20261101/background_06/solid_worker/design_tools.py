from tools_local import *
import numpy as np
from partial_style import object_paths
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
def source_objects(q):return json.loads((TASK/q/'context.json').read_text(encoding='utf-8'))['objects']
def match_edge(q,prefix,ends):
    ends=np.array(ends,float)
    matches=[o for o in source_objects(q) if o['id'].startswith(prefix) and o.get('styleable') and o['geometry']['type']=='segment' and (np.allclose(o['geometry']['points'],ends,atol=1e-9,rtol=0) or np.allclose(o['geometry']['points'],ends[::-1],atol=1e-9,rtol=0))]
    assert len(matches)==1,{'prefix':prefix,'ends':ends.tolist(),'matches':[o['id'] for o in matches]}
    return matches[0]['id']
def path_bindings(q,targets):
    scene=AD.scene(q)
    try:
        scene.fig.canvas.draw();out={}
        for target in targets:
            out[target]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,target)]
        return out
    finally:scene.close()
def style(target,color,width=2,interval=None):
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
    if interval:a['interval']=interval
    return a
def interval(q,target,start,end):
    p=path_bindings(q,[target])[target][0]
    return {'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
def save_candidate(q,vid,expected,actions,roles,mechanism,math,math_path):
    check=eligibility(q);assert check['eligible'],check
    folder=TASK/q/vid
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism[:999],'intent':mechanism[:999],'params':{'actions':actions}}
    report=AD.render_candidate(plugin,folder)
    assert len(roles)==len(actions)
    targets=sorted({a['target'] for a in actions if a['type']=='set_object_style'})
    paths=path_bindings(q,targets)
    write(folder/'marker_path_bindings.json',paths)
    objs={o['id']:o for o in source_objects(q)}
    write(folder/'design.json',{'question_id':q,'variant_id':vid,'expected_wrong_answer':expected,'formal_correct_answer':AD.records[q]['answer'],'created_at':datetime.now(timezone.utc).isoformat(),'mechanism':mechanism,'marker_roles':[{'action_index':i,'action':a,'role':role,'original_object':objs[a['target']] if a['type']=='set_object_style' else None} for i,(a,role) in enumerate(zip(actions,roles))],'primary_math':math,'math_audit_path':str(math_path),'marker_path_bindings_sha256':file_hash(folder/'marker_path_bindings.json'),'context_sha256':file_hash(folder/'context.json'),'candidate_png_sha256':file_hash(folder/'candidate.png'),'limits':['No original control unless later saved separately.','Primary review only; parent must commission a NEW independent review before delivery.','No claim about human performance or per-marker statistical causal necessity. Appearance marks do not add mathematical givens.']})
    write(folder/'eligibility_before_design.json',check)
    return folder
