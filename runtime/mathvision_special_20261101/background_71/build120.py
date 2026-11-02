from env71 import *
import gc

Q='Solid120'
VID='r71_visible_tick_count_to_halfturn_unit'
DEST=OWN/Q/VID
try:
    if (OWN/'local_failure.json').exists(): raise RuntimeError('Existing local failure prohibits further work/calls')
    DEST.mkdir(parents=True,exist_ok=False)
    current=eligibility(Q)
    assert current['eligible']
    save(DEST/'eligibility_before_design.json',current)
    install_render()
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    from workbench_io import load_config,pixel_hash
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths
    config=load_config()
    adapter=RendererAdapter(config)
    context=adapter.inspect_question(Q)
    save(DEST/'context.json',context)
    capture=adapter.scene(Q)
    try:
        noop=png_bytes(capture)
        ids=[f'tick0_{i}' for i in range(1,12)]+['rim0']
        paths={target:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(capture,target)] for target in ids}
    finally: capture.close()
    assert pixel_hash(noop)==context['original_pixel_sha256']
    (DEST/'no_op.png').write_bytes(noop)
    save(DEST/'frozen_paths.json',paths)
    actions=[{'type':'set_object_style','target':target,'color':'#DC2626','linewidth_pt':1.5} for target in ids]
    plugin={'plugin_schema_version':'1.0.0','question_id':Q,'category':'C','operation':'C_manual','description':VID,'intent':'','params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{Q:context})
    normalized=renderer.normalize(plugin)
    assert renderer.normalize(normalized)==normalized
    save(DEST/'plugin_submitted.json',plugin)
    save(DEST/'plugin.json',normalized)
    _,first,px=renderer.render(normalized,frozen=True)
    _,second,px2=renderer.render(normalized,frozen=True)
    assert first==second and px==px2
    (DEST/'candidate.png').write_bytes(first)
    (DEST/'repeat.png').write_bytes(second)
    scene=read(PROJECT/'SolidGeometry/dataset_generator/scenes/Solid120.json')
    obj={x['id']:x for x in scene['objects']}
    assert obj['rim0']['domain_deg']==[180,360]
    roles=[]
    for i,action in enumerate(normalized['params']['actions']):
        target=action['target']
        role=(f'Source member {i+1} of the eleven existing numbered front ticks. Its one-for-one membership in the selected count set supplies the incorrect count-based unit, rather than selecting a misaligned value in another turn.' if i<11 else 'Receiver: the existing radius-one bottom rim is exactly the visible 180-degree semicircle. Its shared red appearance associates the count of eleven front ticks with one half-revolution; this is the specific count-to-length transfer being tested.')
        roles.append({'action_index':i,'action':action,'role':role,'original_object':next(o for o in context['objects'] if o['id']==target),'native_3D_object':obj[target],'exact_paths':paths[target]})
    proof='A regular measuring tape advances by a fixed number per full turn. Actual same-azimuth printed pairs 1/22, 6/27 and 11/32 all give 21. The requested tick is two full turns above 6, so 6+2*21=48 uniquely. The original scene confirms equal x/y coordinates for each same-phase pair; the rise is0.7 per turn. The selected rim is only the180..360-degree bottom semicircle. Eleven visible numbered ticks are eleven objects, not eleven tape-length intervals along that semicircle. Values1..11 span ten units; the extreme ticks are inset from the silhouettes by pi/42 each, so the entire half-turn spans10.5 units. This agrees with21 per whole turn. Styling their color cannot make11 a new length given.'
    hypothesis='Count the eleven red existing ticks as eleven length units of the red true half-circle, double to22 per revolution, then extrapolate two turns from6:6+2*(2*11)=50. The error is cardinality-to-interval length plus half-to-whole calibration. It does not use6-to28 correspondence: no middle-turn or target tick is colored and no inter-turn guide/node is added.'
    difference='Every old Solid120/Solid138 plugin colors or dots the lower6, misphased middle28, and requested tick, with optional inter-turn dashed guides/intermediate dot. New source is the ENTIRE eleven-member lower tick count; new receiver is the actual existing bottom semicircular rim. Old tick0_6 is present only as one undistinguished counted member among11, not a singled calibration anchor. No tick1_7 (28), target tick, node, guide or old failed PNG is reused. The same numerical preset50 now follows the independently stated11-count/half-turn derivation, not an observed old final. Incidental old full-raw mentions of11/12 circumferences have been read and disclosed, but had no matching count-to-semicircle plugin/preset design; none are relabelled as success.'
    semantics='The task asks for a number on a fixed measuring tape, not a transformed picture or the number of red marks. All existing ticks remain exactly eleven on each original row, all printed numbers stay black/readable, and every tape boundary remains in place. Red is shared comparison styling, not an equality/length relation symbol. Even if red is treated as actual ink on these fixed objects, it does not change their readings, number, spacing or winding. No added point, ruler tick, arrow, text, polygon, paint fill or partition is present. Unlike a uniform whole-figure recolor, one selected source count set is bound to a distinct actual semicircle receiver; all upper rows and boundaries stay black. Primary targeting judgment only; independent reviewers may still assess its strength.'
    save(DEST/'design_difference_audit.json',{'at':now(),'question_id':Q,'variant_id':VID,'old_history':'../../old_designs_plugins_reviews.json','old_full_raw':'../../old_full_raw_responses.json','substantive_difference':difference,'specific_new_information_transfer':hypothesis,'expected_wrong_answer':'50','cosmetic_repeat':False,'reused_old_image':False,'posthoc_preset':False,'candidate_sha256':sha(DEST/'candidate.png'),'plugin_sha256':sha(DEST/'plugin.json'),'frozen_before_any_calls':True})
    save(DEST/'design.json',{'question_id':Q,'variant_id':VID,'created_at':now(),'expected_wrong_answer':'50','correct_answer':'48','primary_unique_math_proof':proof,'wrong_answer_derivation':hypothesis,'substantive_difference':difference,'human_semantics':semantics,'every_marker_roles':roles,'candidate_sha256':sha(DEST/'candidate.png'),'pixel_sha256':px,'plugin_sha256':sha(DEST/'plugin.json'),'context_sha256':sha(DEST/'context.json'),'frozen_paths_sha256':sha(DEST/'frozen_paths.json'),'review_level':'PRIMARY design; parent NEW independent review required if two hits; no approval/Pass/Collect/delivery'})
    save(DEST/'render_check.json',{'at':now(),'no_op_formal_pixels_equal':True,'schema_defaults_normalized':True,'normalization_idempotent':True,'repeat_PNG_byte_identical':True,'repeat_pixels_identical':True,'candidate_sha256':sha(DEST/'candidate.png'),'design_sha256':sha(DEST/'design.json'),'actual_PNG_manual_view_still_required':True,'API_calls':0})
    save('prepared_candidates.json',[{'question_id':Q,'variant_id':VID,'path':str(DEST),'image_sha256':sha(DEST/'candidate.png'),'design_sha256':sha(DEST/'design.json'),'expected_wrong_answer':'50'}])
    print(Q,VID,'frozen;',len(actions),'original-object styles; no calls',flush=True)
except BaseException as exc:
    save('local_failure.json',{'at':now(),'stage':'new_candidate_build','error_type':type(exc).__name__,'error':str(exc),'stop_subsequent_calls':True,'API_calls':0})
    raise
