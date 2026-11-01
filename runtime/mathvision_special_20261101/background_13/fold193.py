from tools13 import *
import numpy as np
from collections import deque
qid='Solid193';s=AD.scenes[qid]
p=ROOT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/qid/'scene.json'
ns=json.loads(p.read_text(encoding='utf-8'));out=[]
def t(a):return tuple(float(x) for x in a)
for ix,panel in enumerate(ns['net_panels']):
    off=np.array(panel['page_offset']);cells={tuple(r['xy']) for r in panel['unit_cells']}
    root=min(cells);trans={root:(np.zeros(3),np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1]))};q=deque([root])
    while q:
        cell=q.popleft();o,u,v,n=trans[cell]
        for d,oo,uu,vv,nn in [( (1,0),o+u,-n,v,u),((-1,0),o-n,n,v,-u),((0,1),o+v,u,-n,v),((0,-1),o-n,u,n,-v)]:
            nc=(cell[0]+d[0],cell[1]+d[1])
            if nc in cells and nc not in trans:trans[nc]=(oo,uu,vv,nn);q.append(nc)
    normals={t(v[3]) for v in trans.values()};alln={(1.,0.,0.),(-1.,0.,0.),(0.,1.,0.),(0.,-1.,0.),(0.,0.,1.),(0.,0.,-1.)};missing=next(iter(alln-normals))
    tris=[]
    for j in range(4):
        a=s['objects'];name=f'net{ix}triangle{j}side'
        sides=[next(x for x in a if x['id']==name+str(k))['points'] for k in [0,1]]
        base=[np.array([v[0],v[2]])-off for v in [sides[0][0],sides[1][0]]];apex=np.array([sides[0][1][0],sides[0][1][2]])-off
        midpoint=(base[0]+base[1])/2;found=[]
        for cell in cells:
            cx,cy=cell
            if midpoint[0]==cx and cy<=midpoint[1]<=cy+1:found.append((cell,'W'))
            if midpoint[0]==cx+1 and cy<=midpoint[1]<=cy+1:found.append((cell,'E'))
            if midpoint[1]==cy and cx<=midpoint[0]<=cx+1:found.append((cell,'S'))
            if midpoint[1]==cy+1 and cx<=midpoint[0]<=cx+1:found.append((cell,'N'))
        assert len(found)==1,(ix,j,found)
        cell,d=found[0];o,u,v,n=trans[cell]
        normal={'W':-u,'E':u,'S':-v,'N':v}[d]
        apt={'W':o+v/2-n/2,'E':o+u+v/2-n/2,'S':o+u/2-n/2,'N':o+v+u/2-n/2}[d]
        b3=[o+(b[0]-cell[0])*u+(b[1]-cell[1])*v for b in base]
        tris.append({'triangle':j,'hinge_cell':cell,'side':d,'base_local':[t(b) for b in base],'folded_normal':t(normal),'folded_apex':t(apt),'folded_base':[t(b) for b in b3],'lies_on_missing_face':t(normal)==missing})
    valid=len(normals)==5 and all(x['lies_on_missing_face'] for x in tris) and len({tuple(sorted(map(tuple,x['folded_base']))) for x in tris})==4 and len({tuple(x['folded_apex']) for x in tris})==1
    out.append({'net':ix+1,'square_faces':{str(k):{'o':t(z[0]),'u':t(z[1]),'v':t(z[2]),'n':t(z[3])} for k,z in trans.items()},'missing_normal':missing,'triangles':tris,'valid':valid})
write(TASK/qid/'primary_fold_audit.json',{'source':str(p.relative_to(ROOT)),'source_sha256':file_hash(p),'method':'Independently propagate each unit-square hinge by exact 90-degree cube fold, then fold all four quarter-face triangles at their existing base edge. Valid iff five distinct square normals and four distinct quarter triangles cover the missing face with common apex center.','results':out,'invalid_nets':[x['net'] for x in out if not x['valid']],'correct_answer':'E','duplicate_source_choices':'C and D both 2 and 4, neither correct; preserved unchanged.'})
print([(x['net'],x['valid'],[z['lies_on_missing_face'] for z in x['triangles']]) for x in out])
