from tools08 import *
earlier=json.loads((HERE/'source_preservation_audit.json').read_text(encoding='utf-8'));checks={}
for p,d in earlier['files'].items():
    digest=file_hash(ROOT/p);checks[p]={'before':d['before'],'after':digest,'unchanged':d['before']==digest}
assert all(d['unchanged'] for d in checks.values())
write(HERE/'source_preservation_final.json',{'at':now(),'files':checks,'count':len(checks),'all_unchanged':True,'previous_audit_sha256':file_hash(HERE/'source_preservation_audit.json'),'formal_files_modified':False,'shared_helpers_modified':False,'write_guard_scope':str(HERE),'environment_and_bridge_temp_isolation':ISOLATION})
print(json.dumps({'final_source_hashes_unchanged':len(checks)}))
