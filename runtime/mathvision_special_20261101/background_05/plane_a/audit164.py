from tools05 import *
from itertools import product
m=json.loads((HERE/'Plane164/context.json').read_text());obs={o['id']:o['geometry'] for o in m['objects']}
def symbol(prefix):
    return next(s for s in ['circle','diamond','plus_h'] if prefix+'_'+s in obs).replace('_h','')
def extract(prefix):
    cells={}
    for oid,g in obs.items():
        if oid.startswith(prefix) and oid.endswith('_square'):
            cells[(min(p[0] for p in g['points']),min(p[1] for p in g['points']))]={'symbol':symbol(oid[:-7]),'square_id':oid}
    minx=min(p[0] for p in cells);miny=min(p[1] for p in cells)
    return {(int(p[0]-minx),int(p[1]-miny)):v for p,v in cells.items()}
pieces=[extract('piece'+str(i)+'_') for i in range(2)];boards=[extract('option'+str(i)+'_') for i in range(5)]
def placements(cells,mirrors=False):
    result=[]
    for mirror in range(2 if mirrors else 1):
        for rot in range(4):
            transformed={}
            for (x,y),v in cells.items():
                if mirror:x=-x
                for k in range(rot):x,y=-y,x
                transformed[(x,y)]=v
            minx=min(x for x,y in transformed);miny=min(y for x,y in transformed)
            transformed={(x-minx,y-miny):v for (x,y),v in transformed.items()}
            maxx=max(x for x,y in transformed);maxy=max(y for x,y in transformed)
            for dx in range(4-maxx):
                for dy in range(4-maxy):
                    result.append({'mirror':bool(mirror),'rotation_quarter_turns':rot,'offset':[dx,dy],'cells':{(x+dx,y+dy):v for (x,y),v in transformed.items()}})
    return result
allcells=set(product(range(4),repeat=2));report={'source_pieces':[{str(k):v for k,v in p.items()} for p in pieces],'options':[{str(k):v for k,v in p.items()} for p in boards],'rotation_only':{},'reflection_also_allowed':{}}
for mirrors,key in [(False,'rotation_only'),(True,'reflection_also_allowed')]:
    for i,board in enumerate(boards):
        trials=[]
        for a in placements(pieces[0],mirrors):
            for b in placements(pieces[1],mirrors):
                if set(a['cells']) & set(b['cells']) or set(a['cells'])|set(b['cells'])!=allcells:continue
                mismatches=[]
                for pn,p in enumerate([a,b]):
                    for pos,v in p['cells'].items():
                        if v['symbol']!=board[pos]['symbol']:mismatches.append({'piece':pn,'xy':list(pos),'source':v,'board':board[pos]})
                trials.append({'mismatch_count':len(mismatches),'mismatches':mismatches,'placements':[{**{k:v for k,v in p.items() if k!='cells'},'cells':{str(k):v for k,v in p['cells'].items()}} for p in [a,b]]})
        trials.sort(key=lambda t:t['mismatch_count'])
        report[key][chr(65+i)]={'shape_tilings':len(trials),'exact_symbol_tilings':sum(t['mismatch_count']==0 for t in trials),'best':trials[:2]}
write(HERE/'Plane164/exact_tiling_audit.json',report)
for key in ['rotation_only','reflection_also_allowed']:
 print(key,{k:{'shape_tilings':v['shape_tilings'],'exact':v['exact_symbol_tilings'],'best_mismatch':v['best'][0]['mismatch_count']} for k,v in report[key].items()})
 print(json.dumps({k:v['best'][0] for k,v in report[key].items() if k!='A'},ensure_ascii=False))
