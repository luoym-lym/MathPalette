from review_bootstrap import *
import collections

r=read(OWN/'native_render_audit.json')
outside=r['changed_pixels_outside_4px_marked_segment_tubes']
deltas=collections.Counter(max(abs(a-b) for a,b in zip(p['before'][:3],p['after'][:3])) for p in outside)
print(json.dumps({'render':{k:v for k,v in r.items() if k not in ['native_bindings','changed_pixels_outside_4px_marked_segment_tubes']},
                 'outside_count':len(outside),'outside_delta_histogram':dict(deltas),'outside_delta_gt1':[p for p in outside if max(abs(a-b) for a,b in zip(p['before'][:3],p['after'][:3]))>1]},ensure_ascii=False,indent=2))
d=read(OWN/'documents_history_audit.json')
def strip_repeated(obj):
    if isinstance(obj,dict):return {k:strip_repeated(v) for k,v in obj.items() if k not in ['full_assistant_content','formal_record','frozen_content','original_content','all_original_frozen_inputs','files','per_marker_roles','results','complete_raw_manual_finals','unique_primary_math_proof','evidence_paths','prior_files']}
    if isinstance(obj,list):return [strip_repeated(v) for v in obj]
    return obj
print(json.dumps({'candidate_render_check':strip_repeated(d['candidate_documents']['render_check.json']),
                 'background20':strip_repeated(d['background20_complete_relevant_history']),
                 'background41':strip_repeated(d['background41']),
                 'references':strip_repeated(d['reference_lessons']),
                 'historical_hash_checks':{k:{a:b for a,b in v.items() if a not in ['matches','unresolved_keys']} for k,v in d['historical_hash_checks'].items()}},ensure_ascii=False,indent=2))
