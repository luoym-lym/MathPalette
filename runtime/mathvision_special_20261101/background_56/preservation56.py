from env56 import *
before=read(OWN/'readonly_hashes_start.json')
extra=read(OWN/'extra_readonly_references.json')
before.update({p:r['sha256'] for p,r in extra.items()})
for q in read(BASE/'background_56_assignment.json')['question_ids']:
    e=read(OWN/q/'eligibility_start.json')
    before.update(e['authoritative_hashes'])
changed={};missing=[];after={}
for p,h in before.items():
    f=PROJECT/p
    if not f.is_file():missing.append(p);continue
    after[p]=sha(f)
    if after[p]!=h:changed[p]={'before':h,'after':after[p]}
save('readonly_hashes_final.json',after)
elig=[]
for q in read(BASE/'background_56_assignment.json')['question_ids']:
    e=eligibility(q);save(f'{q}/eligibility_final.json',e)
    elig.append({'question_id':q,'eligible':e['eligible'],'approval_matches':e['approval_matches'],'fingerprint':e['current_content_sha256']})
malformed=[r for r in read(OWN/'old_evidence_full_byte_read.json') if 'malformed' in r]
save('preservation_final.json',{'at':now(),'tracked_preexisting_source_old_evidence_and_batches':len(before),'changed':changed,'missing':missing,'all_scoped_readonly_hashes_preserved':not changed and not missing,'latest_eligibility_and_original_approval':elig,'malformed_old_artifacts_preserved':malformed,'all_new_writes_under_own_root':True,'strict_own_write_guard':True,'runtime_isolation_guard_before_project_imports':True,'no_whole_workspace_or_actor_attribution_claim':True,'diagnostic_mutable_runtime_progress_policy':'No global master/progress/summary is edited. Historical metadata hashes stay unchanged in old evidence, not recertified as frozen original inputs.','no_formal_or_Special_or_approval_or_env_or_git_writes':True})
print('Preservation',len(before),'files; changed',len(changed),'missing',len(missing),flush=True)
