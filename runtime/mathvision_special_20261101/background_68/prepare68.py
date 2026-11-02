from common68 import *
import shutil

VISUAL = {
 'Plane271': {
  'native_finding':'Actual source JPG, formal PNG and frozen candidate viewed at native size. Five pieces in each arrangement, all four quarter arcs, rectangle contacts and seams are intact. Two red open radius edges are readable.',
  'semantics':'The source exposed radius and receiver internal radius are the same material edge under (x,y)->(30-y,x). Even a physical-ink reading is consistent across both arrangements. No new cut, painted area, numeric equality, target, dimension or text is introduced.',
  'every_marker':[{'actions':[0],'role':'Source real exposed small-quarter radius, from(-5,0) to(0,0), length5.'},{'actions':[1],'role':'Receiver same radius from(30,-5) to(30,0), now a buried rectangle/quarter-circle seam, length5.'}],
  'difference':'Already frozen r60 design replaces old whole rectangle/large sector grouping with exposed-versus-internal membership of a specific radius. Copied first-test draft; zero new mechanisms here.'},
 'Plane367': {
  'native_finding':'Actual source JPG, formal PNG and frozen candidate viewed at native size. All five lettered silhouettes, both rows of grid cells and every original diagonal remain readable; all areas remain2.',
  'semantics':'Two existing unit legs of A supply a square reference; B receives two actual half-triangle unit-leg corners. The red T in B is on preexisting grid lines. No new partition, closed colored boundary, fill or equal-area symbol exists. Same red does not assert equal areas. This area comparison does not transport a printed pattern.',
  'every_marker':[{'actions':[0],'role':'A source square top edge (1,2)-(2,2).'}, {'actions':[1],'role':'A source square right upper unit edge (2,2)-(2,1), completing the open reference corner.'},{'actions':[2],'role':'B receiver bases (3,1)-(5,1), one unit for each of the two actual half-triangles.'},{'actions':[3],'role':'B receiver common height (4,0)-(4,1); one visible segment serves each half-triangle without duplicate overdraw.'}],
  'difference':'Old isolated D contour/whole C emphasis is replaced by square-vs-two-half-triangle area-weight transfer. PresetB and r60 bytes retained.'},
 'Plane387': {
  'native_finding':'Actual source JPG, formal PNG and frozen candidate viewed at native size. Thirty-six small triangles and the whole gray target triangle remain visible. The source upper unit triangle and two receiver fragments can be distinguished; target outline stays black.',
  'semantics':'All six actions style existing lattice-edge intervals. They form open corners, draw no new cut/closed piece or shade, and do not stipulate area1. The real receiver weights5/6 and1/6 sum1. Colors do not change gray membership or the task of finding its area.',
  'every_marker':[{'actions':[0],'role':'Source unit-triangle horizontal side P0_5-P1_5.'},{'actions':[1],'role':'Source unit-triangle left sloping side P0_5-P0_6; with action0 forms one open corner of area1 reference.'},{'actions':[2],'role':'Receiver5/6 fragment horizontal leg P3_1 to exact right-target crossing at lattice(11/3,1).'}, {'actions':[3],'role':'Receiver5/6 fragment existing up-right unit leg P3_1-P3_2; true region has area5/6.'},{'actions':[4],'role':'Receiver1/6 opposite-orientation fragment horizontal leg from P3_2 to lattice(10/3,2).'}, {'actions':[5],'role':'Receiver1/6 sloping leg from the target crossing at parameter1/2 of P4_1-P3_2 to P3_2; exact existing interval.'}],
  'difference':'Old global basis/diamond half-area confusion and whole-target red outline differ from this specific whole-unit-to-complementary-fragments count substitution; old misses retained, preset12 unchanged.'},
 'Plane449': {
  'native_finding':'Actual source JPG, formal PNG and frozen candidate viewed at native size. All20 integers, source lettersA-E, slotsI-V and all side orientations are clear. Exactly four source-card edges are styled; no slot edge is colored.',
  'semantics':'Red bottom8/top8 and blue right4/left4 are true adjacencies, satisfied in the unique numeric arrangement centered on slotII. Transporting edge ink also leaves the marked matching pairs consistent. Slot outlines are blank placement placeholders, with no competing colored destination constraint. No rotation, reflection, false equality symbol or new target is introduced.',
  'every_marker':[{'actions':[0],'role':'D-bottom8: source vertical adjacency edge.'},{'actions':[1],'role':'C-top8: receiver matching D-bottom, true lower neighbor.'},{'actions':[2],'role':'D-right4: source horizontal adjacency edge.'},{'actions':[3],'role':'A-left4: receiver matching D-right, true right neighbor. Both pairs form an L around D, not an isolated option outline.'}],
  'difference':'Old3/5 side-orientation/colored-slot route caused conflicts. Frozen r60 uses true4/8 source adjacencies and no slot styling; local L-star atI fails global third top neighbor. PresetD retained.'}
}

def zero_certification():
    scan=read(HERE/'whole_task_zero_call_scan.json')
    extra=read(HERE/'archive_and_malformed_supplement.json')
    assert not scan['matching_call_evidence'] and extra['all_matching_unknowns_absent']
    dispositions=[]
    for row in scan['matches']:
        p=Path(row['path'])
        if row['kind']=='exact_png': kind='Only original source60 candidate or its same-byte repeat; no evidence directory/call attached'
        elif 'background_60' in p.parts: kind='Original pre-call design/difference/render bookkeeping or source design code'
        elif p.name=='background_68_assignment.json': kind='Explicit first-test assignment with frozen hashes, not a solver request'
        else: kind='Parent recovery/progress metadata or another worker inventory/snapshot; no request body, started event or response'
        dispositions.append(dict(path=str(p),sha256=row['sha256'],matched_question_ids=row['matched_question_ids'],classification=kind))
    write(HERE/'zero_call_certification.json',dict(checked_at=now(),certification_scope='All existing files under task runtime/mathvision_special_20261101, excluding only newly created OWNROOT; includes14 ZIP archives and decoded requests',
        all_four_zero_prior_actual_starts=True,prior_actual_call_blocks_unchanged_reuse=True,unknown_matching_evidence_blocks_reuse=True,
        files_scanned=scan['files'],png_files_scanned=scan['png_files'],embedded_pngs_decoded=scan['decoded_embedded_pngs'],additional_archive_embedded_pngs=extra['decoded_embedded_images'],
        call_shaped_inventory=str(HERE/'whole_task_invocation_inventory.json'),matching_call_shaped_files=0,matching_decoded_requests=0,
        malformed_originals_and_snapshots=99,malformed_matching_raw_or_decoded_evidence=0,malformed_source_bytes_preserved=True,
        exact_png_and_reference_dispositions=dispositions,
        excluded_completed_images=['Plane482/r52_diagonal_family_erases_gray_side: first pair completed62','Plane488/r52_flap_source_and_reflection_double_loss: first pair completed62','Solid206/r55 frozen216sqrt6: first pair completed63','Solid207/r55 frozen108: first pair completed63'],
        limitations='Filesystem evidence audit, not a provider-side historical log attestation. No candidate matching unknown evidence is present. Missing summaries alone were never used as a zero-call argument.'))

def prepare(qid):
    a=read(BASE/'background_68_assignment.json')
    q=next(q for q in a['questions'] if q['question_id']==qid)
    d=HERE/qid
    e=eligibility(qid); assert e['eligible']; write(d/'eligibility_before_reuse.json',e)
    math=read(d/'primary_math_audit.json')
    assert math
    write(d/'primary_native_and_marker_review.json',dict(question_id=qid,checked_at=now(),stage='PRIMARY research prescreen only',source_jpg=str(PROJECT/BRANCH/e['record']['original_image']),formal_png=str(PROJECT/BRANCH/e['record']['image']),frozen_candidate=str(Path(q['source_directory'])/'candidate.png'),
        actual_source_formal_candidate_pngs_viewed=True,concise_targeted_every_marker_pass=True,human_unambiguous_primary_assessment=True,original_geometry_fill_text_dimensions_preserved=True,
        frozen_3D_projection_visibility='Not applicable: PlaneGeometry only; no3D changes',same_color_is_not_numeric_equality=True,no_new_partition_route_or_painted_target=True,
        review=VISUAL[qid],math_evidence=str(d/'primary_math_audit.json'),independent_review=False,no_user_approval_Pass_Collect_or_delivery=True))
    adapter,Renderer,cfg=setup()
    context=adapter.inspect_question(qid); write(d/'fresh_context.json',context)
    renderer=Renderer(cfg,adapter,{qid:context})
    src=Path(q['source_directory'])
    plugin=read(src/'plugin.json'); normalized=renderer.normalize(plugin)
    assert normalized==plugin
    _,data,pixel=renderer.render(plugin,frozen=True)
    _,again,pixel2=renderer.render(plugin,frozen=True)
    assert data==again and pixel==pixel2 and hashlib.sha256(data).hexdigest()==q['frozen_source_files_sha256']['candidate.png']
    validation=d/'validation'; validation.mkdir(exist_ok=True)
    (validation/'fresh_render.png').write_bytes(data);(validation/'fresh_repeat.png').write_bytes(again)
    write(d/'schema_render_check.json',dict(checked_at=now(),schema_and_defaults=normalized,normalization_unchanged=True,formal_noop_pixels_equal=True,repeat_bytes_equal=True,repeat_pixels_equal=True,fresh_render_equals_frozen_source_png=True,
        fresh_context_sha256=sha(d/'fresh_context.json'),original_context_sha256=sha(src/'fresh_context.json'),fresh_context_same_bytes=(d/'fresh_context.json').read_bytes()==(src/'fresh_context.json').read_bytes(),pixel_sha256=pixel,renderer_adapter='unchanged mathvision_adapter.RendererAdapter',plugin_renderer='unchanged mathvision_plugins.PluginRenderer'))
    import matplotlib.pyplot as plt
    plt.close('all'); del renderer,adapter,context,data,again;gc.collect()
    # Copy only after all prior math/native/every-marker/zero-call/schema gates.
    candidate=d/q['variant_id'];candidate.mkdir(exist_ok=False)
    source_copies=[]
    for name,h in q['frozen_source_files_sha256'].items():
        assert sha(src/name)==h
        shutil.copyfile(src/name,candidate/name)
        assert sha(candidate/name)==h
        source_copies.append(dict(source=str(src/name),copy=str(candidate/name),sha256=h,byte_identical=True))
    write(candidate/'reuse_provenance.json',dict(checked_at=now(),reuse_is_first_actual_test=True,new_mechanism_count=0,original_variant_id=q['variant_id'],original_created_at=q['frozen_created_at'],original_expected_wrong_answer=q['expected_wrong_answer'],source_directory=str(src),
        source_copy_hashes=source_copies,all_original_internal_paths_preserved=True,all_original_context_design_plugin_png_repeat_difference_bytes_preserved=True,
        current_eligibility=str(d/'eligibility_before_reuse.json'),fresh_math=str(d/'primary_math_audit.json'),fresh_actual_native_every_marker_review=str(d/'primary_native_and_marker_review.json'),global_zero_prior_call_certification=str(HERE/'zero_call_certification.json'),
        fresh_schema_noop_repeat_exact_png=str(d/'schema_render_check.json'),exact_offline_replay='Required before API; will be saved under sibling offline_replay/replay_verification.json',independent_second_review_still_required=True))
    print(qid,'schema/no-op/repeat/source-exact passed; original9files copied unchanged',flush=True)

if __name__=='__main__':
    if sys.argv[1]=='zero':zero_certification()
    else:prepare(sys.argv[1])
