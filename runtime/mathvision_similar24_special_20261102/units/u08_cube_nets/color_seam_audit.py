from worker import *
from fractions import Fraction as F
from itertools import permutations,product
from collections import Counter

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
rotations=[]
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        r=[tuple(signs[i]*int(j==perm[i]) for j in range(3)) for i in range(3)]
        if dot(r[0],cross(r[1],r[2]))==1:rotations.append(r)
assert len(rotations)==24
proof=read(OWN/'Solid193/primary_math_proof.json')
d=OWN/'Solid193'/(sys.argv[1] if len(sys.argv)>1 else 'C02_truthful_diagonal_with_false_strip_analogy')
targets={a['target'] for a in read(d/'plugin.json')['params']['actions']}
results=[]
for n in (1,2,4):
    p=proof['panels'][str(n)];selected=[]
    for t in p['triangles']:
        for s in (0,1):
            if f'net{n-1}triangle{t["index"]}side{s}' in targets:
                selected.append(tuple(map(F,t['folded_vertices'][s])))
    counts=Counter(selected);assert len(counts)==2 and set(counts.values())=={2}
    a,b=counts;missing=tuple(map(F,p['missing_face_normal']))
    assert tuple(x+y for x,y in zip(a,b))==missing
    winners=[r for r in rotations if tuple(dot(row,missing) for row in r)==(0,-1,0) and tuple(dot(row,a) for row in r) in ((F(-1,2),F(-1,2),F(-1,2)),(F(1,2),F(-1,2),F(1,2)))]
    assert winners
    results.append({'net':n,'red_radial_corner_a':list(map(str,a)),'red_radial_corner_b':list(map(str,b)),'two_copies_of_each_radial':True,'proper_cube_rotation_to_source':winners[0],'target_source_diagonal':'cutdiagonal0 from (15,0,6) to (17,0,8), cube side2; translation center(16,1,7)','scale_after_unit_cube':2,'source_and_valid_net_color_compatible':True})
save(d/'literal_color_fold_audit.json',{'created_at':now(),'method':'Exact Fraction corner incidence and exhaustive 24 proper signed-axis cube rotations; no tolerance','valid_nets':results,'invalid_nets':'3 and5 are geometrically invalid regardless of ink; coloring cannot repair occupied-face collisions.','unique_invalid_pair_after_color_preserving_reading':'E:3and5'})
print('all three valid nets exactly match source red diagonal under proper cube rotations')
