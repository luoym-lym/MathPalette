from env47 import *
import json
from datetime import datetime,timezone
from inspect47 import eligibility,BRANCH
sys.path.insert(0,str(BRANCH/'workbench'))
from workbench_io import load_config,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.mathvision_workbench import png_bytes

qid='Plane456';variant='r47_equal_legs_triangle_area_to_square';root=OWN/qid/variant
preset='C'
hypothesis='The bottom shaded right triangle I and the entire shaded square II have two EXACTLY congruent consecutive unit boundary legs under translation(3,1). Pair those two legs red/blue. Proposed error transfers the source triangle area1/2 to the full square through the matching open L and ignores their different closure. I and III retain correct total1 while II is wrongly counted1/2, selecting C.'
difference='The earlier NEW r47_rotated_square_unit_transfer matched square II to smaller rotated diamonds III, testing a scale error with presetB and observedE/B (MISS). This new rule instead matches the unit right triangle I to unit square II by exactly equal-length translated legs, testing triangle-versus-square area closure. Marks move to two different source/receiver figures and a different geometric invariant. C was not an observed final in the previous pair. No old PNG, preset, raw response or primary report is edited or retested.'
root.mkdir(exist_ok=False)
e=eligibility(qid);assert e['eligible'];dump(root/'eligibility_before_design.json',e)
old=OWN/qid/'r47_rotated_square_unit_transfer'
dump(root/'design_difference_audit.json',{'created_at':datetime.now(timezone.utc).isoformat(),'question_id':qid,'variant_id':variant,'substantive_difference':difference,'new_geometry_error_rule':hypothesis,'expected_wrong_answer':preset,'previous_new_variant':{'design_path':str(old/'design.json'),'design_sha256':sha(old/'design.json'),'image_sha256':sha(old/'candidate.png'),'manual_review_path':str(old/'manual_final_review.json'),'old_preset':'B','old_finals':['E','B'],'status':'MISS'},'prospective_target_not_posthoc_relabel':True})
config=load_config();config['runtime_dir']=str(OWN/'extra_wb_runtime_unused');config['output_dir']=str(OWN/'extra_wb_output_unused')
adapter=RendererAdapter(config);m=adapter.inspect_question(qid);scene=adapter.scene(qid)
actions=[];roles=[];paths={}
try:
    scene.fig.canvas.draw();noop=png_bytes(scene)
    assert pixel_hash(noop)==m['original_pixel_sha256']
    for target,index,color,role in [('grayIbottom',0,'#DC2626','Source triangle I bottom unit leg; one actual half-square, area1/2.'),('grayIbottom',1,'#2563EB','Same source triangle vertical unit leg; the black hypotenuse still distinguishes triangle from whole square.'),('grayII',0,'#DC2626','Receiver whole shaded square II bottom unit side, exact translation(3,1) of the red source leg.'),('grayII',1,'#2563EB','Receiver whole shaded square II right unit side, exact translation(3,1) of the blue source leg. Copying source area is false despite this true local L match.')]:
        p=object_paths(scene,target)[0];n=len(p['segments'])
        actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':index/n,'end':(index+1)/n,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'role':role,'actual_selected_controls':[p['segments'][index]['control'].tolist()]})
        paths[target]=[{k:pp[k] for k in ['id','sha256','closed']}|{'controls':[x['control'].tolist() for x in pp['segments']]} for pp in object_paths(scene,target)]
finally:scene.close()
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
renderer=PluginRenderer(config,adapter,{qid:m});plugin=renderer.normalize(plugin)
norm,a,px=renderer.render(plugin,frozen=True);norm2,b,px2=renderer.render(plugin,frozen=True)
assert a==b and px==px2 and norm==plugin==norm2
(root/'candidate.png').write_bytes(a);(root/'repeat.png').write_bytes(b)
dump(root/'plugin.json',plugin);dump(root/'context.json',m);dump(root/'path_fingerprints.json',paths)
dump(root/'design.json',{'question_id':qid,'variant_id':variant,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':preset,'formal_correct_answer':'A','geometric_error_rule':hypothesis,'material_difference':difference,'per_marker_roles':roles,'primary_math_proof':json.loads((OWN/qid/'math_proof.json').read_text(encoding='utf-8')),'actual_equal_leg_translation':[3,1],'source_area':'1/2','receiver_true_area':'1','wrong_totals_I_II_III':['1','1/2','1'],'plugin_path':str(root/'plugin.json'),'plugin_sha256':sha(root/'plugin.json'),'image_path':str(root/'candidate.png'),'image_sha256':sha(root/'candidate.png'),'pixel_sha256':px,'context_sha256':sha(root/'context.json'),'path_fingerprints_sha256':sha(root/'path_fingerprints.json'),'original_approval_content_sha256':e['current_content_sha256'],'approval_status':'UNREVIEWED; primary only; no Pass/Collect/independent second review'})
dump(root/'render_check.json',{'baseline_pixel_equal':True,'schema_and_normalization_pass':True,'two_consecutive_offline_PNG_bytes_equal':True,'png_sha256':sha(root/'candidate.png'),'repeat_sha256':sha(root/'repeat.png'),'pixel_sha256':px,'all_actions':plugin['params']['actions'],'per_marker_roles':roles,'native_visual_review_done':False})
extra={'question_id':qid,'variant_id':variant,'definition':[variant,preset,hypothesis,difference],'directory':str(root)}
dump(OWN/'additional_designs.json',[extra])
needle="root=next((OWN/qid).glob('r47_*'))"
for source,name in [('run47.py','run47_extra.py'),('record47.py','record47_extra.py')]:
    code=(OWN/source).read_text(encoding='utf-8');assert code.count(needle)==1
    code=code.replace(needle,"root=OWN/qid/'"+variant+"';assert qid=='Plane456'")
    (OWN/name).write_text(code,encoding='utf-8',newline='\n')
code=(OWN/'audit47.py').read_text(encoding='utf-8')
comment='Native768: Four visible red/blue unit sides form two congruent translated open Ls, on the original lower shaded triangle I and full shaded square II. The black triangle hypotenuse and every original partition remain readable. The I upper triangle and both III shaded diamonds remain unchanged. Gray/white membership, labels I/II/III and the correct all-equal answer A are unambiguous. Some source/receiver centerline black overdraw leaves antialiased colored margins, as in the first design; actual colored pixels and native appearance are checked. No point, relation symbol, closed source partition, fill or text is added.'
code=code.replace("if __name__=='__main__':main()", "DEFS={'Plane456': ["+repr(variant)+"]}\nCOMMENTS['Plane456']="+repr(comment)+"\nif __name__=='__main__':main()")
code=code.replace("OWN/'all_prior_binding_inventory.json'","OWN/'all_prior_binding_inventory_extra.json'")
(OWN/'audit47_extra.py').write_text(code,encoding='utf-8',newline='\n')
print(json.dumps({'new_variant':variant,'preset':preset,'actions':len(actions),'source_receiver_exact_translation':[3,1],'PNG':str(root/'candidate.png')},ensure_ascii=False))
