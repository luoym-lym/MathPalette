from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp
import json
out=[]
for n in range(1,15):
    p=TASK/f'batch_{n:02d}'/'manifest.json'
    d=read(p)
    candidates=d.get('candidates',d.get('items',[]))
    if isinstance(candidates,dict):candidates=list(candidates.values())
    e={'path':str(p),'sha256':sha(p),'full_manifest_read':True,'reference_information':[{k:c[k] for k in ('question_id','mechanism','quality_review','expected_wrong_answer','tested_final_answers','candidate_source') if k in c} for c in candidates]}
    out.append(e)
save(HERE/'delivered_batches_reference_audit.json',{'time':stamp(),'read_only':True,'no_causal_gain_inferred':True,'all_fourteen_manifests':out,'lesson':'Use actual source/receiver features and explicit distinct error, preserve human semantics and frozen geometry. Two observations do not establish incremental causal gains; no correct-original-control gate imposed.'})
print(json.dumps([{'batch':n+1,'candidates':e['reference_information']} for n,e in enumerate(out)],ensure_ascii=False,indent=2))
# Complete continuation read is preserved initially. Extract every paragraph
# concerning scope and current discipline, while retaining the full text snapshot.
text=(TASK/'continuation_brief.txt').read_text(encoding='utf-8-sig')
paragraphs=text.split('\n\n')
relevant=[p for p in paragraphs if any(s in p for s in ('Solid212','Solid222','Solid227','Solid235','background_61','background_73','API','quota','原','标注','SEMANTIC'))]
save(HERE/'continuation_full_read_scope_extract.json',{'path':str(TASK/'continuation_brief.txt'),'current_sha256':sha(TASK/'continuation_brief.txt'),'complete_utf8_read':True,'scope_paragraphs':relevant})
print('CONTINUATION SCOPE')
for p in relevant:print(p)
