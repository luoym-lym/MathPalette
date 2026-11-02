import bootstrap
from bootstrap import OWNROOT,PROJECT,check_write
import json,hashlib
from datetime import datetime,timezone
from dataset_tools.catalog import read,rows,content,digest

out=OWNROOT/'Solid151/face_center_inventory_to_core_confusion'
design=read(out/'design.json'); r=next(r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid151');a=read(PROJECT/'provenance/approvals.json')['approvals']['Solid151'];c=content(PROJECT,'SolidGeometry',r)
assert r['source_dataset']=='MathVision' and digest(c)==a['content_sha256'] and c==read(out/'render_check.json')['source_fingerprints']
assert a['reviewer']=='user' and a['instruction']
sp=PROJECT/'SolidGeometry/special_variant/Solid151'
assert not (sp/'recipes.json').exists() and not (sp/'collection.json').exists()
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    assert not [v for v in rows(sp.parent/name) if v['question_id']=='Solid151']
for key,name in [('candidate_png_sha256','candidate.png'),('plugin_sha256','plugin.json'),('design_difference_audit_sha256','design_difference_audit.json'),('marker_path_bindings_sha256','marker_path_bindings.json')]:
    assert hashlib.sha256((out/name).read_bytes()).hexdigest()==design[key]
assert read(out/'offline_replay_check.json')['replay_equals_frozen_candidate_bytes']
assert read(out/'primary_native_visual_review.json')['actual_native_candidate_viewed']
assert design['expected_wrong_answer']=='E' and design['correct_answer']=='A'
assert not list(OWNROOT.rglob('run_*_started.json')) and not (OWNROOT/'api_process.json').exists()
blocked=False
try:check_write(PROJECT/'_guard_must_block_without_creating_file')
except PermissionError:blocked=True
assert blocked
with (out/'eligibility_immediately_before_calls.json').open('x',encoding='utf-8') as f:
    json.dump({'checked_at':datetime.now(timezone.utc).isoformat(),'source_dataset':'MathVision','current_approval_fingerprint':digest(c),'matches_original_user_approval':True,'formal_question_sha256':hashlib.sha256(r['question'].encode()).hexdigest(),'no_passed_variant':True,'not_collected':True,'no_special_completion':True,'immutable_design_sha256':hashlib.sha256((out/'design.json').read_bytes()).hexdigest(),'immutable_png_sha256':design['candidate_png_sha256'],'expected_wrong_answer':'E','offline_replay_and_native_primary_complete':True,'prior_new_API_calls':0,'strict_write_guard_rejects_outside_ownroot_without_any_write':blocked,'all_pre_API_gates_pass':True},f,ensure_ascii=False,indent=2)
print('Fresh authoritative eligibility and every frozen binding pass immediately before the two-call invocation.')
