from worker_env import *
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer,check_schema
from workbench_io import load_config
config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
adapter=RendererAdapter(config)
for qid,variant in [('Solid186','r05_face_scale_comparison'),('Solid226','r05_front_plane_loss')]:
    e=eligibility(qid);assert e['eligible']
    f=OWN/qid/variant; f.mkdir(parents=True,exist_ok=True)
    save(f/'eligibility_before_design.json',e,True)
    context=adapter.inspect_question(qid)
    assert context==load(OWN/qid/'fresh_context.json')
    native=load(OWN/qid/'native_scene_snapshot.json')
    objects={o['id']:o for o in native['objects']}
    actions=[]; roles=[]
    def style(ids,color,role,receiver):
        for target in ids:
            action={'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
            actions.append(action)
            roles.append({'index':len(actions)-1,'action':action,'source_object':objects[target],
                'information_role':role,'receiver':receiver,'effective':True,
                'purpose':'Actual existing boundary measurement/comparison, no extra geometry or painting condition'})
    R,B='#DC2626','#2563EB'
    if qid=='Solid186':
        style(['panel0e2','panel0e5','panel0e11'],R,'Complete original front-face height, three unit edges','Two-unit height on actual recessed rear face')
        style(['panel1e19','panel1e23'],R,'Actual recessed rear-face height, two unit edges','Three-unit complete original front-face height')
        style(['panel0e0','panel0e19','panel0e32'],B,'Complete original front-face width, three unit edges','Two-unit width on actual recessed rear face')
        style(['panel1e32','panel1e47'],B,'Actual recessed rear-face width, two unit edges','Three-unit complete original front-face width')
        expected,value='D','4 litres'
        mechanism='Two true perpendicular boundary comparisons frame a 3-by-3 original front square and a 2-by-2 new rear square. Predicted specific error: substitute the single-face scale ratio (2/3)^2=4/9 for the complete solid surface ratio, obtaining 9*(4/9)=4 litres, D. This is a face-scale substitution, not volume counting or new-area-only E.'
        difference='The failed first design paired three removed 2-by-2 patches with three new equal 2-by-2 patches and froze E=2 for a changed-area-only error; actual finals C/A. This design introduces the previously unmarked complete outer 3-unit height and width, compares them to one actual recessed 2-unit square, and removes all other patch motifs. Source area changes from a removed 4-unit patch to a complete 9-unit face. New D=4 follows exact 9*(2/3)^2, independent of old observed C/A. Not a cosmetic color/line-width alteration and not the same PNG.'
        semantics='Both open L motifs are two perpendicular sides of real square faces, with existing unit seams retaining true counts 3 and 2. No closed false partition, point, fill, removed cube or cutting line is added. A thin intrinsic edge-color reading leaves the complete surface at 54 and the whole-surface wording unchanged. The compared faces need not be equal; same color identifies measurement direction only. The two face areas genuinely differ 9 versus 4, but this does not change the uniquely correct whole-solid paint answer A.'
    else:
        style(['line_5','line_9','line_17','line_6','line_7'],B,'Outer full 9-by-3 front rectangle of the original solid, existing perimeter portions','Actual one-unit front notch boundary')
        snaps={p['id']:p for p in context['snap_points']}
        action={'type':'add_line','id':'former_front_upper_edge','endpoints':[snaps['blockp63']['xy'],snaps['blockp72']['xy']],
          'color':B,'linestyle':'dashed'}
        actions.append(action)
        roles.append({'index':len(actions)-1,'action':action,'source_points':[snaps['blockp63'],snaps['blockp72']],
          'information_role':'Exactly the missing segment of the original straight front upper perimeter, dashed to indicate removed contour',
          'receiver':'Actual red unit notch U in the same front plane','effective':True,'purpose':'Complete original front rectangle for before/after planar area comparison'})
        style(['line_10','line_12','line_13'],R,'Actual U boundary of the one-square-foot patch missing from the large front face','Full blue original front perimeter')
        expected,value='B','1 less square foot'
        mechanism='The reconstructed full blue front rectangle has real area 9*3=27; the visible front plane with red U notch has real area 26. Predicted error: report this real front-plane-only loss of 1 as the change in total six-sided surface area, B, omitting the changes on other faces. Does not infer a rear cavity or extra cutting.'
        difference='Old historical three-L scheme separated three new faces and froze E; finals C/D. The first new roof design supplied the removed top roof square versus three new faces and also froze E; finals D/C. This new design compares a different actual surface: complete original 9-by-3 front rectangle versus its 26-unit notched front plane. New long exterior bottom/side/top boundary targets establish that plane. Only one former top-front edge is dashed; no roof quadrilateral or three-new-face scheme remains. New preset B=1 less is the exact front-plane loss, not either old observed response and not relabeling E to D.'
        semantics='All blue original rectangle perimeter portions except its missing upper bridge already exist. The single dashed bridge joins exact visible notch-rim endpoints on the original top-front straight edge; the original block is explicitly rectangular. Red U lies on actual visible cut boundaries and does not add a cut. It is a before/after comparison of one real plane. Even when interpreted as edge ink, the dimensions and complete surface are unchanged and the all-six-sides question uniquely gives C. No face fill, text legend, new material, masked dimension, fake closed internal partition or altered visibility.'
    assert len({a.get('target',a.get('id')) for a in actions})==len(actions)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
      'description':'Compare real source and receiving boundaries','intent':'Boundary comparison','params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{qid:context})
    check_schema(plugin,renderer.schema,renderer.schema)
    plugin=renderer.normalize(plugin)
    save(f/'plugin.json',plugin,True);save(f/'context.json',context,True)
    p1,b1,h1=renderer.render(load(f/'plugin.json'))
    p2,b2,h2=renderer.render(load(f/'plugin.json'))
    assert p1==p2==plugin and b1==b2 and h1==h2
    (f/'candidate.png').write_bytes(b1)
    pngsha=sha(f/'candidate.png')
    sameid=[q for q in load(TASK/'history_index.json')['questions'] if q['question_id']==qid][0]
    assert not [t for t in sameid['all_saved_transport_groups_for_question'] if t['image_sha256']==pngsha]
    prior=[]
    for d in (OWN/qid).glob('r05_*/design.json'):
        old=load(d)
        assert old['image_sha256']!=pngsha
        prior.append({'design_path':str(d),'sha256':sha(d),'expected_wrong_answer':old['expected_wrong_answer'],
          'image_sha256':old['image_sha256'],'manual_audit':str(d.parent/'manual_finals_and_binding_audit.json')})
    save(f/'marker_roles.json',roles,True)
    first={'Solid186':'r05_three_patch_changed_area_binding','Solid226':'r05_removed_roof_to_new_cut_faces'}[qid]
    manifest=load(OWN/qid/first/'input_manifest.json')
    manifest.update(at=now(),context_sha256=sha(f/'context.json'),environment=environment())
    for path,h in manifest['source_manifest'].items(): assert sha(PROJECT/path)==h
    save(f/'input_manifest.json',manifest,True)
    save(f/'reference_migration.json',{'reference':'Solid126 current C01','actual_current_PNG_and_plugin_read':True,
      'png_sha256':sha(TASK/'references/Solid126/C01.png'),'plugin_sha256':sha(TASK/'references/Solid126/C01.json'),
      'method':'Red/blue actual boundary source-to-receiver comparison, rather than reusing source option/color descriptions from old18',
      'target_specific_comparison':mechanism,'all_mark_roles':str(f/'marker_roles.json'),'no_fully_overwritten_actions':True},True)
    save(f/'design_difference_audit.json',{'at':now(),'all_same_question_history_read':str(OWN/qid/'complete_history_read_extract.json'),
       'new_failed_history_before_this_design':prior,'substantive_difference':difference,'old_input_not_retried':True,
       'same_formal_question_and_tested_PNG_collision':False,'no_cross_question_borrowing':True},True)
    math=load(OWN/qid/'primary_mathematics.json')
    save(f/'design.json',{'created_at':now(),'question_id':qid,'variant_id':variant,'correct_answer':math['unique_answer'],
      'expected_wrong_answer':expected,'expected_wrong_value':value,'mechanism':mechanism,
      'primary_proof':math['proof'],'math_path':str(OWN/qid/'primary_mathematics.json'),
      'marker_roles_path':str(f/'marker_roles.json'),'human_semantics':semantics,
      'reference_migration_path':str(f/'reference_migration.json'),'difference_path':str(f/'design_difference_audit.json'),
      'image_sha256':pngsha,'pixel_sha256':h1,'plugin_sha256':sha(f/'plugin.json'),'context_sha256':sha(f/'context.json'),
      'status':'FROZEN_PRIMARY_RESEARCH_DESIGN_BEFORE_ANY_CALL','no_user_approval_or_independent_review':True},True)
    save(f/'render_gates.json',{'at':now(),'fresh_schema':True,'default_normalization':True,
      'normalized_plugin_equals_saved':p1==load(f/'plugin.json'),'two_same_process_PNG_bytes_equal':b1==b2,
      'two_pixels_equal':h1==h2,'fresh_noop':load(OWN/qid/'no_op_audit.json'),'image_sha256':pngsha,
      'pixel_sha256':h1,'design_sha256':sha(f/'design.json'),'fresh_process_replay_required_before_API':True},True)
    print(qid,variant,'actions',len(actions),'frozen preset',expected,value,pngsha,flush=True)
cp=load(OWN/'checkpoint.json'); cp.update(at=now(),status='new_information_comparisons_frozen_pending_native_view_and_fresh_replay')
save(OWN/'checkpoint.json',cp)
