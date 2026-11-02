import own_runtime as rt
d=rt.OWN/'Plane238/u01_actual_crease_to_wrong_packet_separator'
v=rt.read(d/'visual_primary_before_calls.json')
rt.save(d/'visual_primary_pre_view_timestamp_preserved.json',{'original_record':v,
    'correction':'This record timestamp preceded the direct view_image tool in the same orchestration call. The actual PNG has now been viewed before any API request; replace the mutable pre-call visual review with a newly timed record. The old timing claim is retained here, not treated as prior native-view evidence.',
    'at':rt.now(),'calls_started_at_correction':len(list((d/'tests').glob('*/run_*_started.json'))),'design_and_image_unchanged':True})
