"""Finite runtime-only research helpers; never uses workbench mutation APIs."""
from pathlib import Path
import os, sys
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
sys.dont_write_bytecode = True
for key, name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p = HERE / name
    p.mkdir(exist_ok=True)
    os.environ[key] = str(p)
sys.path.insert(0,str(HERE.parent))
from runtime_isolation import install
ISOLATION = install(HERE/'render_tmp')
import json, hashlib
from datetime import datetime, timezone

def jl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []

def write(path, value):
    with path.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(value,f,ensure_ascii=False,indent=2)
        f.write('\n')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def eligible(branch,qid):
    base=PROJECT/branch
    record=next(r for r in jl(base/'dataset.jsonl') if r['id']==qid)
    accepted=base/'special_variant/accepted_index.jsonl'
    collected=base/'special_variant/collected_index.jsonl'
    reasons=[]
    if any(r.get('question_id')==qid and r.get('status')=='passed' for r in jl(accepted)):
        reasons.append('accepted_index_passed')
    if any(r.get('question_id')==qid and r.get('status')=='collected' for r in jl(collected)):
        reasons.append('collected_index_collected')
    inputs={str(p.relative_to(PROJECT)):sha(p) for p in [accepted,collected] if p.exists()}
    folder=base/'special_variant'/qid
    recipe=folder/'recipes.json'
    if recipe.exists():
        inputs[str(recipe.relative_to(PROJECT))]=sha(recipe)
        data=json.loads(recipe.read_text(encoding='utf-8-sig'))
        entries=data if isinstance(data,list) else data.get('recipes',data.get('variants',[]))
        if isinstance(entries,dict): entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):
            reasons.append('recipe_passed_or_reviewed')
    collection=folder/'collection.json'
    if collection.exists():
        inputs[str(collection.relative_to(PROJECT))]=sha(collection)
        data=json.loads(collection.read_text(encoding='utf-8-sig')).get('current',{})
        if data.get('status')=='collected' or data.get('collected_at') or data.get('special_case'):
            reasons.append('collection_or_special_completed')
    if record.get('source_dataset')!='MathVision':reasons.append('not_MathVision')
    return {'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),
            'eligible':not reasons,'exclusion_reasons':reasons,'current_status_file_hashes':inputs,'record':record}

if __name__=='__main__':
    action=sys.argv[1]
    if action=='prepared240':
        check=eligible('SolidGeometry','Solid240')
        write(HERE/'prepared_Solid240/eligibility.json',check)
        if not check['eligible']:raise SystemExit('Currently excluded; no rendering or API')
        from bridge_adapter import RuntimeBridgeAdapter
        adapter=RuntimeBridgeAdapter()
        plugin=json.loads((HERE/'prepared_Solid240/plugin.json').read_text(encoding='utf-8-sig'))
        report=adapter.render_candidate(plugin,HERE/'prepared_Solid240/fresh_replay')
        same=sha(HERE/'prepared_Solid240/candidate.png')==sha(HERE/'prepared_Solid240/fresh_replay/candidate.png')
        write(HERE/'prepared_Solid240/fresh_validation.json',{'copied_png_byte_equal_fresh_replay':same,**report})
        print(json.dumps({'replay_identical':same,'baseline_matches_formal':report['baseline_matches_formal']}))
    elif action=='shortlist':
        old=json.loads((HERE.parent/'exploration_report.json').read_text(encoding='utf-8-sig'))
        attempted={r['question_id'] for r in old['attempts']}
        rows=jl(HERE.parent/'remaining_questions.jsonl')
        print(json.dumps({'remaining_fields':list(rows[0])},ensure_ascii=False))
        for r in rows:
            qid=r.get('question_id',r.get('id'))
            if qid in attempted:continue
            branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
            record=next(x for x in jl(PROJECT/branch/'dataset.jsonl') if x['id']==qid)
            print(json.dumps({'id':qid,'answer':record['answer'],'question':record['question']},ensure_ascii=False))
