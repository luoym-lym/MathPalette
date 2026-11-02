from tools_local import *
for q in ASSIGNED:
    dep=next(p for p in AD.records[q]['runtime_dependencies'] if p.endswith('/scene.json'))
    s=json.loads((AD.branch/dep).read_text(encoding='utf-8-sig'))
    extra={k:v for k,v in s.items() if k not in AD.scenes[q]}
    write(TASK/q/'native_model.json',extra)
    print(q,json.dumps(extra,ensure_ascii=False))
