from tools24 import *
def history(qid):
    files=[p for p in BASE.rglob('*') if p.is_file() and not p.is_relative_to(HERE) and (qid in p.parts or p.stem.startswith(qid+'_'))]
    designs=[p for p in files if p.name=='design.json']
    print('\nQUESTION',qid,'DESIGNS',len(designs),flush=True)
    for p in sorted(designs):
        d=read(p);print('DESIGN',str(p.relative_to(BASE)));print(json.dumps(d,ensure_ascii=False,indent=2))
        plugin=p.with_name('plugin.json')
        if plugin.exists():print('PLUGIN',json.dumps(read(plugin),ensure_ascii=False))
        for review in sorted(p.parent.glob('*review*.json')):
            v=read(review)
            if isinstance(v,dict) and 'runs' in v:
                v=copy.deepcopy(v)
                for run in v['runs']:run.pop('full_answer',None)
            print('REVIEW',review.name,json.dumps(v,ensure_ascii=False))
        for raw in sorted(p.parent.glob('tests/**/run_*_response.json')):
            data=read(raw);print('RAW_COMPLETE_REPLY',str(raw.relative_to(BASE)));print(json.dumps(data,ensure_ascii=False,indent=2))
    for p in sorted(files):
        if p.name in ('primary_math_audit.json','exact_flip_math_audit.json','source_primary_audit.json') or 'independent_review' in p.parts and p.suffix in ('.json','.md','.txt'):
            print('ADDITIONAL_REVIEW',str(p.relative_to(BASE)));print(p.read_text(encoding='utf-8-sig'))
    out=HERE/qid/'prior_history_inventory.json'
    if not out.exists():write(out,{'question_id':qid,'created_at':now(),'all_same_question_file_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(files)},'prior_design_paths':[str(p.relative_to(ROOT)) for p in sorted(designs)],'raw_response_paths':[str(p.relative_to(ROOT)) for p in files if p.name.endswith('_response.json')],'independent_review_paths':[str(p.relative_to(ROOT)) for p in files if 'independent_review' in p.parts]})
if __name__=='__main__':
    for q in sys.argv[1:]:history(q)
