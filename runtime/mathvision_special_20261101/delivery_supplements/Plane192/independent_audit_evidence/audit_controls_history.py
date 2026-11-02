from review_bootstrap import *
import json,hashlib,base64
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(name,v): (OWN/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=BASE/'plane_explore/Plane192/original_control'
t=next((d/'tests').iterdir()); b=read(t/'binding.json');req=read(t/'request.json')
png=base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
controls={'binding_path':str(t/'binding.json'),'binding_sha256':sha(t/'binding.json'),
    'png_equals_current_formal_bytes':png==(ROOT/'PlaneGeometry/image/Plane192.png').read_bytes()==(d/'original.png').read_bytes(),
    'request_hash_matches':sha(t/'request.json')==b['request_body_sha256'],
    'exact_formal_question':req['messages'][1]['content'][0]['text']==read(OWN/'evidence_audit.json')['formal_record']['question'],
    'runs':[]}
for i in (1,2):
    p=t/f'run_{i:02d}_response.json';r=read(p);run=read(t/f'run_{i:02d}.json')
    controls['runs'].append({'raw_response_path':str(p),'sha256':sha(p),
        'raw_hash_matches':sha(p)==run['response_sha256'],
        'completed':run['status']=='completed' and run['http_status']==200 and not run['truncated'] and run['finish_reason']=='stop',
        'full_final':r['choices'][0]['message']['content'],'manually_read_final':'A'})
prior=[]
for i in (1,2,3):
    d=BASE/f'plane_explore/Plane192/v{i:02d}'
    prior.append({'variant_id':f'v{i:02d}', 'design':read(d/'design.json'),
        'plugin':read(d/'plugin.json'),'candidate_sha256':sha(d/'candidate.png'),
        'raw_finals':[{'path':str(p),'sha256':sha(p),'full_response':read(p)['choices'][0]['message']['content']} for p in sorted(d.glob('tests/*/run_??_response.json'))]})
reports={name:BASE/'independent_review'/name/'independent_review.json' for name in
    ['Plane192_v03','Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane233_two_U_partial_partition_binding']}
files={str(p.relative_to(ROOT)):sha(p) for p in reports.values()}
files.update({str(p.relative_to(ROOT)):sha(p) for p in (BASE/'plane_explore/Plane192/original_control').rglob('*') if p.is_file()})
classification=read(BASE/'background_07/source_preservation_classification_final.json')
all_question_bindings=[]
for p in BASE.rglob('binding.json'):
    bq=read(p)
    if bq.get('question_id')=='Plane192':
        all_question_bindings.append({'path':str(p),'sha256':sha(p),'image_sha256':bq.get('image_sha256'),
            'created_at':bq.get('created_at'),'preset':bq.get('expected_wrong_answer'),
            'runs':len(list(p.parent.glob('run_??.json')))})
write('controls_and_history_audit.json',{'controls':controls,'prior_materially_different_designs':prior,'prior_report_hashes':files,
    'unit07_classification_path':str(BASE/'background_07/source_preservation_classification_final.json'),
    'unit07_classification_sha256':sha(BASE/'background_07/source_preservation_classification_final.json'),
    'all_runtime_Plane192_bindings':all_question_bindings})
print(json.dumps({'controls':controls,'unit07_classification_keys':list(classification),
    'all_runtime_Plane192_bindings':all_question_bindings},ensure_ascii=False,indent=2))
