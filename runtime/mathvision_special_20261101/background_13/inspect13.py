from tools13 import *
for qid in sys.argv[1:]:
    s=AD.scenes[qid];c=json.loads((TASK/qid/'context.json').read_text(encoding='utf-8-sig'))
    print('\nQUESTION',qid)
    print('view',s.get('view'),'vis keys',s.get('visibility',{}).keys())
    print('vis summary',str({k:v for k,v in s.get('visibility',{}).items() if k not in ['edge_visibility','intervals','face_visibility','edge_intervals','occlusion_audit']})[:5000])
    print('ambiguities',s.get('ambiguities'))
    print('labels',s.get('labels'))
    print('objects',json.dumps([{'id':o['id'],'styleable':o.get('styleable'),'g':o.get('geometry'),'paths':[{k:v for k,v in p.items() if k not in ['samples','segments']} for p in o.get('partial_paths',[])]} for o in c['objects'] if o.get('styleable')],ensure_ascii=False))
