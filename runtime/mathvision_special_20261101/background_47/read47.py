from env47 import *
import json
from inspect47 import IDS, BRANCH

def select_nodes(value, qid):
    if isinstance(value,dict):
        if value.get('question_id', value.get('id')) == qid:
            return [value]
        result=[]
        for k,v in value.items():
            if k==qid:
                result.append({k:v})
            elif isinstance(v,(dict,list)):
                result.extend(select_nodes(v,qid))
        return result
    if isinstance(value,list):
        result=[]
        for item in value:
            result.extend(select_nodes(item,qid))
        return result
    return []

def main():
    old_global = ['plane_explore/checkpoint.json','exploration_report.json','inventory.json','remaining_questions.jsonl','background_21/checkpoint.json']
    for qid in IDS:
        root = OWN/qid
        manifest=json.loads((root/'old_file_manifest.json').read_text(encoding='utf-8'))
        dossier=[]
        for entry in manifest:
            p=Path(entry['path'])
            if p.suffix != '.json' or p.name in ['context.json','input_fingerprints.json','source_scene_snapshot.json','eligibility_start.json','eligibility_end.json','formal_record.json','request.json']:
                continue
            try:
                value=json.loads(p.read_text(encoding='utf-8-sig'))
                dossier.append({'path':str(p),'sha256':entry['sha256'],'full_content':value})
            except Exception as e:
                dossier.append({'path':str(p),'sha256':entry['sha256'],'parse_error':str(e),'raw_text':p.read_text(encoding='utf-8-sig'),'called_status':'unknown_from_parse_failure; do not infer no call'})
        for rel in old_global:
            p=ROOT/rel
            if not p.exists():continue
            try:
                vals=[json.loads(l) for l in p.read_text(encoding='utf-8-sig').splitlines() if l.strip()] if p.suffix=='.jsonl' else json.loads(p.read_text(encoding='utf-8-sig'))
                selected=select_nodes(vals,qid)
                if selected:dossier.append({'path':str(p),'sha256':sha(p),'relevant_full_nodes':selected,'mutable_diagnostic_metadata':True})
            except Exception as e:
                dossier.append({'path':str(p),'sha256':sha(p),'global_parse_error':str(e)})
        # Unabridged upstream numeric scene and source records, not stale formal summaries.
        item=BRANCH/'dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/qid
        for name in ['scene.json','source.json','execution.json','protocol_review.json']:
            p=item/name
            dossier.append({'path':str(p),'sha256':sha(p),'full_content':json.loads(p.read_text(encoding='utf-8-sig'))})
        dump(root/'reading_dossier.json',dossier)
        print(qid,[(Path(d['path']).name,len(json.dumps(d,ensure_ascii=False))) for d in dossier])

if __name__=='__main__':main()
