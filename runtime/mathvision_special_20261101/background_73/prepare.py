from bootstrap import HERE,PROJECT,TASK,renderer_setup
from audit import read,save,sha,eligibility,stamp
import sys,json,hashlib,copy,gc

SPECS={
'Solid227':{
 'id':'r73_cross_role_inverse_volume',
 'preset':'C',
 'mechanism':'Pair given radius10 withC axial height10 in red and given axial height5 withC radius5 in blue. The true numeric-role swap invites reversing the requested comparison: Vgiven/VC=(10/5)^2*(5/10)=2, leadingC althoughVC/Vgiven=1/2. The hypothesis is inverse comparison after cross-role matching, not the old linear radius-volume rule.',
 'difference':'Old design pairs given/A radii and equal heights, testslinear V proportionalr*h, presetA, fullfinalsE/B. This design leavesA entirely black, usesC with two CROSS-ROLE dimension matches, and predeclares the inverse-volume criterion selectingC. Receiver geometry, factor binding and error direction differ. Same colors/widths do not constitute the novelty; the actual source/receiver dimension roles do.',
 'styles':[('line_4','#DC2626','Source given radial10, center-to-rim, compared toC axial10.'),('line_17','#DC2626','ReceiverC left silhouette, true axial height10, cross-role to given radius10.'),('line_2','#2563EB','Source given axial height5, compared toC radial5.'),('line_19','#2563EB','ReceiverC radial5, center-to-rim, cross-role to given axial5.')],
 'semantics':'Numerical geometry volume comparison, not printed-picture transformation. Red and blue identify existing length-bearing lines; all labels remain and both paired numeric values are actually equal10 or5. No equality/angle glyph or changed length is introduced. Human can still distinguish radius from axial height by endpoints and orientation and computeB. Coloring has no physical-volume effect.'},
'Solid235':{
 'id':'r73_unit_top_faces_underside_omission',
 'preset':'B',
 'mechanism':'Match the original unit square top-face corner to two existing adjacent unit top edges on each output slabC,B,A,D. This transfers the real unit-face area to four exposed top surfaces. The intended error inventories these one-sided visible unit faces but omits all four exposed undersides:4 tops+3 vertical area=7, presetB instead of11.',
 'difference':'Old design styles source horizontal cut traces line13/line11 and output narrow contact-top edges lowerline10/lowerline2, falsely treating sideglue as fullunitface, presetA, finals11/6. New source is the ORIGINAL TOP unit square (line1/line3), receivers are the actual TOP corners on ALL FOUR output pieces, and no old styled edge is reused. Error is omission of four bottom surfaces, not full-unit glue subtraction. It does not repurpose the old11/6 observations or hypothetical cumulative-depth directions.',
 'styles':[('line_1','#DC2626','Source original unit top square front width1.'),('line_3','#DC2626','Source original unit top square depth1; together these two sides identify a unit face.'),('lowerline_1','#DC2626','ReceiverC top front width1.'),('lowerline_3','#DC2626','ReceiverC top left depth1; same unit-face corner as source.'),('lowerline_9','#DC2626','ReceiverB top front width1.'),('lowerline_11','#DC2626','ReceiverB top left depth1; identifiesB top area1 independently of thickness.'),('lowerline_15','#DC2626','ReceiverA top front width1.'),('lowerline_17','#DC2626','ReceiverA top left depth1; identifiesA top area1.'),('lowerline_21','#DC2626','ReceiverD visible rear width1, used because its front top boundary is occluded byA.'),('lowerline_23','#DC2626','ReceiverD visible right top depth1, adjacent to its rear width; identifiesD top despite occlusion. No hidden edge is exposed.')],
 'semantics':'Total surface area of a fixed glued solid; boundary strokes do not create material area, glue or an additional face. Same color compares real unit top faces; this is not a claim that only marked faces count or that bottoms are absent. All original steps, slab identities, fractional height labels, common bottom and visible/hidden intervals remain. Even if thin colored ink is imagined on those existing edges, the physical geometry and surface area stay11. No face fill or physical-piece membership is changed.'}}

def prepare(q):
    spec=SPECS[q]
    d=HERE/q/spec['id']
    d.mkdir(exist_ok=True)
    eligibility(q,'eligibility_before_render.json')
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import describe_paths
    from renderer_adapter import scene_png
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    config=read(PROJECT/'SolidGeometry/workbench/config.json')
    config['dataset_file']=str(PROJECT/'SolidGeometry/dataset.jsonl')
    adapter=RendererAdapter(config)
    c=adapter.inspect_question(q)
    assert c==read(HERE/q/'context_fresh.json')
    save(d/'context.json',c)
    actions=[]
    markers=[]
    scene=adapter.scene(q)
    try:
        with mpl.rc_context(scene.settings):scene.fig.canvas.draw()
        points={p['id']:p for p in c['snap_points']}
        for target,color,role in spec['styles']:
            original=next(o for o in c['objects'] if o['id']==target)
            action={'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
            paths=describe_paths(scene,target)
            markers.append({'action_index':len(actions),'role':role,'original_object':original,'path_bindings':paths,'exact_endpoints':[points[p] for p in original['geometry']['points']]})
            actions.append(action)
    finally:
        scene.close()
        plt.close('all')
    renderer=PluginRenderer(config,adapter,{q:c})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':spec['mechanism'],'intent':spec['mechanism'],'params':{'actions':actions}}
    normalized=renderer.normalize(plugin)
    assert renderer.normalize(normalized)==normalized
    save(d/'plugin_submitted.json',plugin)
    save(d/'plugin.json',normalized)
    save(d/'marker_geometry_audit.json',markers)
    hashes=[]
    for iteration in range(2):
        scene=adapter.scene(q)
        try:
            noop,ph=scene_png(scene)
            assert ph==c['original_pixel_sha256']
            frozen=(copy.deepcopy(scene.objects),copy.deepcopy(scene.snap_points),[(t.get_text(),t.get_position()) for t in scene.ax.texts])
            patches=list(scene.ax.patches)
            fills=[(type(a).__name__,str(a.get_facecolor())) for a in patches]
            with mpl.rc_context(scene.settings):renderer.apply_actions(scene,normalized)
            assert frozen==(scene.objects,scene.snap_points,[(t.get_text(),t.get_position()) for t in scene.ax.texts])
            assert fills==[(type(a).__name__,str(a.get_facecolor())) for a in patches]
            assert all(a.get_facecolor()[3]==0 for a in scene.ax.patches if a not in patches)
            png,pix=scene_png(scene)
            assert pix!=ph
            dest=d/('candidate.png' if iteration==0 else 'repeat.png')
            with dest.open('xb') as f:f.write(png)
            hashes.append({'png_sha256':sha(dest),'pixel_sha256':pix})
            del noop,png
        finally:
            scene.close()
            plt.close('all')
        gc.collect()
    assert hashes[0]==hashes[1]
    duplicate=[]
    for p in TASK.rglob('*.png'):
        if not p.is_relative_to(HERE) and sha(p)==hashes[0]['png_sha256']:
            duplicate.append(str(p))
    assert not duplicate,'same oldPNG is forbidden'
    proof=read(HERE/q/'primary_math_native.json')
    design={'question_id':q,'variant_id':spec['id'],'created_at':stamp(),'expected_wrong_answer':spec['preset'],'formal_correct_answer':proof['formal_answer'],'mechanism':spec['mechanism'],'primary_math_proof':proof,'marker_roles':markers,'human_semantics':spec['semantics'],'candidate_png_sha256':hashes[0]['png_sha256'],'candidate_pixel_sha256':hashes[0]['pixel_sha256'],'plugin_sha256':sha(d/'plugin.json'),'context_sha256':sha(d/'context.json'),'status':'PRIMARY candidate only; no userapproval/Pass/Collect/delivery; new parent independentreview required if2hits'}
    save(d/'design.json',design)
    save(d/'design_difference_audit.json',{'question_id':q,'variant_id':spec['id'],'frozen_before_calls':True,'material_difference':spec['difference'],'new_mechanism':spec['mechanism'],'predeclared_wrong_answer':spec['preset'],'candidate_png_sha256':hashes[0]['png_sha256'],'design_sha256':sha(d/'design.json'),'all_prior_PNG_hashes_distinct':True,'same_old_or_cross_ID_failed_PNG_matches':duplicate,'all_old_full_raw_read':True,'old_evidence_manifest':str(HERE/q/'old_evidence_manifest.json'),'prior_request_scan':str(HERE/'global_old_call_and_objection_scan_v2.json'),'no_relabel_or_cosmetic_retest':True})
    save(d/'render_check.json',{'fresh_schema_and_defaults':True,'normalized_idempotent':True,'fresh_context_equal':True,'no_op_formal_pixel_match':True,'repeat_byte_identity':True,'renders':hashes,'frozen_geometry_snaps_text_fill_unchanged':True,'appearance_changes':renderer.appearance_changes(normalized),'actual_native_image_view_pending':True})
    print(q,spec['id'],'frozen',hashes[0]['png_sha256'],flush=True)

def replay(q):
    d=HERE/q/SPECS[q]['id']
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from renderer_adapter import scene_png
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    config=read(PROJECT/'SolidGeometry/workbench/config.json')
    config['dataset_file']=str(PROJECT/'SolidGeometry/dataset.jsonl')
    adapter=RendererAdapter(config)
    c=adapter.inspect_question(q)
    assert c==read(d/'context.json')
    renderer=PluginRenderer(config,adapter,{q:c})
    plugin=read(d/'plugin.json')
    assert renderer.normalize(plugin)==plugin
    scene=adapter.scene(q)
    try:
        png,pix=scene_png(scene)
        assert pix==c['original_pixel_sha256']
        del png
        with mpl.rc_context(scene.settings):renderer.apply_actions(scene,plugin)
        png,pix=scene_png(scene)
        assert png==(d/'candidate.png').read_bytes()
        with (d/'offline_replay.png').open('xb') as f:f.write(png)
        save(d/'offline_replay_audit.json',{'time':stamp(),'fresh_process':True,'fresh_context_exact':True,'fresh_noop_formal_pixels':True,'schema_normalized_again':True,'exact_frozen_plugin':sha(d/'plugin.json'),'exact_frozen_PNG':sha(d/'candidate.png'),'fresh_offline_byte_identity':True,'pixel_sha256':pix,'no_passed_recipe_fabricated':True})
    finally:
        scene.close()
        plt.close('all')
    print(q,'fresh exact offline replay pass')

if __name__=='__main__':
    if sys.argv[1]=='prepare':prepare(sys.argv[2])
    elif sys.argv[1]=='replay':replay(sys.argv[2])
