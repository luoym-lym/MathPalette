from tools26 import *
if sys.argv[1]=='refs':
    for p in sorted(BASE.glob('batch_*/manifest.json')):
        d=read(p);print(p.parent.name)
        for c in d.get('candidates',[]):print(json.dumps({k:v for k,v in c.items() if k in ['question_id','mechanism','correct_answer','expected_wrong_answer','quality_review']},ensure_ascii=False))
elif sys.argv[1]=='scene':
    for q in sys.argv[2:]:
        r=read(HERE/q/'formal_record.json');p=next(ROOT/'PlaneGeometry'/x for x in r['runtime_dependencies'] if '/items/'+q+'/scene.json' in x)
        s=read(p);print(q+' '+str(p))
        for o in s['objects']:
            if len(o.get('points',[]))>16:
                pts=o['points'];xs=[x[0] for x in pts];ys=[x[1] for x in pts]
                o={k:v for k,v in o.items() if k!='points'}|{'bounds':[min(xs),max(xs),min(ys),max(ys)]}
            print(json.dumps(o,ensure_ascii=False))
        print('labels '+json.dumps(s['labels'],ensure_ascii=False))
elif sys.argv[1]=='paths':
    for q in sys.argv[2:]:
        c=read(HERE/q/'context.json');print(q)
        for t in c['canvas']['targets']:
            print(json.dumps({'id':t['id'],'paths':[{'id':p['id'],'sha256':p['sha256'],'closed':p.get('closed'),'samples':p.get('samples')} for p in t['partial_paths']]},ensure_ascii=False))
