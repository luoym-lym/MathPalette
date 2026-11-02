from review_env import *
import ast, base64, copy
from dataset_tools import catalog
BASE=ROOT/'runtime/mathvision_special_20261101'
CAND=BASE/'background_37/Solid126/r37_local_area_replacement'
OLD=BASE/'background_14/Solid126/remaining_height_to_cut_binding'
TEST=next((CAND/'tests').iterdir())
BRANCH=ROOT/'SolidGeometry'
row=next(r for r in catalog.rows(BRANCH/'dataset.jsonl') if r['id']=='Solid126')
content=catalog.content(ROOT,'SolidGeometry',row)
approval_data=read(ROOT/'provenance/approvals.json')
approval=approval_data['Solid126'] if 'Solid126' in approval_data else approval_data['approvals']['Solid126']
special={}
for name in ('accepted_index.jsonl','collected_index.jsonl'):
    p=BRANCH/'special_variant'/name
    special[name]={'path':str(p),'sha256':sha(p),'question_records':[r for r in catalog.rows(p) if r.get('question_id',r.get('id'))=='Solid126']}
for name in ('recipes.json','collection.json'):
    p=BRANCH/'special_variant/Solid126'/name
    special[name]={'path':str(p),'exists':p.exists(),'content':read(p) if p.exists() else None}
eligible={'checked_at':stamp(),'formal_record':row,'formal_record_canonical_sha256':catalog.digest(row),'approval':approval,'recomputed_content':content,'recomputed_content_sha256':catalog.digest(content),'approval_matches_current':catalog.digest(content)==approval['content_sha256'],'special_records':special,'special_question_directory_exists':(BRANCH/'special_variant/Solid126').exists()}
save('authoritative_eligibility.json',eligible)
paths={ROOT/'AGENTS.md',ROOT/'MATHPALETTE_PROTOCOL.md',BRANCH/'REDRAW_PROTOCOL.md',BRANCH/'dataset_generator/protocol.json',BRANCH/'workbench/README.md',BRANCH/'workbench/agent_prompt.md',BRANCH/'workbench/plugin.schema.json',BRANCH/'dataset.jsonl',ROOT/'question_bank.jsonl',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json',ROOT/'dataset_tools/catalog.py',ROOT/'dataset_tools/question_review.py',ROOT/'dataset_tools/geometry_dataset.py'}
paths.update(BRANCH/rel for rel in content['files'] if not rel.startswith('..'))
paths.update(ROOT/rel for rel in read(CAND/'render_check.json')['frozen_inputs']['files'])
paths.update((BASE/'background_37/Solid126').rglob('*'))
paths.update((BASE/'background_14/Solid126').rglob('*'))
paths.update(BRANCH/'special_variant'/name for name in ('accepted_index.jsonl','collected_index.jsonl'))
paths.update(BRANCH/'workbench'/name for name in ('quick_test.py','config.json','render_plugins.py','renderer_adapter.py','partial_style.py','workbench_io.py'))
extra=['Solid126_r37_local_area_replacement_independent_review_brief.txt','Solid126_r37_local_area_replacement_parent_binding_precheck.json','annotation_semantics_lesson_plane242_r24_20261102.json','background_37/checkpoint.json','background_37/second_review_queue.json','background_37/final_verification.json','background_37/independent_primary_math_audit.json','background_37/run37.py']
paths.update(BASE/p for p in extra)
references=[]
for prefix in ('Solid128','Solid197','Plane192','Plane233','Plane242'):
    for p in (BASE/'independent_review').glob(prefix+'*/independent_review.json'):
        paths.add(p);references.append(p)
paths.update(p for p in (BASE/'batch_12').glob('*.json') if any(x in p.name for x in ('checkpoint','manifest','delivery')))
files={str(p.relative_to(ROOT)).replace('\\','/'):{'sha256':sha(p),'size':p.stat().st_size,'mtime_ns':p.stat().st_mtime_ns} for p in sorted(paths) if p.is_file()}
save('read_only_inputs_before.json',{'created_at':stamp(),'files':files,'absent_special_paths':[str(BRANCH/'special_variant/Solid126'/name) for name in ('recipes.json','collection.json')]})
save('isolation.json',{'pid':os.getpid(),'python':sys.version,'executable':sys.executable,'argv':sys.argv,'isolation':ISOLATION,'env':{k:os.environ[k] for k in ('TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONDONTWRITEBYTECODE')},'sys_dont_write_bytecode':sys.dont_write_bytecode})
def prune(v):
    if isinstance(v,dict):
        return {k:prune(val) for k,val in v.items() if not any(t in k.lower() for t in ('sha256','hash','artifact','manifest','fingerprint','evidence_files','read_only','source_integrity','file_inventory'))}
    if isinstance(v,list): return [prune(x) for x in v]
    return v
selected={}
for name in ('checkpoint.json','second_review_queue.json','final_verification.json','independent_primary_math_audit.json'):
    v=read(BASE/'background_37'/name)
    def extract(x):
        if isinstance(x,dict):
            if x.get('question_id')=='Solid126': return x
            return {k:extract(val) for k,val in x.items() if k=='Solid126' or (isinstance(val,(dict,list)) and 'Solid126' in json.dumps(val,ensure_ascii=False))}
        if isinstance(x,list):return [extract(val) for val in x if isinstance(val,(dict,list)) and 'Solid126' in json.dumps(val,ensure_ascii=False)]
        return x
    selected[name]={'top_level_summary':{k:v for k,v in v.items() if not isinstance(v,(dict,list))},'Solid126':extract(v)}
selected['parent_precheck']=read(BASE/'Solid126_r37_local_area_replacement_parent_binding_precheck.json')
selected['annotation_semantics_lesson']=read(BASE/'annotation_semantics_lesson_plane242_r24_20261102.json')
save('selected_primary_history_and_references.json',selected)
refout={str(p.relative_to(BASE)):prune(read(p)) for p in references}
save('reference_reviews_semantic_content.json',refout)
print('ELIGIBILITY',json.dumps({k:v for k,v in eligible.items() if k!='recomputed_content'},ensure_ascii=False,indent=2))
print('SOURCE_NOTES',json.dumps(content['source_notes'],ensure_ascii=False,indent=2))
print('PRIMARY_EXTRACT',json.dumps(selected,ensure_ascii=False,indent=2))
print('REFERENCE_FIELDS',[(k,list(v)) for k,v in refout.items()])
print('SNAPSHOT_FILE_COUNT',len(files),'BLOCKED',BLOCKED,'PID',os.getpid())
