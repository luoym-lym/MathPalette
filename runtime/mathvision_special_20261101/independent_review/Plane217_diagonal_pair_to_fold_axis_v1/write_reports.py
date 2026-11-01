"""Write the independent reviewer's conclusions; never edits input evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import sys

sys.dont_write_bytecode = True
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
TASK = ROOT/'runtime/mathvision_special_20261101'
OWN = [TASK/'independent_review/Plane217_diagonal_pair_to_fold_axis_v1',TASK/'independent_review/Plane234_three_feature_match_ignores_gray']
def guard(event,args):
    def check(p):
        if p is not None and not isinstance(p,int) and not any(Path(os.fsdecode(p)).resolve().is_relative_to(x.resolve()) for x in OWN):
            raise PermissionError('Write outside independent review folders')
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
    elif event in ('socket.connect','socket.connect_ex','socket.getaddrinfo'):raise PermissionError('Offline reviewer')
sys.addaudithook(guard)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def relative(p):return Path(p).relative_to(ROOT).as_posix()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

paths = ['background_05/plane_a/Plane217/diagonal_pair_to_fold_axis_v1','background_05/plane_b/Plane234/three_feature_match_ignores_gray']
for qid,cdir,out,target,correct,finals,controls in zip(['Plane217','Plane234'],paths,OWN,['A','D'],['C','B'],[['A','A'],['D','D']],[['C','C'],[]]):
    cand=TASK/cdir
    audit=read(out/'integrity_audit.json')
    math=read(out/'independent_math_audit.json')
    assert audit['all_required_integrity_checks_pass']
    report={
      'review_kind':'NEW_INDEPENDENT_SECOND_REVIEW',
      'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
      'decision':'recommended',
      'question_id':qid,
      'candidate_directory':cdir,
      'candidate_path':(cand/'candidate.png').as_posix(),
      'formal_correct_answer':correct,
      'predeclared_wrong_answer':target,
      'actualcandidatefinals':finals,
      'controlfinals':controls,
      'actual_candidate_finals':finals,
      'original_control_finals':controls,
      'recommendation_scope':'Independent recommendation for parent review only. No user approval, Pass, Collect, formal write or publication.',
      'independence_and_execution':{
        'candidate_designer':False,'subagents_started':0,'model_or_API_calls':0,
        'reviewer_writes_and_caches':'Only the two named independent_review folders; Python -X utf8 -B; own-folder filesystem write guard; socket connection guard.',
        'optional_render':'Fresh no-op and two exact production candidate redraws per case, with shared runtime_isolation.install before drawing imports; TMP/TEMP/MPLCONFIGDIR/XDG_CACHE_HOME all inside own review folder.',
        'prior_evidence_and_formal_files_preserved':True,
        'protected_existing_files_verified':3515},
      'checks':{
        'current_eligibility':{'status':'pass','detail':'Current formal MathVision record has its exact authoritative user approval content fingerprint. No matching accepted-index or collected-index entry and no question Special directory, recipes or collection (including special completion). Mutable remaining_questions status is now explored_no_deliverable; this does not create an accepted or collected item.','approval_content_sha256':audit['approval']['computed_current_content_sha256']},
        'frozen_request_and_two_separate_calls':{'status':'pass','detail':'Decoded actual request image bytes equal the current candidate. Exact existing solver SYSTEM_PROMPT plus exactly formal question and PNG; only system/user messages, with no history, answer, source, intent, instructions or token caps. Exact quicktest3 mimo-v2.6-flash, thinking.type=disabled, stream=false, configured official endpoint. Current quick_test.py hash matches frozen binding. Both run starts/results and complete raw provider bodies bind the same immutable request/design/image. Distinct run and provider response IDs; both HTTP 200, completed, finish_reason=stop, untruncated. Provider prefix caching, where recorded, does not add conversation history.'},
        'preset_before_both_starts':{'status':'pass','detail':'Current design.json is byte-identical to design_snapshot.json; target is unchanged in both and binding. Design creation precedes binding creation and each recorded start. Read-only harness inspection confirms snapshot/request writes precede its two-call loop and it checks unchanged image/design before each call. Chronology is local evidence, not a signed external timestamp.'},
        'all_material_hashes':{'status':'pass','detail':'Independently recomputed current formal record, dataset, approval content, original source JPG, formal PNG/pixels, candidate PNG/pixels, plugin, design, design snapshot, actual request, each raw response, reference quick_test.py, all recorded rendering inputs, and every claimed actual vector-path fingerprint. All match the relevant frozen bindings and reports. Exact hashes and run IDs are in integrity_audit.json.','hashes':audit['original_and_candidate_hashes'],'request_body_sha256':audit['candidate_tests']['binding']['request_body_sha256'],'question_record_sha256':audit['candidate_tests']['binding']['question_record_sha256']},
        'runtime_summary_hashes':{'status':'nonblocking_metadata_mismatch','detail':'The historical eligibility snapshot hashes of remaining_questions.jsonl and exploration_report.json no longer equal their current bytes. Both now track the completed exploration, without Pass/Collect. All other recorded eligibility state hashes match. This diagnostic is retained as false in integrity_audit.json; no historical evidence was rewritten. Current eligibility was independently re-established from authoritative formal/approval/accepted/collected state.'},
        'schema_and_reproduction':{'status':'pass','detail':'Actual production schema/default/semantic-target/whitelist validation accepts the frozen plugin without normalization changes. Fresh production no-op matches formal pixels, and two fresh candidate renders match each other and the exact tested PNG bytes and pixels. No pixel guard bypass, geometry edit, changed viewport, added text or hidden formal parameter.'},
        'manual_complete_response_review':{'status':'pass','candidate_finals':finals,'control_finals':controls,'detail':'Reviewer manually read both complete candidate raw bodies, and both complete original-control raw bodies where available. Final choices are taken from the conclusions, not keyword counts or summary tails.'},
        'rigorous_unique_unchanged_math':{'status':'pass','unique_answer':correct,'evidence':relative(out/'independent_math_audit.json')},
        'human_problem_and_mark_roles':{'status':'pass','detail':'Actual source JPG, formal PNG and current tested candidate PNG viewed. Candidate preserves original given features, object ownership, labels and readable solution. Every action has a specific correspondence role as listed below; no count quota or causal per-marker necessity claim is used.'},
        'preservation':{'status':'pass','detail':'3515 existing evidence/formal/protocol/dependency files were hashed before and after the isolated audit; no changes or deletions. Write guards restrict reviewer output to own folders.'}},
      'issues':[],
      'rationale':[],
      'marker_necessity':[],
      'limitations':[
        'Two target hits are two observed outputs on one frozen image; they are not a causal or statistical gain estimate or a guarantee on future calls.',
        'No human-performance experiment or per-marker statistical ablation was conducted; neither is imposed as an additional hard gate.',
        'Roles justify the complete marking scheme; they do not establish that each individual action is causally indispensable.',
        'Distinct stateless requests are verified from the local request/harness and response records. Provider-side implementation and unsigned historical timing cannot be independently authenticated offline.',
        'Historical mutable runtime summary hashes differ as disclosed; authoritative current formal/approval/Special state and frozen test evidence remain consistent.'],
      'evidence':{'integrity_audit':relative(out/'integrity_audit.json'),'independent_math_audit':relative(out/'independent_math_audit.json'),'preservation_audit':relative(out/'preservation_audit.json'),'candidate_tests':audit['candidate_tests']['directory']},
      'manual_final_readings':[
        {'run':i+1,'final_choice':finals[i],'raw_response_path':audit['candidate_tests']['runs'][i]['raw_response_path'],'raw_response_sha256':audit['candidate_tests']['runs'][i]['response_sha256'],'complete_body_read':True}
        for i in range(2)]}
    if qid=='Plane217':
      report['checks']['rigorous_unique_unchanged_math']['detail']='Paper center is (10,8), holes are (+/-1,+/-0.55). Horizontal and vertical midline reflections identify exactly those four holes into one punch position, yielding C. A diagonal reflection swaps the unequal magnitudes 1 and 0.55, so it generates absent holes; the exact A orbit is independently enumerated. All B/E folds are vertical and preserve y, impossible for two hole heights. Every D crease has slope +1, so each reflection and any composition preserve x+y; the four observed holes have four distinct sums, impossible from one punch. C is therefore uniquely valid.'
      report['checks']['human_problem_and_mark_roles']['detail']='At the actual 768x768 image, all four tiny holes still have separate white interiors and unchanged 1pt contours/centers/radii. The nonsquare 2 by 1.1 hole-center rectangle remains visible. Only A existing diagonal axes get colored 2pt dashed strokes; all crease counts, orientations, paper boundaries and A-E labels remain clear. Colors are optional Special correspondence marks, not stated physical invariants of a punch or extra equality conditions.'
      report['checks']['original_controls']={'status':'pass','finals':['C','C'],'detail':'Both complete control responses select C; the control PNG bytes exactly equal the current formal PNG. Control design/binding preset remains A, while its observed correct finals are C/C. Correct control answers support the description of this small comparison but are not an extra eligibility gate and do not prove causation.'}
      report['issues']=[
        {'severity':'nonblocking_documentation_nuance','location':'Frozen design.json and primary_review.json mechanism wording','detail':'The phrase same-slope is numerically inaccurate: the red/blue hole chords have slopes -0.55/+0.55, whereas A axes have slopes -1/+1. The supported description is falling/rising orientation and same-color diagonal-pair correspondence, not exact parallelism. Frozen documentation was preserved.'},
        {'severity':'nonblocking_evidence_limit','detail':'Candidate run 2 incorrectly calls the hole rectangle a square and misdescribes D as vertical; both candidate narratives wrongly treat outline colors as folding invariants. These are model errors, not proof of geometry or a requirement for identical reasoning. The independent reflection proof does not rely on them.'},
        {'severity':'nonblocking_runtime_metadata','detail':report['checks']['runtime_summary_hashes']['detail']}]
      report['rationale']=[
        'Recommend this exact frozen candidate: both complete independent quicktest3 calls end A, with predeclared A, while the unique rigorous answer remains C and the original-control finals are C/C.',
        'The four source-hole marks encode two opposite endpoint pairs. A corresponding colored dashed axis in A completes each specific false pair-to-fold-axis association. This carries ordered geometric feature information beyond generic option highlighting, even though the chord/axis directions only agree qualitatively.',
        'The observed responses follow color-based opposite-hole grouping while overlooking the nonsquare metric/reflection obstruction. That is consistent with the proposed feature correspondence hypothesis; two calls do not isolate its cause.',
        'All six actions have concrete roles, preserve the given geometry and hole readability, and add no extraneous objects or visual clutter. The slope wording must be qualified in any later explanation; do not edit this frozen design or its tested image.']
      roles={
        'o2':('red','top-left existing hole','o3 and o7','First endpoint of the falling opposite-hole pair; supplies the source member, not a new hole.'),
        'o3':('red','bottom-right existing hole','o2 and o7','Second endpoint completes that source pair and fixes its falling orientation.'),
        'o1':('blue','bottom-left existing hole','o4 and o6','First endpoint of the rising opposite-hole pair; separates it from the red pair.'),
        'o4':('blue','top-right existing hole','o1 and o6','Second endpoint completes the rising pair and its different diagonal ordering.'),
        'o7':('red','A existing falling dashed axis','o2 and o3','Binds the red opposite-hole pair to an incorrect candidate folding axis through color and falling direction; 2pt increases visibility without changing dashed semantics.'),
        'o6':('blue','A existing rising dashed axis','o1 and o4','Binds the other opposite-hole pair to A second axis, completing a two-feature correspondence rather than only highlighting A.')}
      for i,a in enumerate(read(cand/'plugin.json')['params']['actions']):
        color,owner,pair,role=roles[a['target']]
        report['marker_necessity'].append({'action_index_1_based':i+1,'type':a['type'],'target':a['target'],'color_group':color,'feature_owner':owner,'paired_features':pair,'role':role,'new_geometry':False,'linewidth_pt':a.get('linewidth_pt',1)})
      report['limitations'].append('Original controls also use approximate square-pattern wording; their C finals do not replace the independent coordinate proof.')
      report['evidence']['original_control_tests']=audit['control_tests']['directory']
      report['manual_control_final_readings']=[{'run':i+1,'final_choice':'C','complete_body_read':True,'raw_response_path':audit['control_tests']['runs'][i]['raw_response_path'],'raw_response_sha256':audit['control_tests']['runs'][i]['response_sha256']} for i in range(2)]
    else:
      report['checks']['rigorous_unique_unchanged_math']['detail']='From actual frozen path vertices and semantic shades, ordered clockwise by tip angle starting at the top ray, the source word is MMLLSMLSSSMLLMSLSS. S=(white,radius1.5), M=(gray,radius1.75), L=(dark,radius2), with common face radius1 and 20-degree ray spacing. Actual options A=LLSS, B=LMSL, C=MLMS, D=LSSL, E=SSLS. Independently enumerated all 18 four-ray cyclic windows: only B occurs, at sunray12..15. Rotating their actual vertices by 270 degrees and translating aligns B to numerical precision, preserving shades. The marked sector sunray3..6 is LSML; D is LSSL. Their third rays differ in both shade and length. Geometry, shades and order are unchanged by the legal outline/edge operations, so B remains unique.'
      report['checks']['human_problem_and_mark_roles']['detail']='Viewed full source/formal/candidate images at native size, then own-runtime nearest-neighbor analysis enlargements of the source and D. The green source third ray retains a discernible medium-gray triangular interior, distinct from both its blue white neighbor and the white interior of D green ray. It also visibly projects farther from the circular base than a short white ray: source radius1.75 versus1.5, approximately7.2px of tip-radius difference at the actual common image scale. These two redundant distinguishing cues survive. The outline reduces gray area but does not erase or make it white. Small scale is a caveat; this pass is based on visible shade plus length, not fill parameters or a pixel-count cutoff. All 18 source rays, four rays in each option, face and option letters remain identifiable; no new ray, connecting line or label clutter.'
      report['checks']['semantic_fill_preservation']={'status':'pass_with_small_feature_caveat','detail':'Read semantic_fill_preservation_audit.json and independently checked every listed retained fill pixel against actual formal/candidate PNG. sunray5 retains16 original exact-gray pixels from27 originally reported; all16 coordinates are verified. The four marked source ray interiors retain their dark/white/gray/dark identities. This count is supporting evidence only; native-image and shade/length visual review determines legibility.'}
      report['checks']['overlaid_endpoints']={'status':'pass','detail':'All eight add_line actions have endpoints exactly equal to the corresponding two existing straight sides in current frozen commands. Fresh captured vector segments independently agree. Each is a 1pt solid whitelisted color overlay; the four source styles are legal 2pt edge overrides. Numeric-leading D IDs cannot be set_object_style targets under the actual schema, so exact edge overlays legally supply the four partner contours. No new ray tip or base endpoint is created.'}
      report['checks']['manual_complete_response_review']['run_2_trailer']='The complete raw run 2 body explicitly concludes Answer: D and then ends System instruction:. No text follows that trailer and no contradictory choice occurs; finish_reason is stop, no length or HTTP truncation is recorded. This is malformed trailing response text, not an extra message in the request or a competing final answer.'
      report['checks']['original_controls']={'status':'not_run','finals':[],'detail':'No Plane234 original-control evidence is present; none was newly requested or run. This is disclosed, not treated as an extra gate.'}
      report['issues']=[
        {'severity':'nonblocking_small_feature_caveat','detail':'The source sun is small and the 2pt green outline narrows the critical gray interior. After direct native-size and own analysis-zoom inspection, gray shade and greater length remain distinguishable. Recommendation is for these exact tested bytes; further stroke thickening or rescaling requires a fresh review.'},
        {'severity':'nonblocking_response_artifact','detail':'Run2 has trailing System instruction: after its unambiguous final D, without contradictory continuation. Full body was inspected and preserved.'},
        {'severity':'nonblocking_runtime_metadata','detail':report['checks']['runtime_summary_hashes']['detail']}]
      report['rationale']=[
        'Recommend this exact candidate: two complete separate quicktest3 finals are D/D against a D preset frozen before both starts, and independent cyclic-word and coordinate checks retain unique correct answer B.',
        'Four ordered color correspondences bind an almost matching source part LSML to D LSSL. Outer dark rays locate its endpoints, the blue white ray fixes internal order, and green is the specific false correspondence between a medium-gray longer ray and a short white ray. This supplies targeted feature matching beyond generic wrong-option salience.',
        'The critical green source ray remains visibly gray and longer, while the green D partner is white and shorter. Native images and analysis enlargements support the human gate jointly on shade and length; retaining a fill parameter or16 pixels alone would not suffice.',
        'Each of the twelve actions has a traceable ray/side role, all overlay endpoints coincide with existing sides, and no added rays or unrelated marks occur. Both responses choose colored correspondence while failing to compare original shades; this describes the observed behavior without a causal or gain claim.']
      colors=['red','blue','green','orange']
      semantic_roles=[
        'First long dark ray anchors the beginning of the proposed four-ray part and its orientation.',
        'Second short white ray fixes the first internal feature and its position in the ordered match.',
        'Third medium-gray longer source ray is the exact mismatch; the color falsely associates it with D short white third ray while both distinguishing cues remain visible.',
        'Fourth long dark ray closes the part and fixes its end; together the end rays delimit the four-feature sequence.']
      for i,a in enumerate(read(cand/'plugin.json')['params']['actions']):
        if a['type']=='set_object_style':
          j=int(a['target'].removeprefix('sunray'))-3
          role=semantic_roles[j]
          obj=a['target']
          pair=f'3ray{j}'
          detail='One original whole ray outline, including its two flanks; fill, tip, circular base, length and angular placement remain frozen.'
        else:
          obj,edge=a['id'].removeprefix('Pair_').split('_edge')
          j=int(obj.removeprefix('3ray'))
          pair=f'sunray{3+j}'
          side='first' if edge=='0' else 'second'
          role=f'The {side} original straight flank of D ray {j+1} completes that ray color contour and its pairing with {pair}. '
          role+=('This is the intentionally false third-feature correspondence: white/short versus medium gray/longer.' if j==2 else semantic_roles[j])
          detail='Exactly coincident 1pt trace of this existing side, independently checked against both frozen endpoints and fresh actual vector segment. It adds no ray or free-standing construction.'
        report['marker_necessity'].append({'action_index_1_based':i+1,'type':a['type'],'target_or_id':a.get('target',a.get('id')),'feature_owner':obj,'paired_feature':pair,'color_group':colors[j],'role':role,'geometry_and_fill_preservation':detail,'linewidth_pt':a['linewidth_pt']})
      report['limitations']+=['No original-control pair exists for Plane234; D/D alone cannot measure a change from the formal-image baseline.',
        'The tiny semantic gray region makes native readability sensitive to display scaling. No human accuracy rate is claimed; this review inspected the exact 768x768 PNG plus analysis-only nearest-neighbor crops, never substituting those crops for the tested image.',
        'Both candidate responses prioritize color correspondence and fail to correctly compare the preserved gray fills. The two reasoning narratives are evidence of these outputs, not an independent mathematical proof.']
      report['evidence']['analysis_only_source_comparison']=relative(out/'analysis_source_comparison_6x.png')
      report['evidence']['analysis_only_D_comparison']=relative(out/'analysis_option_D_comparison_6x.png')

    # Verify current candidate and all prior monitored input bytes again, after
    # writing scripts and before committing either conclusion.
    assert sha(cand/'candidate.png')==audit['original_and_candidate_hashes']['candidate_png_sha256']
    write(out/'independent_review.json',report)
    print(qid,report['decision'],(out/'independent_review.json').as_posix())

before=read(OWN[0]/'protected_files_before.json')
after={p:sha(ROOT/p) for p in before}
assert after==before
for out in OWN:
    preserve={'checked_existing_files':len(before),'all_preserved':True,'changed':[],'no_existing_files_deleted':True,'rechecked_after_final_reports':True}
    write(out/'preservation_audit.json',preserve)
    report=read(out/'independent_review.json')
    assert report['decision'] in ('recommended','hold','reject')
    assert all(k in report for k in ('question_id','candidate_directory','candidate_path','checks','issues','rationale','marker_necessity','limitations','actualcandidatefinals','controlfinals'))
    assert len(report['marker_necessity'])==({'Plane217':6,'Plane234':12}[report['question_id']])
    print(report['question_id'],'report_schema_and_every_action_role_ok',len(report['marker_necessity']))
print('Final preservation verification:',len(before),'existing files unchanged')
