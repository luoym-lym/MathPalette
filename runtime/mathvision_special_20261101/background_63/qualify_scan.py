from bootstrap import *
import re
s=read(HERE/'global_prior_invocation_scan.json')
refs=[]
for m in s['matches']:
    if m['kind']=='api_hash_reference':
        assert Path(m['path'])==BASE/'background_55/evidence_binding_final.json'
        v=read(m['path'])
        assert v['question_id']=='Solid195' and v['actual_calls']==2
        for q in ('Solid206','Solid207'):
            assert v['untested_frozen_candidates'][q]['API_calls']==0
            assert not v['untested_frozen_candidates'][q]['has_process_launch']
            assert not v['untested_frozen_candidates'][q]['has_tests']
        refs.append(dict(m,disposition='Aggregate audit of Solid195 pair; explicit separate zero-call statements for206/207. Not an invocation artifact for either target.'))
mal=[]
for m in s['malformed_records']:
    assert not m['related_question'] and not m['exact_hash_mentions']
    p=Path(m['path']); raw=p.read_bytes(); txt=raw.decode('utf-8-sig',errors='replace')
    if m['error']=='Only base64 data is allowed':
        value=json.loads(txt)
        reason='Valid report JSON with a quoted shortened/redacted data-image URL in an unrelated Plane342 review; not an actual request. Exact original bytes preserved.'
        assert 'Plane342' in txt or 'Plane342' in str(p)
    else:
        reason='Unrelated context console JSONL or truncated offline path-coordinate serialization; no request payload, target identifier/hash, or target-image binding.'
        assert 'path' in str(p).lower() or 'context_output' in str(p)
    mal.append(dict(m,disposition=reason))
related=[]
for r in rows(HERE/'global_scan_files.jsonl'):
    if r.get('related_question'): related.append(r)
actual=[]
for r in related:
    p=Path(r['path']); txt=p.read_text(encoding='utf-8-sig',errors='replace')
    if re.fullmatch(r'(binding|request|summary|run_\d+(?:_started|_response)?)\.json',p.name) and ('/tests/' in p.as_posix()):
        actual.append(r)
assert not actual
assert not any(m['kind']=='embedded_request_image' for m in s['matches'])
write(HERE/'zero_prior_invocation_qualified.json',dict(checked_at=now(),counts=s['counts'],exact_prior_API_matches=[],exact_png_copies=[m for m in s['matches'] if m['kind']=='png_file'],noninvocation_reference_dispositions=refs,all_related_API_named_records=related,actual_related_invocation_artifacts=actual,malformed_dispositions=mal,malformed_bytes_preserved=True,zero_visible_exact_prior_invocations=True,raw_scan_path=str(HERE/'global_prior_invocation_scan.json'),scope_and_limits=s['limitations'],note='Initial filename heuristic conservatively flagged one aggregate evidence_binding report. Full content independently read and classified here; initial scan unchanged.'))
print('qualified zero prior calls; malformed',len(mal),'related API-named reports',len(related))
