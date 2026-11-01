from tools import *
import itertools,collections,numpy as np,math
notes=read(ROOT/'provenance/source_notes.json')
ev={q:notes[q].get('geometry_notes',{}).get('additional_model_evidence',{}) for q in ASSIGNED}
def adjacency(cells):
    cells=[tuple(round(float(t),8) for t in c) for c in cells]
    return [sum(abs(sum(abs(a-b) for a,b in zip(c,d))-1)<1e-7 for d in cells) for c in cells]
def surface(boxes):
    axes=[sorted({float(b[k][i]) for b in boxes for k in ('min','max')}) for i in range(3)]
    occ=set()
    for ix in itertools.product(*(range(len(a)-1) for a in axes)):
        mid=[(axes[d][ix[d]]+axes[d][ix[d]+1])/2 for d in range(3)]
        if any(all(b['min'][d]<mid[d]<b['max'][d] for d in range(3)) for b in boxes):occ.add(ix)
    total=0;bottom=0
    for ix in occ:
        for d in range(3):
            for sign in (-1,1):
                other=list(ix);other[d]+=sign
                if tuple(other) in occ:continue
                area=math.prod(axes[k][ix[k]+1]-axes[k][ix[k]] for k in range(3) if k!=d);total+=area
                if d==2 and sign==-1 and axes[2][ix[2]]==0:bottom+=area
    return {'full_surface_area':total,'bottom_on_ground_area':bottom,'exposed_excluding_ground':total-bottom,'method':'Exact coordinate-grid union of frozen axis-aligned boxes; partly overlapping contacts counted by subrectangles.'}
proof={}
for q,key in [('Solid139','digit_voxels'),('Solid113','voxel_model')]:
    cells=ev[q][key]['cubes'];degrees=adjacency(cells);proof[q]={'cube_count':len(cells),'degree_histogram':dict(collections.Counter(degrees)),'glued_face_pairs':sum(degrees)//2,'total_exterior_unit_faces':6*len(cells)-sum(degrees),'exactly_four_painted_faces':degrees.count(2)}
assert proof['Solid139']['exactly_four_painted_faces']==60
assert proof['Solid113']['total_exterior_unit_faces']==36
for q in ['Solid224','Solid232','Solid226','Solid231']:
    boxes=ev[q]['solid_models'];proof[q]=surface(boxes)
    if q in ['Solid232','Solid231']:
        cells=[b['min'] for b in boxes];degrees=adjacency(cells);proof[q].update(cube_count=len(cells),degree_histogram=dict(collections.Counter(degrees)),glued_face_pairs=sum(degrees)//2,exactly_four_painted_faces=degrees.count(2))
assert proof['Solid224']['exposed_excluding_ground']==33
assert proof['Solid232']['exactly_four_painted_faces']==6
assert proof['Solid231']['full_surface_area']==26
assert proof['Solid226']['full_surface_area']==2*(1*9+1*3+9*3)
boxes=[{'min':c,'max':[c[0]+1,c[1]+1,c[2]+1]} for c in ev['Solid135']['surface_proof']['cubes']]
proof['Solid135']={**surface(boxes)};proof['Solid135']['paint_m2']=proof['Solid135']['exposed_excluding_ground']/4;proof['Solid135']['cans']=math.ceil(proof['Solid135']['paint_m2']/4)
assert proof['Solid135']['cans']==4
rots=[]
for p in itertools.permutations(range(3)):
    for signs in itertools.product([-1,1],repeat=3):
        mat=np.zeros((3,3),dtype=int)
        for i in range(3):mat[i,p[i]]=signs[i]
        if round(np.linalg.det(mat))==1:rots.append(mat)
def norm(cells):
    a=np.array(cells,dtype=int);a=a-a.min(axis=0);return sorted(map(tuple,a.tolist()))
for q in ['Solid147','Solid190']:
    if q=='Solid147':
        p=ev[q]['piece_cells'];occupied=[*p['light'],*p['dark']];full=list(itertools.product(range(3),range(2),range(2)));options=dict(zip('ABCDE',p['options']))
    else:
        p=ev[q];occupied=[r['cube'] for r in p['piece_colors'] if r['material']!='dark'];full=list(itertools.product(range(4),range(2),range(2)));options=p['option_cube_sets']
    target=[list(c) for c in full if list(c) not in occupied]
    matches=[letter for letter,cells in options.items() if any(norm(np.array(cells)@R.T)==norm(target) for R in rots)]
    proof[q]={'other_visible_piece_cells':occupied,'complete_box_cells':full,'target_complement':target,'target_degree_histogram':dict(collections.Counter(adjacency(target))),'proper_rotation_count':len(rots),'option_matches_under_rotations':matches,'source_of_cell_coordinates':'Current frozen scene/material pattern plus additional_model_evidence, checked against actual original PNG. No solver output used in geometric proof.'}
    assert matches==[AD.records[q]['answer']]
gray={tuple(c) for c in ev['Solid86']['voxel_model']['visible_colored_cubes']}
visible={c for c in itertools.product(range(4),range(2),range(3)) if c[1]==0 or c[2]==2 or c[0]==3}
white=visible-gray
proof['Solid86']={'dimensions':[4,2,3],'total_white':12,'visible_colored_cells':sorted(gray),'visible_white_cells':sorted(white),'unique_visible_white_count':len(white),'hidden_white':12-len(white),'red_pair_cubes':[[2,0,2],[2,0,2]],'blue_pair_cubes':[[2,0,1],[2,1,2]]}
assert proof['Solid86']['hidden_white']==2
remaining=[c for c in itertools.product(range(3),range(3),range(3)) if not(c[0]>=1 and c[1]<2 and c[2]>=1)]
proof['Solid125']={**surface([{'min':c,'max':[t+1 for t in c]} for c in remaining]),'original_surface_unit_area':54,'white_cut_planes_unit_areas':[4,4,4],'paint_kg':9*12/54,'remaining_cube_count':len(remaining)}
proof['Solid126']={'original_dimensions':[12,6,8],'original_area':432,'cut_dimensions':[9,6,3],'lost_front_back_area':54,'replaced_top_side_areas':[54,18],'remaining_area':378,'decrease_percent':12.5,'correct_choice':'B'}
proof['Solid156']={'cube_world_edge':3,'counts_width_depth_height':[3,2,6],'shortest_cm':4,'cube_edge_cm':24,'brick_dimensions_cm':[8,12,4],'brick_count':36,'correct_choice':'C'}
for q in ['Solid160','Solid196']:proof[q]={'cube_count':4,'small_face_area_cm2':4,'dimensions_unit_cubes':[2,1,2],'glued_face_pairs':4,'exposed_unit_faces':16,'surface_cm2':64}
proof['Solid109']={'dimensions':[5,4,4],'interior_dimensions':[3,2,2],'blue_inside_count':12}
proof['Solid112']={'original_dimensions':[3,3,2],'original_cube_count':18,'remaining_full_base_layer':9,'remaining_upper_cubes':2,'removed_count':7}
proof['Solid82']={'columns':6,'cubes_per_column':5,'white_z':[1,3],'white_per_column':2,'total_white':12}
proof['Solid123']={'total_cube_volume':27,'light_L_count':2,'light_L_unit_volume':5,'dark_bar_count':2,'dark_bar_unit_volume':3,'white_count':27-2*5-2*3,'note':'Source-visible material pattern fixes two5-cubeLs and two3-cube bars; used for prescreen only, no tested candidate or independent tiling claim.'}
proof['Solid124']={'vertical_lengths':[12,12,12],'front_horizontal_parts':[8,4],'depth_length':12,'route_length':60,'invariance':'Front parts a and12-a sum12 at any unchanged route crossing location. Total3*12+12+12=60.'}
write(TASK/'primary_math_audit.json',{'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Primary review only; does not replace NEW independent second review','proofs':proof})
print(json.dumps({q:proof[q] for q in ['Solid224','Solid232','Solid135','Solid147','Solid190','Solid231']},ensure_ascii=False))
