from env70 import *
from design70 import NAMES,directory
import ast
import difflib

for script in OWN.glob('*.py'):
    ast.parse(script.read_text(encoding='utf-8-sig'),filename=str(script))
denials=[]
for event,args in [('open',(str(PROJECT/'runtime/outside_owner_probe_70.txt'),'w',os.O_WRONLY|os.O_CREAT)),
                   ('os.mkdir',(str(PROJECT/'.runtime/outside_owner_probe_70'),0o777,-1))]:
    try:sys.audit(event,*args)
    except PermissionError:denials.append(event)
assert len(denials)==2
save('strict_writeguard_probe.json',{'at':now(),'synthetic_audit_events_only_no_filesystem_action':True,
      'outside_OWNROOT_events_denied':denials,'guard_installed_before_project_imports':True})
zero=read(OWN/'global_new_PNG_zero_call_audit.json')
assert zero['zero_exact_old_PNG_requests_and_files']
malformed=zero['malformed_embedded_PNG_strings_preserved']
assert all(v['prefix']=='<exact frozen candidate>' and v['suffix']=='<exact frozen candidate>' and v['encoded_length']==24 for v in malformed)
assert all('/no_leak_request/' in v['json_path'] for v in malformed)
save('embedded_placeholder_classification.json',{'checked_at':now(),'entries':malformed,
     'finding':'Every non-decodable data URL is the literal24-character documentation placeholder <exact frozen candidate> in a copied Plane342 independent no-leak audit/report. They are not transport request.json payloads. Actual original Plane342 request files are separate and were decoded in the full scan.',
     'source_bytes_unchanged':True,'old_audit_v1_exception_preserved':True,
     'actual_candidate_zero_call_gate_passes':True,
     'JSON_parse_failures_preserved_in_global_scan':zero['malformed_JSON_preserved']})
source=BASE/'harness/quicktest3_isolated.py';target=OWN/'harness/quicktest3_isolated.py'
s=source.read_text(encoding='utf-8');t=target.read_text(encoding='utf-8')
assert t==s.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
source_functions=[ast.dump(n,include_attributes=False) for n in ast.parse(s).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))]
target_functions=[ast.dump(n,include_attributes=False) for n in ast.parse(t).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))]
assert source_functions==target_functions
save('harness_exact_function_AST_audit.json',{'checked_at':now(),'source_sha256':sha(source),
     'relocated_sha256':sha(target),'all_function_ASTs_identical':True,
     'single_PROJECT_line_diff':list(difflib.unified_diff(s.splitlines(),t.splitlines(),lineterm='')),
     'remote_payload_system_model_thinking_profile_token_timeout_logic_unchanged':True})
frozen=read(OWN/'readonly_hashes_start.json')
changes=[{'path':p,'old':h,'current':sha(PROJECT/p)} for p,h in frozen.items() if sha(PROJECT/p)!=h]
assert not changes
save('readonly_pre_all_calls.json',{'checked_at':now(),'files':len(frozen),'changes':changes})
records=[]
for qid in QIDS:
    r=read(OWN/qid/'assessment.json');assert r['current_eligibility']['eligible']
    records.append({'question_id':qid,'status':r['status'],'assessment':str(OWN/qid/'assessment.json')})
for qid in NAMES:
    d=directory(qid)
    assert read(d/'primary_review.json')['proceed_to_API']
    assert read(d/'offline_replay_check.json')['exact_byte_replay']
    assert not list((d/'tests').glob('**/run_*_started.json'))
snapshot={'unit':'background_70','stage':'material_refinement','status':'pre_call_all_gates_passed',
     'created_at':now(),'own_root':str(OWN),'question_ids':list(QIDS),'actual_assessed_question_ids':list(QIDS),
     'unworked_question_ids':[],'new_designs':2,'API_calls':0,'completed_calls':0,
     'credible_primary_doublehits':0,'second_review_queue':[],
     'records':records,'candidate_directories':{q:str(directory(q)) for q in NAMES},
     'global_zero_call_audit':str(OWN/'global_new_PNG_zero_call_audit.json'),
     'read_only_source_hashes_passed':True,'no_formal_or_old_source_edits':True,
     'no_nested_agents_threads_worktrees_servers':True,'new_independent_parent_review_required_for_doublehit':True,
     'offline_parser_exception':'Documentation placeholder encountered; failed v1 auditor retained, classified before any call. No allocation/import/render failure occurred.',
     'no_live_API_requests_at_checkpoint':True}
save('checkpoint_before_calls.json',snapshot)
save('checkpoint.json',snapshot)
save('second_review_queue.json',[])
print(json.dumps({'all_gates_passed':True,'new_candidates':2,'API_calls':0,'frozen_paths':len(frozen)}))
