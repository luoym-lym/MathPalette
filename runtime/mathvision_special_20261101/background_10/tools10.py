import os, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=HERE.parent
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def own_guard(event,args):
    def check(p):
        if p is None or isinstance(p,int):return
        if not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):raise PermissionError('Unit10 write outside own root: '+str(p))
    if event=='open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_guard)
import json,hashlib,copy
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
ASSIGNED=json.loads((BASE/'background_10_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    br=ROOT/'PlaneGeometry';record=next((r for r in rows(br/'dataset.jsonl') if r['id']==qid),None);reasons=[]
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    approvals=json.loads((ROOT/'provenance/approvals.json').read_text(encoding='utf-8-sig'))['approvals']
    if qid not in approvals:reasons.append('no_original_approval')
    from dataset_tools import catalog
    current_content=catalog.digest(catalog.content(ROOT,'PlaneGeometry',record)) if record else None
    if qid in approvals and current_content!=approvals[qid].get('content_sha256'):reasons.append('original_approval_fingerprint_mismatch')
    paths=[br/'dataset.jsonl',ROOT/'provenance/approvals.json']
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=br/'special_variant'/name;paths.append(p)
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(p)):reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p=br/'special_variant'/qid/name;paths.append(p)
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            if name=='recipes.json':
                e=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]));e=list(e.values()) if isinstance(e,dict) else e
                if any(x.get('status')=='passed' or x.get('reviewed_at') for x in e if isinstance(x,dict)):reasons.append('passed_recipe')
            else:
                c=d.get('current',{})
                if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collection_or_special_completed')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'formal_record':record,'original_approval':approvals.get(qid),'current_original_content_sha256':current_content,'original_approval_fingerprint_matches':current_content==approvals.get(qid,{}).get('content_sha256'),'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in [BASE/'remaining_questions.jsonl',BASE/'exploration_report.json']}}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output');return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];br=ROOT/'PlaneGeometry'
    paths=[br/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]+list(ad.input_files.values())
    paths += [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',ROOT/'provenance/approvals.json',br/'REDRAW_PROTOCOL.md',br/'workbench/plugin.schema.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad=adapter()
    for qid in ASSIGNED:
        folder=HERE/qid;check=eligibility(qid);write(folder/'eligibility_start.json',check)
        if not check['eligible']:continue
        before=inputs(ad,qid);m=ad.inspect_question(qid)
        write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes());assert before==inputs(ad,qid)
        print(json.dumps({'qid':qid,'baseline_match':True,'objects':len(m['objects']),'snaps':len(m['snap_points'])}),flush=True)
    from PIL import Image,ImageDraw
    for i in range(0,len(ASSIGNED),6):
        qs=ASSIGNED[i:i+6];sheet=Image.new('RGB',(1152,800),'white');d=ImageDraw.Draw(sheet)
        for j,q in enumerate(qs):
            p=HERE/q/'original.png'
            if p.exists():
                im=Image.open(p).convert('RGB');im.thumbnail((384,384));sheet.paste(im,((j%3)*384,(j//3)*400+16));d.text(((j%3)*384+8,(j//3)*400+2),q,fill='black')
        sheet.save(HERE/f'contact_{i//6+1}.png')
if __name__=='__main__':inspect_all()
