from env58 import *
from itertools import product
import math

def track_vector(word):
    # z=exp(i*pi/8), minimal polynomial z^8+1. Chords have common
    # positive length 2*sin(pi/8) and direction z^(2*k+s).
    vec=[0]*8
    k=0
    for s in word:
        exponent=(2*k+s)%16
        vec[exponent%8] += 1 if exponent<8 else -1
        k+=s
    return k,vec

def sample_track(word):
    x=y=theta=0.0
    points=[(x,y)]
    for sign in word:
        initial=theta
        x0,y0=x,y
        for step in range(1,65):
            angle=initial+sign*math.pi/4*step/64
            points.append((x0+sign*(math.sin(angle)-math.sin(initial)),
                           y0+sign*(math.cos(initial)-math.cos(angle))))
        theta+=sign*math.pi/4
        x,y=points[-1]
    return points

def track():
    counts=[]
    constructions=[]
    for n in range(2,13):
        closed=[]
        for tail in product((1,-1),repeat=n-2):
            word=(1,-1)+tail
            turn,vec=track_vector(word)
            if turn%8==0 and not any(vec):
                closed.append(list(word))
        counts.append({'N':n,'words_with_required_opposite_prefix':2**(n-2),
                       'exact_position_and_tangent_closed_words':len(closed)})
        if n==12: constructions=closed
    assert all(v['exact_position_and_tangent_closed_words']==0 for v in counts if v['N']<12)
    assert constructions
    selected=constructions[0]
    save('Plane275/exact_track_proof.json', {'created_at':now(),'method':'Exact cyclotomic chord enumeration, no numerical closure decisions',
        'encoding':'z=exp(i*pi/8), z^8+1=0, chord sign unit z^(2*k+s), k starts zero; prefix +1,-1 fixes the shown S up to rigid motion/reflection',
        'independence':'No stored answer, preset or solver reply used in the enumeration',
        'all_counts':counts,'all_N12_closed_words':constructions,'selected_word':selected,
        'selected_exact_closure':track_vector(selected),'sampled_centerline_for_inspection':sample_track(selected),
        'construction_native_clearance_check_pending':True})
    print(json.dumps({'Plane275':counts,'selected':selected}),flush=True)

def tile_graph(bits):
    # Ports share a vertex exactly when they coincide on a common tile edge.
    edges=[]
    for r in range(4):
        for c in range(4):
            N=('h',r,c); S=('h',r+1,c); W=('v',r,c); E=('v',r,c+1)
            pairs=((N,E),(S,W)) if bits[r*4+c]==0 else ((N,W),(S,E))
            edges.extend((a,b,(r,c,arc)) for arc,(a,b) in enumerate(pairs))
    adj={}
    for i,(a,b,_) in enumerate(edges):
        adj.setdefault(a,[]).append((b,i))
        adj.setdefault(b,[]).append((a,i))
    unused=set(range(32)); components=[]
    while unused:
        ei=next(iter(unused)); pending=[edges[ei][0]]; vertices=set(); used=set()
        while pending:
            v=pending.pop()
            if v in vertices: continue
            vertices.add(v)
            for w,i in adj[v]:
                used.add(i)
                if w not in vertices: pending.append(w)
        unused-=used
        components.append({'arcs':len(used),'edge_indices':sorted(used),
                           'boundary_endpoints':[v for v in vertices if len(adj[v])==1]})
    return edges,components

def tile():
    selected=None
    for bits in product((0,1),repeat=16):
        edges,comps=tile_graph(bits)
        if max(c['arcs'] for c in comps)==22:
            selected=(bits,edges,comps);break
    assert selected
    bits,edges,comps=selected
    proof=['There are 32 quarter-circle arcs, and every one of the 16 external side-midpoint ports has degree 1. Every internal port has degree 2, so there are exactly eight open chain components plus zero or more closed components.',
           'A chain with one arc must connect two external ports in a corner tile. Only the four corner tiles can do this, so at most four chains have one arc; every other open chain has at least two.',
           'If the selected longest component is open, the other seven open chains require at least 4*1+3*2=10 arcs. Thus its length is at most 32-10=22 arcs.',
           'If the selected component is closed, all eight open chains are outside it and require at least 4*1+4*2=12 arcs, leaving at most 20. Therefore no component exceeds 22.',
           'The recorded 4x4 binary tile orientation construction has one 22-arc chain, four 1-arc chains and three 2-arc chains. All edges are the original quarter arcs. This achieves 22*5=110 dm uniquely among the offered numerical values.']
    save('Plane326/exact_tile_proof.json',{'created_at':now(),'independent_upper_bound':proof,
        'tile_orientation_key':'0 joins N-E/S-W; 1 joins N-W/S-E; rows top to bottom',
        'construction_rows':[list(bits[r*4:(r+1)*4]) for r in range(4)],
        'edges':edges,'components':comps,'curve_lengths_sorted':sorted(c['arcs'] for c in comps)})
    print(json.dumps({'Plane326_constructive_counts':sorted(c['arcs'] for c in comps),
                      'orientations':[list(bits[r*4:(r+1)*4]) for r in range(4)]}),flush=True)

if __name__=='__main__':
    if sys.argv[1]=='track':track()
    elif sys.argv[1]=='tile':tile()
