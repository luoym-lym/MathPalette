from research import *
spec=importlib.util.spec_from_file_location('_inventory_readonly_final',BASE/'inventory.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
before=json.loads((HERE/'formal_files_before.json').read_text(encoding='utf-8'));after=module.scan();prior=json.loads((HERE/'previous_evidence_before.json').read_text(encoding='utf-8'))
value={'checked_at':datetime.now(timezone.utc).isoformat(),'existing_non_runtime_non_git_file_count':len(before),'changed':[p for p in before.keys()&after.keys() if before[p]!=after[p]],'added':sorted(after.keys()-before.keys()),'deleted':sorted(before.keys()-after.keys()),'prior_runtime_evidence_count':len(prior),'prior_evidence_changed_or_deleted':[p for p,h in prior.items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h],'method':'Read-only full SHA-256 scan outside root runtime/.git; pre-existing .runtime entries retain metadata-only checks. Hash all prior runtime evidence except harness cache directory, excluding this fresh unit.','no_writes_outside_runtime':True}
write(HERE/'source_preservation_final.json',value)
print(json.dumps({k:v for k,v in value.items() if k not in ['method']}))
