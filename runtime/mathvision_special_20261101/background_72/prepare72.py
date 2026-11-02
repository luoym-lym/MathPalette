from tools72 import *
R='#DC2626';B='#2563EB'

def interval(q,oid,start,end,color,wrap=False):
    p=read(HERE/q/'exact_paths.json')[oid][0]
    return {'type':'set_object_style','target':oid,'color':color,'linewidth_pt':1.5,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':wrap}}

def prepare(q):
    if q=='Plane335':
        variant='r72_congruent_apex_wedge_binding';wrong='1'
        actions=[interval(q,t,1/3,2/3,R,True) for t in ['triangle0','triangle1']]
        mechanism='Compare the two existing left-pointing open V motifs of the congruent triangles. The predeclared error treats corresponding geometric tips as the only attachment pair, returning one rather than checking exterior access at both ends of all nine pairs.'
        roles=[{'action_index':0,'source_feature':'The two original sloping edges meeting at left triangle tip 0L.','useful_information':'An open two-edge shape/incident-corner anchor, not a drawn proposed connector. The black vertical edge and its endpoints remain clear.'},{'action_index':1,'receiver_feature':'The two original sloping edges meeting at right triangle tip 1L.','useful_information':'True translated V motif corresponding to the first tip. Same shape identity is real, while equal shape role does not imply an exterior-valid join.'}]
        difference='Old near_apex_three_paths drew three candidate connectors to 1L and was rejected before calls for a contradictory internal connector. Old tangent_endpoint_pairs marked the four far upper/lower endpoints in red/blue and predicted 2, but full raw finals were 7 and 4, both misses. This uses neither new connector nor marked upper/lower tangent endpoint pair. It compares the incident sloping-edge motifs at the two unmarked leftward tips, replacing tangent-count collapse with same-shape-tip attachment-role substitution. Preset 1 is fixed from this new tip-pair hypothesis, not a relabel of either old result.'
        math='All nine segments are independently clipped using exact rational coordinates against both open triangle interiors. Every segment from 0L enters triangle0; 0U-1D and 0D-1U enter triangle1. The other four, 0U-1L,0D-1L,0U-1U,0D-1D, do not enter either interior. Boundary contact does not dissect. Therefore the answer is uniquely 4. Styling original edges cannot remove any of the six vertices or restrict the choices of endpoints.'
        semantics='The task counts possible vertex joins, with no reference to color. Both marked open Vs are true original triangle boundaries; no join, route, equality mark, new vertex or closed new region is added. A literal colored-edge reading preserves exactly the same two triangles and permits all original endpoints; it does not stipulate a red-only attachment rule. Upper/lower and left/right distinctions, interiors and all six vertices stay visible.'
    elif q=='Plane355':
        variant='r72_width_to_fold_measurement_role';wrong='E'
        actions=[interval(q,'o0',.75,1,B),{'type':'set_object_style','target':'o3','color':B,'linewidth_pt':1.5},interval(q,'o0',0,.25,R),{'type':'set_object_style','target':'o2','color':R,'linewidth_pt':1.5}]
        mechanism='Use the true strip-width edge and equal-width turn base as a blue source/receiver pair. Compare the red x-scoped straight edge against the red 45-degree turn diagonal. The predeclared error substitutes the turn diagonal 4sqrt(2) for the requested exposed rectangle length x, choosing E.'
        roles=[{'action_index':0,'source_feature':'Original left vertical side of P, the actual 4 cm strip width.','useful_information':'Anchors the width from the printed 4x13 condition to a visible straight paper edge.'},{'action_index':1,'receiver_feature':'Original dashed horizontal base of the turn, length 4 by the 45-degree fold.','useful_information':'True width-to-width correspondence establishing the 4-by-4 turn square; retains its dashed style.'},{'action_index':2,'source_feature':'Original bottom edge of P, exactly the segment whose span is identified by the existing x dimension below.','useful_information':'Anchors the requested measurement to its actual edge and distinguishes that length from the turn.'},{'action_index':3,'receiver_feature':'Original diagonal fold across the turn square.','useful_information':'The alternate actual length 4sqrt(2) is derived from the same width and 45-degree datum. Red compares this candidate measurement with the x span without adding an equality symbol.'}]
        difference='The old Plane355 prescreen saved no candidate, PNG, preset or API pair. It rejected a contemplated direct diagonal-to-width color match as a false metric relation. This proposal keeps the real equal-width pair blue, with the diagonal distinctly red rather than presenting it as another 4 cm width. Red compares the actual requested x span with the turn diagonal, targeting measurement-role substitution and predeclaring E=4sqrt(2). No relation symbol is added and red does not stipulate equal lengths. Old Plane186/394 prescreens offer no frozen failed image to reuse. This is a new geometry-role hypothesis; actual native clarity is a separate pre-call gate.'
        math='Let y be the exposed height of rectangle Q. Both rectangles have strip width 4, so P=4x and Q=4y. The 45-degree fold turns the strip by 90 degrees, and the transition consumes exactly one width 4 along the original 13 cm strip, giving x+4+y=13. P=2Q gives x=2y, hence 3y=9, y=3 and x=6 uniquely, choice C. The fold diagonal is 4sqrt(2), a different segment from x. These conclusions use the printed width, strip length, fold angle and P=2Q, not display lengths measured from pixels.'
        semantics='No image transformation option is being selected: the choices are numeric lengths. Literal ink on these fixed edges leaves every physical length, strip boundary and the single fold unchanged. Blue marks two true widths. Red groups two visibly different measurements for comparison; common color adds no numerical equality condition. The existing x dimension still spans only P; P,Q,45 degrees and all original solid/dashed lines remain legible. No area paint, new fold, new piece, partition, length label, arrow or false equality is introduced.'
    else:raise ValueError(q)
    d=HERE/q/variant;d.mkdir(exist_ok=False)
    e=eligibility(q);write(d/'eligibility_before_design.json',e);assert e['eligible']
    assigned=next(x for x in read(BASE/'background_72_assignment.json')['questions'] if x['question_id']==q)
    source_checks={k:sha(v['path'])==v['sha256'] for k,v in assigned['source_assignment_question']['source_inputs'].items()}
    assert all(source_checks.values())
    write(d/'wrong_preset.json',{'question_id':q,'variant_id':variant,'created_at':now(),'expected_wrong_answer':wrong,'mechanism':mechanism,'immutable_before_calls':True})
    write(d/'design_difference_audit.json',{'question_id':q,'variant_id':variant,'created_at':now(),'substantive_difference':difference,'old_history_inventory':str(HERE/'old_history_inventory.json'),'all_old_full_finals_manually_read':True,'old_final_values_335':['7','4'],'old_preset_335':'2','old_preset_hits_335':[False,False],'new_wrong_answer':wrong,'source_hashes_match_assignment':source_checks,'neither_retest_nor_cross_ID_copy':True,'not_a_claim_of_effectiveness':True})
    adapter,Renderer,cfg=setup();context=adapter.inspect_question(q)
    write(d/'fresh_context.json',context)
    renderer=Renderer(cfg,adapter,{q:context})
    submitted={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'','params':{'actions':actions}}
    write(d/'plugin_submitted.json',submitted)
    plugin=renderer.normalize(submitted);write(d/'plugin.json',plugin)
    _,data,pix=renderer.render(plugin,frozen=True);(d/'candidate.png').write_bytes(data)
    _,again,pix2=renderer.render(plugin,frozen=True);(d/'repeat.png').write_bytes(again)
    assert data==again and pix==pix2
    old_images=[r for r in read(HERE/'old_history_inventory.json') if r['path'].endswith('.png')]
    assert sha(d/'candidate.png') not in [r['sha256'] for r in old_images]
    write(d/'design.json',{'question_id':q,'variant_id':variant,'created_at':now(),'expected_wrong_answer':wrong,'formal_correct_answer':e['record']['answer'],'mechanism':mechanism,'primary_unique_math_proof':math,'marker_roles':roles,'human_semantics':semantics,'candidate_sha256':sha(d/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':sha(d/'plugin.json'),'wrong_preset_sha256':sha(d/'wrong_preset.json'),'design_difference_audit_sha256':sha(d/'design_difference_audit.json'),'approval_status':'PRIMARY ONLY, pending actual native visual gate; no independent review or user approval'})
    write(d/'render_check.json',{'normalized_frozen_roundtrip':renderer.normalize(plugin)==plugin,'no_op_formal_pixels_equal':True,'baseline':str(HERE/q/'baseline_check.json'),'repeat_bytes_equal':data==again,'candidate_sha256':sha(d/'candidate.png'),'repeat_sha256':sha(d/'repeat.png'),'old_images_hash_different':True,'strict_own_directory_write_guard':True,'isolation':ISOLATION if 'ISOLATION' in globals() else str(HERE/'render_tmp')})
    import matplotlib.pyplot as plt
    plt.close('all');del data,again,renderer,adapter,context;gc.collect()
    print(q,variant,'frozen; no API; actual native visual gate pending',flush=True)

if __name__=='__main__':prepare(sys.argv[1])
