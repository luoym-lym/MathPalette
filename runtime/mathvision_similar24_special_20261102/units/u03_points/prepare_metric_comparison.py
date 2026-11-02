from unit_env import *
from mathvision_plugins import PluginRenderer
from workbench_io import environment_versions

qid='Plane364';vid='square_side_diagonal_role_comparison'
eligible=eligibility(qid)
assert eligible['eligible']
config,adapter,meta=adapter_context(qid)
folder=OWN/qid/vid
folder.mkdir(parents=True,exist_ok=True)
save(folder/'eligibility_before_design.json',eligible)
save(folder/'context.json',meta)
xy={p['id']:p['xy'] for p in meta['snap_points']}
R,B='#DC2626','#2563EB'
actions=[];roles=[]
for target,start,end,points in [('h3',5/34,21/34,['P3','P4']),('v3',1/6,0.7,['P5','P1'])]:
    path=next(t for t in meta['canvas']['targets'] if t['id']==target)['partial_paths'][0]
    actions.append({'type':'set_object_style','target':target,'color':R,'linewidth_pt':1.5,
                    'interval':{'path_id':path['id'],'path_sha256':path['sha256'],
                                'start':start,'end':end,'wrap':False}})
    roles.append({'action_index':len(actions)-1,'source':points,'recipient':'the other red span and the blue square side spans',
                  'information':'Actual square diagonal with squared length 16; both red spans are equal and perpendicular.',
                  'purpose':'Compare a true diagonal point-pair role with side point-pair roles, rather than restrict orientations or allowed point subsets.'})
for i,(a,b) in enumerate([('P3','P1'),('P1','P4'),('P4','P5'),('P5','P3')]):
    actions.append({'type':'add_line','id':f'side{i+1}','endpoints':[xy[a],xy[b]],'color':B,'linestyle':'solid'})
    roles.append({'action_index':len(actions)-1,'source':[a,b],'recipient':'red diagonal spans and the other blue boundary spans',
                  'information':'Actual square boundary side with squared length 8; the four blue sides are equal and adjacent ones perpendicular.',
                  'purpose':'Show the geometric edge role and compare its true length with a different point-pair role (diagonal); no false equality mark is added.'})
renderer=PluginRenderer(config,adapter,{qid:meta})
raw={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'','intent':'','params':{'actions':actions}}
plugin=renderer.normalize(raw)
assert renderer.normalize(plugin)==plugin
save(folder/'plugin_input.json',raw);save(folder/'plugin.json',plugin)
n1,d1,p1=renderer.render(plugin,frozen=True);n2,d2,p2=renderer.render(plugin,frozen=True)
assert n1==n2==plugin and d1==d2 and p1==p2
(folder/'candidate.png').write_bytes(d1);(folder/'repeat.png').write_bytes(d2)
assert not any(read(p).get('candidate_sha256')==sha(d1) for p in OWN.glob('Plane*/**/design.json'))
hist=read(TASK/'history_index.json')
assert not any(d.get('frozen_candidate_png_sha256')==sha(d1) for q in hist['questions'] for d in q['designs'])
difference='The first tilted-square trial compared opposite parallel classes; the second existing-grid trial compared axis directions. This new design compares the actual side vs diagonal roles of different point pairs: squared lengths 8 vs16. All blue boundary sides belong to one class; both red internal diagonals to the other. The predicted side/diagonal role-mixing error is different from orientation restriction or universal equal-sidedness. This is not a relabel of either failed test and does not reuse its PNG.'
human='All six black marked points remain at their exact positions. The four blue sides form a true permitted square. Two red intervals lie on the original horizontal/vertical grid through its actual diagonals. Their crossing is an already existing unmarked grid intersection, not a new allowed corner. No new point, label, angle/equality tick, restriction on allowed joins, or paper cut is introduced. Even literal colored grid and illustrative square ink leave all A-D constructions possible, so E remains uniquely correct. The side/diagonal distinction is readable from incidence and the existing grid; no text legend is required.'
design={'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'A','expected_wrong_value':'square',
        'correct_answer':'E','formal_record':eligible['record'],'mathematical_proof':read(OWN/qid/'mathematical_proof.json'),
        'marker_roles':roles,'mechanism':'Red diagonal point pairs have length4, blue side point pairs have length sqrt(8). The specific predicted error is mixing the two point-pair roles and demanding that all emphasized pair lengths be equal for a square, falsely concluding no square (A). The real square requires equality only of its four boundary sides; its diagonals are correctly longer by sqrt(2).',
        'difference_from_old':difference,'human_semantics':human,
        'remaining_risk':'The square may instead be made obvious by these correct geometric relations. Only the frozen two-call observation can evaluate the preset; no repeated old input or posthoc label change is allowed.',
        'candidate_sha256':sha(d1),'plugin_sha256':sha((folder/'plugin.json').read_bytes()),
        'context_sha256':sha((folder/'context.json').read_bytes()),'status':'FROZEN_BEFORE_BOTH_CALLS_PRIMARY_ONLY'}
save(folder/'design.json',design)
save(folder/'reference_transfer.json',{'primary_reference':'Plane308','current_reference_actual_viewed':True,
     'reference_png_sha256':sha((TASK/'references/Plane308/C01.png').read_bytes()),
     'reference_plugin_sha256':sha((TASK/'references/Plane308/C01.json').read_bytes()),
     'migration':'Two true geometric point-pair classes are compared by red and blue, following the current group/contour comparison method rather than an old option/color description.',
     'secondary_reference':'Current Plane427 compares two true equal triangle legs against a different base role; here side and diagonal roles have different actual lengths.'})
save(folder/'history_difference_audit.json',{'created_at':now(),'material_difference':difference,
     'exact_global_previous_candidate_hash_matches':[],'not_a_posthoc_relabel':True,
     'preset_source':'The new 8-vs16 metric role comparison, frozen before this candidate is tested.'})
save(folder/'offline_gates.json',{'created_at':now(),'fresh_schema_sha256':sha((PROJECT/'PlaneGeometry/workbench/plugin.schema.json').read_bytes()),
     'schema_validation':True,'default_normalization_idempotent':True,'frozen_render_normalized_exact':True,
     'original_noop_pixel_equal':True,'repeat_PNG_bytes_exact':True,'repeat_pixel_sha256_exact':True,
     'candidate_sha256':sha(d1),'pixel_sha256':p1,'plugin_sha256':design['plugin_sha256'],
     'environment':environment_versions(),'adapter_manifest':adapter.manifest,'independent_process_replay':'pending'})
checkpoint=read(OWN/'checkpoint.json')
checkpoint['updated_at']=now();checkpoint['question_status'][qid]='third_material_metric_role_design_prepared_visual_replay_pending'
save(OWN/'checkpoint.json',checkpoint,replace=True)
print(json.dumps({'qid':qid,'vid':vid,'image_sha256':sha(d1),'preset':'A','actions':6}))
