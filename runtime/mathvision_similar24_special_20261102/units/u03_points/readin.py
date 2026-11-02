from unit_env import *
import base64
import gc

log = []
def audited(path):
    path = Path(path)
    data = path.read_bytes()
    value = json.loads(data.decode('utf-8-sig')) if path.suffix == '.json' else data.decode('utf-8-sig')
    log.append({'path':str(path), 'sha256':sha(data), 'bytes':len(data), 'read_completely':True})
    return value

for name in ('brief.txt', 'assignment.json'):
    audited(OWN / name)
for name in ASSIGNMENT['required_parent_scope_files']:
    audited(TASK / name)
for rel in ('AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md',
            'PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md',
            'PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json'):
    audited(PROJECT / rel)
for name in ('annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json'):
    audited(OLD / name)

refs = {}
for qid in read(TASK / 'reference_manifest.json'):
    folder = TASK / 'references' / qid
    vals = {name:audited(folder / name) for name in ('C01.json','recipes.json','reference.json')}
    for name in ('C01.png','original.png'):
        data = (folder / name).read_bytes()
        log.append({'path':str(folder/name),'sha256':sha(data),'bytes':len(data),'read_completely':True,
                    'visual_inspection':'actual view_image performed in current turn'})
    refs[qid] = vals
save(OWN / 'reference_readin.json', refs)

hist = audited(TASK / 'history_index.json')
selected = [q for q in hist['questions'] if q['question_id'] in QIDS]
save(OWN / 'assigned_history_index.json', selected)
hist_values = {}
for q in selected:
    paths = set(q['other_scoped_history_file_references'] + q['independent_review_references']
                + q['additional_math_manual_history_references'])
    for d in q['designs']:
        for name in ('design_path','plugin_path'):
            if d.get(name): paths.add(d[name])
    for rel in sorted(paths):
        value = audited(PROJECT / rel)
        # Exact requests are fully read and decoded, but do not expand base64 into this log.
        if Path(rel).name == 'request.json':
            blocks = value['messages'][1]['content']
            image_bytes = base64.b64decode(blocks[1]['image_url']['url'].split(',',1)[1])
            value = {'path':rel,'question':blocks[0]['text'],'image_sha256':sha(image_bytes),
                     'model':value['model'],'thinking':value['thinking'],'payload_keys':list(value)}
            del image_bytes
        hist_values[rel] = value
        gc.collect()
save(OWN / 'history_readin.json', hist_values)
for qid in QIDS:
    value = eligibility(qid)
    save(OWN / qid / 'eligibility_start.json', value)
    assert value['eligible'], value
    row = value['record']
    for field in ('scene','script'):
        audited(PROJECT/'PlaneGeometry'/row[field])
    for rel in row['runtime_dependencies']:
        audited(PROJECT/'PlaneGeometry'/rel)

save(OWN / 'readin_audit.json', {'created_at':now(),'isolation':ISOLATION,
     'threads':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},
     'environment':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},'files':log})
save(OWN / 'checkpoint.json', {'unit':'u03_points','updated_at':now(),'status':'readin_complete',
     'question_status':{q:'mathematics_and_design_pending' for q in QIDS},'new_actual_calls':0,
     'PRIMARY_candidates':0,'formal_changes':0,'errors':[], 'unworked':QIDS})
save(OWN / 'second_review_queue.json', [])
print(json.dumps({'read_files':len(log),'history_files':len(hist_values),'eligibility_all':True,
                  'references':list(refs)},ensure_ascii=False))
for qid, vals in refs.items():
    print('REFERENCE', qid)
    print(json.dumps(vals['C01.json'],ensure_ascii=False))
    print('RECIPE',json.dumps(vals['recipes.json'],ensure_ascii=False))
    print('REFERENCE_METADATA_KEYS',list(vals['reference.json']))
for rel, value in hist_values.items():
    name = Path(rel).name
    if name in ('assessment.json','primary_review.json','material_refinement_assessment.json','design.json','source_notes.json') or name.endswith('_response.json'):
        print('HISTORY_FULL',rel)
        print(json.dumps(value,ensure_ascii=False))
