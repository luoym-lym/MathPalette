from tools08 import *
files={};conflicts=[]
for q in ASSIGNED:
    snap=json.loads((HERE/q/'input_fingerprints.json').read_text(encoding='utf-8'))
    for name,digest in snap['files'].items():
        if name in files and files[name]!=digest:conflicts.append(name)
        files[name]=digest
checks={p:{'before':digest,'after':file_hash(ROOT/p),'unchanged':digest==file_hash(ROOT/p)} for p,digest in files.items()}
write(HERE/'source_preservation_audit.json',{'audited_at':now(),'frozen_file_count':len(checks),'snapshot_conflicts':conflicts,'all_unchanged':not conflicts and all(x['unchanged'] for x in checks.values()),'files':checks,'scope':'All original inputs/manifests frozen at each of the 20 fresh inspect_question calls. Root diagnostic exploration metadata is separately classified, not a frozen source input.'})
assert not conflicts and all(x['unchanged'] for x in checks.values())
for q in ASSIGNED:write(HERE/q/'eligibility_end.json',eligibility(q))
report=BASE/'exploration_report.json';rd=json.loads(report.read_text(encoding='utf-8-sig'));previous={r['question_id'] for r in rd['attempts']}
remain=BASE/'remaining_questions.jsonl';entries={r['question_id']:r for r in rows(remain) if r['question_id'] in ASSIGNED}
inventory=BASE/'inventory.json';iv=json.loads(inventory.read_text(encoding='utf-8-sig'))
write(HERE/'history_freshness_audit.json',{'at':now(),'assigned_ids':ASSIGNED,'intersection_with_prior_global_attempts':sorted(set(ASSIGNED)&previous),'remaining_entries':entries,'inventory_top_level_keys':list(iv) if isinstance(iv,dict) else None,'diagnostic_runtime_metadata_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in [inventory,remain,report]},'note':'No global summaries/helpers changed by this worker. Authoritative eligibility is established separately from formal record, user content fingerprint, accepted/collected records and delivery manifests; mutable runtime metadata is diagnostic only.'})
assert not set(ASSIGNED)&previous
required=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','runtime/mathvision_special_20261101/background_08_brief.txt','runtime/mathvision_special_20261101/background_08_assignment.json','runtime/mathvision_special_20261101/parallel_expansion_20261101.json','runtime/mathvision_special_20261101/continuation_brief.txt']
write(HERE/'protocol_read_audit.json',{'all_required_read_in_full_before_design':True,'paths_and_sha256':{p:file_hash(ROOT/p) for p in required},'continuation_location':'runtime/mathvision_special_20261101/continuation_brief.txt','initial_root_lookup_missing':True,'explicit_user_overrides':'Finite autonomous hypotheses/real quicktest3 and own runtime root are explicitly authorized; no state submit, Pass/Collect or publication. No nested agents/delegates created.'})
print(json.dumps({'source_files_checked':len(checks),'all_unchanged':True,'all20_currently_eligible':all(json.loads((HERE/q/'eligibility_end.json').read_text(encoding='utf-8'))['eligible'] for q in ASSIGNED),'prior_attempt_overlap':[]}))
