from tools08 import *
for q in sys.argv[1:]:
    m=json.loads((HERE/q/'context.json').read_text(encoding='utf-8'))
    print(q,'canvas', {k:m['canvas'][k] for k in ['xlim','ylim']})
    for o in m['objects']:
        g=o.get('geometry',{});pts=g.get('points',[])
        print(json.dumps({'id':o['id'],'type':o['type'],'kind':o.get('kind'),'source_call':o.get('source_call'),'geometry':g if len(str(g))<550 else {'point_count':len(pts),'first':pts[:2],'last':pts[-2:]}},ensure_ascii=False))
    print('targets',[(t['id'],[(p['id'],p['sha256'],p.get('closed')) for p in t.get('partial_paths',[])]) for t in m['canvas'].get('targets',[])])
