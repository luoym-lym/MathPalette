from bootstrap import install,OWN,PROJECT,SESSION
install()
from research import load,save,sha
import json

semantic=[]
for p in sorted((OWN/'reference_read').glob('*.json')):
    d=load(p)['full_report']
    wanted={k:v for k,v in d.items() if any(x in k for x in ['reason','semantics','objection','visual_inspection','proof_correction','limitation','requirement_disposition'])}
    semantic.append({'source':load(p)['source'],'sha256':load(p)['sha256'],'all_report_keys':list(d),'semantic_findings':wanted})
save(OWN/'reference_semantics_read.json',semantic)
for v in semantic: print(json.dumps(v,ensure_ascii=False,separators=(',',':')))

refs=[]
for i in range(1,15):
    folder=SESSION/f'batch_{i:02}'
    designs=[]
    for p in folder.rglob('design.json'):
        if 'original_control' in str(p):continue
        d=load(p)
        narrative={k:v for k,v in d.items() if any(x in k for x in ['description','hypothesis','reason','mechanism','intent','marker_roles','name','variant_id','design_id','question_id'])}
        designs.append({'path':str(p),'sha256':sha(p),'narrative':narrative})
    refs.append({'batch':i,'designs':designs})
save(OWN/'delivered_reference_study.json',refs)
for ref in refs:print(json.dumps(ref,ensure_ascii=False,separators=(',',':')))
