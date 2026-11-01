import os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=ROOT/'runtime/mathvision_special_20261101'
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
sys.dont_write_bytecode=True;os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def owncheck(path):
    if isinstance(path,int) or path is None:return
    if not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):raise PermissionError('background_12 write outside own directory: '+str(path))
def own_guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(own_guard)
import json,hashlib,copy,io
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools import catalog
ASSIGNED=json.loads((BASE/'background_12_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);owncheck(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def rows(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    branch=ROOT/'PlaneGeometry';reasons=[];record=next((r for r in rows(branch/'dataset.jsonl') if r['id']==qid),None)
    paths=[branch/'dataset.jsonl',ROOT/'provenance/approvals.json']
    approval=read(paths[1])['approvals'].get(qid,{})
    current=catalog.digest(catalog.content(ROOT,'PlaneGeometry',record)) if record else None
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    if approval.get('reviewer')!='user' or not approval.get('instruction') or current!=approval.get('content_sha256'):reasons.append('current_original_not_approved')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=branch/'special_variant'/name;paths.append(p)
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(p)):reasons.append(name)
    recipe=branch/'special_variant'/qid/'recipes.json';paths.append(recipe)
    if recipe.exists():
        d=read(recipe);entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed_recipe')
    collection=branch/'special_variant'/qid/'collection.json';paths.append(collection)
    if collection.exists():
        cur=read(collection).get('current',{})
        if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('collected_or_special_completed')
    for manifest in BASE.glob('batch_*/manifest.json'):
        paths.append(manifest)
        if qid in manifest.read_text(encoding='utf-8-sig'):reasons.append('already_delivered:'+manifest.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'current_approval_fingerprint':current,'saved_approval_fingerprint':approval.get('content_sha256'),'approval_time':approval.get('approved_at_utc'),'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'formal_record':record}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];branch=ROOT/'PlaneGeometry'
    paths=[branch/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())+[ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'provenance/approvals.json',branch/'dataset.jsonl',branch/'REDRAW_PROTOCOL.md',branch/'dataset_generator/protocol.json',branch/'workbench/plugin.schema.json',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect(qid,ad):
    check=eligibility(qid);folder=HERE/qid;write(folder/'eligibility_start.json',check)
    if not check['eligible']:return
    before=inputs(ad,qid);meta=ad.inspect_question(qid)
    write(folder/'context.json',meta);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
    (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
    assert before==inputs(ad,qid)
    print(json.dumps({'qid':qid,'objects':len(meta['objects']),'baseline_pixel_match':True}),flush=True)
if __name__=='__main__':
    cfg,ad=adapter()
    for q in sys.argv[1:] or ASSIGNED:inspect(q,ad)
    from PIL import Image,ImageDraw
    for n,group in enumerate([ASSIGNED[:10],ASSIGNED[10:]],1):
        montage=Image.new('RGB',(1600,840),'white');d=ImageDraw.Draw(montage)
        for i,q in enumerate(group):
            p=HERE/q/'original.png'
            if not p.exists():continue
            im=Image.open(p).convert('RGB');im.thumbnail((320,390))
            x=(i%5)*320;y=(i//5)*420;montage.paste(im,(x,y+25));d.text((x+10,y+5),q,fill='black')
        montage.save(HERE/f'original_montage_{n}.png')
