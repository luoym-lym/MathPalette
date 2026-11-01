from tools_local import *
qid='Solid144';vid='reflected_three_edge_frame';folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
audit=json.loads((TASK/qid/'lattice_corner_congruence_audit.json').read_text(encoding='utf-8'))
assert audit['proper_rotation_matches']==['W','Y'] and audit['reflections_only']==['X','Z']
correspondences=json.loads((TASK/qid/'available_reflected_edge_correspondences.json').read_text(encoding='utf-8'))['candidates']
roles=[];actions=[]
for given,color,part in [('given_graye0','#DC2626','First longitudinal boundary edge at the initial end of the main shaft.'),('given_graye26','#2563EB','Transverse boundary edge at the remote terminal arm.'),('given_graye32','#16A34A','Third independent-axis edge at the other end of the main shaft.')]:
    row=next(r for r in correspondences if r['given']==given)
    for group in ['given','X','Z']:
        ident=row[group]
        actions.append({'type':'set_object_style','target':ident,'color':color,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':ident,'role':part+' This color binds the corresponding physical feature under a determinant -1 reflection map, falsely suggesting a proper rotation match.','correspondence_lattice_endpoints':row['reference_lattice_endpoints'],'group':group})
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Bind three independent edge features through a reflected spatial frame to X and Z.','intent':'Mirror correspondence mistaken for proper spatial rotation.','params':{'actions':actions}}
AD.render_candidate(plugin,folder)
write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':'B','formal_correct_answer':'A','created_at':datetime.now(timezone.utc).isoformat(),'mechanism':'Three independent colored edge directions bind the gray input to X and Z using exact reflected 3D feature correspondences. These local features agree under a left-handed map; choosing X and Z requires overlooking handedness and treating this reflection as a rotation. W and Y remain fully visible and unmodified.','marker_roles':roles,'primary_math':'Frozen 3D boundary-corner frames show W/Y admit proper signed-axis rotations, while all matches for X/Z have determinant -1. The ordered 3-axis frame distinguishes rotation from reflection; input geometry and all dashed edges stay frozen.','math_audit_path':str(TASK/qid/'lattice_corner_congruence_audit.json'),'context_sha256':file_hash(TASK/qid/'context.json'),'candidate_png_sha256':file_hash(folder/'candidate.png'),'limits':['No calls yet and no original control.','Primary analysis only; independent review still required.','Color correspondence is an appearance cue, not a new condition that rotations must preserve.']})
write(folder/'eligibility_before_design.json',check)
print(str(folder))
