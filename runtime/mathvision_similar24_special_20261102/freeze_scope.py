from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import hashlib, json, shutil, sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT))
from dataset_tools import catalog
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 p=Path(p);assert p.resolve().is_relative_to(HERE)
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
def rows(p):return list(catalog.rows(p))
refs=['Plane217','Plane233','Plane308','Plane427','Solid126','Solid142','Solid167','Solid176','Solid203']
matches=read(ROOT/'runtime/mathvision_similar9_20261102/uncollected_matches.json')
targets=matches['candidate_ids'];assert len(targets)==len(set(targets))==24
approvals=read(ROOT/'provenance/approvals.json')['approvals']
data={};used={};reference={};eligible={}
for b in ['PlaneGeometry','SolidGeometry']:
 records={r['id']:r for r in rows(ROOT/b/'dataset.jsonl')}
 accepted=rows(ROOT/b/'special_variant/accepted_index.jsonl')
 collected=rows(ROOT/b/'special_variant/collected_index.jsonl')
 for q in [q for q in refs+targets if q in records]:
  r=records[q];assert r['source_dataset']=='MathVision'
  fp=catalog.digest(catalog.content(ROOT,b,r));a=approvals[q]
  assert a['reviewer']=='user' and a.get('instruction') and fp==a['content_sha256'],q
  dependencies={r[k] for k in ['image','original_image','scene','script'] if r.get(k)}|set(r.get('runtime_dependencies',[]))
  dependencies={b+'/'+p:sha(ROOT/b/p) for p in dependencies}
  used.update(dependencies)
  own_acc=[v for v in accepted if v.get('question_id',v.get('id'))==q]
  own_col=[v for v in collected if v.get('question_id',v.get('id'))==q]
  folder=ROOT/b/'special_variant'/q
  rec=read(folder/'recipes.json') if (folder/'recipes.json').exists() else []
  col=read(folder/'collection.json') if (folder/'collection.json').exists() else None
  state={'question_id':q,'branch':b,'formal_record':r,'approval':a,'current_content_sha256':fp,'frozen_source_files_sha256':dependencies,'accepted_entries':own_acc,'collected_entries':own_col,'recipes':rec,'collection':col}
  if q in targets:
   assert not own_acc and not own_col and not rec and col is None,q
   eligible[q]={**state,'eligible':True}
  else:
   assert len(own_acc)==len(rec)==1 and own_acc==rec and rec[0]['slot_id']=='C01'
   td=HERE/'references'/q;td.mkdir(parents=True,exist_ok=False)
   copies={}
   for name,src in [('C01.png',ROOT/b/rec[0]['image_path']),('C01.json',ROOT/b/rec[0]['plugin_path']),('recipes.json',folder/'recipes.json'),('original.png',ROOT/b/r['image'])]:
    dst=td/name;shutil.copyfile(src,dst);assert sha(dst)==sha(src)
    copies[name]={'source':src.relative_to(ROOT).as_posix(),'sha256':sha(src)};used[src.relative_to(ROOT).as_posix()]=sha(src)
   assert copies['C01.png']['sha256']==rec[0]['png_sha256'] and copies['C01.json']['sha256']==rec[0]['plugin_sha256']
   save(td/'reference.json',{**state,'copied_files':copies})
   reference[q]={'directory':td.relative_to(HERE).as_posix(),'png_sha256':copies['C01.png']['sha256'],'plugin_sha256':copies['C01.json']['sha256'],'formal_approval_content_sha256':fp}
for p in ['MATHPALETTE_PROTOCOL.md','provenance/approvals.json','dataset_tools/catalog.py','dataset_tools/mathvision_workbench.py']:
 used[p]=sha(ROOT/p)
for b in ['PlaneGeometry','SolidGeometry']:
 for p in ['dataset.jsonl','REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/README.md','workbench/agent_prompt.md','workbench/plugin.schema.json','workbench/config.json','workbench/quick_test.py']:
  used[b+'/'+p]=sha(ROOT/b/p)
for p in ['runtime_isolation.py','delivery_bridge_adapter.py','harness/quicktest3_isolated.py','validate_candidate_replay.py','publish_batch.py']:
 used['runtime/mathvision_special_20261101/'+p]=sha(ROOT/'runtime/mathvision_special_20261101'/p)
save(HERE/'eligibility_initial.json',eligible)
save(HERE/'reference_manifest.json',reference)
save(HERE/'readonly_source_sha256.json',used)
save(HERE/'task.json',{'created_at_utc':datetime.now(timezone.utc).isoformat(),'user_instruction':'帮我按照我标注那9道题的方法，给这24道相近的题每道题标一个类似的specialvar。要满足通过标准。','scope':targets,'question_count':24,'references':refs,'previous_search':str(ROOT/'runtime/mathvision_similar9_20261102/uncollected_matches.json'),'qualification':'Each delivered candidate: two complete quicktest3 finals on identical frozen PNG both match wrong preset frozen before both calls; fresh independent second review confirms rigorous unique mathematics, targeted useful concise legal marks and unambiguous native readability.','formal_readonly':True,'all_new_files_only_under_runtime':True,'no_Pass_Collect_or_user_approval_inferred':True,'old_general_exploration_remains_paused':True})
assert all(sha(ROOT/p)==v for p,v in used.items())
print(json.dumps({'targets':targets,'reference_count':len(reference),'source_files':len(used),'eligible':len(eligible)},ensure_ascii=False))
