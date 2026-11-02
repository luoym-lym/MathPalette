from design_tools import *
def make(q,vid,expected,specs,mechanism,new_difference,wrong_rationale):
    actions=[];roles=[]
    for prefix,edge,color,role in specs:
        target=match_edge(q,prefix,edge)
        assert AD.scenes[q]['objects'][next(i for i,o in enumerate(AD.scenes[q]['objects']) if o['id']==target)]['visibility']=='visible'
        actions.append(style(target,color,1.5));roles.append(role)
    assert len({a['target'] for a in actions})==len(actions)
    proof=json.loads((TASK/q/'primary_math_audit.json').read_text(encoding='utf-8'))
    path=save_candidate(q,vid,expected,actions,roles,mechanism,proof,TASK/q/'primary_math_audit.json')
    write(path/'design_difference_audit.json',{'question_id':q,'variant_id':vid,'stage':'material_refinement','before_any_API_calls':True,'old_history':str(TASK/q/'history_audit.json'),'old_designs':0,'old_calls':0,'new_matched_information':new_difference,'specific_wrong_inference':wrong_rationale,'expected_wrong_answer':expected,'cosmetic_or_posthoc':False,'unchanged_failed_image_retest':False,'candidate_png_sha256':file_hash(path/'candidate.png'),'design_sha256':file_hash(path/'design.json'),'primary_math_unique_answer':AD.records[q]['answer'],'appearance_only':'All marks recolor actual visible source segments. No additional edges, cubes, labels, fills, contact, pip or relation glyph. Original geometry/projection/visibility/text frozen.'})
    print(q,vid,'marks',len(actions),'preset',expected)

q='Solid99';specs=[]
for z,role in [(1,'donor straight cell (1,0,1), with opposite vertical contacts and four painted faces'),(2,'receiver branch cell (1,0,2), with up/down/left contacts and only three painted faces')]:
    specs.extend([('chain',[[2,0,z],[2,0,z+1]],RED,role+': front-right upright side border'),('chain',[[2,0,z+1],[2,1,z+1]],RED,role+': upper side seam, not a new contact')])
make(q,'r36_straight_branch_side_seam', '11',specs,'Pair identical open right-side L seams of a straight chain cube and the three-contact branch cube. Transfer the straight cube two-contact classification to the branch despite its additional left neighbour.','Old screening rejected whole-chain or selected-die salience. Four exact side-edge styles create one donor/receiver pair spanning two different contact degrees, preserving the complete2x2cycle and its seams.','The true graph has10degree2,1degree1,1degree3. Misassign only the branch as degree2 by importing its side-identical straight neighbour classification:10+1=11four-painted cubes.')

q='Solid112';specs=[]
for prefix,dx,z,kind in [('before',0,2,'donor complete upper course'),('after',5.3,1,'receiver exposed bottom-course surface')]:
    for y in [0,1]:
        for x in [1,2]:
            color=RED if y==0 else BLUE
            specs.extend([(prefix,[[x+dx,y,z],[x+1+dx,y,z]],color,f'{kind} tile({x},{y}): front unit grid edge'),(prefix,[[x+1+dx,y,z],[x+1+dx,y+1,z]],color,f'{kind} tile({x},{y}): receding unit grid edge; top height remains {z}')])
make(q,'r36_four_tile_cross_course_binding','3',specs,'Match four true upper-plane tiles on the complete block to four exposed lower-plane tiles on the remainder. The same two-row open grid groups encourage transferring upper-course occupancy across a height change.','Old screen considered mapping the two surviving upper cubes, which supports the correct answer. This instead binds four newly exposed lower tiles to the source upper tiles, while all tall-cube side faces and height risers stay black and visible.','If these four colored exposed lower faces are wrongly assigned to still-present upper cubes, retained count is9base+2trueupper+4falseupper=15, so18-15=3removed. The four false upper cubes are an explicitly modelled misconception; none is drawn or added.')

q='Solid117';specs=[]
for edge in [[[2,0,3],[3,0,3]],[[3,0,3],[3,1,3]],[[3,0,2],[3,0,3]]]:specs.append(('full',edge,RED,'donor: one true upper front-right unit-cube corner of the full reference'))
for x,y,h in [(1,0,2),(1,1,2),(2,0,1),(2,1,1),(2,2,2)]:
    dx=6.6;dz=1.65
    for edge,part in [([[x+dx,y,h+dz],[x+1+dx,y,h+dz]],'front top unit edge'),([[x+1+dx,y,h+dz],[x+1+dx,y+1,h+dz]],'right top unit edge'),([[x+1+dx,y,h-1+dz],[x+1+dx,y,h+dz]],'upright one-course edge')]:
        specs.append(('partial',edge,RED,f'receiver lowered column({x},{y}), actual height{h}, missing{3-h}: {part}; existing remaining-cube edge, not an empty-cube wireframe'))
make(q,'r36_lowered_column_unit_corner_binding','5',specs,'Reuse the complete unit-cube three-edge corner on each of five lowered-column tops, encouraging one missing cube per visible lowered top and collapsing the two deeper deficits.','Old screen suggested generic layer rails. This binds one exact3edge unit-corner exemplar to five actual lowered-top cube corners, where two columns need2cubes and three need1. No empty missing-cube outline or extra partition appears.','Five lowered columns have deficits1,1,2,2,1. Counting the five matched top-corner units as one deficit each gives5, instead of1+1+2+2+1=7.')

q='Solid139';specs=[]
for digit,dx in [(0,0),(2,10.2),(3,15.3)]:
    for z,role in [(6,'true free endpoint donor,degree1'),(3,'middle-left elbow receiver,degree2'),(0,'bottom-left elbow receiver,degree2')]:
        specs.extend([(f'digit{digit}',[[dx,0,z+1],[dx+1,0,z+1]],BLUE,f'digit{digit} {role}: upper front rim/seam'),(f'digit{digit}',[[dx,0,z],[dx,0,z+1]],BLUE,f'digit{digit} {role}: left front vertical; open L corresponds to endpoint')])
    for z,role in [(0,'true free endpoint donor,degree1'),(3,'middle-right elbow receiver,degree2'),(6,'upper-right elbow receiver,degree2')]:
        specs.extend([(f'digit{digit}',[[dx+3,0,z],[dx+4,0,z]],RED,f'digit{digit} {role}: lower front rim/seam'),(f'digit{digit}',[[dx+4,0,z],[dx+4,0,z+1]],RED,f'digit{digit} {role}: right front vertical; open L corresponds to endpoint')])
make(q,'r36_endpoint_elbow_front_L_transfer','48',specs,'For each2, blue upper-left and red lower-right open L groups pair each true one-contact endpoint with two true two-contact elbows. Transfer endpoint five-painted-face classification onto elbows sharing the same local front L.','Old screen rejected whole-digit recoloring and generic endpoint/elbow proposals. This explicitly fixes six donor endpoint cells, twelve receiver elbow cells, exact two-edge counterparts, and all unaffected straight cells/the0. Distinct digits remain unconnected.','True answer60counts all degree2cells. Wrongly treating the twelve colored elbow receivers like their same-color endpoint donors excludes12eligiblecubes:60-12=48. Degree2straight cells and the0cycle remain unaffected in this hypothesis.')
