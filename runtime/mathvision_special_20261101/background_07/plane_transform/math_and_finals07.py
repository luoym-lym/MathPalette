from tools_local import *
import numpy as np
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
_new_write=write
def write(p,v):
    if Path(p).exists():assert load(p)==v;return
    _new_write(p,v)
def objs(qid):return {o['id']:o for o in load(HERE/qid/'context.json')['objects']}
oo=objs('Plane259');source=np.array(oo['o10']['geometry']['points'],dtype=float)
def centred(p):return p-(p.max(axis=0)+p.min(axis=0))/2
src=centred(source);desired=-src*8/9
errors={}
for label,oid in zip('ABCDE',['o11','o12','o13','o14','o15']):
    p=centred(np.array(oo[oid]['geometry']['points'],dtype=float))
    errors[label]=float(np.max(np.abs(p-desired)))
assert errors['C']<1e-12 and all(v>.1 for k,v in errors.items() if k!='C')
quarter=np.column_stack([src[:,1],-src[:,0]])*8/9
wrong=centred(np.array(oo['o14']['geometry']['points'],dtype=float))
assert np.max(np.abs(wrong-quarter))<1e-12
for original,reflected,signs in [('o5','o7',[-1,1]),('o7','o9',[1,-1])]:
    a=np.array(oo[original]['geometry']['points'],dtype=float);b=np.array(oo[reflected]['geometry']['points'],dtype=float)
    assert np.max(np.abs(a*np.array(signs)-b))<1e-12
write(HERE/'Plane259/exact_reflection_math_audit.json',{'question_id':'Plane259','method':'Use fullprecision source context polygon vertices, centre by exact bounding-box centre and apply-I with common8/9scale. Check every corresponding vertex, not only a matching edge.','source_object':'o10','source_vertex_count':len(source),'worked4_reflections_exact':True,'expected_transformation':[[-1,0],[0,-1]],'all_option_max_coordinate_errors_under_halfturn':errors,'unique_match':'C','target_D_verified_clockwise90_instead':True,'target_D_max_error_under_clockwise90':float(np.max(np.abs(wrong-quarter))),'no_solver_calls':True})
oo=objs('Plane215');p=np.array(oo['o1']['geometry']['points'],dtype=float)-[11.2,7]
errors={}
arc_errors={}
for label,oid,c in [('A','o203',[1.25,1.25]),('B','o207',[5.25,1.25]),('C','o211',[9.25,1.25]),('D','o215',[13.25,1.25]),('E','o219',[17.25,1.25])]:
    # Polygon sampling starts at differing radial edges: compare cyclic point sets.
    target=np.array(oo[oid]['geometry']['points'],dtype=float)-c
    desired=-p*1.25
    errors[label]=float(max(np.linalg.norm(desired[:,None,:]-target[None,:,:],axis=2).min(axis=1)))
    arc=oo['o'+str(int(oid[1:])+1)]['geometry'];angles=np.deg2rad(np.linspace(arc['start_deg'],arc['end_deg'],181))
    target_arc=np.column_stack([np.cos(angles),np.sin(angles)])*1.125
    src_angles=np.deg2rad(np.linspace(180,360,181));desired_arc=-np.column_stack([np.cos(src_angles),np.sin(src_angles)])*1.125
    arc_errors[label]=float(max(np.linalg.norm(desired_arc[:,None,:]-target_arc[None,:,:],axis=2).min(axis=1)))
combined={k:max(errors[k],arc_errors[k]) for k in errors}
assert combined['A']<1e-12 and all(v>.1 for k,v in combined.items() if k!='A')
write(HERE/'Plane215/exact_flip_math_audit.json',{'question_id':'Plane215','method':'Compose perpendicular flips-I; transform complete34vertex black quarter boundary and complete semicircle, common1.25scale to choices. Check both printed black region and enclosing semicircle.','all_option_black_quarter_errors':errors,'all_option_semicircle_errors':arc_errors,'all_option_combined_errors':combined,'unique_match':'A','black_fill_quarter_retained':True,'verification_lesson':'Black quarter alone also matchesE. The full semicircle orientation excludesE; the final proof checks both and does not infer uniqueness from the quarter alone. Initial partial-check assertion was corrected locally before any final review record.','no_solver_calls':True})
for qid,vid,finals,notes in [
 ('Plane215','single_flip_quarter_correspondence',['D','A'],['Final explicitlyD but falsely saysDblank and secondflipstillback; narrative contradicts visible option.','Final explicitlyA after misreading flips as translations; correctletter with unsound explanation.']),
 ('Plane259','cap_stem_quarterturn_binding',['D','D'],['Explicit finalD. Recognizes orientation markers but reverses their sourcecolors and falsely describesD180degrees.','Explicit finalD. Talks about180degrees but misidentifiesDrededge as bottomhorizontal; Dactuallyhasredrightvertical cap.'])]:
    out=HERE/qid/vid;ev=next((out/'tests').iterdir());binding=load(ev/'binding.json');runs=[load(ev/f'run_{i:02d}.json') for i in [1,2]]
    assert all(r['status']=='completed' and r['finish_reason']=='stop' and not r['truncated'] for r in runs)
    hit=all(a==binding['expected_wrong_answer'] for a in finals)
    write(out/'manual_final_review.json',{'reviewed_at':now(),'manually_read_full_answers':True,'question_id':qid,'expected_wrong_answer':binding['expected_wrong_answer'],'correct_answer':load(HERE/qid/'formal_record.json')['answer'],'manual_final_answers':finals,'both_predeclared_hits':hit,'final_letter_value_consistency':'These are pictorial option letters with no separate numeric value pair; both Plane259 finals explicitlyD. Their flawed geometry narratives are disclosed and are not treated as proofs.','runs':[{'run_index':i+1,'path':str(ev/f'run_{i+1:02d}.json'),'response_path':str(ev/f'run_{i+1:02d}_response.json'),'manual_final':finals[i],'full_answer':r['answer'],'observations':notes[i],'image_sha256':r['image_sha256'],'design_sha256':r['design_sha256']} for i,r in enumerate(runs)],'raw_binding_path':str(ev/'binding.json'),'same_frozen_image_and_design':True,'retries':0,'status':'POSSIBLE_TWO_HIT_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW' if hit else 'PRESET_MISS_DO_NOT_RETRY_IDENTICAL_CANDIDATE','no_original_controls':True,'causal_limits':'No causal attribution or human/statistical/per-marker claim. Narratives differ and contain visual errors. Only two actual identical-input calls were made.'})
print(json.dumps({'math':'exact_halfturn_uniqueC_and_flip_uniqueA','manual_finals':{'Plane215':['D','A'],'Plane259':['D','D']}}))
