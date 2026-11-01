from tools04 import *
import math
def load_scene(qid):return json.loads((ROOT/'PlaneGeometry/dataset_generator/scenes'/f'{qid}.json').read_text(encoding='utf-8-sig'))
def multiply(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
s=load_scene('Plane225');p=s['points'];objects={o['id']:o for o in s['objects']}
matrices=[];axes=[]
for edge in ['mirror_edge_2','mirror_edge_3']:
    a,b=[p[k] for k in objects[edge]['points']];v=[b[0]-a[0],b[1]-a[1]];norm=math.hypot(*v);u=[v[0]/norm,v[1]/norm]
    matrices.append([[2*u[i]*u[j]-(i==j) for j in range(2)] for i in range(2)]);axes.append({'object_id':edge,'endpoints':[a,b],'direction_degrees_mod180':math.degrees(math.atan2(v[1],v[0]))%180})
combined=multiply(matrices[1],matrices[0]);errors={letter:max(abs(combined[i][j]-objects[f'option{letter}_butterfly']['matrix'][i][j]) for i in range(2) for j in range(2)) for letter in 'ABCDE'}
assert [k for k,v in errors.items() if v<1e-12]==['B']
out={'Plane225':{'geometric_axes_from_frozen_endpoints':axes,'reflection_matrices':matrices,'first_to_third_composition':combined,'maximum_entry_error_against_each_option':errors,'unique_answer':'B','asymmetry':'Allsixdistinctanimalidentities and their poses distinguish rotations/reflections; computation uses frozenedgecoordinates, not the answerfield.'}}
out['Plane238']={'formula':'6*(r-1)+c with r from top; orbit under r->7-r,c->7-c','actual_orbit':sorted({6*(r-1)+c for r in [3,4] for c in [2,5]}),'false_marked_orbit':sorted({6*(r-1)+c for r in [3,4] for c in [3,4]}),'actual_intermediate_column':5,'marked_intermediate_column':4,'unique_answer':'C'}
out['Plane240']={'holes_hour_positions':[1,5],'hole_separation_degrees':120,'choice_minimum_hour_separations':{k:min(abs(a-b),12-abs(a-b)) for k,(a,b) in {'A':(4,9),'B':(5,10),'C':(5,9),'D':(6,9),'E':(7,12)}.items()},'unique_answer':'C'}
for qid,prefix in [('Plane197','path'),('Plane258','black_path'),('Plane314','thick_snake')]:
    scene=load_scene(qid);lengths=[]
    for o in scene['objects']:
        if o['id'].startswith(prefix):
            a,b=o['points'];lengths.append(math.dist(a,b))
    out[qid]={'segment_lengths_frozen_display_units':lengths,'sum':sum(lengths),'length_cm_or_dm':sum(lengths)*(20 if qid!='Plane197' else 1),'unique_answer':'C'}
out['Plane332']={'reassembled_horizontal_decomposition':[13,11+13],'x':13+11+13,'unique_answer':37}
out['Plane322']={'outer_radius_cm':3,'inner_radius_cm':2,'outer_diameter_cm':6,'successive_centres_cm':4,'chain_length_cm':170,'number_of_rings':(170-6)/4+1}
write(HERE/'primary_mathematical_audit.json',out)
print(json.dumps({k:v.get('unique_answer',v.get('number_of_rings')) for k,v in out.items()},ensure_ascii=False))
