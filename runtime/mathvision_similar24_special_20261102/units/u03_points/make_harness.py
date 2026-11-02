from unit_env import *
import difflib

source=OLD/'harness/quicktest3_isolated.py'
original=source.read_bytes()
changes=[(b'PROJECT = Path(__file__).resolve().parents[3]',('PROJECT = Path('+repr(str(PROJECT))+')').encode()),
         (b'HARNESS = Path(__file__).resolve().parent',b'HARNESS = Path(__file__).resolve().parent.parent / "ownruntime" / "harness"')]
local=original
for old,new in changes:
    assert local.count(old)==1
    local=local.replace(old,new)
reverse=local
for old,new in reversed(changes):
    assert reverse.count(new)==1
    reverse=reverse.replace(new,old)
assert reverse==original
target=OWN/'harness/quicktest3_isolated.py'
target.parent.mkdir(parents=True,exist_ok=True)
with target.open('xb') as f:f.write(local)
diff=''.join(difflib.unified_diff(original.decode('utf-8').splitlines(True),local.decode('utf-8').splitlines(True),
                                  fromfile=str(source),tofile=str(target)))
(OWN/'harness/localization.diff').write_text(diff,encoding='utf-8',newline='')
save(OWN/'harness/localization_audit.json',{'created_at':now(),'original_path':str(source),
     'original_sha256':sha(original),'local_path':str(target),'local_sha256':sha(local),
     'changes':[{'before':o.decode(),'after':n.decode()} for o,n in changes],
     'reverse_replacement_bytes_equal':reverse==original,'remote_payload_changed':False,
     'only_local_project_and_cache_paths_changed':True})
print(diff)
