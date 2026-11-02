from tools_local import *

def collect():
    records={q:[] for q in ASSIGNED}
    for p in TASK.parent.rglob('design.json'):
        if p.is_relative_to(TASK):continue
        d=json.loads(p.read_text(encoding='utf-8-sig'))
        q=d.get('question_id')
        if q not in records:continue
        folder=p.parent
        files=[f for f in folder.rglob('*') if f.is_file()]
        records[q].append({'folder':str(folder.relative_to(ROOT)),'design':d,
            'files':{str(f.relative_to(ROOT)):file_hash(f) for f in files},
            'texts':{str(f.relative_to(ROOT)):f.read_text(encoding='utf-8-sig') for f in files if f.suffix in ('.json','.txt','.md') and f.name not in ('context.json','request.json','source_scene_snapshot.json')},
            'request_paths':[str(f.relative_to(ROOT)) for f in files if f.name=='request.json']})
    write(TASK/'all_prior_same_question_evidence.json',records)
    for q,v in records.items():
        print(q)
        for x in v:print(x['folder'],x['design'].get('expected_wrong_answer',x['design'].get('predicted_wrong_answer')),len(x['files']))
    write(TASK/'source_preservation_baseline.json',{
        'formal_and_helpers':{str(p.relative_to(ROOT)):file_hash(p) for p in [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',ROOT/'provenance/approvals.json',ROOT/'SolidGeometry/dataset.jsonl',ROOT/'SolidGeometry/workbench/plugin.schema.json',TASK.parent/'harness/quicktest3_isolated.py',TASK.parent/'runtime_isolation.py']},
        'prior_evidence':{p:h for v in records.values() for x in v for p,h in x['files'].items()},
        'per_question_frozen_inputs':{q:AD.frozen_inputs(q) for q in ASSIGNED},
        'mutable_progress_diagnostic':{str(p.relative_to(ROOT)):file_hash(p) for p in [TASK.parent/'remaining_questions.jsonl',TASK.parent/'exploration_report.json']},
        'current_authoritative_eligibility':{q:eligibility(q) for q in ASSIGNED},
        'workbench_state_diagnostic':{str(p.relative_to(ROOT)):file_hash(p) for p in [ROOT/'.runtime/solid_special/state.json',ROOT/'.runtime/plane_special/state.json'] if p.exists()}})

def read(q):
    all=json.loads((TASK/'all_prior_same_question_evidence.json').read_text(encoding='utf-8'))
    for x in all[q]:
        print('\nFOLDER',x['folder']);print('DESIGN',json.dumps(x['design'],ensure_ascii=False,indent=2))
        for p,t in x['texts'].items():
            if p.endswith(('design.json','design_snapshot.json','render_check.json','binding.json','summary.json')):continue
            if p.endswith('_response.json'):
                raw=json.loads(t)
                print('\nFULL RAW RESPONSE',p,json.dumps(raw,ensure_ascii=False,indent=2))
            elif any(s in Path(p).name for s in ('primary','review','math','final','audit')):
                d=json.loads(t) if p.endswith('.json') else t
                if isinstance(d,dict):
                    for repeated in ('roles','marker_roles','math_evidence'):
                        if repeated in d:
                            print('Repeated field',repeated,'read from design:',d[repeated]==x['design'].get(repeated,d[repeated]))
                            d.pop(repeated)
                print('\nEVIDENCE',p,json.dumps(d,ensure_ascii=False,separators=(',',':')) if isinstance(d,dict) else d)
        print('\nEXACT REQUEST AUDIT')
        for p in x['request_paths']:
            req=json.loads((ROOT/p).read_text(encoding='utf-8'))
            img=req['messages'][1]['content'][1]['image_url']['url']
            import base64
            print(json.dumps({'path':p,'sha256':file_hash(ROOT/p),'settings':{k:v for k,v in req.items() if k!='messages'},'system':req['messages'][0],'question_text':req['messages'][1]['content'][0],'image_bytes_sha256':hashlib.sha256(base64.b64decode(img.split(',',1)[1])).hexdigest(),'top_keys':list(req),'user_content_only_question_and_image':len(req['messages'][1]['content'])==2},ensure_ascii=False))

if __name__=='__main__':
    if len(sys.argv)==1:collect()
    else:read(sys.argv[1])
