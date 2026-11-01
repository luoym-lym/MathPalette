from tools_local import *
from collections import deque
base={(0,0),(0,1),(1,1),(2,1)};poss={1:(0,-1),2:(1,0),3:(2,0),4:(3,1),5:(2,2),6:(1,2),7:(0,2),8:(-1,1),9:(-1,0)}
neg=lambda a:tuple(-x for x in a)
def fold(cells):
 d={(0,1):((1,0,0),(0,1,0),(0,0,1))};queue=deque(d)
 while queue:
  xy=queue.popleft();u,v,n=d[xy]
  for delta,f in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
   c=(xy[0]+delta[0],xy[1]+delta[1])
   if c not in cells:continue
   if c in d:
    if d[c]!=f:return {'valid':False,'cycle_inconsistent':True}
   else:d[c]=f;queue.append(c)
 normals={str(c):ori[2] for c,ori in sorted(d.items())}
 return {'valid':len(set(ori[2] for ori in d.values()))==len(cells),'normals':normals}
r={str(i):fold(base|{c}) for i,c in poss.items()};write(TASK/'Solid211/folding_audit.json',{'base':sorted(base),'positions':poss,'all_nine':r,'valid_positions':[i for i,c in r.items() if c['valid']]});print(json.dumps(r,indent=2))
