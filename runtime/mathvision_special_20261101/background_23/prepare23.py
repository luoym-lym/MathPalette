from common23 import *
from datetime import datetime,timezone
branch=sys.argv[1]
sys.path.insert(0,str(ROOT/branch/'workbench'))
from workbench_io import load_config,pixel_hash,environment_versions
from partial_style import describe_paths
if branch=='PlaneGeometry':
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
else:
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
config=load_config();config['runtime_dir']=str(OUT/'state');config['output_dir']=str(OUT/'output')
ad=RendererAdapter(config)
R='#DC2626';B='#2563EB'
def sty(target,color,interval=None):
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
    if interval:a['interval']=interval
    return a
for qid in sys.argv[2:]:
    e=eligibility(qid);assert e['eligible'];meta=ad.inspect_question(qid)
    if qid=='Plane192':
        vid='r23_maximal_run_unit_binding';wrong='A'
        actions=[sty('route'+str(i)+'_0',R) for i in range(4)]
        rationale='One first maximal rising run is red in EACH of the four input routes. Their actual grid lengths are 4sqrt2,3sqrt2,2sqrt2,sqrt2. The shared role (one straight run) is the proposed false unit: count runs instead of summing unit diagonals, favoring the two-run A. No complete option is emphasized and all competitor routes retain original continuous black ink.'
        difference='v01/v02 singled out the entire D route; v03 singled out the entire A route and dashed all competitors. This removes those salience/fragmentation operations and introduces four-way matched maximal-run exemplars of unequal metric length. The hypothesis is object-unit substitution across all inputs, rather than whole-option highlighting.'
        roles=[{'action_index':i,'target':a['target'],'role':f'First maximal rising run of {"ABCD"[i]}: {4-i} unit diagonals; corresponding exemplar for counting one run as one unit, while the grid still exposes its true length.'} for i,a in enumerate(actions)]
    elif qid=='Plane233':
        vid='r23_exterior_notch_correspondence';wrong='B'
        actions=[sty('given_27',B),sty('B_11',B),sty('given_29',R),sty('B_8',R)]
        rationale='Match ONLY the pre-existing outer missing-corner notch of the whole board to the right inner notch corner of B under a half-turn. Source rays from (14,8) point down/blue and right/red; B rays from (8,1) point up/blue and left/red. This is real local boundary compatibility, falsely generalized to three-copy global tileability.'
        difference='The rejected design closed TWO internal U silhouettes and reasonably asserted a false 5,5,3,2 partition. This design styles zero internal source-grid edges and encloses zero source subsets. It removes every apparent cut while changing the correspondence from two complete trial pieces to the actual exterior concavity. Compared with the old cross design, neither an X placement nor a whole option contour remains.'
        roles=[{'action_index':0,'target':'given_27','role':'Existing vertical exterior wall beside the missing board cell, from (14,7) to (14,8); blue down-ray of concave corner.'},{'action_index':1,'target':'B_11','role':'Right inner wall of B notch, (8,1)-(8,2); blue half-turn counterpart.'},{'action_index':2,'target':'given_29','role':'Existing horizontal exterior wall above the missing board cell, (14,8)-(15,8); red right-ray.'},{'action_index':3,'target':'B_8','role':'Floor of B notch, (7,1)-(8,1); red half-turn counterpart. Only one unit notch corner is matched, not a five-cell outline.'}]
    elif qid=='Solid220':
        vid='r23_strip_endpoint_skip_transfer';wrong='A'
        actions=[sty('line_3',R),sty('line_15',R),sty('line_8',B),sty('line_17',B)]
        rationale='Red identifies the first face of each planar strip (U in U-V-W and X in X-Z); blue identifies its terminal face (W and Z). The real three-face strip U-V-W has opposite endpoint faces. The proposed error transfers that endpoint rule to the two-face X-Z strip, losing the intervening-face requirement and answering Z/A.'
        difference='The held variant framed Z with its top/bottom borders. The later dot and edge pairs marked only X/Z and failed E/E. This adds a concrete input analogy with the true opposite pair U/W: four ordered endpoint features across two different strip lengths. It is not a cosmetic change to the failed pair: without U/W there is no skip-rule transfer. Only one edge on each of four distinct faces is marked; no Z frame or generic pair of dots.'
        roles=[{'action_index':0,'target':'line_3','role':'U exterior left edge: red first endpoint of three-face U-V-W strip.'},{'action_index':1,'target':'line_15','role':'X exterior left edge: red first endpoint of two-face X-Z strip.'},{'action_index':2,'target':'line_8','role':'W exterior right edge: blue last endpoint of three-face strip. U and W truly fold to opposite normals.'},{'action_index':3,'target':'line_17','role':'Z exterior right edge: blue last endpoint of two-face strip. X/Z actually share a hinge and are adjacent; false endpoint analogy is the targeted error.'}]
    elif qid=='Plane263':
        vid='r23_complementary_hook_closure';wrong='2'
        scene=ad.scene(qid)
        try:
            scene.fig.canvas.draw()
            paths={o['id']:describe_paths(scene,o['id']) for o in meta['objects']}
        finally:scene.close()
        def interval(target,start,end):
            p=paths[target][0]
            return {'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
        actions=[sty('cell'+str(i),R,interval('cell'+str(i),.5,.75)) for i in [1,2,3]]
        actions += [sty('cell4',B,interval('cell4',.25,.5)),sty('cell3',B,interval('cell3',.25,.5))]
        rationale='The red three-unit concave shoulder is a real mating edge for a 180-degree rotated second L. The blue one-unit upright at the notch and the far-right terminal upright are its two complementary hook endpoints. Two copies close these boundaries into a 2x5 rectangle. Predicted wrong2 confuses that completed rectangle with the required square. No second tile or closing outline is drawn.'
        difference='The rejected v01 uniformly recolored all five unit-cell outlines and targeted the area-only answer5. This selects only the actual complementary hook interface, leaving the rest black. It has a new geometric closure hypothesis and independently predeclares2, rather than reusing the old observed5 after a cosmetic change.'
        roles=[{'action_index':i,'target':a['target'],'interval':a['interval'],'role':('One of three consecutive shoulder units of the actual concave interface y=1, x=1..4.' if i<3 else ('Upright notch hook x=1,y=1..2.' if i==3 else 'Complementary outer terminal hook x=4,y=0..1; maps to notch hook under half-turn (x,y)->(5-x,2-y).'))} for i,a in enumerate(actions)]
    else:raise ValueError(qid)
    target=OUT/qid/vid
    if target.exists():
        assert not (target/'candidate.png').exists() and not (target/'api_process.json').exists()
        if (target/'design_difference_audit.json').exists():
            (target/'difference_audit_preflight_failed.json').write_bytes((target/'design_difference_audit.json').read_bytes())
    target.mkdir(parents=True,exist_ok=True)
    write(target/'eligibility_before_design.json',e)
    write(target/'design_difference_audit.json',{'stage':'material_refinement','question_id':qid,'variant_id':vid,'written_before_calls':True,'new_hypothesis':rationale,'substantive_difference':difference,'old_candidates':read(OUT/qid/'prior_history_manifest.json'),'old_held_rejected_not_promoted':True,'not_pixel_hash_only':True,'planned_wrong_answer':wrong,'per_marker_roles':roles})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':rationale,'intent':rationale,'params':{'actions':actions}}
    renderer=PluginRenderer(config,ad,{qid:meta})
    normalized,data,pixels=renderer.render(plugin)
    normalized2,data2,pixels2=renderer.render(normalized,frozen=True)
    assert normalized==normalized2 and data==data2 and pixels==pixels2
    assert e['frozen_source_files']==eligibility(qid)['frozen_source_files']
    (target/'candidate.png').write_bytes(data);(target/'repeat.png').write_bytes(data2)
    write(target/'plugin.json',normalized)
    write(target/'fresh_context.json',meta)
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        paths={a['target']:describe_paths(scene,a['target']) for a in actions}
    finally:scene.close()
    write(target/'path_fingerprints.json',paths)
    write(target/'render_check.json',{'schema_actual_normalization':True,'normalized_plugin_sha256':sha(target/'plugin.json'),'formal_noop_pixels_match':True,'noop_path':str(OUT/qid/'noop.png'),'twice_byte_identical':True,'png_sha256':sha(target/'candidate.png'),'pixel_sha256':pixels,'frozen_inputs_unchanged':True,'environment':environment_versions(),'isolation':ISOLATION})
    write(target/'design.json',{'stage':'material_refinement','question_id':qid,'branch':branch,'variant_id':vid,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':wrong,'correct_answer':e['formal_record']['answer'],'hypothesis':rationale,'substantive_difference':difference,'per_marker_roles':roles,'image_sha256':sha(target/'candidate.png'),'plugin_sha256':sha(target/'plugin.json'),'pixel_sha256':pixels,'fresh_context_sha256':sha(target/'fresh_context.json'),'difference_audit_sha256':sha(target/'design_difference_audit.json'),'status':'PRIMARY_DRAFT_REQUIRES_NATIVE_INSPECTION_AND_PARENT_NEW_INDEPENDENT_REVIEW'})
    print(json.dumps({'question_id':qid,'variant_id':vid,'png_sha256':sha(target/'candidate.png'),'actions':len(actions)}),flush=True)
