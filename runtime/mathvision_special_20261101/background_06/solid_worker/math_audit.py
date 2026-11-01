from tools_local import *
import itertools
import numpy as np
def matrices():
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1],repeat=3):
            m=np.zeros((3,3),dtype=int)
            for r in range(3):m[r,perm[r]]=signs[r]
            yield m,int(round(np.linalg.det(m)))
def normalized(cells):
    a=np.array(list(cells),dtype=int);a-=a.min(axis=0)
    return sorted(map(list,a))
q='Solid127';models=AD.scenes[q]['visibility']['models']
full=set(itertools.product(range(5),range(2),range(3)))
missing=full-set(map(tuple,models['given_incomplete_cuboid']['unit_cubes']))
out={'missing_cells':sorted(map(list,missing)),'proper_matches':[],'improper_matches':[],'maps':{}}
for key in 'ABCDE':
    cells=np.array(models[key]['unit_cubes']);hits=[]
    for m,det in matrices():
        a=cells@m.T
        if normalized(a)==normalized(missing):
            shift=np.min(np.array(list(missing)),axis=0)-a.min(axis=0)
            hits.append({'matrix':m.tolist(),'determinant':det,'cell_origin_translation':shift.tolist()})
    out['maps'][key]=hits
    if any(h['determinant']==1 for h in hits):out['proper_matches'].append(key)
    if any(h['determinant']==-1 for h in hits):out['improper_matches'].append(key)
write(TASK/q/'cavity_congruence_audit.json',out);print(q,json.dumps(out))

# Visible surface colours fix the colour of every unit cube touching these faces.
# Search exact coloured straight rod/domino tilings, without inventing hidden colours.
def surface_colors(model):
    sx,sy,sz=model['size'];known={};conflicts=[]
    for r in model['visible_regions']:
        u0,v0,u1,v1=r['uv_bounds']
        for u in range(int(u0),int(u1)):
            for v in range(int(v0),int(v1)):
                cell=(u,0,v) if r['face']=='front' else (sx-1,u,v) if r['face']=='right' else (u,v,sz-1)
                color='W' if r['color'].lower()=='#ffffff' else 'G'
                if cell in known and known[cell]!=color:conflicts.append(cell)
                known[cell]=color
    assert not conflicts,conflicts
    return known
def solve_rods(size,known,pattern,counts=None):
    cells=set(itertools.product(*(range(d) for d in size)));placements=[];L=len(pattern)
    patterns={tuple(pattern),tuple(reversed(pattern))}
    if counts:patterns={tuple([color]*L) for color in counts}
    for c in cells:
        for axis in range(3):
            line=tuple(tuple(c[k]+(t if k==axis else 0) for k in range(3)) for t in range(L))
            if not set(line)<=cells:continue
            for colors in patterns:
                if all(p not in known or known[p]==col for p,col in zip(line,colors)):
                    placements.append((frozenset(line),dict(zip(line,colors)),colors[0] if counts else None))
    bycell={c:[p for p in placements if c in p[0]] for c in cells}
    nodes=0
    def search(left,stock,path):
        nonlocal nodes
        nodes+=1
        if not left:return path
        c=min(left,key=lambda c:sum(p[0]<=left and (not counts or stock[p[2]]>0) for p in bycell[c]))
        for p in bycell[c]:
            if p[0]<=left and (not counts or stock[p[2]]>0):
                nextstock=stock.copy()
                if counts:nextstock[p[2]]-=1
                hit=search(left-p[0],nextstock,path+[{'cells':sorted(map(list,p[0])),'colors':{','.join(map(str,c)):co for c,co in p[1].items()}}])
                if hit is not None:return hit
        return None
    hit=search(cells,counts.copy() if counts else {},[])
    return {'possible':hit is not None,'witness':hit,'search_nodes':nodes,'compatible_placement_count':len(placements)}
for q,counts,pattern in [('Solid119',{'W':1,'G':3},'WW'),('Solid137',{'W':2,'G':4},'WW'),('Solid130',None,'GGW')]:
    models=AD.scenes[q]['visibility']['surface_models'];out={}
    for key in 'ABCDE':
        model=models[key];known=surface_colors(model)
        out[key]={'known_colors':{','.join(map(str,c)):co for c,co in known.items()},**solve_rods(model['size'],known,pattern,counts)}
    write(TASK/q/'exact_colored_tiling_audit.json',{'method':'Exhaust all axis-aligned straight unit-cell rod placements in the exact size, both orientations, constrained by all original visible colours; exact cover with actual brick stock. Hidden colours remain unconstrained.','options':out})
    print(q,{k:{f:v[f] for f in ['possible','search_nodes','compatible_placement_count']} for k,v in out.items()})
q='Solid98';models=AD.scenes[q]['visibility']['cuboid_models'];out={}
for key in 'ABCDE':
    model=models[key];sx,sy,sz=model['dimensions'];known={}
    for y,line in enumerate(model['top_rows_front_to_back']):
        for x,color in enumerate(line):known[x,y,sz-1]=color
    for z,line in enumerate(model['front_rows_bottom_to_top']):
        for x,color in enumerate(line):known[x,0,z]=color
    known[sx-1,sy-1,0]=model['back_bottom_right_cube']
    out[key]=solve_rods(model['dimensions'],known,'WWGG')
write(TASK/q/'exact_colored_tiling_audit.json',{'method':'A length4 rod in a4x2x2 box must lie along x. Each four-cell row must be WWGG or GGWW. Exact cover over every visible source colour, hidden colours unconstrained.','options':out})
print(q,{k:v['possible'] for k,v in out.items()})

q='Solid121';models=AD.scenes[q]['visibility']['models']
assembled=models['assembled'];gray=[list(map(int,c.split(','))) for c,color in assembled['colors'].items() if color=='#cccccc']
out={'gray_cells':gray,'gray_count':len(gray),'candidate_counts':{k:len(models[k]['unit_cubes']) for k in 'ABCDE'},'proper_rotation_matches':[]}
for key in 'ABCDE':
    if any(det==1 and normalized(np.array(models[key]['unit_cubes'])@m.T)==normalized(gray) for m,det in matrices()):out['proper_rotation_matches'].append(key)
write(TASK/q/'gray_complement_audit.json',out);print(q,json.dumps(out))
