from env41 import *
import math
import numpy as np
out=HERE/'Plane427/r41_isosceles_base_angle_frame';p=read(HERE/'Plane427/source_scene_snapshot.json')['points']
p={k:np.array(v) for k,v in p.items()}
def angle(a,b,c):
    u=p[a]-p[b];v=p[c]-p[b]
    return math.degrees(math.acos(float(np.clip((u@v)/np.linalg.norm(u)/np.linalg.norm(v),-1,1))))
values={k:angle(*pts) for k,pts in {'RTV':['R','T','V'],'STV':['S','T','V'],'TSV':['T','S','V'],'RSV':['R','S','V']}.items()}
assert all(abs(values[k]-n)<1e-8 for k,n in {'RTV':70,'STV':130,'TSV':25,'RSV':35}.items())
write(out/'primary_math_supplement.json',{'question_id':'Plane427','role':'designer supplemental primary proof, NOT independent second review','created_at_utc':now(),'exact_source_coordinates':{k:v.tolist() for k,v in p.items()},'numeric_checks_deg':values,'ray_directions_at_T_deg':{k:math.degrees(math.atan2(*(p[k]-p['T'])[::-1])) for k in ('S','R','V')},'equal_radii':{k:float(np.linalg.norm(p[k]-p['T'])) for k in ('R','S','V')},'second_valid_primary_derivation':'RST equilateral and the congruent rotated triangle imply TR=TS=TV. Therefore R,S,V lie on the conceptual circle centered at T. The shown S lies outside the minorRV70-degree arc, so inscribed angleRSV is half70, i.e.35. This is a proof device only; no circle or new radius has been added to the candidate.','why_model25_is_wrong':'The actual rays at T have TV thenTR thenTS in order, so70 and60 are adjacent and sum130. Both frozen responses incorrectly subtract and derive10. Their final25 is a valid preset hit but does not validate the originally forecast omitted-last-subtraction mechanism.','human_unique_answer_unchanged':'Only D35 matches the original mathematical angle; blue equality of ST/TV is true, dottedSV remains dotted, original target arc and70 arc remain clear.','no_new_control_or_solver_call':True,'no_frozen_evidence_changes':True})
print(values)
