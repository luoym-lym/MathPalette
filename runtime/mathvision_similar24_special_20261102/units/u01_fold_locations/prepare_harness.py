import own_runtime as rt
import difflib,hashlib
original=rt.OLD/'harness/quicktest3_isolated.py'
before=original.read_bytes()
old=b'PROJECT = Path(__file__).resolve().parents[3]'
new=('PROJECT = Path('+repr(str(rt.PROJECT))+')').encode('utf-8')
assert before.count(old)==1
after=before.replace(old,new)
assert after.replace(new,old)==before
d=rt.OWN/'harness';d.mkdir(exist_ok=True)
(d/'quicktest3_isolated.py').write_bytes(after)
diff=''.join(difflib.unified_diff(before.decode().splitlines(keepends=True),after.decode().splitlines(keepends=True),fromfile=str(original),tofile=str(d/'quicktest3_isolated.py')))
(d/'harness.diff').write_text(diff,encoding='utf-8')
rt.save(d/'isolation_audit.json',{'original_path':str(original),'original_sha256':hashlib.sha256(before).hexdigest(),
    'local_sha256':hashlib.sha256(after).hexdigest(),'allowed_substitutions':{'old':old.decode(),'new':new.decode()},
    'reverse_substitution_byte_equal':True,'remote_payload_changed':False,'timeout_changed':False,
    'cache_location':'HARNESS directory resolves inside own_root; no code change needed','strict_write_root':str(rt.OWN)})
print(diff)
