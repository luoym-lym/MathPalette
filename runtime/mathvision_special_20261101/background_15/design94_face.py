from design_tools import *
q='Solid94';proof='For cube[-1,1]^3, the center piece satisfies all eight signed inequalities sx*x+sy*y+sz*z<=1, so equals |x|+|y|+|z|<=1. It is the regular octahedron A. In particular, intersecting the original front face y=-1 with this region forces x=z=0: the square face has only its center remaining, not an octagonal face. Wrong C retains an octagonal original-face remnant, which corresponds to shallower cuts. Both the source square face and distractor octagonal face are already-existing geometry and remain exactly in their original locations. Red outlines add no plane, cut, equality or new physical boundary; the colored polygon on the source is the original cube face, not a proposed cut. A human can still check every specified adjacent vertex and determine the octahedron uniquely.'
p=TASK/q/'face_remnant_proof.json';write(p,{'question_id':q,'proof':proof,'review_kind':'PRIMARY_ONLY'})
src=['givenCB','givenCD','givenDA','givenAB'];dst=['optionC012','optionC1214','optionC1417','optionC1517','optionC153','optionC35','optionC25','optionC02']
objs={o['id']:o for o in source_objects(q)}
assert all(t in objs for t in src+dst)
# Assert each distractor edge is in its actual front plane and perimeter is a closed8-cycle.
from collections import Counter
es=[objs[t]['geometry']['points'] for t in dst];ys={round(p[1],10) for e in es for p in e};assert len(ys)==1
counts=Counter(tuple(p) for e in es for p in e);assert len(counts)==8 and set(counts.values())=={2}
a=[style(t,RED,2) for t in src+dst]
roles=[f'Source front-square boundary {t}; one side of the input face being falsely matched to a retained polygonal original-face remnant.' for t in src]+[f'Existing front octagon perimeter edge {t} in C. Each of its8 edges completes the single specific face-remnant receiver, rather than marking the whole option or its label.' for t in dst]
save_candidate(q,'original_face_to_octagonal_remnant_binding','C',a,roles,'A red closed outline binds the actual source front square face to the existing front octagonal face in C, inviting the false assumption that original cube faces retain area after the specified full-depth cuts.',proof,p)
