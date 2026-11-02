from tools45 import *
import itertools as it
import numpy as np

def rotations(det=1):
    out=[]
    for perm in it.permutations(range(3)):
        for signs in it.product([-1,1],repeat=3):
            m=np.zeros((3,3),dtype=int)
            for j in range(3):m[perm[j],j]=signs[j]
            if round(np.linalg.det(m))==det:out.append(m)
    return out
ROT=rotations()
def source(q):
    r=AD.records[q];return read((ROOT/'SolidGeometry'/r['runtime_dependencies'][0]).parent/'scene.json')
notes=read(ROOT/'provenance/source_notes.json')
aud={}

# A domino tiling is exactly a perfect matching of the face-adjacency graph.
sets=notes['Solid81']['audit']['inventory']['image2']
def matchings(cells):
    cells=set(map(tuple,cells))
    if not cells:return [[]]
    a=min(cells);result=[]
    for b in sorted(cells-{a}):
        if sum(abs(x-y) for x,y in zip(a,b))==1:
            result += [[[a,b]]+tail for tail in matchings(cells-{a,b})]
    return result
aud['Solid81']={'method':'Fresh exhaustive face-adjacency perfect matching; no fixed cuts added.','cube_sets':sets,'matchings':{k:matchings(v) for k,v in sets.items()},'unique_answer':'B','proof':'B is K1,3: any first domino consumes the center and one leaf, leaving two nonadjacent leaves. A,C,D,E have witnesses listed.'}

# Fix the first cube orientation; enumerate all six-face completions and all 24 rotations.
normals=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
initial={(0,0,1):'square',(0,-1,0):'line',(1,0,0):'small_diamond'}
free=[v for v in normals if v not in initial];valid=[]
for perm in it.permutations(['big_diamond','plus','X']):
    labels={**initial,**dict(zip(free,perm))}
    for m in ROT:
        turned={tuple(m@np.array(n)):v for n,v in labels.items()}
        if turned[(0,0,1)]=='plus' and turned[(0,-1,0)]=='square' and turned[(1,0,0)]=='X':
            valid.append({'labeling':{str(k):v for k,v in labels.items()},'rotation':m.tolist(),'opposite_square':labels[(0,0,-1)]})
assert valid and {v['opposite_square'] for v in valid}=={'big_diamond'}
aud['Solid84']={'method':'All 6 completions of first visible corner times 24 proper cube rotations','valid_configurations':valid,'unique_answer':'C','proof':'The square face is adjacent to line and small diamond in view1 and plus and X in view2. These are four distinct neighbors; its only opposite is big diamond. No facial pattern is recolored.'}

label={(0,0,1):2,(0,0,-1):5,(0,-1,0):1,(0,1,0):6,(-1,0,0):3,(1,0,0):4}
valids={}
for determinant in [1,-1]:
    vv=[]
    for m in rotations(determinant):
        turned={tuple(m@np.array(n)):v for n,v in label.items()}
        if turned[(0,0,1)]==6 and turned[(0,-1,0)]==4:vv.append({'matrix':m.tolist(),'right_face':turned[(1,0,0)]})
    valids[str(determinant)]=vv
assert [x['right_face'] for x in valids['1']]==[5] and [x['right_face'] for x in valids['-1']]==[2]
aud['Solid97']={'method':'Fresh full signed-axis enumeration, keeping only determinant+1 for actual rotations','first_die_normal_values':{str(n):v for n,v in label.items()},'rotation_and_reflection_comparison':valids,'unique_answer':'A = only5','predeclared_misconception':'Improper reflection instead of a proper rotation gives exactly2 (B).','red_edge_color_preserving_reading':'The two red seams bound distinct opposite edge pairs {1,3} and {4,6} on one standard die. Edge {1,3} is not visible in view2 and edge {4,6} is not visible in view1. A cube with these two actual red edges and all other shown edges black realizes BOTH views, with right face5. Thus a material edge-ink reading does not eliminate the original answer.','pip_integrity':'Only dicee6 and dicee10 are styled; no pip objects or unknown arrow are edited.'}

# Each rigid length4 bar must lie on the box's only four-unit axis.
models=notes['Solid98']['audit']['inventory']['visible_models'];rowaudit={}
for qid,m in models.items():
    if qid=='given':continue
    rows=m['front_rows_bottom_to_top']+m['top_rows_front_to_back']
    rowaudit[qid]={'required_rows':rows,'illegal_rows':[r for r in rows if r not in ['WWGG','GGWW']],'possible':all(r in ['WWGG','GGWW'] for r in rows)}
assert [k for k,x in rowaudit.items() if x['possible']]==['A']
aud['Solid98']={'method':'Fresh row-orientation necessity and explicit hidden-row completion; visible colors read against source JPG and native model','row_audit':rowaudit,'A_hidden_back_bottom_witness':'WWGG (right cube G agrees with shown side)','unique_answer':'A','new_prospective_mechanism_assessed':'Rearrange the given WW/GG ordered pair into a bent2x2 top-left group of C rather than the old B straight front rows. Counts agree locally but a rigid rod cannot turn.','semantic_objection':'Coloring source edges and only a bent receiver can reasonably become physical colored-rod matching; full matching in A then loses source marks. Drawing a closed2x2 receiving outline would additionally suggest a fixed new block partition. No clean, concise external comparison presentation established; skip rather than test a cosmetic front-row relocation.'}

aud['Solid100']={'method':'Independent regular-polygon angle formula and actual tiling incidence','n':8,'interior_angle_degrees':(8-2)*180/8,'outer_vertex_wholly_in_one_rhombus':'P0 belongs only to top rhombus, so its135degree interior angle is the rhombus obtuse angle. The four rhombi are congruent.','unique_answer':'A=135degrees','target_search':'Boundary/square/acute-rhombus confusion naturally yields45,90,225,270; none is a distractor. A140/144/145/150 preset would lack a specific geometric derivation. No call.'}

triples={'A':[2,3,1],'B':[1,1,1],'C':[3,1,3],'D':[3,2,2],'E':[1,2,2]};inventory={1:3,2:2,3:1};multiplicity={}
for k,t in triples.items():
    used={v:t.count(v) for v in inventory}
    possible=all(used[v]<=inventory[v] for v in inventory)
    multiplicity[k]={'visible_top_left_front':t,'used':used,'possible':possible,'hidden_face_completion':sum(([v]*(inventory[v]-used[v]) for v in inventory),[]) if possible else None}
assert [k for k,x in multiplicity.items() if not x['possible']]==['C']
aud['Solid101']={'method':'Multiply the probabilities by6 and independently check each pictured corner inventory','face_inventory':inventory,'options':multiplicity,'unique_answer':'C','local_grouping_assessed':'Compare D/E repeated2 faces by true rim edges, or B three1 faces as one same-value group. Both are legal multiplicities; the hypothesized global rejection has no distinct geometric source feature beyond simply emphasizing a legal option. No new face/pip/color identity is introduced and no call is warranted.'}

# Fresh exact disjoint packing: independent enumeration, not old witnesses.
native=notes['Solid105']['audit']['inventory']['native_models'];target=set(map(tuple,native['target']['unit_cubes']))
def placements(cubes):
    result={}
    for m in ROT:
        pts=[tuple(m@np.array(v)) for v in cubes]
        for a in pts:
            for b in target:
                delta=tuple(np.array(b)-a);image=frozenset(tuple(np.array(v)+delta) for v in pts)
                if image<=target:result.setdefault(image,{'rotation':m.tolist(),'translation':delta,'cells':sorted(image)})
    return result
packing={}
for j,k in enumerate('ABCDE'):
    l=placements(native[str(j)+'left']['unit_cubes']);r=placements(native[str(j)+'right']['unit_cubes'])
    witnesses=[{'left':vl,'right':r[frozenset(target-sl)]} for sl,vl in l.items() if frozenset(target-sl) in r]
    packing[k]={'left_placement_count':len(l),'right_placement_count':len(r),'solutions':witnesses}
assert [k for k,v in packing.items() if v['solutions']]==['A']
aud['Solid105']={'method':'Fresh24 proper-rotation/translation exact pair cover; reflected pieces forbidden','models':native,'packing':packing,'unique_answer':'A','local_mechanisms_assessed':['Pair B mirror-handed terminal caps are projected alike but globally incompatible.','C/E single matching cap cannot establish a disjoint eight-voxel union.'],'skip_reason':'At native size the unit is roughly17px; marking terminal caps while retaining all chirality cues and a clear source-to-both-piece mapping was not established. Colored material edge matching could add an independent assembly restriction; external multi-segment connectors either cross the tiny discriminating seams or carry no actual source contact information. No arbitrary wrong pair highlighting.'}

# Tetrahedron contact propagation on the actual seven-triangle graph.
s=source('Solid108');P=s['projection']
def projected(p):return tuple(np.round(np.array(P['matrix'])@(np.array(p)-P['origin'])+P['offset'],12))
edges=[tuple(projected(p) for p in x['points']) for x in s['objects'] if x['id'].startswith('netedge')]
verts=sorted({p for e in edges for p in e});es={frozenset(e) for e in edges}
triangles=[frozenset(t) for t in it.combinations(verts,3) if all(frozenset(e) in es for e in it.combinations(t,2))]
centers={lab['text']:np.array(projected(lab['anchor'])) for lab in s['labels']}
named={k:min(triangles,key=lambda t:np.linalg.norm(np.mean(list(t),axis=0)-c)) for k,c in centers.items()}
named['blank']=next(t for t in triangles if t not in named.values())
route=[named[k] for k in ['START','blank','A','B','C','D','E']];walks=[]
for assignment in it.permutations([0,1,2]):
    ids=dict(zip(sorted(route[0]),assignment));apex=3;faces=[sorted(ids.values())]
    for a,b in zip(route,route[1:]):
        common=a&b;assert len(common)==2
        removed=next(iter(a-b));added=next(iter(b-a));old=ids[removed]
        ids={v:ids[v] for v in common}|{added:apex};apex=old;faces.append(sorted(ids.values()))
    first=next(j for j,f in enumerate(faces[1:],1) if f==[0,1,2]);assert first==6
    walks.append({'initial_assignment':assignment,'contact_faces':faces,'first_return_roll':first})
aud['Solid108']={'method':'Fresh tetrahedron vertex/apex propagation on actual projected strip graph; all6 initial marked-face labelings','triangles':{k:sorted(v) for k,v in named.items()},'ordered_route':['START','blank','A','B','C','D','E'],'walks':walks,'unique_answer':'E after6rolls','hinge_correspondence':'Red START->blank(edge1) corresponds to red C->D(edge9); blue blank->A(edge3) corresponds to blue D->E(edge11). The two open two-hinge paths are congruent under a planar-120degree rotation and translation. That planar mapping sends START triangle to C, but does not preserve the rolled contact face: C has face123, not012.','semantics':'Only existing fixed-board crossing edges are colored. No tetrahedron edge/face is recolored, no second marked face or extra triangle, new rolling edge, shortcut or arrow. Colors of the stationary board cannot be a physical face-ink preservation condition.'}

def convert(v):
    if isinstance(v,dict):return {str(k):convert(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [convert(x) for x in v]
    if isinstance(v,np.generic):return v.item()
    return v
write(TASK/'independent_primary_math_audit.json',convert(aud))
for q,x in aud.items():print(q,x['unique_answer'])
