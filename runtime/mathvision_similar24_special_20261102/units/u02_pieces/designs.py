from worker import *

PLANS = {
 'Plane218': {
    'variant_id': 'p01_detached_C_four_by_two_comparison', 'expected_wrong_answer': 'C',
    'correct_answer':'A',
    'groups': [
       ('source_width', [[12,7],[16,7]], [0,-0.32], '#DC2626', 'The board has a true four-cell bottom run. Compare it with the full four-cell lower arm of C.'),
       ('option_width', [[12,0],[16,0]], [0,-0.32], '#DC2626', 'C has a true four-cell bottom run, occupying the entire board width in a horizontal placement.'),
       ('source_height', [[16,7],[16,9]], [0.32,0], '#2563EB', 'The lower two units of the original board right boundary supply a real two-cell height comparison. It is an open boundary interval, not an internal cut.'),
       ('option_height', [[16,0],[16,2]], [0.32,0], '#2563EB', 'C has a true two-cell vertical end. Compare two copies of its 4 by 2 bounding span with the 4 by 3 board, while the unchanged notch still permits interlocking.')],
    'mechanism': 'Paired detached red four-unit and blue two-unit span brackets transfer the true 4 by 2 bounding span of C to the board. Predicted error: treat two such bounding boxes as disjoint rectangles, infer height 2+2 exceeds 3, and select C as impossible while overlooking the valid half-turn interlock. The brackets compare actual lengths, not an invented source partition.',
    'wrong_answer_semantics': 'C means the pictured four-cell straight arm with a fifth cell above its right end is asserted not to admit two disjoint copies. This is false: the saved proof constructs a rotation-only disjoint pair. Letter and option value are both C.',
    'difference': 'Plane218 has no saved tested prior design. Old prescreen only established exhaustive placements and reported no clear trap. This proposal uses the independently verified 4 by 2 bounding-span/interlock distinction. It does not reuse Plane233 C pixels or assert coverage of all twelve cells.'},
 'Plane398': {
    'variant_id': 'p01_detached_A_square_orientation_comparison', 'expected_wrong_answer':'A',
    'correct_answer':'E',
    'groups': [
       ('source_square_vertical', [[12,5.5],[12,8.5]], [-0.27,0], '#DC2626', 'The given 3 by 3 piece has a true three-cell left border. Red names the vertical span of that particular source orientation.'),
       ('option_square_vertical', [[0,0],[0,3]], [-0.27,0], '#DC2626', 'The lower-left 3 by 3 region of A has a matching exterior left span. It is the actual square-piece location in A, not a guessed L-piece corner.'),
       ('source_square_horizontal', [[12,5.5],[15,5.5]], [0,-0.27], '#2563EB', 'The source square has a true three-cell lower border. Blue distinguishes the horizontal span and makes the source orientation comparison explicit.'),
       ('option_square_horizontal', [[0,0],[3,0]], [0,-0.27], '#2563EB', 'The lower-left 3 by 3 region of A has a matching exterior bottom span. Compare the black-white arrangement in the marked corner to the unchanged source square; a quarter-turn remains permitted.')],
    'mechanism': 'Compare the source 3 by 3 square with its actual lower-left placement in A using red vertical and blue horizontal detached brackets. Predicted error: freeze the square in its displayed orientation, reject the mismatch in the marked A region, and select A as impossible rather than rotating the square by three quarter-turns. The full black-white data and legal rotation remain visibly available.',
    'wrong_answer_semantics':'A means the pictured first 4 by 4 black-white tile is asserted impossible to assemble from the two given pieces. This is false: both pieces rotated by three quarter-turns give the saved A witness. Letter and option value are both A.',
    'difference':'The one old tested design paired the 7-cell L-piece four-unit arms with the unsuitable top-right corner of C; preset C, finals D and A. This proposal instead compares the separate 9-cell square and its genuine lower-left location in A, targeting its necessary rotation. It replaces on-material coloring with visibly detached external span brackets to avoid transporting colored ink. Neither changing an old preset nor recoloring the old relation is involved.'}
}

PLANS2 = {
 'Plane218': {
    'variant_id':'p02_detached_U_quarterturn_span_comparison','expected_wrong_answer':'B','correct_answer':'A',
    'groups':[
      ('source_three_side',[[12,7],[12,10]],[-0.32,0],'#DC2626','The full three-cell left board side is the receiver for the three-cell long side of B after a quarter-turn.'),
      ('option_three_side',[[6,2],[9,2]],[0,0.32],'#DC2626','The U-piece B has a genuine three-cell top side; compare its rotated orientation with the full board height.'),
      ('source_two_foot',[[12,7],[14,7]],[0,-0.32],'#2563EB','The first two cells of the bottom board boundary supply the perpendicular two-cell width after rotating B.'),
      ('option_two_foot',[[6,0],[6,2]],[-0.32,0],'#2563EB','B has a genuine two-cell left side. Together with its red top, this maps to a 2 by 3 vertical lane in the board without drawing any lane partition.')],
    'mechanism':'Paired three-cell red and two-cell blue exterior spans compare the U-piece B with a quarter-turned 2 by 3 fit in the board. Predicted error: examine two U-pieces with their mouths kept in the displayed orientation, find unavoidable overlap, and declare B impossible without allowing a relative half-turn or a common quarter-turn. This tests orientation freedom of a concave U rather than C long-arm bounding boxes.',
    'wrong_answer_semantics':'B asserts that two copies of the pictured U-shaped pentomino cannot be cut from the board. The independently saved exact enumeration has six disjoint pairs, including rotation-only witnesses, so B is false.',
    'difference':'No historical tested Plane218 design existed. The current p01 four-long/two-high C bounding-span hypothesis produced complete B,C finals against preset C and is permanently excluded. This proposal uses a different 3 by 2 concave U, red/blue axes exchanged through an explicit quarter-turn comparison and the relative orientation of its open mouths. It is not a recolor, width change or rerun of p01.'},
 'Plane398': {
    'variant_id':'p02_detached_two_piece_B_independent_rotations','expected_wrong_answer':'B','correct_answer':'E',
    'groups':[
      ('source_L_top',[[7,10],[11,10]],[0,0.27],'#DC2626','The actual four-cell top arm of the seven-cell L carries an alternating black-white boundary row.'),
      ('option_L_top',[[5,4],[9,4]],[0,0.27],'#DC2626','B has the same top four-cell alternating row, the actual location of the L top arm in its valid assembly.'),
      ('source_L_left',[[7,6],[7,10]],[-0.27,0],'#DC2626','The other full four-cell arm completes the true exterior corner of the given L; both arms have the same alternating pattern.'),
      ('option_L_left',[[5,0],[5,4]],[-0.27,0],'#DC2626','B has the matching four-cell left arm. Top plus left is the real L placement, without drawing an interior seam.'),
      ('source_square_bottom',[[12,5.5],[15,5.5]],[0,-0.27],'#2563EB','The separate square has a three-cell bottom boundary. Compare its displayed orientation with the complementary three-cell bottom run in B.'),
      ('option_square_bottom',[[6,0],[9,0]],[0,-0.27],'#2563EB','The lower-right three-cell boundary is the genuine bottom edge of the 3 by 3 square location in B. The pattern requires a rotation of that piece independently of the red L.')],
    'mechanism':'Red exterior brackets identify the genuine L placement on the top and left of B. Blue brackets compare the bottom edge of the remaining 3 by 3 square to the separate source square. Predicted error: preserve the zero rotation suggested by the two red arm matches for both pieces, reject the blue square pattern mismatch, and declare B impossible. In reality L needs zero rotation and the square three quarter-turns; separate pieces are free to move independently.',
    'wrong_answer_semantics':'B asserts that the second 4 by 4 black-white tile cannot be formed. It is constructible with the L unchanged and the square rotated three quarter-turns, as the independent exhaustive witness records. The formal unique impossible tile remains E.',
    'difference':'Old wrong_corner_L_transfer tested an unsuitable C corner (preset C, D/A finals). Current p01 compared only the square and the lower-left region of A (preset A, C/B finals). This new hypothesis compares both independently movable pieces at the actual B assembly: a full two-arm L match and a complementary three-cell square edge. The potential error is propagating the red piece orientation to the other piece, not repeating the old C reflection or merely changing the square-only A target.'}
}

def marker_actions(plan):
    actions = []; roles = []
    for name, (a,b), offset, color, purpose in plan['groups']:
        a1 = [a[0]+offset[0],a[1]+offset[1]]
        b1 = [b[0]+offset[0],b[1]+offset[1]]
        horizontal = a[1] == b[1]
        tick = [0,0.10] if horizontal else [0.10,0]
        marks = [('span',[a1,b1]),
                 ('start_cap',[[a1[0]-tick[0],a1[1]-tick[1]],[a1[0]+tick[0],a1[1]+tick[1]]]),
                 ('end_cap',[[b1[0]-tick[0],b1[1]-tick[1]],[b1[0]+tick[0],b1[1]+tick[1]]])]
        for suffix, endpoints in marks:
            aid = name+'_'+suffix
            actions.append({'type':'add_line','id':aid,'endpoints':endpoints,
                            'color':color,'linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions)-1,'id':aid,'kind':suffix,
                          'true_source_edge_endpoints':[a,b], 'offset':offset,
                          'purpose':purpose if suffix=='span' else
                          'Short transverse end cap fixes the exact extent of this external length-comparison bracket; it does not touch or subdivide the piece.',
                          'group_purpose':purpose,
                          'receiver_group':name.replace('source','option') if name.startswith('source') else name.replace('option','source'),
                          'no_added_material_edge':True})
    return actions, roles

def create(qid, number='p01'):
    from math import isclose
    cfg, ad = adapter()
    from mathvision_plugins import PluginRenderer
    from workbench_io import pixel_hash, environment_versions
    if number=='p03':
        from native_plans import metadata
        plan=metadata(qid)
    else:
        plan = (PLANS if number == 'p01' else PLANS2)[qid]
    out = OWN / qid / plan['variant_id']
    if (out / 'design.json').exists():
        raise FileExistsError('Design is immutable; do not overwrite: '+str(out))
    check = eligibility(qid); assert check['eligible'], check['reasons']
    write(out / 'eligibility_before_design.json', check)
    before = fingerprints(ad,qid)
    context = ad.inspect_question(qid)
    old_context = read(OWN / qid / 'context.json')
    assert canonical(context) == canonical(old_context), 'Exact JSON-normalized context changed'
    write(out / 'context.json',context)
    if number=='p03':
        from native_plans import build_actions
        actions,roles=build_actions(qid,ad,context)
    else:
        actions, roles = marker_actions(plan)
    plugin = {'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
              'description':plan['mechanism'],'intent':'','params':{'actions':actions}}
    renderer = PluginRenderer(cfg,ad,{qid:context})
    normalized = renderer.normalize(plugin)
    assert normalized == plugin
    fresh_schema = read(PROJECT / 'PlaneGeometry/workbench/plugin.schema.json')
    from render_plugins import check_schema
    check_schema(plugin,fresh_schema,fresh_schema)
    first,png,pix = renderer.render(plugin,frozen=True)
    second,png2,pix2 = renderer.render(plugin,frozen=True)
    assert first == second == plugin and png == png2 and pix == pix2
    out.mkdir(parents=True,exist_ok=True)
    (out / 'candidate.png').write_bytes(png)
    write(out / 'plugin.json',plugin)
    allhistory = read(TASK / 'history_index.json')
    collisions = []
    for q in allhistory['questions']:
        for d in q['designs']:
            if d['frozen_candidate_png_sha256'] == digest(png):
                collisions.append({'question_id':q['question_id'],'design':d['design_path']})
    for p in OWN.glob('Plane*/*/candidate.png'):
        if p.parent != out and filehash(p) == digest(png):
            collisions.append({'question_id':p.parent.parent.name,'design':str(p.parent/'design.json')})
    assert not collisions, collisions
    design = {'question_id':qid,'variant_id':plan['variant_id'],'created_at':now(),
              'expected_wrong_answer':plan['expected_wrong_answer'],
              'expected_wrong_value':plan['expected_wrong_answer'],'correct_answer':plan['correct_answer'],
              'wrong_answer_semantics':plan['wrong_answer_semantics'],'mechanism':plan['mechanism'],
              'marker_roles':roles,'primary_mathematical_proof_path':str(OWN / qid / 'primary_mathematical_proof.json'),
              'primary_mathematical_proof_sha256':filehash(OWN / qid / 'primary_mathematical_proof.json'),
              'source_reference':plan.get('source_reference','Current user Plane233 C01, actually viewed; true open-L boundary lengths paired red/blue, no source partition. Migrated to detached span annotations to preserve the physical-paper interpretation.'),
              'reference_PNG_sha256':filehash(TASK / 'references/Plane233/C01.png'),
              'reference_plugin_sha256':filehash(TASK / 'references/Plane233/C01.json'),
              'material_difference_from_all_known_prior_attempts':plan['difference'],
              'historical_PNG_collision_audit':collisions,
              'human_semantics_before_visual_review':plan.get('human_semantics','Every added mark is outside the material with a nonzero gap and short perpendicular end caps: an external dimension/comparison bracket, not transported colored edging. Original grids, all unit-cell fills, all source/option boundaries and labels are untouched. The 4 independent brackets are open; no interior partition, closed region or third area-bearing piece is drawn. Under physical paper/ink reading all shown material remains exactly the original black-white material. Actual image still requires primary visual review before calls.'),
              'conciseness':plan.get('conciseness','Four meaningful span lines plus their eight extent caps. Each cap disambiguates a true endpoint; no overwritten or duplicate properties.'),
              'status':'FROZEN_UNTESTED_PRIMARY_RESEARCH_ONLY',
              'no_Pass_Collect_or_user_approval':True}
    if number=='p03':
        design['marking_mode']='native_boundary'
        design['material_color_proof_path']=plan['color_proof_path']
        design['material_color_proof_sha256']=filehash(plan['color_proof_path'])
    with (out / 'design.json').open('x',encoding='utf-8',newline='\n') as f:
        json.dump(design,f,ensure_ascii=False,indent=2,allow_nan=False); f.write('\n')
    write(out / 'reference_transfer.json',{'created_at':now(),'question_id':qid,
        'current9_references_all_viewed_and_plugins_read':True,
        'main_reference':design['source_reference'],'PNG_sha256':design['reference_PNG_sha256'],
        'plugin_sha256':design['reference_plugin_sha256'],'migration_groups':plan['groups'],
        'current_reference_not_old18':True,'historical_difference':plan['difference'],
        'limitation':'Detachment is a deliberate adaptation needed by the physical-piece semantics. It is subject to parent independent review.'})
    write(out / 'render_gates.json',{'created_at':now(),'fresh_schema_passed':True,
        'schema_sha256':filehash(PROJECT / 'PlaneGeometry/workbench/plugin.schema.json'),
        'default_normalization_exact':True,'original_noop_pixel_equal':True,
        'current_context_exact_JSON_equal':True,
        'context_comparison':'JSON canonicalization only converts tuple/list representation; all values/order/keys remain exact. No tolerances.',
        'twice_identical_plugin_bytes_and_PNG_bytes':True,
        'image_sha256':digest(png),'pixel_sha256':pix,'plugin_sha256':filehash(out/'plugin.json'),
        'design_sha256':filehash(out/'design.json'),'environment':environment_versions(),
        'source_inputs':before,'isolation':ISOLATION,'strict_ownroot_writeguard':True,
        'independent_process_exact_replay_required_before_API':True})
    assert fingerprints(ad,qid) == before
    write(out / 'source_edge_path_fingerprints.json',{
        'context_sha256':filehash(out/'context.json'),
        'frozen_context_canonical_sha256':digest(canonical(context).encode()),
        'original_targets_and_paths':context['canvas']['targets'],
        'all_new_marks_are_declared_add_line_actions':all(a['type']=='add_line' for a in actions),
        'no_original_path_overrides':all(a['type']!='set_object_style' for a in actions),
        'true_comparison_edges':[g[1] for g in plan['groups']]})
    checkpoint = read(OWN / 'checkpoint.json')
    checkpoint['updated_at'] = now()
    checkpoint['question_status'][qid] = 'frozen_rendered_awaiting_visual_review_and_exact_replay'
    write(OWN / 'checkpoint.json',checkpoint)
    print(json.dumps({'question_id':qid,'directory':str(out),'image_sha256':digest(png),'actions':len(actions)},ensure_ascii=False))

def replay(qid, variant):
    cfg, ad = adapter()
    from mathvision_plugins import PluginRenderer
    from workbench_io import pixel_hash
    out = OWN / qid / variant
    before = fingerprints(ad,qid)
    assert before == read(out/'render_gates.json')['source_inputs']
    context = ad.inspect_question(qid)
    assert canonical(context) == canonical(read(out/'context.json'))
    renderer = PluginRenderer(cfg,ad,{qid:context})
    plugin = read(out/'plugin.json')
    normalized,data,pix = renderer.render(plugin,frozen=True)
    assert normalized == plugin
    assert data == (out/'candidate.png').read_bytes()
    assert pix == read(out/'render_gates.json')['pixel_sha256']
    assert fingerprints(ad,qid) == before
    write(out/'independent_process_exact_replay.json',{
        'created_at':now(),'pid':os.getpid(),'python_command':sys.argv,
        'frozen_plugin_equal':True,'PNG_bytes_equal':True,'pixel_hash_equal':True,
        'context_JSON_exact_equal':True,'source_inputs_equal':True,
        'image_sha256':digest(data),'plugin_sha256':filehash(out/'plugin.json'),
        'design_sha256':filehash(out/'design.json'),'strict_ownroot_writeguard':True,
        'scope':'Independent local replay process only; this is not an independent second review.'})
    print(json.dumps({'question_id':qid,'new_process_exact_replay':True,'pid':os.getpid()}))

if __name__ == '__main__':
    if sys.argv[1] == 'create': create(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'p01')
    elif sys.argv[1] == 'replay': replay(sys.argv[2],sys.argv[3])
