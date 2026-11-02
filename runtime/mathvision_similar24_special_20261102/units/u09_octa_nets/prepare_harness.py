from own_bootstrap import *
import difflib

original=OLD/'harness/quicktest3_isolated.py'
target=OWN/'harness/quicktest3_isolated.py'
before=original.read_bytes()
needle=b'PROJECT = Path(__file__).resolve().parents[3]'
replacement=('PROJECT = Path('+repr(str(PROJECT))+')').encode('utf-8')
assert before.count(needle)==1
after=before.replace(needle,replacement)
assert after.replace(replacement,needle)==before
target.parent.mkdir(parents=True,exist_ok=True)
with target.open('xb') as f:f.write(after)
diff=''.join(difflib.unified_diff(before.decode('utf-8').splitlines(True),after.decode('utf-8').splitlines(True),
        fromfile=str(original),tofile=str(target)))
(OWN/'harness/path_only.diff').write_text(diff,encoding='utf-8',newline='\n')
save(OWN/'harness/copy_integrity.json',{'original_path':str(original),'original_sha256':sha(original),
    'copied_path':str(target),'copied_sha256':sha(target),'only_replacement':{'before':needle.decode(),'after':replacement.decode()},
    'reverse_replacement_byte_equal':True,'diff':diff,'payload_system_model_thinking_private_key_timeout_and_no_retry_unchanged':True},exclusive=True)
print(diff)
