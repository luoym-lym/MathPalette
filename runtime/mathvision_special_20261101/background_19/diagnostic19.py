from tools19 import *
for qid in sys.argv[1:]:
    print(qid)
    m=read(HERE/qid/'context.json')
    for o in m['objects']:
        g=o.get('geometry',{});p=g.get('points',[])
        if qid=='Plane372' and not (g.get('locus') or g['type']=='polygon' and len(p)==8):continue
        d={'id':o['id'],'type':g.get('type')}
        if p:d.update(n=len(p),first=p[0],last=p[-1],bbox=[min(x[0] for x in p),max(x[0] for x in p),min(x[1] for x in p),max(x[1] for x in p)])
        for k in ('center','radius','start_deg','end_deg'): 
            if k in g:d[k]=g[k]
        print(json.dumps(d),flush=True)
