from review_env import *
from dataset_tools.catalog import content, digest

before=read(OWN/'read_only_before.json')
after={p:{'sha256':fh(ROOT/p),'size':(ROOT/p).stat().st_size} for p in before['files']}
changes={p:{'before':before['files'][p],'after':after[p]} for p in after if before['files'][p]!=after[p]}
write('read_only_after.json',{'at':now(),'files':after,'changes':changes,'all_tracked_files_unchanged':not changes,
    'scope':'334 exact source, formal dependency, protocol, approval/index and preexisting evidence files; no assertion about unrelated concurrent workspace changes.'})
evidence=read(OWN/'evidence_audit.json')
native=read(OWN/'native_render_pixel_audit.json')
proof=read(OWN/'independent_math_proof.json')
eligibility=read(OWN/'eligibility_current.json')
record=next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid230')
approval=read(ROOT/'provenance/approvals.json')['approvals']['Solid230']
assert digest(content(ROOT,'SolidGeometry',record))==approval['content_sha256']==eligibility['independently_computed_content_sha256']
assert not any(r.get('question_id',r.get('id'))=='Solid230' for name in ['accepted_index.jsonl','collected_index.jsonl'] for r in rows(ROOT/'SolidGeometry/special_variant'/name))
assert not (ROOT/'SolidGeometry/special_variant/Solid230/recipes.json').exists()
assert not (ROOT/'SolidGeometry/special_variant/Solid230/collection.json').exists()
assert evidence['all_checks_pass'] and eligibility['eligible'] and not changes
required_native={k:v for k,v in native['checks'].items() if k!='noop_bytes_exact_formal'}
assert all(required_native.values())
containers=read(OWN/'noop_png_container_audit.json')
formal_chunks=containers['formal']['chunks'];noop_chunks=containers['noop']['chunks']
assert containers['formal']['inflated_IDAT_sha256']==containers['noop']['inflated_IDAT_sha256']
assert [c for c in formal_chunks if c['type']!='tEXt']==[c for c in noop_chunks if c['type']!='tEXt']
write('acceptance_checks.json',{'at':now(),'required_evidence_checks':evidence['checks'],'required_native_checks':required_native,
    'all_required_checks_pass':True,'source_preservation_pass':not changes,'current_eligibility_rechecked_at_report':True,
    'optional_diagnostic':{'noop_bytes_exact_formal':False,'blocking':False,
        'resolution':'Only PNG Software tEXt metadata differs; IHDR, pHYs, IDAT and IEND chunks match, as do all RGBA pixels. Protocol requires no-op pixel identity, which passes. Tested candidate replay matches bytes exactly.'}})

markers=[]
group_details=[
    {
        'group_id':'top_value1_face_anchor',
        'visible_face':'Top die, top face z=3, normal (0,0,1), 1 dot at (0.5,0.5,3).',
        'targeting_zh':'line_10 是顶骰 1 点顶面的真实后缘，处在可见顶面与外部白底之间；它不属于顶骰正面的 2 点面或右面的 3 点面。只把这一条外缘标红，使读者能定位要与底层 1 点面比较的第一个实际面。',
        'usefulness_zh':'提供等值比较的第一个面身份锚点。开放单边保留该面四边原有轮廓和中央 1 点，不必涂满或圈住面；与另一红边合起来，显示题中相同点值可出现在不同骰子的不同方向面上。',
        'concision_zh':'一条原有实线的颜色与白名单 2 pt 宽度覆盖；没有新的线、点、文字、等长记号或闭合框。没有无用途的额外边。',
        'clarity_zh':'顶面轮廓和中央点在 768×768 原生图中清楚，红边离最近点中心超过 45 px；它不延伸到中层 6 点面，也不把两面连成一个对象。'
    },
    {
        'group_id':'bottom_value1_face_anchor',
        'visible_face':'Bottom die, right face x=1, 0<=z<=1, normal (1,0,0), 1 dot at (1,0.5,0.5).',
        'targeting_zh':'line_2 是底骰右侧 1 点面的真实下缘，处在可见右面与外部白底之间；没有把底骰正面 5 点面的底边标红，也没有触及中骰右面。它定位第二个真实 1 点面，所选值与顶面相同但骰子、法向和位置不同。',
        'usefulness_zh':'提供重复值的第二个独立面身份。两条共同红色构成面值比较组，比较对象正好是七个可见面中仅有的两个 1 点面，而不是两个任意边或整图轮廓。单独保留其中一条就不再完整表达这对重复值参照；这是表示用途判断，不是消融因果结论。',
        'concision_zh':'只覆盖一条现有实线，2 pt 合法；不补面、不增隐藏边、不连接两红边，也不改 1 点的大小、位置或颜色。',
        'clarity_zh':'右侧面的上下斜边及竖边仍完整，底骰与中骰分界仍清楚；红下缘没有遮住中央点，没有产生第二个点或把边解释为点。'
    }
]
for technical,semantic in zip(native['markers'],group_details):
    markers.append({**technical,**semantic,'information_targeting':'sufficient','validity':'pass','concision':'pass','native_readability':'pass','human_unique_semantics':'pass',
        'path_binding':'Whole original segment object; interval omitted, so no partial-path id/hash applies. Exact original object geometry SHA256 and endpoints above identify the full path.'})

primary_caution=read(CAND/'primary_review.json')['information_targeting_caution']
history=read(OWN/'history_primary_exact_excerpts.json')
held=next(n['content'] for n in history['runtime/mathvision_special_20261101/background_37/second_review_queue.json'] if n['pointer'].startswith('$.held_numeric_two_hits'))
old_assessment=history['runtime/mathvision_special_20261101/background_13/checkpoint.json'][0]['content']
hash_paths=set()
hash_paths.update(ROOT/p for p in read(SHARED/'background_37/Solid230/frozen_inputs.json')['files'])
hash_paths.update(p for p in (SHARED/'background_37/Solid230').rglob('*') if p.is_file())
hash_paths.update(p for p in (SHARED/'background_13/Solid230').rglob('*') if p.is_file())
hash_paths.update(ROOT/p for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/quick_test.py','SolidGeometry/dataset.jsonl','question_bank.jsonl','provenance/approvals.json','provenance/source_notes.json','SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl'])
hash_paths.update(SHARED/p for p in ['background_13/checkpoint.json','background_37/checkpoint.json','background_37/second_review_queue.json','background_37/final_verification.json','background_37/independent_primary_math_audit.json','Solid230_r37_equal_value_face_identity_parent_binding_precheck.json','Solid230_r37_equal_value_face_identity_independent_review_brief.txt'])
hashes={rel(p):fh(p) for p in sorted(hash_paths)}
limits=[
    '两次都明确数了两个 1，并把未标记的 middle-right 6 读成 5。事前 equal-value face identity collapse 未被响应证实；本推荐不能称为值合并机制成功，也不能把意图事后改成诱导 6→5。',
    '本题没有既有原图模型对照，也没有新增。没有因果、相对原图增益、统计显著性、跨模型稳健性或人群错误率证据；不把这些未要求的实验设为硬门槛。',
    '标记信息性来自实际面值、面身份、真实边归属及原生图文的独立审阅；它不是由 42/42 自动推出。标记可能帮助细读者避免重复值合并，这不等于该候选已经显示出预设诱导机制。',
    '没有逐组消融或人类实验。每组的有用角色是图面信息表达与比较定位，不是经过实验确认的单标记因果必要性。',
    '两次完整响应支持本冻结 PNG 的两次事前数值命中，不能据此推断模型内部机制、总体命中率或标记造成该次 6→5 误读。',
    '本地请求、原始响应、时序与哈希一致性已独立核验；哈希没有外部不可抵赖时间证明，现有目录扫描也不排除未保存或外部未披露的历史。',
    'recommended 仅是这份全新独立研究复核的推荐。原主审 hold/primary_twohit=false 保持原样；不代表用户原题重新审批、Special Pass/Collect、发布或历史状态变更。',
    '源只读结论限定于 334 个明确跟踪的文件及本次写入隔离；不宣称其他并行任务修改的整个工作区都没有变化。'
]
report={
    'schema_version':'1.0.0','question_id':'Solid230','variant_id':'r37_equal_value_face_identity','branch':'SolidGeometry',
    'decision':'recommended','review_kind':'NEW independent second review; not author self-review or user approval',
    'reviewed_at_utc':now(),
    'reason_zh':'推荐作为研究候选：独立证明唯一正确答案为 41；实际三图均可数清 22 个可见点，候选完整保留全部 pip 像素；同一冻结图两次完整 MiMo quicktest3 disabled 调用均明确以事前预设 42 结束。两条红边精确定位七个可见面中仅有的两个 1 点面，构成点值相同而骰子/面身份不同的实际比较组，具有具体信息角色且开放、简洁、原生可读，没有新增条件或合理竞争答案。响应中的实际错误是未标记 6→5，未证实预设值合并机制；本次独立推荐不回写主审 hold，也不声称因果或增益。',
    'approval_status':'RESEARCH_RECOMMENDATION_ONLY; no user approval, Pass, Collect, submission or publication',
    'independence':{'brief_read_in_full':True,'all_required_protocols_read_in_full':True,'no_parent_history_used_as_proof':True,
        'parent_precheck_role':'Read last as index/cross-check only; independently read raw requests/responses, rebuilt fingerprint, counted image pixels and replayed exact candidate.',
        'no_child_agents_threads_or_worktrees':True,'new_solver_calls':0,'new_original_controls':0,'new_retries':0,'frozen_inputs_or_preset_modified':False},
    'original_problem':{'question':record['question'],'answer_type':record['answer_type'],'choices':None,'source_options':[],
        'source_dataset':'MathVision','source_key':record['source_key'],'source_image_token_only_removed':True,
        'formal_record':record,'formal_record_canonical_sha256':canonical(record)},
    'unique_correct_answer':'41','expected_wrong_answer':'42','observed_final_answers':['42','42'],
    'complete_two_raw_final_answers':evidence['runs'],
    'independent_mathematical_proof':proof,
    'actual_visual_inspection':{'method':'Actually opened all three original local image files with view_image detail=original, in sequence. Native source 235×522 and both PNGs 768×768 inspected; no resized sheet or parent judgment substituted.',
        'images':native['images'],'native_visible_face_count':7,'native_pip_count':22,
        'middle_right_six':'Six distinct black points in two source-aligned rows of three, all visibly separated from borders. Raster connected components independently find all six; no point changed or hidden.',
        'raster_component_counts':{k:v['pip_component_count'] for k,v in native['raster_components'].items()},
        'all22_pip_patches_exact_equal':True,'per_pip_patch_details_file':str(OWN/'native_render_pixel_audit.json'),
        'minimum_pip_center_to_any_changed_pixel_distance':native['minimum_pip_center_distance_to_any_change'],
        'pip_pixel_preservation_old_report_independently_recomputed':True},
    'marker_group_reviews':markers,
    'joint_marker_semantics':{
        'information_targeting_zh':'同色开放边分别邻接且只邻接一个可见 1 点面；两个被选中的面，恰是所有可见面中点值唯一重复的那一对。顶面法向 (0,0,1)、底骰右面法向 (1,0,0)，上下两骰身份与空间间隔直接可见。颜色组将这两个真实重复值对象置于共同注意力组，具体比较点值相等与可见面记录分别计数的区别。这一信息对应在图片里能自行读到，不依赖设计说明发给 solver。',
        'usefulness_vs_nominal_pairing_zh':'若仅高亮任意两个轮廓则无此依据；本次两边选在各自 1 点面的非共享外缘，避开相邻 2/3/5/6 点面，在不圈面、不增加图形对象的情况下完成重复值面的双端定位。它们不提供新的数学条件，但有任务相关的实际定位与比较作用，故不判为任意醒目色。',
        'concision_zh':'两组各一条必要的定位边，没有整图描边、无用途配色、连接装饰、额外点、文字或闭合区域。没有使用任意动作数量上限；通过理由是每组的表示性角色。',
        'human_unambiguity_zh':'题干明言三骰各面 1 至 6，七面可见。颜色和宽度不改变 pip 数、骰子身份、面法向或原有分界；同色不是等长刻痕/平行箭头，两个开放段也不相连。将红色视为棱上油漆或图外强调，都仍有 22 个可见点、唯一隐藏和 41。没有合理读法可把同一颜色的两个不同面的 1 点只算一次，也没有把六点读成五点的像素依据。',
        'paper_color_objection_zh':'已阅读 Plane242 完整 JSON 的任务特定彩边异议与 lesson。Solid230 不要求搬运纸片或匹配保留油墨的结果图，无选项图颜色对应约束。红棱解释为实物油漆也不增减任何圆形黑点，故不会重现该纸片题无匹配选项的歧义。',
        'new_geometry_projection_visibility_text_fill_dimension_changes':False,
        'response_supported_mechanism':False,
        'observed_effectiveness':'Two complete final numeric hits to immutable 42 only. Explicit narrative error is middle-right 6→5, not equal-value collapse.',
        'causal_or_incremental_effect_established':False},
    'old_objections_rechecked':[
        {'origin':str(SHARED/'background_13/checkpoint.json'),'exact_original_assessment':old_assessment,
         'disposition':'Old screening history retained, not relabeled as a tested miss or success.',
         'independent_resolution_zh':'旧目录只有 6 份快照/上下文文件，无设计、测试或原图对照。新设计实际选中两个且仅两个可见 1 点面的真实外缘；具体等值面比较的双对象已经存在，独立审阅据此认为超过任意 pip salience。旧历史未改。'},
        {'origin':str(CAND/'primary_review.json'),'exact_primary_caution':primary_caution,
         'disposition':'Factual caution fully confirmed; mechanism limitation retained.',
         'independent_resolution_zh':'两响应正文都计算两个 1，且都把中右 6 写成 5。42/42 数值证据有效，但不能证实冻结 equal-value identity collapse；没有将意图改成诱导 6→5。图片自身的信息角色按上面的精确面/边对应独立通过，不由终答反推。'},
        {'origin':str(SHARED/'background_37/second_review_queue.json'),'exact_primary_disposition':held['primary_disposition'],
         'exact_primary_twohit':held['primary_twohit'],'exact_original_review_status':held['review_status'],
         'exact_original_information_targeting_objection':held['information_targeting_objection'],
         'disposition':'Original HOLD preserved; this is a separate new independent recommendation, explicitly allowed by the queue.',
         'not_a_retroactive_primary_pass':True},
        {'origin':str(CAND/'pip_pixel_preservation.json'),'disposition':'Independently verified all 22 patches and actual rasters; no missing pip or mid-right occlusion.'},
        {'origin':'User standard and reviewed reference cases Solid128, Solid197, Plane192, Plane233, Plane242',
         'disposition':'Two terminal hits and independent targeted/valid/concise/unambiguous image review applied together. No extra correct-control, identical-narrative, ablation, population-study or causal-gain gate imposed.'}
    ],
    'primary_claims_independently_corrected':[
        {'finding':'No Solid230 mathematical error found in primary 41/22 proof or its precise line_10/line_2 face identification. Its warning that outputs do not support equal-value collapse is correct.',
         'action':'No primary fact or history edited. Do not call its held numeric pair a primary-approved result.'},
        {'finding':'Formal scene source_note contains legacy text "Original image and question retained independently; no formal approval." This is not the current approval authority.',
         'qualification':'Current formal dataset, user instruction/time and recomputed approval content SHA256 independently match. The legacy note was preserved; no new approval inferred from this review.',
         'blocking':False},
        {'finding':'manual_final_review letter_and_value_consistent=true is vacuous for this number question: there are no options or required letter.',
         'qualification':'Both complete raw endings explicitly give numeric 42. No option letter was invented or inferred.', 'blocking':False}
    ],
    'two_hit_evidence_audit':evidence,
    'exact_hash_bindings_sha256':hashes,
    'image_pixel_hashes':{'formal':'938ffad04ec59afbaa2ba21e09f38d2e523c52804adb937bcca26cc0f8441255','candidate':'189555d17ff5bb58b9eab60fbc2aa4e6c1ae2bef3f430291e5de7e46f0a64890','definition':'SHA256 of b"768x768:RGBA:" + RGBA pixel bytes'},
    'frozen_render_replay':{'all_required_checks_pass':True,'required_checks':required_native,
        'noop_pixels_identical':True,'noop_png_byte_identical':False,'noop_metadata_only_difference':'Software tEXt: formal MathPalette strict protocol renderer; no-op MathPalette SolidGeometry 1.0.0. All other PNG chunks including compressed IDAT are identical.',
        'noop_byte_sha256':native['noop_sha256'],'formal_byte_sha256':native['images']['formal']['sha256'],
        'replay1_sha256':native['replay1_sha256'],'replay2_sha256':native['replay2_sha256'],'candidate_replayed_byte_exact_twice':True,
        'changed_pixels':native['changed_pixels'],'all_changes_local_to_selected_edges':True,
        'max_changed_pixel_distance_to_selected_centerline':native['maximum_changed_pixel_distance_to_selected_centerlines'],
        'projection_sha256':native['projection_sha256'],'projection_matches_frozen_visibility_binding':native['projection_sha256']==native['frozen_visibility']['projection_sha256'],
        'geometry_projection_visibility_fills_labels_dimensions_preserved':True,'appearance_changes':native['appearance_changes'],
        'all_scene_handles_and_figures_closed':True,'optional_noop_byte_diagnostic_qualification_file':str(OWN/'acceptance_checks.json')},
    'authoritative_current_eligibility':eligibility,
    'protocols_read_in_full':read(OWN/'protocol_receipt.json'),
    'objections':{'blocking':[],'confirmed_nonblocking_limitations':limits,'frozen_evidence_repairs_performed':False},
    'limitations':limits,
    'read_only_preservation':{'baseline_file_count':len(before['files']),'all_tracked_sources_and_old_evidence_unchanged':not changes,'changes':changes,
        'baseline_file':str(OWN/'read_only_before.json'),'final_file':str(OWN/'read_only_after.json'),
        'only_assigned_directory_written':True,'formal_approval_special_indexes_unchanged':True,
        'no_git_env_or_shared_helper_writes':True,'no_api_ledger_writes':True,'no_formal_changes_or_aggregate_rebuild':True},
    'process_cleanup':{'python_pids':[9848,2096,45968,10284,os.getpid()],'all_commands_foreground':True,
        'own_background_processes_started':0,'child_agents_threads_worktrees_created':0,'solver_api_calls':0,'servers_started':0,
        'network_and_subprocess_blocked_in_review_python':True,'strict_own_directory_guard_installed_before_project_imports':True,
        'all_caches_inside_assigned_directory':True,'all_captured_scenes_closed':True,
        'final_external_process_audit':'PENDING final read-only PowerShell check after this report writer exits; see process_cleanup_final.json'},
    'auxiliary_evidence':{p.name:{'absolute_path':str(p),'sha256':fh(p)} for p in sorted(OWN.iterdir()) if p.is_file() and p.name!='independent_review.json'},
    'report_absolute_path':str(OWN/'independent_review.json')
}
write('independent_review.json',report)
print(json.dumps({'decision':report['decision'],'correct_answer':'41','two_finals':['42','42'],'tracked_files_unchanged':len(after),
    'all_required_checks_pass':True,'report':str(OWN/'independent_review.json'),'report_writer_pid':os.getpid()},ensure_ascii=False))
