import os, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=HERE.parent
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def guard(event,args):
    def check(p):
        if p is None or isinstance(p,int):return
        if not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):raise PermissionError('Unit18 write outside own root: '+str(p))
    if event=='open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(guard)
import json,copy,hashlib
from datetime import datetime,timezone
BRANCH='SolidGeometry' if len(sys.argv)>1 and sys.argv[1].startswith('Solid') else 'PlaneGeometry'
sys.path.insert(0,str(ROOT/BRANCH/'workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from dataset_tools import catalog
ASSIGNED=json.loads((BASE/'background_18_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry';br=ROOT/branch
    record=next((r for r in rows(br/'dataset.jsonl') if r['id']==qid),None);reasons=[]
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    approvals=json.loads((ROOT/'provenance/approvals.json').read_text(encoding='utf-8-sig'))['approvals'];approval=approvals.get(qid,{})
    current=catalog.digest(catalog.content(ROOT,branch,record)) if record else None
    if approval.get('reviewer')!='user' or not approval.get('instruction') or current!=approval.get('content_sha256'):reasons.append('original_approval_missing_or_changed')
    paths=[br/'dataset.jsonl',ROOT/'provenance/approvals.json']
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=br/'special_variant'/name;paths.append(p)
        if any(r.get('question_id',r.get('id'))==qid for r in rows(p)):reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p=br/'special_variant'/qid/name;paths.append(p)
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            if name=='recipes.json' and d:reasons.append('existing_recipes')
            if name=='collection.json' and d.get('current'):reasons.append('existing_collection_or_special_completion')
    for p in BASE.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'formal_record':record,'original_approval':approval,'current_original_content_sha256':current,'original_approval_fingerprint_matches':current==approval.get('content_sha256'),'state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths}}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'outputs')
    if BRANCH=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
        ad=RendererAdapter(cfg)
    else:
        from dataset_tools import mathvision_workbench as bridge
        from renderer_adapter import scene_png
        from render_plugins import PluginRenderer
        class SolidBridge:
            def __init__(self):
                self.records={r['id']:r for r in rows(ROOT/BRANCH/'dataset.jsonl')}
                self.original_paths={q:ROOT/BRANCH/r['image'] for q,r in self.records.items()}
            def scene(self,q):return bridge.build_scene(ROOT/BRANCH,self.records[q])
            def inspect_question(self,q):
                import matplotlib,numpy as np
                s=self.scene(q)
                try:
                    _,actual=scene_png(s);expected=pixel_hash(self.original_paths[q]);assert actual==expected,(q,'baseline mismatch')
                    with matplotlib.rc_context(s.settings):s.fig.canvas.draw()
                    w,h=s.fig.canvas.get_width_height();mat=np.array([[1,0,0],[0,-1,h],[0,0,1]])@s.ax.transData.get_affine().get_matrix()
                    return {'original_pixel_sha256':expected,'objects':copy.deepcopy(s.objects),'snap_points':copy.deepcopy(s.snap_points),'canvas':{'width':w,'height':h,'data_to_pixel':mat.tolist(),'pixel_to_data':np.linalg.inv(mat).tolist()},'xlim':list(s.ax.get_xlim()),'ylim':list(s.ax.get_ylim()),'renderer_mode':'checked_in_MathVision_bridge'}
                finally:s.close()
        ad=SolidBridge()
    return cfg,ad,PluginRenderer
def inputs(ad,qid):
    r=ad.records[qid];br=ROOT/BRANCH
    paths=[br/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(getattr(ad,'input_files',{}).values())
    paths+=[ROOT/p for p in ['MATHPALETTE_PROTOCOL.md','AGENTS.md','dataset_tools/mathvision_workbench.py','dataset_tools/geometry_dataset.py']]
    paths+=[br/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','dataset_generator/common_renderer.py','workbench/config.json','workbench/plugin.schema.json','workbench/render_plugins.py','workbench/partial_style.py','workbench/renderer_adapter.py','workbench/workbench_io.py']]
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad,pr=adapter()
    for qid in ASSIGNED:
        if qid.startswith('Solid')!=(BRANCH=='SolidGeometry'):continue
        folder=HERE/qid;check=eligibility(qid);write(folder/'eligibility_start.json',check)
        if not check['eligible']:print(qid,check['reasons'],flush=True);continue
        before=inputs(ad,qid);m=ad.inspect_question(qid)
        write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes());assert before==inputs(ad,qid)
        write(folder/'baseline_check.json',{'no_op_pixel_equal':True,'frozen_before_after_equal':True,'isolation':ISOLATION})
        print(qid,'baseline exact, objects',len(m['objects']),flush=True)
if __name__=='__main__':inspect_all()
