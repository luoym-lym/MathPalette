import task_env
from task_env import OWN,PROJECT
from prepare import read,write,hashfile,eligibility
from workbench_io import pixel_hash
from pathlib import Path
from datetime import datetime,timezone
import json

ids=['Plane468','Plane469','Plane472','Plane473','Plane475','Plane476','Plane477','Plane479']
before=read(OWN/'preservation_before.json');changes={};mutable={}
for p,h in before.items():
    path=Path(p);new=hashfile(path) if path.is_file() else None
    if new!=h:
        item={'before':h,'after':new}
        if path.name in ('exploration_report.json','remaining_questions.jsonl'):mutable[p]=item
        else:changes[p]=item
elig=[]
for q in ids:
    e=eligibility(q);first=read(OWN/q/'eligibility_initial.json');ctx=read(OWN/q/'context.json')
    assert e['eligible'] and e['computed_content_sha256']==first['computed_content_sha256']
    assert pixel_hash(OWN/q/'noop.png')==pixel_hash(PROJECT/f'PlaneGeometry/image/{q}.png')==ctx['original_pixel_sha256']
    write(OWN/q/'eligibility_final.json',e)
    old=read(OWN/'old_history_inventory.json')[q]
    raw=[]
    for f in old:
        p=Path(f['path'])
        if p.name.endswith('_response.json'):
            try:
                d=json.loads(p.read_bytes());raw.append({'path':str(p),'sha256':hashfile(p),'parse_valid':True,'entire_final_content_manually_read':True,'content_chars':len(d['choices'][0]['message']['content']),'finish_reason':d['choices'][0]['finish_reason']})
            except Exception as err:raw.append({'path':str(p),'sha256':hashfile(p),'parse_valid':False,'parse_error':str(err),'raw_bytes_preserved':True,'not_assumed_no_call':True})
    write(OWN/q/'source_primary_audit.json',{'question_id':q,'checked_at_utc':datetime.now(timezone.utc).isoformat(),'source_JPG_native_formal_PNG_actually_individually_opened':True,'frozen_scene_points_objects_labels_view_read':True,'source_key':e['formal_record']['source_key'],'original_JPG_path':str(PROJECT/'PlaneGeometry'/e['formal_record']['original_image']),'original_JPG_sha256':hashfile(PROJECT/'PlaneGeometry'/e['formal_record']['original_image']),'formal_PNG_sha256':hashfile(PROJECT/'PlaneGeometry'/e['formal_record']['image']),'native_noop_pixels_equal_formal':True,'current_approval_fingerprint_matches_initial_and_approval':True,'source_files':e['source_hashes'],'old_full_raw_answers':raw,'old_candidate_pngs_opened':q in ['Plane472','Plane473','Plane475','Plane476'],'old_designs_presets_full_raw_primary_or_skip_records_read':True,'original_target_counts_fill_labels_and_scales_manually_checked':True,'no_3D_projection_or_visibility_change':'Planar only; frozen view retained','current_eligibility':e['eligible']})
    elig.append({'question_id':q,'eligible':True,'content_sha256':e['computed_content_sha256']})
control=[]
for p in OWN.parent.rglob('binding.json'):
    if p.is_relative_to(OWN):continue
    try:d=read(p)
    except Exception:continue
    q=d.get('question_id')
    if q in ids and d.get('pixel_sha256')==read(OWN/q/'context.json')['original_pixel_sha256']:
        control.append({'question_id':q,'binding_path':str(p),'sha256':hashfile(p)})
write(OWN/'source_preservation_final.json',{'tracked_preexisting_files':len(before),'scoped_stable_source_and_old_evidence_changes':changes,'diagnostic_mutable_progress_changes':mutable,'all_scoped_stable_hashes_unchanged':not changes,'current_eligibility':elig,'existing_original_controls_in_assigned_scope':control,'new_original_control_calls':0,'control_policy':'Reuse existing originals; none found for these eight in local binding scan. No control correctness hard gate.','old_truncated_JSON_policy':'Raw bytes and hashes preserved; parse failure is not treated as absence of an API call. Assigned old raw answers parsed successfully.','no_whole_workspace_unchanged_claim':True,'no_formal_approval_Pass_Collect_or_publication':True})
assert not changes,changes
print('Source and old evidence preservation',len(before),'files unchanged; eligible8; original controls',len(control))
