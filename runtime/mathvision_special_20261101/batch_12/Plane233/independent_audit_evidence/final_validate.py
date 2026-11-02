from review_env import *
from datetime import datetime,timezone
import ast

r=read(OUT/'independent_review.json')
assert r['question_id']=='Plane233' and r['variant_id']=='r23_four_cell_corner_spine'
assert r['decision']=='recommended' and r['original_unique_answer']=='A' and r['preset_wrong_answer']=='C'
assert len(r['two_complete_final_answers'])==2 and len(r['per_action_review'])==12 and len(r['marker_groups'])==4
baseline=read(OUT/'baseline_hashes.json')
drift=[p for p,h in baseline.items() if sha(ROOT/p)!=h]
assert not drift,drift
for name,v in r['supporting_artifacts'].items():
    assert sha(Path(v['path']))==v['sha256'],name
for i,x in enumerate(r['two_complete_final_answers'],1):
    raw=read(TEST/f'run_{i:02}_response.json')
    body=raw['choices'][0]['message']['content']
    assert x['full_raw_assistant_content']==body
    assert x['manual_final_option']=='C' and x['matches_pre_call_preset']
    assert not x['contradictory_terminal_option_or_numeric_value']
    assert body.replace('\\n','\n').endswith(x['literal_terminal_final'])
binding=read(TEST/'binding.json')
design=read(CAND/'design.json')
diff=read(CAND/'design_difference_audit.json')
assert sha(CAND/'design_difference_audit.json')==design['difference_audit_sha256']
assert diff['before_calls'] and diff['new_wrong_answer']=='C' and diff['geometry_feature_lengths']==[4,2]
assert sha(ROOT/'PlaneGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256']
tree=ast.parse((ROOT/'PlaneGeometry/workbench/quick_test.py').read_text(encoding='utf-8-sig'))
system=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SYSTEM_PROMPT' for t in n.targets))
profiles=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='TEST_PROFILES' for t in n.targets))
assert system==binding['system_prompt']
for k,v in profiles['quicktest3'].items():assert binding['settings'][k]==v
assert binding['settings']['api_base']=='https://token-plan-cn.xiaomimimo.com/v1'
assert sha(CAND/'candidate.png')==r['exact_evidence_bindings']['candidate_png_sha256']
approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane233']
assert approval==r['current_authoritative_eligibility']['approval']
for idx in ['accepted_index.jsonl','collected_index.jsonl']:
    p=ROOT/'PlaneGeometry/special_variant'/idx
    rows=[json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    assert not any(x.get('question_id')=='Plane233' for x in rows)
assert not (ROOT/'PlaneGeometry/special_variant/Plane233').exists()
assert sha(ROOT/'PlaneGeometry/dataset.jsonl')==binding['dataset_sha256']
r['workspace_and_process_discipline']['process_exit_check_path']=str(OUT/'process_exit_check.json')
r['workspace_and_process_discipline']['final_validation_path']=str(OUT/'final_validation.json')
save('independent_review.json',r)
validation={'validated_at_utc':datetime.now(timezone.utc).isoformat(),'validator_pid':os.getpid(),
    'question_id':r['question_id'],'variant_id':r['variant_id'],'decision':r['decision'],
    'required_report_fields_present':True,'complete_raw_answers_exact':True,'frozen_profile_reference_matches':True,
    'design_difference_hash_and_preset_matches':True,'scoped_source_evidence_hash_drift':drift,
    'supporting_artifact_hashes_match':True,'current_formal_eligibility_still_valid':True,
    'new_solver_calls':0,'report_sha256':sha(OUT/'independent_review.json')}
save('final_validation.json',validation)
emit(validation)
