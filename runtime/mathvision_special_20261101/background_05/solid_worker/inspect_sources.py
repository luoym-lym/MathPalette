from tools_local import *
for qid in sys.argv[1:]:
    record=AD.records[qid]
    p=next(ROOT/'SolidGeometry'/p for p in record['runtime_dependencies'] if p.endswith('/scene.json'))
    source=json.loads(p.read_text(encoding='utf-8-sig'))
    print(qid, 'source_keys',list(source),flush=True)
    for k in ['notes','source_note','ambiguities','metadata','model','shapes','nets','blocks','objects','panels','views','geometry']:
        if k in source:print(k,json.dumps(source[k],ensure_ascii=False)[:30000],flush=True)
