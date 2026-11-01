from tools_local import *
import math
meta=json.loads((HERE/'Plane187/context.json').read_text(encoding='utf-8'));oo={o['id']:o for o in meta['objects']}
groups={'shown_step1':range(15,22),'A':range(36,43),'B':range(57,64),'C':range(78,85),'D':range(99,106),'E':range(120,127)}
angles={}
for k,ids in groups.items():
    got=[]
    for i in ids:
        a,b=oo['o'+str(i)]['geometry']['points'];theta=math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]))%180
        if abs(theta-180)<1e-10:theta=0
        got.append(theta)
    angles[k]=got
expected={'shown_step1':21,'A':72,'B':144,'C':36,'D':108,'E':0}
assert all(all(abs(t-expected[k])<1e-10 for t in vals) for k,vals in angles.items())
fits=[n for n in range(1,25) if (21*n)%72==0];assert fits==[24]
write(HERE/'Plane187/exact_return_math_audit.json',{'question_id':'Plane187','source_fullprecision_stripe_angles_mod180':angles,'regular_pentagon_rotational_symmetry_degrees':72,'step_degrees':21,'gcd':math.gcd(21,72),'first_positive_return_step':24,'total_rotation':504,'total_rotation_mod360':144,'unique_matching_choice':'B','wrong_target_C_orientation':36,'colored_source_target_slopes_not_equal':True,'colored_line_pair_role':'Ordered lowerred/upperblue stripe pair carries a proposed rising-orientation correspondence. It is deliberately not an exactangle or same-material-ink condition.','human_unique_answer_unchanged':True,'no_solver_calls':True})
print(json.dumps({'first_return_step':24,'angle_mod360':144,'unique_choice':'B'}))
