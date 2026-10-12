"""Build the portable review package from an explicitly supplied audited staging root."""
from pathlib import Path
import json,shutil,hashlib,sys,re
ROOT=Path(__file__).resolve().parent; REPO=ROOT.parents[1]
sys.path.insert(0,str(REPO))
from dataset_tools.answer_schema import validate_answer
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build(src):
 rows=[json.loads(l) for l in (src/'candidates.jsonl').read_text().splitlines() if l];notes=json.loads((src/'provenance/source_notes.json').read_text());result=[]
 family_sources={'plane':src/'plane_angles/renderer','plane_arrows':src/'plane_angles_tail/renderer','plane_curves':src/'plane_lengths_support/renderer','plane_extended':src/'plane_remaining/renderer','solid':src/'solids/code','analytics_frozen':src/'plane_remaining/analytics_renderer','analytics_functions':src/'functions'}
 for family,folder in family_sources.items():
  dest=ROOT/'shared'/family;dest.mkdir(parents=True,exist_ok=True)
  for name in ['common_renderer.py','protocol.json']:
   shutil.copyfile(folder/name,dest/name)
  for name in ['frozen_renderer.py'] if family=='analytics_frozen' else ['render.py'] if family=='analytics_functions' else []:
   text=(folder/name).read_text();text=text.replace("os.environ.setdefault('MPLCONFIGDIR',str(Path(__file__).parent/'audit'/'mplconfig'))",'')
   (dest/name).write_text(text)
 for old in rows:
  cid='MV'+str(old['source_problem_index']).zfill(4);item=ROOT/'items'/cid;item.mkdir(parents=True,exist_ok=True);note=notes[old['id']];group=old['script'].split('/')[0]
  family='solid' if old['subject']=='SolidGeometry' else ('analytics_functions' if group=='functions' else 'analytics_frozen') if old['subject']=='Analytics' else {'plane_angles':'plane','plane_lengths':'plane','plane_angles_tail':'plane_arrows','plane_lengths_support':'plane_curves','plane_remaining':'plane_extended'}[group]
  row={k:v for k,v in old.items() if k not in ['image','original_image','script','scene']};row.update(id=cid,candidate_id=cid,legacy_id=old['id'],renderer_family=family,user_approved=False,status='prepared_for_user_review',original_question=note['original_question'],original_answer=note['original_answer'])
  def put(key,name,source):
   shutil.copyfile(source,item/name);row[key]=(item/name).relative_to(REPO).as_posix()
  put('image','redrawn.png',src/old['image']);put('original_image','source.png',src/old['original_image'])
  svg=(src/old['image']).with_suffix('.svg')
  if svg.exists():put('svg','redrawn.svg',svg)
  else:row['svg']=(item/'redrawn.svg').relative_to(REPO).as_posix() if (item/'redrawn.svg').exists() else None
  # Original frozen scene retained as source evidence; portable scene changes identity/path only.
  scene=json.loads((src/old['scene']).read_text());scene['id']=cid
  if 'source_image' in scene:scene['source_image']='source.png'
  save(item/'scene.json',scene);row['scene']=(item/'scene.json').relative_to(REPO).as_posix()
  put('original_script','source_redraw.py',src/old['script'])
  packaging_changes=[]
  try:validate_answer(row)
  except ValueError:
   if row['answer_type']!='choice':raise
   old_question=row['question'];heading=re.search(r'\bchoices?\s*:',old_question,re.IGNORECASE)
   if heading is None:raise
   row['question']=old_question[:heading.start()].rstrip()+'\nChoices:\n'+'\n'.join(k+': '+v for k,v in row['choices'].items())
   validate_answer(row)
   packaging_changes.append({'type':'choice_label_format_normalization','candidate_question_before':old_question,'candidate_question_after':row['question'],'reason':'Normalize existing option labels to A: notation for the formal answer schema; no option text, order or answer changes.'})
  audit=json.loads((src/note['adaptation_and_answer_audit']).read_text());save(item/'provenance.json',{'source':{k:v for k,v in note.items() if k not in ['worker_record','adaptation_and_answer_audit']},'audit':audit,'packaging_changes':packaging_changes,'legacy_scene_id':old['id']})
  row['provenance']=(item/'provenance.json').relative_to(REPO).as_posix()
  evidence={}
  parent=(src/old['script']).parent
  for name in ['source_record.json','redraw_report.json','answer_verification.json']:
   if (parent/name).exists():evidence[name]=json.loads((parent/name).read_text())
  if group=='solids':evidence['checks']=json.loads((src/'solids/reports'/f"{old['id']}_checks.json").read_text())
  if group=='functions':evidence['checks']=audit
  evidence['packaging']={'source_sha256':sha(src/old['original_image']),'image_sha256':sha(src/old['image']),'scene_source_sha256':sha(src/old['scene']),'script_source_sha256':sha(src/old['script']),'user_approved':False}
  save(item/'verification.json',evidence);row['verification']=(item/'verification.json').relative_to(REPO).as_posix()
  source_answer=str(row['original_answer']).strip();resolved=row.get('choices',{}).get(str(row['answer']),row['answer'])
  source_options=dict(re.findall(r'(?:^|\n)([A-Z])\s*[:.)]\s*([^\n]+)',row['original_question']))
  source_resolved=source_options.get(source_answer,source_answer)
  norm=lambda value:re.sub(r'\s+','',str(value)).replace('$','').replace('°','').strip()
  same=norm(source_resolved)==norm(resolved)
  adaptation=audit.get('adaptation',{})
  explicit_correction=(isinstance(adaptation,dict) and adaptation.get('mathematical_answer_correction') is True) or any(isinstance(a,dict) and 'source_answer_conflict' in a.get('type','') for a in audit.get('adaptations',[])) or any(term in str(adaptation).lower() for term in ['corrected the answer','source answer is incorrect','source answer is wrong'])
  if isinstance(adaptation,dict) and adaptation.get('mathematical_answer_correction') is False:same=True
  row['candidate_answer_value']=resolved;row['source_answer_value']=source_resolved
  row['answer_consistency']={'status':'consistent' if same else 'corrected' if explicit_correction else 'needs_manual_confirmation','reason':'Resolved answers agree, or provenance explicitly records a representation-only answer normalization.' if same else 'Explicit correction recorded in provenance.' if explicit_correction else 'Different answer representations; consult derivation and source before judging equivalence.'}
  row['differences']={'question_changed':row['question']!=row['original_question'],'answer_changed':row['answer']!=row['original_answer'],'note':'String changes include normalization; see provenance for substantive corrections and explicit verification limits.'}
  row['script']=(item/'redraw.py').relative_to(REPO).as_posix();row['candidate_path']=(item/'candidate.json').relative_to(REPO).as_posix()
  save(item/'candidate.json',row)
  from promotion import wrapper
  (item/'redraw.py').write_text(wrapper(row,cid,'../../shared/runtime.py','scene.json','../../../..',candidate=True),encoding='utf-8')
  result.append(row)
 result.sort(key=lambda x:int(x['source_problem_index']));assert len(result)==731 and len({r['id'] for r in result})==731 and len({r['source_key'] for r in result})==731
 (ROOT/'index.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in result))
 print('Packaged',len(result))
if __name__=='__main__':build(Path(sys.argv[1]).resolve())
