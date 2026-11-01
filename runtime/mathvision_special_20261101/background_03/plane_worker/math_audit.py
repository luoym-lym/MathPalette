from new_tools import *
import itertools,math
result={}
tiles={'I':{'T':8,'R':9,'B':7,'L':3},'II':{'T':6,'R':3,'B':2,'L':4},'III':{'T':7,'R':5,'B':0,'L':1},'IV':{'T':2,'R':1,'B':6,'L':9}}
layouts=[]
for p in itertools.permutations(tiles):
    a,b,c,d=[tiles[x] for x in p]
    if a['R']==b['L'] and a['B']==c['T'] and b['B']==d['T'] and c['R']==d['L']:layouts.append(dict(zip('ABCD',p)))
assert layouts==[{'A':'II','B':'I','C':'IV','D':'III'}]
result['Plane471']={'method':'Enumerated24 translation-only tile assignments using unchanged labels read from original PNG.','unique_layout':layouts,'correct_answer':'D','tempting_marked_layout':{'A':'I','B':'IV','C':'III','D':'II'},'unmatched_bottom_edge':[5,4]}
choices={'A':{4,6,12},'B':{1,5,10},'C':{2,4,9},'D':{3,6,9},'E':{5,7,12}}
rotations=[{((n-1+k)%12)+1 for n in [1,5,7]} for k in range(12)]
matches={label:[k*30 for k,r in enumerate(rotations) if r==numbers] for label,numbers in choices.items()}
assert [k for k,v in matches.items() if v]==['A']
result['Plane313']={'method':'Enumerated12 clock-step rotations of actual hole positions1,5,7.','choice_rotation_degrees':matches,'correct_answer':'A','incorrect_correspondence':{'1':'9','5':'2','7':'4'},'limitation':'Colored sectors are markers only, not an additional rotation condition.'}
source=[(1,2),(1,4)];target=[(3,2),(5,2)];centres={'T':(1,1),'U':(2,1),'V':(2,3),'W':(3,4)}
rotation_records={}
for name,o in centres.items():
    found=[]
    for theta in [90,-90]:
        transformed=[]
        for x,y in source:
            dx,dy=x-o[0],y-o[1]
            rx,ry=(-dy,dx) if theta==90 else (dy,-dx)
            transformed.append((rx+o[0],ry+o[1]))
        if set(transformed)==set(target):found.append({'degrees':theta,'ordered_images':transformed})
    rotation_records[name]=found
assert [k for k,v in rotation_records.items() if v]==['U','W']
result['Plane425']={'method':'The undirected orientation change vertical-to-horizontal requires±90mod180; enumerating±90 for each labeledcentre exhausts possibilities.','centre_checks':rotation_records,'correct_answer':'C'}
scene=json.loads((ROOT/'PlaneGeometry/dataset_generator/scenes/Plane250.json').read_text(encoding='utf-8-sig'))
counts={}
for index in range(4):
    count={'diagonal':0,'vertical':0,'horizontal':0}
    for obj in scene['objects']:
        if not obj['id'].startswith(f'path{index}_'):continue
        (x,y),(u,v)=obj['points'];key='vertical' if x==u else 'horizontal' if y==v else 'diagonal';count[key]+=1
    counts[index]=count
assert counts=={0:{'diagonal':5,'vertical':0,'horizontal':0},1:{'diagonal':5,'vertical':4,'horizontal':0},2:{'diagonal':0,'vertical':6,'horizontal':5},3:{'diagonal':3,'vertical':4,'horizontal':2}}
result['Plane250']={'method':'Counted exact frozen path object directions, solved linearbasis equations from formal diagram lengths.','counts':counts,'d':5,'v':3,'h':4,'Tin_length':35,'wrong_basis_Tin_length':43,'correct_answer':'35'}
result['Plane407']={'mathematical_solution':'If widths are a,b,c,d then the two centre distances are(a+b)/2 and(c+d)/2. Their sum=(a+b+c+d)/2=36/2=18 (A).','prescreen_status':'HOLD_NO_VARIANT_NO_API','reason':'Current proposed marks on unequal dividers/centres would risk arbitrary attention or unclear measurement attribution. No sufficiently purposeful and clear deceptive correspondence was found within this finite subset.'}
result['Plane435']={'fold_map':'x->10-x,y unchanged','matching_pairs':[['o17','o18'],['o19','o20'],['o21','o22']],'nonmatching_pairs':{'o23/o24':'Circle centres(.5,1.5),(8.5,1.5) have distances4.5 and3.5 from x5, so not coincident.','o25/o26':'The bottom triangles have the same handedness; reflected vertices{(7,0),(6,0),(7,1)} differ from{(6,0),(7,0),(6,1)}.'},'correct_answer':'3'}
write(HERE/'mathematical_audit.json',result)
print('Mathematical audit saved: unique Plane471 layout; Plane313 rotationA; Plane425 U/W; Plane250 Tin35.',flush=True)
