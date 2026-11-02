import bootstrap75 as boot
from research75 import *
import difflib
source=BASE/'harness/quicktest3_isolated.py'
old=source.read_bytes()
needle=b'PROJECT = Path(__file__).resolve().parents[3]'
assert old.count(needle)==1
new=old.replace(needle,b'PROJECT = Path(__file__).resolve().parents[4]')
target=OWN/'harness/quicktest3_isolated.py';target.parent.mkdir(parents=True,exist_ok=True)
target.write_bytes(new)
assert new.replace(b'PROJECT = Path(__file__).resolve().parents[4]',needle)==old
diff=''.join(difflib.unified_diff(old.decode('utf-8').splitlines(True),new.decode('utf-8').splitlines(True),fromfile=str(source),tofile=str(target)))
(OWN/'harness_relocation.diff').write_text(diff,encoding='utf-8')
put(OWN/'harness_relocation_audit.json',{'created_at':now(),'source':snapshot(source),'relocated':str(target),'original_sha256':sha(old),'relocated_sha256':sha(new),'only_change':'PROJECT parents[3] -> parents[4] for one additional own-unit directory; HARNESS caches resolve naturally inside ownroot','exact_reverse_byte_identity':True,'remote_payload_profile_systemprompt_tokens_timeouts_credentials_logic_unchanged':True,'wrapper_guard_before_project_imports':True,'wrapper':str(OWN/'api_entry75.py'),'runs':2,'check_or_connectivity_ping_executed':False})
for rel in ['refinement_dispatch_20261102.json','quota_resume67_73_20261102.json','quota_resume74_76_20261102.json','quota_interruption_recovery_20261102.json']:
    p=BASE/rel;val=read(p);snapshot(p);del val
put(OWN/'additional_runtime_metadata_read_audit.json',{'created_at':now(),'full_UTF8_JSON_reads':['refinement_dispatch_20261102.json','quota_resume67_73_20261102.json','quota_resume74_76_20261102.json','quota_interruption_recovery_20261102.json'],'full_snapshots_preserved':True,'metadata_not_source':True})
print(diff)
