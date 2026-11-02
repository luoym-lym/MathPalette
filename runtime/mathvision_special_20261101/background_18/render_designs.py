from tools18 import *
R='#DC2626';B='#2563EB';O='#EA580C'
cfg,ad,Renderer=adapter()
def style(target,color,width=2):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
def partial(q,target,color,start,end,width=2):
    from partial_style import describe_paths
    s=ad.scene(q)
    try:
        s.fig.canvas.draw();paths=describe_paths(s,target);p=paths[0]
    finally:s.close()
    return {**style(target,color,width),'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
def save(q,vid,wrong,actions,mechanism,roles,proof):
    assert q in ASSIGNED and eligibility(q)['eligible']
    out=HERE/q/vid;out.mkdir(parents=True,exist_ok=False)
    before=inputs(ad,q);m=ad.inspect_question(q)
    write(out/'fresh_context.json',m);write(out/'eligibility_before_design.json',eligibility(q))
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':vid,'intent':mechanism,'params':{'actions':actions}}
    renderer=Renderer(cfg,ad,{q:m});norm,png,pix=renderer.render(plugin);norm2,png2,pix2=renderer.render(norm,frozen=True)
    assert norm==norm2 and png==png2 and pix==pix2
    assert before==inputs(ad,q)
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png);(out/'repeat.png').write_bytes(png2)
    design={'question_id':q,'variant_id':vid,'expected_wrong_answer':wrong,'created_at':now(),'mechanism':mechanism,'marker_roles':roles,'primary_math_proof':proof,'candidate_png_sha256':file_hash(out/'candidate.png'),'candidate_pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'frozen_before_two_calls':True,'schema_normalized':True,'no_control_run':True}
    write(out/'design.json',design)
    write(out/'render_check.json',{'baseline_pixel_equal':True,'normalized_frozen_replay':True,'two_png_bytes_identical':True,'pixel_sha256':pix,'png_sha256':file_hash(out/'candidate.png'),'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION})
    notes=json.loads((ROOT/'provenance/source_notes.json').read_text(encoding='utf-8-sig'))[q]
    write(out/'source_audit.json',{'question_id':q,'formal_record':ad.records[q],'source_notes_file_sha256':file_hash(ROOT/'provenance/source_notes.json'),'source_audit':notes.get('audit'),'own_primary_proof':proof,'formal_original_preserved':True,'source_scene_png_hashes':before})
    print(q,vid,wrong,len(actions),flush=True)
if BRANCH=='PlaneGeometry':
    q='Plane366'
    actions=[partial(q,'o13',R,0.78,1),partial(q,'o14',R,0.78,1),partial(q,'o13',B,0,0.22),partial(q,'o14',B,0,0.22)]
    save(q,'directed_endpoint_binding','D',actions,'Bind the upper vertical end to the right horizontal end and the lower vertical end to the left horizontal end; treating appearance as a fixed endpoint identity suppresses the alternative X rotation.',[
        'Red upper 22% of original vertical segment is the source end feature.', 'Red rightmost22% of horizontal segment is its false forced correspondence.', 'Blue bottom22% of vertical is the complementary end feature.', 'Blue leftmost22% of horizontal closes the directed pairing; no marker on an answer label or centre.'
    ],'Use frozen endpoints U=(1,4),L=(1,2),V=(3,2),W=(5,2). About X=(3,4), counterclockwise90 sends U to V and L to W. About T=(2,1), clockwise90 sends U to W and L to V. For Y=(2,3) all source distances squared are2 whereas target distances are2,10; for Z=(1,1), source distances squared9,1 whereas target5,17. Thus exactly X,T, optionC. Styles add no endpoint equality or geometric condition.')
else:
    q='Solid239'
    proof='The closed packet has crease boundaries right x=1 and bottom y=0, open stacked edges top/left. In local quarter[0,1]^2, cut endpoints(.5,0),(1,.5) remove the corner triangle at(1,0). Reflections(x,y),(2-x,y),(x,-y),(2-x,-y) give diamond vertices(.5,0),(1,.5),(1.5,0),(1,-.5), strictly interior to original[0,2]×[-1,1]. OnlyE has this hole. D omits the final reflection andC has axis-aligned edges. Original dashedcut, fold/open edges, all fills and choices retained.'
    save(q,'single_unfold_triangle_binding','D',[
        style('line148',R),partial(q,'line161',R,2/3,1),style('closed_layer3_edge0_interval0',B),partial(q,'line161',B,0,1/3)
    ],'Map the given diagonal cut to D\'s rising hole side and the packet bottom fold boundary to D\'s horizontal hole base. This targets stopping after a single unfold instead of both perpendicular reflections.',[
        'Red dashed original cut identifies the actual diagonal operation, with dashes unchanged.','Red rising side of D triangle is the false cut-output correspondence.','Blue bottom packet fold edge identifies an actual folding boundary.','Blue horizontal base of D hole is the false persistence of the crease as final cut boundary; existing triangle contour only.'
    ],proof)
    save(q,'crease_axes_as_hole_edges','C',[
        style('closed_layer3_edge0_interval0',R),partial(q,'line157',R,0,0.25),style('closed_layer3_edge1_interval0',B),partial(q,'line157',B,0.25,0.5)
    ],'Bind two perpendicular packet crease edges to the bottom/right edges of C\'s axis-aligned square hole, confusing crease directions with the diagonal cut directions.',[
        'Red existing bottom crease provides horizontal input feature.','Red bottom square-hole edge in C provides false output feature.','Blue existing right crease provides vertical input feature.','Blue right square-hole edge in C provides false output feature. No full option outline is emphasized.'
    ],proof)
    q='Solid145'
    proof='Index the four top and bottom notches0..3. Given visible front edges areT0-B0,T1-B2,T2-B3, with endsE0-T0,E1-T3. A halfturn around the shown long axis exchanges old top/bottom. Each offered front must supply the missing back edges so the union is one unbranched path with exactly2free ends, without a separate loop. A also leaves freeends above after the shown turn. B supplies the valid path; C/D/E give invalid repeated/unused/branched or disconnected routes. The initial hidden route has more than one completion but onlyB among the listed views is compatible. Primary graph audit saved separately before any delivery recommendation.'
    save(q,'front_strand_identity_transfer','C',[style('line4',R),style('line31',R),style('line5',B),style('line32',B),style('line3',O),style('line33',O)],'Bind all three known front strands to C\'s two sloping strands and vertical strand, carrying front-feature identities onto the newly visible back instead of checking continuous rope topology.',[
        'Red source first sloping strand.','Red C first sloping strand is its false front-to-back mate.','Blue source second sloping strand.','Blue C second longer diagonal is its false mate.','Orange source vertical strand.','Orange C vertical strand completes the three-feature transfer. Existing rope ink only.'
    ],proof)
    save(q,'free_end_upper_side_binding','A',[style('line6',R),style('line16',R),style('line7',B),style('line17',B),style('line4',O),style('line13',O)],'Bind original two upper free-end hooks to A\'s still-upper hooks and a slanted strand to A\'s opposite slope, treating the turn as a planar reflection and missing the top/bottom exchange.',[
        'Red source left free-end hook.','Red A upper-left hook is its false postturn location.','Blue source right free-end hook.','Blue A upper-right hook is its false postturn location.','Orange original sloping strand.','Orange A reflected sloping strand completes the mirror correspondence.'
    ],proof)
