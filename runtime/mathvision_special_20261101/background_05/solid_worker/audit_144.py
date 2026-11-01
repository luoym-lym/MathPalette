from tools_local import *
import numpy as np
import itertools
qid='Solid144'
context=json.loads((TASK/qid/'context.json').read_text(encoding='utf-8'))
groups={}
for name in ['given_gray','W','X','Y','Z']:
    objects=[o for o in context['objects'] if o['id'].startswith(name+'e') and o['styleable']]
    lines=[np.array(o['geometry']['points'],float) for o in objects]
    a=lines[0][1]-lines[0][0];a=a/np.linalg.norm(a)
    b=next((p[1]-p[0])/np.linalg.norm(p[1]-p[0]) for p in lines if abs(np.dot((p[1]-p[0])/np.linalg.norm(p[1]-p[0]),a))<1e-7)
    c=np.cross(a,b);frame=np.array([a,b,c]).T;origin=lines[0][0]
    corners=set();off_grid=[]
    for line in lines:
        for p in line:
            v=frame.T@(p-origin)
            if max(abs(v-np.rint(v)))<1e-7:corners.add(tuple(int(x) for x in np.rint(v)))
            else:off_grid.append(v.tolist())
    groups[name]={'frame':frame.tolist(),'origin':origin.tolist(),'lattice_corners':sorted(corners),'off_grid_visibility_split_points':off_grid}
def normal(points):
    p=np.array(points,dtype=int);p=p-np.min(p,axis=0);return tuple(sorted(map(tuple,p.tolist())))
reference=normal(groups['given_gray']['lattice_corners']);matches={}
for name in ['W','X','Y','Z']:
    points=np.array(groups[name]['lattice_corners'],int);found=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1],repeat=3):
            matrix=np.eye(3,dtype=int)[list(perm)]*np.array(signs)[:,None]
            if normal(points@matrix.T)==reference:found.append({'determinant':int(round(np.linalg.det(matrix))),'lattice_matrix':matrix.tolist()})
    matches[name]=found
result={'question_id':qid,'method':'Recover a right-handed orthonormal lattice frame from frozen 3D edge directions. Exclude non-lattice visibility split endpoints; enumerate all 48 signed axis permutations and translations of the full remaining boundary-corner point set.','groups':groups,'matches':matches,'proper_rotation_matches':[n for n,m in matches.items() if any(t['determinant']==1 for t in m)],'reflections_only':[n for n,m in matches.items() if m and not any(t['determinant']==1 for t in m)]}
write(TASK/qid/'lattice_corner_congruence_audit.json',result)
print(json.dumps({'corner_counts':{k:len(v['lattice_corners']) for k,v in groups.items()},'proper':result['proper_rotation_matches'],'reflections_only':result['reflections_only'],'matches':matches},ensure_ascii=False))
