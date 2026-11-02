from worker_env import *
from itertools import product
from fractions import Fraction
from collections import Counter
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer, check_schema
from workbench_io import load_config
from renderer_adapter import scene_png

def boundary(cells):
    result=set()
    for cell in cells:
        for axis in range(3):
            for side in (-1,1):
                neighbor=list(cell); neighbor[axis]+=side
                if tuple(neighbor) not in cells:
                    plane=list(cell)
                    if side==1: plane[axis]+=1
                    result.add(tuple(plane)+(axis,side))
    return result

def proof(qid):
    if qid=='Solid186':
        original=set(product(range(3),repeat=3))
        removed={(x,y,z) for x,y,z in original if x>=1 and y<2 and z>=1}
        reason='The 3 by 3 by 3 cube loses precisely the 2 by 2 by 2 front-right-top corner. The three removed exterior patches each have area 4. The three new inner patches at x=1, y=2 and z=1 each have area 4. The bottom remains 9 and is included. Unchanged exposed area 42 plus new 12 gives 54. Equal complete areas require 9 litres, uniquely choice A.'
    else:
        original=set(product(range(1),range(9),range(3)))
        removed={(0,4,2)}
        reason='Original block is 1 by 9 by 3 feet; its complete area is 2(9+3+27)=78. The unit cube at y=4..5,z=2..3 spans the full x thickness. Removed surfaces are top z=3, front x=1 and back x=0, each area 1. Newly exposed are floor z=2 and side walls y=4 and y=5, each area 1. The bottom remains 9 and is included. Delta=-3+3=0, uniquely C. Treating the notch as a corner pocket or leaving a rear wall contradicts the width-1 given.'
    after=original-removed
    beforefaces,afterfaces=boundary(original),boundary(after)
    lost,new=beforefaces-afterfaces,afterfaces-beforefaces
    out={'question_id':qid,'method':'Independent exact oriented unit-face enumeration, all six directions; not using stored answer/model output',
         'original_voxels':sorted(original),'removed_voxels':sorted(removed),'remaining_voxels':sorted(after),
         'all_original_unit_faces':sorted(beforefaces),'all_remaining_unit_faces':sorted(afterfaces),
         'lost_faces':sorted(lost),'new_faces':sorted(new),'preserved_faces':len(beforefaces & afterfaces),
         'before_area':len(beforefaces),'after_area':len(afterfaces),'lost_area':len(lost),'new_area':len(new),
         'by_oriented_direction_before':{str(k):v for k,v in Counter((f[-2],f[-1]) for f in beforefaces).items()},
         'by_oriented_direction_after':{str(k):v for k,v in Counter((f[-2],f[-1]) for f in afterfaces).items()},
         'proof':reason,'unique_answer':'A' if qid=='Solid186' else 'C',
         'viewing_basis':'Actual source JPG and formal PNG inspected; native scene and current dedicated bridge context read',
         'geometry_projection_visibility_separate':True}
    assert (len(beforefaces),len(afterfaces),len(lost),len(new))==((54,54,12,12) if qid=='Solid186' else (78,78,3,3))
    if qid=='Solid186':
        out['complete_surface_paint_litres']=str(Fraction(9*len(afterfaces),len(beforefaces)))
        out['wrong_subtask_new_faces_only_litres']=str(Fraction(9*len(new),len(beforefaces)))
    return out

config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
adapter=RendererAdapter(config)
for qid in ('Solid186','Solid226'):
    current=eligibility(qid)
    assert current['eligible']
    variant='r05_three_patch_changed_area_binding' if qid=='Solid186' else 'r05_removed_roof_to_new_cut_faces'
    folder=OWN/qid/variant
    folder.mkdir(parents=True,exist_ok=True)
    save(folder/'eligibility_before_design.json',current,True)
    math=proof(qid)
    save(OWN/qid/'primary_mathematics.json',math,True)
    context=adapter.inspect_question(qid)
    assert context==load(OWN/qid/'fresh_context.json')
    renderer=PluginRenderer(config,adapter,{qid:context})
    native=load(OWN/qid/'native_scene_snapshot.json')
    objects={o['id']:o for o in native['objects']}
    actions=[];roles=[]
    def style(ids,color,role,pair):
        for target in ids:
            action={'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
            actions.append(action)
            roles.append({'index':len(actions)-1,'action':action,'source_object':objects[target],
              'information_role':role,'comparison_pair':pair,'receiver':pair,'purpose':'Trace an actual area-patch boundary for comparison; does not restrict which surfaces count',
              'effective':True,'no_new_condition':True})
    R,B='#DC2626','#2563EB'
    if qid=='Solid186':
        style(['panel0e24','panel0e42','panel0e10','panel0e15'],R,'Original top removed 2 by 2 patch, two open sides','old top to new floor')
        style(['panel1e28','panel1e41','panel1e2','panel1e17'],R,'New horizontal 2 by 2 cut floor, corresponding open sides','old top to new floor')
        style(['panel0e20','panel0e33','panel0e6','panel0e12'],B,'Original front removed 2 by 2 patch, bottom and left sides','old front to new rear wall')
        style(['panel1e32','panel1e47','panel1e19','panel1e23'],B,'New rear 2 by 2 wall, bottom and left sides','old front to new rear wall')
        style(['panel0e44','panel0e53','panel0e40','panel0e45'],B,'Original right removed 2 by 2 patch, top and front sides','old right to new left wall')
        style(['panel1e13','panel1e22','panel1e8','panel1e15'],B,'New left 2 by 2 wall, top and front sides','old right to new left wall')
        preset='E';value='2 litres'
        mechanism='Matching the old removed patches to the three new patches isolates the changed-area subtotal 12. Predicted error: answer the new-cut-surfaces-only subtask, 9*(12/54)=2 litres, instead of painting the entire remaining surface. The actual entire-surface wording is retained. No volume heuristic, rounding or altered painting condition.'
        difference='No saved design or actual transport for Solid186 in the history index. Prior prescreens considered the correct unchanged-area correspondence and a non-option 19/27 volume heuristic, but did not construct or test this explicit three-patch old/new boundary relation with a frozen E=2 new-area-only preset. New cue and exact arithmetic are recorded before calls.'
        semantics='Every colored segment is an existing unit seam or existing patch rim. All motifs are open, and uncolored unit seams and the full outside silhouette remain. Even if the colors are intrinsic thin edge ink, they neither add material nor define a different painted subset: the question says surface of the shape, not colored faces. No face fill, mask, new cut or label is added. The entire solid still has exactly 54 unit faces.'
    else:
        style(['line_2','line_14'],R,'Existing two transverse top rims bound the top square removed from the original block','former roof square versus three new faces')
        snaps={p['id']:p for p in context['snap_points']}
        for lid,a,b in [('former_roof_back','blockp62','blockp66'),('former_roof_front','blockp63','blockp72')]:
            action={'type':'add_line','id':lid,'endpoints':[snaps[a]['xy'],snaps[b]['xy']],'color':R,'linestyle':'dashed'}
            actions.append(action)
            roles.append({'index':len(actions)-1,'action':action,'source_points':[snaps[a],snaps[b]],
              'information_role':'Former top perimeter of the explicitly original rectangular block, not a new surface/cut; dashed distinguishes removed contour',
              'receiver':'blue three new cut faces','comparison_pair':'former roof square versus three new faces','effective':True,'no_new_condition':True})
        style(['line_10','line_13','line_16'],B,'Existing visible vertical cut-wall boundary fragments distinguish both unit end walls','former roof square versus three new faces')
        style(['line_11','line_12'],B,'Existing partly occluded rear floor edge and complete front floor edge locate the new unit floor','former roof square versus three new faces')
        preset='E';value='2 more square feet'
        mechanism='The explicit red former roof perimeter supplies a real removed unit-square source that the old attempt lacked; blue locates the three new faces. Predicted error: compare only red roof area 1 against three blue new unit faces area 3, overlooking the old front/back patches, so +2, choice E. This is a new removed-versus-added relation, not another three-L face-color variant.'
        difference='Old three_new_face_visibility_binding used only six existing edges, three colors, to separate three new faces; preset E, raw finals C and D/1 more, so failed and must never be retested. Here two precisely snapped dashed former top edges complete the true original roof footprint, paired with real new faces. The former roof source is new informational content. Labels, full thickness and all original visible fragments remain. Not a color/linewidth-only change; do not relabel to old D.'
        semantics='The problem explicitly contrasts an original rectangular block with a cut-out unit cube. Red dashed segments retrace precisely the former straight top edges between actual notch-rim endpoints; they are the missing contour of that stated original block. No arbitrary cut or extra object is invented. Existing solid rims remain solid, and the new floor and wall edges remain visible. In an ink-on-edges reading, ink does not change area or all-six-surfaces wording. A surviving roof covering the cut-out cube would contradict the explicit cube-cut-out condition, not form a competing lawful solid. No painted subset or additional text legend.'
    assert len({a.get('target',a.get('id')) for a in actions})==len(actions)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':'Compare actual removed outer patch boundaries with newly exposed cut-face boundaries',
            'intent':'Source-to-new-surface boundary comparison','params':{'actions':actions}}
    check_schema(plugin,load(PROJECT/'SolidGeometry/workbench/plugin.schema.json'),load(PROJECT/'SolidGeometry/workbench/plugin.schema.json'))
    normalized=renderer.normalize(plugin)
    save(folder/'plugin.json',normalized,True)
    save(folder/'context.json',context,True)
    p1,data1,px1=renderer.render(load(folder/'plugin.json'))
    p2,data2,px2=renderer.render(load(folder/'plugin.json'))
    assert p1==p2==normalized and data1==data2 and px1==px2
    (folder/'candidate.png').write_bytes(data1)
    save(folder/'marker_roles.json',roles,True)
    source_manifest={str(p.relative_to(PROJECT)):sha(p) for p in [PROJECT/'dataset_tools/mathvision_workbench.py',OLD/'delivery_bridge_adapter.py',OLD/'runtime_isolation.py']+[PROJECT/'SolidGeometry/workbench'/f for f in ('render_plugins.py','renderer_adapter.py','plugin.schema.json','partial_style.py','workbench_io.py','config.json','quick_test.py')]}
    save(folder/'input_manifest.json',{'at':now(),'source_manifest':source_manifest,'geometry_sha256':sha(OWN/qid/'native_scene_snapshot.json'),'context_sha256':sha(folder/'context.json'),'environment':environment()},True)
    history=load(TASK/'history_index.json')
    hq=next(q for q in history['questions'] if q['question_id']==qid)
    png_sha=sha(folder/'candidate.png')
    old_equal=[g for g in hq['all_saved_transport_groups_for_question'] if g['image_sha256']==png_sha]
    assert not old_equal,'Do not retest same question/input'
    save(folder/'design_difference_audit.json',{'history_read':str(OWN/qid/'complete_history_read_extract.json'),'prior_designs':hq['designs'],'substantive_difference':difference,'same_question_tested_PNG_collision':old_equal,'old_frozen_input_not_retried':True,'no_cross_question_evidence_reuse':True},True)
    save(folder/'reference_migration.json',{'reference':'Solid126 current user C01','reference_png_sha':sha(TASK/'references/Solid126/C01.png'),'reference_plugin_sha':sha(TASK/'references/Solid126/C01.json'),'actual_PNG_viewed':True,'method':'Red true removed-versus-new-area boundaries and blue depth/wall edges; source and receiver have explicit roles','discarded_reference_action':'Earlier red removed2 is fully overwritten by blue; not migrated','new_roles':str(folder/'marker_roles.json'),'old18_not_authority':True},True)
    save(folder/'design.json',{'created_at':now(),'question_id':qid,'variant_id':variant,'correct_answer':math['unique_answer'],
       'expected_wrong_answer':preset,'expected_wrong_value':value,'mechanism':mechanism,
       'primary_proof':math['proof'],'math_path':str(OWN/qid/'primary_mathematics.json'),
       'marker_roles_path':str(folder/'marker_roles.json'),'human_semantics':semantics,
       'reference_migration_path':str(folder/'reference_migration.json'),'difference_path':str(folder/'design_difference_audit.json'),
       'image_sha256':png_sha,'pixel_sha256':px1,'plugin_sha256':sha(folder/'plugin.json'),'context_sha256':sha(folder/'context.json'),
       'status':'FROZEN_PRIMARY_RESEARCH_DESIGN_BEFORE_ANY_CALL','no_user_approval_or_independent_review':True},True)
    save(folder/'render_gates.json',{'at':now(),'fresh_schema':True,'default_normalization':True,
        'normalized_plugin_equals_saved':p1==load(folder/'plugin.json'),'two_same_process_PNG_bytes_equal':data1==data2,
        'two_pixels_equal':px1==px2,'fresh_noop':load(OWN/qid/'no_op_audit.json'),
        'image_sha256':png_sha,'pixel_sha256':px1,'design_sha256':sha(folder/'design.json'),
        'fresh_process_replay_required_before_API':True},True)
    print(qid,variant,'actions',len(actions),'preset',preset,value,'SHA',png_sha,flush=True)
save(OWN/'checkpoint.json',{'at':now(),'status':'two_designs_frozen_pending_native_view_and_fresh_replay','assigned':['Solid186','Solid226'],'calls':0,'questions':{q:{'status':'frozen_pre_API_candidate'} for q in ('Solid186','Solid226')}})
