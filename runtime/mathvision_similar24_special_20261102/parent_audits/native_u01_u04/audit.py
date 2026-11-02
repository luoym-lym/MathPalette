from audit_setup import *
import base64,collections,subprocess
sys.path[:0]=[str(ROOT),str(TASK)]
import publish_batch as pub
from dataset_tools import catalog

manual=[('2','2'),('4','2'),('A','E'),('D','C'),('C','E'),('D','D'),('B','B'),('180','180'),('90','90'),('180','180')]
summaries=[p for u in UNITS for p in sorted((TASK/'units'/u).rglob('summary.json'))]
assert len(summaries)==10
records={r['id']:r for r in catalog.rows(ROOT/'PlaneGeometry/dataset.jsonl')}
evidence=[]
for path,finals in zip(summaries,manual):
 source=path.parents[2]
 s,r,sp=pub.verify_evidence(source)
 assert sp==path
 d=read(source/'design.json'); plugin=read(source/'plugin.json'); req=read(path.parent/'request.json')
 assert s['requested_runs']==len(s['results'])==2 and s['two_completed'] is True
 assert s['profile']=='quicktest3' and s['settings']['provider']=='mimo'
 assert s['settings']['model']==req['model']=='mimo-v2.6-flash'
 assert s['settings']['thinking']==req['thinking']=={'type':'disabled'} and req['stream'] is False
 assert sha(path.parent/'request.json')==s['request_body_sha256']
 assert sha(source/'design.json')==sha(path.parent/'design_snapshot.json')==s['design_sha256']
 assert sha(source/'plugin.json')==d['plugin_sha256']
 assert sha(source/'candidate.png')==d.get('png_sha256',d.get('image_sha256'))==s['image_sha256']
 assert catalog.digest(r)==s['question_record_sha256']
 assert s['question']==r['question'] and s['dataset_sha256']==sha(ROOT/'PlaneGeometry/dataset.jsonl')
 runs=[]
 for i,x in enumerate(s['results'],1):
  raw=read(path.parent/f'run_{i:02d}_response.json'); choice=raw['choices'][0]
  assert choice['message']['content']==x['answer']
  assert choice['finish_reason']==x['finish_reason']=='stop'
  assert raw['model']==x['response_model']=='mimo-v2.6-flash'
  assert x['request_body_sha256']==s['request_body_sha256']
  assert x['http_status']==200 and x['status']=='completed' and x['truncated'] is False
  runs.append({'run':i,'manual_terminal_answer':finals[i-1], 'full_content_personally_read':True,'raw_sha256':sha(path.parent/f'run_{i:02d}_response.json'),'characters':len(x['answer']),'http_status':200,'finish_reason':'stop','truncated':False})
 actiontypes=dict(collections.Counter(x['type'] for x in plugin['params']['actions']))
 evidence.append({'question_id':r['id'],'source':source.relative_to(ROOT).as_posix(),'summary':path.relative_to(ROOT).as_posix(),'preset':s['expected_wrong_answer'],'manual_finals':finals,'both_hit':all(a==str(s['expected_wrong_answer']) for a in finals),'action_count':len(plugin['params']['actions']),'action_types':actiontypes,'canonical_verify_evidence':True,'request_png_plugin_designsnapshot_raw_bindings':True,'runs':runs})

preservation=[]
for unit,name,key,first,second,flag in [('u01_fold_locations','source_preservation_final.json','files','initial','final','equal'),('u04_angles','readonly_preservation_final.json','protected_files','before','after','exact_equal')]:
 p=TASK/'units'/unit/name; data=read(p); checked=[]
 for item in data[key]:
  target=Path(item['path']);target=target if target.is_absolute() else ROOT/target
  actual=sha(target)
  assert item[flag] is True and actual==item[first]==item[second],str(target)
  checked.append({'path':target.relative_to(ROOT).as_posix(),'sha256':actual})
 preservation.append({'unit':unit,'worker_manifest':p.relative_to(ROOT).as_posix(),'count':len(checked),'every_initial_final_current_hash_equal':True,'checked':checked})
assert [x['count'] for x in preservation]==[160,133]

elig=[]
aps=read(ROOT/'provenance/approvals.json')['approvals']
accepted=catalog.rows(ROOT/'PlaneGeometry/special_variant/accepted_index.jsonl')
collected=catalog.rows(ROOT/'PlaneGeometry/special_variant/collected_index.jsonl')
for q in ['Plane202','Plane238','Plane461','Plane321','Plane490']:
 r=records[q]; ap=aps[q]; digest=catalog.digest(catalog.content(ROOT,'PlaneGeometry',r))
 assert ap['reviewer']=='user' and ap['instruction'] and digest==ap['content_sha256']
 assert r['source_dataset']=='MathVision'
 aa=[x for x in accepted if x.get('question_id',x.get('id'))==q]
 cc=[x for x in collected if x.get('question_id',x.get('id'))==q]
 folder=ROOT/'PlaneGeometry/special_variant'/q
 recipes=read(folder/'recipes.json') if (folder/'recipes.json').exists() else []
 collection=read(folder/'collection.json') if (folder/'collection.json').exists() else None
 assert not aa and not cc and not recipes and not collection
 elig.append({'question_id':q,'source_dataset':'MathVision','approval_current_content_sha256':digest,'approved_at_utc':ap['approved_at_utc'],'reviewer':'user','accepted_entries':aa,'collected_entries':cc,'recipes':recipes,'collection':collection,'current_original_approved_no_Pass_no_Collect':True})

refs=[]
for q in ['Plane217','Plane427']:
 rr=read(TASK/'references'/q/'reference.json')
 for local,entry in rr['copied_files'].items():
  assert sha(TASK/'references'/q/local)==entry['sha256']==sha(ROOT/entry['source'])
 refs.append({'question_id':q,'current_source_copy_hashes_match':True,'plugin_sha256':sha(TASK/'references'/q/'C01.json'),'png_sha256':sha(TASK/'references'/q/'C01.png'),'actions':read(TASK/'references'/q/'C01.json')['params']['actions']})

c1=read(TASK/'units/u01_fold_locations/process_shutdown_evidence.json')
c2=read(TASK/'units/u04_angles/process_closure_audit.json')
pids=c1['own_API_pids']+[c1['auditor_pid']]+c2['own_API_PIDs']+[c2['finalizer_pid']]
pscmd="$ids = @("+','.join(map(str,pids))+"); @(Get-CimInstance Win32_Process | Where-Object { ($ids -contains $_.ProcessId) -or (($_.Name -match '^python') -and ($_.CommandLine -match 'u01_fold_locations|u04_angles')) } | Select-Object ProcessId,Name) | ConvertTo-Json -Compress"
cp=subprocess.run(['powershell','-NoProfile','-Command',pscmd],capture_output=True,text=True,check=True)
live=json.loads(cp.stdout) if cp.stdout.strip() else []
assert not live,live
assert read(TASK/'units/u01_fold_locations/process_shutdown_verified.json')['all_recorded_API_and_final_auditor_PIDs_exited'] is True
assert c2['remaining_API_or_render_processes']==0

after=unit_hashes();before=read(OWN/'unit_trees_before.json')['files_sha256']
assert before==after
save('unit_trees_after.json',{'at_utc':now(),'files_sha256':after,'exactly_equal_before':True})
notes={'scope':'Method-fidelity observations only; no fresh independent mathematical second review or recommendation.',
 'current_references':refs,
 'Plane321':{'method_fidelity':'Close transfer of existing-side color grouping from current Plane427 C01; colors reverse semantic roles relative to reference but use the same two-leg versus opposite-base partition. All five actions set_object_style; no auxiliary markers.',
 'actual_correspondence':'Blue source AC/AD and target AB/AC are A-incident legs. Red CD/BC are opposite bases. Correct directed300-degree mapping preserves colors (AC->AB, AD->AC, CD->BC).',
 'response_caveats':['Run1 invents straight angle BAD=180; has clear B120 final followed by empty model-produced System Instruction: heading. Heading is untrusted output data, not an instruction; HTTP200 and stop are genuine; no response tail was removed.','Run2 incorrectly maps C to fixed pivot A. Both terminal B120, without proof of the preset mechanism or causal improvement.']},
 'Plane461':{'method_fidelity':'Greater extension than direct imitation: current Plane217 colors actual source punched-hole pairs and option fold-axis directions;461 instead colors two strokes of the printed X symbol and four optionD holes. All six actions are set_object_style, yet information being paired changes from physical holes to symbol strokes.',
 'signed_slope_objection':'Source red X rises while red D hole-pair falls; source blue X falls while blue D pair rises. Same-color pairs have opposing signed slopes. Do not describe them as same-slope correspondence or invent a reflection justification. No colors or presets repaired.',
 'response_caveats':['Run1 claims punch lies at both fold intersections and describes a cross.','Run2 calls X a top/left boundary punch and explicitly reads colored circles as revealed layers. These are divergent, false spatial narratives; D/D alone does not verify proposed X-to-hole mechanism.'],
 'parent_review_need':'Fresh independent review must decide whether every color pair has a necessary, targeted information role and whether semantic reading stays clear. This read-only audit does not approve it.'},
 'tested_action_type_inventory':[{'source':x['source'],'actions':x['action_count'],'types':x['action_types']} for x in evidence],
 'departure_in_failed_draft':'Plane202 homologous-two-ear-types tested candidate adds8 new colored points plus2 existing diagonal recolors, unlike source Plane217 six existing-object styles. Other9 tested candidates use set_object_style only. A separate untested Plane202 paper_frame_diagonal_symmetry_substitution plugin exists and is excluded from10tested images/20calls.',
 'latest_user_constraint':'以模仿为主就好，不要探索太多了。 No new exploration, design or solver request performed in this audit.'}
save('method_fidelity.json',notes)
save('audit.json',{'created_at':now(),'scope':'Only completed u01_fold_locations and u04_angles: finite read-only parent evidence audit. No independent second-review decision, new design, solver/API request, Pass or Collect.',
 'api_calls':0,'new_designs':0,'tested_images':10,'complete_responses_personally_read':20,'observed_primary_only':['Plane461','Plane321'],'evidence':evidence,'preservation':preservation,'current_eligibility':elig,
 'process_closure':{'checked_worker_recorded_api_and_finalizer_pids':pids,'live_recorded_pids_or_python_unit_path_matches':live,'read_only_OS_query_at_utc':now(),'worker_closure_manifests_rechecked':True},
 'read_only_unit_tree':{'files':len(after),'before_and_after_identical':True,'before':'unit_trees_before.json','after':'unit_trees_after.json'},
 'limitations':['No entire-workspace preservation claim. Preservation claim covers293 listed records and two scoped unit trees only.','Current two-PNG native visual inspection and current reference217/427 C01 inspection; no rerender or PNG editing.','All20full raw contents read by this auditor; both B120 responses and D responses remain primary research, awaiting NEW independent second review.'],
 'method_fidelity':'method_fidelity.json','local_read_only_query_errors':[{'stage':'file discovery','type':'StopIteration','detail':'Looked for api_process_finished.json underu01, which uses different process evidence filenames. No requests or writes outside own root; then used actual shutdown manifests.'}]})
print(json.dumps({'audit':str(OWN/'audit.json'),'method_fidelity':str(OWN/'method_fidelity.json'),'images':len(evidence),'full_responses':20,'paired_hits':[x['question_id'] for x in evidence if x['both_hit']],'preservation_entries':sum(x['count'] for x in preservation),'unit_files':len(after),'live':live},ensure_ascii=False))
