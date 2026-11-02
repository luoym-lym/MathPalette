from tools18 import *
assert BRANCH=='SolidGeometry'
import itertools,numpy as np
q='Solid164';v='upright_yes_face_alias';out=HERE/q/v
assert eligibility(q)['eligible'];out.mkdir(parents=True,exist_ok=False)
cfg,ad,Renderer=adapter();before=inputs(ad,q);c=ad.inspect_question(q)
write(out/'fresh_context.json',c);write(out/'eligibility_before_design.json',eligibility(q))
scene=json.loads((ROOT/BRANCH/ad.records[q]['scene']).read_text(encoding='utf-8-sig'))
objects={o['id']:o for o in c['objects']}
chosen=[]
for cube,axis in [(0,0),(1,1)]:
    obj=next(o for o in c['objects'] if o['id'].startswith('cube'+str(cube)+'_') and '(0.0), np.float64(0.0), np.float64(0.0))' in o['id'] and o['id'].endswith('_'+str(axis)))
    endpoints=[]
    for xyz in obj['geometry']['points']:
        snap=next(s for s in c['snap_points'] if s.get('world_xyz')==xyz)
        endpoints.append(snap['xy'])
    chosen.append({'object_id':obj['id'],'world_endpoints':obj['geometry']['points'],'exact_snap_endpoints':endpoints})
actions=[{'type':'add_line','id':'alias_edge_'+str(i),'endpoints':x['exact_snap_endpoints'],'color':'#DC2626','linestyle':'solid'} for i,x in enumerate(chosen)]
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':v,'intent':'Map first right YES lower edge to middle left YES lower edge, falsely merging two distinct upright YES faces because their word baselines look alike.','params':{'actions':actions}}
renderer=Renderer(cfg,ad,{q:c});n,a,pix=renderer.render(plugin);n2,b,pix2=renderer.render(n,frozen=True)
assert a==b and pix==pix2 and before==inputs(ad,q)
write(out/'plugin.json',n);(out/'candidate.png').write_bytes(a);(out/'repeat.png').write_bytes(b)
write(out/'render_check.json',{'baseline_pixel_equal':True,'normalized_frozen_replay':True,'two_png_bytes_identical':True,'pixel_sha256':pix,'png_sha256':file_hash(out/'candidate.png'),'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(n),'isolation':ISOLATION,'new_ink_coincident_with_original_edges':chosen})
# Reconstruct the same die from all three directed face-word observations.
normals=[(0,0,1),(-1,0,0),(0,-1,0)]
observations=[ [('no',(0,-1,0)),('YES',(0,-1,0)),('YES',(0,0,1))], [('YES',(0,1,0)),('YES',(0,0,1)),('maybe',None)], [('no',(0,-1,0)),('YES',(0,1,0)),('no',(1,0,0))] ]
rots=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1,1),repeat=3):
        mat=np.zeros((3,3),dtype=int)
        for i,j in enumerate(perm):mat[i,j]=signs[i]
        if round(np.linalg.det(mat))==1:rots.append(mat)
solutions=[]
for r1 in rots:
    for r2 in rots:
        words={};axes={};okay=True
        for rot,obs in zip((np.eye(3,dtype=int),r1,r2),observations):
            for normal,(word,direction) in zip(normals,obs):
                master=tuple(int(x) for x in rot@normal)
                axis=tuple(int(x) for x in rot@direction) if direction is not None else None
                if master in words and words[master]!=word:okay=False;break
                if axis is not None and master in axes and axes[master]!=axis:okay=False;break
                words[master]=word
                if axis is not None:axes[master]=axis
            if not okay:break
        if okay:solutions.append({'r1':r1.tolist(),'r2':r2.tolist(),'words':[{'normal':list(k),'word':w,'baseline':axes.get(k)} for k,w in words.items()]})
assert solutions and all(sum(f['word']=='YES' for f in x['words'])==3 and len(x['words'])==6 for x in solutions)
proof={'enumerated_rotation_pairs':24*24,'solutions':solutions,'unique_word_configuration_count':len(solutions),'YES_faces':3,'probability':'1/2','answer':'B','method':'Proper signed permutation cube rotations; equal normals must have equal words and directed baseline vectors. maybe baseline is unconstrained. First panel fixes global orientation; simultaneous rotations of other views are exhaustively checked.'}
write(out/'primary_math_enumeration.json',proof)
roles=['First cube right-face bottom edge is a precise local feature bordering one YES face.','Middle cube left-face bottom edge is its false same-face mate: equal upright screen word direction is not sufficient for 3D face identity. Both short red strokes coincide with original edges; no option label or whole cube is selected.']
write(out/'design.json',{'question_id':q,'variant_id':v,'expected_wrong_answer':'A','created_at':now(),'mechanism':plugin['intent']+' Expected shortcut: merge the two distinct faces and count only2YES faces, hence1/3(A).','marker_roles':roles,'primary_math_proof':proof,'candidate_png_sha256':file_hash(out/'candidate.png'),'candidate_pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'frozen_before_two_calls':True})
write(out/'source_audit.json',{'question_id':q,'formal_record':ad.records[q],'primary_enumeration':proof,'frozen_input_hashes':before,'exact_edge_bindings':chosen})
print(q,v,'solutions',len(solutions),'rendered; actual visual review required',flush=True)
