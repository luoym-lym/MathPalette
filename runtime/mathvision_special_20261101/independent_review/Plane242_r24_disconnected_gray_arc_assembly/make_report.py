from review_env import *
import hashlib
import json
from datetime import datetime, timezone
from PIL import Image

def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def fh(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def write(name,data):
    with (HERE/name).open('x',encoding='utf-8',newline='\n') as f:
        json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False); f.write('\n')
audit = read(HERE/'evidence_audit.json')
render = read(HERE/'native_render_audit.json')
assert all(audit['checks'].values()) and all(render['checks'].values())
assert all(all(r['checks'].values()) for r in audit['runs'])
assert audit['eligibility']['eligible']
QID,VID = audit['question_id'],audit['variant_id']
CAND = BASE/'background_24'/QID/VID
TEST = next((CAND/'tests').iterdir())
BRANCH = ROOT/'PlaneGeometry'
scene = read(BRANCH/'dataset_generator/scenes/Plane242.json')
formal = audit['eligibility']['formal_record']
source = read(BRANCH/'dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane242/source.json')
design = read(CAND/'design.json')
before = audit['frozen_artifacts_before']
after = {p:fh(ROOT/p) for p in before}
drift = {p:{'before':v['sha256'],'after':after[p]} for p,v in before.items() if v['sha256'] != after[p]}
assert not drift,drift
write('preservation_after.json',{'checked_at_utc':now(),'tracked_files':len(before),
    'changes_to_tracked_preexisting_files':drift,'after_sha256':after,
    'scope':'Relevant formal source, workbench implementation, exact candidate evidence and selected historical evidence only; no whole-workspace unchanged claim.'})

option_proof = {}
fractions = {'A':{'gray':'1/4','white':'1/4','black':'1/2'},
             'B':{'gray':'1/2','white':'1/8','black':'3/8'},
             'C':{'gray':'3/8','white':'1/4','black':'3/8'},
             'D':{'gray':'1/2','white':'1/4','black':'1/4'},
             'E':{'gray':'1/2','white':'1/4','black':'1/4'}}
elimination = {
    'A':'Gray sectors are 50 + 40 = 90 degrees, area pi/4, half the required gray paper area pi/2. Its black area is also pi/2 rather than pi/4.',
    'B':'Gray is a valid 180-degree half-disk, but the white sector is only 45 degrees, area pi/8 rather than pi/4. No-overlap preserves the entire white piece; it cannot lose half its area.',
    'C':'White is a valid 90-degree quarter, but gray is only 135 degrees, area 3pi/8 rather than pi/2.',
    'D':'Areas agree, but gray occupies opposite quadrants 0..90 and 180..270. This set is nonconvex with disconnected interior and is not a rigid half-disk. See explicit witness and center-point qualification below.',
    'E':'Gray sector 125..305 is one intact 180-degree half-disk; white 350..440 is one intact 90-degree quarter; they do not overlap. The two black gaps are 80..125 and 305..350, each 45 degrees. Explicit placements are given below.'}
for i,letter in enumerate('ABCDE'):
    objects = [x for x in scene['objects'] if x['id'].startswith(f'option{i}_')]
    option_proof[letter] = {'frozen_native_sectors':objects,'areas_as_multiples_of_pi':fractions[letter],
                            'disposition':elimination[letter],'possible':letter == 'E'}

roles = [
  ('red_source','Source gray outer arc 0..90 degrees, the right half of the single semicircular outer boundary. It identifies one 90-degree arc without adding a radius or dividing the paper.',
   'Matched to D upper-right gray arc by translation (local rotation 0 degrees).'),
  ('blue_source','Source gray outer arc 90..180 degrees, the left half of that SAME continuous outer boundary; it meets the red portion at the top of the intact paper.',
   'Matched to D lower-left gray arc by local rotation +90 degrees. This different rotation is precisely the false independent-fragment move.'),
  ('red_D','D upper-right gray quarter outer arc 0..90 degrees. It is a genuinely congruent local arc, but not the outer boundary of a whole source semicircle.',
   'Red source counterpart; targets a specific part-to-part correspondence, rather than the choice label or the whole choice.'),
  ('blue_D','D lower-left gray quarter outer arc 180..270 degrees. Together with the red D arc it preserves total gray area while breaking the source half-disk into opposite quarters.',
   'Blue source counterpart; exposes the local-arc versus intact-paper error.'),
  ('green_source','The entire curved boundary of the actual source white 90-degree quarter. Both source radial edges and the right angle remain black and visible.',
   'A genuine whole-quarter match to D white quarter, not the old erroneous 90-versus-45-degree ordered-ray match.'),
  ('green_D','D white upper-left quarter outer arc 90..180 degrees. The full white region is a true rotation by +90 degrees of the source white piece.',
   'Completes the correct second-piece match so that the targeted D defect is the gray paper integrity, not a white area mismatch.')]
per_marker = []
for m,(name,feature,role) in zip(render['marker_geometry'],roles):
    per_marker.append({**m,'marker_name':name,'feature':feature,'informational_role':role,
      'legality':'Pass: actual frozen path/interval and permitted color/2 pt width; original solid style retained. No added point, auxiliary line, text, fill or freehand geometry.',
      'targeting':'Pass as an intended comparison annotation; the actual local arc/white-piece correspondence is verified independently.',
      'effectiveness':'Visible and informative; both frozen finals choose D. No causal or per-marker marginal effect is inferred.',
      'conciseness':'One existing open 90-degree arc with a specific source/counterpart role. No redundant invisible segment or unrelated decoration was found.',
      'human_readability':'Pass at native 768px: about 71.42px curved length, 2.78px stroke, visible gray/white interiors and black radial edges.',
      'human_unambiguity':'Fails at the combined image level: this mark is on the moving paper boundary itself and can reasonably be read as paper ink/colored edging. See the explicit color-preserving interpretation below.',
      'creates_new_cut_or_closed_region_or_relation_symbol':False})

finals = []
for r in audit['runs']:
    i = r['run_index']
    finals.append({'run_index':i,'full_final_text':r['complete_final_text'],
       'manually_read_entire_raw_response':True,'final_answer':'D','matches_predeclared_wrong_answer':True,
       'contradictory_terminal_letter_or_value':False,
       'raw_response_sha256':r['record']['response_sha256'],
       'raw_response_path':str(TEST/f'run_{i:02d}_response.json'),
       'started_at_utc':r['record']['started_at'],'finished_at_utc':r['record']['finished_at'],
       'finish_reason':r['record']['finish_reason'],'status':r['record']['status'],
       'narrative_corrections':('It wrongly says the black remainder is 3/4, misdescribes D gray as the left half and swaps D white/gray top quadrants. Actual remainder is 1/4; D gray is upper-right plus lower-left. These are narrative errors, not a competing final numerical answer to this pictorial choice question.' if i==1 else
        'It wrongly describes D gray as a bottom semicircle. It explicitly treats the colored boundaries as features the correct result must display and excludes A/B/C/E for lacking them. That illustrates color-as-content use, but does not prove the intended area-fragmentation causal mechanism.')})

candidate_files = {p:v for p,v in before.items() if str(CAND.relative_to(ROOT)) in p}
source_files = {p:v for p,v in before.items() if p.startswith('PlaneGeometry') and ('Plane242' in p or 'workbench' in p or p.endswith('dataset.jsonl'))}
image_inspection = []
for p in (BRANCH/'originals/Plane242.jpg',BRANCH/'image/Plane242.png',CAND/'candidate.png'):
    with Image.open(p) as im: size = list(im.size)
    image_inspection.append({'absolute_path':str(p),'actual_image_tool_opened':True,'size_px':size,'sha256':fh(p)})

report = {
 'question_id':QID,'variant_id':VID,'decision':'reject','reviewed_at_utc':now(),
 'role':'Fresh independent second research reviewer; worked alone. No solver call, subagent, thread, worktree, approval, Pass, Collect, formal publication or evidence alteration.',
 'reason':'不推荐此冻结图。两次预设 D 命中、技术合法性、图形保真和局部信息针对性均成立；但在题目要求放置实体纸片并识别结果的语境下，彩色外缘存在合理的纸片自带印色/彩边解读。此解读中 E 丢失彩边，D 又不可能由完整灰色半圆得到，没有选项完整匹配。单纯宣称这些是标注不能消除图像与题干自身的语义歧义。',
 'original_unique_answer':'E','preset_wrong_answer':'D','two_complete_final_answers':finals,
 'requirement_disposition':{
    'independently_proved_unique_original_answer':'pass: E, with primary proof corrected below',
    'two_completed_predeclared_target_hits':'pass: D and D on the exact same frozen PNG/request',
    'actual_quicktest3_profile_and_no_prompt_leakage':'pass',
    'source_geometry_fill_text_view_and_path_preservation':'pass',
    'information_targeting':'pass for the proposed annotation-only mechanism',
    'concise_useful_visible_marks':'pass; all six have specific visible roles',
    'normal_size_geometric_readability':'pass',
    'human_unambiguous_semantics':'fail: exact physical paper/color counter-reading below',
    'current_authoritative_eligibility':'pass; research-only state remains unapproved'},
 'independent_unique_answer_proof':{
    'formal_question_full':formal['question'],'source_question_full':source['record']['question'],
    'method':'Read actual source JPEG, original formal PNG and candidate at native size; then verify frozen vector inventory, areas, convexity and an explicit feasible construction. The stored answer was used only for agreement checking.',
    'source_inventory':scene['objects'][:3],
    'interpretation':'Place the two shown intact rigid planar paper pieces on the disk without overlapping their interiors. Placement supplies no cutting, stretching or removal operation. The pictured choices show no paper extending beyond the disk. Black is the exposed background, not an extra paper piece.',
    'area_invariant':'Radius is 1 for both pieces and the background disk. Gray area is pi/2, white area pi/4; no-overlap leaves black area pi/4. Each paper remains fully visible, so neither color can lose area by occlusion.',
    'options':option_proof,
    'D_convexity_witness':{'coordinate_system':'Relative to D center (9,0)',
       'gray_interior_p':[0.6,0.2],'gray_interior_q':[-0.2,-0.6],
       'midpoint_in_black_interior':[0.2,-0.2],
       'proof':'Both endpoints have squared radius 0.4 and lie in the two gray quadrants. Their midpoint lies strictly in black quadrant IV. Every rigid image of the closed source half-disk is convex, so it cannot be D. Equivalently its interior is connected, while D gray has two interior components. No-overlap prevents the white piece from masking a connected gray half-disk into these regions.'},
    'center_point_qualification':'The two closed mathematical gray quarter sectors of D share the center point. Thus their union is connected as a closed set; a bare disconnected-closed-set argument is imprecise. The disconnected INTERIOR / nonconvexity argument above is decisive and does not depend on a center-pixel convention.',
    'E_explicit_rigid_placements':{
       'gray':'F_g(x)=(12,0)+R_125deg(x-(5,7)), mapping source angles 0..180 to 125..305.',
       'white':'F_w(x)=(12,0)+R_350deg(x-(7,7)), mapping source angles 0..90 to 350..440.',
       'no_overlap':'Angular interiors are disjoint modulo 360; black occupies two 45-degree gaps. Both papers are exactly their original size/shape.'},
    'correct_restricted_center_argument':'For a radius-1 SEMICIRCLE contained in a unit disk centered at O, its diameter endpoints P,Q satisfy 2=|P-Q|<=|P-O|+|Q-O|<=2. Equality forces P,Q to be antipodal disk points and their midpoint, the semicircle center, to equal O. This does not establish the same claim for a quarter. Separately, a piece whose nondegenerate circular boundary matches an actual option outer-circle arc must share its center, since distinct circles cannot share an open arc. The E construction already proves existence without any general quarter containment lemma.',
    'frozen_angle_precision_limit':'A 50/40-degree split and the other exact angles are the frozen formal reconstruction, not numerical givens measured from the JPEG. The actual source image independently shows the required qualitative size/shape distinctions. No high-precision pixel measurement is asserted.',
    'unique_original_answer':'E','agrees_with_formal_and_source_after_derivation':True},
 'primary_proof_corrections':[
    {'location':str(CAND/'design.json')+' : primary_math_proof',
     'incorrect_claim':'Any rigid placement of a radius1 sector inside the equal-radius disk has its circular arc centered at the disk center.',
     'counterexample':'Take Q={(x,y): x>=0, y>=0, x^2+y^2<=1} and translate it by (-1/4,-1/4). For r=sqrt(x^2+y^2), the translated squared distance from O is r^2-(x+y)/2+1/8 <= r^2-r/2+1/8 <= 5/8 < 1 for 0<=r<=1. This entire radius-1 quarter fits strictly inside the unit disk although its arc center is (-1/4,-1/4).',
     'correction':'Use the valid semicircle diameter-endpoint argument, actual boundary matching, area, D nonconvexity and the explicit E construction above. The original E answer survives.',
     'frozen_primary_file_changed':False},
    {'location':'Primary gray connectivity terminology',
     'qualification':'D closed gray sectors can touch at the center; its interior is disconnected and the set is nonconvex. Single point contact cannot make it a rigid half-disk.',
     'frozen_primary_file_changed':False}],
 'actual_image_inspection':{
    'images':image_inspection,'native_full_image_viewed':True,
    'original_and_candidate_geometry_findings':'The source gray paper is one uniformly gray semicircle with a continuous black diameter and no interior seam. Red changes to blue only at the top point of its curved perimeter. D visibly has gray upper-right and lower-left quarters, white upper-left and black lower-right. E remains one continuous gray half-disk and a white quarter. All A-E labels and gray/white/black distinctions are clear.',
    'radius_px':render['original_geometry_text_view']['native_radius_px'],
    'stroke_width_px':render['marker_geometry'][0]['stroke_width_px'],
    'pixel_comparison':render['pixel_comparison'],
    'what_is_and_is_not_proved':'Vector fills and their paths/transforms and all labels/views are unchanged. Widened colored outlines do change visible pixels near boundaries; 2492 changed pixels are confined to the six actual arc neighborhoods. These facts establish rendering preservation, not semantic exemption of ink.'},
 'per_marker':per_marker,
 'marker_group_assessments':{
    'red_pair':{'actions_zero_based':[0,2],'targeting':'True equal-radius 90-degree local-arc correspondence, rotation 0 degrees.',
       'validity':'Locally correct; insufficient for whole gray paper congruence. It cannot authorize moving half of an intact piece.',
       'conciseness':'Two short existing arc portions; each is a visible counterpart.',
       'human_unambiguity':'Combined paper-content ambiguity fails.'},
    'blue_pair':{'actions_zero_based':[1,3],'targeting':'True equal-radius 90-degree local-arc correspondence, rotation +90 degrees.',
       'validity':'Locally correct. Red and blue would require inconsistent rotations of the same source paper; that is the precise false fragmentation hypothesis.',
       'conciseness':'Two visible arc portions distinguish this second gray-part correspondence.',
       'human_unambiguity':'Combined paper-content ambiguity fails.'},
    'green_pair':{'actions_zero_based':[4,5],'targeting':'Actual full white-quarter match, rotation +90 degrees.',
       'validity':'A true whole-piece geometric match. This keeps D area-correct and isolates the gray integrity defect.',
       'conciseness':'One source and one result arc; useful second-piece check. It is not an empirical minimal-marker claim.',
       'human_unambiguity':'Colored edging itself can be read as part of the physical white paper; E has no corresponding green edging.'}},
 'human_semantics':{
    'decision':'fails for this exact frozen presentation',
    'annotation_only_reading':'If the colors are known to be external comparison annotations and excluded from paper content, a careful human can reject D and uniquely select E by the proof above.',
    'reasonable_material_color_reading':'The question asks what picture results when the two shown physical papers are placed on a black circle. Red and blue lie exactly on the boundary of the gray source paper, and green on the white source paper. They look like colored edging/ink attached to the shown pieces, with matching edging only in D. No text or visible separate annotation convention states that these particular moving-paper features vanish or may be discarded.',
    'explicit_incompatibility':[
       'The source red 0..90 arc and blue 90..180 arc share the same top endpoint and form one continuous semicircular outer arc. Any single rigid movement, including a planar reflection, preserves their endpoint incidence and adjacency.',
       'D red is 0..90 and blue is 180..270. These arcs are separated around the outer circle by a white quadrant and a black quadrant; they do not share an endpoint. Their closest endpoints are sqrt(2) radii apart. They cannot both be the moved edging of one intact source gray semicircle.',
       'E is the only possible uncolored arrangement, but E has no red, blue or green outer-edge ink. In this actual E arrangement both source curved edges lie on the outside of the disk and remain exposed; no overlap is available to hide them.',
       'A/B/C already fail the underlying paper geometry and also lack the edging. Thus the exact color-preserving reading has no matching choice, whereas the annotation-only reading has E.' ],
    'why_not_a_blanket_color_ban':'Authorized color styling is not automatically promoted to a new numerical or geometric given. The objection here comes from the task-specific physical transformation of the very objects carrying the colored boundaries and the explicit absence of a matching transformed picture. A purely relational geometry highlight need not have this problem.',
    'primary_semantics_claim_disposition':'The design statement that colors are annotations and not extra physical ink constraints is an author intention outside the actual question/PNG delivered to the solver. It does not resolve the competing reasonable human reading.',
    'no_new_cut_claim':'There is no new radius, interior cut, closed source subregion or extra gray paper in this new design. Color transitions at the existing arc midpoint do not draw a cut. That passes the Plane233-specific partition objection but does not settle the different paper-ink issue.',
    'basis':'Actual image and complete wording plus the explicit adjacency/color-preservation calculation; not the model narratives and not a numerical cap on marks.'},
 'old_objections_rechecked':[
    {'source':'Plane242 diameter_and_ordered_sector_rays primary rejection',
     'finding':'Old green B diameter half was occluded by the blue white radial edge and the 8-action draft was untested. The new six selected arcs each show actual exact-color pixels (112..119 each) with no invisible action. That old defect is resolved.'},
    {'source':'Plane242 semicircle_and_ordered_sector_rays prior B/E pair',
     'finding':'I read both old full raw responses and opened both old candidate images. Old preset B had B then E, only one hit. New preset D was separately written before calls; new marks select two source gray 90-degree outer arcs and D opposite quarters plus a true white 90-degree arc pair. It is a material change from the old whole-gray-half plus 90-versus-45 white ordered rays, not a palette/width rename or post-hoc preset change.'},
    {'source':'Plane233_two_U_partial_partition_binding actual independent report',
     'finding':'The old closed source contours could represent incompatible fixed partitions. Here all six selected portions are open outer arcs of existing piece boundaries. No new closed interior partition exists. Do not reject this image under the old fixed-partition reason.'},
    {'source':'Plane295_inner_ear_shoulder_correspondence actual independent report',
     'finding':'The shared relevant lesson is original-content versus comparison-annotation semantics, not a general color prohibition. Its tiny-ear readability objection is not reproduced here: the source and D arcs and gray/white sectors are clearly visible at native size.'},
    {'source':'Plane342_quarterturn_wedge_edge_binding actual independent report',
     'finding':'The analogous issue survives case-specific rechecking: the moving physical paper can reasonably carry its colored edging, yet no option preserves the full material picture. This is a new explicit paper-edge/adjacency calculation, not adoption of a prior verdict.'}],
 'two_hit_evidence':{
    'disposition':'pass','binding_checks':audit['checks'],
    'exact_frozen_binding':audit['binding'],'request_without_base64':audit['request_summary'],
    'run_checks':[r['checks'] for r in audit['runs']],
    'no_answer_or_intent_supplied':'The request body contains only the reference system instruction, exact formal question and one embedded candidate PNG. The design, preset D, correct answer E, plugin description/intent, proof and original control image are absent from the solver request.',
    'exact_count_and_retry_assessment':'One invocation for this exact candidate contains exactly two starts, two HTTP-200 completed records and two full stop responses. The same request/image/design hashes appear in both. The unchanged harness loop and run24 process records contain no automatic retry; no partial/error artifact or alternative same-image binding was found. Older B/E runs are for a different frozen image and are disclosed separately, not selected into this pair.',
    'same_question_binding_inventory':audit['same_question_binding_inventory'],
    'evidence_limit':'This is a local immutable-evidence audit, not access to a provider-side exhaustive invocation ledger. No unsupported claim about all possible external activity is made.'},
 'controls_and_effect_limits':{
    'existing_original_control_bindings_found':audit['original_controls_found'],'new_solver_calls':0,
    'original_control_status':'No original Plane242 control invocation was found in the runtime binding scan or prior history. The old B/E pair used an annotated different candidate, not an original control.',
    'limits':'Two observed D finals do not establish causal gain, statistical reliability, identical reasoning or per-marker contribution. Those were not required as hard gates. Narrative geometry/area errors do not cancel unambiguous D final hits, but they prevent asserting a demonstrated area-fragmentation mechanism.'},
 'current_authoritative_eligibility':audit['eligibility'],
 'exact_frozen_hashes':{'candidate_and_all_its_evidence':candidate_files,
    'source_and_implementation':source_files,
    'question_record_sha256':audit['binding']['question_record_sha256'],
    'original_current_approval_content_sha256':audit['eligibility']['computed_current_content_sha256'],
    'original_pixel_sha256':render['formal_pixel_sha256'],'candidate_pixel_sha256':render['candidate_pixel_sha256'],
    'native_path_hashes':[{'action_index':m['action_index'],'target':m['action']['target'],
        'path_id':m['action']['interval']['path_id'],'sha256':m['actual_path_sha256']} for m in per_marker]},
 'timestamp_binding':{
    'source_formal_question_approved_at_utc':audit['eligibility']['approval']['approved_at_utc'],
    'design_difference_created_at_utc':read(CAND/'design_difference_audit.json')['created_before_calls'],
    'preset_design_created_at_utc':design['created_at'],'binding_created_at_utc':audit['binding']['created_at'],
    'run_intervals_utc':[[r['record']['started_at'],r['record']['finished_at']] for r in audit['runs']],
    'file_metadata':'Exact mtime/ctime/byte hashes of source image, question dataset, preset/design/plugin, request, snapshot and both raw responses are included in exact_frozen_hashes and evidence_audit.json.',
    'limit':'Stored UTC timestamps and file metadata establish internal chronology consistent with preset-before-call binding; they are not an independent trusted timestamp service.'},
 'preservation':{'fresh_native_renderer_checks':render['checks'],
    'historical_relevant_source_comparisons':audit['historical_relevant_source_comparisons'],
    'tracked_preexisting_file_count':len(before),'tracked_preexisting_hash_changes':drift,
    'all_prior_evidence_and_original_inputs_read_only':True,
    'no_entire_shared_workspace_unchanged_claim':True,
    'unrelated_concurrent_workbench_edits':'Preserved. No restoration, author attribution, aggregate rebuild, .runtime change, .env read/write, .git modification, formal approval write, Pass/Collect or publication was performed.',
    'mutable_runtime_progress_policy':'Historical remaining_questions/exploration_report snapshots are diagnostic metadata; no attempt was made to restore them or treat their possible drift as source geometry corruption.',
    'three_dimensional_geometry_projection_visibility':'Not applicable to this planar sector diagram. Frozen 2D data/view and native solid boundaries are preserved; no visibility override was introduced.'},
 'concrete_objections':[
    {'severity':'blocking','code':'PHYSICAL_PAPER_EDGE_INK_VS_EXTERNAL_ANNOTATION',
     'finding':'Reasonable material-color reading has no valid choice; annotation-only reading uniquely gives E. This exact presentation therefore fails requested human unambiguity despite legal, targeted, readable marks and D/D observations.'},
    {'severity':'corrected_primary_proof_error','code':'FALSE_GENERAL_SECTOR_CONTAINMENT_LEMMA',
     'finding':'The broad equal-radius-sector containment claim is false for a quarter. Counterexample and correct independent unique-E proof are supplied; original frozen files are preserved.'},
    {'severity':'precision_qualification','code':'D_CENTER_SINGLE_POINT_CONTACT',
     'finding':'Use nonconvexity/disconnected gray interior rather than claiming the union of closed gray quarters is disconnected.'}],
 'limitations':[
    'This is an independent research judgment, not formal-original approval or user Pass/No Pass/Collect.',
    'No human population study or readability estimate is claimed. The explicit competing interpretation suffices for the requested semantic review.',
    'No new correct original controls, new solver calls, retries, hypothesis edits, causal-gain requirement, identical-narrative requirement or numerical marker cap was added.',
    'Reject applies to this exact frozen candidate. No repair, relaxation of the human ambiguity requirement or alternative design was made.',
    'All supporting file hashes and preservation conclusions are scoped to the tracked sources/evidence; concurrent unrelated workspace changes are not attributed to this reviewer.'],
 'workspace_and_process_discipline':{'fresh_assigned_output_directory':str(HERE),
    'strict_own_directory_write_guard_installed_before_project_imports':True,
    'shared_runtime_isolation':ISOLATION,'TEMP_TMP_TMPDIR_and_caches_inside_assigned_directory':True,
    'network_and_child_process_execution_blocked_in_review_python':True,
    'all_captured_scenes_closed':render['all_captured_scenes_closed'],
    'foreground_python_pids':[audit['pid'],render['pid'],os.getpid()],
    'own_background_processes_started':0,
    'process_status':'All review commands are foreground; inspection and rendering commands exited successfully. The report writer exits on completion, followed by an external read-only process check. No server or background helper was started.'},
 'supporting_new_review_files':{name:{'absolute_path':str(HERE/name),'sha256':fh(HERE/name)}
       for name in ('evidence_audit.json','native_render_audit.json','preservation_after.json',
                    'independent_noop.png','independent_reproduced.png','review_env.py','inspect_evidence.py','render_audit.py')},
 'approval_status':'RESEARCH_REJECT_RECOMMENDATION_ONLY; no approval/Pass/Collect/publication action performed'
}
write('independent_review.json',report)
print(json.dumps({'decision':report['decision'],'original_unique_answer':'E','preset_wrong_answer':'D',
                  'manual_final_answers':['D','D'],'report':str(HERE/'independent_review.json'),
                  'report_sha256':fh(HERE/'independent_review.json'),'tracked_files':len(before),
                  'preexisting_file_hash_changes':len(drift),'own_process_ids':report['workspace_and_process_discipline']['foreground_python_pids']},ensure_ascii=False))
