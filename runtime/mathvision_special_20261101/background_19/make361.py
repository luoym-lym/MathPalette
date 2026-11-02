from tools19 import *
from dataset_tools.mathvision_workbench import png_bytes
qid='Plane361';vid='diagonal_to_terminal_arc_radius_binding';out=HERE/qid/vid
assert eligibility(qid)['eligible']
cfg,ad=adapter();m=ad.inspect_question(qid);write(out/'fresh_context.json',m)
pts=[p['xy'] for p in m['snap_points']]
for xy in [[0.0,0.0],[2.0,2.0],[9.0,0.0],[7.0,2.0]]:assert xy in pts
actions=[{'type':'add_line','id':'initial_opposite_corner_diagonal','endpoints':[[0.0,0.0],[2.0,2.0]],'color':'#DC2626'}, {'type':'set_object_style','target':'o7','color':'#DC2626','linewidth_pt':2}, {'type':'add_line','id':'terminal_opposite_corner_diagonal','endpoints':[[9.0,0.0],[7.0,2.0]],'color':'#DC2626'}, {'type':'set_object_style','target':'o21','color':'#DC2626','linewidth_pt':2}]
hyp='Bind the actual initial and terminal square diagonals to the neighboring terminal P arcs, falsely attributing the diagonal radius to both end quarter-turns and a side radius to the middle quarter-turn, yielding D.'
proof='Each roll about the next contact vertex is 90 degrees. P follows successive radii 10,10*sqrt(2),10 before first returning to the line; the subsequent pivot at P contributes no additional distance. Total (pi/2)*(20+10*sqrt(2)) = 10*pi+5*pi*sqrt(2), choice C uniquely. The displayed start and end half-arcs are illustrative portions of the first and third quarter-circle. The two new dashed opposite-corner diagonals are valid auxiliary segments inside the unchanged square snapshots. Their length is 10*sqrt(2), but their remote endpoints are not the contact pivot during those terminal arcs. The original contact line, side lengths, square orientation, snapshots, P and original trajectory arcs remain unchanged. Rolling wording does not count internal regions, and dashed diagonals do not become a new piece of the solid trajectory.'
roles=['Initial P to opposite original corner, a real diagonal, false long-radius reference.','Actual first displayed P trajectory arc, bound to the wrong diagonal radius.','Terminal P to opposite original corner, a real diagonal, second false long-radius reference.','Actual terminal displayed P trajectory arc, bound to the wrong diagonal radius.']
p={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':vid,'intent':hyp,'params':{'actions':actions}}
renderer=PluginRenderer(cfg,ad,{qid:m});p=renderer.normalize(p)
write(out/'plugin.json',p)
write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'D','correct_answer':'C','hypothesis':hyp,'marker_roles':roles,'primary_unique_answer_proof':proof,'approval_status':'UNREVIEWED; primary exploration only','solver_input_policy':'Only formal question and candidate PNG; unchanged harness and profile.'})
before=inputs(ad,qid);scene=ad.scene(qid)
try:baseline=png_bytes(scene)
finally:scene.close()
assert pixel_hash(baseline)==pixel_hash(ad.original_paths[qid])
(out/'no_op.png').write_bytes(baseline)
_,data,h=renderer.render(p,frozen=True);_,data2,h2=renderer.render(p,frozen=True)
assert data==data2 and h==h2
(out/'candidate.png').write_bytes(data);(out/'repeat.png').write_bytes(data2)
write(out/'render_check.json',{'actual_schema_normalized':True,'normalization_idempotent':renderer.normalize(p)==p,'baseline_pixel_equal_formal':True,'baseline_pixel_sha256':pixel_hash(baseline),'candidate_sha256':file_hash(out/'candidate.png'),'repeat_sha256':file_hash(out/'repeat.png'),'byte_identical_twice':True,'candidate_pixel_sha256':h,'frozen_inputs_before':before,'frozen_inputs_after':inputs(ad,qid),'action_count':len(actions),'source_geometry_text_fill_visibility_modified':False})
print(json.dumps({'qid':qid,'variant':vid,'candidate_sha256':file_hash(out/'candidate.png')}),flush=True)
