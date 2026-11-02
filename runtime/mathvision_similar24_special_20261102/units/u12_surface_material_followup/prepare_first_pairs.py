from bootstrap import *
import shutil,difflib
source=TASK/'followup_surface_offline'
r=read(source/'hypothesis_report.json')
assert r['new_solver_API_calls']==0 and len(r['hypotheses'])==2
pres=read(source/'source_preservation_final.json')
assert pres['tracked_files']==87 and pres['all_tracked_files_match']
assert all(sha(Path(p))==h for p,h in pres['files_sha256'].items())
assert not read(source/'offline_process_closure.json')['any_owned_live_request']
assert all(sha(source/p)==h for p,h in read(source/'artifact_hashes_final.json').items())
entries=[]
for h in r['hypotheses']:
 q=h['question_id'];src=Path(h['directory']);d=OWN/q/h['variant_id'];d.mkdir(parents=True,exist_ok=False)
 assert h['fresh_separate_process_exact_replay_pass'] and h['new_API_calls']==0
 assert h['PNG_sha256']==sha(src/'candidate.png')
 assert read(src/'design.json')['expected_wrong_answer']==h['tentative_wrong_answer']
 e=eligibility(q);save(d/'eligibility_before_copy.json',e)
 copied=[]
 for p in src.iterdir():
  if not p.is_file():continue
  shutil.copyfile(p,d/p.name);assert sha(d/p.name)==sha(p)
  copied.append({'file':p.name,'sha256':sha(p)})
 extra=d/'source_offline_evidence';extra.mkdir()
 for name in ['context.json','native_scene_snapshot.json','fresh_eligibility.json','no_op_audit.json']:
  p=source/q/name;shutil.copyfile(p,extra/name);assert sha(extra/name)==sha(p)
 replay=Path(h['replay_path']);shutil.copyfile(replay,extra/'source_replay_verification.json')
 assert read(replay)['png_sha256']==sha(d/'candidate.png')
 save(d/'reuse_provenance.json',{'at_utc':now(),'source_directory':str(src),'original_variant_id':h['variant_id'],'source_created_at_utc':read(src/'design.json')['created_at_utc'],'wrong_preset':h['tentative_wrong_answer'],'wrong_value':h['tentative_wrong_value'],'type':'Byte-identical never-called offline draft; FIRST actualpair only, not a retry or new image.','copied_files_sha256':copied,'all_existing_source_bytes_preserved':True,'source_replay_record':str(replay),'source_87_hashes_unchanged':True,'old_u05_failed_inputs_and_presets_preserved':True,'source_status_zero_calls_is_frozen_creation_time_not_a_live_counter':True})
 save(d/'parent_primary_pretest_assessment.json',{'at_utc':now(),'actual_native_candidate_PNG_personally_viewed':True,'formal_source_JPG_personally_viewed':True,'every_marker_roles_personally_read':True,'math_and_difference_proofs_personally_read':True,'allowed':'Fresh localcopyreplay and samequestion+PNG zero-prior-call gate then FIRST exact2 original quicktest3 calls.','not_independent_review_or_qualification':True,'human_semantics':'Only existing original edges are styled; no fill,text,number,geometry,newcut or paintedsubset is introduced. All marks contribute to explicit complete open paths or three spatial arms; true original unique answer remains.','specific_information':h['mechanism'],'substantive_difference':h['substantive_difference'],'limits':h['limitation']})
 entries.append({'question_id':q,'variant_id':h['variant_id'],'candidate_directory':str(d),'expected_wrong_answer':h['tentative_wrong_answer'],'expected_wrong_value':h['tentative_wrong_value'],'PNG_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json')})
save('first_pair_candidates.json',entries)
save('assignment.json',{'at_utc':now(),'execution':'parent_direct_FIRSTpairs_of_new_material_offline_drafts; no T3 u12 delegate exists','scope':['Solid186','Solid226'],'frozen_candidates':entries,'source_hypothesis_report':str(source/'hypothesis_report.json'),'source_hypothesis_report_sha256':sha(source/'hypothesis_report.json'),'canonical_source':str(OLD/'harness/quicktest3_isolated.py'),'exact_two_calls_per_image':True,'new_independent_review_required_if_two_hits':True,'formal_writes':0})
raw=(OLD/'harness/quicktest3_isolated.py').read_bytes();before=b'PROJECT = Path(__file__).resolve().parents[3]';after=('PROJECT = Path('+repr(ROOT.as_posix())+')').encode()
assert raw.count(before)==1
local=raw.replace(before,after);assert local.replace(after,before)==raw
harness=OWN/'harness';harness.mkdir(exist_ok=False);(harness/'quicktest3_isolated.py').write_bytes(local)
save('harness_relocation_audit.json',{'at_utc':now(),'original_sha256':sha(OLD/'harness/quicktest3_isolated.py'),'local_sha256':sha(harness/'quicktest3_isolated.py'),'inverse_byte_replacement_exact':True,'only_change':'Local PROJECT resolution; original profile/model/thinking/systemprompt/question/payload/API/no-token/no-timeout/retry unchanged.'})
(OWN/'harness_relocation.patch').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),local.decode().splitlines(True))),encoding='utf-8')
print(json.dumps({'copied':entries,'all_API_calls_so_far_here':0},ensure_ascii=False))
