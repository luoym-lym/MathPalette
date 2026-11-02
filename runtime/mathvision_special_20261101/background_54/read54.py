from env54 import *
import sys

hist=read(OWN/'old_history_manifest.json')
mode=sys.argv[1]
if mode=='old':
    for q,entries in hist.items():
        print('\nQUESTION',q)
        for e in entries:
            p=PROJECT/e['path']
            if p.suffix.lower()!='.json' or p.name in ('request.json','context.json','input_fingerprints.json','formal_record.json','frozen_inputs.json','source_scene_snapshot.json'):continue
            data=read(p)
            if p.name.endswith('_response.json'):
                print('\nRAW RESPONSE',e['path']);print(data['choices'][0]['message'].get('content',''))
            elif p.name in ('design.json','primary_review.json','mathematical_audit.json','manual_finals.json','assessment.json','prescreen.json','prescreen_assessment.json','history_audit.json','exact_math.json'):
                print('\nRECORD',e['path'])
                if isinstance(data,dict):
                    data={k:v for k,v in data.items() if k not in ('current_eligibility','eligibility_recheck','authoritative_state_hashes','source_hashes','context','input_fingerprints') and 'hash' not in k}
                print(json.dumps(data,ensure_ascii=False,indent=2))
elif mode=='native':
    for q in sys.argv[2:]:
        rec=read(OWN/q/'formal_record.json');ctx=read(OWN/q/'context.json')
        print('\nQUESTION',q,rec['question'])
        print('OBJECTS',json.dumps(ctx['objects'],ensure_ascii=False))
        p=PROJECT/'PlaneGeometry'/rec['scene'];data=read(p)
        print('FROZEN SCENE',json.dumps(data,ensure_ascii=False))
elif mode=='old_fields':
    for q,entries in hist.items():
        print(q)
        for e in entries:
            p=PROJECT/e['path']
            if p.name in ('prescreen_assessment.json','assessment.json','prescreen.json'):
                d=read(p)
                print(e['path'],json.dumps({k:d[k] for k in d if any(s in k for s in ('reason','note','context','proof','decision','status')) and not isinstance(d[k],dict)},ensure_ascii=False))
