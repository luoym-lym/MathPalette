from tools_local import *

if sys.argv[1]=='raw':
    prior=json.loads((TASK/'all_prior_same_question_evidence.json').read_text(encoding='utf-8'))
    for q in sys.argv[2:]:
        for v in prior[q]:
            print('\nVARIANT',v['folder'])
            for p,t in v['texts'].items():
                if p.endswith('_response.json'):
                    d=json.loads(t);print(p);print(d['choices'][0]['message']['content']);print('FINISH',d['choices'][0]['finish_reason'])
elif sys.argv[1]=='models':
    for q in sys.argv[2:]:
        sc=AD.scenes[q];print(q,'keys',list(sc));vis=sc.get('visibility',{});print('visibility_keys',list(vis))
        print(json.dumps({k:v for k,v in vis.items() if k not in ('edge_intervals','occlusion','intervals')},ensure_ascii=False,indent=2)[:45000])
elif sys.argv[1]=='objects':
    q=sys.argv[2];filt=sys.argv[3] if len(sys.argv)>3 else ''
    data=json.loads((TASK/q/'context.json').read_text(encoding='utf-8'))
    for o in data['objects']:
        if filt in o['id']:print(o['id'],o.get('styleable'),json.dumps(o.get('geometry',{}),separators=(',',':')))
elif sys.argv[1]=='source':
    for q in sys.argv[2:]:
        print(q)
        for k in AD.records[q]['runtime_dependencies']:
            if k.endswith('/scene.json'):
                sc=json.loads((ROOT/'SolidGeometry'/k).read_text(encoding='utf-8-sig'))
                print('keys',list(sc))
                print(json.dumps({k:v for k,v in sc.items() if k!='objects'},ensure_ascii=False,indent=2))
