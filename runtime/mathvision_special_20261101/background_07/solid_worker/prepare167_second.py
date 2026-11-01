from design_tools import *
q='Solid167';prior=TASK/q/'orthogonal_notch_family_binding'
evidence=next((prior/'tests').iterdir())
write(prior/'manual_final_review.json',{'question_id':q,'expected_wrong_answer':'A','complete_final_answers_manually_read':True,'run_final_answers':['A','D'],'run_01_explicit_final':'Therefore, the correct diagram is A. A','run_02_explicit_final':'The correct diagram is D.','predeclared_wrong_hit':[True,False],'credible_two_hit':False,'evidence_dir':str(evidence),'status':'miss; no repeat of this image','notes':'Both answers are wrong but only one equals immutable preset A. No incidental options counted.'})
proof=json.loads((TASK/q/'fold_math_audit.json').read_text())
actions=[style('line14',RED,2,interval(q,'line14',.7,.9)),style('line14',BLUE,2,interval(q,'line14',.3,.5)),style('line42',RED),style('line45',RED),style('line43',BLUE),style('line44',BLUE)]
roles=['Red existing left-fold triangular notch sides identify actual horizontal-diamond family.','Blue existing top-fold triangular notch sides identify actual vertical-diamond family.','D top horizontal hole is the correct local shape for the red family.','D bottom horizontal hole is its correct reflection mate.','D left horizontal hole falsely binds blue top notch to a horizontal hole, inducing copied long-axis orientation.','D right horizontal hole completes this false blue reflection pair.']
mechanism='Complementary orthogonal-notch family trap: red left-notch maps correctly to D top/bottom horizontal diamonds; blue top-notch maps incorrectly to D left/right horizontal diamonds. Unlike prior A design this tests collapse to all-horizontal outputs, with a newly frozen preset D and distinct PNG.'
out=save_candidate(q,'top_notch_horizontal_family_binding','D',actions,roles,mechanism,proof,TASK/q/'fold_math_audit.json')
print(out)
