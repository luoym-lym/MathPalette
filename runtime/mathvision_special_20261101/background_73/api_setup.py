from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp
from prepare import SPECS
import difflib,json,hashlib,base64,gc

source=TASK/'harness/quicktest3_isolated.py'
text=source.read_text(encoding='utf-8')
old='PROJECT = Path(__file__).resolve().parents[3]'
new='PROJECT = Path(__file__).resolve().parents[4]'
assert text.count(old)==1
relocated=text.replace(old,new)
target=HERE/'harness/quicktest3_isolated.py'
target.parent.mkdir(exist_ok=True)
with target.open('x',encoding='utf-8',newline='') as f:f.write(relocated)
assert relocated.replace(new,old)==text
diff=''.join(difflib.unified_diff(text.splitlines(True),relocated.splitlines(True),fromfile=str(source),tofile=str(target)))
(HERE/'harness_relocation.diff').write_text(diff,encoding='utf-8')
save(HERE/'harness_byte_diff_audit.json',{'original_source':str(source),'original_sha256':sha(source),'relocated_path':str(target),'relocated_sha256':sha(target),'only_PROJECT_resolution_changed':True,'diff':diff,'cache_logic_unchanged_and_now_under_OWNROOT':True,'remote_payload_profile_model_thinking_system_max_tokens_timeout_private_credentials_logic_changed':False,'no_check_or_ping_run':True,'strict_guard_installed_by_run_api_wrapper_before_harness_import':True})
print('Harness relocation: exact single local PROJECT line; remote logic unchanged')
