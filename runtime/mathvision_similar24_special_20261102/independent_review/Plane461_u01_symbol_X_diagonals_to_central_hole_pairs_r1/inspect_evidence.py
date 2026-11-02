import review_bootstrap as r
import json

def emit(label, value):
    print(label, json.dumps(value, ensure_ascii=False, indent=2))

ctx = r.read(r.CAND/'context.json')
emit('CONTEXT_METADATA', {k:v for k,v in ctx.items() if k not in ('objects','snap_points','canvas')})
emit('ALL_CONTEXT_OBJECTS',ctx['objects'])
for name in ('history_index.json',):
    obj=r.read(r.TASK/name)
    emit(name+'_STRUCTURE', {k:(len(v) if isinstance(v,(list,dict)) else v) for k,v in obj.items()})
    for k,v in obj.items():
        if isinstance(v,dict) and 'Plane461' in v:
            r.save(r.OWN/('history_Plane461_'+k+'.json'),v['Plane461'])
            emit(name+'_'+k+'_Plane461_STRUCTURE', {a:(len(b) if isinstance(b,(list,dict)) else b) for a,b in v['Plane461'].items()} if isinstance(v['Plane461'],dict) else len(v['Plane461']))
for rel in ('audit.json','method_fidelity.json'):
    obj=r.read(r.TASK/'parent_audits/native_u01_u04'/rel)
    if isinstance(obj,dict):
        emit('PARENT_'+rel+'_STRUCTURE',{k:(len(v) if isinstance(v,(list,dict)) else v) for k,v in obj.items()})
        for k,v in obj.items():
            if isinstance(v,list):
                for item in v:
                    if isinstance(item,dict) and item.get('question_id')=='Plane461':
                        emit('PARENT_'+rel+'_'+k,item if len(json.dumps(item))<16000 else {a:b for a,b in item.items() if a not in ('files','source_files','checked_records','raw_final_reviews')})
            if isinstance(v,dict) and 'Plane461' in v: emit('PARENT_'+rel+'_'+k,v['Plane461'])
    else: emit('PARENT_'+rel,obj)
for name in ('request.json',):
    obj=r.read(next((r.CAND/'tests').iterdir())/name)
    if name=='request.json':
        obj={**obj,'messages':[({**m,'content':[{**b,'image_url':{'url':'[BASE64 OMITTED HERE; independently decoded and hashed in integrity script]'}} if b.get('type')=='image_url' else b for b in m['content']] } if isinstance(m.get('content'),list) else m) for m in obj['messages']]}
    emit(name,obj)
for name in ('source_preservation_final.json','readonly_inputs_initial.json','process_shutdown_evidence.json','process_shutdown_verified.json'):
    obj=r.read(r.UNIT/name)
    emit(name+'_STRUCTURE', {k:(len(v) if isinstance(v,(list,dict)) else v) for k,v in obj.items()})
    if 'process' in name: emit(name,obj)
