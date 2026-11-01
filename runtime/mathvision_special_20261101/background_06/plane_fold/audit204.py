from tools06 import *
import math
qid='Plane204';check=eligibility(qid);assert check['eligible'];write(HERE/qid/'eligibility_before_math_prescreen.json',check)
m=json.loads((HERE/qid/'context.json').read_text(encoding='utf-8'))
objects={o['id']:o['geometry']['points'] for o in m['objects']}
def key(points):return tuple(sorted((round(x,7),round(y,7)) for x,y in points))
target={key(objects[f'target{i}']):i for i in range(18)}
centers=[tuple(sum(p[k] for p in objects[f'target{i}'])/3 for k in (0,1)) for i in range(18)]
def transform(points,k,mirror):
    c,s=math.cos(k*math.pi/3),math.sin(k*math.pi/3)
    return [(c*(-x if mirror else x)-s*y,s*(-x if mirror else x)+c*y) for x,y in points]
result={}
for letter,n in [('A',6),('B',2),('C',6),('D',6),('E',3)]:
    source=[objects[f'option{letter}{i}'] for i in range(n)];placements={}
    for mirror in (False,True):
      for k in range(6):
        shape=[transform(t,k,mirror) for t in source];anchor=tuple(sum(p[a] for p in shape[0])/3 for a in (0,1))
        for cen in centers:
          dx,dy=cen[0]-anchor[0],cen[1]-anchor[1]
          translated=[[(x+dx,y+dy) for x,y in t] for t in shape]
          keys=[key(t) for t in translated]
          if all(t in target for t in keys):
            ids=tuple(sorted(target[t] for t in keys));mask=sum(1<<i for i in ids)
            placements.setdefault(mask,{'target_triangles':list(ids),'rotation_multiple60':k,'mirror':mirror,'translation':[dx,dy]})
    full=(1<<18)-1;solutions=[];nodes=[0]
    def cover(used,chosen):
      nodes[0]+=1
      if used==full:solutions.append(list(chosen));return
      i=next(i for i in range(18) if not used>>i&1)
      for mask,p in placements.items():
        if mask>>i&1 and not mask&used:cover(used|mask,chosen+[p])
    cover(0,[])
    result[letter]={'cell_count':n,'placement_count':len(placements),'complete_cover_count':len(solutions),'example_cover':solutions[0] if solutions else None,'placements':list(placements.values()),'search_nodes':nodes[0]}
assert {l:bool(d['complete_cover_count']) for l,d in result.items()}=={'A':True,'B':True,'C':True,'D':False,'E':True}
write(HERE/qid/'tiling_exact_cover_audit.json',{'method':'Enumerate every lattice placement from all6 rotations and reflections by aligning first triangle centroid to each source triangle, compare all three vertices rounded7decimal. Exhaustively cover18 source elementary triangles using each candidate tile only. Any tile boundary edge is along this triangular lattice, hence any legal alignment has one of these rotations; reflections are included conservatively.','source_original_PNG_viewed':True,'target_triangle_count':18,'formal_answer':'D','results':result,'source_fingerprints_path':str(HERE/qid/'input_fingerprints.json')})
print({l:(d['placement_count'],d['complete_cover_count']) for l,d in result.items()})
