from tools_local import *
from collections import deque,Counter
import numpy as np
CELLS={(0,0),(1,0),(2,0),(3,0),(1,1),(1,-1)}
def frames():
    f={(1,0):(np.array([0,0,0]),np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1]))};q=deque([(1,0)])
    while q:
        x,y=q.popleft();o,u,v,n=f[x,y]
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            key=(x+dx,y+dy)
            if key not in CELLS or key in f:continue
            if dx==1:uu,vv,nn=-n,v,u;oo=o+u
            elif dx==-1:uu,vv,nn=n,v,-u;oo=o-uu
            elif dy==1:uu,vv,nn=u,-n,v;oo=o+v
            else:uu,vv,nn=u,n,-v;oo=o-vv
            f[key]=(oo,uu,vv,nn);q.append(key)
    return f
F=frames()
def point(cell,p):
    o,u,v,n=F[cell]
    return tuple((o+(p[0]-cell[0])*u+(p[1]-cell[1])*v).tolist())
def diagonal_graph(qid):
    result={};scene=AD.scenes[qid]
    for i,letter in enumerate('ABCD'):
        offset=7*i;edges=[]
        for obj in scene['objects']:
            if obj['id'].startswith(letter+'diagonal'):
                pts=[(p[0]-offset,p[2]) for p in obj['points']]
                cell=(int((pts[0][0]+pts[1][0])/2//1),int((pts[0][1]+pts[1][1])/2//1))
                edges.append({'id':obj['id'],'cell':cell,'page_endpoints':pts,'folded_endpoints':[point(cell,p) for p in pts]})
        degrees=Counter(p for e in edges for p in e['folded_endpoints'])
        result[letter]={'edges':edges,'vertex_degrees':{str(k):v for k,v in degrees.items()},'forms_triangle':sorted(degrees.values())==[2,2,2]}
    return result
if __name__=='__main__':
    r=diagonal_graph('Solid188');write(TASK/'Solid188/fold_graph_audit.json',r);print(json.dumps(r,ensure_ascii=False))
