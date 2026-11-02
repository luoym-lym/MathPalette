from common68 import *
import runpy
import traceback

qid=sys.argv[1]
assert qid in IDS
q=next(q for q in read(BASE/'background_68_assignment.json')['questions'] if q['question_id']==qid)
candidate=HERE/qid/q['variant_id']
assert not (HERE/qid/'hold_before_API.json').exists(), 'Native/math/targeting hold blocks unchanged testing'
assert read(HERE/'zero_call_certification.json')['all_four_zero_prior_actual_starts']
assert read(HERE/qid/'primary_native_and_marker_review.json')['human_unambiguous_primary_assessment']
assert read(HERE/qid/'offline_replay/replay_verification.json')['matches_tested_png_bytes']
assert read(HERE/'archive_and_malformed_supplement.json')['all_matching_unknowns_absent']
assert not (candidate/'tests').exists(), 'Never rerun or retry an invocation directory'
e=eligibility(qid);assert e['eligible']
write(candidate/'eligibility_immediately_before_calls.json',e)
initial=read(HERE/qid/'source_binding_audit.json')
for p,h in initial['frozen_dependencies'].items(): assert sha(p)==h,(p,'source dependency drift')
for name,h in q['frozen_source_files_sha256'].items():
    assert sha(Path(q['source_directory'])/name)==h and sha(candidate/name)==h
original=BASE/'harness/quicktest3_isolated.py'
copied=HERE/'harness/quicktest3_isolated.py'
assert copied.read_bytes().replace(b'PROJECT = Path(__file__).resolve().parents[4]',b'PROJECT = Path(__file__).resolve().parents[3]')==original.read_bytes()
write(candidate/'reuse_ready.json',dict(checked_at=now(),question_id=qid,original_variant_id=q['variant_id'],original_created_at=q['frozen_created_at'],unchanged_wrong_preset=q['expected_wrong_answer'],source_copy_hashes=read(candidate/'reuse_provenance.json')['source_copy_hashes'],
    fresh_approval_matches=e['approval_matches_current'],current_source_dataset=e['record']['source_dataset'],no_passed_variant=e['no_passed_variant'],not_collected=e['not_collected'],
    zero_prior_actual_calls_certified=True,exact_offline_replay=read(HERE/qid/'offline_replay/replay_verification.json'),
    math_review_sha256=sha(HERE/qid/'primary_math_audit.json'),native_marker_review_sha256=sha(HERE/qid/'primary_native_and_marker_review.json'),harness_byte_audit_sha256=sha(HERE/'harness_relocation_byte_audit.json'),
    profile='Original quicktest3 mimo-v2.6-flash, thinking.disabled; unchanged system/API/private credential/max_tokens/timeout logic',runs=2,no_retry_third_call_or_cherrypick=True,solver_sees_only='Formal question text + identical frozen PNG + original system prompt',new_mechanism_count=0))
write(candidate/'api_process_started.json',dict(started_at=now(),pid=os.getpid(),executable=sys.executable,argv=list(sys.orig_argv),question_id=qid,ownroot=str(HERE),image_sha256=sha(candidate/'candidate.png'),design_sha256=sha(candidate/'design.json'),requested_runs=2))
network_gates=[]
def before_network(event,args):
    if event!='urllib.Request': return
    # Audit immediately before each actual transport, without modifying the
    # original harness, request bytes, remote settings, headers or timeout.
    url,body,headers,method=args
    assert method=='POST' and url.endswith('/chat/completions')
    assert len(network_gates)<2, 'No third actual request'
    live=eligibility(qid); assert live['eligible']
    for p,h in initial['frozen_dependencies'].items(): assert sha(p)==h,(p,'source drift before transport')
    for name,h in q['frozen_source_files_sha256'].items():
        assert sha(Path(q['source_directory'])/name)==h and sha(candidate/name)==h
    index=len(network_gates)+1
    write(candidate/f'actual_request_gate_{index:02d}.json',dict(checked_at=now(),pid=os.getpid(),run_index=index,
        current_eligibility=live,request_body_sha256=hashlib.sha256(body).hexdigest(),all_frozen_sources_and_copies_hash_exact=True,
        image_sha256=sha(candidate/'candidate.png'),design_sha256=sha(candidate/'design.json'),headers_or_credential_recorded=False,
        request_payload_or_remote_settings_modified=False))
    network_gates.append(index)
sys.addaudithook(before_network)
exit_status='completed'
try:
    sys.argv=[str(copied),'--branch',BRANCH,'--question',qid,'--image',str(candidate/'candidate.png'),'--design',str(candidate/'design.json'),'--output',str(candidate/'tests'),'--runs','2']
    runpy.run_path(str(copied),run_name='__main__')
except BaseException as err:
    exit_status='exception'
    write(candidate/'runner_exception.json',dict(checked_at=now(),exception_type=type(err).__name__,error=str(err),traceback=traceback.format_exc(),no_retry=True))
    raise
finally:
    write(candidate/'api_process_finished.json',dict(finished_at=now(),pid=os.getpid(),runner_status=exit_status,actual_transport_gates=len(network_gates),no_further_calls_from_this_process=True))
