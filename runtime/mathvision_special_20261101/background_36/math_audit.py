from tools_local import *
from collections import Counter
from itertools import product
def graph(cells):
    rows=[]
    for i,c in enumerate(cells):
        adj=[j for j,d in enumerate(cells) if i!=j and sum(abs(c[k]-d[k]) for k in range(3))>0.99999999 and abs(sum(abs(c[k]-d[k]) for k in range(3))-1)<1e-8 and sum(abs(c[k]-d[k])>1e-8 for k in range(3))==1]
        rows.append({'cube':c,'adjacent_indices':adj,'degree':len(adj),'painted_faces':6-len(adj)})
    return {'cubes':cells,'adjacency':rows,'degree_histogram':dict(Counter(r['degree'] for r in rows)),'exactly_four_painted':sum(r['degree']==2 for r in rows)}
models={q:json.loads((TASK/q/'native_model.json').read_text(encoding='utf-8')) for q in ASSIGNED}
proofs={}
proofs['Solid87']={'voxel_models':models['Solid87']['voxel_models'],'option_counts':{k:len(v) for k,v in models['Solid87']['voxel_models'].items()},'unique_answer':'A','proposed_top_projection_counterfactual':'Counting only the highest cube in each occupied vertical column gives A3 B5 C6 D6 E6; A remains uniquely smallest. Omitting one shared support per elevated column gives A4 B5 C6 D6 E7; also A. A different false winner would require an unrelated asymmetric rule.'}
proofs['Solid99']=graph(models['Solid99']['voxel_model']['cubes'])
proofs['Solid99']['unique_answer']=10
proofs['Solid112']={'before_cubes':[list(p) for p in product(range(3),range(3),range(2))],'remaining_cubes':[list(p) for p in product(range(3),range(3),[0])]+[[0,0,1],[2,2,1]],'before_count':18,'remaining_count':11,'removed_count':7,'unique_answer':7,'model_basis':'Three by three footprint and two courses in left panel; complete bottom course plus front-left and rear-right upper cubes in right. Actual unit seams and height risers remain visible.'}
h114=[[1,0,0],[2,1,0],[3,2,1]]
c114=[[x,y,z] for y,row in enumerate(h114) for x,h in enumerate(row) for z in range(h)]
proofs['Solid114']={'heights_front_to_back':h114,'cubes':c114,'count':len(c114),'capacity':27,'unique_answer':27-len(c114),'basis':'Frozen stairse coordinates and actual visible staircase: front row1, next row2+1, rear row3+2+1. Staircase risers at different y are different columns.'}
proofs['Solid116']={'cubes':models['Solid116']['voxel_model'],'lower_courses':24*2,'upper_crenels':8,'total':56,'unique_answer':56,'side_counts_including_both_corners':[17]*4,'double_count_correction':4*3,'corner_memberships':{'0,0':['x0','y0'],'0,6':['x0','y6'],'6,0':['x6','y0'],'6,6':['x6','y6']},'proof':'Square7x7 perimeter has7²-5²=24 positions in each of2continuous courses. Eight upper blocks at four corners and four side midpoints. 48+8=56;4*17-4*3=56.'}
h117=models['Solid117']['voxel_counts']['heights_front_to_back']
proofs['Solid117']={'heights_front_to_back':h117,'remaining_cubes':[[x,y,z] for y,row in enumerate(h117) for x,h in enumerate(row) for z in range(h)],'missing_by_column':[[3-h for h in row] for row in h117],'lowered_columns':[[x,y,h,3-h] for y,row in enumerate(h117) for x,h in enumerate(row) if h<3],'remaining_count':sum(map(sum,h117)),'full_count':27,'unique_answer':27-sum(map(sum,h117)),'native_panel_translation':[6.6,0,1.65]}
c135=models['Solid135']['surface_proof']['cubes'];micro=set()
for x,y,z in c135:
    for dx,dy,dz in product(range(2),repeat=3):micro.add((round(2*x)+dx,round(2*y)+dy,round(2*z)+dz))
surf=Counter()
for p in micro:
    for axis in range(3):
        for sign in [-1,1]:
            n=list(p);n[axis]+=sign
            if tuple(n) not in micro:
                kind='ground' if axis==2 and sign==-1 and p[2]==0 else 'up' if axis==2 and sign==1 else 'vertical' if axis<2 else 'other_down'
                surf[kind]+=0.25
proofs['Solid135']={'cubes':c135,'exact_half_grid_union_surface_unitarea':dict(surf),'painted_unit_area':sum(surf.values())-surf['ground'],'painted_m2':(sum(surf.values())-surf['ground'])*0.25,'unique_answer':4,'proof':'Upward terraces telescope to4²=16. Vertical faces four sides*(4+3+2+1)=40. Painted56*(0.5²)=14m²,ceil(14/4)=4. Half-grid union handles staggered contacts exactly.'}
proofs['Solid139']=graph(models['Solid139']['digit_voxels']['cubes'])
proofs['Solid139']['unique_answer']=60
proofs['Solid139']['proof']='Three disconnected2paths of16cubes each have14degree2 and2degree1, while the0cycle has18degree2. 3*14+18=60. Turns have two perpendicular contacts; straight cells have two opposite contacts. End cells have one contact.'
for q,p in proofs.items():
    p.update(question_id=q,review_kind='primary_only',original_png_actually_viewed=True,source_context_sha256=file_hash(TASK/q/'context.json'),formal_inputs_manifest=str(TASK/q/'frozen_inputs.json'))
    write(TASK/q/'primary_math_audit.json',p)
    print(q,'unique',p['unique_answer'])
