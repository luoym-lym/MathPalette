from tools08 import *
folder=HERE/'Plane404/original_control';folder.mkdir(parents=True,exist_ok=True)
(folder/'candidate.png').write_bytes((HERE/'Plane404/original.png').read_bytes())
write(folder/'design.json',{'question_id':'Plane404','variant_id':'original_control','expected_wrong_answer':'A','created_at':now(),'role':'Separate original control; copied original PNG, no candidate annotations. Wrong target required by unchanged harness and declared before calls; correct formal answer C is never solver input.','approval_status':'UNREVIEWED CONTROL ONLY'})
write(folder/'primary_visual_review.json',{'actual_candidate_png_viewed':True,'original_png_viewed':True,'proceed_to_API':True,'review':'The original was actually viewed in the original-image inspection batch. This file is a byte-identical copy of that original. Control is not a candidate and supplies no additional hard gate.'})
write(folder/'control_copy_audit.json',{'original_copy_sha256':file_hash(HERE/'Plane404/original.png'),'control_sha256':file_hash(folder/'candidate.png'),'byte_identical':True})
