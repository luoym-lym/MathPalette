from research import *
qid,name=sys.argv[1:3]
folder=HERE/qid/name
check=eligible('SolidGeometry',qid)
write(folder/'eligibility_immediately_before_calls.json',check)
if not check['eligible']:raise SystemExit('Question now excluded; no API')
write(folder/'primary_prescreen.json',{
    'question_id':qid,'actual_png_viewed':True,
    'no_labels_fills_questions_or_frozen_3d_projection_visibility_changed':True,
    'marker_role_review':'Each original-object target and exact interval was checked against the current scene and actual PNG; roles and primary unique-solution proof are in immutable design.json.',
    'unique_answer_preserved':True,'status':'primary_only_not_independent_second_review',
    'image_sha256':sha(folder/'candidate.png'),'design_sha256':sha(folder/'design.json')})
sys.path.insert(0,str(HERE.parent/'harness'))
from quicktest3_isolated import run_tests
result=run_tests('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',2)
print(json.dumps({'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']},ensure_ascii=False),flush=True)
