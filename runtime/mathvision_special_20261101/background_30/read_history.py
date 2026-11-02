import tools_local as t
old={}
report=t.json.loads((t.BASE/'exploration_report.json').read_text(encoding='utf-8-sig'))
for q in (t.sys.argv[1:] or t.ASSIGNED):
    files=[]
    for p in t.BASE.rglob('*'):
        if not p.is_file() or p.is_relative_to(t.HERE) or q not in p.parts:continue
        files.append(p)
    old[q]={'files':{str(p.relative_to(t.ROOT)):t.file_hash(p) for p in files},
            'attempts':[a for a in report['attempts'] if a['question_id']==q]}
    print('QUESTION',q)
    print('PRIOR_ATTEMPTS',t.json.dumps(old[q]['attempts'],ensure_ascii=False))
    wanted=['design.json','plugin.json','manual_final_review.json','primary_review.json','primary_visual.json','primary_visual_review.json','tiling_math_audit.json','completion_math_audit.json','render_failure.json']
    for p in files:
        if p.name in wanted or p.name.endswith('_response.json'):
            print('FULL_FILE',str(p.relative_to(t.ROOT)))
            print(p.read_text(encoding='utf-8-sig'))
    reviews=[]
    for p in (t.BASE/'independent_review').rglob('*.json'):
        if q in str(p.relative_to(t.BASE)) and p.name in ['independent_review.json','review.json']:
            reviews.append(p)
            print('INDEPENDENT_FULL',p,p.read_text(encoding='utf-8-sig'))
    old[q]['independent_review_files']=[str(p.relative_to(t.ROOT)) for p in reviews]
manifest=t.HERE/('old_history_'+('_'.join(t.sys.argv[1:]) or 'manifest')+'.json')
if not manifest.exists():t.write(manifest,old)
