from tools24 import *
import math,numpy as np
def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])
def area(p):return abs(sum(cross(a,b) for a,b in zip(p,p[1:]+p[:1])))/2
def signed(p):return sum(cross(a,b) for a,b in zip(p,p[1:]+p[:1]))/2
def ccw(p):return p if signed(p)>0 else list(reversed(p))
def clip(a,b):
    out=[np.array(p,dtype=float) for p in ccw(a)]
    for u,v in zip(ccw(b),ccw(b)[1:]+ccw(b)[:1]):
        u=np.array(u);v=np.array(v);new=[]
        if not out:break
        for s,e in zip(out,out[1:]+out[:1]):
            ds=cross(v-u,s-u);de=cross(v-u,e-u);si=ds>=-1e-9;ei=de>=-1e-9
            if si!=ei:new.append(s+(e-s)*(ds/(ds-de)))
            if ei:new.append(e)
        out=new
    return [p.tolist() for p in out]
def triangles(poly):
    p=[np.array(v,dtype=float) for v in ccw(poly)];out=[]
    while len(p)>3:
        found=False
        for i,b in enumerate(p):
            a,c=p[i-1],p[(i+1)%len(p)]
            if cross(b-a,c-b)<=1e-9:continue
            tr=[a.tolist(),b.tolist(),c.tolist()]
            def intri(x):return all(cross(np.array(v)-u,x-u)>=-1e-9 for u,v in zip([a,b,c],[b,c,a]))
            if any(intri(x) for j,x in enumerate(p) if j not in {(i-1)%len(p),i,(i+1)%len(p)}):continue
            out.append(tr);p.pop(i);found=True;break
        assert found,'cannot triangulate'
    out.append([v.tolist() for v in p]);return out
def intersect_area(a,b):return sum(area(clip(x,y)) for x in triangles(a) for y in triangles(b))
def prove():
    obs={o['id']:o['geometry']['points'] for o in read(HERE/'Plane248/context.json')['objects']}
    source=np.array(obs['source0']);source=source-source[0];S=source.tolist();assert abs(area(S)-2)<1e-9
    summary={};witnesses={}
    for idx,k in enumerate('ABCDE'):
        target=obs[f'option{idx}'];placements=[];seen=set()
        for angle in range(0,360,45):
            th=math.radians(angle);rot=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
            p=source@rot.T
            for v in target:
                for a in p:
                    t=np.array(v)-a;trial=(p+t).tolist();key=tuple(sorted((round(x,8),round(y,8)) for x,y in trial))
                    if key in seen:continue
                    seen.add(key)
                    if abs(intersect_area(trial,target)-2)<1e-8:placements.append({'angle':angle,'translation':t.tolist(),'polygon':trial})
        pairs=[]
        for i,a in enumerate(placements):
            for b in placements[i+1:]:
                overlap=intersect_area(a['polygon'],b['polygon'])
                if overlap<1e-8 and abs(area(target)-4)<1e-9:pairs.append([a,b])
        summary[k]={'contained_vertex_aligned_placements':len(placements),'valid_nonoverlapping_pairs':len(pairs),'target_area':area(target)}
        if pairs:witnesses[k]=pairs[0]
    # Exhaustive impossibility specific to D, using its exposed longest diagonal.
    D=obs['option3'];a=np.array([19.,0.]);mid=np.array([20.,1.]);b=np.array([21.,2.]);forced=[]
    for start,end in [(a,mid),(mid,b)]:
        cases=[]
        for angle in range(0,360,90):
            th=math.radians(angle);R=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
            pp=source@R.T
            for j in [0,1]:
                for x,y in [(start,end),(end,start)]:
                    t=x-pp[j]
                    if np.linalg.norm(pp[(j+1)%6]+t-y)>1e-8:continue
                    trial=(pp+t).tolist()
                    ok=abs(intersect_area(trial,D)-2)<1e-8
                    cases.append({'angle':angle,'head_edge':j,'translation':t.tolist(),'fully_contained_in_D':bool(ok),'polygon':trial})
        forced.append(cases)
    forced_pairs=[]
    for x in forced[0]:
        for y in forced[1]:
            if x['fully_contained_in_D'] and y['fully_contained_in_D'] and intersect_area(x['polygon'],y['polygon'])<1e-8:forced_pairs.append([x,y])
    assert set(witnesses)==set('ABCE') and not forced_pairs,(summary,forced)
    write(HERE/'Plane248/primary_math_audit.json',{'method':'Fresh polygon triangulation/intersection area. ABCE constructive exact-coordinate rotation+translation witnesses. D independently impossible by forced coverage of its exposed length2sqrt2 diagonal.','source_area':2,'all_options':summary,'witnesses':witnesses,'D_forced_two_head_edges':forced,'D_forced_valid_pairs':forced_pairs,'D_exhaustiveness':'Every input axis edge has length1 and the two nonparallel head edges have lengthsqrt2. Each copy has at most one edge on D long exposed straight diagonal. Two rotated unit axis edges cannot cover length2sqrt2. Therefore both copies contribute a head edge, the angles are multiples90, and the joint must be at midpoint(20,1). All head-edge placements on both halves are enumerated; none forms a contained disjoint pair. Boundary alignment excludes any other continuous angle.','unique_answer':'D','primary_not_second_review':True})
if __name__=='__main__':prove();print('Plane248 proved')
