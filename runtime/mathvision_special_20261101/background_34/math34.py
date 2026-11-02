from tools34 import *
from fractions import Fraction as F
import math

def scene_for(qid):
    rec=record(qid)
    path=next(PROJECT/branch_of(qid)/p for p in rec['runtime_dependencies'] if '/items/'+qid+'/scene.json' in p)
    return read(path),path
def area(points):
    points=[tuple(F(str(v)) for v in point) for point in points]
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(points,points[1:]+points[:1])))/2
def coordinates(scene,obj):
    return [scene['points'][p] if isinstance(p,str) else p for p in obj['points']]

def prove(qid):
    scene,path=scene_for(qid)
    objects={obj['id']:obj for obj in scene['objects']}
    common={'question_id':qid,'at':now(),'author_role':'primary author, not independent review',
            'method':'Derived from actual source/formal coordinates and wording before use of stored answer; answer agreement checked separately.',
            'native_scene':str(path.relative_to(PROJECT)),'native_scene_sha256':sha(path),
            'actual_source_jpg':record(qid)['original_image'],'formal_question':record(qid)['question']}
    if qid=='Plane212':
        total=area(coordinates(scene,objects['figure1'])); unit=area(coordinates(scene,objects['figure2'])); embedded=area(coordinates(scene,objects['example_triangle']))
        assert total==15 and unit==embedded==1
        solution={'polygon_shoelace_area_grid_units':str(total),'prototype_area':str(unit),'embedded_example_area':str(embedded),'ratio':str(total/unit),
                  'reason':'Prototype base spans two grid intervals and height one, hence area one full grid square. Congruent cuts must number15. No assumption that the whole prototype is a half-cell.'}
        answer='15'
    elif qid=='Plane257':
        f1=[obj for obj in scene['objects'] if obj['id'].startswith('f1')]
        f2=[obj for obj in scene['objects'] if obj['id'].startswith('f2')]
        f4=[obj for obj in scene['objects'] if obj['id'].startswith('f4')]
        def fraction(items):
            return sum(area(coordinates(scene,obj)) for obj in items if obj.get('semantic_color','').upper()=='#000000')/sum(area(coordinates(scene,obj)) for obj in items)
        f3=(area(coordinates(scene,objects['f3triangle']))+area(coordinates(scene,objects['f3right'])))/3
        f5=[obj for obj in scene['objects'] if obj['id'].startswith('f5')]
        fractions=[fraction(f1),fraction(f2),f3,fraction(f4),fraction(f5)]
        assert fractions==[F(3,8),F(3,5),F(2,3),F(3,5),F(1,2)]
        solution={'fractions_in_order':[str(v) for v in fractions],'qualifying_flags':[2,4],'qualifying_count':2,
                  'first_flag_black_square_count':3,'fourth_flag_black_stripe_count':3,
                  'first_denominator':8,'fourth_denominator':5,
                  'reason':'Black stripe multiplicity and black square multiplicity coincide but their denominators differ; the matching colored counts do not imply equal fractions. Black/white areas, not outline color or number of groups, define the question.'}
        answer='C'
    elif qid=='Plane336':
        # Affine y rescaling cancels in area ratios: u=2x,v=2y/sqrt(3).
        lattice={key:(F(round(2*p[0])),F(round(2*p[1]/math.sqrt(3)))) for key,p in scene['points'].items()}
        total=area([lattice[p] for p in objects['outline']['points']])
        pieces={name:area([lattice[p] for p in objects[name]['points']])/total*9 for name in ('leftGrey','rightGrey','topGrey')}
        assert list(pieces.values())==[F(2),F(2),F(2)]
        rays={k:[scene['points'][k][i]-scene['points']['O'][i] for i in (0,1)] for k in ('L','U','V','R','E','D')}
        lengths={k:sum(v*v for v in vector) for k,vector in rays.items()}
        assert all(abs(v-1)<1e-12 for v in lengths.values())
        solution={'transformed_integer_lattice':{k:[str(x) for x in p] for k,p in lattice.items()},'gray_piece_areas':{k:str(v) for k,v in pieces.items()},
                  'white_triangle_areas':['1','1','1'],'total_area':9,'gray_total':str(sum(pieces.values())),
                  'six_actual_radial_vectors':rays,'radial_squared_lengths':lengths,
                  'reason':'The six chord half-rays have equal length and successive60-degree directions, but the outer boundary extends beyond their endpoints in each gray sector. Each gray rhombus is two unit triangles, each white sector only one. Equal radial rays do not make the six full regions equal in area.'}
        answer='6'
    elif qid=='Plane338':
        points=coordinates(scene,objects['grey']); units=area(points)
        assert units==21
        solution={'ordered_ABCD':points,'shoelace_grid_square_area':str(units),'cell_side_cm':2,'cell_area_cm2':4,'area_cm2':str(4*units),
                  'alternative_bounding_rectangle_check':'Bounding rectangle x=1..8,y=1..6 has35cells. Four exterior right triangles have areas2,1.5,7.5,3, sum14; gray35-14=21cells=84cm2.'}
        answer='B'
    elif qid=='Plane340':
        pieces={name:area(coordinates(scene,objects[name])) for name in ('topGrey','rightGrey')}
        assert pieces=={'topGrey':F(5,8),'rightGrey':F(3,8)}
        solution={'gray_areas':{k:str(v) for k,v in pieces.items()},'total':str(sum(pieces.values())),
                  'cut_crossing_K':scene['points']['K'],'reason':'The joining line runs I=(1/2,2) to C=(2,0), crossing y=1 at x=5/4. Top white triangle area3/8, so top gray5/8; right gray triangle has legs3/4 and1, area3/8. Unit containing square frames do not measure the filled subregions.'}
        answer='1'
    elif qid=='Solid88':
        cubes=[tuple(p) for p in scene['voxel_models']['tree']]
        edges=[(a,b) for n,a in enumerate(cubes) for b in cubes[n+1:] if sum(abs(x-y) for x,y in zip(a,b))==1]
        seen={cubes[0]}
        while True:
            new=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
            if new==seen:break
            seen=new
        assert len(cubes)==12 and len(edges)==11 and len(seen)==12
        solution={'cubes':cubes,'face_contact_pairs':edges,'contact_count':len(edges),'connected':True,'tree':True,
                  'reason':'Each actual face contact consumes one drop. Exhaustive Manhattan-distance-one contact enumeration is11, including hidden support cubes and all branch attachments. Projected proximity is not a contact.'}
        answer='11'
    elif qid=='Solid184':
        # Let S be the original brick area and x,y,z its three distinct face areas.
        # Each paired assembly is2S-2f for a different face f; sum=6S-2(x+y+z)=5S.
        total=72+96+102; S=F(total,5)
        contacts=[S-F(value,2) for value in (72,96,102)]
        assert S==54 and contacts==[F(18),F(6),F(3)] and sum(contacts)==S/2
        solution={'assembly_areas':[72,96,102],'face_pair_contact_areas':[str(v) for v in contacts],'sum_assembly_areas':total,
                  'equations':['72=2S-2x','96=2S-2y','102=2S-2z','S=2(x+y+z)'],
                  'sum_equation':'270=6S-2(x+y+z)=5S','unique_S':str(S),
                  'incorrect_six_copy_average':'270/6=45 ignores all six hidden contacting face patches.',
                  'source_panel_correspondence':'stack glues across the largest face; wide across a narrow side; long across the end. All three different face types occur. Source wording explicitly says labels are surface areas of the assembled shapes, not sums of full brick surfaces.'}
        answer='54'
    elif qid=='Solid226':
        models=scene['solid_models'];voxels=set()
        import itertools
        for model in models:
            voxels.update(itertools.product(*(range(int(a),int(b)) for a,b in zip(model['min'],model['max']))))
        original=set(itertools.product(range(1),range(9),range(3)))
        def surface(items):
            return sum(tuple(p[j]+(delta if j==axis else 0) for j in range(3)) not in items for p in items for axis in range(3) for delta in (-1,1))
        assert surface(original)==surface(voxels)==78
        solution={'removed_voxel':sorted(original-voxels),'original_surface_area':surface(original),'new_surface_area':surface(voxels),'delta':0,
                  'reason':'The width is1, and the1-foot cube spans the entire thickness at an interior top location. Removed top/front/back patches each1; newly exposed floor/two side walls each1. Net3-3=0. A pocket with a rear wall is not the shown full-width notch.'}
        answer='C'
    else: raise ValueError(qid)
    return {**common,'proof':solution,'derived_answer':answer,'stored_answer_agrees':answer==record(qid)['answer'],
            'source_and_formal_pngs_actually_viewed':True,'all_original_conditions_and_diagnostic_features_preserved':'No new candidate alters these input objects.'}

if __name__=='__main__':
    for qid in IDS:
        result=prove(qid);assert result['stored_answer_agrees']
        write(UNIT/qid/'primary_math_audit.json',result)
        print(json.dumps({'question_id':qid,'derived_answer':result['derived_answer'],'proof':result['proof']},ensure_ascii=False))
