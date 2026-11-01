from tools_local import *
qid='Solid187';vid='false_cap_notch_partner';folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
roles=[];actions=[]
for ids,color,role in [(['hole0_1','hole1_1','Bboundary9','Bboundary34'],'#DC2626','One target edge hole has two half-notch inner bases; bind both to B central joined-hinge cut, which is a locally valid paired hole.'),(['hole2_1','hole3_1','Bboundary45','Bboundary55'],'#2563EB','The other target edge hole has two half-notch inner bases; falsely bind them to B outer top and bottom cap cuts, which fold to different cube edges, not one pair.')]:
    for ident in ids:
        actions.append({'type':'set_object_style','target':ident,'color':color,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':ident,'role':role})
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Pair target notch halves with one true hinge pair and one false top/bottom cap pair.','intent':'Wrong identification of unfolded half-notch partners.','params':{'actions':actions}}
AD.render_candidate(plugin,folder)
write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':'B','formal_correct_answer':'C','created_at':datetime.now(timezone.utc).isoformat(),'mechanism':'Red inner bases bind the two halves of target hole0 to B joined-hinge cut. Blue inner bases bind target hole1 to the separate upper and lower cap notches in B, inviting the false belief that those two caps close onto one edge. The original cap positions and all black boundaries remain visible; no cuts or geometry are added.','marker_roles':roles,'unique_math':'Target contains two holes centered on opposite parallel cube edges. Full per-face fold audit finds A and D have two paired holes on adjacent parallel edges; B only one paired hole plus two unpaired notches on distinct edges; E has face-interior holes. Only C gives the target pair of opposite edge holes.','math_audit_path':str(TASK/qid/'folded_notch_audit.json'),'context_sha256':file_hash(TASK/qid/'context.json'),'candidate_png_sha256':file_hash(folder/'candidate.png'),'limits':['No calls or original controls yet.','No causal or human performance claims; primary review must inspect actual candidate.','Parent must commission a new independent second review before any delivery.']})
write(folder/'eligibility_before_design.json',check)
print(str(folder))
