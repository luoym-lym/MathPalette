from review_bootstrap import *
import json, hashlib
from datetime import datetime, timezone
from dataset_tools import catalog

def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,v): (OWN/name).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
e=read(OWN/'evidence_audit.json'); n=read(OWN/'native_render_audit.json'); h=read(OWN/'controls_and_history_audit.json')
baseline=read(OWN/'read_only_baseline_manifest.json')
changes=[{'path':p,'before':v['sha256'],'after':sha(ROOT/p) if (ROOT/p).exists() else None}
    for p,v in baseline.items() if not (ROOT/p).exists() or sha(ROOT/p)!=v['sha256']]
assert not changes, changes
assert all(e['checks'].values()) and all(n['checks'].values())
assert all(all(r['checks'].values()) for r in e['runs'])
record=next(json.loads(line) for line in (ROOT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip() and json.loads(line).get('id')=='Plane192')
ap=read(ROOT/'provenance/approvals.json')['approvals']['Plane192']
current=catalog.digest(catalog.content(ROOT,'PlaneGeometry',record))
def matching_index(name):
    return [json.loads(s) for s in (ROOT/'PlaneGeometry/special_variant'/name).read_text(encoding='utf-8-sig').splitlines()
            if s.strip() and json.loads(s).get('question_id',json.loads(s).get('id'))=='Plane192']
assert current==ap['content_sha256']==e['eligibility']['current_content_sha256']
assert record==e['formal_record'] and not matching_index('accepted_index.jsonl') and not matching_index('collected_index.jsonl')
assert not (ROOT/'PlaneGeometry/special_variant/Plane192').exists()
roles=[
    {'route':'A','target':'route0_0','unit_diagonals':4,
     'targeting':'首个最长上升直线段 (1,1)→(5,5)，将跨四个单位对角线的整段作为一个视觉对象；它是把对象数量误当距离时的长段参照。没有把 A 的下降段也染红。',
     'functional_effectiveness':'确实完整选中一个 maximal run，且网格交点仍显示它实际包含四个单位。与 B/C/D 同角色配对，支持“一个整段算一个单位”的具体错误映射。单独因果贡献未测。',
     'conciseness':'一条完整已有线段即表达此角色，无额外框、文字、点或整条 A 着色；2 pt 使类别标识可见。',
     'human_judgment':'4 格水平跨度和 4 格升高可直接追踪；峰顶之后的黑色下降段连续可见。相同颜色不赋予它和短红段等长条件。'},
    {'route':'B','target':'route1_0','unit_diagonals':3,
     'targeting':'首个上升直线段 (13,1)→(16,4)，提供与 A 同角色但实际只有三个单位的比较对象；B 其余 1、1、3 单位段保留黑色。',
     'functional_effectiveness':'选中三单位的整段，暴露同为一个 maximal run 却并非相同度量单位；B 还是长短不等的四段路线，不能靠把每段一律当一个单位正确计长。单独因果贡献未测。',
     'conciseness':'只标首段，没有把 B 整体变蓝/虚线，也没有为了强调 A 而降低竞争路线可见性。',
     'human_judgment':'首峰、随后的一格下上小凹口、右侧下降段及端点清楚；不会把 B 错分成新增路线或把凹口填平。'},
    {'route':'C','target':'route2_0','unit_diagonals':2,
     'targeting':'首个上升直线段 (25,1)→(27,3)，是两个单位的中间尺度参照；C 的四个整段都长 2sqrt(2)。',
     'functional_effectiveness':'把二单位整段与 A 的四单位、B 的三单位、D 的一单位置于相同类别；C 与 B 的整段数量同为四，但组成不同，具体展示段数和单位累计数是不同概念。单独因果贡献未测。',
     'conciseness':'一处对应标记即可涵盖 C，无需标它的四段或加新关系符号。',
     'human_judgment':'两格升降、中央谷底和第二峰仍清楚；红黑相接只发生在原有顶点，不建立新切割。'},
    {'route':'D','target':'route3_0','unit_diagonals':1,
     'targeting':'首个上升直线段 (37,1)→(38,2)，是实际单个单位对角线，作为其他较长红段被错误单位化时的一单位参照。',
     'functional_effectiveness':'标记恰好覆盖一个真实单位对角线；它和前三个红段共享“一个 maximal run”而非“相同长度”。D 的八个单位段全部仍可计数。单独因果贡献未测。',
     'conciseness':'只标八段中的首段，避免旧版整条 D 加粗着色；最短红段也具有明确校准作用。',
     'human_judgment':'原生长度约 20.03 px，名义线宽约 2.78 px，首端点后的红色斜段仍可辨认；后续七段黑线和末端点可见，不是红点或断路。'}
]
for i,v in enumerate(roles):
    v.update({'index':i,'legality':'pass: set_object_style on exact existing object; #DC2626 and 2 pt are permitted; no linestyle or interval override.',
        'original_solid_linestyle_preserved':True,'native_evidence':n['per_marker_native_evidence'][i],
        'frozen_path':read(BASE/'background_23/Plane192/r23_maximal_run_unit_binding/path_fingerprints.json')[v['target']],
        'new_points_lines_text_fills_equality_ticks_or_regions':False,
        'human_readable_and_unambiguous':True,
        'empirical_per_marker_effect':'not established; two-hit evidence concerns the combined frozen image'})

old_dispositions=[
    {'prior':'plane_explore/Plane192/v01','prior_preset':'D','prior_full_finals_manually_read':['A','D'],
     'finding':'旧图整条 D 红色 2 pt；两次没有都命中 D。新图四路首段均红，不复用旧图或其测试结果。'},
    {'prior':'plane_explore/Plane192/v02','prior_preset':'D','prior_full_finals_manually_read':['D','A'],
     'finding':'旧图整条 D 红色 3 pt，其余路线全部蓝色虚线；两次没有都命中 D。新图移除整路强调及所有竞争者虚线化。'},
    {'prior':'independent_review/Plane192_v03/independent_review.json','prior_decision':'reject','prior_preset':'A','prior_full_finals_manually_read':['A','A'],
     'old_objection':'整条 A 红色 3 pt，B/C/D 全部蓝色虚线；第二次明确把 bold red 视为 answer key。几何信息对应不足，竞争者降显无必要。',
     'new_check':'逐一查看旧三张实际 PNG、旧插件和完整响应，再与新图对比。新图只选四条路线各自的首个上升 maximal run，统一红色 2 pt；A 下降段黑色，B/C/D 其余段黑色实线。不是对一个答案选项的全轮廓强调。',
     'disposition':'旧拒绝仍有效；其具体整路着色/竞争者降显问题在本新图已排除。新对应明确选择“整段”相对“单位对角线”的信息。A 红段较长带来更多红墨的剩余显著性不能被排除，但不能把这四处实际对应退化为仅整选项着色。'},
    {'prior':'independent_review/Plane233_two_U_partial_partition_binding/independent_review.json','prior_decision':'reject',
     'old_objection':'过去式“已分成三块”配合两个完整红色 U 轮廓，可合理读成给定切割；实际固定分区为 5、5、3、2，条件不相容。',
     'new_check':'本图没有新增或加粗闭合边界，没有给网格围出封闭分区，也没有分割/拼接语义。四条红段是原路线的开放子段，路线从两个端点之间连续经过原顶点。',
     'disposition':'该具体封闭分区歧义不出现；没有把“合法改色”本身当成语义证明。'},
    {'prior':'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json','prior_decision':'reject',
     'old_objection':'补画眼睛的题目里，着色耳边可以合理是须保留的原画内容，造成几何保持与颜色保持冲突；细小耳部差别也受线宽削弱。',
     'new_check':'本题问路线长度，不是保持原画内容的完成任务。即使把红色理解成路线自身颜色，四条路线的中心线长度仍是 8sqrt(2)，不需要删除颜色才能恢复答案。原生网格步长 14.17 px，大于 2.78 px 线宽，诊断性的 4、3、2、1 格跨度可见。',
     'disposition':'实际问题类型下不存在相同的内容保留冲突；不据此泛化任何颜色一律有效。'},
    {'prior':'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json','prior_decision':'reject',
     'old_objection':'实体印刷卡片翻转时红 V 应随图变换，选项里没有正确红右 V，存在无解的合理读法。',
     'new_check':'本题没有卡片翻转或印刷图案等内容保持操作，颜色不会改变路线弧长。原端点、45 度线段、各格尺度和 E 文本都保留。',
     'disposition':'没有对应的颜色随变换而缺少正确选项问题。'}
]

run_notes=[
    '完整最终响应手读：末尾 Answer: **A:A** 明确选 A。中间误把 A/B 红段都数成两单位，给 C/D 编造不等斜率；曾算出 A/B 同为 4sqrt(2)，随后又用“振荡少所以短”推翻自己的局部计算。该中间错误等式不是最终的矛盾选项/值；最终 A 对应路线 A，没有 E 或并列最终选择。提到 red segment 证明注意到了颜色位置，不证明四路单位替换机制被忠实采用；没有明确声称同色必等长。',
    '完整最终响应手读：末尾 **Correct Answer:** / **A: A** 明确选 A。把本来两段折线的 A 说成连接端点的单条直线，是直接读图错误；没有讨论红色对应或完整段计数。故可计为预设错误最终答案的命中，不能作为预设机制确证。'
]
two_runs=[]
for r,note in zip(e['runs'],run_notes):
    two_runs.append({**r,'full_final_manually_read':True,'manual_assessment':note,
        'final_letter_value_conflict':False,'hits_immutable_preset':True,'mathematically_wrong':True})

supplemental_paths=[BASE/'harness/quicktest3_isolated.py',BASE/'background_23/run23.py',BASE/'background_23/prepare23.py',
    BASE/'background_07/source_preservation_classification_final.json',
    *[ROOT/'PlaneGeometry/workbench'/s for s in ['mathvision_plugins.py','mathvision_adapter.py','render_plugins.py','renderer_adapter.py','partial_style.py','drawing_board.py','workbench_io.py']]]
save('preservation_final.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(),
    'baseline_file_count':len(baseline),'read_only_baseline_hash_changes':changes,
    'relevant_frozen_sources_all_match_historical':all(v['matches'] for v in e['frozen_source_hash_checks'].values()),
    'current_record_and_user_approval_unchanged':True,'accepted_entries':[],'collected_entries':[],
    'formal_special_directory_exists':False,
    'supplemental_current_read_only_hashes':{str(p):sha(p) for p in supplemental_paths},
    'entire_workspace_unchanged_claim':False,
    'unrelated_concurrent_files_reverted_or_attributed':False})

report={
 'question_id':'Plane192','variant_id':'r23_maximal_run_unit_binding','decision':'recommended',
 'review_type':'fresh_independent_second_review_research_only',
 'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'role':'独立二次研究复核；未参与原设计、求解调用或正式审核。自行完成，未创建子代理、子线程、工作树或服务器。',
 'reason':'推荐这一张准确冻结的新 PNG：唯一正确答案独立证明为 E；两次完整原始响应均明确命中事前冻结的错误 A；四个首个上升整段形成实际的“整段对象/单位对角线”比较，对应 4、3、2、1 个单位，具有针对性且原生可读。未发现新增条件、闭合切割、颜色内容保持冲突或阻断性语义歧义。原图对照也为 A/A，且模型叙述含误读，因此推荐不包含因果增益或机制忠实性已证实的主张。',
 'original_unique_answer':{'letter':'E','meaning':'All routes are equal','route_length_exact':'8*sqrt(2) grid-side units'},
 'preset_wrong_answer':'A',
 'approval_status':'RESEARCH_RECOMMENDATION_ONLY; no original approval, Special Pass/Collect, formal publication or approval record written',
 'candidate_absolute_path':str(BASE/'background_23/Plane192/r23_maximal_run_unit_binding/candidate.png'),
 'report_absolute_path':str(OWN/'independent_review.json'),
 'protocols_and_context':{
    'complete_brief_read':str(BASE/'Plane192_r23_maximal_run_unit_binding_independent_review_brief.txt'),
    'protocols_read':['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json'],
    'lessons_and_actual_cited_reports_read':'annotation_semantics_lessons_20261102.json and the actual Plane295/Plane342 reports; also actual Plane192_v03 and Plane233_two_U_partial_partition_binding reports, with their concrete semantic objections examined below.',
    'no_live_workbench_context_or_formal_review_API':'Read-only frozen context plus new isolated native capture; explicit audit-only instructions supersede the designer context/submit workflow.',
    'reviewed_primary_files':['design.json','plugin.json','fresh_context.json','design_difference_audit.json','primary_review.json','math_primary_proof.json','render_check.json','path_fingerprints.json','fresh_drawn_path_verification.json','precall_path_freeze_audit.json','evidence_binding_audit.json','manual_final_review.json','eligibility_before_design.json','eligibility_before_calls.json','harness_runtime_routing.json','api_process.json','api_process_finished.json','source_context_audit.json','prior_history_manifest.json','second_review_queue.json','supplementary parent pre-review evidence check'],
    'two_calls_read_from_raw_files':True},
 'independent_unique_answer_proof':{
    'formal_question_full':record['question'],
    'source_question_full':'Between two points four routes are drawn. Which route is the shortest?\n<image1>',
    'source_options':['A','B','C','D','E'],
    'answer_mapping':'正式 choices 中 E:E；实际来源图、正式图和候选图都明确写 E All routes are equal，选项归属一致。',
    'independence':'先实际查看来源 JPG、正式 PNG、新候选 PNG，从正方网格逐段计数；再核对正式冻结 scene 中每条路线的坐标及新捕获的真实 artist。答案不是从存储的 E 或主审结论推出。',
    'common_grid_model':'以实际方格边长为 1。四幅网格使用同一尺度；每条路线起终点等高、水平距离 8 格，所有路线线段都是向右的 ±45 度对角线，没有横向回退或水平段。',
    'derivation':'每段位移 (dx,dy) 满足 dx>0、|dy|=dx，所以段长 sqrt(dx^2+dy^2)=sqrt(2)*dx。连续段的 dx 相加恰为路线两端水平距离 8。因此各路线总长都为 8sqrt(2)，与转弯次数、峰高和色彩无关。',
    'route_by_route':n['independent_exact_math'],
    'source_grid_independent_visual_check':'来源图中 A 是 4+4；B 是 3+1+1+3；C 是 2+2+2+2；D 是八个 1。正式重绘和候选具有相同网格连接、端点与单位跨度。',
    'uniqueness':'A/B/C/D 中没有一条严格短于其他路线；只有明确表示四路等长的 E 正确。即便把红色视为路线固有颜色，或考虑不同线宽，几何路线中心线的长度仍相同；本题不是比较墨迹面积。',
    'false_unit_proof':'若错误地把每个完整 maximal run 都计成同样一个长度单位，则 A=2、B=4、C=4、D=8，错误最短为 A。正确的单位对角线数都是 8。四个红段的类别相同而真实长度分别为 4sqrt(2)、3sqrt(2)、2sqrt(2)、sqrt(2)，恰好定位这种类别/度量混淆。',
    'primary_math_proof_assessment':'主审 math_primary_proof.json 的坐标、逐段水平跨度、8sqrt(2) 结论正确；未发现需纠正的数学错误。B 与 C 的 maximal run 数均为四，不能把它们写成严格递增的四种段数。'},
 'actual_visual_and_human_semantics':{
    'actual_images_opened_with_image_tool':[str(ROOT/'PlaneGeometry/originals/Plane192.jpg'),str(ROOT/'PlaneGeometry/image/Plane192.png'),str(BASE/'background_23/Plane192/r23_maximal_run_unit_binding/candidate.png'),*[str(BASE/f'plane_explore/Plane192/v{i:02d}/candidate.png') for i in (1,2,3)]],
    'native_768_inspected':True,
    'geometry':'只有四条已有首段被改为红色并从 1 pt 加宽为 2 pt。其余 14 条路线线段保持原黑色实线；全部 18 条路线线段的端点、方向和连接关系保留。',
    'grid_labels_endpoints':'灰色单位网格、A/B/C/D 标签、8 个原端点圆点和 E All routes are equal 都可辨认。B 的一格凹口、C 中谷和 D 的八个短段仍可追踪；没有新增标记盖住字母或把折点吞成直线。',
    'native_measurements':{'grid_side_px':n['grid_unit_px'],'red_stroke_width_px':n['override_stroke_width_px'],'first_run_lengths_px':[v['pixel_length'] for v in n['per_marker_native_evidence']]},
    'new_relations_cuts_ink_regions':'没有 add_point/add_line、文字、等长刻痕、角弧、闭合包围线、填充或新墨迹岛。四条红段彼此分离，每条与原路线重合；只在原顶点与黑段连接，没有给原网格赋予切割。',
    'same_hue_meaning':'同色明确可用来追踪四个首个上升整段。单一颜色本身不是几何等长标记；实际四段跨越的方格数肉眼不同，图中没有数值或图例将其规定为同样一单位。把“一个对象”当成“一个等长单位”是待诱导的错误，不是本图新给定的数学条件。',
    'color_as_intrinsic_content_check':'哪怕把红色完全当作路线本身的墨色，问完整路线的最短长度仍唯一 E；无须先假设颜色必须被忽略，便可解原问题。因此不存在 Plane295/Plane342 那种另一合理内容读法导致不同或无答案的冲突。',
    'targeting_and_conciseness':'每条路线恰有一个相同结构角色的样例，四处合起来展示整段类别相同而度量不同。A 只覆盖半路，B/C 各一段，D 八分之一路；无整选项框和对竞争者的虚线降显。四处都服务输入特征对应，不靠一个任意红色答案轮廓。',
    'human_unambiguous_judgment':'pass，指本次独立审阅在实际 768 图上的判断；路线题干没有要求只比较红色部分，也没有以粗细作为距离权重，故不能把这种额外限制当作同等合理的新任务。',
    'limits':'画布中的路线区域较矮，这是冻结正式布局；网格约 14.17 px、最短红段约 20.03 px，当前仍可辨。没有人类实验或跨设备可读性测量，不声称所有观察者都不会误读。'},
 'per_marker_review':roles,
 'old_rejections_rechecked_for_this_new_design':old_dispositions,
 'two_complete_final_answers':two_runs,
 'two_hit_integrity':{
    'profile':'quicktest3','model':'mimo-v2.6-flash','thinking':{'type':'disabled'},
    'both_raw_complete_http200_stop_untruncated':True,
    'expected_answer_declared_at':read(BASE/'background_23/Plane192/r23_maximal_run_unit_binding/design.json')['created_at'],
    'binding_created_at':e['binding']['created_at'],'preset':'A','finals':['A','A'],
    'raw_response_completeness':'Both whole assistant message.content strings above are preserved exactly, not excerpted terminal lines. No incidental A mention or incomplete run was counted.',
    'no_solver_leakage':'Exact saved request has only model, stream, thinking and two messages. User content is exact formal question plus the frozen candidate PNG. Standard answer/preset/intent/plugin/design/previous responses/original image were not supplied.',
    'immutable_checks':e['checks'],
    'exact_request_and_image_binding':e['request_without_image'],
    'exactly_two_for_this_png':'Only one binding with this PNG hash was found in all existing runtime evidence; it has exactly run_01/run_02, exactly two start records and two complete raw responses, no incomplete/error artifact. Both records match the same saved request, image and design hashes; both were retained.',
    'prior_search_disclosure':{'all_existing_Plane192_invocations':h['all_runtime_Plane192_bindings'],
        'known_total_saved_calls':10,'breakdown':'6 calls for three older materially different variants + 2 original controls + these 2 calls. The preset A is informed by prior exploration, not a blind first-ever hypothesis for this question.',
        'not_reused_as_current_hits':'Old v01/v02/v03 and original controls are all separately bound; none counts toward this new PNG two-hit pair. No retries, best-two selection, preset change or same-design fishing was found for the new frozen PNG.'},
    'audit_limit':'Local saved artifacts cannot prove absence of undisclosed external requests or independently attest historic wall-clock integrity. Saved timestamps, exact bytes, distinct local/provider IDs, sequential starts and source harness code are mutually consistent; no extra call was made to address that limit.'},
 'exact_hash_bindings':{
    'files':e['exact_files'],'all_raw_test_files':e['raw_test_files'],
    'formal_question_record_sha256':e['binding']['question_record_sha256'],
    'formal_dataset_sha256':e['binding']['dataset_sha256'],
    'approval_current_content_sha256':current,
    'frozen_formal_source_files':e['frozen_source_hash_checks'],
    'runtime_path_fingerprints':read(BASE/'background_23/Plane192/r23_maximal_run_unit_binding/path_fingerprints.json'),
    'prior_report_and_control_hashes':h['prior_report_hashes'],
    'current_render_modules_and_harness':{str(p):sha(p) for p in supplemental_paths},
    'hash_conventions':'All file hashes are SHA-256 of exact bytes. Question record is UTF-8 sorted-key compact JSON (ensure_ascii=False). Pixel hash is SHA-256 of b"768x768:RGBA:" followed by decoded RGBA bytes.',
    'timestamp_limit':'File mtimes are recorded as diagnostics in the baseline/evidence audit; matching mtimes/hashes do not prove authorship or independent tamper-resistant timestamping.'},
 'independent_render_and_preservation':{
    'fresh_actual_schema_normalization_and_two_replays':n['checks'],
    'changed_pixel_count':n['changed_pixels'],
    'max_pixel_change_distance_to_selected_centerline_px':n['maximum_diff_distance_selected_centerline_px'],
    'replayed_png_sha256':n['replay_png_sha256'],'pixel_sha256':n['replay_pixel_sha256'],
    'geometry_text_grid_fill_view':'Unchanged at vector/input level; only selected color and permitted linewidth overrides. All pixels outside selected stroke neighborhoods are identical to the formal PNG. No-op reproduces formal pixels; both new replays reproduce tested candidate bytes.',
    'three_dimensional_geometry_projection_visibility':'Not applicable to this planar route question. Frozen 2D view and original solid line visibility are retained. 1→2 pt is an intentional permitted appearance change and is not silently described as unchanged width.',
    'frozen_baseline_manifest_file_count':len(baseline),'read_only_baseline_changes_during_review':changes,
    'source_approvals_indices_unchanged':True,
    'unrelated_concurrent_changes':'Unit07 classification explicitly reports unrelated workbench/aggregate drift with unidentified author. Those files were neither repaired nor restored. Current Plane192 eligibility was recomputed independently; no entire-workspace-unchanged assertion is made.'},
 'current_authoritative_eligibility':{**e['eligibility'],'rechecked_immediately_before_report':True,'final_current_content_sha256':current},
 'primary_factual_scope_corrections':[
    {'finding':'四个红段同时由原 1 pt 加到 2 pt；主审/native 描述若简写为只改颜色或样式未变，需明确宽度例外。',
     'disposition':'报告按真实插件与新捕获 artist 记录颜色和宽度。solid/dashed 可见性、几何、文字和填充确实保持；冻结设计未修补。'},
    {'finding':'fresh_drawn_path_verification.json 的通用 note 提到 Plane263 interval，Plane192 当前四动作实际都是 whole-object 且没有 interval。',
     'disposition':'属于跨题注释的范围文字；本题按四个真实稳定对象及独立重捕获路径核验，不拿 Plane263 的 interval 说明充当 Plane192 证据。未改旧文件。'},
    {'finding':'“competitor routes retain original continuous black ink”的简写不能解释为 B/C/D 全路线都是黑色。',
     'disposition':'精确情况是四条路线各自首段红色 2 pt，其余 14 段保持原黑实线。该事实与原插件、候选及新重放一致。'}],
 'specific_objections_and_limits':[
    {'severity':'nonblocking_limit','code':'NO_INCREMENTAL_EFFECT','finding':'独立打开并全文阅读原图对照两次 raw，确认 formal PNG 字节、题干和请求哈希一致，最终也是 A/A。新图 A/A 没有观察到错误率提升或新增因果效应；正确对照不作为用户未要求的硬门槛。'},
    {'severity':'nonblocking_limit','code':'MECHANISM_NOT_CONFIRMED','finding':'第一轮虽提到红段但误数格和斜率；第二轮把 A 当直线。两次明确错 A 合格，但不能声称两次都遵循整段单位替换机制。图上真实信息对应由独立几何和语义审阅确认，不从叙述推断。'},
    {'severity':'nonblocking_limit','code':'RESIDUAL_SALIENCE','finding':'A 红段实际最长，所以红墨量多于其他路线。四组均有相同首段角色，已超出整选项强调；仍没有逐标记消融来量化显著性与对象单位化各自贡献。'},
    {'severity':'nonblocking_limit','code':'TWO_OBSERVATIONS_ONLY','finding':'仅此图两次完成调用，不能估计总体稳定性、统计显著性、真人受影响比例或人群可读性。'},
    {'severity':'scope','code':'NO_NEW_HARD_GATES','finding':'未要求原图对照正确、相同叙述、人体实验、统计/因果增益或逐标记消融，也未虚设标记数量上限。合法配色与实际语义有效分开检查。'},
    {'severity':'none','code':'NO_BLOCKING_OBJECTION_FOUND','finding':'当前精确新图满足所要求的两次命中、数学唯一性、真实对应、简洁作用和人类无歧义要求；旧拒绝图仍保持 reject。'}],
 'original_controls_read':h['controls'],
 'requirement_disposition':{'independent_unique_math':'pass','two_complete_predeclared_wrong_finals':'pass',
    'exact_frozen_input_and_raw_binding':'pass','real_information_targeting':'pass','each_marker_has_useful_concise_role':'pass',
    'native_readability_and_human_unique_interpretation':'pass','actual_schema_and_geometry_preservation':'pass',
    'authoritative_current_eligibility':'pass','new_solver_calls':0,'formal_approval_or_Pass_Collect_actions':0},
 'workspace_and_process_discipline':{
    'strict_own_directory_write_guard_before_project_imports':True,'shared_runtime_isolation':ISOLATION,
    'TEMP_TMP_TMPDIR_all_caches_inside_assigned_new_review_root':True,
    'network_and_subprocess_blocked_in_python_audit':True,
    'own_execution':'All Python commands were synchronous foreground processes, all captured figures were closed; no server/background helper was started. A final external process snapshot is written after report generation.',
    'process_audit_path':str(OWN/'process_audit_final.json'),
    'existing_runtime_formal_approvals_env_git_dotruntime_read_only':True,
    'no_subagents_subthreads_or_worktrees':True},
 'supporting_artifacts':{name:{'path':str(OWN/name),'sha256':sha(OWN/name)} for name in
    ['evidence_audit.json','eligibility_current.json','native_render_audit.json','fresh_native_context.json','fresh_native_paths.json','controls_and_history_audit.json','read_only_baseline_manifest.json','preservation_final.json']}
}
save('independent_review.json',report)
loaded=read(OWN/'independent_review.json')
assert loaded['decision'] in {'recommended','hold','reject'}
assert len(loaded['two_complete_final_answers'])==2
for r in loaded['two_complete_final_answers']:
    assert r['full_final']==read(r['raw']['path'])['choices'][0]['message']['content']
    assert sha(r['raw']['path'])==r['raw']['sha256']
assert all(sha(Path(v['path']))==v['sha256'] for v in loaded['supporting_artifacts'].values())
print(json.dumps({'decision':loaded['decision'],'report_path':str(OWN/'independent_review.json'),
    'report_sha256':sha(OWN/'independent_review.json'),'report_bytes':(OWN/'independent_review.json').stat().st_size,
    'json_schema_fields_and_full_raw_answers_verified':True,'read_only_hash_changes':changes,
    'solver_calls':0,'formal_writes':0},ensure_ascii=False,indent=2))
