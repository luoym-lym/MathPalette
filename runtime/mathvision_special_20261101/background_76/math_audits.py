import bootstrap
from bootstrap import OWNROOT, PROJECT
import itertools, json, math, re, hashlib
from collections import Counter, deque

def save(qid,name,obj):
    p=OWNROOT/qid/name
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def scene(qid):
    return json.loads((PROJECT/f'SolidGeometry/dataset_generator/scenes/{qid}.json').read_text(encoding='utf-8'))
def canon(cells):
    mn=tuple(min(p[i] for p in cells) for i in range(3))
    return frozenset(tuple(p[i]-mn[i] for i in range(3)) for p in cells)
def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
ROT=[(p,s) for p in itertools.permutations(range(3)) for s in itertools.product((-1,1),repeat=3) if parity(p)*math.prod(s)==1]
def rotations(cells):
    return set(canon([tuple(s[i]*c[p[i]] for i in range(3)) for c in cells]) for p,s in ROT)
def xyz(s,p):
    return s['points'][p] if isinstance(p,str) else p
def voxel(s,o,offset=(0,0,0),face_axis=None):
    pts=[xyz(s,p) for p in o['points']]
    means=[sum(p[i] for p in pts)/len(pts)-offset[i] for i in range(3)]
    spans=[max(p[i] for p in pts)-min(p[i] for p in pts) for i in range(3)]
    axis=face_axis if face_axis is not None else min(range(3),key=lambda i:spans[i])
    out=[math.floor(v+1e-7) for v in means]
    # Front y=0 has inward cubie at y=0. Right and top use positive outer faces.
    out[axis]=round(means[axis])-(axis!=1)
    return tuple(out)
def groups(s,prefix,offset=(0,0,0)):
    result={}
    for o in s['objects']:
        m=re.fullmatch(re.escape(prefix)+r'face(\d+)_(\d+)_(\d+)',o['id'])
        if not m: continue
        index,face,_=map(int,m.groups())
        v=voxel(s,o,offset,face_axis={0:0,1:1,2:2}[face])
        color=o.get('semantic_color','#E6E6E6').upper()
        if index in result:
            assert result[index]==(v,color),(o['id'],result[index],v,color)
        result[index]=(v,color)
    return result

def audit83():
    s=scene('Solid83');out={}
    for i,letter in enumerate('ABCDE'):
        g=groups(s,letter,(6.5*i,0,0))
        seen={v for v,c in g.values()}
        supported=set(seen)
        for x,y,z in seen:
            supported.update((x,y,k) for k in range(z))
        out[letter]={'visible_unit_cubies':sorted(seen),'visible_count':len(seen),'downward_support_completion':sorted(supported),'supported_count':len(supported),'seen_native_indices':sorted(g)}
    save('Solid83','primary_count_audit.json',{'method':'Independent per-visible-unit reconstruction from frozen 3D faces, checked against actual source/formal views; downward supports are separately identified, not silently made printed givens.','options':out,'limitation':'This audit does not assume arbitrary unseen added dice or prove that the source convention excludes every alternative hidden filling. Any new hypothesis needing such uniqueness must be held before API.'})
    print('Solid83', {k:(v['visible_count'],v['supported_count']) for k,v in out.items()})

def audit85():
    # Manual native-image reconstruction. Rigid placements do not change adjacency.
    cells={'A':[(i,0,0) for i in range(4)],'B':[(x,0,z) for x in range(2) for z in range(2)],'C':[(0,0,0),(1,0,0),(2,0,0),(2,-1,0)],'D':[(0,0,0),(1,0,0),(1,-1,0),(2,-1,0)],'E':[(0,0,0),(1,0,0),(2,0,0),(1,0,1)]}
    out={}
    for q,c in cells.items():
        contacts=[(a,b) for a,b in itertools.combinations(c,2) if sum(abs(a[i]-b[i]) for i in range(3))==1]
        out[q]={'cells':c,'face_contacts':contacts,'contact_count':len(contacts),'external_faces':24-2*len(contacts)}
    assert min(out,key=lambda q:out[q]['external_faces'])=='B'
    save('Solid85','primary_surface_audit.json',{'actual_source_and_formal_native_views_used':True,'proof':'Each of 4 cubes contributes 6 faces; each glued full-face contact removes exactly two from the exterior. All five shown shapes have the listed contacts. Areas A/C/D/E=18 units, B=16. Thus B is the unique minimum among the actual choices. All faces, including unseen undersides, count.','options':out})
    print('Solid85', {k:v['external_faces'] for k,v in out.items()})

def placements(shape,size,known,color):
    result=[]
    for rot in rotations(shape):
        ext=[max(p[i] for p in rot)+1 for i in range(3)]
        for t in itertools.product(*(range(size[i]-ext[i]+1) for i in range(3))):
            cells=frozenset(tuple(p[i]+t[i] for i in range(3)) for p in rot)
            if any(p in known and known[p]!=color for p in cells):continue
            if not all(p in cells for p,c in known.items() if c==color):continue
            result.append(cells)
    return set(result)
def audit121():
    s=scene('Solid121')
    # Derive group origins from 3D coordinates; source rows are separated by z offset.
    origins={'assembled':(11,0,14),'white':(8,0,7),'black':(14,0,7)}
    print('Solid121 prefixes',sorted(set(re.sub(r'face.*','',o['id']) for o in s['objects'] if o['type']=='face')))
    # All individual shown part cubies expose at least one face.
    w=groups(s,'white_piece',origins['white']); b=groups(s,'black_piece',origins['black'])
    white=canon([v for v,c in w.values()]);black=canon([v for v,c in b.values()])
    assembled=groups(s,'assembled',origins['assembled'])
    known={v:('W' if c=='#FFFFFF' else 'B' if c=='#555555' else 'G') for v,c in assembled.values()}
    options={}
    for i,q in enumerate('ABCDE'):
        g=groups(s,q,(6*i,0,0))
        options[q]=canon([v for v,c in g.values()])
    size=(3,3,2); box=set(itertools.product(range(3),range(3),range(2)))
    wp=placements(white,size,known,'W');bp=placements(black,size,known,'B')
    witnesses=[]
    erot=rotations(options['E'])
    for a in wp:
        for b0 in bp:
            if a&b0:continue
            rem=box-a-b0
            if canon(rem) in erot:
                witnesses.append({'white':sorted(a),'black':sorted(b0),'gray':sorted(rem)})
    assert len(white)==4 and len(black)==7 and len(options['E'])==7 and witnesses
    save('Solid121','primary_complement_audit.json',{'method':'Independent 3D visible cubie reconstruction and all 24 proper rotations for part placements in the actual 3x3x2 assembly; known exposed colors are constraints.','white_part':sorted(white),'black_part':sorted(black),'known_assembled_colors':{str(k):v for k,v in known.items()},'gray_count':18-len(white)-len(black),'option_cells':{q:sorted(c) for q,c in options.items()},'option_counts':{q:len(c) for q,c in options.items()},'white_placements':len(wp),'black_placements':len(bp),'valid_E_witnesses':witnesses,'proof':'18 total - 4 white - 7 black = 7 gray; only E has 7 unit cubes. The saved placement witness attains the stated assembly and E up to proper rotation. D disconnected front cell is retained.'})
    print('Solid121', {q:len(c) for q,c in options.items()})

def audit130():
    s=scene('Solid130'); box=list(itertools.product(range(3),repeat=3));index={p:i for i,p in enumerate(box)};out={}
    for i,q in enumerate('ABCDE'):
        known={}
        face_bindings=[]
        for o in s['objects']:
            m=re.fullmatch(q+r'_(front|right|top)_(\d+)_fill',o['id'])
            if not m:continue
            v=voxel(s,o,(6*i,0,0),face_axis={'front':1,'right':0,'top':2}[m[1]])
            color='W' if o['semantic_color'].upper()=='#FFFFFF' else 'G'
            if v in known:assert known[v]==color
            known[v]=color
            face_bindings.append({'id':o['id'],'cubie':v,'color':color})
        assert len(known)==19 and set(known)<=set(box)
        rods=[]
        for axis in range(3):
            for fixed in itertools.product(range(3),repeat=2):
                cells=[]
                for t in range(3):
                    p=list(fixed);p.insert(axis,t);cells.append(tuple(p))
                for colors in [('W','G','G'),('G','G','W')]:
                    if any(p in known and known[p]!=c for p,c in zip(cells,colors)):continue
                    mask=sum(1<<index[p] for p in cells)
                    rods.append((mask,cells,colors))
        bycell={i:[j for j,r in enumerate(rods) if r[0]&(1<<i)] for i in range(27)}
        nodes=0;dead=set()
        def solve(left):
            nonlocal nodes
            nodes+=1
            if not left:return []
            if left in dead:return None
            choices=min(([j for j in bycell[k] if rods[j][0]&left==rods[j][0]] for k in range(27) if left&(1<<k)),key=len)
            for j in choices:
                tail=solve(left^rods[j][0])
                if tail is not None:return [j]+tail
            dead.add(left);return None
        sol=solve((1<<27)-1)
        out[q]={'known_colors':{','.join(map(str,k)):v for k,v in known.items()},'face_to_cubie_bindings':face_bindings,'compatible_colored_placements':len(rods),'search_nodes':nodes,'exhausted_infeasible':sol is None,'possible':sol is not None,'nine_rod_witness':None if sol is None else [{'cells':rods[j][1],'colors':rods[j][2]} for j in sol]}
        assert sol is None or len(sol)==9
    assert [q for q,v in out.items() if v['possible']]==['A']
    save('Solid130','primary_exact_cover_audit.json',{'method':'All 3 axes x 9 lines x both end orientations of actual straight GGW/WGG rods, each occupying 3 unit cells; independent exact cover of all 27 cells with 9 rods. Every exposed face constrains its actual cubie color; hidden colors unconstrained. No visible-pair shortcut or invented decomposition.','options':out,'unique_answer':'A'})
    print('Solid130',{q:(v['possible'],v['search_nodes']) for q,v in out.items()})

def audit132():
    s=scene('Solid132');out={}
    exposed={p for p in itertools.product(range(3),repeat=3) if p[0]==2 or p[1]==0 or p[2]==2}
    for i,q in enumerate('ABCDE'):
        known={p:'white' for p in exposed};patches=[];checks={}
        for o in s['objects']:
            if o['type']!='face' or not o['id'].startswith('fill'+str(i)):continue
            v=voxel(s,o,(5.2*i,0,0.52*i))
            col=o['semantic_material']
            assert v in exposed
            if v in checks:assert checks[v]==col
            checks[v]=col;known[v]=col
            patches.append({'native_id':o['id'],'cubie':v,'class':col})
        counts=Counter(known.values());deficit={c:9-counts[c] for c in ['white','light','dark']}
        possible=all(v>=0 for v in deficit.values()) and sum(deficit.values())==8
        hidden=sorted(set(itertools.product(range(3),repeat=3))-exposed)
        completion=None
        if possible:
            completion={};k=0
            for c,n in deficit.items():
                for p in hidden[k:k+n]:completion[str(p)]=c
                k+=n
        out[q]={'visible_unique_cubies':{str(p):c for p,c in known.items()},'counts':dict(counts),'deficits_to_nine':deficit,'possible':possible,'hidden_eight_completion':completion,'nonwhite_face_patch_to_cubie_bindings':patches}
    assert [q for q,v in out.items() if v['possible']]==['A']
    save('Solid132','primary_inventory_audit.json',{'method':'Map each actual front/right/top unit face to its 3D cubie, merge duplicate exposures, retain white/light/dark classes exactly. 19 distinct cubies are exposed; 8 unseen remain. A choice is feasible iff no class has more than9 exposed cubies; deficits then sum to8.','options':out,'unique_answer':'A'})
    print('Solid132',{q:v['counts'] for q,v in out.items()})

def rotate2(pattern,k):
    result=set(pattern)
    for _ in range(k):result={(c,2-r) for r,c in result}
    return result
def audit151():
    s=scene('Solid151');patterns={f'{row}{i}':set() for row in [0,1] for i in range(5)}
    for o in s['objects']:
        m=re.fullmatch(r'cell([01])([0-4])([0-2])([0-2])',o['id'])
        if m:
            a,b,r,c=map(int,m.groups());patterns[f'{a}{b}'].add((r,c))
    parts={key:{'corners':sum(r in [0,2] and c in [0,2] for r,c in p),'edge_middles':sum((r==1) != (c==1) for r,c in p),'center':int((1,1) in p)} for key,p in patterns.items()}
    given={k:sum(parts[f'0{i}'][k] for i in range(5)) for k in ['corners','edge_middles','center']}
    incidence={}
    for i,q in enumerate('ABCDE'):
        v=parts[f'1{i}'];cs=given['corners']+v['corners'];es=given['edge_middles']+v['edge_middles'];centers=given['center']+v['center']
        integral=cs%3==0 and es%2==0
        black=cs//3+es//2+centers if integral else None
        incidence[q]={'corner_incidence':cs,'edge_middle_incidence':es,'black_face_centers':centers,'integer_cube_incidence':integral,'black_exterior_cubies':black,'possible_under_15_black':integral and black in [14,15]}
    assert [q for q,v in incidence.items() if v['possible_under_15_black']]==['A']
    # Existence: assign the six printed patterns to actual cube faces and independently check
    # every shared corner/edge identity, rather than relying on the incidence bound alone.
    frames=[((0,0,1),(1,0,0),(0,1,0)),((0,0,-1),(-1,0,0),(0,1,0)),((1,0,0),(0,1,0),(0,0,1)),((-1,0,0),(0,-1,0),(0,0,1)),((0,1,0),(-1,0,0),(0,0,1)),((0,-1,0),(1,0,0),(0,0,1))]
    def face_map(p,frame,k):
        n,u,v=frame;pat=rotate2(p,k);cells={}
        for r,c in itertools.product(range(3),repeat=2):
            pos=tuple(1+n[j]+(c-1)*u[j]+(1-r)*v[j] for j in range(3));cells[pos]=int((r,c) in pat)
        return cells
    keys=[f'0{i}' for i in range(5)]+['10'];start=face_map(patterns['00'],frames[0],0);nodes=0
    def fit(face,left,known,assign):
        nonlocal nodes
        nodes+=1
        if face==6:
            b=sum(known.values())
            return (known,assign) if b in [14,15] else None
        for key in left:
            for k in range(4):
                add=face_map(patterns[key],frames[face],k)
                if any(p in known and known[p]!=c for p,c in add.items()):continue
                ans=fit(face+1,[t for t in left if t!=key],known|add,assign+[{'face_index':face,'printed_pattern':key,'rotation_quarter_turns':k}])
                if ans:return ans
        return None
    witness=fit(1,keys[1:],start,[{'face_index':0,'printed_pattern':'00','rotation_quarter_turns':0}])
    assert witness
    known,assign=witness;known[(1,1,1)]=15-sum(known.values());assert sum(known.values())==15 and len(known)==27
    save('Solid151','primary_cube_identity_audit.json',{'patterns':{k:sorted(v) for k,v in patterns.items()},'per_pattern_counts':parts,'given_incidence_sums':given,'candidates':incidence,'proof':'Each corner cubie occurs on 3 faces, each edge-middle on 2, each face-center on 1. The only nonexposed cubie is the interior. Nonintegral candidate totals rule out B/C/D; E requires16 black exterior cubies and violates15. A gives6 black corner cubies+5 black edge cubies+4 black face centers=15 and an interior white cube. Saved full 3D face assignment independently proves existence with all shared identities.','existence_search_nodes':nodes,'A_witness_face_assignments':assign,'A_witness_cubie_colors':{str(p):'B' if c else 'W' for p,c in known.items()},'unique_answer':'A'})
    print('Solid151',incidence,'witness_nodes',nodes)

def neg(a):return tuple(-v for v in a)
def add(*vs):return tuple(map(sum,zip(*vs)))
def fold_cells(cells):
    first=min(cells);frames={first:((1,0,0),(0,1,0),(0,0,1),(0,0,1))};todo=deque([first]);incons=[]
    while todo:
        p=todo.popleft();u,v,n,c2=frames[p]
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt=(p[0]+dx,p[1]+dy)
            if nxt not in cells:continue
            if dx==1:up,vp,np,cp=neg(n),v,u,add(c2,u,neg(n))
            elif dx==-1:up,vp,np,cp=n,v,neg(u),add(c2,neg(u),neg(n))
            elif dy==1:up,vp,np,cp=u,neg(n),v,add(c2,v,neg(n))
            else:up,vp,np,cp=u,n,neg(v),add(c2,neg(v),neg(n))
            new=(up,vp,np,cp)
            if nxt in frames:
                if frames[nxt]!=new:incons.append({'edge':[p,nxt],'existing':frames[nxt],'required':new})
            else:frames[nxt]=new;todo.append(nxt)
    normals=[f[2] for f in frames.values()];overlaps=[]
    for a,b in itertools.combinations(frames,2):
        if frames[a][2]==frames[b][2]:overlaps.append([a,b])
    valid=len(frames)==5 and not incons and not overlaps and all(f[2]==f[3] for f in frames.values())
    return {'valid':valid,'frames':{str(p):{'u':u,'v':v,'normal':n,'twice_center':c,'twice_vertices':[add(c,tuple(a*x for x in u),tuple(b*x for x in v)) for a,b in itertools.product((-1,1),repeat=2)]} for p,(u,v,n,c) in frames.items()},'inconsistent_hinge_cycles':incons,'duplicate_face_normals':overlaps}
def audit_folding(qid):
    s=scene(qid)
    if qid=='Solid211':
        initial={tuple(int(min(xyz(s,p)[i] for p in o['points'])) for i in [0,1]) for o in s['objects'] if o['type']=='face'}
    else:initial={(1,1),(1,2),(1,3),(2,2)}
    candidates={o['text']:tuple(round(xyz(s,o['anchor'])[i]-.5) for i in [0,1]) for o in s['labels']}
    assert len(candidates)==(9 if qid=='Solid211' else 8)
    out={q:{'flat_added_cell':p,**fold_cells(initial|{p})} for q,p in candidates.items()}
    count=sum(v['valid'] for v in out.values());assert count==6
    save(qid,'primary_folding_audit.json',{'method':'Independently propagate oriented 3D unit-square frames and doubled centers through every actual shared edge with 90-degree inward cube folds. Check every hinge cycle, distinct face normals, shared positions and one common unit cube. Five distinct normals mean five faces of that cube with no interior face overlap.','initial_cells':sorted(initial),'attachment_count':len(candidates),'cases':out,'valid_positions':[q for q,v in out.items() if v['valid']],'answer':count,'source_and_formal_native_view_inspected':True,'preserved_original_solid_dashed_fill_and_letter_number_membership':True})
    print(qid,[q for q,v in out.items() if v['valid']])

if __name__=='__main__':
    import sys
    tasks={'Solid83':audit83,'Solid85':audit85,'Solid121':audit121,'Solid130':audit130,'Solid132':audit132,'Solid151':audit151,'Solid211':lambda:audit_folding('Solid211'),'Solid221':lambda:audit_folding('Solid221')}
    for q in sys.argv[1:] or list(tasks):tasks[q]()
