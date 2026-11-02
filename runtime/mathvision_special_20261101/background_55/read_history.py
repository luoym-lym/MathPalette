from tools55 import *
import base64

inventory=read(HERE/'old_evidence_inventory.json')
out=[]; bindings=[]
for qid, files in inventory.items():
    for f in files:
        p=PROJECT/f['path']
        if p.suffix!='.json': continue
        data=read(p)
        if p.name=='request.json':
            msg=data['messages'][1]['content']
            raw=base64.b64decode(msg[1]['image_url']['url'].split(',',1)[1])
            bindings.append(dict(path=f['path'],sha256=f['sha256'],image_sha256=hashlib.sha256(raw).hexdigest(),model=data['model'],thinking=data.get('thinking'),system=data['messages'][0]['content'],question=msg[0]['text'],request_keys=list(data)))
        elif p.name.endswith('_response.json'):
            out.append(dict(qid=qid,path=f['path'],kind='full_raw_response_decoded',value=data))
        elif p.name in ['design.json','plugin.json','primary_visual_review.json','manual_final_review.json','prescreen.json','primary_prescreen.json','assessment.json']:
            out.append(dict(qid=qid,path=f['path'],kind='full_design_or_primary_review',value=data))
save=__import__('preflight').save
save(HERE/'old_history_readable.json',out)
save(HERE/'old_request_binding_audit.json',bindings)
print('FILES',len(out),'BINDINGS',len(bindings))
for entry in out:
    if entry['kind']=='full_raw_response_decoded':
        print('\nRAW',entry['path']); print(json.dumps(entry['value'],ensure_ascii=False))
    elif entry['value'].get('question_id') in ['Solid208','Solid210','Solid96']:
        print('\nDOCUMENT',entry['path']);print(json.dumps(entry['value'],ensure_ascii=False))
