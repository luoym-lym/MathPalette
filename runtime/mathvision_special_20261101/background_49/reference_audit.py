import research_env as env
import json
from inspect_sources import save,sha,QIDS

def main():
 refs=[]
 for i in range(1,14):
  p=env.SHARED/f'batch_{i:02d}'/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
  for c in m['candidates']:
   refs.append({'batch':m['batch'],**{k:c.get(k) for k in ['question_id','mechanism','quality_review','tested_final_answers','original_control_answers','candidate_source']}})
 save(env.ROOT/'delivered_reference_information.json',refs)
 print(json.dumps(refs,ensure_ascii=False,indent=2))
 history=[]; controls=[]; designs=[]; source=[]
 for name in ['binding.json','design.json']:
  for p in env.SHARED.rglob(name):
   if p.is_relative_to(env.ROOT):continue
   raw=p.read_bytes()
   if not any(q.encode() in raw for q in QIDS):continue
   try:d=json.loads(raw.decode('utf-8-sig'))
   except Exception as exc:
    history.append({'path':str(p),'sha256':sha(p),'parse_failure':str(exc),'does_not_imply_no_call':True});continue
   if d.get('question_id') not in QIDS:continue
   item={'path':str(p),'sha256':sha(p),'question_id':d['question_id'],'data':d}
   if name=='design.json':designs.append(item)
   else:
    history.append(item)
    if 'control' in str(p).lower() or 'original' in str(p).lower():controls.append(item)
 for q in QIDS:
  p=env.PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/q/'source.json'
  source.append({'question_id':q,'path':str(p),'sha256':sha(p),'record':json.loads(p.read_text(encoding='utf-8'))})
 save(env.ROOT/'global_old_binding_design_scan.json',{'bindings':history,'designs':designs,'existing_controls':controls})
 save(env.ROOT/'source_records_full.json',source)
 print('EXHAUSTIVE_RELEVANT_BINDINGS',json.dumps([{k:x[k] for k in ['path','question_id']} for x in history if 'question_id' in x]))
 print('EXISTING_CONTROLS',json.dumps(controls,ensure_ascii=False))
 print('SOURCE_RECORDS',json.dumps(source,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
