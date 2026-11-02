from bootstrap46 import *
seen={}
def dedup(v, path):
    if isinstance(v,(dict,list)) or isinstance(v,str) and len(v)>80:
        key=json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
        if key in seen: return {'EXACT_DUPLICATE_OF':seen[key]}
        seen[key]=path
    if isinstance(v,dict): return {k:dedup(x,path+'/'+k) for k,x in v.items()}
    if isinstance(v,list): return [dedup(x,path+'/'+str(i)) for i,x in enumerate(v)]
    return v
for name in ['background_46_assignment.json','closure38_40_parent_preparation.json','background_40/checkpoint.json','background_40/draft_handoff.json']:
    source=TASK/name
    result={'source':str(source),'sha256':sha(source),'complete_lossless_deduplicated_content':dedup(read(source),name)}
    save(OWN/'reading'/ (source.name+'.dedup.json'),result)
    print(source.name, (OWN/'reading'/(source.name+'.dedup.json')).stat().st_size)
