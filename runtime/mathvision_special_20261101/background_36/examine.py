from tools_local import *
for q in ASSIGNED:
    s=AD.scenes[q]
    print(q,'keys',list(s))
    for k,v in s.items():
        if k not in ['objects','points','visibility','labels']:
            txt=json.dumps(v,ensure_ascii=False)
            print(k,txt if len(txt)<6500 else txt[:1000]+'...')
    rec=AD.records[q]
    print('script',rec['script'],'dependencies',rec.get('runtime_dependencies'))
