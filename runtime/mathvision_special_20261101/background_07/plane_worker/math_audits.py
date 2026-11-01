from tools_local import *
import math,itertools
def polygon_cells(poly):
    def inside(x,y):
        c=False
        for a,b in zip(poly,poly[1:]+poly[:1]):
            if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:c=not c
        return c
    return {(x,y) for x in range(math.floor(min(p[0] for p in poly)),math.ceil(max(p[0] for p in poly))) for y in range(math.floor(min(p[1] for p in poly)),math.ceil(max(p[1] for p in poly))) if inside(x+.5,y+.5)}
def norm(cells):
    a=min(x for x,y in cells);b=min(y for x,y in cells)
    return frozenset((x-a,y-b) for x,y in cells)
def orientations(cells):
    out=set()
    for flip in [1,-1]:
        for k in range(4):
            s=[]
            for x,y in cells:
                x*=flip
                for _ in range(k):x,y=-y,x
                s.append((x,y))
            out.add(norm(s))
    return out
def grid_cells(meta,prefix):
    edges={tuple(sorted(tuple(p) for p in o['geometry']['points'])) for o in meta['objects'] if o['kind']=='segment' and o['id'].startswith(prefix)}
    # Any drawn unit square has all four edges; absent cells have no internal grid.
    vertices={p for e in edges for p in e};cells=set()
    for x,y in vertices:
        es=[((x,y),(x+1,y)),((x+1,y),(x+1,y+1)),((x,y+1),(x+1,y+1)),((x,y),(x,y+1))]
        if all(tuple(sorted(e)) in edges for e in es):cells.add((x,y))
    return cells
def audit239():
    q='Plane239';m=json.loads((HERE/q/'context.json').read_text());objs=m['objects'];results={}
    for opt,inds in zip('ABCDE',[[9,11,12,13,14,15,16,17],[18,19,20,21,23,24,25,26],[27,28,30,31,32,33,34,35],[36,37,38,39,40,41,42,44],[45,46,47,48,49,50,52,53]]):
        nodes=[]
        for i in inds:
            g=objs[i]['geometry'];p=g['points'];center=[(min(v[0] for v in p)+max(v[0] for v in p))/2,(min(v[1] for v in p)+max(v[1] for v in p))/2]
            nodes.append({'id':objs[i]['id'],'xy':center,'color':g['fill_color']})
        head=next(i for i,n in enumerate(nodes) if n['color']=='#FFFF00');adj={i:[j for j in range(8) if j!=i and abs(math.dist(nodes[i]['xy'],nodes[j]['xy'])-1)<1e-10] for i in range(8)};paths=[]
        def dfs(path):
            if len(path)==8:paths.append([nodes[i]['id'] for i in path]);return
            required='#000000' if len(path)%2 else '#FFFFFF'
            for j in adj[path[-1]]:
                if j not in path and nodes[j]['color']==required:dfs(path+[j])
        dfs([head]);results[opt]={'nodes':nodes,'adjacency':adj,'complete_head_to_tail_alternating_paths':paths,'solution_count':len(paths)}
    assert [k for k,v in results.items() if v['solution_count']]==['A']
    write(HERE/q/'mathematical_audit.json',{'method':'Enumerate all contact-edge Hamiltonian paths starting at the marked head; original body order must alternate black/white, end black. Incidental contacts are allowed, but each consecutive body pair must touch.','results':results,'unique_answer':'A'})
def audit247():
    q='Plane247';m=json.loads((HERE/q/'context.json').read_text());ids=[o['id'] for o in m['objects']];prefixes=sorted({i.split('_')[0] for i in ids});print('247 prefixes',prefixes)
    remaining=grid_cells(m,'remaining_square_');gap={(x,y) for x in range(7) for y in range(7)}-remaining
    shapes={str(i):grid_cells(m,f'piece{i}_') for i in range(1,5)}
    if any(not c for c in shapes.values()):print('247 IDs',ids);return
    placements={}
    for k,cells in shapes.items():
        placements[k]=[]
        for shape in orientations(cells):
            for x in range(7):
                for y in range(7):
                    place={(a+x,b+y) for a,b in shape}
                    if place<=gap and place not in placements[k]:placements[k].append(place)
    results={}
    for a,b in itertools.combinations(shapes,2):
        sols=[{'a':sorted(p),'b':sorted(r)} for p in placements[a] for r in placements[b] if not p&r and p|r==gap]
        results[a+'+'+b]={'area':len(shapes[a])+len(shapes[b]),'solutions':sols,'count':len(sols)}
    write(HERE/q/'mathematical_audit.json',{'remaining_cells':sorted(remaining),'gap_cells':sorted(gap),'shape_cells':{k:sorted(c) for k,c in shapes.items()},'results':results,'unique_answer':'C'})
def audit262():
    q='Plane262';m=json.loads((HERE/q/'context.json').read_text());raw={o['id']:o['geometry'] for o in m['objects']}
    def extract(g):
        g=copy.deepcopy(g)
        origin=g['commands'][0]['point'];fraction=[origin[i]-math.floor(origin[i]) for i in range(2)]
        for command in g['commands']:
            for field in ['point','center']:
                if field in command:command[field]=[command[field][i]-fraction[i] for i in range(2)]
        poly=[];flags={};cur=None
        for c in g['commands']:
            if c['op'] in ['move','line']:cur=tuple(c['point']);poly.append(cur)
            else:
                end=tuple(round(c['center'][i]+c['radius']*[math.cos(math.radians(c['end_deg'])),math.sin(math.radians(c['end_deg']))][i],9) for i in range(2))
                flags[tuple(sorted((tuple(round(v,9) for v in cur),end)))]=1 if c['end_deg']>c['start_deg'] else -1
                cur=end;poly.append(cur)
        return polygon_cells(poly),flags
    extracted={k:extract(v) for k,v in raw.items()};results={}
    def boundary(cells):
        es={}
        for x,y in cells:
            for e in [((x,y),(x+1,y)),((x+1,y),(x+1,y+1)),((x,y+1),(x+1,y+1)),((x,y),(x,y+1))]:
                e=tuple(sorted(e));es[e]=es.get(e,0)+1
        return {e for e,n in es.items() if n==1}
    for option in range(5):
        target,tf=extracted['option'+str(option)];tb=boundary(target);candidates={}
        for p in range(4):
            cells,flags=extracted['given'+str(p)];baseverts=[(x,y) for x,y in cells]+[(x+1,y+1) for x,y in cells]
            poss=[]
            for k in range(4):
                def tr(v):
                    x,y=v
                    for _ in range(k):x,y=-y,x
                    return x,y
                transformedverts=[tr(v) for v in baseverts];ox=min(v[0] for v in transformedverts);oy=min(v[1] for v in transformedverts)
                cs=set()
                for x,y in cells:
                    vv=[tr((x,y)),tr((x+1,y)),tr((x,y+1)),tr((x+1,y+1))];cs.add((min(v[0] for v in vv)-ox,min(v[1] for v in vv)-oy))
                fs={tuple(sorted((tuple(tr(v)[i]-[ox,oy][i] for i in range(2)) for v in e))):sg for e,sg in flags.items()}
                for dx in range(math.floor(min(x for x,y in target)),math.ceil(max(x for x,y in target))+1):
                    for dy in range(math.floor(min(y for x,y in target)),math.ceil(max(y for x,y in target))+1):
                        cc={(x+dx,y+dy) for x,y in cs}
                        if not cc<=target:continue
                        ff={tuple(sorted((tuple(v[i]+[dx,dy][i] for i in range(2)) for v in e))):sg for e,sg in fs.items()}
                        bb=boundary(cc)
                        if any(ff.get(e,0)!=tf.get(e,0) for e in bb&tb):continue
                        poss.append({'cells':cc,'flags':ff,'boundary':bb,'rotation':k*90,'offset':[dx-ox,dy-oy]})
            candidates[p]=poss
        sols=[]
        def dfs(chosen,covered):
            p=len(chosen)
            if p==4:
                if covered==target:sols.append(chosen)
                return
            for c in candidates[p]:
                if c['cells']&covered:continue
                if any(any(c['flags'].get(e,0)+old['flags'].get(e,0)!=0 for e in c['boundary']&old['boundary']) for old in chosen):continue
                dfs(chosen+[c],covered|c['cells'])
        if sum(tf.values())==sum(sum(extracted['given'+str(p)][1].values()) for p in range(4)):dfs([],set())
        results[chr(65+option)]={'base_cells':sorted(target),'convex_minus_concave':sum(tf.values()),'placements_per_piece':{str(p):len(v) for p,v in candidates.items()},'solution_count':len(sols),'witness':[{'piece':p,'rotation':c['rotation'],'offset':c['offset'],'cells':sorted(c['cells'])} for p,c in enumerate(sols[0])] if sols else None}
    assert all(results[k]['solution_count'] for k in 'ABCD') and not results['E']['solution_count'],results
    write(HERE/q/'mathematical_audit.json',{'method':'Exact grid rectangle-base tiling with signed unit-diameter semicircle edge flags. Internal shared edge flags must sum to zero; exterior flags must equal target. Four rotations; no reflections needed. All four pieces used without overlap.','input_shapes':{k:{'base_cells':sorted(c),'signed_semicircle_edges':[{'edge':e,'sign':v} for e,v in f.items()]} for k,(c,f) in extracted.items() if k.startswith('given')},'results':results,'unique_answer':'E','area_proof':'Four source rectangle bases have total area6 and +3/-3 semicircles cancel. E has base area6 and +3/-1 semicircles: area6+pi/4, impossible.'})
if __name__=='__main__':
    for arg in sys.argv[1:]:globals()['audit'+arg]()
