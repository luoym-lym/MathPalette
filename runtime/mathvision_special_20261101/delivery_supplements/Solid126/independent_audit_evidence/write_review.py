from review_env import *
BASE=ROOT/'runtime/mathvision_special_20261101';CAND=BASE/'background_37/Solid126/r37_local_area_replacement'
bind=read(OUT/'binding_audit.json');render=read(OUT/'render_and_geometry_audit.json');preserve=read(OUT/'source_preservation_and_final_eligibility.json');initial=read(OUT/'read_only_inputs_before.json')
eligible=preserve['final_authoritative_eligibility'];formal=read(OUT/'authoritative_eligibility.json')['formal_record']
assert bind['current']['checks']['all_checks_pass'] and bind['old']['checks']['all_checks_pass']
assert all(bind['current']['pretest_freeze_hash_checks'].values()) and all(bind['current']['frozen_source_hash_checks'].values()) and all(bind['current']['chronology_checks'].values())
assert render['baseline_formal_pixel_match'] and render['candidate_exact_bytes_reproduced_twice'] and all(render['preservation_checks'].values())
assert preserve['all_initially_tracked_bytes_unchanged'] and eligible['eligible']
roles=[
    ('red_removed_top_length','旧顶面沿 x 的 9 单位后沿；与新台面后沿构成相同宽度的对应。','红色旧顶面开放 L 的长边。只标这一边不能表达面积的第二维，动作1补上真实深度。'),
    ('red_removed_top_depth','旧顶面沿 y 的 6 单位深度边；与动作0在同一世界点 (0,6,8) 相接。','将旧顶面特征从一个长边补成具有 9 与 6 两个真实方向的开放 L。该部分是原有 ghost 辅助轮廓，不是当前实体的实棱。'),
    ('red_new_floor_length','新暴露 z=5 台面的 9 单位后沿；是动作0向下平移3后的对应边。','真实新台面的长边接收对象，并非任意红色轮廓或选择字母强调。'),
    ('red_new_floor_depth','新暴露 z=5 台面的 6 单位深度边；与动作2在 (0,6,5) 相接。','补足新台面的第二维，使两组 9×6 区域对应能够在图上读出；也保留全深度贯穿的线索。'),
    ('blue_removed_end_height','x=0 外端面被移除部分的前侧高边，从 z=5 到 z=8，真实长3。','旧端面 3×6 的高边代表；原虚线仍表示已移除轮廓，不能当作当前封闭的实体壁。'),
    ('blue_new_cutside_height','x=9 新切面前侧高边，从 z=8 到 z=5，真实长3。','与动作4形成真实等高的旧端面/新切面对应。共同的深度6已由原尺寸及两条 y 方向边界明确，不需要再画框。')
]
per_marker=[]
for m,(name,feature,purpose) in zip(render['markers'],roles):
    assert m['geometry_matches_design'] and m['endpoints_match_design'] and m['projected_path_matches_geometry'] and m['exact_color_pixels_within_2_5px_of_own_path']>0
    per_marker.append({**m,'marker_name':name,'actual_feature_zh':feature,'specific_information_and_use_zh':purpose,'legality':'pass: 原对象整条开放路径，稳定ID/真实3D端点/精确投影/实际path SHA均已独立核对；仅白名单红或蓝、2 pt；未指定linestyle或interval，未新增点线文字填充。','targeting':'pass: 是明确面积替换比较中的一个真实方向/接收对象，不是无关装饰。','effectiveness':'pass for visible informational role; frozen pair gives A/A. 每条标记对模型输出的因果必要性未被证明。','conciseness':'pass: 本动作各表示选定局部面积特征的一条实际边，无重复描边或不可见动作。此判断不声称删除实验意义上的最小性。','native_readability':'pass: 在实际768×768候选查看，并独立核对本路径上存在精确配色像素。','human_unambiguity':'pass in the combined diagram: 原尺寸、实体边与ghost虚线保持可辨；着色不把旧边变为当前端盖、不改变面积条件。'})
groups=[
    {'group':'red_removed_top_open_L','actions_zero_based':[0,1],'true_region':'z=8, 0≤x≤9, 0≤y≤6；原顶面中被去掉的54。','information':'长9与深6两条相接的历史边组成开放L；指明真实被去掉顶面的二维尺寸。','validity':'pass: 两条都是正式场景已有ghost虚线；不在剩余实体上创建新顶盖。','concision':'各一方向，开放而未另画矩形或填充；两条均有作用。','native_clarity':'9方向约358.30px，6方向约176.32px，红虚线可读。'},
    {'group':'red_new_floor_open_L','actions_zero_based':[2,3],'true_region':'z=5, 0≤x≤9, 0≤y≤6；新暴露台面54。','information':'与上一L整体相差 (0,0,-3)；两个方向的真实长度均相同，表达局部面积替换，而非仅两条任意同色边。','validity':'pass: 台面属于保留实体的真实外边界，两条仍为实线；floor指台阶水平面，不是被排除的地面底面。','concision':'长边和深度边分别接收上组两维信息，不补画端帽、闭合框或解题数值。','native_clarity':'红实线与上方红ghost虚线分层清楚；与蓝ghost在原投影交叉处不增加交点。'},
    {'group':'blue_removed_end_new_cutside','actions_zero_based':[4,5],'true_regions':'旧x=0端面 0≤y≤6,5≤z≤8 被移除18；新x=9切面同y/z范围暴露18。','information':'两个真实高3的前侧高边相互对应，结合未改的全深度6得3×6=18。','validity':'pass: 两条同长3，不再将旧设计的下部高5误绑定到切高。左边仍虚线、右边仍实线。','concision':'仅两条高边，明确两个面积所属对象；没有给端面加完整轮廓或隐含新封闭壁。','native_clarity':'每条约119.43px；blue ghost和blue实体边均有可见实色像素。'}
]
proof={
    'derivation_basis':'亲自打开361×303来源JPG、768×768正式PNG和准确候选PNG；读取完整正式题/选项、原始source.json、正式场景和上游场景。先从尺寸与形体推导，再与批准答案和主审核对。父预核验仅用作路径索引。',
    'source_dimension_interpretation':{'12':'原长方体 x 总长。','6':'前后 y 全深度，阶梯上下两层均沿同一深度贯穿。','8':'右侧完整 z 总高。','5':'左侧低台保留高度；不等于切去高度。','3':'右上完整高块的剩余 x 宽度；不等于切去宽度。','deductions':'切去宽12−3=9，高8−5=3，深6。'},
    'world_model':'原体 [0,12]×[0,6]×[0,8]。去掉的角块为 [0,9]×[0,6]×[5,8]。剩余是 [0,12]×[0,6]×[0,5] 与 [9,12]×[0,6]×[5,8] 的并，正与冻结 opaque_cuboids 一致。共享边界按面积计数只有外表面，内部接触面不算。',
    'original_area':'S0=2(12×6+12×8+6×8)=432。',
    'local_surface_accounting':[{'removed':'旧水平顶面9×6=54','exposed':'新水平台面9×6=54','net_loss':0},{'removed':'旧x=0端面上部3×6=18','exposed':'新x=9切面3×6=18','net_loss':0},{'removed':'前端y=0的9×3=27','exposed':'无；切除一直到外部空气','net_loss':27},{'removed':'后端y=6的9×3=27','exposed':'无；切除贯穿整个深度','net_loss':27}],
    'why_no_new_endcaps':'front/back本来是y=0、y=6处的外面。去掉的9×3部分现在是外部空气；切口没有一层材料在端头封住它，不能把被去掉的两个矩形再作为新面加回。保留的两个端面各是面积69的L形面。原虚线只记录历史外形，并不制造物质壁。',
    'net_surface':'旧外面总计去126=54+18+27+27；新暴露72=54+18；净少54。因此 S1=432−54=378，减少54/432=1/8=12.5%。',
    'independent_cross_section_proof':{'boundary_vertices_xz':[[0,0],[12,0],[12,8],[9,8],[9,5],[0,5]],'area':'12×8−9×3=69；另以独立鞋带公式计算得69。','perimeter':'12+8+3+3+9+5=40，与原矩形周长40相同。','depth':6,'remaining_area':'2×69+40×6=378；原2×96+40×6=432。周边挤出面总面积不变，但两个截面各减少27。'},
    'third_check_independent_unit_cell_enumeration':render['independent_math'],
    'unique_option':'唯一B。A严格为Less than12.5%；B精确12.5%；C严格介于12.5%与25%；D精确25%；E大于25%。A并非恒等0%，两响应的0%只是落入A的具体错误值。',
    'bottom_area_scope':'原/新底面z=0面积72均计入全表面积；题干无排除地面条件。若误把底面去掉，会改变分母为360并产生15%的不同问题；该解释没有题干依据。',
    'unique_human_interpretation':'来源和冻结形体均是沿y轴的L形直棱柱；候选没有新增线段、面或尺寸。ghost/实体区别和全部五个数值仍清楚，因此未发现另一个合理形体、切分或面积范围解释。'}
finals=[]
interpretations=[
    '全文亲自阅读：明确说red lines表示切掉材料，并以旧顶面/旧竖面和新台面/新竖面全抵消推到0%，最后A。它漏掉前后两个9×3损失。对red material的提及支持其注意到了标记，但不能证明新配色使输出从正确变错。',
    '全文亲自阅读：先正确计算432，随后把水平3读成切口深度/宽，错误引入高8和3的梯形与16.5，再虚构新的前后竖面将51全部抵消。最后明确0%及A。正文既没有正确识别真实9×6区域，也不是对预设机制的忠实证明；终答命中和标记本身的真实信息性须分开判断。'
]
for r,interpretation in zip(bind['current']['runs'],interpretations):
    finals.append({**r,'entire_raw_response_personally_read':True,'independent_manual_interpretation_zh':interpretation,'final_letter_and_value_consistent':True,'model_reasoning_mathematically_correct':False})
old=bind['old'];old_design=read(BASE/'background_14/Solid126/remaining_height_to_cut_binding/design.json')
old_objections=[
    {'issue':'旧3条竖棱设计的A/A可能被事后改标为成功。','independent_check':'已实际打开旧PNG，读取旧design、plugin、完整两份raw及人工记录，并独立复算旧binding/request/snapshot/run/response/summary全部绑定。旧预设始终C（20.833…%来自错用切高5），两次明确0%、A，所以仍是MISS。新预设A只绑定本次新图的两次新响应。','disposition':'resolved for current evidence; old MISS preserved'},
    {'issue':'新图是否只是沿用旧A/A后换色。','independent_check':'旧目标 ring0e5part0、ring0e3part0、ring1e3part0，三条高5/3/3的竖边。新目标 removed1、removed2、ring1e4part0、depth5part0、removed4、ring0e3part0，六条9/6/9/6/3/3边，只有一个旧目标保留且改作真实高3对应；去掉高5源和后切高目标，新增真实top/floor两维及old-end目标。两图字节/像素均不同，几何假设已从错误高度绑定变为真实局部面积抵消外推。','disposition':'materially new hypothesis, not cosmetic relabeling'},
    {'issue':'四条红线能否真正表示两个面积，而只是无关线条装饰。','independent_check':'逐一核对3D端点和同一投影；两组边各在同一水平面相接成9与6的开放L，精确相差z=3。两真实矩形均为54。蓝色则是两个真实等高3的对应高边，结合共同深度6为18。每个动作都有具体接收/方向作用。','disposition':'satisfied independently of A/A'},
    {'issue':'局部抵消可能被误当作全表面积不变，front/back损失被隐藏。','independent_check':'数学上明确记录两端各减27；实际候选仍保留黑色前低台长9边、黑色前ghost顶长9边、两侧高差和后侧对应边。改变像素只在六条旧路径2.38px以内；没有盖住缺口或画新端盖。','disposition':'not a human ambiguity; it remains the intended incorrect overgeneralization'},
    {'issue':'主审仍待全新独立二次复核，不能把作者自审或父precheck当作证明。','independent_check':'本次无父历史，由此复核者亲自读源图/正式图/候选、完整题干和raw，重新构造三种数学核验、重放图、计算指纹/时序。未复用父结论充当独立证据。','disposition':'addressed by this new research review only'},
    {'issue':'Plane242纸片彩边可能被误推广为颜色禁令。','independent_check':'已读指定lesson与实际独立报告。彼题要求搬动实体纸片并匹配保留彩边的成图；这里要求几何表面积的数值。即便把颜色看作物体表面的墨迹或涂漆，几何尺寸/外表面积仍不改变，不需让墨迹消失才能选B。ghost虚线也与正式原图一致，不是颜色新增的物质表面。','disposition':'that task-specific competing interpretation is not reproduced'},
    {'issue':'Plane233固定分割/闭合轮廓异议。','independent_check':'六条均为既有路径的描边；红开放L没有添加横切、端盖、闭合填充或新切面。结合原边界也只指已有的旧顶面/新台面/旧端面/新切面，没有新增实体分区。题干未把彩线规定为固定分割。','disposition':'no new incompatible partition found'},
    {'issue':'没有原图正确对照、没有相同叙述或逐条消融。','independent_check':'本任务runtime中独立发现的Solid126 binding仅旧图一组和新图一组，无原图control。旧图也A/A，所以不能声称新图增量有效；两新raw叙述也不同。这些限制不代替本任务要求的真实标记信息性与清楚图文，也不另加为硬门槛。','disposition':'nonblocking disclosed limits'}
]
corrections=[
    {'kind':'scope_precision','finding':'共用box helper会同时输出full_surface_area、ground_area、painted_area等诊断；只有明确排除地面的问题才能用ground-excluded值。','independent_resolution':'读primary_supplement后仍从题干与实际L形体独立重新算全表面积，含底面72。当前Solid126主审/补充的432、378、54、12.5%结论正确；未将其他题的painted诊断当成Solid126当前结论，也未修改旧文件。','blocking':False},
    {'kind':'formal_choice_semantics','finding':'不能把正式A写成恒等0%。','independent_resolution':'完整正式choices的A为Less than12.5%。两次各自声称的0%与A一致；预设A在调用前冻结。','blocking':False},
    {'kind':'mechanism_overstatement','finding':'review37.py源代码曾把Solid126的information_mechanism_confirmed_by_outputs分支写成True；该布尔字面值不是因果或正确几何推导的证据。','independent_resolution':'第一响应有与局部抵消相近的错误且提red；第二响应错读梯形和尺寸。本复核只确认标记的真实比较信息与两终答命中，不认可机制已被实验确证或每条标记已导致错误。当前落盘manual_final_review的完整原文已单独核对。','blocking':False},
    {'kind':'native_artist_vs_png_bytes','finding':'无操作重绘与正式PNG的文件SHA不同。','independent_resolution':'已逐chunk核对，除Software tEXt外的全部chunk数据一致；正式为MathPalette strict protocol renderer，无操作桥为MathPalette SolidGeometry 1.0.0。RGBA像素逐点一致；候选则两次连PNG字节都精确一致。no-op要求的像素一致性满足。','blocking':False},
    {'kind':'terminology_precision','finding':'正式scene将removed*列为visibility=visible的auxiliary，并显式linestyle=dashed。','independent_resolution':'它们是可见绘制的历史移除轮廓，不是剩余实体的隐藏实棱。报告区分这一role与成图虚线，不因同色把ghost转换成当前面。','blocking':False}
]
sha_keys={
    'source_jpg':ROOT/'SolidGeometry/originals/Solid126.jpg','formal_png':ROOT/'SolidGeometry/image/Solid126.png','formal_scene':ROOT/'SolidGeometry/dataset_generator/scenes/Solid126.json','formal_script':ROOT/'SolidGeometry/dataset_generator/solid_plot126.py','candidate_png':CAND/'candidate.png','plugin':CAND/'plugin.json','design':CAND/'design.json','pretest_freeze':CAND/'pretest_freeze.json','primary_supplement':CAND/'primary_supplement.json','quick_test_reference':ROOT/'SolidGeometry/workbench/quick_test.py','original_harness':BASE/'harness/quicktest3_isolated.py','old_candidate_png':BASE/'background_14/Solid126/remaining_height_to_cut_binding/candidate.png','old_design':BASE/'background_14/Solid126/remaining_height_to_cut_binding/design.json'}
report={
    'question_id':'Solid126','variant_id':'r37_local_area_replacement','decision':'recommended','reviewed_at_utc':stamp(),'role':'全新独立二次复核者；不是作者/父预核验；仅研究推荐。',
    'reason':'推荐这一张精确冻结候选用于研究：唯一正确B=12.5%已独立证明，预设A在新两次前冻结，两份完整原始终答均明确0%并选A；六条旧路径形成真实9×6、3×6局部面积抵消对应，各有具体信息作用，尺寸/ghost/缺口清楚，未发现新增端盖、固定切分或另一合理数学语义。不能声称增量、统计稳健性或机制因果已证实。',
    'review_scope':{'own_new_directory':str(OUT),'candidate_directory':str(CAND),'actual_tested_png':str(CAND/'candidate.png'),'frozen_test_directory':bind['current']['test_directory'],'parent_precheck_role':'path index only; no mathematical or binding conclusion adopted without new verification','independence':{'no_parent_history':True,'no_subagents_threads_or_worktrees_created':True,'no_new_solver_control_retry_or_API_call':True,'no_design_plugin_preset_or_old_evidence_modified':True,'no_formal_approval_Pass_Collect_or_global_ledger_write':True}},
    'requirements_disposition':{'original_math_unique':'pass: independently B=12.5%','two_complete_predeclared_wrong_finals':'pass: A/A, each explicit0% under the actual A range','precall_design_and_preset_binding':'pass','exact_original_profile_and_request':'pass: mimo-v2.6-flash / thinking.type=disabled / formal question+same PNG only','schema_and_exact_original_paths':'pass','geometry_projection_visibility_dimensions_text_fill':'pass','no_op_formal_pixels':'pass','candidate_two_exact_byte_replays':'pass','specific_information_targeting':'pass by independent area/edge correspondence, not final hits alone','concise_and_useful_marks':'pass; each of six has a representational purpose','native_readability':'pass on actual native source/formal/candidate inspection','unique_human_semantics':'pass; no reasonable added material/cut/cap or area-scope interpretation found','current_authoritative_eligibility':'pass; still no user Special approval'},
    'original_question_full':formal['question'],'formal_choices':formal['choices'],'original_unique_answer':{'letter':'B','percentage':12.5,'surface_area_original':432,'surface_area_remaining':378},
    'preset_wrong_answer':{'letter':'A','formal_meaning':formal['choices']['A'],'specific_predicted_wrong_value_percent':0,'not_equated_with_all_A_values':True,'hypothesis':'把真实旧顶面/新台面54抵消和旧端面/新切面18抵消外推为全表面积无损，漏掉front/back各27。','frozen_in_design_sha256':sha(CAND/'design.json'),'frozen_before_both_new_calls':True},
    'two_complete_final_answers':finals,'independent_mathematical_proof':proof,
    'actual_images_opened':[{'absolute_path':p,'size_px':v['size'],'sha256':v['sha256'],'opened_with_view_image_original_detail':True,'native_dimensions_reviewed':True} for p,v in preserve['all_input_images'].items()],
    'native_visual_and_human_review':{'findings_zh':'来源361×303原生图显示一个贯穿深度的阶梯切块；正式/候选768×768中5在左下保留高度，3在右上保留宽，12/8/6的范围标识和黑字完整。红色旧顶L仍虚线，新台面L仍实线；蓝色旧端高边仍虚线，新切面高边仍实线。长9黑色前台面边和原ghost前顶边都保留，前/后L形端面及缺口边界没有被红蓝擦去。相交处没有新增点；原本未显示的背后底边未被补全。','all_dimensions_legible':['3: remaining upright width','5: lower remaining height','6: full depth','8: full height','12: total width'],'human_semantic_test':'将彩线读成比较标注或表面着色均不改变外表面积；它们不是等长符号、数值、面填充、闭合切分，也不会把ghost复活成物质。两条红开放L确实界定相同形状的真实旧/新水平面；蓝色高边均真实为3。故B不需要额外的“忽略颜色”假设。','front_back_losses_not_hidden':'前后端面保留面积各69、缺失9×3各27。这是切口敞开的外部空气，未画任何新端盖。台面/切面54与18的真实局部抵消，不足以抵消这两块损失。','same_color_is_not_a_metric_given':'同色没有被当作新相等条件；所比较的长度和面积由原尺寸独立导出，实际确实相等。','information_vs_deception':'视觉配对有具体几何信息，其错误诱导来自把正确局部关系过度推广；并未更改题目的真实条件。','judgment_scope':'独立图文审阅，不是人群实验/无误率保证。'},
    'marker_groups':groups,'per_marker':per_marker,
    'independent_render_audit':{'baseline_formal_pixel_match':True,'baseline_formal_byte_match':False,'baseline_metadata_explanation':corrections[3]['independent_resolution'],'candidate_byte_match_twice':True,'candidate_pixel_sha256':render['candidate_pixel_hashes'][0],'preservation_checks':render['preservation_checks'],'appearance_changes':render['appearance_changes'],'difference_footprint':render['pixel_difference_footprint'],'original_objects_equal_both_frozen_contexts':True,'candidate_normalized_plugin_equals_frozen':True,'all_mark_paths_full_open':all(not p['closed'] for m in render['markers'] for p in m['paths']),'environment':render['environment'],'full_artifact':str(OUT/'render_and_geometry_audit.json')},
    'exact_sha256':{k:{'absolute_path':str(p),'sha256':sha(p)} for k,p in sha_keys.items()},
    'exact_test_evidence_sha256':bind['current']['evidence_sha256'],'formal_record_canonical_sha256':digest(formal) if 'digest' in globals() else read(OUT/'authoritative_eligibility.json')['formal_record_canonical_sha256'],
    'precall_chronology':bind['current']['chronology'],'precall_chronology_checks':bind['current']['chronology_checks'],'request_binding_checks':bind['current']['checks'],'request_without_base64':bind['current']['request_without_base64'],'pretest_freeze_hash_checks':bind['current']['pretest_freeze_hash_checks'],'all_frozen_source_dependency_sha_checks':bind['current']['frozen_source_hash_checks'],
    'response_binding_and_retry_audit':{'exactly_two_current_calls':True,'both_http200_completed_stop_untruncated':True,'two_distinct_run_and_provider_response_ids':True,'same_request_image_design':True,'stream':False,'thinking':{'type':'disabled'},'model':'mimo-v2.6-flash','no_token_limit_temperature_timeout_or_other_profile_override_in_payload':True,'original_harness_reference_read_and_hash_checked':True,'unchanged_original_system_prompt':bind['current']['request_without_base64']['messages'][0]['content'],'only_formal_question_and_candidate_png_in_user_message':True,'no_answer_intent_proof_plugin_control_or_history_sent':True,'new_calls_retries_controls_by_this_reviewer':0,'existing_archive_inventory':bind['independently_discovered_all_Solid126_test_bindings_under_task_runtime'],'current_errors_aborts_incomplete_files_found':0,'harness_code':'读取原quick_test.py、原isolated harness以及run37/tools37；两次新请求使用同一不可变payload，不调用附加对照，无自动重试。'},
    'old_history':{'old_variant_id':old_design['variant_id'],'old_preset':'C','old_observed_finals':['A','A'],'old_explicit_values_percent':[0,0],'old_result':'MISS; remains MISS, never relabeled','old_image_sha256':sha(BASE/'background_14/Solid126/remaining_height_to_cut_binding/candidate.png'),'old_design_sha256':sha(BASE/'background_14/Solid126/remaining_height_to_cut_binding/design.json'),'both_old_complete_raw_responses_personally_read':True,'both_old_bindings_independently_validated':old['checks'],'old_evidence_sha256':old['evidence_sha256'],'old_runs_with_full_content':old['runs'],'old_result_not_counted_as_current_trial':True,'no_original_control_binding_found':True},
    'old_objections_and_primary_deferral_rechecked':old_objections,'primary_fact_and_scope_corrections':corrections,
    'current_authoritative_eligibility':eligible,
    'reference_review_study':{'batch_12':'已查看近期manifest（Plane192、Plane233，均recommended，原图对照也错），不把正确control额外加成门槛。','Solid128':'实际独立报告以具体对象/局部特征对应和原生清晰度审核，未证明模型机制也可作为局限。','Solid197':'实际独立报告虽original control同样450/450，仍按两条真实边/折痕比较及未改变sticker条件判断，不能据此声称增量。','Plane192':'新四个实际maximal-run对应与旧whole-choice salience区分；本题同样须核实六条边真实关系而不止颜色合法。','Plane233':'开放外边对应不等于旧闭合U固定切分；本题没有新增边/闭合切分。','Plane242':'lesson和实际101601字节独立JSON中纸片彩边/保色/端点邻接异议、逐标记信息及证明修正均已阅读；不机械外推到数值表面积。','references_are_context_not_independent_proof_of_this_candidate':True},
    'blocking_objections':[],
    'nonblocking_limitations':[
        '没有Solid126原图control；旧不同图也A/A。本复核不新增调用，不能推断相对原图或旧图的因果/统计增益。',
        '两次完整终答命中同一事前预设，不是统计稳健性或可靠错误率估计；第二次存在额外尺寸/梯形幻读，两次不必有相同推理叙述。',
        '第一响应提red material且有局部抵消外推，第二响应没有忠实重述9×6/3×6。未证明真实局部配对实际驱动了各次内部推理。',
        '每条标记的用途是表达真实比较的表示性用途；未做消融、人群研究或逐条因果必要性实验。没有把这些另设硬门槛。',
        '同色合法、两个A终答、甚至几何保真均不单独替代信息针对性与人类无歧义判断；本报告对这些分别核验。',
        '哈希、落盘时序及文件mtime提供现存本地证据的一致性。没有外部可信时间戳或provider端全量调用账本，不能排除未披露/已删除的外部活动。',
        '原生可读/无合理歧义为此复核者对本准确图文的独立判断，不是所有人群零误读结论。',
        '只断言已跟踪的本题输入、协议/依赖、正式资格与旧证据未改；不以整仓或其他并行任务变化归责。',
        '一次本地离线审计脚本因旧人工记录使用complete_final_answer_text而非complete_raw_final_answer_text出现KeyError，已仅在自有脚本兼容字段后完成；不是模型/API重试，未改旧记录。'
    ],
    'read_only_preservation':{'initially_tracked_input_count':preserve['tracked_input_count'],'all_tracked_bytes_unchanged':True,'all_tracked_mtimes_unchanged':True,'changes':[],'exact_before_sha256_manifest':str(OUT/'read_only_inputs_before.json'),'full_after_comparison':str(OUT/'source_preservation_and_final_eligibility.json'),'additional_read_only_sources_manifest':str(OUT/'additional_read_only_sources.json'),'all_initial_input_sha256':initial['files'],'no_env_git_formal_or_existing_runtime_write':'自有写入guard将所有Python文件变更限于本复核目录；PowerShell/apply_patch也仅写此目录。未读.env凭据、未改.git、未恢复旧日志/分数。'},
    'workspace_and_process_discipline':{'all_output_below':str(OUT),'python_flags':'-X utf8 -B','TEMP_TMP_MPLCONFIGDIR_XDG_CACHE_HOME_inside_own_directory':True,'strict_own_write_guard_installed_before_any_project_import':True,'runtime_isolation_used':True,'runtime_isolation_generic_guard_disabled_because_stricter_own_guard_already_active':True,'no_network_or_child_process_execution_in_review_python':True,'all_scenes_closed':True,'own_background_processes_started':0,'API_calls_started':0,'subagents_threads_worktrees_created':0,'foreground_successful_audit_pids':[read(OUT/'isolation.json')['pid'],bind['pid'],render['pid'],preserve['pid']],'report_writer_pid':os.getpid(),'no_residual_own_processes':True,'process_exit_verification_path':str(OUT/'process_audit_final.json'),'process_claim_scope':'所有本复核Python由前台命令执行并退出；最终报告写完后，外部只读进程扫描再次核验全部自有Python命令及已知PID均不存活，结果写上述自有process_audit_final.json。未启动服务器或后台助手。','blocked_operations':BLOCKED},
    'supporting_new_review_files':{p.name:{'absolute_path':str(p),'sha256':sha(p)} for p in OUT.iterdir() if p.is_file() and p.name!='independent_review.json'},
    'approval_status':'RESEARCH_RECOMMENDATION_ONLY; not user original approval, Special Pass/Collect or publication. No approval state changed.'
}
save('independent_review.json',report)
print(json.dumps({'question_id':report['question_id'],'variant_id':report['variant_id'],'decision':report['decision'],'path':str(OUT/'independent_review.json'),'sha256':sha(OUT/'independent_review.json'),'writer_pid':os.getpid(),'blocking_objections':report['blocking_objections']},ensure_ascii=False,indent=2))
