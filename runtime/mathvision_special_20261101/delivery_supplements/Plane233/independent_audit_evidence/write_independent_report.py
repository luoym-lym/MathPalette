from review_env import *
from datetime import datetime,timezone

math=read(OUT/'independent_math.json')
raw=read(OUT/'raw_evidence_audit.json')
render=read(OUT/'render_geometry_audit.json')
preserve=read(OUT/'preservation_audit.json')
history=read(OUT/'history_and_binding_audit.json')
design=read(CAND/'design.json')
binding=raw['binding']

proof_C_D=(
    'C 和 D 都包含一条连续四格的直条。棋盘宽、高均为四格，故任何这样的直条必占满整列或整行。'
    '可用满列只有 x=0,1,2，可用满行只有 y=1,2,3。一个满列与一个满行必在现有格相交，'
    '所以三个互不重叠的直条必须同向。若全竖直，它们占据 x=0,1,2，最左直条的第五格只能在 x=-1（越界）'
    '或 x=1（已被另一条占据）；若全水平，它们占据 y=1,2,3，最上直条的第五格只能在 y=4（越界）'
    '或 y=2（已被占据）。因此 C、D 无论转动、翻面都不能用三份铺满。'
)
proof_B=(
    'B 的四个不同 D4 朝向分别是 U 朝上、下、左、右。对每个朝向，在 4×4 包围框中逐一平移并剔除覆盖缺格者，'
    '得到 20 个不同五格集合。附件 independent_math.json 完整列出全部 20 个集合及 first-uncovered-cell 递归证书。'
    '独立的三元组合检查逐一遍历 C(20,3)=1140 个无序三元组；没有一组两两不交且并集等于棋盘。'
    '递归检查每次选择字典序最小未覆盖格，穷尽覆盖此格且包含于剩余格集的 B 放置，得到同样的零解。'
    '这是有限穷尽证明；没有以“看起来不好拼”或一组试放失败代替全局不可铺结论。'
)

groups=[
 {'group':'source_red_four_unit_spine','action_indices':[0,2,3,4],
  'targets':['given_0','given_2','given_4','given_6'],
  'information':'棋盘左外边界 x=11、7≤y≤11 的四个连续单位段，显示完整四格高度。',
  'targeting':'与 C 的四格外侧柱边等长且同向；A/B/E 的最大跨度不足四格，D 虽有四格直条，但第五格接在内部位置。',
  'effectiveness':'几何对应真实、原生尺寸可辨；与 C 红边相差平移 (1,-7)。两次 C 结果是整张图的观察，未单独证明此组的因果效果。',
  'concision':'四个单位段构成一条连续四单位边；没有重复动作、内部边、标签高亮或不相关笔画。',
  'human_unambiguity':'它是整块棋盘的外边，不是内部切口；不规定左列必须属于哪一块。'},
 {'group':'source_blue_two_unit_subrun','action_indices':[1,5],
  'targets':['given_1','given_10'],
  'information':'棋盘底边 y=7 上 11≤x≤13 的左端两单位子段；整条底边实际延至 x=14，长三单位。',
  'targeting':'两单位子段与 C 的完整底脚等长，在左下角接上四单位红边，给出具体 L 试放位置而非只突出字母 C。',
  'effectiveness':'两段合成长约 46 px 的蓝线，右端留下约 23 px 的原黑底边，长度、终点和原完整棋盘都清楚。未做分组消融。',
  'concision':'两段是准确传达所选二单位长度的最直接现有对象表示；不是整条三单位底边，也没有补画第三段。',
  'human_unambiguity':'蓝线末端位于原有格顶点，未转入棋盘内部；原黑底边继续可见，不闭合任何真子区域。'},
 {'group':'C_red_four_unit_spine','action_indices':[6,8,9,10],
  'targets':['C_0','C_2','C_4','C_6'],
  'information':'C 左外边界 x=12、0≤y≤4 的四个连续单位段，逐段对应源红边。',
  'targeting':'只选中与题面同一四单位特征对应的边；C 的其余轮廓、内部格线和字母均未高亮。',
  'effectiveness':'可直接比较四格直柱；不把 C 局部可放的事实等同于全局铺满。',
  'concision':'四段来自原图对单位边的拆分，拼成一条连续边，无重复或无用途边。',
  'human_unambiguity':'保留 C 的五格 L 轮廓和全部内部格线；并非完整 C 轮廓描边或新画的拼块。'},
 {'group':'C_blue_two_unit_foot','action_indices':[7,11],
  'targets':['C_1','C_10'],
  'information':'C 底部 y=0、12≤x≤14 的两单位完整外底边，与源蓝子段平移一致。',
  'targeting':'把红色长柱的末端足部定位为 C 的端点附格，区分 D 的内侧附格，完成长度和朝向的配对。',
  'effectiveness':'足部和红柱在左下端相接；实际 C 细胞结构和源局部放置吻合。未证明此组单独能改变模型输出。',
  'concision':'两单位段恰好给出整个 C 底脚；没有涂完整选项、改填充或额外注释。',
  'human_unambiguity':'仅重设原边样式，未增加第五格以外的区域，也未与源图连线或画出强制配对等号。'}
]
per_action=[]
for row in render['per_action_geometry']:
    group=next(g for g in groups if row['action_index'] in g['action_indices'])
    color_role='四单位竖边的一个必需连续单位段' if row['color']=='#DC2626' else '两单位底边的一个必需连续单位段'
    per_action.append({**row,'group':group['group'],'individual_informational_role':color_role,
        'targeting':'pass: '+group['targeting'],
        'effectiveness':'pass for visible geometric role; '+group['effectiveness'],
        'concision':'pass: 恰为所声明连续特征中的一个唯一现有单位段；无重复目标。',
        'human_unambiguity':'pass: '+group['human_unambiguity'],
        'necessity_limit':'需要此动作才能完整着色所选的整段特征；不声称删除此动作必使人或模型无法识别特征。'})

run_notes=[
    '把 B 数成六格，错误否定 A，正文还先声称可排除 C，随后又选择 C；其铺法混用 T/L、重叠区域和不可能的 2×5 中间区。'
    '把 C 误称为 vertical T-shape。上述是正文推理自相矛盾，不是另一个相冲突的最终选项；结论句和 Final Answer 均选 C。',
    '把 A、B、D 各数成四格，正确识别 C 的四格柱加一格脚，却错误地以局部能放为足够条件，'
    '并提出“两 L 加一 cross”的非全等方案；没有有效三份拼合证明。结论和 Correct Answer 都明确为 C。'
]
runs=[]
for i,r in enumerate(raw['raw_runs']):
    runs.append({**r,'complete_response_personally_read':True,'manual_final_option':'C',
        'literal_terminal_final':('**Final Answer:**\nThe correct choice is **C**.' if i==0 else
                                  '**Correct Answer:**\nThe figure representing one of the pieces is **(C)**.'),
        'matches_pre_call_preset':True,'contradictory_terminal_option_or_numeric_value':False,
        'narrative_objections':run_notes[i],
        'color_as_given_error':'本响应没有显式声称红/蓝是题设颜色约束；不据此推测模型是否忽略或使用了颜色。',
        'mechanism_limit':'完整响应不证明模型实际使用了本设计的四格柱/二格脚对应。'})

history_out=[]
known_finals=[['E','A'],['B','B'],['D','B'],['C','C']]
for h,finals in zip(history['histories'],known_finals):
    history_out.append({k:h[k] for k in ['directory','design_sha256','plugin_sha256','candidate_sha256','created_at','preset','mechanism',
        'source_styled_unit_edges','source_styled_internal_edges','cut_graph_region_sizes']} | {'manual_raw_final_options':finals})

objections=[
 {'severity':'nonblocking_factual_precision','issue':'source_foot_is_a_subrun',
  'finding':'主审把源侧称为 two-cell bottom-corner foot，须理解为选择底边左端两单位，不能理解为棋盘底边只有两格；实际底边三格。',
  'correction':'本报告明确记录蓝线是 2/3 的外底边子段，且 (13,7)-(14,7) 黑线仍然存在。该选择真实且可见，不修改冻结设计。'},
 {'severity':'nonblocking_metadata_reuse','issue':'shared_primary_math_artifact_contains_prior_notch_metadata',
  'finding':'共用 math_primary_proof.json 的 notch_correspondence_transform 是上一 notch 假设的数据，不是本图的映射。',
  'correction':'本图准确映射为 (x,y)→(x+1,y-7)，已逐一验证全部六对单位边。主审的 D4 单元清单、放置数和 A2/其余0 结果均被独立重新计算确认，没有发现其数学结论错误。'},
 {'severity':'limitation','issue':'observed_hit_is_not_mechanism_or_gain_proof',
  'finding':'原图旧对照本来也是 C/C；新图仍为 C/C。两次正文有多项数学和图形识别错误，不能据此声称因果增益或逐标记效果。',
  'correction':'只推荐为满足明确两次命中、合法且语义清楚、具有真实信息针对性的候选。'}
]

report={
 'question_id':'Plane233','variant_id':'r23_four_cell_corner_spine','decision':'recommended',
 'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'summary':'推荐此精确冻结候选作为研究变体。独立数学唯一 A，冻结预设 C、两次完整最终答案 C/C，所有12动作都有真实的四单位柱/两单位脚对应；六条源边全在外轮廓，结合原外边界仍不产生内部切分。原生图清楚，旧闭合轮廓拒绝理由已对本新图逐项排除。',
 'review_status':'Independent research recommendation only; no original approval, user Pass/Collect, submission, publication or formal status change.',
 'independence':{'worked_alone':True,'subagents_threads_worktrees_created':False,'new_solver_calls':0,
    'blind_review':False,'method':'brief 已披露主审 A/C/C/C 主张；本复核实际打开原 JPG、正式 PNG、新 PNG 和三张旧 PNG，读全文题干、两份原始完整响应及原始证据，自行从冻结单位边恢复格子并双方法穷尽核验。不是把已知答案作为算法条件，也不伪称盲审。'},
 'original_unique_answer':'A','preset_wrong_answer':'C','two_complete_final_answers':runs,
 'requirements_disposition':{'unique_correct_mathematics':'pass under original congruent whole-grid-cell cutout convention, D4 allowed',
    'exact_two_predeclared_hits':'pass C/C','frozen_inputs_and_exact_tested_image':'pass',
    'information_targeting':'pass: exact length-and-corner correspondence, not answer-label or whole-choice salience alone',
    'every_mark_useful_and_concise':'pass at feature/representation level; no numeric action cap or ablation necessity required',
    'native_readability':'pass','human_unambiguous_geometric_question':'pass',
    'current_authoritative_eligibility':'pass','formal_approval':'not performed or inferred'},
 'independent_unique_answer_proof':{
    'full_formal_question':preserve['eligibility_end']['record']['question'],
    'actual_source_record':render['original_source_record'],
    'source_and_formal_geometries_identical':render['source_scene_geometry_equals_native_source_scene'],
    'coordinate_convention':math['convention'],
    'grid_and_option_cells':math['normalized_cell_inventories'],
    'area':'棋盘缺右下角 (3,0)，面积15；A 至 E 均恰五格。面积只能限定每份五格，不能筛出 C。',
    'option_descriptions':{'A':'P 五连方：底行三格、上行右侧两格。','B':'U 五连方：底行三格、上行两端各一格。',
        'C':'L 五连方：竖柱四格，右下端附一格。','D':'Y 五连方：横条四格，上方第三列附一格；不是 V，也不是四格 T。','E':'X 五连方：中心格及其上下左右四格。'},
    'enumeration_method':'从实际现有边识别四边均存在的单位格，确认每组所有边恰是恢复格集合的边并集；遍历不同 D4 朝向和框内全部整数平移。穷举所有无序三元放置，并用独立 first-uncovered-cell 递归比对全部解。完整放置列表和失败分支在 independent_math.json。',
    'enumeration':{k:{s:x[s] for s in ['orientation_count','placement_count','unordered_triples_checked','cover_count']} for k,x in math['results'].items()},
    'A_constructive_covers':math['results']['A']['covers'],
    'A_cover_explanation':'列出的每个集合五格，与 A 经旋转/翻面全等；每组的三集合两两不交且并集恰等于15格棋盘。两种划分并不代表两个答案，唯一可行选项仍是 A。',
    'B_impossibility':proof_B,'C_D_impossibility':proof_C_D,
    'E_impossibility':'任何 X 放置的中心必须离四周边界至少一格，故棋盘左下凸角格 (0,0) 不能被任何 X 的中心或臂格覆盖；不可能铺满。',
    'C_local_fit':{'cells':math['C_corner_trial_cells'],'complement':math['C_trial_complement'],
        'fits':True,'two_C_complement_covers':math['C_trial_complement_two_copy_covers'],
        'meaning':'C 沿左下角的一个五格试放是真实的；源红蓝仅标其与棋盘重合的六单位外边，并未画出其余六单位内侧轮廓。局部可放不推出全局可铺。'},
    'allowed_congruence_precision':'未要求平面内同面旋转、也未要求三块具有相同彩色印刷；实际切下的几何拼块可以翻面。额外禁止反射时五个选项都零解，A 也为零；这一诊断已计算，不能偷偷用旋转限定来否定原题。',
    'primary_math_verification':'主审所有 D4 格库存、朝向数、放置数及完整解数均与本复算一致；没有需改正的数学结论。源底边长度及共用旧 notch 元数据的精度问题单列记录。'},
 'visual_and_semantic_review':{
    'actual_images_opened_with_image_tool':[
        str(ROOT/'PlaneGeometry/originals/Plane233.jpg'),str(ROOT/'PlaneGeometry/image/Plane233.png'),str(CAND/'candidate.png'),
        *[str(BATCH/h['directory']/'candidate.png') for h in history['histories'][:3]]],
    'native_size_judgment':'实际768×768全图中单格约23 px，红长边约92 px，蓝底边约46 px，2 pt线宽约2.78 px。五个选项及其各五格结构、A 的2×2块加一格、B 的凹口、C 的四高、D 的内侧附格、E 的十字，均可逐格辨认；缺失右下角与所有字母归属清楚。未用放大图代替原生尺寸判断。',
    'preservation':'离线当前场景与冻结 fresh_context 完全相同；所有12真实路径指纹重新提取一致。当前执行器按冻结插件重绘 PNG 与实测 candidate.png 和 repeat.png 字节一致。834个变动像素均距原目标线段不超过2.397 px；除此目标描边邻域外像素不变。坐标、单位格、轮廓、原线型、文字、白底、视窗和绘图次序未改；无新增点、线、填充、标号或关系符号。',
    'source_cut_topology':{'all_source_outer_unit_edges':render['source_outer_boundary_unit_edges'],
        'all_source_internal_unit_edges':render['source_internal_unit_edges'],'styled_outer_edges':6,'styled_internal_edges':0,
        'components_when_styled_source_edges_are_treated_as_cut_barriers':[15],
        'proof':'每条源标记仅邻接一个已有格，而内部格边应邻接两个。把这些标记连同原外边界作为隔离边，内部22个邻接边未被切断，15格仍同一连通分量。标记图是外轮廓的一条六边路径；与余下原外轮廓接通只围住整个原棋盘，不闭合任何真子区域。因此不是仅以“路径开放”推断无切分。',
        'possible_black_grid_completion':'原黑网格本就闭合每个单位格；可以人为沿黑线勾出多种候选拼块，但本图没有选中其中任何内部边来把某个 L 指定为已给定切块。不能把猜测补齐的六条内部边当成实际新标记。'},
    'color_semantics':{
        'geometric_reading':'此题询问几何全等切块，未要求保持彩色印刷、继续未完成图画或对图案翻面。红蓝位于已有棋盘边，只标出可比较的长度及角端，既未绘制分割，也未声明颜色等同于拼块身份。几何全等按标准定义忽略描边颜色，独立答案仍 A。',
        'literal_ink_test':'即使把红蓝视作实际外边墨迹，这些墨迹也不能增加或删掉单位格、产生内部切割，或把“相同形状”变成“相同彩色边纹”。C 的真实局部放置可含该墨迹，但题目仍需三个全等几何块；三C数学上不可能。',
        'why_prior_drawing_print_objection_does_not_transfer':'Plane295 明确要求完成既有画，Plane342 明确变换印在卡片上的图案，保留墨迹是任务本身；本题没有这种内容保持操作。对本题强加三块彩纹完全一致会额外改变几何全等定义，并非图文所要求。',
        'judgment':'未发现本精确图文产生另一套合理的固定分割或图案保持条件，使 A 变为其他答案或无解。此判断依据题干和实际像素，不以白名单配色或作者意图代替语义检查。'},
    'human_readability_scope':'这是一次独立实际图像检查和语义判断，不是人群实验，也不保证所有读者不会作出局部到全局的推理错误。',
    'threeD_projection_visibility':'不适用三维。平面冻结 view、完整2D映射、现有实线线型均复核一致；不存在改动三维或隐藏线输入。'},
 'marker_groups':groups,'per_action_review':per_action,
 'old_objections_rechecked':[
    {'objection':'两条完整 U 源轮廓暗示已给定固定切分 5,5,3,2。','new_check':'重新读取原独立拒绝报告及旧设计并实际打开旧图；按旧22条源边重新计算分量为2,3,5,5。新图源标记仅6条全外边，内部标记为0，分量为15，不指定两块 U 或任何内部切块。','disposition':'resolved for this new image; old rejection remains valid and unchanged'},
    {'objection':'开放路径也可能结合原外边界封闭新分区。','new_check':'本次未只检查路径开放性。全部源标记都属于原16单位外轮廓，已结合原外轮廓和格邻接完整计算；围住的仅原15格整块，没有新增真子区域。','disposition':'resolved'},
    {'objection':'整选项高亮或配色合法不足以构成信息针对性。','new_check':'C 只标四单位直边与两单位端足，源侧有逐单位精确平移对应；不涂 C 字母、填充或完整轮廓。全长4与端足2的配合特指C，D内部附格不匹配端足。','disposition':'resolved by actual geometry, not schema alone'},
    {'objection':'图画补全/印刷变换题把颜色当内容会改变答案。','new_check':'已读 annotation_semantics_lessons 及 Plane295、Plane342 实际报告的语义证明，并依据本题几何切块语义完成上面的墨迹检查。此题不要求传递或保留印刷图案；彩边没有产生新区域。','disposition':'not applicable as a blocking objection to this geometric question'},
    {'objection':'局部试放正确不表示三份能铺满。','new_check':'真实验证左下C试放，并以全直条不相交证明和完整816个三元组两方法证明C不能铺满；唯一A不依赖主审答案。','disposition':'preserved as the targeted misconception, not a mathematical inference by the reviewer'},
    {'objection':'原图对照C/C已错，不能声称增益。','new_check':'直接读取旧原图两份完整原始响应并验证其嵌入PNG是正式原图；结尾均C。新图同C/C，不作增益或因果声明。','disposition':'disclosed limit; correct controls not invented as a hard gate'}],
 'history_and_pre_call_audit':{
    'all_saved_question_invocations':history_out,'original_control_final_options':['C','C'],
    'full_history_artifact':str(OUT/'history_and_binding_audit.json'),
    'all_runtime_binding_scan':'根runtime扫描只发现5份Plane233 binding：cross、two_U、原图controls、notch、本corner-spine；各2次。与本PNG相同的binding仅1份，两个start、两个completed和两个raw response，未发现不完整或额外同图调用。',
    'material_difference':'旧cross为E的完整十字边界（按实际切边得到1,5,9），旧two_U为B的两完整U边界（2,3,5,5），上一个notch仅强调缺角凹口两条一单位边并对应B。本图是左侧四格长边与左端二格外底边，精确对应C的柱和脚，选中特征、位置、尺度和目标形状均改变；不是只改颜色/粗细，也没移用旧C/C控制响应。',
    'target_timing':{'design_created_at':design['created_at'],'primary_reviewed_at':read(CAND/'primary_review.json')['reviewed_at'],
        'binding_created_at':binding['created_at'],'starts':[r['record']['started_at'] for r in runs],
        'finishes':[r['record']['finished_at'] for r in runs],'design_png_plugin_mtimes':history['current_mtimes_diagnostic_only'],
        'snapshot_bytes_equal_current_design':True,'preset_fixed_before_both_calls':True},
    'not_blind_preregistration':'旧原图C/C和旧候选结果在新假设形成前已可用；这是一轮知晓历史的设计修订，不是事前盲选。新C预设和新图在本两次调用前冻结，有独立几何理由。没有本图测后改目标、选取成功响应或未变图重试的证据。',
    'caller_and_harness_review':'实际阅读原 harness 和 run23.py：冻结请求、图像、设计snapshot后固定for两次；每次验证图像/设计字节不变；失败break，无自动retry；不按答案选择或替换结果。两次调用均只有固定system+正式题干+同一PNG，没有前一次响应上下文。',
    'provenance_limit':'文件记录、哈希、时间和执行代码相互一致，但不是外部签名证据，不能排除未记录的外部调用或证明所有历史操作的作者。'},
 'exact_evidence_bindings':{
    'candidate_directory':str(CAND),'candidate_png_sha256':sha(CAND/'candidate.png'),
    'candidate_pixel_sha256':binding['pixel_sha256'],'plugin_sha256':sha(CAND/'plugin.json'),
    'design_sha256':sha(CAND/'design.json'),'design_snapshot_sha256':sha(TEST/'design_snapshot.json'),
    'original_png_sha256':sha(ROOT/'PlaneGeometry/image/Plane233.png'),
    'source_jpg_sha256':sha(ROOT/'PlaneGeometry/originals/Plane233.jpg'),
    'formal_scene_sha256':sha(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane233.json'),
    'frozen_context_sha256':sha(CAND/'fresh_context.json'),'live_context_sha256':sha(OUT/'live_context.json'),
    'path_fingerprints_sha256':sha(CAND/'path_fingerprints.json'),
    'formal_question_record_sha256':binding['question_record_sha256'],
    'dataset_sha256_at_calls':binding['dataset_sha256'],'dataset_sha256_now':history['current_dataset_sha256'],
    'request_body_sha256':sha(TEST/'request.json'),'binding_sha256':sha(TEST/'binding.json'),
    'primary_review_sha256':sha(CAND/'primary_review.json'),'primary_math_proof_sha256':history['primary_math_proof_sha256'],
    'raw_response_sha256':[r['raw_response_sha256'] for r in runs],
    'solver_profile':binding['profile'],'model':'mimo-v2.6-flash','thinking':{'type':'disabled'},
    'reasoning_tokens':[r['record']['usage']['completion_tokens_details']['reasoning_tokens'] for r in runs],
    'no_answer_preset_or_intent_in_solver_request':True,'solver_system_prompt':binding['system_prompt'],
    'frozen_source_files_compared_to_actual':history['current_frozen_source_comparison'],
    'all_scoped_source_and_evidence_start_hashes':str(OUT/'baseline_hashes.json')},
 'current_authoritative_eligibility':preserve['eligibility_end'],
 'objections_and_corrections':objections,
 'limitations':[
    '旧原图也C/C；仅观察到新冻结图两次明确命中预设错误C，无正确率下降、因果增益、统计稳健性或人群效果结论。',
    '两响应正文不一致且多处数学错误，未证明预设特征对应实际驱动了输出。未做逐标记/逐组消融。',
    '每标记的必要性是完整表达所选特征的表示性用途，不是删除实验意义的因果必要性；没有发明动作数量上限。',
    '人类无歧义是独立图文判断，不是新的人类研究。自然几何拼块约定允许翻面，并以全等而非仅等面积解释 equal pieces。',
    '记录时间与文件mtime为内部历史证据，哈希不提供不可抵赖时间戳。未记录的外部模型调用无法被文件审计排除。',
    '只断言本题相关冻结输入及旧证据未改。并行的Author designed/工作台/aggregate和mutable exploration/remaining元数据不能按整仓hash归责；未恢复或改写这些文件。',
    'recommended 只是这份新候选的研究复核推荐，不替代用户原题审核或Special Pass/Collect。'],
 'workspace_and_process_discipline':{
    'own_output_root':str(OUT),'strict_own_directory_write_guard_before_project_imports':True,
    'shared_runtime_isolation':render['isolation'],'TEMP_TMP_TMPDIR_all_caches_inside_own_root':True,
    'network_and_child_process_blocked_by_python_audit_guard':True,'new_solver_calls':0,
    'formal_files_approvals_state_and_previous_evidence_modified':False,'scoped_preserved_files':preserve['baseline_file_count'],
    'scoped_hash_changes':preserve['changed_scoped_sources_or_old_evidence'],
    'whole_workspace_unchanged_claim':False,'unrelated_changes_preserved':True,
    'all_matplotlib_figures_closed':preserve['all_figures_closed'],
    'background_helpers_or_servers_started':False,'own_processes':'所有审计/重绘脚本均前台运行并已退出；无子代理、后台服务或求解进程。最终由独立终检记录自有PID退出状态。'},
 'supporting_artifacts':{name:{'path':str(OUT/name),'sha256':sha(OUT/name)} for name in [
    'independent_math.json','raw_evidence_audit.json','render_geometry_audit.json','history_and_binding_audit.json','preservation_audit.json','baseline_hashes.json','live_context.json','replay.png']}
}
save('independent_review.json',report)
emit({'decision':report['decision'],'report':str(OUT/'independent_review.json'),'sha256':sha(OUT/'independent_review.json'),
      'complete_raw_answer_count':len(runs),'per_action_count':len(per_action),'groups':len(groups)})
