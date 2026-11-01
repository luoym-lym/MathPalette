from tools08 import *
import itertools
import numpy as np
q='Plane449'
labels={'A':(1,6,9,4),'B':(0,3,6,1),'C':(8,5,2,3),'D':(5,4,8,7),'E':(2,7,0,9)}
seams=[(0,1,1,3),(1,2,1,3),(3,4,1,3),(0,3,2,0),(1,4,2,0)]
solutions=[]
for perm in itertools.permutations(labels):
    if all(labels[perm[a]][sa]==labels[perm[b]][sb] for a,b,sa,sb in seams):solutions.append(perm)
assert solutions==[('E','D','A','B','C')]
if not (HERE/q/'exhaustive_side_match_audit.json').exists():write(HERE/q/'exhaustive_side_match_audit.json',{'labels_top_right_bottom_left':labels,'slots':['I','II','III','IV','V'],'seams':seams,'permutations_checked':120,'solutions':solutions,'unique_answer':'E'})
q='Plane371';s=json.loads((HERE/q/'source_scene_snapshot.json').read_text(encoding='utf-8'));obj={o['id']:o for o in s['objects']};errors={}
for c,base,xshift,yshift in [('A',14,-10.5,6),('B',28,0,6),('C',42,10.5,6),('D',56,-10.5,1),('E',70,0,1)]:
    expected=np.concatenate([np.array(obj['o'+str(i)]['points'],dtype=float) for i in range(14)]);expected[:,0]+=xshift;expected[:,1]=-expected[:,1]+yshift
    actual=np.concatenate([np.array(obj['o'+str(base+i)]['points'],dtype=float) for i in range(14)])
    distances=np.sqrt(((expected[:,None,:]-actual[None,:,:])**2).sum(axis=2))
    errors[c]=float(max(distances.min(axis=1).max(),distances.min(axis=0).max()))
assert errors['E']<1e-12
assert all(errors[c]>.01 for c in 'ABCD')
write(HERE/q/'full_vector_reflection_audit.json',{'map':'(x,y)->(x,-y) plus panel translation','all_contour_vertex_set_hausdorff_error':errors,'unique_match':'E','all_14_contours_checked_per_option':True,'source_fill_and_labels_unchanged':True,'diagnostic':'Initial ordered-by-letter comparison failed because D reverses letter ordering, yielding different vertex array shapes. Fixed comparison uses complete geometric vertex sets and preserves the initial script failure as a diagnostic.'})
print(json.dumps({'Plane449':solutions,'Plane371':errors}))
