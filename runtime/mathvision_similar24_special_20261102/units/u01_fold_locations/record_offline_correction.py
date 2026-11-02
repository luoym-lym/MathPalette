import own_runtime as rt
rt.save(rt.OWN/'offline_error_001.json',{'stage':'path_fingerprints serialization after successful two identical local renders',
    'question_id':'Plane202','error':'TypeError: Object of type ndarray is not JSON serializable',
    'location':'prepare_candidates.py:142 -> own_runtime.py:58 json.dumps(paths)',
    'diagnosis':'object_paths returns internal renderer ndarray path data. The intended audit needs only the actual stable id,sha256,closed path fingerprints; serialize exactly those primitive fields.',
    'not_host_render_geometry_or_API_failure':True,'API_requests_at_error':0,'design_frozen_at_error':False,
    'correction':'Project renderer and schema unchanged; unit helper now selects the three primitive fingerprint keys. All offline gates and fresh context will rerun. Partial candidate/repeat PNG retained at the same path; no immutable design or response exists.',
    'at':rt.now()})
