from bootstrap import *
from math_tools import prove
c=read(OWN/'current_context.json');board,proof=prove(c)
def edges(cs):
    out=set()
    for x,y in cs:
        for n,a,b in [((x-1,y),(x,y),(x,y+1)),((x+1,y),(x+1,y),(x+1,y+1)),((x,y-1),(x,y),(x+1,y)),((x,y+1),(x,y+1),(x+1,y+1))]:
            if n not in cs:out.add(tuple(sorted((a,b))))
    return out
def canonical(es):
    forms=[]
    for flip in (-1,1):
        points=[(flip*x,y) for e in es for x,y in e]
        for _ in range(4):
            x0=min(x for x,y in points);y0=min(y for x,y in points)
            normalized=[(x-x0,y-y0) for x,y in points]
            forms.append(tuple(sorted(tuple(sorted(normalized[i:i+2])) for i in range(0,len(normalized),2))))
            points=[(-y,x) for x,y in points]
    return min(forms)
def components(es):
    left=set(es);out=[]
    while left:
        one={left.pop()};vertices={p for e in one for p in e}
        while True:
            add={e for e in left if set(e)&vertices}
            if not add:break
            one|=add;left-=add;vertices|={p for e in add for p in e}
        out.append(sorted(one))
    return sorted(out,key=lambda es:(-len(es),es))
be=edges(board);assert len(be)==16
results={}
for k in 'BCDE':
    classes={};allplacements=[]
    for p in proof[k]['all_valid_placements']:
        cs=set(map(tuple,p));shared=edges(cs)&be
        if not shared:continue
        key=repr(canonical(shared));cc=components(shared)
        entry={'cells':p,'shared_exterior_edges':sorted(shared),'shared_edge_count':len(shared),'component_edge_counts':[len(x) for x in cc],'components':cc}
        classes.setdefault(key,[]).append(entry);allplacements.append(entry)
    maximal=max(x['shared_edge_count'] for x in allplacements)
    results[k]={'valid_placements':len(proof[k]['all_valid_placements']),'maximum_shared_exterior_edges':maximal,'distinct_shared_profile_classes':len(classes),'all_placements':allplacements,'profiles_at_maximum_or_at_least4_edges':[{'canonical_edges':key,'count':len(v),'representatives':v} for key,v in classes.items() if len(v[0]['shared_exterior_edges'])>=4]}
save('all_local_exterior_correspondence_profiles.json',{'at_utc':now(),'question_id':'Plane213','method':'Exhaust all edge-derived D4 whole-cell placements of B/C/D/E and intersect their real boundary edges with the whole board true exterior. Group common-edge subsets up to D4+translation. This classifies this specific family of true correspondences; it does NOT prove no possible Special exists.','board_coordinate_offset':[11,7],'results':results,'new_API_calls':0})
print(json.dumps({k:{'maximum_shared_exterior_edges':v['maximum_shared_exterior_edges'],'profile_classes':v['distinct_shared_profile_classes'],'profiles_at_least4':[{'count':x['count'],'edge_count':len(x['representatives'][0]['shared_exterior_edges']),'component_edge_counts':x['representatives'][0]['component_edge_counts'],'sample_cells':x['representatives'][0]['cells'],'sample_edges':x['representatives'][0]['shared_exterior_edges']} for x in v['profiles_at_maximum_or_at_least4_edges']]} for k,v in results.items()},ensure_ascii=False,indent=2))
