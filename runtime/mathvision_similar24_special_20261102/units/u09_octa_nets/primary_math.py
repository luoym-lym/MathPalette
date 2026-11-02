from own_bootstrap import *
from itertools import combinations, permutations, product
from collections import defaultdict, deque
import math

def neg(v): return tuple(-x for x in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def canon(s): return sorted(tuple(x) for x in s)

def fold(faces, seed, initial):
    fm={seed:dict(zip(faces[seed],initial))}
    steps=[]
    queue=deque([seed])
    while queue:
        a=queue.popleft()
        for b in faces:
            common=set(faces[a])&set(faces[b])
            if len(common)!=2: continue
            old=next(v for v in faces[a] if v not in common)
            new=next(v for v in faces[b] if v not in common)
            candidate={v:fm[a][v] for v in common}
            candidate[new]=neg(fm[a][old])
            if b in fm:
                assert candidate==fm[b]
            else:
                fm[b]=candidate;queue.append(b)
                steps.append({'from':a,'to':b,'hinge':[list(v) for v in sorted(common)],
                    'old_third':list(old),'new_third':list(new),'old_world':fm[a][old], 'new_world':candidate[new]})
    assert len(fm)==8
    unique={tuple(canon(v.values())) for v in fm.values()}
    assert len(unique)==8
    vertices=set(v for f in fm.values() for v in f.values())
    assert len(vertices)==6
    for coords in fm.values():
        assert len(set(coords.values()))==3
        assert all(dot(a,b)==0 for a,b in combinations(coords.values(),2))
    return fm,steps

def audit_solid(qid,scene):
    objs=[o for o in scene['objects'] if o['type']=='segment' and not o['id'].startswith('net') and
          (qid=='Solid166' or o['points'][0] in ('T','L','R','F','H','Z'))]
    def p(v): return tuple(scene['points'][v] if isinstance(v,str) else v)
    edges={frozenset(map(p,o['points'])):o for o in objs}
    vertices=set(v for e in edges for v in e)
    assert len(vertices)==6 and len(edges)==12
    center=tuple(sum(v[i] for v in vertices)/6 for i in range(3))
    distances=[sum((a-b)**2 for a,b in zip(*tuple(e))) for e in edges]
    assert max(distances)-min(distances)<1e-12
    assert all(sum(v in e for e in edges)==4 for v in vertices)
    faces=[f for f in combinations(vertices,3) if all(frozenset(e) in edges for e in combinations(f,2))]
    assert len(faces)==8
    front={}
    for f in faces:
        normal=cross(sub(f[1],f[0]),sub(f[2],f[0]))
        if dot(normal,sub(f[0],center))<0:normal=neg(normal)
        front[frozenset(f)]=dot(normal,scene['projection']['toward_viewer'])>0
    audit=[]
    for e,o in edges.items():
        adjacent=[f for f in front if e<=f]
        expected='visible' if any(front[f] for f in adjacent) else 'hidden'
        audit.append({'object':o['id'],'frozen':o['visibility'],'computed_convex_edge_visibility':expected,
                     'matches':expected==o['visibility']})
    assert all(v['matches'] for v in audit)
    return {'vertices':canon(vertices),'center':center,'edge_length_squared_min_max':[min(distances),max(distances)],
            'convex_faces':len(faces),'projection':scene['projection'],'frozen_visibility':scene['visibility'],
            'visibility_checks':audit,'world_projection_and_visibility_audited_separately':True}

def proof166():
    scene=load(PROJECT/'SolidGeometry/dataset_generator/scenes/Solid166.json')
    faces={o['id']:[tuple(p[:2]) for p in o['points']] for o in scene['objects'] if o['type']=='face'}
    eq={k:[math.dist(a,b) for a,b in combinations(f,2)] for k,f in faces.items()}
    assert all(abs(d-1)<1e-14 for ds in eq.values() for d in ds)
    fm,steps=fold(faces,'netface0',[(1,0,0),(0,1,0),(0,0,1)])
    by_flat={}
    for m in fm.values():
        for p,v in m.items():
            assert p not in by_flat or by_flat[p]==v
            by_flat[p]=v
    edges={o['id']:[tuple(p[:2]) for p in o['points']] for o in scene['objects'] if o['id'].startswith('netedge')}
    edge_world={k:canon(by_flat[p] for p in vs) for k,vs in edges.items()}
    labels={'1':'netedge11','2':'netedge9','3':'netedge13','4':'netedge2','5':'netedge4','x':'netedge15'}
    tests={k:{'target':v,'flat_endpoints':edges[v],'folded_endpoints':edge_world[v],
               'coincides_with_x':edge_world[v]==edge_world[labels['x']]} for k,v in labels.items() if k!='x'}
    assert [k for k,v in tests.items() if v['coincides_with_x']]==['5']
    proof={'question_id':'Solid166','method':'Independent convex octahedron adjacent-face propagation from actual formal eight net faces.',
        'mathematical_basis':'A regular octahedron is conv{+/-e1,+/-e2,+/-e3}. A triangular face uses one vertex on each axis. Across a fixed edge the unique other face has the negative of the former third vertex. A connected net determines every face after any seed basis; any other convex folding is a global octahedral isometry, so seam equality is invariant.',
        'net_faces':faces,'equilateral_side_lengths':eq,'fold_steps':steps,
        'folded_faces':{f:[{'flat':p,'world':v} for p,v in m.items()] for f,m in fm.items()},
        'all_net_edge_endpoints':edge_world,'target_x':{'edge':'netedge15','flat':edges['netedge15'],'world':edge_world['netedge15']},
        'exhaustive_numbered_edge_test':tests,'derived_unique_answer':'5','formal_answer_used_as_proof':False,
        'world_projection_visibility':audit_solid('Solid166',scene),
        'human_semantics':{'number_labels':'1..5 are edge identifiers, not lengths.',
            'edge_color_reading':'A colored paper boundary is still the same physical edge. The question imposes no requirement that equal-colored sides must meet or that unlike-colored sides cannot meet. All numbered sides remain permissible answers; the two endpoint identities decide.',
            'no_missing_color_option_issue':'There are no alternative result pictures whose printed ink must match the source. The requested quantity is an edge identifier on this same net.',
            'geometry_unchanged':True}}
    save(OWN/'Solid166/primary_math.json',proof,exclusive=True)
    print('Solid166 exact edge tests',json.dumps(tests,ensure_ascii=False))

def proof240():
    scene=load(PROJECT/'SolidGeometry/dataset_generator/scenes/Solid240.json')
    points={k:tuple(v[:2]) for k,v in scene['points'].items() if k.startswith('net(')}
    ed={frozenset(o['points']) for o in scene['objects'] if o['type']=='segment' and o['points'][0] in points and o['points'][1] in points}
    triangles=[c for c in combinations(points,3) if all(frozenset(e) in ed for e in combinations(c,2))]
    assert len(triangles)==8
    # Independent centroid binding to the actual frozen source labels, not saved solver mappings.
    faces={}
    for tri in triangles:
        coords=[points[k] for k in tri]
        center=tuple(sum(v[i] for v in coords)/3 for i in range(2))
        matches=[o['text'] for o in scene['labels'] if math.dist(center,scene['points'][o['anchor']][:2])<1e-14]
        assert len(matches)==1
        faces[matches[0]]=coords
    qapex=points['net(3, 0.8660254037844386)']; qleft=points['net(2.5, 0)']; qright=points['net(3.5, 0)']
    initial_map={qapex:(0,0,1),qleft:(-1,0,0),qright:(0,1,0)}
    fm,steps=fold(faces,'Q',[initial_map[p] for p in faces['Q']])
    adjacent={k for k,m in fm.items() if k!='Q' and len(set(m.values())&set(fm['Q'].values()))==2}
    assert adjacent=={'1','2','6'}
    # Three orientation-preserving octahedron symmetries preserve Q's face as a set.
    # S sends Q's vertices z -> -x -> y -> z; S^3=I, det(S)=+1.
    def S(v): return (-v[2],-v[0],v[1])
    symmetries=[]
    target={(0,0,1),(0,1,0),(1,0,0)} # displayed T,H,R face
    for i in range(3):
        def transform(v):
            for _ in range(i): v=S(v)
            return v
        transformed={k:{transform(v) for v in m.values()} for k,m in fm.items()}
        assert transformed['Q']==set(fm['Q'].values())
        answer=next(k for k,v in transformed.items() if v==target)
        symmetries.append({'power':i,'matrix_columns':[transform(v) for v in ((1,0,0),(0,1,0),(0,0,1))],
            'Q_flat_vertex_to_display_vertex':[
                {'flat':p,'canonical':transform(v),'display':{(0,0,1):'T',(-1,0,0):'L',(0,1,0):'H'}[transform(v)]} for p,v in fm['Q'].items()],
            'displayed_Q_face':['T','L','H'],'right_rear_face':['T','H','R'],'right_face_number':answer})
    assert {d['right_face_number'] for d in symmetries}=={'1','2','6'}
    frozen=load(PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid240/scene.json')['semantic_models'][0]
    assert frozen['Q_apex_maps_to_T'] is True
    derived={k:{str(p):v for p,v in m.items()} for k,m in fm.items()}
    report={'question_id':'Solid240','formal_correct_answer':'1','formal_original_not_changed':True,
        'independent_net_faces_from_segment_graph':faces,'fold_steps':steps,'independent_folded_faces':derived,
        'Q_adjacent_faces':sorted(adjacent),'world_projection_visibility':audit_solid('Solid240',scene),
        'frozen_internal_orientation_assumption':{'path':'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid240/scene.json',
           'Q_apex_maps_to_T':True,'conditional_answer':'1','verified_independently':True,
           'not_visible_to_solver':'The named T,L,H,R are internal construction IDs and do not occur in the delivered question or image.'},
        'counterexample_symmetries':symmetries,
        'binding_issue':'Q is a face label in a transparent wireframe. Neither net Q vertex nor corresponding right-side vertex has a displayed label, arrow or other orientation marker. A regular triangular face has a threefold stabilizer. The three proper rotations above keep the Q face at the same depicted T,L,H location but exchange its neighboring faces at T,H,R. The arrow between drawings indicates folding, not a labelled vertex correspondence.',
        'glyph_orientation_assessment':'Ordinary geometric face labels are typeset upright at their anchors, not literal affine images of physically printed glyphs. The canonical redraw stores Q as vertex/text annotation and applies a page-point offset. Treating Q as a physically oriented ink mark could select an orientation, but that is not an explicit paper-print instruction and is a competing interpretation, so it does not establish unambiguous human uniqueness.',
        'gate_decision':'HOLD_ORIGINAL_ORIENTATION_UNIQUENESS',
        'reason':'Original mathematical uniqueness for the visible question/PNG has not been established: 1 is correct after assuming Q apex -> T, while 6 and 2 are achievable under proper rotations preserving the labelled Q face. No color design may add that missing datum as an unannounced new condition.',
        'API_calls':0,'new_special_candidate':None,'PRIMARY_second_review_user_Pass_Collect':False}
    save(OWN/'Solid240/primary_math_and_orientation_hold.json',report,exclusive=True)
    print('Solid240 orientation counterexamples',json.dumps(symmetries,ensure_ascii=False))

if __name__=='__main__':
    proof166();proof240()
