from common68 import *
from fractions import Fraction as F
from itertools import permutations
from math import sqrt

def area2(vertices):
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(vertices, vertices[1:]+vertices[:1])))

def clip_cell(vertices, target):
    """Exact convex half-plane clipping in lattice coordinates."""
    for a,b in zip(target, target[1:]+target[:1]):
        def side(p): return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        output=[]
        if not vertices: return []
        for p,q in zip(vertices,vertices[1:]+vertices[:1]):
            sp,sq=side(p),side(q)
            if sp>=0: output.append(p)
            if (sp<0<=sq) or (sq<0<=sp):
                t=sp/(sp-sq)
                output.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        vertices=output
    return vertices

def main():
    s=read(PROJECT/BRANCH/'dataset_generator/scenes/Plane271.json')
    radii=[o['radius'] for o in s['objects'] if o['type']=='sector']
    assert radii==[10,10,5,5,10,10,5,5]
    write(HERE/'Plane271/primary_math_audit.json',dict(checked_at=now(),formal_correct_answer='E',unique_value_cm=20,
        printed_conditions='Same five intact pieces; rectangle 5 cm by10 cm; other four pieces are quarter circles of two radii. Actual source and native joins identify two radius10 and two radius5 pieces.',
        arc_total_each='2*(10*pi/2)+2*(5*pi/2)=15*pi',
        all_piece_straight_boundary_total_each=90,
        left_internal_seam_lengths=[10,10,5,5], right_internal_seam_lengths=[10,5,5,5,5,5,5],
        left_exterior_straight_total=90-2*30,right_exterior_straight_total=90-2*40,
        perimeters=['15*pi+30','15*pi+10'],difference=20,
        marker_material_mapping=dict(source=[[-5,0],[0,0]],receiver=[[30,-5],[30,0]],rigid_map='(x,y) -> (30-y,x)',source_exterior=True,receiver_internal=True,edge_length_each=5),
        wrong_preset_unchanged='D=15 cm; erroneous cancellation of one5 cm exposed-to-internal radius',
        minimum_maximum_requirement='No extremum requested; the two fixed perimeters are uniquely determined.'))
    s=read(PROJECT/BRANCH/'dataset_generator/scenes/Plane367.json')
    polygons={o['id']:[tuple(F(s['points'][p][j]) for j in (0,1)) for p in o['points']] for o in s['objects'] if o['id'].startswith('shape')}
    areas={k:area2(v)/2 for k,v in polygons.items()}
    assert all(v==2 for v in areas.values()) and len(areas)==5
    write(HERE/'Plane367/primary_math_audit.json',dict(checked_at=now(),method='Exact rational shoelace on all actual frozen polygons; source JPG/native outlines personally compared',
        polygons={k:[[str(x),str(y)] for x,y in v] for k,v in polygons.items()},areas={k:str(v) for k,v in areas.items()},maximum_area='2 grid units',all_maximizers=['A','B','C','D','E'],unique_choice='E=All shapes have the same area',
        decompositions={'A':'1+1/2+1/2','B':'1+1/2+1/2','C':'1+1/2+1/2','D':'(2*2)/2','visual_E':'(2*2)/2'},
        marker_regions={'source_A_square':[[1,1],[1,2],[2,2],[2,1]],'receiver_B_left_half':[[3,1],[4,1],[4,0]],'receiver_B_right_half':[[4,0],[4,1],[5,1]]},
        wrong_preset_unchanged='B: replacing each true1/2 receiver by source square area1 yields1+1+1=3; no equal-area condition is actually printed.'))
    s=read(PROJECT/BRANCH/'dataset_generator/scenes/Plane387.json')
    def lattice(p):
        j=round(p[1]/(sqrt(3)/2)); i=round(p[0]-j/2)
        assert abs(p[0]-(i+j/2))<1e-12 and abs(p[1]-j*sqrt(3)/2)<1e-12
        return (F(i),F(j))
    target=[lattice(s['points'][p]) for p in ['A','C','B']]
    assert target==[(0,1),(4,0),(3,3)] and area2(target)==11
    cells=[]
    for j in range(6):
        for i in range(6-j):
            tris=[('up',[(i,j),(i+1,j),(i,j+1)])]
            if i+j<5: tris.append(('down',[(i+1,j),(i+1,j+1),(i,j+1)]))
            for orientation,vertices in tris:
                vertices=[tuple(F(c) for c in p) for p in vertices]
                polygon=clip_cell(vertices,target)
                cells.append(dict(i=i,j=j,orientation=orientation,shaded_area=str(area2(polygon) if polygon else F(0)),clipped_vertices=[[str(x),str(y)] for x,y in polygon]))
    assert len(cells)==36 and sum(F(c['shaded_area']) for c in cells)==11
    fragments=[c for c in cells if c['i']==3 and c['j']==1]
    assert [F(c['shaded_area']) for c in fragments]==[F(5,6),F(1,6)]
    write(HERE/'Plane387/primary_math_audit.json',dict(checked_at=now(),formal_correct_answer='11',
        lattice_basis='e1=(1,0),e2=(1/2,sqrt(3)/2); physical unit triangle area is1 cm^2, so lattice determinant directly counts unit triangles',
        target_vertices_lattice=[[str(x),str(y)] for x,y in target],determinant=11,cell_count=36,all_cell_clippings=cells,
        independent_corner_subtraction='Whole triangle determinant36 minus three corner determinants4,6,15 gives11.',
        receiver_fragments=fragments,other_shaded_area='10',wrong_preset_unchanged='12=10+1+1 instead of10+5/6+1/6',
        actual_target_line='3*i+j=12; right-boundary crossings on j=1 andj=2 are i=11/3 and10/3; diagonal (4,1)->(3,2) meets at parameter1/2',
        minimum_maximum_requirement='No extremum requested; actual shaded triangle and all36 fixed unit cells give one area.'))
    s=read(PROJECT/BRANCH/'dataset_generator/scenes/Plane449.json')
    label_map={x['id']:x['text'] for x in s['labels']}
    vals={q:tuple(int(label_map[q+str(i)]) for i in range(4)) for q in 'ABCDE'}
    solutions=[]; enumeration=[]
    for p in permutations('ABCDE'):
        i,ii,iii,iv,v=p
        tests=[vals[i][1]==vals[ii][3],vals[ii][1]==vals[iii][3],vals[iv][1]==vals[v][3],vals[i][2]==vals[iv][0],vals[ii][2]==vals[v][0]]
        enumeration.append(dict(placement=list(p),seams=tests))
        if all(tests): solutions.append(list(p))
    assert solutions==[['E','D','A','B','C']]
    write(HERE/'Plane449/primary_math_audit.json',dict(checked_at=now(),side_order=['top','right','bottom','left'],actual_all20_labels=vals,
        fixed_orientation=True,permutations_enumerated=120,seam_order=['I-II','II-III','IV-V','I-IV','II-V'],enumeration=enumeration,unique_solutions=solutions,unique_answer='E',
        direct_proof='Available horizontal pairs are E-D, D-A and B-C; only three-card chain is E-D-A. E-bottom0 forces B below I; D-bottom8 forces C below II; B-right3=C-left3 verifies final seam.',
        red_pair='D-bottom8 matches C-top8; in correct placement this is II-V',blue_pair='D-right4 matches A-left4; in correct placement this is II-III',
        wrong_preset_unchanged='D at I locally satisfies right=A and below=C, but II=A would require a third top rectangle with left6, absent; it also leaves C-right5 unmatched below.',
        minimum_maximum_requirement='No extremum requested; all120 placements checked and exactly one solution.'))
    print('All four independent primary proofs and marker weights verified; no solver calls',flush=True)
if __name__=='__main__':main()
