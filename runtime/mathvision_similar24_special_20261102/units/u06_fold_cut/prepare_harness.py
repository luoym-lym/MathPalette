from local_env import *
import difflib
source=OLD/'harness/quicktest3_isolated.py'
original=source.read_bytes()
before=b'PROJECT = Path(__file__).resolve().parents[3]'
after=('PROJECT = Path('+repr(str(PROJECT))+')').encode('utf-8')
assert original.count(before)==1
routed=original.replace(before,after)
assert routed.replace(after,before)==original
dest=OWN/'ownruntime/harness/quicktest3_isolated.py'
dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('xb') as f:f.write(routed)
patch=''.join(difflib.unified_diff(original.decode().splitlines(True),routed.decode().splitlines(True),fromfile=str(source),tofile=str(dest)))
(dest.parent/'routing.diff').write_text(patch,encoding='utf-8')
save(dest.parent/'routing_provenance.json',{'source':str(source),'source_sha256':sha(source),
 'routed':str(dest),'routed_sha256':sha(dest),'only_replaced':before.decode(),
 'replacement':after.decode(),'reverse_replacement_bytes_equal':True,
 'remote_payload_unchanged':True,'cache_location':'All HARNESS-relative caches remain inside ownruntime/harness',
 'original_timeout_None_no_retry':True},True)
print(patch)
