from tools05 import *
from itertools import product
obs={o['id']:o['geometry'] for o in json.loads((HERE/'Plane199/context.json').read_text())['objects']}
def extract(prefix):
    squares=[g['points'] for oid,g in obs.items() if oid.startswith(prefix) and oid.endswith('_border')]
    minx=min(p[0] for s in squares for p in s);miny=min(p[1] for s in squares for p in s)
    cells={(round(min(p[0] for p in s)-minx),round(min(p[1] for p in s)-miny)) for s in squares}
    pips={(round((g['point'][0]-minx)*100),round((g['point'][1]-miny)*100)) for oid,g in obs.items() if oid.startswith(prefix) and '_pip' in oid}
    return cells,pips
def placements(shape):
    cells,pips=shape;result=[]
    for rot in range(4):
        def turn(p):
            x,y=p
            for k in range(rot):x,y=-y,x
            return x,y
        vertices=[turn((100*x+dx,100*y+dy)) for x,y in cells for dx,dy in product([0,100],repeat=2)]
        minx=min(x for x,y in vertices);miny=min(y for x,y in vertices);maxx=max(x for x,y in vertices);maxy=max(y for x,y in vertices)
        pips2={(x-minx,y-miny) for x,y in map(turn,pips)}
        centers=[turn((100*x+50,100*y+50)) for x,y in cells]
        cells2={((x-minx-50)//100,(y-miny-50)//100) for x,y in centers}
        for dx in range(3-(maxx-minx)//100):
            for dy in range(3-(maxy-miny)//100):
                result.append({'rotation':rot,'offset':[dx,dy],'cells':{(x+dx,y+dy) for x,y in cells2},'pips':{(x+dx*100,y+dy*100) for x,y in pips2}})
    return result
sources=[extract('source0'),extract('source1')];options=[extract('opt'+str(i)+'_') for i in range(5)];report={}
for i,(boardcells,boardpips) in enumerate(options):
    solutions=[]
    for a in placements(sources[0]):
        for b in placements(sources[1]):
            if a['cells'] & b['cells'] or a['cells']|b['cells']!=boardcells:continue
            if a['pips']|b['pips']==boardpips:
                solutions.append([{k:(sorted(v) if isinstance(v,set) else v) for k,v in p.items()} for p in [a,b]])
    report[chr(65+i)]={'exact_rotational_domino_assemblies':len(solutions),'solutions':solutions}
write(HERE/'Plane199/exact_domino_audit.json',report)
print(json.dumps(report,ensure_ascii=False))
