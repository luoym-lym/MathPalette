from review_bootstrap import *

e=read(OWN/'evidence_audit.json')
m=read(OWN/'independent_math.json')
r=read(OWN/'native_render_audit.json')
p=read(OWN/'precision_and_AA_audit.json')
a=read(OWN/'native_artist_audit.json')
elig=read(OWN/'eligibility_current.json')
docs=read(OWN/'documents_history_audit.json')

before=read(OWN/'read_only_baseline_manifest.json')['files']
after=inventory()
changes={name:{'before':item,'after':after.get(name)} for name,item in before.items() if item!=after.get(name)}
added=[name for name in after if name not in before]
assert not changes and not added
preservation={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'tracked_file_count':len(before),'tracked_byte_count':sum(x['size'] for x in before.values()),
 'changed_preexisting_files':changes,'new_files_in_tracked_source_roots':added,'all_tracked_hashes_and_mtimes_unchanged':True,
 'read_error_paths':[k for k,v in after.items() if 'read_error' in v],
 'scope':'Formal Plane427 inputs and dependencies; provenance; shared dataset tools and Plane workbench code; all background_41 evidence; all background_20 Plane427 evidence and background_20 root history; authoritative Plane Special indexes; root catalog; opaque .env hash and .git HEAD/index/config. Strict own-root Python write guard covers every other path as well. No whole-workspace immutability assertion is made.',
 'no_formal_or_prior_evidence_or_shared_helper_or_approval_or_global_ledger_write':True,
 'own_initial_housekeeping':'An overbroad read-only all-workspace baseline scan was stopped by verified owned PID 21832 and replaced with this 460-file relevant-source manifest before any project import. Its only operations were reads. The replacement and all subsequent Python work have finished as foreground commands; no solver was called.'}
write('preservation_final.json',preservation)

old_input=read(TASK/'background_20/Plane427/input_fingerprints.json')
old_matches={path:sha(PROJECT/path)==expected for path,expected in old_input['files'].items()}
old_mismatches={path:{'recorded':old_input['files'][path],'current':sha(PROJECT/path)} for path,ok in old_matches.items() if not ok}
old_check={'full_fingerprint_object_sha256':sha(TASK/'background_20/Plane427/input_fingerprints.json'),
           'files_count':len(old_matches),'mismatches':old_mismatches,'environment':old_input['environment'],'question_record_sha256':old_input['question_record_sha256']}
write('old_background20_input_check.json',old_check)

artifact_paths=[PROJECT/'PlaneGeometry/originals/Plane427.jpg',PROJECT/'PlaneGeometry/image/Plane427.png',PROJECT/'PlaneGeometry/dataset_generator/scenes/Plane427.json',
 CAND/'candidate.png',CAND/'plugin.json',CAND/'design.json',CAND/'design_difference_audit.json',CAND/'primary_review.json',CAND/'eligibility_immediately_before_calls.json',TEST/'binding.json']
artifacts={str(path):{'sha256':sha(path),'size_bytes':path.stat().st_size,'mtime_utc':datetime.fromtimestamp(path.stat().st_mtime,tz=timezone.utc).isoformat(),
                      'creation_time_utc':datetime.fromtimestamp(path.stat().st_birthtime,tz=timezone.utc).isoformat()} for path in artifact_paths}
for path in [CAND/'design.json',CAND/'plugin.json',CAND/'candidate.png',CAND/'design_difference_audit.json',CAND/'primary_review.json',CAND/'eligibility_immediately_before_calls.json']:
    assert path.stat().st_mtime < datetime.fromisoformat(e['two_runs'][0]['started_at']).timestamp()

markers=[]
roles=[
 {'name':'蓝色 ST','source_edge':['S','T'],'color':'#2563EB','linewidth_pt':2,
  'information':'ST 是原等边三角形的一边，也是绕 T 旋转的实际半径；它与 TV 组成真实等腰 STV 的两腰。只把一条腰改蓝不能清楚表达这一成对对应，ST 提供比较的原边。',
  'specific_use':'与第二条蓝边配对，突出可用于求底角 TSV 的等腰三角形。ST 与 SV 在 S 夹出的是中间角25°，并非题干所问的黑色 SR 与红色 SV 之间的角。',
  'validity':'TS=TV 已由原题的等边性和实际旋转推出。蓝色配对没有虚构等长、等角或新点。原边仍为实线，原 RS/RT 未改色。'},
 {'name':'蓝色 VT','source_edge':['V','T'],'color':'#2563EB','linewidth_pt':2,
  'information':'VT 是 ST 经实际同一旋转所得的边，构成比较的像边；与 ST 共享 T，准确闭合两个相等半径，而不是把 RT 错称为 TV 的原像。',
  'specific_use':'第二条腰确定顶角所在 T，并把原70°弧所在的 TV 射线纳入这组三角形。它与 ST 共同定位130°顶角，减少任意两条边被误作配对的可能。',
  'validity':'真正对应为 S→V、R→U、T→T。VT 的2pt蓝实线覆盖原 o1 最后一条边，TU、UV 继续黑色1pt，未改三角形位置或角度。'},
 {'name':'红色原点线 SV','source_edge':['S','V'],'color':'#DC2626','linewidth_pt':1.5,
  'information':'SV 是原图已给的点线，连接两条蓝腰的自由端，明确它们的共同基底；同时它是所求角 RSV 与中间角 TSV 的共同分界射线。',
  'specific_use':'给出成对半径比较所需的基底和在 S 处分角的边界，具有明确的组合用途；不是任意第三条显著线。它闭合的是早已存在的真实三角形 STV，没有新画边、切割或区域填充。',
  'validity':'保留实际原点线的1.0/1.65pt节距及相位，仅改变墨色/白名单宽度；未改实线，也未给目标角增加新弧或数值。精确 end=0.9999999999999999 留下约1.02e-13像素黑色尾段，无可见缺口。'}]
for index,role in enumerate(roles):
    binding=r['native_bindings'][index]
    markers.append({'action_index':index,**role,'target':binding['target'],'path_id':binding['interval']['path_id'],
                    'path_sha256':binding['actual_path_sha256'],'exact_interval':binding['interval'],
                    'frozen_scene_endpoints':[elig['original_content']['record']['id']] if False else [m['points'][name] for name in role['source_edge']],
                    'actual_native_path_endpoints':binding['selected_exact_endpoints'],
                    'conciseness_judgment':'保留此完整真实特征有明确表示用途，没有冗余自由线、重复弧或装饰标记。此用途判断不声称消融意义的因果必要性。',
                    'effectiveness_judgment':'信息对应清楚且与中间角/目标角区分有关；两次终答命中是另外核验的观察。没有据此声称该单一标记导致错误。'})

objections=[
 {'code':'OLD_UNIT20_FALSE_EQUALITY_CONCERN','status':'resolved_for_this_exact_candidate','finding':'已完整解码 background_20 的本题资料及根历史/完整终答汇总/检查点。本题旧状态为 screened_without_design，树中只有 assessment/context/eligibility/formal/input_fingerprints/original.png，没有候选、插件或求解调用。旧理由反对虚构等角等长，当前只配对确实满足 ST=TV 的半径，不是旧失败图换色。'},
 {'code':'TRUE_COMPARISONS_MAY_AID_CORRECT_PROOF','status':'nonblocking_limit','finding':'旧预筛认为真实对应会帮助正确证明，这个担忧成立为机制局限。当前三标记的真实信息角色足够具体，且正确解法仍清楚；既有两次 B25 仅满足规定的终答观察，并不证明此真实提示本身增加错误率。未把无控制或无因果增益另设为门槛。'},
 {'code':'INFORMATION_CONTENT_VS_GENERIC_SALIENCE','status':'resolved','finding':'逐一核对的具体内容是原半径、对应像半径、两自由端的原基底/目标分界线。三者是一组真实等腰角框架；不是只因配色合法或动作少就通过，也没有假定同色本身可作新数学公理。'},
 {'code':'TARGET_ARC_MISREAD_OR_EXTRA_CONDITION','status':'resolved','finding':'原S小弧确在 SV 与 SR 之间；25°中间角在 SV 与 ST 之间，没有新弧声称两者相等。两条原弧的路径、线宽、墨色、文字绑定均未动；所有S/T/R/U/V和70°在768原生画布清楚。错误把130°读成10°违反实际射线顺序，不构成合理另一解。'},
 {'code':'ACTUAL_MODEL_REASONING_DIFFERS_FROM_PRESET_HYPOTHESIS','status':'nonblocking_limit_and_factual_correction','finding':'两次都写 STV=70−60=10、TSV=85、RSV=85−60=25。未出现先正确求中间25再漏减的预设叙述。保留事前机制原文，不事后改成“诱导射线相减”，不声称中间角替代机制已证实。'},
 {'code':'RUN2_ROTATION_CORRESPONDENCE_ERROR','status':'corrected_nonblocking','finding':'run2的“RT对应TV”错误；实际 RT 对应 UT，ST 对应 VT。原题等边/全等仍使 RT=TV 为真，故这不使蓝色真实配对非法，也不影响独立唯一D35。'},
 {'code':'PRIMARY_RAY_NAMES_AT_T','status':'precision_correction_nonblocking','finding':'主审有“ST,RT,VT at T”的口头顺序写法；严格的有向射线应写 TS,TR,TV。当前独立向量角为177°,117°,47°，两邻角相加130°，主审数值结论正确。'},
 {'code':'PLANE242_PHYSICAL_PAPER_COLOR_OBJECTION','status':'not_applicable_as_blocker','finding':'已读其完整独立报告及任务语义教训。Plane242 要在图像选项中追踪移动纸片墨边，存在物理色边读法无正确图像的具体冲突。本题问数值角度，蓝 ST 也确实随同一旋转映到蓝 TV；红 SV 是原辅助基底。没有图像选项要求墨色消失/移动，颜色不会给出另一合法数值角度。此结论来自本题图文，不把作者“仅标注”意图当证明，也不外推任意色线禁令。'},
 {'code':'UNSELECTED_PIXEL_AND_CLOSING_JOIN_DIFFERENCES','status':'quantified_nonblocking','finding':'不能声称未选边所有像素完全不变。4046个变化像素中，3721在指定三条中心线4px内；外部325个都在原黑边2px内，其中322个仅灰阶1级变化，R点三像素为23/10/10级的闭合接点栅格变化。精确路径覆盖、线宽和连接保持，无第四条新改色边、断口、填充或新关系。详见 precision_and_AA_audit.json。'},
 {'code':'STALE_PRIMARY_RENDER_PENDING_FIELD','status':'nonblocking_stage_metadata','finding':'render_check.json 仍含 native_view_pending=true，是制图阶段字段；其后主审有实际查看记录。本次独立实际打开三张原生图并核验重放，因此没有把该旧字段或父级查看声明当作完成证明。'},
 {'code':'NO_OP_SOURCE_FILL','status':'resolved','finding':'来源JPG有灰色底，当前已批准正式PNG为无填充轮廓；候选保持当前正式PNG的填充表现。冻结场景中semantic_fill元数据未改，native before/after fills完全相同。没有把离线重绘冒充缺失来源，也没有要求候选恢复已批准重绘的历史样式。'}]

report={
 'question_id':'Plane427','variant_id':'r41_isosceles_base_angle_frame','decision':'recommended',
 'review_role':'全新独立二次复核；自行完成，未创建子代理、线程或工作树。',
 'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
 'approval_status':'RESEARCH_RECOMMENDATION_ONLY; 不是用户批准、Special Pass、Collect或special-complete。',
 'summary':'推荐此精确冻结候选作为研究变体。独立唯一答案D35；三处样式覆盖分别提供真实半径/对应半径/原基底的信息，简洁、原生可读且不产生合理另一数学解释。同一冻结PNG的两次完整终答确为事前预设B25。预设中间角替代机制未被正文证实，不能改写为射线相减诱导或宣称因果增益。',
 'decision_basis':[
  '先独立证明D35和核对真实图文，再判断三组标记的信息用途；合法配色和B/B都不是单独的通过理由。',
  '三个精确path intervals确实只改变原ST、VT、SV的颜色/白名单宽度，保留真实连接、原点线、原弧、黑文字及冻结视窗。两个完整renderer重放逐字节等于测试PNG。',
  '事前B预设与设计快照在两次调用前一致；两次独立run/response ID、HTTP200、stop、未截断、同一请求/PNG/设计hash，无输入泄漏。全任务已有证据扫描只找到这两次本题调用。',
  '无具体阻断异议。缺少原图control、统计/消融或机制因果确证如实记为非阻断局限，没有将它们升级为额外验收门槛。'],
 'blocking_objections':[],
 'formal_question':elig['formal_record']['question'],'formal_choices':elig['formal_record']['choices'],
 'correct_answer':{'letter':'D','degrees':35,'unique':True},'predeclared_wrong_answer':{'letter':'B','degrees':25},
 'independent_mathematics':m,'marker_group_reviews':markers,
 'native_visual_and_semantic_review':{
  'actually_opened_source_JPG_formal_PNG_exact_candidate_PNG':True,'view_detail':'original pixels; not a contact sheet or thumbnail',
  'opened_absolute_paths':[str(PROJECT/'PlaneGeometry/originals/Plane427.jpg'),str(PROJECT/'PlaneGeometry/image/Plane427.png'),str(CAND/'candidate.png')],
  'source_JPG_size':[670,463],'formal_and_candidate_size':[768,768],
  'human_unique_answer':True,'all_letters_and_70_text_native_readable':True,'S_target_arc_between_SR_and_SV_clear':True,
  'T_70_arc_between_TR_and_TV_clear':True,'all_six_text_boxes_identical_pixels':r['text_boxes_pixel_comparison'],
  'no_new_tick_angle_arc_relation_label_intersection_fill_or_cut':True,
  'human_interpretation':'∠RSV的顶点是S、两射线是SR与SV，原小弧正好绑定它。颜色框出的STV给出有用中间角，但没有替换所求角。25°作为答案必须忽视题干/原弧或犯实际角度关系错误；其不是同图同题的一种合理正确解。',
  'conciseness':'ST和TV各提供配对的一端，SV连接两自由端并形成目标分界射线；没有明显无用或混乱标记。没有设置任意动作数量上限，也不声称实验上逐条不可删除。',
  'physical_transform_check':'同一-130°旋转把蓝ST映为蓝TV，着色并未虚构对应。红色原SV不作为移动三角形的新边或物理纸片切口。数值角问题没有出现墨色追踪的选项矛盾。',
  'three_dimensional_geometry_projection_visibility':'不适用；本题二维坐标、视窗、原生线条、文字、弧和线型均冻结并核验。'},
 'render_and_precision':{k:v for k,v in r.items() if k not in ['changed_pixels_outside_4px_marked_segment_tubes','native_bindings']},
 'precision_qualification':{k:v for k,v in p.items() if k!='segmentation_coverage'},
 'existing_test_evidence':e,'two_complete_final_answers':e['two_runs'],
 'freeze_and_hash_binding':{'artifact_metadata':artifacts,'all_request_image_design_snapshot_start_run_raw_summary_SHA256':e['file_hashes'],
  'precalls_eligibility_checked_at':read(CAND/'eligibility_immediately_before_calls.json')['checked_at_utc'],
  'design_created_at':e['design_created_at'],'binding_created_at':e['binding_created_at'],
  'file_mtimes_for_plugin_png_design_primary_and_eligibility_precede_first_call':True,
  'later_supplement_not_used_as_predeclared_design':'full_precision_marker_bindings和primary_math_supplement是在调用后形成的审核材料；事前冻结由plugin/design/design_snapshot/request/start绑定证明。',
  'model_profile':e['profile'],'system_prompt':read(TEST/'binding.json')['system_prompt'],
  'solver_payload':'只有原system prompt + 正式题干/未改选项 + 精确candidatePNG；无答案字段、预设B、标注意图、历史、原图或control。题干中的原选择项不是答案泄漏。'},
 'history_and_old_objections':objections,
 'historical_source_checks':{'background41_adapter_files_checked':3416,'background41_all_3416_match_current':p['all_3416_path_hashes_match'],
  'background41_preservation_manifest':{'recorded_files':3523,'current_hash_mismatches':docs['historical_hash_checks'][str(TASK/'background_41/source_hashes_before.json')]['mismatches']},
  'background20_full_input_check':old_check,
  'old_Plane427_candidate_calls':0,'new_frozen_candidate_calls':2,'controls_found':0,
  'full_task_scan_counts':{k:e['full_task_scan'][k] for k in ['files_visited','binding_files_fully_parsed','request_files_fully_parsed','unique_call_count','scan_errors']},
  'reference_review_paths':[str(path) for path in docs['reference_lessons']],
  'reference_policy':'参照batch13和Solid128/Solid197/Plane192/Plane233的证据局限处理方式，仍按本题实际图文判断；未因其他题推荐而自动推荐，也未照搬其他题的拒绝理由。',
  'complete_read_receipts_file':str(OWN/'documents_history_audit.json')},
 'current_eligibility':elig,
 'nonblocking_limitations':[
  '原图control不存在，未新增。无法宣称相对原图增加错误、正确率下降、统计稳健性或因果增益。',
  '两次确实终答B25，但正文实际是错误的角相减/射线顺序。预设“先正确中间25再漏减”机制未被证实；设计原文保留，未事后更换机制或预设。',
  '蓝边和红基底有真实具体信息用途；这不等于其诱导效果或每一条的因果必要性已被验证。未做新消融/人群研究；未将此另设硬门槛。',
  '本次原生可读、人类无歧义属于独立图文判断，不是人群测验。',
  '局部重绘存在已精确分类的AA/接点微差及浮点尾段，未声称未选像素完全一致；无几何、原弧、文字、线型、填充或目标改变。',
  '哈希和内部/文件/响应时间证明现存材料的一致性，不能排除未保存或删除的外部调用，也不是外部可信时间戳或提供商账户审计。',
  '只读核验限定于明列源/证据；严格写入guard涵盖其余项目路径。并行无关工作保留，不恢复任何旧全局日志或分数。'],
 'source_readonly_verification':preservation,
 'workspace_process_discipline':{
  'own_new_output_root':str(OWN),'strict_own_directory_guard_before_project_imports':True,
  'TEMP_TMP_MPLCONFIGDIR_XDG_CACHE_HOME_inside_own_root':True,'all_python_invoked_with':'python -X utf8 -B',
  'runtime_isolation_in_memory_only':a['runtime_routing'],'network_and_child_process_execution_blocked_in_review_Python':True,
  'new_solver_calls':0,'new_control_retry_or_design_modification':False,'subagents_threads_worktrees_created':0,
  'no_approval_Pass_Collect_or_publication_action':True,'all_rendered_figures_closed':r['all_figures_closed'],
  'no_server_or_background_helper_started':True,'final_external_process_audit_path':str(OWN/'process_audit_final.json'),
  'final_external_check_runs_after_this_foreground_writer_exits':True},
 'supporting_new_artifacts':{}
}
for path in sorted(OWN.glob('*')):
    if path.is_file() and path.name not in ['independent_review.json','process_audit_final.json']:
        report['supporting_new_artifacts'][path.name]={'absolute_path':str(path),'sha256':sha(path)}
write('independent_review.json',report)
write('report_validation.json',{'question_id':report['question_id'],'variant_id':report['variant_id'],'decision':report['decision'],
      'report_sha256':sha(OWN/'independent_review.json'),'full_raw_contents_match':all(run['full_assistant_content']==read(Path(run['raw_response_path']))['choices'][0]['message']['content'] for run in report['two_complete_final_answers']),
      'exactly_two_complete_finals':len(report['two_complete_final_answers'])==2,'current_eligibility':elig['eligible'],'source_manifest_changes':len(changes),
      'no_new_solver_calls':True,'foreground_writer_pid':os.getpid()})
print(json.dumps({'decision':report['decision'],'report':str(OWN/'independent_review.json'),'report_sha256':sha(OWN/'independent_review.json'),
                  'source_changes':len(changes),'old_input_mismatches':len(old_mismatches),'writer_pid':os.getpid()},ensure_ascii=False))
