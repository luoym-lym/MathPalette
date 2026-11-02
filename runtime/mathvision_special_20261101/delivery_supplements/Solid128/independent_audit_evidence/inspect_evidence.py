from audit_bootstrap import *
import copy
import base64

mode = sys.argv[1]
if mode == 'history':
    value = read(BASE / 'background_35/history_read_audit.json')
    print('History top-level keys:', list(value))
    def relevant(value, path=''):
        if isinstance(value, dict):
            if value.get('question_id', value.get('id')) == 'Solid128':
                print(path, json.dumps(value, ensure_ascii=False, indent=2)); return
            for k,v in value.items():
                if 'Solid128' in str(k):
                    print(path+'/'+k, json.dumps(v, ensure_ascii=False, indent=2))
                elif isinstance(v, (dict,list)):
                    relevant(v, path+'/'+k)
                elif isinstance(v,str) and ('Solid128' in v or ('old_' in k and 'Solid156' not in v)):
                    print(path+'/'+k, v)
        elif isinstance(value,list):
            for i,v in enumerate(value):
                relevant(v, path+'/'+str(i))
    relevant(value)
    for p in sorted((BASE/'background_15/Solid128').glob('*.json')):
        if any(s in p.name for s in ['context','frozen_inputs','scene_snapshot']):
            print(p.name, 'keys', list(read(p)), 'sha256',sha(p))
        else:
            print(str(p.relative_to(ROOT)),json.dumps(read(p),ensure_ascii=False,indent=2))
    print('Old candidate/plugin/test files:',[str(p.relative_to(ROOT)) for p in (BASE/'background_15/Solid128').rglob('*') if p.is_file() and ('plugin' in p.name or p.name.startswith('run_') or p.name == 'candidate.png')])
elif mode == 'request':
    p = TEST/'request.json'
    req = read(p)
    exposed = copy.deepcopy(req)
    for msg in exposed['messages']:
        if isinstance(msg['content'],list):
            for item in msg['content']:
                if item.get('type') == 'image_url':
                    url=item['image_url']['url']
                    image_bytes=base64.b64decode(url.split(',',1)[1],validate=True)
                    item['image_url']['url']={'prefix':url.split(',',1)[0], 'decoded_bytes':len(image_bytes),'decoded_sha256':hashlib.sha256(image_bytes).hexdigest(),'exact_candidate_bytes_equal':image_bytes==(CANDIDATE/'candidate.png').read_bytes()}
    print(json.dumps(exposed,ensure_ascii=False,indent=2))
    print('Raw request bytes SHA256',sha(p))
    for name in ['run_01_started.json','run_02_started.json','summary.json']:
        print(name,json.dumps(read(TEST/name),ensure_ascii=False,indent=2))
elif mode == 'metadata':
    p=QUESTION/'material_refinement_assessment.json'
    print(str(p.relative_to(ROOT)),json.dumps(read(p),ensure_ascii=False,indent=2))
    def specific(v,path=''):
        if isinstance(v,dict):
            if v.get('question_id',v.get('id'))=='Solid128':
                print(path,json.dumps(v,ensure_ascii=False,indent=2)); return
            for k,x in v.items():
                if isinstance(x,(dict,list)): specific(x,path+'/'+k)
                elif 'Solid128' in str(x) or 'unchanged' in k or 'concurrent' in k or 'classification' in k:
                    print(path+'/'+k,x)
        elif isinstance(v,list):
            for i,x in enumerate(v):
                if isinstance(x,(dict,list)): specific(x,path+'/'+str(i))
    for p in [BASE/'background_15/checkpoint.json',BASE/'background_35/source_preservation_classification_final.json']:
        v=read(p)
        print(str(p.relative_to(ROOT)),'keys',list(v)); specific(v)
