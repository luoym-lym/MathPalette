import bootstrap75 as boot
from research75 import *

RED='#DC2626'
BLUE='#2563EB'
def line(i,a,b,color):return {'type':'add_line','id':i,'endpoints':[list(a),list(b)],'color':color,'linestyle':'solid'}

def specifications(q):
    if q=='Plane317':
        name='r75_hole_corner_choice_synchronization'
        actions=[];roles=[]
        for k,(x,y) in enumerate([(1,1),(1,6),(6,1),(6,6)]):
            for role,a,b,color in [('top',(x,y+1),(x+1,y+1),RED),('right',(x+1,y+1),(x+1,y),BLUE)]:
                actions.append(line('hole'+str(k)+'_'+role,a,b,color))
                roles.append({'action_id':actions[-1]['id'],'source_or_receiver':'source local hole' if k==0 else 'receiver homologous hole '+str(k),'true_information':f'The existing {role} unit side of black hole ({x},{y}) borders the eight-white-cell ring; together the red/blue incident sides preserve its orientation and identify the two local cyclic domino choices.','misconception_role':'Transfers the same local clockwise/anticlockwise choice frame to four independent rings; target error treats homologous choice categories as a global synchronized choice.','not_new_given':'No edge is added inside a white field, no domino position is outlined, black/white cell membership unchanged. Colors assert no required common domino orientation.'})
        return name,actions,roles,'2','The two possible cyclic ring coverings are misread as two globally synchronized patterns across all four identically oriented red/blue hole corners, rather than independent choices at four rings.','Earlier background08 retained no design: proposed domino partitions risked fixed coverings. This uses only open incident sides of the four original black holes, maps a local orientation frame across independent components, and draws zero candidate domino boundaries or white-cell partitions. No earlier frozen candidate exists to reuse.','Wording explicitly counts all white-field coverings and distinguishes any changed stone, with the board fixed. Colored open hole edges do not change that universe. Same colors compare true homologous hole corners without a common-choice condition. Black holes, 40 white cells, all grid edges and narrow bridges stay visible.'
    if q=='Plane337':
        name='r75_reentrant_to_frame_corner_binding'
        actions=[line('template_reentrant_horizontal',(5,2),(6,2),RED),line('template_reentrant_vertical',(6,2),(6,3),BLUE),line('board_convex_horizontal',(3,4),(4,4),RED),line('board_convex_vertical',(4,4),(4,3),BLUE)]
        roles=[]
        for i,a in enumerate(actions):
            roles.append({'action_id':a['id'],'source_or_receiver':'source template reentrant corner' if i<2 else 'receiver board exterior corner','true_information':'One existing unit side at the template 270-degree reentrant corner (6,2).' if i<2 else 'One existing unit side at the board 90-degree convex corner (4,4).','misconception_role':'The colored two-edge elbows have matching local lengths after reflection but opposite occupied-side roles. Hypothesis transfers superficial corner fit to assume the area bound of four skew tetrominoes is attainable.','not_new_given':'Existing outline only; no internal board cut or closed candidate piece is drawn; no false angle/equality symbol or changed template.'})
        return name,actions,roles,'0','Confuse the template reentrant elbow with a convex board corner after reflection, infer a four-piece complete packing from local boundary resemblance and area16/4, and report zero cells remaining.','Earlier background08 rejected a proposed colored packing because it would fix cuts. The new design compares two OPEN original outline corners with opposite interior-side roles, never marks a proposed board packing, and tests an explicit local-fit-versus-global-packability misconception. The old source65 direction was prospective only.','The 4x4 board and complete skew tetromino remain clear. The open board elbow lies entirely on its exterior; source elbow lies on the original notch. Colors preserve both 90/270-degree roles and do not draw cuts. Physical mirror/rotation permission remains exact; the area bound is not asserted as a packing construction.'
    if q=='Plane385':
        name='r75_tilted_side_to_unit_diagonal_binding'
        actions=[line('real_tilted_side',(1,2),(2,1),RED),line('unit_square_diagonal',(0,2),(1,1),RED)]
        roles=[{'action_id':'real_tilted_side','source_or_receiver':'source','true_information':'Segment P12-P21 is a genuine side of the unique tilted square, with squared length2 and vector(1,-1).','misconception_role':'Provides a real tilted-side exemplar for the translated segment.','not_new_given':'Connects two existing dots; one open segment does not draw a new given square or add points.'},{'action_id':'unit_square_diagonal','source_or_receiver':'receiver','true_information':'Segment P02-P11 has the exact same vector(1,-1) and length as the source, but is the diagonal of a unit square and cannot be completed as a tilted-square side using the available dots.','misconception_role':'Hypothesis transfers the source side role across translation and counts one extra rotated square without checking all four vertices, predicting3 upright+2 tilted=5.','not_new_given':'Both endpoints already exist; no missing(0,0) point, closure, right-angle marker or equal-length stipulation is added. The true geometric segment equality is a comparison cue only.'}]
        return name,actions,roles,'5','Treat a translated equal-slope/length segment that is actually a unit-square diagonal as the side of another tilted square, giving3 real upright plus2 imagined tilted squares.','Old axis_aligned_square_subset outlined all3 unit squares and preset3 got6/3; old tilted_square_family_only outlined the full diamond and preset1 got6/6. Both remain misses. The new candidate has neither closed family; it compares one true tilted side with one actual unit-square diagonal, a new mixed-role correspondence. The preset5 follows this geometry before outputs and is not old observed6 relabeling.','The actual eight dots remain visible, with no new dots, intersections, closed polygons or prescribed square. The question counts every possible square obtained by joining these dots; existing thin example segments do not limit that count. Both marks are physically valid segments, while only one has a complete available side-square. Exact distance enumeration still gives4.'
    raise ValueError(q)

def candidate(q):
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    name,actions,roles,wrong,hypothesis,difference,semantics=specifications(q)
    target=OWN/q/name;target.mkdir(parents=True,exist_ok=True)
    if (target/'candidate.png').exists():raise ValueError('Frozen candidate already exists; no overwrite/retest')
    e=eligible(q);put(target/'eligibility_design.json',e)
    if not e['eligible']:raise ValueError('Eligibility failed')
    config=load_config();config['runtime_dir']=str(OWN/'workbench_runtime');config['output_dir']=str(OWN/'workbench_output')
    adapter=RendererAdapter(config);context=adapter.inspect_question(q);put(target/'fresh_context.json',context)
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{q:context});normalized=renderer.normalize(plugin)
    put(target/'plugin_submitted.json',plugin);put(target/'plugin.json',normalized)
    # Freeze exact native paths for every existing edge covered by each auxiliary mark.
    from partial_style import object_paths
    bindings=[];scene=adapter.scene(q)
    try:
        scene.fig.canvas.draw()
        # Freeze numeric geometry/style and the original native path fingerprint.
        # Runtime artist handles are deliberately not serializable source data.
        def plain(v):
            if isinstance(v,dict):return {k:plain(x) for k,x in v.items() if k!='artist'}
            if isinstance(v,(list,tuple)):return [plain(x) for x in v]
            if hasattr(v,'tolist'):return plain(v.tolist())
            return v
        paths={o['id']:plain(object_paths(scene,o['id'])) for o in context['objects'] if o.get('styleable')}
        for a,r in zip(normalized['params']['actions'],roles):
            ends=a['endpoints']; snaps=[]
            for xy in ends:
                matches=[p['id'] for p in context['snap_points'] if p['xy']==xy]
                if not matches:raise ValueError('Endpoint not actual frozen point: '+str(xy))
                snaps.append(matches)
            bindings.append({**r,'normalized_action':a,'endpoint_snap_ids':snaps})
        put(target/'native_paths.json',paths)
    finally:scene.close()
    put(target/'marker_bindings.json',bindings)
    put(target/'design_difference_audit.json',{'created_at':now(),'question_id':q,'variant_id':name,'substantive_difference':difference,'new_source_receiver_information':roles,'immutable_wrong_hypothesis':wrong,'new_wrong_hypothesis_rationale':hypothesis,'cosmetic_retry':False,'no_old_image_reused':True,'old_source65_no_design_no_calls':True,'not_a_causal_effect_claim':True})
    normalized,data,pixels=renderer.render(normalized,frozen=True)
    normalized2,again,pixels2=renderer.render(normalized,frozen=True)
    assert normalized==normalized2 and data==again and pixels==pixels2
    (target/'candidate.png').write_bytes(data);(target/'repeat.png').write_bytes(again)
    old_audit=read(OWN/'old_history_full_read_audit.json');olds=[x for x in old_audit['files'] if x['path'].endswith('.png')]
    collisions=[x for x in olds if x['sha256']==sha(data)]
    assert not collisions
    proof=read(OWN/q/'math_proof.json');put(target/'math_proof_snapshot.json',proof)
    put(target/'design.json',{'question_id':q,'variant_id':name,'created_at':now(),'expected_wrong_answer':wrong,'correct_answer':e['formal_record']['answer'],'hypothesis':hypothesis,'substantive_difference':difference,'primary_math_proof_path':str(target/'math_proof_snapshot.json'),'per_marker_roles':roles,'human_semantics_pretest':semantics,'pretest_immutable':True,'baseline_pixels_equal_formal':True,'repeat_byte_identical':data==again,'image_sha256':sha(data),'pixel_sha256':pixels,'plugin_sha256':sha((target/'plugin.json').read_bytes()),'context_sha256':sha((target/'fresh_context.json').read_bytes()),'math_proof_sha256':sha((target/'math_proof_snapshot.json').read_bytes()),'difference_audit_sha256':sha((target/'design_difference_audit.json').read_bytes()),'approval_status':'PRIMARY UNREVIEWED; NEW independent parent review required before any delivery'})
    put(target/'render_audit.json',{'rendered_at':now(),'schema_default_normalization':True,'no_op_pixels_equal_formal':True,'twice_byte_identical':True,'image_sha256':sha(data),'pixel_sha256':pixels,'old_failed_aborted_png_hash_collisions':collisions,'native_png_manual_view_pending':True,'offline_replay_pending':True})
    print(json.dumps({'candidate':str(target),'sha256':sha(data),'expected_wrong_answer':wrong}))

def replay(q):
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    name=specifications(q)[0];target=OWN/q/name
    config=load_config();config['runtime_dir']=str(OWN/'workbench_runtime');config['output_dir']=str(OWN/'workbench_output')
    adapter=RendererAdapter(config);context=adapter.inspect_question(q)
    renderer=PluginRenderer(config,adapter,{q:context});plugin=read(target/'plugin.json');_,data,pixels=renderer.render(plugin,frozen=True)
    expected=(target/'candidate.png').read_bytes();assert data==expected
    (target/'offline_replay.png').write_bytes(data)
    put(target/'offline_replay_audit.json',{'replayed_at':now(),'fresh_process':True,'same_unchanged_native_adapter_and_PluginRenderer':True,'normalized_frozen_plugin':True,'byte_identical':True,'sha256':sha(data),'pixel_sha256':pixels,'plugin_sha256':sha((target/'plugin.json').read_bytes()),'strict_root':str(OWN)})
    print(json.dumps({'replayed':q,'byte_identical':True,'sha256':sha(data)}))

if __name__=='__main__':
    if sys.argv[1]=='candidate':candidate(sys.argv[2])
    elif sys.argv[1]=='replay':replay(sys.argv[2])
