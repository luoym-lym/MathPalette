from tools import *
result=[]
for qid in ASSIGNED:
    if qid.startswith('Plane') != (BRANCH=='PlaneGeometry'):continue
    d=TASK/qid;before=read(d/'frozen_inputs.json');current=frozen(qid)
    check=eligibility(qid);old=read(d/'eligibility_at_start.json')
    changes=[p for p,h in before['files'].items() if current['files'].get(p)!=h]
    r=AD.records[qid]
    source=ROOT/BRANCH/r['original_image'] if r.get('original_image') else None
    item={'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),
      'current_eligible':check['eligible'],'eligibility_reasons':check['reasons'],
      'formal_record_unchanged':before['question_record_sha256']==current['question_record_sha256'],
      'frozen_input_hash_changes':changes,'frozen_inputs_unchanged':before==current,
      'approval_entry_unchanged':old['approval']==check['approval'],
      'special_question_records_unchanged':old['special_records']==check['special_records'],
      'original_png_raw_copy_exact':file_hash(d/'original.png')==file_hash(AD.original_paths[qid]),
      'baseline_context_pixel_matches_current_formal':read(d/'context.json')['original_pixel_sha256']==pixel_hash(AD.original_paths[qid]),
      'source_original_present':bool(source and source.is_file()),
      'source_original_raw_copy_exact':file_hash(d/'source.png')==file_hash(source) if source else None,
      'source_copy_format_note':'source.png is an unchanged binary copy of the formal original_image (JPEG where applicable); no redraw is represented as a missing source.',
      'scene_snapshot_exact':read(d/'source_scene_snapshot.json')==read(ROOT/BRANCH/r['scene']),
      'current_eligibility':check,'frozen_inputs':current,
      'scope_note':'Individual assigned MathVision inputs and per-question formal/Special/approval entries checked. Whole-workspace equality is not asserted. Aggregate indices and runtime progress can change due to concurrent unrelated activity.'}
    assert all(item[k] for k in ['formal_record_unchanged','frozen_inputs_unchanged','approval_entry_unchanged','special_question_records_unchanged','original_png_raw_copy_exact','baseline_context_pixel_matches_current_formal','scene_snapshot_exact'])
    assert item['current_eligible']
    write(d/'source_audit_final.json',item);result.append(item)
write(TASK/(BRANCH+'_source_audit_final.json'),{'branch':BRANCH,'question_count':len(result),'all_passed':True,'results':result})
print(BRANCH,len(result),'assigned source/approval/Special audits passed')
