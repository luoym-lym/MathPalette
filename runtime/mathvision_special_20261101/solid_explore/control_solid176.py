from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
folder=OUT/'Solid176/false_flap_pair';control=folder/'baseline_control';control.mkdir(parents=True,exist_ok=True)
shutil.copyfile(ROOT/'SolidGeometry/image/Solid176.png',control/'original.png')
(control/'design.json').write_text(json.dumps({'question_id':'Solid176','expected_wrong_answer':'D','control':True,'purpose':'Original image control after two candidate responses D; same question/profile, no annotation.'},ensure_ascii=False,indent=2),encoding='utf-8')
review={'question_id':'Solid176','correct_answer':'C','expected_wrong_answer':'D','geometry_unchanged':True,'labels_occluded':False,'new_geometry':False,'new_conditions':False,'marked_objects':['flap310b','flap311b','flap300b','flap301b'],'folding_proof':{'side_strip':'Four unit squares wrap into four side faces. End-cap triangles fold into z=1 or z=0; coordinates below are cap x/y.','D_top_triangles':[[[0,0],[1,0],[1,1]],[[1,1],[0,1],[0,0]]],'D_bottom_triangles':[[[0,0],[1,0],[0,1]],[[1,1],[0,1],[1,0]]],'D_result':'Both pairs are complementary half-squares, with disjoint interiors and total area1. D closes both ends and is valid.','C_bottom_triangles':[[[0,0],[1,0],[0,1]],[[0,1],[0,0],[1,0]]],'C_result':'The two lower flaps cover the same half-square, leaving the other half uncovered; C cannot form the cube.'},'human_solvability':'Red color and width2 apply to four original flap diagonal edges only. Original fold boundaries, labels and shape remain readable. No equality or gluing condition is added.','approval_status':'Agent review only; not user Pass/Collect.'}
(folder/'human_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
print(control)
