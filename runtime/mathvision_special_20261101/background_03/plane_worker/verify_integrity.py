from new_tools import *
reports=[]
for path in sorted(HERE.glob('Plane*/*/render_check.json')):
    report=json.loads(path.read_text(encoding='utf-8-sig'));folder=path.parent
    formal={p:{'matches':file_hash(ROOT/p)==sha,'expected':sha,'current':file_hash(ROOT/p)} for p,sha in report['frozen_inputs'].items()}
    own={'image':file_hash(folder/'candidate.png')==report['png_sha256'],'design':file_hash(folder/'design.json')==report['design_sha256'],'plugin':file_hash(folder/'plugin.json')==report['plugin_sha256']}
    reports.append({'candidate_directory':str(folder.relative_to(ROOT)),'all_frozen_formal_inputs_unchanged':all(v['matches'] for v in formal.values()),'formal_input_checks':formal,'own_bound_artifacts_unchanged':own,'current_eligibility':eligibility(report['question_id'])})
assert all(r['all_frozen_formal_inputs_unchanged'] and all(r['own_bound_artifacts_unchanged'].values()) for r in reports)
write(HERE/'integrity_verification.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'reports':reports,'all_inputs_and_bound_outputs_unchanged':True,'no_formal_writes_performed':True})
print('All frozen formal inputs and immutable candidate/plugin/design bytes verified unchanged.',flush=True)
