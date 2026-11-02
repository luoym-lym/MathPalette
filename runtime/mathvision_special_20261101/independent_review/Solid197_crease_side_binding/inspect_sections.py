import review_bootstrap as b
import json
from pathlib import Path

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

audit = read(b.ROOT / 'audit_bindings.json')
selected = read(b.ROOT / 'selected_primary_and_history.json')
elig = audit['current_eligibility']
print(json.dumps({'eligibility': {k:v for k,v in elig.items() if k not in ('source_notes','formal_record')},
                  'frozen_input_mismatches': audit['frozen_input_mismatches'],
                  'record_matches_snapshot':audit['record_matches_snapshot'],
                  'proof': selected['primary_math_proofs.json'],
                  'preservation': selected['source_preservation_final.json'],
                  'queue':selected['second_review_queue.json']}, ensure_ascii=False, indent=2))
for entry in audit['evidence']['control_original']:
    print('CONTROL BINDING AND SANITIZED REQUEST')
    print(json.dumps({k:v for k,v in entry.items() if k != 'runs'}, ensure_ascii=False, indent=2))
    for r in entry['runs']:
        print('CONTROL COMPLETE RAW RESPONSE')
        print(json.dumps(r['raw_response'], ensure_ascii=False, indent=2))
        print(json.dumps({'record_metadata':{k:v for k,v in r['record'].items() if k != 'answer'},
                          'checks':r['checks']}, indent=2))
print('CANDIDATE REQUEST AND CHECKS')
for entry in audit['evidence']['crease_side_binding']:
    print(json.dumps({k:v for k,v in entry.items() if k != 'runs'}, ensure_ascii=False, indent=2))
    print(json.dumps([r['checks'] for r in entry['runs']], indent=2))
