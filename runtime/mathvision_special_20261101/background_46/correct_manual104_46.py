from tools46 import *
d=OWN/'Solid104/r46_square_contact_records_to_faces';p=d/'manual_final_review.json';old=read(p);corrected=copy.deepcopy(old)
assert old['full_manual_final_reviews'][1]['manual_unambiguous_final']=='50'
corrected['full_manual_final_reviews'][1]['manual_unambiguous_final']='20'
corrected['full_manual_final_reviews'][1]['matches_immutable_preset']=False
corrected['correction']={'corrected_at':now(),'original_incorrect_record':str(p),'original_incorrect_record_sha256':sha(p),'field':'full_manual_final_reviews[1].manual_unambiguous_final','incorrect':'50','correct':'20','basis':'Full raw second response was read above: its calculation60-60+20=20 and explicit terminal Answer:20 agree. I accidentally typed50 in the review-script argument. Original incorrect metadata is preserved. Frozen PNG/design/plugin/preset/request/raw responses are untouched.','consequence':'Unchanged:0of2preset40hits; no candidate and no relabeling to20.'}
save(d/'manual_final_review_correction_46.json',corrected)
print('Solid104 corrected manual finals:50,20;0/2preset40; incorrect metadata retained with explicit correction')
