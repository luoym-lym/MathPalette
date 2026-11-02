from tools24 import *
if sys.argv[1]=='objects':
    for q in sys.argv[2:]:
        print('\n',q)
        for o in read(HERE/q/'context.json')['objects']:
            s=json.dumps(o,ensure_ascii=False)
            if q=='Plane225' and any(k in o['id'] for k in ('radius','edge','mirror')):print(s)
            elif q=='Plane226' and 'heart' in o['id']:print(s)
            elif q in ('Plane248','Plane301','Plane242','Plane220'):print(s)
elif sys.argv[1]=='batch':
    rec=[]
    for p in sorted(BASE.glob('batch_*/manifest.json')):
        d=read(p);print(p.parent.name,'keys',list(d));rec.append({'path':str(p),'sha256':file_hash(p)})
        for a in d.get('candidates',d.get('questions',d.get('items',[]))):print(json.dumps(a,ensure_ascii=False)[:900])
    write(HERE/'delivered_reference_study.json',{'read_all_manifests':rec,'principle':'Match actual source information or ordered existing features; whole wrong-option salience is insufficient. Closed marks must not become false cuts or new givens. Preserve exact geometry and disclose two-call/control limitations.'})
elif sys.argv[1]=='225':
    s=read(HERE/'Plane225/source_scene_snapshot.json')
    print(json.dumps(s.get('constraints'),ensure_ascii=False))
    for o in s['objects']:
        if o['type']=='native_artwork_instance':print(json.dumps(o,ensure_ascii=False))
elif sys.argv[1]=='215':
    d=read(HERE/'Plane215/context.json')
    for o in d['objects']:
        if o['id'] in ('o0','o1','o2','o3','o4','o5','o6','o7','o8','o9','o218','o219','o220','o221'):print(json.dumps(o,ensure_ascii=False))
elif sys.argv[1]=='225art':
    for o in read(HERE/'Plane225/context.json')['objects']:
        if o['kind']=='native_artwork_instance' and any(o['id'].startswith(k) for k in ['fold0','fold1','optionA']):print(json.dumps(o,ensure_ascii=False))
elif sys.argv[1]=='oldsmall':
    for q in ['Plane231','Plane301']:
        inv=read(HERE/q/'prior_history_inventory.json')
        for p in inv['prior_design_paths']:
            d=read(ROOT/p);print(q,json.dumps({k:d[k] for k in d if k not in ['marker_roles','overlay_bindings']},ensure_ascii=False))
elif sys.argv[1]=='batchmechanisms':
    for p in sorted(BASE.glob('batch_*/manifest.json')):
        d=read(p)
        for a in d['candidates']:print(p.parent.name,a['question_id'],a['mechanism'])
