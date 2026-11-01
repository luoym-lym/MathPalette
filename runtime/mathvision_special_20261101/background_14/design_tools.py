from tools import *
import numpy as np
def segment_group(qid,start,end,color,role,width=3):
    a=np.array(start,dtype=float);b=np.array(end,dtype=float);d=b-a;actions=[];markers=[]
    for o in read(TASK/qid/'context.json')['objects']:
        if not o.get('styleable'):continue
        p=np.array(o.get('geometry',{}).get('points',[]),dtype=float)
        if p.shape!=(2,3):continue
        t=(p-a)@d/(d@d)
        if min(t)>=-1e-9 and max(t)<=1+1e-9 and np.max(np.abs(p-a-t[:,None]*d))<1e-8:
            action={'type':'set_object_style','target':o['id'],'color':color,'linewidth_pt':width}
            actions.append(action);markers.append({'action':action,'role':role,'original_world_endpoints':p.tolist(),'source_object_id':o['id'],'partial_paths':o.get('partial_paths',[])})
    if not actions:raise ValueError((qid,start,end,'No existing exact edges'))
    return actions,markers
def named(qid,ids,color,role,width=3):
    out=([],[]);ctx=read(TASK/qid/'context.json')
    for oid in ids:
        o=next(o for o in ctx['objects'] if o['id']==oid);assert o['styleable']
        a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':width}
        out[0].append(a);out[1].append({'action':a,'role':role,'original_world_endpoints':o['geometry'].get('points'),'partial_paths':o.get('partial_paths',[])})
    return out
def save(qid,vid,preset,groups,intent,proof,visual_risks):
    check=eligibility(qid);assert check['eligible'],check
    actions=[a for aa,mm in groups for a in aa];markers=[m for aa,mm in groups for m in mm]
    assert len({a.get('target',a.get('id')) for a in actions})==len(actions),'duplicate style target/id'
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':intent[:1000],'intent':intent[:1000],'params':{'actions':actions}}
    folder=TASK/qid/vid
    report=AD.render_candidate(plugin,folder)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':preset,'correct_answer':AD.records[qid]['answer'],'created_at':datetime.now(timezone.utc).isoformat(),'intent':intent,'pretest_math_proof':proof,'pretest_marker_roles':markers,'pretest_human_semantics':visual_risks,'frozen_png_sha256':report['png_sha256'],'frozen_pixel_sha256':report['pixel_sha256'],'formal_context':str(TASK/qid/'context.json'),'approval_status':'Primary exploration only; NEW independent second review required.'})
    print(json.dumps({'question_id':qid,'variant_id':vid,'preset':preset,'actions':len(actions),'png_sha256':report['png_sha256']}),flush=True)
    return folder
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
