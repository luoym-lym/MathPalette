from tools_local import *
import math,itertools
def poly(qid,oid):
    meta=read(HERE/qid/'context.json');obj=next(o for o in meta['objects'] if o['id']==oid);pts=obj['geometry']['points'];sc=read(ROOT/'PlaneGeometry'/read(HERE/qid/'formal_record.json')['scene'])
    return [sc['points'][p] if isinstance(p,str) else p for p in pts]
def audit244():
    meta=read(HERE/'Plane244/context.json')
    def cells(prefix):
        result=set()
        for o in meta['objects']:
            if o['id'].startswith(prefix):
                xs,ys=zip(*o['geometry']['points'])
                result.update((x,y) for x in range(min(xs),max(xs)) for y in range(min(ys),max(ys)))
        return result
    base=cells('image1_');shapes=set()
    for swap,sx,sy in itertools.product([0,1],[-1,1],[-1,1]):
        c={(sx*(y if swap else x),sy*(x if swap else y)) for x,y in base};mx=min(x for x,y in c);my=min(y for x,y in c);shapes.add(tuple(sorted((x-mx,y-my) for x,y in c)))
    results=[]
    for i in range(2,7):
        target=cells(f'image{i}_');placements=set()
        for shape in shapes:
            ax,ay=shape[0]
            for x,y in target:
                p=frozenset((u+x-ax,v+y-ay) for u,v in shape)
                if p<=target:placements.add(p)
        covers=[]
        for a in placements:
            b=frozenset(target-a)
            if b in placements and tuple(sorted(a))<tuple(sorted(b)):covers.append([sorted(a),sorted(b)])
        results.append({'pattern_ordinal_below_source':i-1,'source_prefix':f'image{i}_','rectangle_count':len(target)//2,'placements':len(placements),'two_block_cover_count':len(covers),'witness':covers[:1]})
    assert [bool(r['two_block_cover_count']) for r in results]==[True,False,True,True,True]
    write(HERE/'Plane244/tiling_math_audit.json',{'source_unit_square_cells':sorted(base),'source_rectangle_count':5,'method':'Enumerate all eight axis-aligned rigid orientations, all integer translations anchored at every target unit-square cell, then exact two-copy disjoint covers. The block outline has axis-aligned exposed boundary, requiring a multiple-of-90-degree orientation. Reflections included conservatively.','results':results,'unique_answer':'4'})
def audit200():
    import numpy as np
    objs=read(HERE/'Plane200/context.json')['objects'];s=np.array([o['geometry']['center'] for o in objs if o['id'].startswith('tri')]);t=np.array([o['geometry']['center'] for o in objs if o['id'].startswith('hex')]);best=0;witness=None;maps=0
    for i,j in itertools.permutations(range(6),2):
        a=s[j]-s[i]
        for k,l in itertools.permutations(range(6),2):
            b=t[l]-t[k]
            if abs(a@a-b@b)>1e-9:continue
            for reflect in [-1,1]:
                us=a/np.linalg.norm(a);ut=b/np.linalg.norm(b);vs=np.array([-us[1],us[0]]);vt=np.array([-ut[1],ut[0]])
                m=np.column_stack((ut,reflect*vt))@np.column_stack((us,vs)).T;out=(s-s[i])@m.T+t[k];count=sum(any(np.linalg.norm(p-q)<1e-8 for q in t) for p in out);maps+=1
                if count>best:best=count;witness={'matrix':m.tolist(),'translation':(t[k]-s[i]@m.T).tolist(),'source_transformed':out.tolist()}
    assert best==4
    write(HERE/'Plane200/overlap_math_audit.json',{'method':'Every rigid alignment retaining at least two centers is determined by an ordered source and target pair and handedness. Enumerate all distance-compatible ordered pairs; include reflections conservatively. Any putative five-center overlap is therefore covered.','evaluated_pair_maps':maps,'maximum_retained_coins':best,'minimum_moves':6-best,'witness':witness})
def audit289():
    source=[poly('Plane289','triangle'+str(i)) for i in range(7)];h=math.sqrt(3)/2;results=[];chosen=None
    for n in range(1,6):
        containing=[]
        for direction in [1,-1]:
            for j in range(-8,9):
                for i in range(-8,9):
                    x=i+j/2;y=j*h;pts=[[x,y],[x+n,y],[x+n/2,y+direction*n*h]]
                    def inside(p):
                        signs=[(pts[(k+1)%3][0]-pts[k][0])*(p[1]-pts[k][1])-(pts[(k+1)%3][1]-pts[k][1])*(p[0]-pts[k][0]) for k in range(3)]
                        return min(signs)>=-1e-8 or max(signs)<=1e-8
                    if all(inside(p) for s in source for p in s):containing.append(pts)
        results.append({'side':n,'containing_triangle_count':len(containing),'first_witness':containing[:1]})
        if n==5:chosen=containing[0]
    assert [bool(r['containing_triangle_count']) for r in results]==[False,False,False,True,True]
    write(HERE/'Plane289/completion_math_audit.json',{'method':'Enumerate integer triangular-lattice translations in a range exceeding the source bounding box by five sides and both upright/downward orientations. A union of unit equilateral triangles with equilateral outer contour has integer side and lattice-parallel sides.','source_triangle_count':7,'results':results,'minimum_added':9,'chosen_nonminimal_triangle':chosen,'nonminimal_added':18})
if __name__=='__main__':
    for f in [audit244,audit200,audit289]:f();print(f.__name__,flush=True)
