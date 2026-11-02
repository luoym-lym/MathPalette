from tools72 import *
import shutil

manifest=read(HERE/'initial_snapshot_manifest.json')
meta=[]
for row in manifest:
    p=Path(row['source'])
    if p.parent==BASE and p.name in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json']:
        old=Path(row['snapshot']).read_bytes();new=p.read_bytes()
        meta.append({'path':str(p),'initial_sha256':row['sha256'],'current_sha256':sha(p),'unchanged':old==new,'exact_old_prefix_of_current':new.startswith(old),'classification':'unchanged' if old==new else ('exact-prefix parent append' if new.startswith(old) else 'parent runtime update; diagnostic only'),'old_full_snapshot':row['snapshot']})
        del old,new;gc.collect()
write(HERE/'parent_metadata_diagnostic_initial.json',meta)

source_manifest={str(p):sha(p) for p in (BASE/'background_60').rglob('*') if p.is_file()}
write(HERE/'source_unit60_complete_initial_hashes.json',source_manifest)

refs=[]
for i in range(1,15):
    p=BASE/f'batch_{i:02d}'/'manifest.json'
    data=read(p)
    for c in data['candidates']:
        source=BASE/c['candidate_source']; design=read(source/'design.json')
        refs.append({'batch':i,'question_id':c['question_id'],'mechanism':c['mechanism'],'source':str(source),'manifest_sha256':sha(p),'design_sha256':sha(source/'design.json'),'marker_roles':design.get('marker_roles',design.get('per_marker',[])),'limits':'Read-only information transfer reference. Historical hits and controls do not prove causal gain.'})
        del design;gc.collect()
    del data;gc.collect()
write(HERE/'delivered_information_references.json',refs)
for r in refs:print(r['batch'],r['question_id'],r['mechanism'],flush=True)

bindings=[]
for row in read(HERE/'old_history_inventory.json'):
    p=Path(row['path'])
    if p.name!='binding.json':continue
    data=read(p)
    req=p.parent/'request.json'
    body=read(req)
    content=body['messages'][1]['content'];text_part=next(v['text'] for v in content if v['type']=='text')
    import base64
    png=base64.b64decode(next(v['image_url']['url'] for v in content if v['type']=='image_url').split(',',1)[1])
    bindings.append({'path':str(p),'binding_sha256':sha(p),'question_id':data['question_id'],'request_hash_matches':sha(req)==data['request_body_sha256'],'image_hash_matches':hashlib.sha256(png).hexdigest()==data['image_sha256'],'formal_question_matches':text_part==eligibility(data['question_id'])['record']['question'],'exact_saved_preset':data['expected_wrong_answer'],'design_snapshot_sha256':sha(p.parent/'design_snapshot.json'),'design_hash_matches':sha(p.parent/'design_snapshot.json')==data['design_sha256'],'started_files':[str(x) for x in p.parent.glob('*started.json')],'full_raw_paths':[str(x) for x in p.parent.glob('*_response.json')]})
    del data,body,content,png;gc.collect()
write(HERE/'old_actual_request_binding_audit.json',bindings)
print('old binding rows',len(bindings),flush=True)
