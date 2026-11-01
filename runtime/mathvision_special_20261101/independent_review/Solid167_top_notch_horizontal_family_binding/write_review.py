"""Compile the independent review without modifying any historical evidence."""
from pathlib import Path
import os,sys,json,hashlib,math
from datetime import datetime,timezone
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
SESSION=ROOT/'runtime/mathvision_special_20261101'
SOURCE=SESSION/'background_07/solid_worker/Solid167'
CAND=SOURCE/'top_notch_horizontal_family_binding'
EVID=CAND/'tests/quicktest3_20261101T150754_53f9ec4b468e'
for key,sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():os.environ[key]=str(HERE/sub)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
def check_write(path):
    if path is not None and not isinstance(path,int) and not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):raise PermissionError(str(path))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check_write(args[0]);check_write(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(SESSION))
from runtime_isolation import install
install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT))
from dataset_tools.catalog import content,digest
from PIL import Image
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rel(path):return str(Path(path).relative_to(ROOT)).replace('\\','/')
def rows(path):return [json.loads(v) for v in Path(path).read_text(encoding='utf-8-sig').splitlines() if v.strip()] if Path(path).exists() else []
audit=read(HERE/'audit_results.json')
extra=read(HERE/'supplement_results.json')
design=read(CAND/'design.json')
plugin=read(CAND/'plugin.json')
binding=read(EVID/'binding.json')
ctx=read(CAND/'context.json')

# Locate every small raster residual against the unchanged source outline.
matrix=ctx['canvas']['data_to_pixel']
def pixel(pt):return [sum(matrix[k][j]*[pt[0],pt[1],1][j] for j in range(3)) for k in range(2)]
segments=[[pixel(v) for v in pair] for pair in audit['fresh_marker_paths']['line14'][0]['controls']]
def distance(pt,segment):
    a,b=segment;v=[b[i]-a[i] for i in (0,1)];den=sum(x*x for x in v)
    t=max(0,min(1,sum((pt[i]-a[i])*v[i] for i in (0,1))/den))
    return math.hypot(*[pt[i]-a[i]-t*v[i] for i in (0,1)])
with Image.open(CAND/'candidate.png') as im:candidate=im.convert('RGBA')
with Image.open(ROOT/'SolidGeometry/image/Solid167.png') as im:formal=im.convert('RGBA')
small_pixel_details=[]
for comp in extra['small_raster_components']:
    x0,y0,x1,y1=comp['bbox_inclusive']
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            old,new=formal.getpixel((x,y)),candidate.getpixel((x,y))
            if old!=new:small_pixel_details.append({'pixel':[x,y],'formal_RGBA':old,'candidate_RGBA':new,'distance_to_original_line14_px':min(distance((x+.5,y+.5),s) for s in segments)})
assert len(small_pixel_details)==17
assert max(p['distance_to_original_line14_px'] for p in small_pixel_details)<2
assert all(len(set(p['candidate_RGBA'][:3]))==len(set(p['formal_RGBA'][:3]))==1 for p in small_pixel_details)

nonblocking={'record_snapshot_file_sha','exactly_six_local_pixel_change_components'}
assert set(audit['failed_checks'])==nonblocking
assert all(v for k,v in extra['extra_checks'].items() if k!='small_differences_only_at_most_one_gray_level')
current_hashes={p:sha(ROOT/p) for p in audit['evidence_files']}
existing_mismatches=[p for p,h in current_hashes.items() if h!=audit['evidence_files'][p]['sha256']]
assert not existing_mismatches,existing_mismatches
helper_mismatches=[p for p,h in extra['helper_sha256'].items() if sha(ROOT/p)!=h]
assert not helper_mismatches,helper_mismatches
record=next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid167')
approval=read(ROOT/'provenance/approvals.json')['approvals']['Solid167']
accepted=[r for r in rows(ROOT/'SolidGeometry/special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))=='Solid167']
collected=[r for r in rows(ROOT/'SolidGeometry/special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))=='Solid167']
assert record['source_dataset']=='MathVision' and approval['reviewer']=='user' and approval['instruction'] and approval['content_sha256']==digest(content(ROOT,'SolidGeometry',record))
assert not accepted and not collected and not (ROOT/'SolidGeometry/special_variant/Solid167').exists()

marker_notes=[
    ('Left folded notch, original sides p18-p19-p20', 'Identifies the actual left-fold triangle as the red family. Its own-fold reflection produces a horizontal rhombus; the other fold duplicates that family at top/bottom.', 'Without this source mark the two red output contours have no explicit source-family anchor. This is a correspondence role, not a claim that a correct human solution requires coloring.', 'The 0.7..0.9 interval selects exactly existing polyline segments 7 and 8 of ten; it adds no triangle base, chord or closed source contour.'),
    ('Upper folded notch, original sides p14-p15-p16', 'Separates the perpendicular top-fold triangle as blue. It should produce vertical rhombi on left/right, exposing the precise orientation error made salient in D.', 'Necessary to express the second, different cut family rather than making all four D holes a single undifferentiated highlight.', 'The 0.3..0.5 interval selects exactly existing segments 3 and 4; the V remains open to the original top fold edge.'),
    ('D top existing horizontal rhombic hole', 'First target of the true red left-notch family: the correct local horizontal shape and top position provide a plausible partial correspondence.', 'Supplies the upper reflection mate in the red family, not a mark on the answer label or option frame.', 'Only the pre-existing closed cut boundary line42 is restyled; its white interior, four vertices, size and position remain fixed.'),
    ('D bottom existing horizontal rhombic hole', 'Second target of the red family, completing top/bottom reflection symmetry.', 'Carries the distinct lower mate. Omitting it would show an incomplete two-fold output mapping.', 'Only existing line45 is restyled; no extra hole, filled region, connection or partition appears.'),
    ('D left existing horizontal rhombic hole', 'First blue target; its location corresponds to the top-cut family but its long axis is horizontal rather than the required vertical direction. This is the specific false orientation correspondence.', 'Supplies one member of the misleading perpendicular family, tied to the actual blue source notch.', 'Only existing line43 is restyled. Its wrong geometry was already present in D; coloring adds no geometric given.'),
    ('D right existing horizontal rhombic hole', 'Second blue target, completing the left/right reflection pair with the same incorrect horizontal long axis.', 'Supplies the other family member and completes the finite source-to-four-hole mapping.', 'Only existing line44 is restyled; original white hole and gray paper survive.')
]
markers=[]
for i,(feature,role,necessity,legality) in enumerate(marker_notes):
    action=plugin['params']['actions'][i]
    markers.append({'action_index':i,'exact_action':action,'feature_independently_identified':feature,'informational_role':role,'design_necessity':necessity,'legality_and_semantics':legality,'normal_size_clarity':'Clearly distinguishable red/blue stroke at native 768x768; 2 pt is in the allowed whitelist. The four D holes remain horizontal closed rhombi with visible white centres.','legal':True})

protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
finals=[
    {'run_index':1,'final_letter':'D','exact_final_text':'Therefore, the correct diagram is D.\n\n**Answer:** D','preset_match':True,'wrong_against_independent_solution':True,'contradictory_final_letter_or_value':False,'complete_raw_response_and_run_record_read':True,'narrative_objections':['Says the result must show two diamonds; actual choices A/C/D each contain four holes and E five.','Describes C as two black diamonds, E as four, and D as one red plus one blue. These are incorrect counts.','Reverses D red/blue locations in its conclusion: actual red is top/bottom and blue left/right.','Explicitly treats color preservation as a given and selects D on that basis. Colors are added annotation appearance, not new mathematics.'],'full_response':audit['runs'][0]['full_raw_message']},
    {'run_index':2,'final_letter':'D','exact_final_text':'Therefore, Diagram D correctly shows the unfolded paper.','preset_match':True,'wrong_against_independent_solution':True,'contradictory_final_letter_or_value':False,'complete_raw_response_and_run_record_read':True,'narrative_objections':['Misstates inward V directions as left/up and claims the unfolded shapes are triangles.','Confuses the two cut families and gives inconsistent quadrant/centre-cross positions.','Rejects C because its holes are rhombi and incorrectly calls the D holes triangles. Actual D contains four horizontal rhombi.','The final sentence is an unambiguous D selection; these earlier shape descriptions are reasoning errors, not a competing final option or a numeric value paired with D.'],'full_response':audit['runs'][1]['full_raw_message']}
]
evidence_keys=['candidate.png','plugin.json','design.json','context.json','marker_path_bindings.json','render_check.json','primary_review.json','primary_post_test_review.json','manual_final_review.json']
key_files={rel(CAND/name):audit['evidence_files'][rel(CAND/name)] for name in evidence_keys}
key_files.update({p:v for p,v in audit['evidence_files'].items() if p.startswith(rel(EVID)+'/')})
key_files.update({rel(SOURCE/name):audit['evidence_files'][rel(SOURCE/name)] for name in ['formal_record.json','frozen_inputs.json','source_audit.json','source_scene_snapshot.json','fold_math_audit.json','original.png']})
report={
    'decision':'recommended',
    'question_id':'Solid167','branch':'SolidGeometry','variant_id':'top_notch_horizontal_family_binding',
    'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
    'review_type':'New independent second review; reviewer worked alone with no parent task history, subagents, delegates, threads or worktrees.',
    'recommendation_reasons':['Original mathematical answer independently proved uniquely C from actual fold/cut geometry and all five original options.','All six legal style actions have specific notch-family or reflection-mate roles and preserve readable original geometry and human semantics.','Two complete quicktest3 raw responses independently verified as D/D against predeclared D, using the same frozen PNG and no extra solver input or calls.','Exact replay, frozen dependencies, record approval and current authoritative MathVision/noPass/notCollected/noSpecialCompletion checks passed.'],
    'approval_or_publication':False,
    'scope':{'candidate_directory':str(CAND),'evidence_directory':str(EVID),'assigned_new_review_directory':str(HERE),'brief_read_in_full':str(SESSION/'Solid167_unit07_independent_review_brief.txt'),'protocols_read_in_full':{p:sha(ROOT/p) for p in protocols},'write_restriction':'Only assigned NEW independent_review directory. All Python analysis set TEMP/TMP/caches there, installed shared runtime_isolation before project imports, and additionally installed a stricter audit write guard for this directory.','no_forbidden_actions':['No existing evidence/helper/formal file modifications','No .env, .runtime or .git changes','No review API, Pass, Collect or publication','No solver calls, original controls or API retries','No unrelated workspace restoration or process termination']},
    'independent_unique_answer_proof':{
        'answer':'C','source_of_solution':'Formal question, actual source JPG, actual formal PNG and candidate PNG; independent unfolding and direct frozen-coordinate verification. Stored answer and primary proof were cross-checks, not the justification.',
        'diagram_interpretation':'The diagram labels the left edge as first fold and upper edge as second fold. They are orthogonal folds. Each triangular notch lies on one fold away from the intersection and away from the other fold. Source is a schematic partly opened four-layer stack, not a new cut partition.',
        'symbolic_proof':[
            'Put the fold intersection at (0,0). Let b>0 be half a notch base, h=sqrt(3)*b its equilateral altitude, and a,c>h be the distances of the two notch centres from the intersection. The shown quarter lies at x>=0,y<=0.',
            'The top notch vertices are (a-b,0),(a,-h),(a+b,0). Reflecting in y=0 gives the rhombus (a-b,0),(a,-h),(a+b,0),(a,h); its vertical diagonal is 2h and horizontal diagonal 2b. Since h/b=sqrt(3), it is vertically elongated. Reflect in x=0 to obtain its distinct left/right mate.',
            'The left notch vertices are (0,-c-b),(h,-c),(0,-c+b). Reflecting in x=0 gives the rhombus (0,-c-b),(h,-c),(0,-c+b),(-h,-c); its horizontal diagonal is 2h and vertical diagonal 2b. Reflect in y=0 to obtain its distinct top/bottom mate.',
            'Thus the unfolded paper has exactly four separate holes: two horizontal rhombi at top/bottom and two vertical rhombi at left/right. Both cut families stay away from the fold intersection, so no central fifth hole can occur. Equilateral half-triangles yield 60/120 degree rhombi, not right-angled squares.'
        ],
        'numeric_cross_check':{'flat_fold_axes':{'x':4.05,'y':7.15},'b':0.1785,'h':0.309171069151045,'a_and_c':1.05,'all_three_sides_of_each_triangle':0.357,'families':audit['independent_math_calculation'],'projection_correspondence':extra['notch_projection_correspondence'],'note':'The unfolded coordinates are flat material geometry. The colored visible notch is on the lifted packet; its projected slopes are not used to infer a false equilateral shape in screen coordinates.'},
        'choice_elimination':{'A':'Four vertical rhombi. Top/bottom long axes are incorrect for the left-fold notch.','B':'Four right-angled squares, incompatible with reflected equilateral triangles.','C':'Exactly the required two horizontal top/bottom and two vertical left/right rhombi.','D':'Four horizontal rhombi. Left/right long axes are incorrect for the top-fold notch.','E':'C-like outer four holes plus an unsupported central fifth hole.'},
        'matches_formal_answer_after_independent_proof':record['answer']=='C'
    },
    'actual_image_visual_and_human_semantics':{
        'actually_viewed':['SolidGeometry/originals/Solid167.jpg','SolidGeometry/image/Solid167.png',rel(CAND/'candidate.png')],
        'native_size_inspected':'768x768 at original detail, with the complete five-option row and fold labels visible; source JPG also inspected directly.',
        'normal_size_finding':'Satisfactory. Original holes are small, but vertical/horizontal long axes are distinguishable without zoom: about 9.0x15.6 versus 15.6x9.0 pixel centreline bounds; squares are about 9.34x9.34. The 2 pt D contours occupy about 19x13 outer pixel boxes yet retain white centres and two visible pointed ends. A/C/E have their exact original pixels.',
        'counts_fills_and_extents':extra['option_fill_hole_and_native_size_checks'],
        'source_notch_clarity':'The red left notch and blue top notch each remain an inward open V on the original packet boundary. Fold names, dashed fold guides, paper layer outlines and notch positions remain clear; no new base closes either V.',
        'source_human_semantics':'Color and allowed thickness emphasize existing edges only. The source packet still depicts the same two triangular cut-outs. No line crosses the paper face, adds an internal piece, joins separated contours, bridges a hole, or creates an incompatible fixed partition.',
        'output_human_semantics':'All four colored D contours were existing closed hole boundaries. They remain white holes in gray paper; neither a new closed region nor a new cut is introduced. All original option labels, frames and hole inventories remain. The colors invite family correspondence but introduce no extra equation, equality, fold instruction or geometric premise.',
        'information_targeting':'D becomes salient through two explicit source notch families and their four output hole targets. No option letter, rectangle frame, arbitrary isolated mark, or unconnected decoration is highlighted. The false blue long-axis correspondence is the mathematical locus of the trap.',
        'geometry_3D_projection_visibility_text_fill_preservation':'Fresh context objects, snap points, canvas transforms and view match the frozen context exactly. All frozen input hashes match; independent no-op matches formal pixels. Appearance changes report world_geometry_changed=false, projection_changed=false, frozen_visibility_intervals_changed=false and no line-style overrides. Plugin contains only six set_object_style actions; no text/fill/coordinate/visibility operations.',
        'raster_residuals':{'total_changed_pixels':961,'substantive_components':6,'extra_tiny_components':12,'extra_tiny_pixels':17,'classification':'Fourteen pixels change by 1 gray level; three pixels at an original lower corner change by up to 11 levels, consistent with cap/join rasterization when the unchanged source polyline is split for partial styling. All are grayscale and within 2 pixels of the same original line14 path. They form no visible new mark, cut or partition. Byte-identical candidate replay reproduces them.','exact_small_pixels':small_pixel_details,'raw_components':audit['pixel_difference']['components']},
        'human_performance_claim':False
    },
    'per_marker_necessity_legality_and_clarity':markers,
    'marker_count_assessment':'Six actions, each with a distinct family-anchor or reflection-mate role. Necessity is assessed for this concise intended correspondence design; no numeric mark cap or empirical per-marker indispensability is imposed.',
    'full_final_and_quicktest_evidence_verification':{
        'predeclared_wrong_answer':'D','independent_correct_answer':'C','observed_complete_final_letters':['D','D'],'observed_two_hit':True,
        'profile':'quicktest3','model':'mimo-v2.6-flash','thinking':{'type':'disabled'},'reasoning_tokens':[0,0],'request_top_level_fields':['model','stream','thinking','messages'],
        'request_content_verified':audit['request_without_base64'],
        'same_frozen_png_verification':'Base64 decoded directly from raw request.json equals candidate.png byte for byte. Both start records and completed run records bind the identical image, request and design hashes; both raw responses match their run records in full. Both have HTTP 200, finish_reason=stop, status=completed and truncated=false.',
        'predeclaration_timing':{'design_created_at':design['created_at'],'candidate_modified_utc':audit['evidence_files'][rel(CAND/'candidate.png')]['modified_utc'],'design_modified_utc':audit['evidence_files'][rel(CAND/'design.json')]['modified_utc'],'binding_created_at':binding['created_at'],'run_01_started_at':audit['runs'][0]['run']['started_at'],'run_01_finished_at':audit['runs'][0]['run']['finished_at'],'run_02_started_at':audit['runs'][1]['run']['started_at'],'run_02_finished_at':audit['runs'][1]['run']['finished_at'],'provider_created_utc':[r['provider_created_utc'] for r in audit['runs']]},
        'manually_read_finals_and_objections':finals,
        'run_records':[r['run'] for r in audit['runs']],
        'no_retry_or_selection_finding':'This D candidate has one evidence invocation, exactly two starts, two complete records and two corresponding original provider responses. Harness and worker driver inspected: fixed two-run loop with one direct request per iteration; errors stop without retries. Both calls count, not a selected subset. No new calls performed during review.',
        'previous_design_history_disclosed':{'variant_id':'orthogonal_notch_family_binding','preset':'A','observed_finals':['A','D'],'two_hit':False,'candidate_sha256':'d7f611c607d121560e718107da96644a41b69579a6709d8312d178b567b1d45f','this_candidate_is_distinct':'Current D PNG hash differs; old design colored four vertical A holes, current design colors four horizontal D holes. Current D preset and full design snapshot predate its own pair and match byte for byte. Prior history is preserved and is not counted toward this pair.','adaptive_design_limit':'The new design was made after the earlier A/D pair. This is exploratory design history, not a preregistered experiment across all designs; no broader absence-of-selection or population success-rate claim is made.'},
        'interpretation_limit':'D/D proves two observed wrong final selections against this image and preset. It does not establish coherent reasoning, identical narratives, causal gain over the original, stable error probability or per-marker causal necessity.'
    },
    'exact_hashes_and_bindings':{
        'candidate_png_sha256':binding['image_sha256'],'candidate_RGBA_pixel_sha256':binding['pixel_sha256'],'plugin_file_sha256':sha(CAND/'plugin.json'),'design_file_and_snapshot_sha256':binding['design_sha256'],'request_body_sha256':binding['request_body_sha256'],'formal_record_canonical_sha256':digest(record),'formal_record_snapshot_raw_file_sha256':sha(SOURCE/'formal_record.json'),'approval_content_sha256':approval['content_sha256'],
        'key_evidence_files':key_files,'all_frozen_input_files':audit['frozen_input_verification'],'all_audited_existing_files':audit['evidence_files'],'helpers':extra['helper_sha256'],'fresh_exact_marker_path_bindings':audit['fresh_marker_paths'],
        'source_question_and_original_bindings':'Formal record parsed equality, canonical record hash, dataset byte hash, formal PNG, source JPG, frozen scene, script and all dependencies match current files and historical binding. Source JPG is c99264565d19fd19d1b853b5ac5717136f4ba41c389e411ef520b7d7c0672931; formal PNG is 5ab154fbce85a719dc94cba4265ccdfc27c249eff046c869b4ad090c1eaeac2a.',
        'nonblocking_factual_mismatch':{'file':rel(SOURCE/'source_audit.json'),'field':'formal_record_sha256','recorded_value':'e5ff1368ff41aa0ebcc6e8e4b738af96609cfc8b9688399a9ca584acb2464339','actual_snapshot_raw_bytes_sha256':sha(SOURCE/'formal_record.json'),'classification':'Historical field name is inaccurate: recorded value is the canonical JSON RECORD hash, not the pretty-printed snapshot FILE hash. Parsed snapshot equals current formal row; binding.question_record_sha256 correctly uses canonical semantics. No math/image/request mismatch. Existing file left unchanged.'}
    },
    'independent_render_verification':audit['replay'],
    'current_authoritative_eligibility':{**audit['eligibility'],'checked_again_at_utc':datetime.now(timezone.utc).isoformat(),'eligible':True,'accepted_entries':accepted,'collected_entries':collected,'special_completion_finding':'No Solid167 special_variant directory, recipes.json or collection.json exists and no accepted/collected index entry exists. Therefore no current Pass, Collect or special completion record.','current_record_canonical_sha256':digest(record),'current_approval_content_sha256':digest(content(ROOT,'SolidGeometry',record))},
    'concurrent_changes_and_runtime_metadata':{'historical_unit07_findings':audit['diagnostic_runtime_progress']['unit07_preservation'],'handling':'Preserved concurrent unrelated Author-designed Plane492..503/workbench, aggregate question_bank and .runtime/plane_special changes. Did not restore, edit or attribute them. Hash scans alone do not identify authors. No whole-workspace-unchanged claim is made.','runtime_progress':audit['diagnostic_runtime_progress'],'progress_interpretation':'remaining_questions/exploration_report are mutable diagnostics, not frozen geometry or exact evidence. Their review-time hashes happen to equal historical values here; later drift does not by itself corrupt the approved question, candidate PNG or raw evidence. Original historical snapshots are untouched.'},
    'objections':{'blocking':[],'nonblocking':['Historical source_audit formal_record_sha256 is a canonical-record fingerprint mislabeled as a snapshot-file hash; both values independently recorded above.','Partial-style replay has 17 tiny grayscale raster residuals on the original uncolored outline, in addition to the six intended mark components; quantified above.','Both model narratives contain major errors; the recommendation is for observed final D/D evidence, not their reasoning.']},
    'limitations':['No original-control solver calls. No causal gain relative to an unannotated original is established or required.','No human study. Native-size human readability is this reviewer\'s actual-image assessment, not measured human accuracy.','Two observed calls only; no statistical success rate, robustness or generalization claim.','No per-marker ablation or statistical causal necessity. Each marker has an inspected design role.','The two narratives differ and are mathematically unreliable; this does not replace independent proof of C or alter their explicit final D selections.','Prior failed A design is preserved; this D design is exploratory rather than a preregistered experiment across designs.','Local bindings, source code and timestamps strongly corroborate the saved two-call history, but are not cryptographically signed provider attestations and cannot prove absence of unsaved activity.','Any future packaging/publication requires its own exact packaged replay; none is performed or authorized by this recommendation.'],
    'review_completion':{'all_requested_requirements_satisfied':True,'new_solver_calls':0,'subagents_or_delegates':0,'existing_files_changed_by_review':False,'tracked_existing_files_unchanged_through_final_report':not existing_mismatches and not helper_mismatches,'no_live_process_check':read(HERE/'no_live_processes.json'),'process_lifecycle':'All review computations ran as awaited foreground commands; no servers or background helpers were started. The script producing this report exits immediately after writing it.','supporting_artifacts':{name:sha(HERE/name) for name in ['audit_results.json','supplement_results.json','audit.py','supplement.py','replayed_candidate.png','no_live_processes.json']},'resolved_raw_diagnostic_assumptions':{'record_snapshot_file_sha':'Resolved as canonical versus serialized hash naming mismatch; no evidence tampering.','exactly_six_local_pixel_change_components':'Raw binary pixel diff has 18 components, of which exactly six are substantive colored marks and twelve comprise 17 grayscale antialias residual pixels on the original outline.','small_differences_only_at_most_one_gray_level':'Overly strict exploratory assumption; 14 pixels change by 1 level and 3 by up to 11, all on the original source corner/edge.'}}
}
with (HERE/'independent_review.json').open('x',encoding='utf-8') as stream:
    json.dump(report,stream,ensure_ascii=False,indent=2,allow_nan=False);stream.write('\n')
print(json.dumps({'decision':report['decision'],'report':str(HERE/'independent_review.json'),'report_sha256':sha(HERE/'independent_review.json'),'report_bytes':(HERE/'independent_review.json').stat().st_size,'existing_mismatches':existing_mismatches,'maximum_small_residual_distance_from_original_edge_px':max(p['distance_to_original_line14_px'] for p in small_pixel_details)},ensure_ascii=False))
