from audit_bootstrap import *
from PIL import Image

ev=read(OWN/'evidence_audit.json')
geo=read(OWN/'render_and_geometry_audit.json')
elig=read(OWN/'authoritative_eligibility.json')
design=read(CANDIDATE/'design.json')
plugin=read(CANDIDATE/'plugin.json')
before=read(OWN/'read_only_inputs_before.json')
assert ev['all_checks_passed'] and geo['all_checks_passed'] and elig['eligible']
changes=[]
after_files={}
for rel,info in before['files'].items():
    p=ROOT/rel
    current=sha(p) if p.is_file() else None
    after_files[rel]={'sha256':current,'same_as_review_start':current==info['sha256']}
    if current!=info['sha256']: changes.append({'path':rel,'before':info['sha256'],'after':current})
assert not changes, changes
preservation={'checked_at':now(),'scope':before['scope'],'review_start_manifest_sha256':sha(OWN/'read_only_inputs_before.json'),'files_checked':len(after_files),'changes':changes,'all_scoped_inputs_unchanged':not changes,'after_files':after_files,'whole_shared_workspace_unchanged_claim':False,'unrelated_concurrent_changes':'Preserved. No restoration, attribution, git reset or catalog/workbench writes. Shared mutable exploration and remaining-question metadata are diagnostic, not frozen geometric inputs.'}
write('read_only_inputs_after.json',preservation)

record=elig['formal_record']
source_path=ROOT/'SolidGeometry'/record['original_image']
formal_path=ROOT/'SolidGeometry'/record['image']
candidate_path=CANDIDATE/'candidate.png'
viewed=[]
for purpose,p in [('source_original_jpg',source_path),('formal_native_png',formal_path),('frozen_tested_candidate_native_png',candidate_path)]:
    with Image.open(p) as img:
        viewed.append({'purpose':purpose,'absolute_path':str(p),'sha256':sha(p),'size':list(img.size),'mode':img.mode,'actually_opened_with_image_tool':True,'inspection':'Opened independently at original image resolution in this review; source JPG and both full 768px PNGs were visually inspected, not inferred from summaries.'})

front=geo['paths_and_styles']['front_top']
ret=geo['paths_and_styles']['return_inner_top']
marker_groups=[
    {
        'group_id':'M1_outer_front_corner_including_run',
        'target':'front_top',
        'action':plugin['params']['actions'][0],
        'world_endpoints':[[0,0,1],[5,0,1]],
        'projected_endpoints_ideal':[[0,1],[5,-0.4]],
        'actual_native_path':front['path_description'][0],
        'targeting':{'judgment':'specific_as_source_member_of_pair','finding_zh':'取前墙外侧上棱作为分摊墙块的参照，完整保留并突出角块沿 x=0..1 的那一段；第二条红边从本棱的第一处分缝 x=1 出发，形成可见的角块归属对比。不是给整个题图、整片区域或所有边统一着色。'},
        'validity':{'judgment':'valid','finding_zh':'该棱在来源图及冻结场景中实际存在且可见；只从原黑色 1pt 改为红色 1.5pt，端点、几何、分缝和实线均未变。它是外侧边，不应被解释为内部空区边长。'},
        'effectiveness':{'judgment':'useful_component_with_pair_level_two_hit_evidence','finding_zh':'使包含角块的外边参照可被同色的内偏回边接收；实际两次回答均出现 36/4=9 再平方的预设错误。未做单标记消融，不能把单独这一动作的因果效果视为已证实。'},
        'concision':{'judgment':'concise','finding_zh':'仅一个已有连续边的样式动作，无数字、箭头、重复描边对象或额外线。全边着色保留其连续边身份，角色由角块一格与第一分缝确定；不要求它本身显示 9 个单位。'},
        'human_unambiguity':{'judgment':'unambiguous_for_original_numerical_task','finding_zh':'正常 768px 尺寸下红边约 2.08px 宽，前墙各竖分缝和底边仍清楚。即使把红色视为墙棱油漆，也不改变立方体数量、边界占据或填充目标；没有把红边作为等长或新墙边界的题设。'}
    },
    {
        'group_id':'M2_inward_offset_return_receiver',
        'target':'return_inner_top',
        'action':plugin['params']['actions'][1],
        'world_endpoints':[[1,0,1],[1,2.7,1]],
        'projected_endpoints_ideal':[[1,0.72],[3.43,1.665]],
        'actual_native_path':ret['path_description'][0],
        'targeting':{'judgment':'specific_receiver_at_one_cube_offset','finding_zh':'该回边位于 x=1，而未着色的外回边位于 x=0；两者相距一立方体厚度。它从前墙第一处分缝 (1,0,1) 出发，在 (1,1,1) 越过已有后沿后进入内侧回边，把角块外参照与内偏一格的垂直方向联系起来。'},
        'validity':{'judgment':'valid_with_precise_segment_role','finding_zh':'整条是已有可见棱/格缝路径；y=0..1 这一单位先跨过前墙顶面，y>=1 才是回墙面向内部空区的上边。因此不能把整条均称为内部空区边界，也不能把 2.7 当成完整方墙尺寸。样式覆盖未补画隐藏边、延长线或新角点。'},
        'effectiveness':{'judgment':'useful_receiver_with_pair_level_two_hit_evidence','finding_zh':'给第一条外侧参照提供了可识别的同色接收对象，具体诱导角块分摊所得 n-1 与内部边长 n-2 混同。两次完整回答都发生了该数值混同，但均未提到红色；已观察到的 81/81 不能证明模型实际注视或使用了本标记。'},
        'concision':{'judgment':'concise','finding_zh':'一个已有开放路径的样式动作；没有添加闭合内方形、完整围墙、尺寸或求解文字。它与前红边的 T 形连接直接显示一格错位，角色区别于泛化全轮廓强调。'},
        'human_unambiguity':{'judgment':'unambiguous_for_original_numerical_task','finding_zh':'黑色外回边、顶面单位格和内侧竖线片段保持可见，约 343px 的红路径端点可分辨。红色路径开放且与第一条形成 T 形，不是新方形或新的固定分割。共同颜色表达注意力对应，不构成等长、等量、平行或角度标记。'}
    }
]

old=BASE/'background_15/Solid128'
history=read(BASE/'background_35/history_read_audit.json')
old_manifest=next(x for x in history['all_previous_same_question_files_read_in_full'] if x['question_id']=='Solid128')
old_objections=[
    {'origin':str(old/'primary_prescreen.json'),'old_objection':'Generic inner-versus-outer rim emphasis lacked a second visual receiver or a specific unambiguous partial-feature correspondence.','new_design_check_zh':'本次实际存在两个不同位置的具体对象：含角块的前外边和偏入一格的回边；它们在第一分缝 (1,0,1) 相接，并在内角 (1,1,1) 与黑后沿相交。以同色将外边计数参照与内侧接收对象绑定，角块差一格的可见特征确实存在。','disposition':'resolved_for_this_new_design','limit_zh':'两个回复没有叙述颜色或角块接收过程，故对应机制属于有几何依据的设计解释，不能据此声称已证实因果机制。'},
    {'origin':str(old/'primary_prescreen.json'),'old_objection':'Do not add extension boundaries implying a different fixed square.','new_design_check_zh':'核对两条原路径、全部 18 个原线对象及真实候选，仅修改两条样式。0 个新点、0 条新线；原图开放端头与不同长度的截取段全部保留；没有远端闭合线、内方形、中心线或尺寸。','disposition':'resolved'},
    {'origin':'Assignment brief: prior Plane233 fixed-partition rejection','old_objection':'New closed source contours implied incompatible fixed partitions.','new_design_check_zh':'两条着色路径均开放，组合为 T 形，没有产生新的闭合轮廓或切割。原有立方体顶面闭合格子仍是原有格子，不被一概禁止，也不被解释成新区域。全体差异像素均位于原有两条描边范围内。','disposition':'not_reproduced_in_this_variant'},
    {'origin':str(BASE/'annotation_semantics_lessons_20261102.json')+' / Plane295','old_objection':'Colored ear boundaries could be intrinsic source content and change a drawing-completion answer; a small diagnostic distinction was weakened.','new_design_check_zh':'本题要求数值填充数量，不要求图案补全。把两条红棱当作真实油漆，单层一格厚方墙和空区均不变；黑外回边与分缝仍清楚，没有抹掉诊断区别。','disposition':'not_reproduced_in_this_variant'},
    {'origin':str(BASE/'annotation_semantics_lessons_20261102.json')+' / Plane342','old_objection':'A literal physical printed-card transformation transports red ink and changes/no longer matches the answer options.','new_design_check_zh':'本题无纸卡旋转、印刷图案搬运或需要保持油墨的选项匹配。油漆与批注两种自然读法都得到同一个空区计数 64；没有需要从数学对象中删去红墨才能得到答案的条件。','disposition':'not_reproduced_in_this_variant'},
    {'origin':'Assignment brief and annotation semantics rule','old_objection':'Schema-valid color or whole-choice salience alone is insufficient; each mark needs an informational role.','new_design_check_zh':'独立检查了一格墙厚、含角块的外边、内偏回边及两处真实交点，证明这里有具体外侧计数到内侧边长的混同对象，而非泛化强调。白名单合规与该语义判断分别记录。','disposition':'satisfied_by_actual_feature_correspondence'}
]

corrections=[
    {'source':str(CANDIDATE/'primary_review.json'),'field':'visual_findings','original_claim':'The red crossing on the wall top is a preexisting projection crossing, no new spatial intersection is introduced.','independent_correction_zh':'“仅投影交叉”不准确。front_top 与 return_inner_top 在 (1,0,1) 真实相接；return_inner_top 与 front_rear_top 在 (1,1,1) 真实相交，后者投影为 (1.9,1.07)。相关路径全部处在 z=1 顶面，不能用二维投影偶遇解释。','effect_on_decision':'nonblocking','reason_zh':'这些真实交点均在原来源/冻结场景中已有，候选没有新增交点或关系；纠正反而使角块一格错位的位置更明确。冻结证据保持原样。'},
    {'source':str(CANDIDATE/'design.json'),'field':'marker_roles / return_inner_top','original_claim':'Actual inward upper edge of the perpendicular return, anchored one cube inward.','independent_correction_zh':'作为简称可用，但整条路径不是纯粹的内空区边：x=1、y=0..1 的段先跨前墙顶面；y>=1 才沿回墙内侧上边。起点 (1,0,1) 沿前外边离外角一单位，而实际内角在 (1,1,1)。','effect_on_decision':'nonblocking','reason_zh':'路径恰为原有连续特征，精确分段解释支持角块归属机制，不改变唯一答案或任何像素。报告不把它写成完整内方形边长。'}
]

protocol_paths=[ROOT/'AGENTS.md',ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'SolidGeometry/REDRAW_PROTOCOL.md',ROOT/'SolidGeometry/dataset_generator/protocol.json',ROOT/'SolidGeometry/workbench/README.md',ROOT/'SolidGeometry/workbench/agent_prompt.md',ROOT/'SolidGeometry/workbench/plugin.schema.json']
key_paths=[source_path,formal_path,ROOT/'SolidGeometry'/record['scene'],CANDIDATE/'candidate.png',CANDIDATE/'plugin.json',CANDIDATE/'design.json',CANDIDATE/'design_difference_audit.json',CANDIDATE/'primary_review.json',CANDIDATE/'marker_geometry_audit.json',CANDIDATE/'render_check.json',CANDIDATE/'evidence_binding_audit.json',CANDIDATE/'manual_final_review.json',CANDIDATE/'context.json',QUESTION/'scene_snapshot.json',QUESTION/'input_fingerprints.json',QUESTION/'source_notes.json',BASE/'Solid128_r35_corner_ownership_mixed_rims_pre_review_evidence_check.json']
hash_bindings={str(p):sha(p) for p in key_paths}
hash_bindings.update({str(ROOT/rel):v['sha256'] for rel,v in ev['raw_evidence_and_design_files'].items()})
process=read(OWN/'process_audit.json')
assert process['remaining_count']==0

report={
    'schema_version':'1.0.0',
    'question_id':'Solid128',
    'variant_id':'r35_corner_ownership_mixed_rims',
    'branch':'SolidGeometry',
    'decision':'recommended',
    'review_kind':'fresh_independent_second_research_review',
    'reviewed_at_utc':now(),
    'decision_reason_zh':'推荐作为研究候选保留：原题由实际单层一格厚墙段及全局 36 块唯一推出 64；同一冻结候选和预设 81 的两次真实完整调用均以 81 结束；两条原棱标记在角块处构成具体的外侧计数/内偏边长对应，正常尺寸可读，无新增固定方形或竞争数学读法。主审的交叉与内边简称两处不精确措辞已独立纠正，不构成设计、证据或答案缺陷。',
    'approval_status':{'research_recommendation_only':True,'user_approval_recorded':False,'formal_state_approved':False,'Pass':False,'Collect':False,'publication':False},
    'independence':{'complete_assignment_brief_read':True,'parent_conclusions_not_used_as_proof':True,'actual_source_and_candidate_opened':True,'formal_full_question_and_both_complete_raw_replies_read':True,'proof_and_geometry_recomputed':True,'nested_agents_or_threads_or_worktrees':0,'new_solver_calls':0,'retries_or_design_changes':0},
    'original_problem':{'formal_question_full':record['question'],'upstream_question_full':read(QUESTION/'source_notes.json')['original_record']['question'],'source_dataset':record['source_dataset'],'source_key':record['source_key'],'answer_type':'number','unique_correct_answer':'64','formal_answer_crosscheck':record['answer'],'expected_wrong_answer_frozen':'81','formal_question_utf8_sha256':hashlib.sha256(record['question'].encode('utf-8')).hexdigest(),'formal_record_canonical_sha256':elig['formal_question_record_canonical_sha256']},
    'unique_correct_answer':'64',
    'expected_wrong_answer':'81',
    'independent_mathematical_proof':{
        'basis_zh':'题干给定完整方形区域周围共 36 个相同立方体；实际来源图与正式重绘图显示单层、一块宽的直角墙段。图只是 section，未画出完整封闭方墙。',
        'steps_zh':[
            '令完整方墙外侧每边含 n 个单位立方体，n>=3。四条含两端角块的完整边各有 n 块，四个角块各被重复计入一次，故墙块总数为 4n-4；也可按四角 4 块加四边各 n-2 块计为 4+4(n-2)。',
            '4n-4=36 唯一得 n=10。墙厚两侧各占一单位，因此内部空区每边为 n-2=8，而不是 n-1=9。',
            '填至一块高、与原墙同高的正方形空区需要 (n-2)^2=8^2=64 个新增立方体。验证：10^2-8^2=100-64=36；另以四个内侧条带 4m 加四角 4 得 4m+4=36、m=8。',
            '若把 36 平均分给四个“只拥有一个角块”的边组，每组 9=n-1；这只是半开分组计数或墙中心线的边长，不是内部空区边长 n-2。把 9 平方得到 81 正是预设错误。若内部真为 9×9，则外边须 11，墙块应为 4×11-4=40，与 36 冲突。'
        ],
        'uniqueness_zh':'方形、单层、单块厚的原题解释下，墙块数关于外边长为严格递增的 4n-4，方程只有 n=10，故填充数唯一为 64。无需从存储答案倒推。',
        'clipped_lengths_not_givens_zh':'冻结坐标里的前段长 5、回边终点 2.7、外回边 2.35 及稀疏续线都是来源示意图的显示截取参数，不是完整边长或有限多立方体的总数；没有以这些显示参数解题。',
        'primary_count_proof_verdict':'The primary 4n-4 and (n-2)^2 proof is mathematically correct. No answer correction required. Geometric wording corrections are listed separately.',
        'independent_lattice_crosscheck':geo['independent_lattice_count']
    },
    'actual_visual_inspection':{'viewed_files':viewed,'native_size_human_judgment_zh':'原图 349×255 可读出前墙单层、顶面一格宽和回墙；两幅 768×768 图保留所有分缝与开放续线。候选仅两条细红边，黑外回边与墙厚仍明显；没有标签遮挡、消失的单位格、答案文字或新尺寸。','source_gray_shading_zh':'来源 JPG 的灰色前面在正式重绘中已依单色协议移除；这是已冻结原题的渲染规则，候选没有新增或改变填充。','native_layout_bbox':geo['raster']['all_ink_bbox_inclusive'],'red_stroke_nominal_width_px':geo['raster']['nominal_marked_stroke_width_px'],'all_other_original_strokes_unchanged':True},
    'marker_group_reviews':marker_groups,
    'joint_marker_semantics':{
        'targeting_verdict':'specific_corner_ownership_correspondence',
        'mechanism_zh':'第一红边保留角块 x=0..1；第二红边相对黑外回边 x=0 内偏到 x=1，并从第一分缝起穿过前墙一格顶面。两者同色将外边计数与内侧边长放在同一注意力组，具体诱发把 36/4=9 的角块归属分摊数转用于内部空区。它不声称图中存在 9 个可直接读出的单位。',
        'new_region_or_cut':'none',
        'new_square_boundary_or_closing_segment':'none',
        'new_dimension_or_numeral_or_text':'none',
        'new_equal_length_or_parallel_or_angle_condition':'none',
        'new_cube_or_changed_wall_membership':'none',
        'world_geometry_projection_frozen_visibility_changes':'none',
        'existing_closed_cube_faces_zh':'原有封闭顶面格并未消失或新增；标记开放不意味着禁止原有格子轮廓。',
        'paint_vs_annotation_reading_zh':'本题是围墙数值计数。将红线解释为真实棱上的涂漆或事后注意力标注，都不改变几何占据或填充目标，均唯一为 64。不存在必须忽略红墨才可解、或保留红墨就无答案的图案转移问题。',
        'shared_hue_zh':'共同红色可以合理引导比较和混同，但没有等长刻痕、平行箭头、端帽或尺寸文字，且两条显示段长度不同、均被题干说明为 section；不能把共同颜色提升为新增相等题设。',
        'human_unambiguity_verdict':'satisfied_by_wording_actual_topology_and_visible_unit_thickness',
        'concision_verdict':'Both actions have source/receiver roles; no unused mark or artificial numeric mark cap.',
        'observed_effectiveness_verdict':'Same frozen image produces two complete preset hits, 81 and 81; causal/per-marker attribution remains untested.'
    },
    'old_objections_rechecked':old_objections,
    'material_difference_audit':{'old_prescreen_status':'screened_out_without_saved_plugin_candidate_or_calls','old_prescreen_file':str(old/'primary_prescreen.json'),'old_prescreen_sha256':sha(old/'primary_prescreen.json'),'old_same_question_independent_reviews':history['independent_same_question_objections'],'old_file_manifest_checked':old_manifest['old_files'],'all_old_files_unchanged':ev['checks']['all_historical_Solid128_evidence_hashes_unchanged'],'finding_zh':'旧资料仅有泛化内外边着色的预筛设想，没有可供复测或微调的旧候选图、插件或测试。新设计在测试前具体固定两条边、端点与错误角块分摊映射；因此在现存证据范围内是实质新设计，而非旧失败图的配色重试。','new_difference_audit_sha256':sha(CANDIDATE/'design_difference_audit.json')},
    'primary_claims_independently_corrected':corrections,
    'two_hit_evidence_audit':{'all_checks_passed':ev['all_checks_passed'],'check_results':ev['checks'],'profile':'quicktest3','provider_response_model':'mimo-v2.6-flash','thinking':{'type':'disabled'},'reasoning_tokens':[0,0],'exact_request_sha256':sha(TEST/'request.json'),'request_contents':ev['request_structure_without_redundant_base64'],'preset_frozen_before_calls':True,'chronology_utc':ev['chronology_utc'],'design_snapshot_byte_identical':True,'base64_image_byte_identical':True,'completed_candidate_calls':2,'complete_final_values':['81','81'],'both_match_same_preset':True,'no_contradictory_terminal_letter_or_value':True,'both_full_run_records_and_raw_responses_manually_read':True,'complete_responses':ev['complete_manually_read_responses'],'no_retry_or_selection_found_in_available_evidence':True,'all_available_same_question_bindings':ev['all_available_Solid128_bindings'],'original_control_calls':0,'parent_binding_check_role':'Supplemental only; all bindings and raw responses independently verified.','narrative_limits_zh':'两次回复都把 36 块直接当作 4s、得到 s=9，再算 81，符合预设错误；没有提红色、没有把同色作为等长题设、没有矛盾的终值或选项。第一份回复称墙包在外侧但仍漏算角块，第二份把“方墙一圈的块数”等同内部周长，均属错误推理而非新合法答案。第二次缓存了 640 个提示 token；完全相同请求没有包含第一次助手回答。'},
    'exact_hash_bindings_sha256':hash_bindings,
    'image_pixel_hashes':{'formal_native_png':geo['baseline_pixel_sha256'],'candidate_png':geo['candidate_pixel_sha256'],'algorithm':'SHA256 of ASCII widthxheight:RGBA: prefix plus RGBA bytes'},
    'formal_source_protocol_renderer_hash_recheck':ev['frozen_input_hash_checks'],
    'frozen_render_replay':{'checks_passed':geo['all_checks_passed'],'candidate_replay_bytes_identical':True,'baseline_no_op_pixels_equal':True,'all_changed_pixels_in_original_target_strokes':True,'changed_pixel_count':geo['raster']['changed_pixel_count'],'maximum_changed_pixel_center_distance_to_target_px':geo['raster']['max_changed_pixel_center_distance_from_either_existing_target_px'],'appearance_changes':geo['appearance_changes'],'open_matplotlib_figures_after_close':geo['figure_numbers_after_close'],'environment':geo['environment'],'note':'Read-only rendering and arithmetic verification, not new model/control testing.'},
    'authoritative_current_eligibility':elig,
    'protocols_read_in_full':[{'path':str(p),'sha256':sha(p)} for p in protocol_paths],
    'objections':{'blocking':[],'nonblocking_factual_corrections':corrections,'frozen_evidence_repairs_performed':False},
    'limitations_zh':[
        '没有原图模型对照；不宣称候选相对原图提高错误率，用户也未要求以原图对照正确作为门槛。',
        '只有同一冻结图的两次正常完成响应；不外推总体命中率、统计显著性、跨模型稳定性或人类错误率。',
        '没有人类实验、逐标记消融或因果研究；单个标记的作用依实际几何与语义论证，两次回复不能证明红边导致了错误。',
        '图为墙段，不是完整方墙。未把截取长度 5 或 2.7、续线位置或可见块数当成完整尺寸；标记没有直接画出 9 个单位。',
        '审核可核验本地原始请求、响应、模型标识、时间与哈希，不持有提供商服务端传输审计或密码学签名；未发现重试/选样的结论限定于现有冻结证据和同题 runtime 扫描。',
        '正常尺寸无歧义属于本次独立审阅判断，不是用户审批或人类群体实验。'
    ],
    'read_only_preservation':{'checked_files':preservation['files_checked'],'all_scoped_inputs_unchanged':True,'manifest_before':str(OWN/'read_only_inputs_before.json'),'manifest_before_sha256':sha(OWN/'read_only_inputs_before.json'),'manifest_after':str(OWN/'read_only_inputs_after.json'),'manifest_after_sha256':sha(OWN/'read_only_inputs_after.json'),'entire_shared_workspace_unchanged_claim':False,'unrelated_changes_restored_or_modified':False,'write_scope':str(OWN),'shared_runtime_isolation_installed_before_project_analysis':True,'strict_own_directory_guard_installed_before_project_imports':True,'network_guard_enabled':True,'env_git_dot_runtime_formal_state_modified':False},
    'process_cleanup':{'background_processes_started':0,'servers_started':0,'solver_processes_started':0,'owned_worker_processes_remaining_at_foreground_check':process['remaining_count'],'process_audit':str(OWN/'process_audit.json'),'process_audit_sha256':sha(OWN/'process_audit.json'),'process_audit_time':process['checked_at_utc'],'matplotlib_figures_remaining':geo['figure_numbers_after_close'],'execution_model':'All Python audit commands run synchronously and exit; this report writer is also foreground only. No unrelated process was killed.'},
    'auxiliary_evidence':[{'absolute_path':str(OWN/n),'sha256':sha(OWN/n)} for n in ['isolation.json','authoritative_eligibility.json','evidence_audit.json','render_and_geometry_audit.json','read_only_inputs_before.json','read_only_inputs_after.json','process_audit.json','reproduced_original.png','reproduced_candidate.png']],
    'report_absolute_path':str(OWN/'independent_review.json')
}
assert report['decision'] in ('recommended','hold','reject')
assert [x['manual_final_value'] for x in report['two_hit_evidence_audit']['complete_responses']]==['81','81']
write('independent_review.json',report)
parsed=read(OWN/'independent_review.json')
assert parsed==report
assert all(sha(Path(p))==h for p,h in report['exact_hash_bindings_sha256'].items())
print(json.dumps({'decision':report['decision'],'correct_answer':report['unique_correct_answer'],'preset':report['expected_wrong_answer'],'complete_final_values':report['two_hit_evidence_audit']['complete_final_values'],'formal_input_hash_count':len(ev['frozen_input_hash_checks']),'evidence_checks':len(ev['checks']),'geometry_render_checks':len(geo['checks']),'unchanged_readonly_files':len(after_files),'report_path':str(OWN/'independent_review.json'),'report_sha256':sha(OWN/'independent_review.json'),'report_size':(OWN/'independent_review.json').stat().st_size,'blocking_objections':0,'nonblocking_factual_corrections':len(corrections)},ensure_ascii=False,indent=2))
