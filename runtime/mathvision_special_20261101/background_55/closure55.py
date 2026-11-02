from pathlib import Path
import sys,os,json,hashlib,base64
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
# Reuse only the standard-library guard and memory-bounded readers; do not rerun finalization.
prefix=(HERE/'finalize55.py').read_text(encoding='utf-8').split("ids=['Solid195'")[0]
exec(compile(prefix,str(HERE/'finalize55.py'),'exec'))

d=HERE/'Solid195/r55_two_arc_procedure_unit_binding';t=next((d/'tests').iterdir());b=read(t/'binding.json');request=read(t/'request.json');summary=read(t/'summary.json')
assert list(request)==['model','stream','thinking','messages']
assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
assert [m['role'] for m in request['messages']]==['system','user']
assert request['messages'][0]['content']==b['system_prompt']
items=request['messages'][1]['content'];assert len(items)==2 and items[0]['type']=='text' and items[1]['type']=='image_url'
assert items[0]['text']==row(BRANCH/'dataset.jsonl','Solid195')['question']
raw=base64.b64decode(items[1]['image_url']['url'].split(',',1)[1]);assert hashlib.sha256(raw).hexdigest()==sha(d/'candidate.png')==b['image_sha256']
assert sha(d/'design.json')==sha(t/'design_snapshot.json')==b['design_sha256']
assert sha(t/'request.json')==b['request_body_sha256']
assert b['expected_wrong_answer']=='3' and b['requested_runs']==2
assert len(summary['results'])==2 and all(r['status']=='completed' for r in summary['results'])
rawfiles={str(p.relative_to(PROJECT)):sha(p) for p in t.iterdir() if p.is_file()}
write(HERE/'evidence_binding_final.json',dict(checked_at=now(),question_id='Solid195',actual_calls=2,identical_frozen_image_and_immutable_wrong_preset=True,
  model=request['model'],thinking=request['thinking'],only_formal_question_and_PNG_in_user_payload=True,no_profile_token_timeout_override=True,
  image_sha256=sha(d/'candidate.png'),design_sha256=sha(d/'design.json'),request_body_sha256=sha(t/'request.json'),all_raw_files_sha256=rawfiles,
  manual_finals=['7','6'],expected_wrong_answer='3',two_target_hits=False,
  untested_frozen_candidates={q:dict(candidate_sha256=sha(HERE/q/n/'candidate.png'),design_sha256=sha(HERE/q/n/'design.json'),API_calls=0,
      has_process_launch=(HERE/q/n/'process_launch.json').exists(),has_tests=(HERE/q/n/'tests').exists()) for q,n in [('Solid206','r55_equilateral_end_to_ridge_prism_binding'),('Solid207','r55_source_halfside_to_full_panel_scale')]}))
assert not (HERE/'Solid206/r55_equilateral_end_to_ridge_prism_binding/tests').exists()
assert not (HERE/'Solid207/r55_source_halfside_to_full_panel_scale/tests').exists()

delivered=[];refs={}
for i in range(1,15):
    path=BASE/f'batch_{i:02d}/manifest.json';m=read(path);refs[str(path.relative_to(PROJECT))]=sha(path)
    for c in m['candidates']:
        delivered.append(dict(batch=i,question_id=c['question_id'],mechanism=c.get('mechanism'),correct=c.get('correct_answer'),preset=c.get('expected_wrong_answer'),quality_review=c.get('quality_review')))
rejects=[]
for folder in ['Solid220_false_face_pair','Plane263_v01','Plane192_v03','Plane233_two_U_partial_partition_binding','Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly']:
    path=BASE/'independent_review'/folder/'independent_review.json';v=read(path);refs[str(path.relative_to(PROJECT))]=sha(path)
    rejects.append(dict(path=str(path.relative_to(PROJECT)),decision=v.get('decision'),human_relevant_objections={k:v[k] for k in ['reason','strict_conclusion','human_semantics','human_semantics_disposition','concrete_objections'] if k in v}))
for path in [BASE/'background_16/primary_math_proofs.json',BASE/'background_03/solid_worker/checkpoint.json',BASE/'annotation_semantics_lessons_20261102.json',BASE/'annotation_semantics_lesson_plane242_r24_20261102.json']:
    refs[str(path.relative_to(PROJECT))]=sha(path)
write(HERE/'support_references_reviewed.json',dict(checked_at=now(),reference_hashes=refs,delivered_information_correspondence_examples=delivered,
  exact_reject_semantics=rejects,
  native_reference_images_viewed=['All8 current formalPNG/sourceJPG','Old208triangle/210height-slant','Both96rim designs'],
  applied_lessons=['No whole-choice salience. Each195fragment belongs to one genuine quarter in a defined2-arc group; each206rim edge defines a congruent end-face area or a specific length role;207has two open scale counterparts.',
    'Numerical geometry does not acquire a new printed-pattern matching constraint merely because a real edge has color. Case-specific shape/count/material identities remain frozen.',
    'Same-color partial feature does not assert equality or change a fixed cut plane. Hence208fake-midpoint proposal skipped, and210oldDmechanism not repackaged.',
    'Old whole-rim-to-volume96designs and163white-count proposals are preserved as misses/screens rather than migrated under new IDs.']))

cp=read(HERE/'checkpoint.json');cp['evidence_binding_final']=str((HERE/'evidence_binding_final.json').relative_to(PROJECT));cp['support_references_reviewed']=str((HERE/'support_references_reviewed.json').relative_to(PROJECT))
cp['process_closure']['live_count']=read(HERE/'process_audit_final.json')['live_count'];assert cp['process_closure']['live_count']==0
cp['raw_binding_audit']=str((HERE/'evidence_binding_final.json').relative_to(PROJECT))
with (HERE/'checkpoint.json').open('w',encoding='utf-8',newline='\n') as f:json.dump(cp,f,ensure_ascii=False,indent=2);f.write('\n')
manifest={str(p.relative_to(HERE)):sha(p) for p in HERE.rglob('*') if p.is_file() and not any(x in p.relative_to(HERE).parts for x in ['tmp','mpl_cache','cache','render_tmp','mplconfig','mplcache'])}
write(HERE/'artifact_hashes_final.json',dict(checked_at=now(),files_sha256=manifest,all_new_paths_under_ownroot=True,
  source_manifest_sha256=sha(HERE/'source_preservation_final.json'),old_evidence_manifest_sha256=sha(HERE/'old_evidence_preservation_final.json'),
  frozen_binding_manifest_sha256=sha(HERE/'evidence_binding_final.json'),checkpoint_sha256=sha(HERE/'checkpoint.json'),queue_sha256=sha(HERE/'second_review_queue.json')))
print(json.dumps(dict(checkpoint_sha256=sha(HERE/'checkpoint.json'),source_manifest_sha256=sha(HERE/'source_preservation_final.json'),old_evidence_manifest_sha256=sha(HERE/'old_evidence_preservation_final.json'),new_binding_manifest_sha256=sha(HERE/'evidence_binding_final.json'),artifact_manifest_sha256=sha(HERE/'artifact_hashes_final.json'),own_API_live_count=0),ensure_ascii=False))
