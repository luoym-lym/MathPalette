import task_env
from task_env import OWN,PROJECT
from prepare import write,hashfile
src=OWN.parent/'harness/quicktest3_isolated.py'
t=src.read_text(encoding='utf-8-sig')
anchor='from __future__ import annotations\n'
insert='\nimport sys as _sys\nfrom pathlib import Path as _Path\n_sys.path.insert(0,str(_Path(__file__).resolve().parents[1]))\nimport task_env\n'
assert t.count(anchor)==1
t=t.replace(anchor,anchor+insert)
assert t.count('PROJECT = Path(__file__).resolve().parents[3]')==1
t=t.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
t=t.replace('RUNTIME = (PROJECT / "runtime").resolve()','RUNTIME = Path(__file__).resolve().parents[1]')
dst=OWN/'harness/quicktest3_isolated.py';dst.parent.mkdir(exist_ok=True)
dst.write_text(t,encoding='utf-8')
restored=t.replace(anchor+insert,anchor).replace('PROJECT = Path(__file__).resolve().parents[4]','PROJECT = Path(__file__).resolve().parents[3]').replace('RUNTIME = Path(__file__).resolve().parents[1]','RUNTIME = (PROJECT / "runtime").resolve()')
assert restored==src.read_text(encoding='utf-8-sig')
write(OWN/'harness_source_audit.json',{'reference_path':str(src),'reference_sha256':hashfile(src),'own_copy':str(dst),'own_sha256':hashfile(dst),'only_edits':['import own task_env before project imports','project ancestor depth for nested own harness','tighten runtime_path to own directory'],'API_payload_profile_timeout_max_tokens_response_handling_loop_unchanged':True,'reverse_edits_exact_source_equal':True})
