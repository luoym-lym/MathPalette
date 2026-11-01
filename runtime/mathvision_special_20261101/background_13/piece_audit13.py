from tools13 import *
import itertools,numpy as np
def conn(cells):
    cells=set(map(tuple,cells))
    if not cells:return False
    seen={next(iter(cells))}
    while True:
        new=seen|{p for p in cells if any(sum(abs(p[i]-q[i]) for i in range(3))==1 for q in seen)}
        if new==seen:return len(seen)==len(cells)
        seen=new
rots=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([-1,1],repeat=3):
        m=np.zeros((3,3),int)
        for i,j in enumerate(perm):m[i,j]=signs[i]
        if round(np.linalg.det(m))==1:rots.append(m)
assert len(rots)==24
def canon(cells):
    a=np.array(cells,int)
    return min(tuple(sorted(map(tuple,(r:=a@m.T)-r.min(axis=0)))) for m in rots)
for qid,w,z0 in [('Solid162',3,5),('Solid198',4,11)]:
    s=AD.scenes[qid];p=ROOT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/qid/'scene.json';native=json.loads(p.read_text(encoding='utf-8'))
    observed={};face_audit=[]
    for obj in s['objects']:
        if obj['type']!='face' or not obj['id'].startswith('main'):continue
        a=np.array(obj['points']);mins=a.min(axis=0);maxs=a.max(axis=0)
        if mins[1]==maxs[1]==0:c=(int(mins[0])-10,0,int(mins[2])-z0)
        elif mins[2]==maxs[2]==z0+2:c=(int(mins[0])-10,int(mins[1]),1)
        elif mins[0]==maxs[0]==10+w:c=(w-1,int(mins[1]),int(mins[2])-z0)
        else:raise ValueError(obj)
        mat=obj['source_material'];assert c not in observed or observed[c]==mat
        observed[c]=mat;face_audit.append({'face_id':obj['id'],'cell':c,'material':mat})
    allc=set(itertools.product(range(w),range(2),range(2)))
    visible={c for c in allc if c[0]==w-1 or c[1]==0 or c[2]==1}
    for c in visible:observed.setdefault(c,'white')
    hidden=sorted(allc-set(observed));mats=sorted(set(observed.values()));solutions=[];attempts=[]
    for assignment in itertools.product(mats,repeat=len(hidden)):
        full={**observed,**dict(zip(hidden,assignment))}
        groups={m:[c for c in allc if full[c]==m] for m in mats}
        if any(len(v)!=4 for v in groups.values()):continue
        connected={m:conn(v) for m,v in groups.items()};valid=all(connected.values())
        attempts.append({'hidden_assignment':[{ 'cube':c,'material':full[c]} for c in hidden],'connectivity':connected,'valid':valid})
        if valid:solutions.append(groups)
    assert len(solutions)==1,(qid,solutions)
    white=solutions[0]['white'];matches={k:canon(v)==canon(white) for k,v in native['option_cube_sets'].items()}
    assert [k for k,v in matches.items() if v]==[AD.records[qid]['answer']]
    report={'question_id':qid,'method':'Reconstruct each observed cell material from frozen source exterior face fills. An unfilled visible unit face is white. Only hidden cells are enumerated; four cells per material and face-connected physical pieces are imposed. Compare white set against all five options under all24 proper cube rotations and translation.','visible_cell_materials':[{'cube':c,'material':m} for c,m in sorted(observed.items())],'source_face_audit':face_audit,'hidden_cells':hidden,'quota_compatible_hidden_assignments':attempts,'unique_complete_piece_sets':solutions[0],'white_option_rotation_matches':matches,'unique_correct_answer':AD.records[qid]['answer'],'source_native_semantic_path':str(p.relative_to(ROOT)),'source_native_sha256':file_hash(p),'important_correction':('Initial design descriptions overstate that all four black cells are visible. Exactly three black cells are visible; the fourth is forced to the adjacent hidden back-bottom cell by connectivity. The immutable design records are preserved and this explicit exhaustive proof supersedes that wording.' if qid=='Solid198' else None),'physical_piece_connectivity_basis':'A piece made of unit cubes is a connected solid joined face to face; disconnected material cells are not one physical piece.'}
    write(TASK/qid/'primary_piece_completion_audit.json',report)
    print(qid,'observed',len(observed),'hidden',hidden,'assignments',len(attempts),'valid',len(solutions),'matches',matches)
