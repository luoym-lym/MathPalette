from tools72 import *
import difflib

source=BASE/'harness/quicktest3_isolated.py'
data=source.read_bytes()
old=b'PROJECT = Path(__file__).resolve().parents[3]'
new=b'PROJECT = Path(__file__).resolve().parents[4]'
assert data.count(old)==1
relocated=data.replace(old,new)
d=HERE/'harness';d.mkdir(exist_ok=True)
(d/'quicktest3_isolated.py').write_bytes(relocated)
write(HERE/'harness_relocation_byte_diff_audit.json',{'original_path':str(source),'original_sha256':sha(source),'relocated_path':str(d/'quicktest3_isolated.py'),'relocated_sha256':sha(d/'quicktest3_isolated.py'),'only_change':'PROJECT parents[3] to parents[4] because of ownroot/harness directory depth','reverse_patch_exact_original_bytes':relocated.replace(new,old)==data,'unified_diff':list(difflib.unified_diff(data.decode('utf-8').splitlines(),relocated.decode('utf-8').splitlines(),fromfile='original',tofile='own relocation')),'remote_payload_profile_credential_logic_unchanged':True,'guard_installed_by_launch72_before_import':True})

for q,v,notes in [
 ('Plane335','r72_congruent_apex_wedge_binding','Viewed full native 768x768 new candidate, formal PNG, source JPG and both old candidate PNGs. The two red open Vs follow only existing oblique triangle edges. All six vertices and both black vertical edges remain obvious; no connector crosses either interior. Color does not specify mandatory or exclusive endpoints. The comparison targets matching apex role rather than old top/bottom tangent ports.'),
 ('Plane355','r72_width_to_fold_measurement_role','Viewed full native 768x768 new candidate, formal PNG and source JPG. Both blue width segments are visible; the turn base retains its dashes. Red x-scoped bottom edge and red turn diagonal remain visibly separate segments with different direction and length; P,Q,x and45 degrees are fully readable. The dimension below P still ends at the fold foot. No paper ink needs to disappear in an image-choice transformation, since choices are numerical values. Same red is a comparison group, not an additional equality given.')]:
    d=HERE/q/v
    write(d/'primary_visual_review.json',{'question_id':q,'variant_id':v,'reviewed_at':now(),'type':'PRIMARY ONLY; not independent second review','actual_candidate_native_png_viewed':True,'source_JPG_and_formal_PNG_viewed':True,'native_size':[768,768],'notes':notes,'all_marks_have_source_receiver_roles':True,'all_original_distinctions_and_question_semantics_preserved':True,'no_arbitrary_marker_count_limit':True,'human_unique_math_proof':str(HERE/q/'unique_math.json'),'design_roles':read(d/'design.json')['marker_roles'],'proceed_to_API':True,'limitations':['No human study, causal mechanism proof, control-correctness requirement or efficacy claim.','Any future double hit remains primary only and requires a NEW parent independent review.']})
print('primary native gates saved; original harness relocation audited',flush=True)
