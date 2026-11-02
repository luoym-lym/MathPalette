from env71 import *
import gc

protocols = ['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
refs = ['background_71_brief.txt','background_71_assignment.json','background_59_brief.txt','background_59_assignment.json','annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','selection58_59_parent_eligibility.json','preparation58_59.json']
mutable = ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','master_progress.json']
snapshots = []
hashes = {}
for rel in protocols+['runtime/mathvision_special_20261101/'+n for n in refs+mutable]:
    path = PROJECT/rel
    if not path.is_file(): continue
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    target = OWN/'readin_snapshots'/rel.replace('/','__')
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists(): raise RuntimeError('Refuse overwrite read-in snapshot')
    target.write_bytes(raw)
    snapshots.append({'path':rel,'bytes':len(raw),'sha256':digest,'snapshot':str(target),'mutable_parent_metadata':path.name in mutable})
    hashes[rel] = digest
    del raw
save('readin_snapshots.json', snapshots)
a71 = read(BASE/'background_71_assignment.json')
a59 = read(BASE/'background_59_assignment.json')
source_map = {q['question_id']:q for q in a59['questions']}
comparison = {}
for q in a71['questions']:
    qid = q['question_id']
    comparison[qid] = q['source_assignment_question']==source_map[qid]
save('source_assignment_full_read_audit.json', {'at':now(),'full_source_parsed':True,'full_source_sha256':sha(BASE/'background_59_assignment.json'),'source_question_keys':list(source_map),'assigned_subtrees_equal_to_fully_read_71':comparison,'source_metadata':{k:v for k,v in a59.items() if k!='questions'}})
history59 = read(BASE/'background_59/old_history_manifest.json')
history = {q:list(history59[q]) for q in QIDS+['Solid185']}
for q in history:
    for path in (BASE/'background_59'/q).rglob('*'):
        if path.is_file(): history[q].append(str(path.relative_to(PROJECT)))
    history[q] = sorted(set(history[q]))
save('old_history_manifest.json',history)
for q in QIDS:
    current = eligibility(q)
    expected = next(x for x in a71['questions'] if x['question_id']==q)['source_assignment_question']['source_inputs']
    exact = {}
    for field in ('formal_png','original','scene','script'):
        path = Path(expected[field+'_path'])
        actual = sha(path)
        exact[field] = {'path':str(path),'expected':expected[field+'_sha256'],'actual':actual,'matches':actual==expected[field+'_sha256']}
        hashes[str(path.relative_to(PROJECT))]=actual
    current['source_assignment_hash_checks']=exact
    save(f'{q}/eligibility_start.json',current)
    save(f'{q}/formal_record.json',current['formal_record'])
    for dependency in current['formal_record']['runtime_dependencies']:
        p=PROJECT/'SolidGeometry'/dependency
        hashes[str(p.relative_to(PROJECT))]=sha(p)
    print(q,'approval',current['approval_matches'],'eligibility',current['eligible'],'source hashes',all(x['matches'] for x in exact.values()),flush=True)
    del current
save('readonly_hashes_start.json',hashes)
save('isolation.json',{'at':now(),'ownroot':str(OWN),'strict_guard_before_project_imports':True,'environment':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},'configuration':'inherited; no provider/model/options override','API_calls':0})
save('checkpoint.json',{'unit':'background_71','stage':'source_history_review','scope':QIDS,'assessed_question_ids':[],'unworked_question_ids':QIDS,'new_API_calls':0,'own_live_API_processes':[]})
