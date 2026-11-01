from tools_local import *
from partial_style import object_paths
from fold_audit import F,point
qid='Solid170';vid='opposite_to_adjacent_hole_pairs';check=eligibility(qid);assert check['eligible'],check
RED='#DC2626';BLUE='#2563EB'
groups=[(RED,['hole0_1','hole1_1','Aboundary9','Aboundary28']),(BLUE,['hole2_1','hole3_1','Aboundary39','Aboundary56'])]
targets=[(t,c) for c,ts in groups for t in ts]
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Pair the crossbars of the upper and lower cube openings with the two adjacent seam openings in net A.','intent':'Predeclared false opposite-to-adjacent opening correspondence A.','params':{'actions':[{'type':'set_object_style','target':t,'color':c,'linewidth_pt':2} for t,c in targets]}}
folder=TASK/qid/vid;report=AD.render_candidate(plugin,folder)
metadata=AD.inspect_question(qid);renderer=PluginRenderer(AD.config,AD,{qid:metadata})
normalized=json.loads((folder/'plugin.json').read_text(encoding='utf-8'));n2,data2,pixels2=renderer.render(normalized,frozen=True)
assert normalized==n2 and data2==(folder/'candidate.png').read_bytes() and pixels2==report['pixel_sha256']
capture=AD.scene(qid)
try:
    capture.fig.canvas.draw();paths={t:[{'id':p['id'],'sha256':p['sha256'],'closed':p.get('closed')} for p in object_paths(capture,t)] for t,c in targets}
finally:capture.close()
folded_seams={str(x):[point((max(0,min(3,x-1)),0),(x,y)) for y in (0,1)] for x in (0,1,2,3,4)}
roles=[]
for color,ts in groups:
    for i,t in enumerate(ts):
        roles.append({'target':t,'color':color,'role':('One of the two cross-face endbars belonging to '+('upper' if color==RED else 'lower')+' actual cube opening; original visibility preserved.' if i<2 else 'One of the two endbars of the proposed '+('left' if color==RED else 'right')+' full seam opening in A; both are required to identify the complete two-face opening rather than just a nearby cube edge.')})
design={'question_id':qid,'variant_id':vid,'expected_wrong_answer':'A','correct_answer':'C','created_at':datetime.now(timezone.utc).isoformat(),'mechanism':'Two distinct color pairs map actual opposite cube-edge openings to A adjacent belt-seam openings. Each pair identifies both cross-face crossbars of one opening. The intended specific error is matching the two individual cutout shapes while failing to preserve their global opposite-edge relation. No option letter, whole face, fill or unrelated boundary is colored.','mathematical_proof':'Given holes lie across parallel edges x=15,z=9 and x=18,z=6, so they are diagonally opposite members of the four-edge belt. In net A the complete straddling openings are at belt seams x=1 and x=2, adjacent. D uses x=1 and closing seam0/4, also adjacent. C uses seam2 and closing seam0/4, opposite, and each has both face halves. B has one complete straddling seam1 opening plus two unmatched single-face notches at far top/bottom edges; those do not give the two depicted complete opposite-edge openings. E holes lie within faces, not across creases. Hence C uniquely folds into the shown cube; equal colors are not added mathematical adjacency conditions.','marker_roles':roles,'folded_unit_belt_seams':folded_seams,'formal_record':AD.records[qid],'target_path_fingerprints':paths,'status':'PRIMARY_DESIGN_ONLY; NEW_PARENT_INDEPENDENT_REVIEW_REQUIRED'}
write(folder/'design.json',design);write(folder/'eligibility_before_design.json',check)
write(folder/'normalized_frozen_replay.json',{'normalized_roundtrip_equal':True,'png_bytes_equal':True,'pixel_sha256':pixels2,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'target_path_fingerprints':paths})
print(json.dumps({'folder':str(folder),'png_sha256':file_hash(folder/'candidate.png'),'markers':len(targets),'expected_wrong_answer':'A'}))
