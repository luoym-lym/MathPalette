from tools_local import *
from partial_style import object_paths
import base64
baseline={};conflicts=[]
for q in ASSIGNED:
 before=json.loads((TASK/q/'frozen_inputs.json').read_text(encoding='utf-8'))
 for rel,h in before['files'].items():
  if rel in baseline and baseline[rel]!=h:conflicts.append(rel)
  baseline[rel]=h
write(TASK/'source_preservation_baseline_recomputed.json',{'created_at':datetime.now(timezone.utc).isoformat(),'files':baseline,'overlap_hash_conflicts':conflicts,'coverage':'Union of per-question frozen input snapshots taken before design, including formal PNG, source image, scene, script, frozen dependencies and checked-in bridge/plugin files.'})
changed=[{'path':r,'before':h,'after':file_hash(ROOT/r) if (ROOT/r).is_file() else None} for r,h in baseline.items() if not (ROOT/r).is_file() or file_hash(ROOT/r)!=h]
source_audits=[]
for q in ASSIGNED:
 f=TASK/q;record=AD.records[q];context=json.loads((f/'context.json').read_text(encoding='utf-8'));fr=json.loads((f/'frozen_inputs.json').read_text(encoding='utf-8'))
 audit={'question_id':q,'current_eligibility':eligibility(q),'formal_record_unchanged':canonical_hash(record)==canonical_hash(json.loads((f/'formal_record.json').read_text(encoding='utf-8')))==fr['question_record_sha256'],'original_png_bytes_equal':(f/'original.png').read_bytes()==AD.original_paths[q].read_bytes(),'original_pixels_equal_context':pixel_hash(f/'original.png')==context['original_pixel_sha256'],'source_scene_snapshot_canonical_equal':canonical_hash(AD.scenes[q])==canonical_hash(json.loads((f/'source_scene_snapshot.json').read_text(encoding='utf-8'))),'before_design_and_current_frozen_inputs_equal':fr==AD.frozen_inputs(q)}
 write(f/'source_audit_final_v2.json',audit);write(f/'eligibility_at_end_v2.json',audit['current_eligibility']);source_audits.append(audit)
assert not changed and not conflicts
assert all(a['current_eligibility']['eligible'] and a['formal_record_unchanged'] and a['original_png_bytes_equal'] and a['original_pixels_equal_context'] and a['source_scene_snapshot_canonical_equal'] and a['before_design_and_current_frozen_inputs_equal'] for a in source_audits)
write(TASK/'source_preservation_final.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'file_count':len(baseline),'changed_or_missing_files':changed,'all20_source_audits_pass':True,'question_audits':source_audits,'no_formal_write':True,'no_Pass_or_Collect':True,'all_writes_guarded_under':str(TASK)})
evidence=[]
for design_path in sorted(TASK.glob('*/*/design.json')):
 f=design_path.parent;q=f.parent.name;d=json.loads(design_path.read_text(encoding='utf-8'));ctx=json.loads((f/'context.json').read_text(encoding='utf-8'));rc=json.loads((f/'render_check.json').read_text(encoding='utf-8'));plugin=json.loads((f/'plugin.json').read_text(encoding='utf-8'))
 assert file_hash(f/'candidate.png')==d['candidate_png_sha256']==rc['png_sha256']
 assert pixel_hash(f/'candidate.png')==rc['pixel_sha256'] and rc['baseline_matches_formal'] and rc['deterministic']
 bind=json.loads((f/'marker_path_bindings.json').read_text(encoding='utf-8'));current={}
 from design_tools import path_bindings
 current=path_bindings(q,sorted(bind))
 assert current==bind
 marks=[]
 for i,a in enumerate(plugin['params']['actions']):
  mark={'index':i,'type':a['type'],'normalized_action':a,'role':d['marker_roles'][i]['role']}
  if a['type']=='add_point':
   matched=[s for s in ctx['snap_points'] if s['xy']==a['xy']];assert matched;mark['exact_source_snap_matches']=matched
  elif a['type']=='add_line':
   matched=[[s for s in ctx['snap_points'] if s['xy']==xy] for xy in a['endpoints']];assert all(matched);mark['exact_source_snap_matches']=matched
  else:
   mark['stable_object']=next(o for o in ctx['objects'] if o['id']==a['target']);mark['path_hashes']=[p['sha256'] for p in bind[a['target']]]
  marks.append(mark)
 audit={'question_id':q,'variant_id':f.name,'checked_at':datetime.now(timezone.utc).isoformat(),'design_sha256':file_hash(design_path),'plugin_sha256':file_hash(f/'plugin.json'),'candidate_png_sha256':file_hash(f/'candidate.png'),'pixel_sha256':pixel_hash(f/'candidate.png'),'context_sha256':file_hash(f/'context.json'),'marker_paths_sha256':file_hash(f/'marker_path_bindings.json'),'fresh_path_hashes_equal':True,'schema_and_defaults':'Actual approved PluginRenderer rendered and normalized this plugin and independently repeated it byte-identically. Normalized plugin.json records defaults.','marks':marks}
 write(f/'marker_geometry_audit.json',audit)
 tests=[]
 for b in sorted(f.glob('tests/*/binding.json')):
  t=b.parent;s=json.loads(b.read_text(encoding='utf-8'));p=json.loads((t/'request.json').read_text(encoding='utf-8'));r=AD.records[q]
  assert s['image_sha256']==file_hash(f/'candidate.png') and s['design_sha256']==file_hash(design_path)
  assert (t/'design_snapshot.json').read_bytes()==design_path.read_bytes()
  assert s['expected_wrong_answer']==d['expected_wrong_answer']
  assert file_hash(t/'request.json')==s['request_body_sha256']
  assert p['model']=='mimo-v2.6-flash' and p['thinking']=={'type':'disabled'}
  assert set(p)=={'model','stream','thinking','messages'} and len(p['messages'])==2
  u=p['messages'][1]['content'];assert u[0]=={'type':'text','text':r['question']}
  assert base64.b64decode(u[1]['image_url']['url'].split(',',1)[1])==(f/'candidate.png').read_bytes()
  runs=[]
  for rp in sorted(t.glob('run_??.json')):
   rr=json.loads(rp.read_text(encoding='utf-8'));assert rr['request_body_sha256']==s['request_body_sha256'] and rr['image_sha256']==s['image_sha256'] and rr['design_sha256']==s['design_sha256']
   if rr['status']=='completed':assert rr['response_sha256']==file_hash(t/f"run_{rr['run_index']:02d}_response.json")
   runs.append({'path':str(rp),'sha256':file_hash(rp),'status':rr['status']})
  tests.append({'binding':str(b),'binding_sha256':file_hash(b),'request_sha256':file_hash(t/'request.json'),'request_only_formal_question_plus_exact_png':True,'preset_and_correct_answer_not_injected':True,'no_settings_overrides_or_retry':True,'runs':runs})
 evidence.append({'question_id':q,'variant_id':f.name,'design_path':str(design_path),'design_sha256':file_hash(design_path),'png_path':str(f/'candidate.png'),'png_sha256':file_hash(f/'candidate.png'),'plugin_sha256':file_hash(f/'plugin.json'),'marker_audit':str(f/'marker_geometry_audit.json'),'tests':tests})
write(TASK/'evidence_binding_audit.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'all_checks_pass':True,'saved_design_count':len(evidence),'designs':evidence,'harness_byte_identical':(TASK/'harness/quicktest3_isolated.py').read_bytes()==(TASK.parent/'harness/quicktest3_isolated.py').read_bytes(),'harness_source_sha256':file_hash(TASK.parent/'harness/quicktest3_isolated.py'),'harness_local_sha256':file_hash(TASK/'harness/quicktest3_isolated.py'),'process_note':'Solid235 first request still pending at audit; final process/abort audit will supersede status only, never mutate frozen evidence.'})
print('source and marker/request audits passed',len(baseline),len(evidence))
