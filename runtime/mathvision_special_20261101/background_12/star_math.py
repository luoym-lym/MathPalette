from tools_local import *
import itertools
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def signed(p):return sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p)))/2 if p else 0
def area(p):return abs(signed(p))
def intersect(a,b,c,d):
    u=[b[0]-a[0],b[1]-a[1]];v=[d[0]-c[0],d[1]-c[1]];den=u[0]*v[1]-u[1]*v[0]
    if abs(den)<1e-12:return None
    t=((c[0]-a[0])*v[1]-(c[1]-a[1])*v[0])/den
    return [a[0]+t*u[0],a[1]+t*u[1]]
def clip(p,q):
    if signed(q)<0:q=list(reversed(q))
    for i,a in enumerate(q):
        b=q[(i+1)%len(q)];result=[]
        if not p:break
        for j,c in enumerate(p):
            d=p[(j+1)%len(p)];ci=cross(a,b,c)>=-1e-10;di=cross(a,b,d)>=-1e-10
            if ci:result.append(c)
            if ci!=di:
                xy=intersect(c,d,a,b)
                if xy is not None:result.append(xy)
        p=result
    return p
def ears(p):
    p=p[:] if signed(p)>0 else list(reversed(p));out=[]
    while len(p)>3:
        found=False
        for i in range(len(p)):
            a,b,c=p[i-1],p[i],p[(i+1)%len(p)]
            if cross(a,b,c)<=1e-10:continue
            if any(all(cross(x,y,z)>=-1e-10 for x,y in [(a,b),(b,c),(c,a)]) for j,z in enumerate(p) if j not in {(i-1)%len(p),i,(i+1)%len(p)}):continue
            out.append([a,b,c]);p.pop(i);found=True;break
        assert found,'ear triangulation failed'
    out.append(p);return out
meta=read(HERE/'Plane230/context.json');star=meta['objects'][0]['geometry']['points'];partition=ears(star)
def overlap(p):return sum(area(clip(p,t)) for t in partition)
tips=star[::2];tiptests=[]
for ids in itertools.combinations(range(5),3):
    p=[tips[i] for i in ids];outside=area(p)-overlap(p);tiptests.append({'tip_indices':ids,'outside_area':outside});assert outside>1e-8
lines=[(star[2*i],star[(2*i+1)%10]) for i in range(5)];candidates=[]
for ids in itertools.combinations(range(5),3):
    pts=[intersect(*lines[ids[i]],*lines[ids[(i+1)%3]]) for i in range(3)]
    if any(p is None for p in pts) or area(pts)<1e-9:continue
    if abs(area(pts)-overlap(pts))<1e-8:candidates.append({'support_lines':ids,'triangle':pts})
def union(ps):
    total=0
    for n in range(1,len(ps)+1):
        for group in itertools.combinations(ps,n):
            p=group[0]
            for q in group[1:]:p=clip(p,q)
            total+=((-1)**(n+1))*area(p)
    return total
witness=None
for group in itertools.combinations(candidates,3):
    u=union([t['triangle'] for t in group])
    if abs(u-area(star))<1e-8:witness={'triangles':group,'union_area':u};break
assert witness
write(HERE/'Plane230/three_triangle_proof.json',{'star_area':area(star),'ear_triangulation':partition,'all_ten_three_tip_hulls_have_positive_outside_area':tiptests,'lower_bound':'Every union triangle must be contained in the source star. Each convex hull of three of its five tips has positive area outside the star, so one triangle can contain at most two tips. Two triangles cover at most four tips. At least three are necessary.','construction_method':'Intersect triples of the five original supporting boundary lines, retain triangles wholly inside the star using exact convex clipping against an ear triangulation, then check three-triangle union area by inclusion/exclusion.','interior_candidate_triangles':candidates,'three_triangle_cover':witness,'upper_bound':'All witness triangles are contained in the original star and their union has the full star area. Hence their union equals the complete closed star region. Three suffice.','unique_minimum':3,'numerical_tolerance':1e-8})
print('star proof: lower3 upper3',flush=True)
