from common38 import *
q,v=sys.argv[1:3];folder=TASK/q/v
assert q in QIDS
check=eligibility(q);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
review=read(folder/'primary_review.json');assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
assert (folder/'design_difference_audit.json').is_file()
p=TASK/'harness/quicktest3_isolated.py';source=BASE/'harness/quicktest3_isolated.py';assert p.read_bytes()==source.read_bytes()
spec=importlib.util.spec_from_file_location('unchanged_unit38_harness',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=(ROOT/'runtime').resolve()
for k,n in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[k]=str(TASK/n)
write(folder/'api_process.json',dict(pid=os.getpid(),argv=sys.argv,started_at=now(),original_harness_sha256=sha(source),local_harness_sha256=sha(p),relocation='Byte-identical isolated harness in own directory, PROJECT/RUNTIME restored after import. Unchanged model/system/profile/API/credential handling; no timeout/max_tokens overrides or retries.'))
r=h.run_tests('PlaneGeometry',q,folder/'candidate.png',folder/'design.json',folder/'tests',2)
write(folder/'api_process_finished.json',dict(pid=os.getpid(),finished_at=now(),evidence_dir=r['evidence_dir'],two_completed=r['two_completed']))
