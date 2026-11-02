from env42 import *
RED='#DC2626';BLUE='#2563EB'
def render(qid):
    cfg,ad=adapter();e=eligibility(qid);assert e['eligible'];before=inputs(ad,qid);m=ad.inspect_question(qid)
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        if qid=='Plane418':
            from dataset_tools.mathvision_workbench import png_bytes
            png_bytes(scene)  # Match the unchanged PluginRenderer baseline serialization before path hashing.
        paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
    finally:scene.close()
    actions=[];roles=[]
    def part(oid,start,end,color,role):
        p=paths[oid][0]
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':oid,'role':role,'full_exact_path':[{'id':v['id'],'sha256':v['sha256'],'closed':v['closed'],'exact_controls':[s['control'].tolist() for s in v['segments']]} for v in paths[oid]]})
    if qid=='Plane413':
        vid='r42_partial_cell_unit_corner_transfer';wrong='24'
        fragments=read(HERE/qid/'cell_fragment_audit.json')
        for cell in [{'x':3,'y':2,'gray_area':'1'},*fragments['partial']]:
            x,y=cell['x'],cell['y'];kind='full unit reference' if cell['gray_area']=='1' else 'partial gray fragment'
            role=f'{kind} cell({x},{y}), actual gray area{cell["gray_area"]}; the same unit top-right grid corner is a shape counterpart, not a claim that gray fills the cell.'
            part('h'+str(y+1),x/9,(x+1)/9,BLUE,role+' Top unit edge.')
            part('v'+str(x+1),y/3,(y+1)/3,BLUE,role+' Right unit edge.')
        diff='Old unit20 saved no design/calls and rejected pairing unequal whole boundary lobes. New design uses exact rational polygon/cell clipping, not whole-lobe equality:10 full gray units and14 partly gray cells, total area17 but24 touched cells. One full-unit reference and every partial cell receive the same open unit-grid corner on actual existing edges. The targeted information error transfers whole-cell area1 from the reference to each partly occupied cell, yielding24. Gray fill and every sloping boundary remain unchanged; no added cut, region or counting dot. Thirty actions form15 purposeful two-edge groups, rather than30 independent decorations.'
        semantics='The question asks gray area, not number of colored outlines. All corner marks lie on the already existing unit grid, remain open, and change no facecolor or polygon boundary. The14 partial fractions remain visibly gray/white; equal unit-grid corners do not assert equal shaded areas. Human area remains17 under the same interpretation. Physical paper or colored-ink transport is absent.'
    elif qid=='Plane418':
        vid='r42_local_corner_fit_to_area_bound_exact_edge_overlay';wrong='5'
        for name,a,b,col,role in [
            ('source_top',[0,3],[3,3],RED,'Actual exterior top bar, union of piece0/1/2 top edges, length3.'),
            ('source_left',[0,2],[0,3],BLUE,'Actual exterior piece0 left edge, length1.'),
            ('board_top',[4.5,4],[7.5,4],RED,'Actual board exterior top interval, union of board3/7/11 top edges, exact source translation(+4.5,+1).'),
            ('board_left',[4.5,3],[4.5,4],BLUE,'Actual board exterior top-left unit edge, exact source translation(+4.5,+1).')]:
            actions.append({'type':'add_line','id':'corner_match_'+name,'endpoints':[a,b],'color':col,'linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions)-1,'role':role+' This1pt overlay exactly coincides with the original visible edge; no new topological segment.','exact_original_xy':[a,b]})
        diff='Old unit16 saved no design/calls because an entire packing would draw apparent pieces. New open source/board corner pairing: red length3 top bar and blue length1 side truly match under(+4.5,+1), but area20/4=5 plus local fit does not prove global attainability. No board interior marked or occupied T outline added. Parity obstruction and explicit packing prove4. Two local interval drafts failed before any PNG/API: piece0 has different exact float hashes before/after baseline serialization, so unchanged normalizer and renderer cannot accept one interval hash (local_path_diagnostic.json). This same hypothesis/preset now uses4 legal1pt lines exactly on visible original edges, with no shared helper change or fingerprint bypass. It is a pre-call technical implementation correction, not another substantive design or API retry.'
        semantics='The board carries only an open L on its existing exterior, with the rest of the grid black. No mark encloses an occupied T, indicates an already placed piece, imposes a cut or removes available squares. The source still consists of the same four unit squares. Color does not define a matching or boundary constraint in a maximum-packing problem; a careful human can use the complete parity obstruction and uniquely obtain4.'
    elif qid=='Plane420':
        vid='r42_reflected_corner_triangle_families';wrong='1'
        part('v0',.5,1,RED,'Vertical side2 leg of top corner triangle; maps by x/y reflection to blue bottom horizontal side2.')
        part('h2',0,1,RED,'Horizontal side2 leg of top corner triangle; maps to blue right vertical side2.')
        part('diagonal',0,.5,RED,'Top half of actual hypotenuse closes that existing corner family, containing three actual triangles.')
        part('h0',.5,1,BLUE,'Horizontal side2 leg of reflected right corner triangle.')
        part('v2',0,1,BLUE,'Vertical side2 leg of reflected right corner triangle.')
        part('diagonal',.5,1,BLUE,'Bottom half of actual hypotenuse closes reflected corner family, containing three actual triangles.')
        diff='No old design or calls; old unit20 prescreen rejected selecting only unit triangles as arbitrary omission. New design binds two genuinely congruent side2 corner triangles via reflection x<->y, including complete size hierarchy (two unit triangles plus one side2 per family). Wrong hypothesis counts the two families (3+3) as exhaustive, missing four actual cross-family triangles, then reports absolute difference |6-7|=1. This is a specified decomposition error, not uniform recoloring or unit-triangle salience.'
        semantics='This is a geometric counting diagram, with no moving physical paper or printed-picture matching. Colored boundaries already existed in black; the question still counts every triangle irrespective of color. No new partition line, fill, label, equality/angle symbol, point or apparent disconnected line is added. Two congruent corner families are actual subfigures; treating them as exhaustive is the intended error, not a changed human counting rule.'
    elif qid=='Plane470':
        vid='r42_parallel_column_endpoint_pairs';wrong='6'
        sc=read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane470/scene.json')
        for x,col in [(0,RED),(1,BLUE),(2,RED)]:
            a,b=sc['points'][f'p{x}0'],sc['points'][f'p{x}1']
            actions.append({'type':'add_line','id':f'column_pair_{x}','endpoints':[a,b],'color':col,'linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions)-1,'role':f'Actual column{x} endpoint pair; the three congruent parallel pairs suggest the restricted choice of one vertex per pair. Outer pairs share red under left-right reflection; the middle blue pair fixes the third column.','exact_original_point_ids':[f'p{x}0',f'p{x}1'],'exact_original_xy':[a,b]})
        diff='No old design or calls. Unit21 rejected rectangle+diagonal lines due to new crossing and apparent triangle targets. This design uses only three disjoint parallel segments between six original dot centers, with zero crossings or new dots. It binds actual equal-length column pairs and targets one-vertex-per-column restriction:2^3 triples minus2 collinear rows=6, omitting12 triangles using both members of a column. All requested18 triangles still use only original dots. Nonstyleable native point artists are untouched; no overlaid marker or size change.'
        semantics='The wording explicitly chooses any three of the six dots. Open parallel segments cannot add a dot or a closed triangle, and have no intersections except their original endpoints. Every original dot remains a distinct black disk. Colors identify column-pair correspondence, without creating a rule that colors or drawn edges limit vertex choices. Counting only the6 restricted triangles is an error; a careful human still uniquely obtains18.'
    elif qid=='Plane478':
        vid='r42_crossed_subrectangle_ladder_binding';wrong='12'
        # Native polygon paths have4 equally parameterized ordered edges.
        part('r1',.5,.5+(2.3-1)/2.3/4,RED,'Top red rail y2.5 fromx2.3 tox1: horizontal intersection ladder hasx-levels1,2,2.3 and three rectangles.')
        part('r0',0,(2.3-1)/2/4,RED,'Bottom red rail y2 fromx1 tox2.3. Together the red pair binds the three actual horizontal-ladder boxes.')
        part('r2',.75+(3.3-2.5)/3.3/4,.75+(3.3-1.5)/3.3/4,BLUE,'Left blue rail x2 fromy2.5 toy1.5; vertical ladder hasy-levels1.5,2,2.5 and three boxes.')
        part('r1',.25,.5,BLUE,'Right blue rail x2.3 fromy1.5 toy2.5. The central[2,2]..[2.3,2.5] box belongs to BOTH ladders.')
        diff='Oldv01 colors all three source contours and presets3 (finals6/7); oldv02 uses one uniform contour color and presets7 (4/4 misses); oldv03 adds an unrelated overlap dot and presets4 (13/24 misses). New design removes all whole-contour styles and that dot, instead marking four open rail intervals of two intersecting subrectangle ladders. Each ladder has three actual rectangles and they share one; double-counting the shared box plus the six remaining rectangles gives12 instead of11. This exact new preset follows a new set-membership/counting proof, not a prior observed final or cosmetic edit.'
        semantics='All four rails coincide with actual original boundary intervals. The two ladders overlap and no new edge or point is introduced. The question counts every geometric rectangle regardless of color. Counting the shared central rectangle twice is not a reasonable alternate mathematical answer; it is the targeted membership error. No physical transport, colored-paper matching, new fill or fixed puzzle partition is implied.'
    else:raise ValueError(qid)
    out=HERE/qid/vid;out.mkdir(exist_ok=False)
    write(out/'design_difference_audit.json',{'question_id':qid,'variant_id':vid,'stage':'material_refinement','created_at':now(),'substantive_difference':diff,'expected_wrong_answer':wrong,'old_history_inventory':str(HERE/qid/'prior_history_inventory.json'),'all_old_designs_presets_full_raw_responses_and_initial_screens_read':True,'all_old_design_PNGs_native_viewed':True,'annotation_semantics_lesson_read':True,'proposed_actions':actions,'not_cosmetic_or_posthoc_preset_change':True})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':diff[:1000],'intent':'Frozen wrong hypothesis '+wrong,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:m});norm,png,pix=pr.render(plugin);norm2,png2,pix2=pr.render(norm,frozen=True)
    assert norm==norm2 and png==png2 and pix==pix2;assert inputs(ad,qid)==before
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png)
    write(out/'context.json',m);write(out/'eligibility_before_design.json',e)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':wrong,'correct_answer':ad.records[qid]['answer'],'mechanism':diff,'marker_roles':roles,'primary_math_audit':str(HERE/qid/'primary_math_audit.json'),'human_semantics':semantics,'approval_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'created_at':now(),'fresh_inspect_question_noop_formal_pixel_equal':True,'schema_defaults_normalized':True,'second_frozen_render_byte_identical':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'original_pixel_sha256':m['original_pixel_sha256'],'input_fingerprints':before,'runtime_isolation':ISOLATION,'strict_own_directory_guard_installed_before_project_import':True})
    print(qid,vid,wrong,len(actions),file_hash(out/'candidate.png'),flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:render(q)
