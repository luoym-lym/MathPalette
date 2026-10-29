"""Record an explicit user approval, then rebuild the formal catalog."""
from __future__ import annotations
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from dataset_tools import catalog

def approve(branch, question_ids, instruction, root=ROOT, *, catalog_lock_held=False):
    root=Path(root)
    if not catalog_lock_held:
        with catalog.catalog_write_lock(root):
            return approve(branch, question_ids, instruction, root, catalog_lock_held=True)
    if branch not in catalog.BRANCHES or not instruction.strip():
        raise ValueError('A known branch and verbatim user approval are required')
    records={r['id']:r for r in catalog.rows(root/branch/'dataset.jsonl')}
    if not question_ids or len(question_ids)!=len(set(question_ids)) or not set(question_ids)<=records.keys():
        raise ValueError('Specify unique question IDs present in this branch')
    path=root/'provenance/approvals.json'
    before=path.read_bytes()
    data=json.loads(before)
    source_notes, notes_fingerprint = catalog._source_notes_snapshot(root)
    for qid in question_ids:
        fingerprint=catalog.digest(catalog.content(root,branch,records[qid],source_notes=source_notes))
        previous=data['approvals'].get(qid)
        if previous and previous['content_sha256']==fingerprint:
            continue  # Rechecking identical content must not replace original review times.
        entry={'id':qid,'branch':branch,'reviewer':'user','instruction':instruction,
               'approved_at_utc':datetime.now(timezone.utc).isoformat(),'content_sha256':fingerprint}
        if previous:
            entry['previous_content_sha256']=previous['content_sha256']
        data['approvals'][qid]=entry
    catalog._assert_source_notes_unchanged(root, notes_fingerprint)
    temporary=path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.replace(temporary,path)
    try:
        catalog.build_locked(root)
    except BaseException:
        path.write_bytes(before)
        raise
    return question_ids

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('branch',choices=catalog.BRANCHES)
    parser.add_argument('question_ids',nargs='+')
    parser.add_argument('--instruction',required=True,help='Verbatim explicit approval from the user; never invent one')
    args=parser.parse_args()
    print(json.dumps({'approved':approve(args.branch,args.question_ids,args.instruction)},ensure_ascii=False))
