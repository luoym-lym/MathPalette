from bootstrap46 import *
import re
scan=read(OWN/'full_task_api_reuse_scan.json');classified=[]
for entry in scan['parse_or_decode_errors']:
    p=Path(entry['path']);raw=p.read_text(encoding='utf-8-sig')
    assert ('paths' in p.name or 'fingerprints' in p.name or 'path_index' in p.name)
    assert not any(h in raw for h in scan['targets'].values())
    assert not any(x in raw for x in ['data:image/png','started_at','request_body_sha256','messages','http_status'])
    classified.append({'path':str(p),'sha256':sha(p),'full_contents':raw,'classification':'incomplete offline vector-path serialization; no call/request/start/run/error schema or candidate SHA or PNG payload'})
prep=read(OWN/'preparation_full_read_hash_verification.json')
save(OWN/'full_task_api_reuse_scan_followup.json',{'previous_scan_sha256':sha(OWN/'full_task_api_reuse_scan.json'),'all_parse_errors_individually_read_and_excluded_as_noncall':classified,'actual_API_parse_errors':[],'actual_call_matches':scan['actual_call_matches'],'reuse_zero_prior_calls_supported':not scan['actual_call_matches'],'preparation_mismatches_diagnostic':prep['mismatches'],'limitations':scan['limitation']})
print(json.dumps({'noncall_parse_error_files_individually_read':len(classified),'actual_API_parse_errors':0,'prior_calls':len(scan['actual_call_matches']),'preparation_mismatches':prep['mismatches']},ensure_ascii=False))
