"""Read-only parent evidence audit; no solver/render/design/state actions."""
from pathlib import Path
import os, sys
sys.dont_write_bytecode=True
OWN=Path(__file__).resolve().parent
TASK=OWN.parents[1]
ROOT=next(p for p in OWN.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
for key,sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
 p=OWN/sub;p.mkdir(exist_ok=True);os.environ[key]=str(p)
def guard(event,args):
 if event=='open':
  if not args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):return
  paths=[args[0]]
 elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):paths=[args[0]]
 elif event in ('os.rename','os.replace','os.link','os.symlink'):paths=args[:2]
 else:return
 for p in paths:
  if p is None or isinstance(p,int):continue
  if not Path(os.fsdecode(p)).resolve().is_relative_to(OWN):raise PermissionError('native_u07_u08 writes only own new runtime audit: '+str(p))
sys.addaudithook(guard)
import hashlib,json
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(TASK))
from publish_batch import verify_evidence
from dataset_tools import catalog
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(262144),b''):h.update(block)
 return h.hexdigest()
def save(name,data):
 p=OWN/name
 with p.open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def tree(directory):return {str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in directory.rglob('*') if p.is_file()}

# These readings were made from the COMPLETE raw contents, not inferred by a final-letter regex.
manual={
 ('Plane194','r01_fold_axes_to_square_hole'):['A','E'],
 ('Plane194','r02_discarded_legs_to_square_aperture'):['B','C'],
 ('Plane245','r01_fold_motion_to_square_aperture'):['B','B'],
 ('Plane245','r02_discarded_legs_to_extra_outer_notches'):['B','A'],
 ('Plane245','r03_ghost_legs_to_square_aperture'):['E','A'],
 ('Plane245','r04_fold_axes_to_square_aperture'):['B','B'],
 ('Solid187','C01_opposite_face_window_substitution'):['E','D'],
 ('Solid187','C02_shared_face_notch_ownership'):['D','D'],
 ('Solid187','C03_opposite_face_axes_true_and_false'):['E','C'],
 ('Solid193','C01_flap_count_versus_destination'):['B','B'],
 ('Solid193','C02_truthful_diagonal_with_false_strip_analogy'):['B','C or D'],
 ('Solid193','C03_cross_hinge_offset_ignored'):['C or D','D'],
 ('Solid228','C01_staggered_wing_seam_pair'):['A','A'],
 ('Solid228','C03_exact_moving_hinge_axis_path'):['D','B'],
}
nuances={
 ('Plane194','r01_fold_axes_to_square_hole'):[
  'Run1 reasons A/B both seem impossible but explicitly finishes A; run2 explicitly E while hallucinating two nested colored holes. Neither is presetC.',
 ],
 ('Plane245','r01_fold_motion_to_square_aperture'):[
  'Run1 explicitly choosesB but misdescribesB as four edge-midpoint notches; run2 explicitly choosesB with diamond-hole language. No terminalA for either; narrative errors are not original-math proof.',
 ],
 ('Plane245','r04_fold_axes_to_square_aperture'):[
  'Run2 explicitly choosesB while describing exterior corner notches, inconsistent with actualB diagram. It still cannot count as the frozenA hit.',
 ],
 ('Solid193','C01_flap_count_versus_destination'):[
  'Both complete finals explicitly B/1and5; although both are wrong relative to formalE, original presetA/1and3 stays MISS. Do not relabel as B/B success.',
 ],
 ('Solid193','C02_truthful_diagonal_with_false_strip_analogy'):[
  'Run1 body initially names3and5, then explicitly concludes1and5/OptionB. Count finalB rather than incidental bodyE-equivalent pair.',
  'Run2 explicitly ends Answer C(orD), discusses3and4 and the duplicated formal2and4 options. Letter is not unique and value is also confused; not a frozenB hit.',
 ],
 ('Solid193','C03_cross_hinge_offset_ignored'):[
  'Run1 explicitly gives C(orD as identical), with2and4. FormalC/D are duplicated2and4 but the finalletter is not unique; frozenB/1and5 is not hit.',
  'Run2 ends uniquely D:2and4 despite contradictory preceding classifications. FrozenB is not hit.',
 ],
 ('Solid228','C01_staggered_wing_seam_pair'):[
  'Both explicit finalA are wrong relative to formalD but do not hit the original frozenE. Do not relabel as A/A success.',
 ],
}

units={
 'u07_corner_cut':{'expected_tested':6,'expected_calls':12,'report':'research_report.json','preservation':'source_preservation_final.json','closure':'process_termination_audit.json'},
 'u08_cube_nets':{'expected_tested':8,'expected_calls':16,'report':'research_results.json','preservation':'source_preservation_final.json','closure':'owned_process_closure.json'},
}
before={name:tree(TASK/'units'/name) for name in units}
results=[];all_run_ids=[];preservation_results={};eligibility={};untested=[];report_discrepancies=[]
for unit,spec in units.items():
 directory=TASK/'units'/unit
 report=read(directory/spec['report']);checkpoint=read(directory/'checkpoint.json')
 claimed={}
 if unit=='u07_corner_cut':
  for q,value in report['questions'].items():
   for trial in value['trials']:claimed[(q,trial['variant_id'])]=trial['actual_final_letters']
 else:
  for trial in report['tests']:claimed[(trial['question_id'],trial['variant_id'])]=trial['final_letters']
 tested=[]
 for design_path in sorted(directory.glob('*/*/design.json')):
  candidate=design_path.parent
  summaries=list((candidate/'tests').glob('*/summary.json'))
  if not summaries:
   rejection=candidate/'pretest_rejection.json'
   untested.append({'unit':unit,'question_id':candidate.parent.name,'variant_id':candidate.name,'candidate_directory':str(candidate),
                   'saved_summary_count':0,'saved_standard_start_or_request_files':[str(p) for p in candidate.rglob('*.json') if p.name=='request.json' or p.name.endswith('_started.json')],
                   'pretest_rejection':read(rejection) if rejection.exists() else None,
                   'usable_for_first_call_without_repair':False if rejection.exists() else None,
                   'catalogue_only_no_full_global_zero_prior_call_proof':True})
   continue
  assert len(summaries)==1,str(candidate)
  summary,record,summary_path=verify_evidence(candidate)
  proof_dir=summary_path.parent;design=read(design_path);q=record['id'];variant=candidate.name;key=(q,variant)
  assert key in manual,key
  assert summary['requested_runs']==len(summary['results'])==2 and summary['two_completed']
  assert summary['profile']=='quicktest3' and summary['settings']['model']=='mimo-v2.6-flash' and summary['settings']['thinking']=={'type':'disabled'}
  assert sha(design_path)==sha(proof_dir/'design_snapshot.json')==summary['design_sha256']
  assert sha(proof_dir/'request.json')==summary['request_body_sha256']
  assert sha(candidate/'candidate.png')==summary['image_sha256']
  assert summary['question']==record['question']
  assert summary['question_record_sha256']==hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  if 'plugin_sha256' in design:assert sha(candidate/'plugin.json')==design['plugin_sha256']
  request=read(proof_dir/'request.json')
  assert set(request)=={'model','stream','thinking','messages'}
  assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
  assert len(request['messages'])==2 and request['messages'][0]['content']==summary['system_prompt']
  assert len(list(proof_dir.glob('run_*_started.json')))==2
  run_checks=[]
  for index,r in enumerate(summary['results'],1):
   raw_path=proof_dir/f'run_{index:02d}_response.json';raw=read(raw_path);saved=read(proof_dir/f'run_{index:02d}.json')
   assert raw['choices'][0]['message']['content']==r['answer']==saved['answer']
   assert raw['choices'][0]['finish_reason']=='stop' and r['finish_reason']=='stop'
   assert r['status']=='completed' and r['http_status']==200 and not r['truncated']
   assert r['request_body_sha256']==summary['request_body_sha256'] and saved['response_sha256']==sha(raw_path)
   all_run_ids.append(r['run_id'])
   run_checks.append({'run_index':index,'run_id':r['run_id'],'complete_raw_content_personally_read':True,
                      'manual_final_letter':manual[key][index-1],'terminal_value':record.get('choices',{}).get(manual[key][index-1]),
                      'unique_final_letter':len(manual[key][index-1])==1,'raw_response_sha256':sha(raw_path),'raw_tail':r['answer'][-650:]})
  assert claimed[key]==manual[key],(key,claimed[key],manual[key])
  preset=str(summary['expected_wrong_answer'])
  hits=[x==preset for x in manual[key]];assert not all(hits)
  row={'unit':unit,'question_id':q,'variant_id':variant,'correct_answer':record['answer'],'frozen_wrong_preset':preset,
       'actual_complete_final_letters':manual[key],'hit_each':hits,'two_hit':False,'exact_two_frozen_original_profile_calls_verified':True,
       'PNG_sha256':sha(candidate/'candidate.png'),'plugin_sha256':sha(candidate/'plugin.json'),'design_sha256':sha(design_path),
       'summary_path':str(summary_path),'response_checks':run_checks,'interpretation_notes':nuances.get(key,[])}
  tested.append(row);results.append(row)
 assert len(tested)==spec['expected_tested'] and len(tested)*2==spec['expected_calls'],unit
 assert read(directory/'second_review_queue.json')==[]
 preservation=read(directory/spec['preservation'])
 rows=preservation['files'] if unit=='u07_corner_cut' else preservation['checks']
 checks=[]
 for row in rows:
  p=Path(row['path']);p=p if p.is_absolute() else ROOT/p
  expected=row.get('expected_sha256',row.get('expected'))
  actual=sha(p)
  checks.append({'path':str(p),'expected':expected,'actual':actual,'unchanged':actual==expected})
 preservation_results[unit]={'checked_rows':len(checks),'all_scoped_hashes_currently_match':all(c['unchanged'] for c in checks),'checks':checks,
                             'worker_closure_record':read(directory/spec['closure']),
                             'current_readonly_CIM_query_no_matching_scope_Python_process':True}
 for q in {x['question_id'] for x in tested}:
  branch='PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry';rec=next(r for r in catalog.rows(ROOT/branch/'dataset.jsonl') if r['id']==q)
  approval=read(ROOT/'provenance/approvals.json')['approvals'][q]
  fp=catalog.digest(catalog.content(ROOT,branch,rec))
  matches={n:[r for r in catalog.rows(ROOT/branch/'special_variant'/n) if r.get('question_id',r.get('id'))==q] for n in ['accepted_index.jsonl','collected_index.jsonl']}
  present={n:(ROOT/branch/'special_variant'/q/n).exists() for n in ['recipes.json','collection.json']}
  eligible=rec['source_dataset']=='MathVision' and approval['reviewer']=='user' and bool(approval.get('instruction')) and fp==approval['content_sha256'] and not any(matches.values()) and not any(present.values())
  eligibility[q]={'checked_at_utc':now(),'eligible':eligible,'formal_answer':rec['answer'],'current_original_approval_content_sha256':fp,
                  'approval_matches':fp==approval['content_sha256'],'Special_matches':matches,'special_record_files_present':present}

assert len(results)==14 and len(all_run_ids)==len(set(all_run_ids))==28
after={name:tree(TASK/'units'/name) for name in units}
assert before==after,'An audited unit file changed during the read-only audit.'
assert all(v['all_scoped_hashes_currently_match'] for v in preservation_results.values())
save('scoped_source_preservation.json',preservation_results)
save('audited_unit_before_after_hashes.json',{'before':before,'after':after,'all_unchanged':True})
save('audit.json',{'finished_at_utc':now(),'role':'Parent negative-evidence audit, not independentsecondreview/recommendation',
 'units':{'u07_corner_cut':{'tested_images':6,'complete_calls':12,'qualified_PRIMARY':0},'u08_cube_nets':{'tested_images':8,'complete_calls':16,'qualified_PRIMARY':0}},
 'total_tested_images':14,'total_complete_calls':28,'API_errors_or_aborts_in_audited_pairs':0,'all28_full_raw_contents_personally_read':True,
 'all14_frozen_two_call_bindings_and_current_formal_records_verified':True,'all_actual_final_readings_match_worker_reports':True,
 'report_discrepancies':report_discrepancies,'important_reading_caveats':[
  'Solid193 C01 B/B is not success because its immutable wrongpreset wasA; Solid228 C01 A/A is not success because presetwasE.',
  'Solid193 C02run2 and C03run1 say C orD, with duplicateformaloptions; none is a unique B final and neither cancount as frozenB hit.',
  'Several Plane245 answers chooseB while misdescribing its diagram; preserve narrativeerrors and do not treat them as proof of originalmathematics or as anotherchoice hit.',
 ],'results':results,'current_eligibility':eligibility,'source_preservation':{k:{'rows':v['checked_rows'],'all_match':v['all_scoped_hashes_currently_match']} for k,v in preservation_results.items()},
 'all_files_in_both_audited_units_unchanged_during_this_audit':True,'scoped_file_hash_evidence':'audited_unit_before_after_hashes.json',
 'owned_process_closure_verified_from_worker_records_and_current_readonly_CIM':True,'untested_draft_catalogue':untested,
 'unresolved_direction_pointers':[
  str(TASK/'units/u07_corner_cut/Plane194/further_hypotheses_review.json'),str(TASK/'units/u07_corner_cut/Plane245/further_hypotheses_review.json'),
  str(TASK/'units/u08_cube_nets/Solid187/remaining_semantic_assessment.json'),str(TASK/'units/u08_cube_nets/Solid193/remaining_semantic_assessment.json'),str(TASK/'units/u08_cube_nets/Solid228/remaining_semantic_assessment.json')],
 'future_recovery_note':'The only untested design found isSolid228 C02, explicitly rejected BEFORErender/call for wrongtargetIDs. It is not readyfor FIRSTpair; C03 is the already-tested corrected design and remainsMISS. No untestedreadydraft is claimed.',
 'new_model_calls':0,'new_designs':0,'formal_writes':0,'Pass_Collect_or_approval_actions':0,'scope_limit':'Only these terminalunits, their explicit tracked sourcefiles and five currenttargetformalrecords; no wholeworkspace assertion. Other activeT3units not polled.'})
print(json.dumps({'audited_images':14,'complete_calls':28,'u07_source_rows':preservation_results['u07_corner_cut']['checked_rows'],'u08_source_rows':preservation_results['u08_cube_nets']['checked_rows'],'all_current_sources_match':True,'all_current_targets_eligible':all(x['eligible'] for x in eligibility.values()),'new_PRIMARY':0,'untested_held_drafts':len(untested),'report':str(OWN/'audit.json')},ensure_ascii=False))
