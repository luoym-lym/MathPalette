import os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=BASE.parents[1]
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def guard(event,args):
    def check(p):
        if p is not None and not isinstance(p,int):
            p=Path(os.fsdecode(p)).resolve()
            if not p.is_relative_to(HERE):raise PermissionError('background_30 write outside own root: '+str(p))
    if event=='open' and args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(guard)
import json,hashlib,copy,importlib.util
from datetime import datetime,timezone
ASSIGN=json.loads((BASE/'background_30_assignment.json').read_text(encoding='utf-8-sig'))
ASSIGNED=ASSIGN['question_ids']
BRANCH=sys.argv[2] if len(sys.argv)>2 and sys.argv[2] in ('PlaneGeometry','SolidGeometry') else 'PlaneGeometry'
sys.path.insert(0,str(ROOT/BRANCH/'workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from partial_style import object_paths
from dataset_tools import catalog
def now():return datetime.now(timezone.utc).isoformat()
def write(path,data):
    p=Path(path);assert p.resolve().is_relative_to(HERE)
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    b='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry';branch=ROOT/b;special=branch/'special_variant'
    ds=branch/'dataset.jsonl';ap=ROOT/'provenance/approvals.json';paths=[ds,ap];reasons=[]
    rec=next((r for r in rows(ds) if r['id']==qid),None)
    approval=json.loads(ap.read_text(encoding='utf-8-sig'))['approvals'].get(qid)
    if not rec or rec.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    current=catalog.digest(catalog.content(ROOT,b,rec)) if rec else None
    if not approval or approval.get('reviewer')!='user' or current!=approval.get('content_sha256'):reasons.append('original_approval_invalid')
    for n in ['accepted_index.jsonl','collected_index.jsonl']:
        p=special/n;paths.append(p)
        if any(r.get('question_id')==qid for r in rows(p)):reasons.append(n)
    for n in ['recipes.json','collection.json']:
        p=special/qid/n;paths.append(p)
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            if n=='collection.json':
                cur=d.get('current',{})
                if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('special_completion')
            else:
                entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                if any(r.get('status')=='passed' or r.get('reviewed_at') for r in entries if isinstance(r,dict)):reasons.append('passed_recipe')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('existing_delivery:'+p.parent.name)
    report=json.loads((BASE/'exploration_report.json').read_text(encoding='utf-8-sig'))
    foreign=[r for r in report['attempts'] if r['question_id']==qid and not str(r.get('candidate','')).replace('\\','/').startswith('background_30/')]
    # Intentional refinement overlap: prior terminal attempts are readonly evidence.
    return {'question_id':qid,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'approval':approval,'current_approval_content_sha256':current,'authoritative_state_hashes':{p.relative_to(ROOT).as_posix():file_hash(p) if p.exists() else None for p in paths},'runtime_diagnostic_metadata':{n:file_hash(BASE/n) for n in ['inventory.json','remaining_questions.jsonl','exploration_report.json']}}
class SolidAdapter:
    def __init__(self,cfg):
        self.branch=ROOT/'SolidGeometry';self.config=cfg
        self.records={r['id']:r for r in rows(self.branch/'dataset.jsonl')}
        self.original_paths={q:self.branch/r['image'] for q,r in self.records.items()}
    def scene(self,qid):
        from dataset_tools.mathvision_workbench import build_scene
        return build_scene(self.branch,self.records[qid])
    def inspect_question(self,qid):
        import matplotlib,numpy as np
        from renderer_adapter import scene_png
        s=self.scene(qid)
        try:
            _,actual=scene_png(s);expected=pixel_hash(self.original_paths[qid]);assert actual==expected
            with matplotlib.rc_context(s.settings):s.fig.canvas.draw()
            w,h=s.fig.canvas.get_width_height();t=np.array([[1,0,0],[0,-1,h],[0,0,1]])@s.ax.transData.get_affine().get_matrix()
            return {'original_pixel_sha256':expected,'objects':copy.deepcopy(s.objects),'snap_points':copy.deepcopy(s.snap_points),'xlim':list(s.ax.get_xlim()),'ylim':list(s.ax.get_ylim()),'canvas':{'width':w,'height':h,'data_to_pixel':t.tolist(),'pixel_to_data':np.linalg.inv(t).tolist(),'coordinate_system':'frozen_projected_2d'}}
        finally:s.close()
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    if BRANCH=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        return cfg,RendererAdapter(cfg)
    return cfg,SolidAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];b=ROOT/BRANCH
    paths=[b/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths +=[ROOT/p for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','dataset_tools/mathvision_workbench.py','dataset_tools/geometry_dataset.py']]
    paths +=[b/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/plugin.schema.json','workbench/config.json','workbench/renderer_adapter.py','workbench/render_plugins.py','workbench/partial_style.py','workbench/workbench_io.py']]
    if BRANCH=='PlaneGeometry':paths +=[b/'workbench/mathvision_adapter.py',b/'workbench/mathvision_plugins.py']
    return {'question_record_sha256':canonical_hash(r),'files':{p.relative_to(ROOT).as_posix():file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad=adapter()
    for qid in ASSIGNED:
        if qid.startswith('Plane')!=(BRANCH=='PlaneGeometry'):continue
        out=HERE/qid;check=eligibility(qid)
        if not (out/'eligibility_start.json').exists():write(out/'eligibility_start.json',check)
        if not check['eligible']:print(qid,check['reasons'],flush=True);continue
        before=inputs(ad,qid);meta=ad.inspect_question(qid)
        if not (out/'context.json').exists():
            write(out/'context.json',meta);write(out/'formal_record.json',ad.records[qid]);write(out/'input_fingerprints.json',before)
            (out/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
        s=ad.scene(qid)
        try:
            s.fig.canvas.draw();paths={o['id']:[{**{k:p[k] for k in ('id','sha256','closed')},'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(s,o['id'])] for o in meta['objects'] if o.get('styleable')}
            write(out/'paths_public.json',paths)
        finally:s.close()
        assert inputs(ad,qid)==before
        print(json.dumps({'qid':qid,'eligible':True,'baseline_match':True,'objects':len(meta['objects'])}),flush=True)
def render(qid,name,actions,preset,hypothesis,roles,math_review):
    assert qid in ASSIGNED
    out=HERE/qid/name
    if out.exists():
        print('Preserved existing candidate: '+str(out),flush=True);return
    check=eligibility(qid)
    if not check['eligible']:raise ValueError(check)
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
    if BRANCH=='PlaneGeometry':from mathvision_plugins import PluginRenderer
    else:from render_plugins import PluginRenderer
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
    ren=PluginRenderer(cfg,ad,{qid:meta});norm,data,pixels=ren.render(plugin);norm2,data2,pixels2=ren.render(norm,frozen=True)
    assert norm==norm2 and data==data2 and pixels==pixels2 and before==inputs(ad,qid)
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(data)
    write(out/'render_check.json',{'qid':qid,'baseline_match':True,'schema_normalized':True,'two_draws_byte_identical':True,'png_sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':pixels,'frozen_inputs':before,'isolation':ISOLATION,'world_geometry_projection_visibility_text_fill_unchanged':True})
    write(out/'eligibility_before_test.json',check)
    write(out/'design.json',{'question_id':qid,'variant_id':name,'design_id':name,'created_at':now(),'expected_wrong_answer':preset,'hypothesis':hypothesis,'marker_roles':roles,'primary_math_review':math_review,'image_sha256':file_hash(out/'candidate.png'),'plugin_sha256':file_hash(out/'plugin.json'),'must_view_native_png_before_test':True,'status':'unreviewed_runtime_only'})
    print(str(out),flush=True)
if __name__=='__main__':
    if sys.argv[1]=='inspect':inspect_all()
    elif sys.argv[1]=='init':
        (HERE/'quicktest3_isolated.py').write_bytes((BASE/'harness/quicktest3_isolated.py').read_bytes())
        write(HERE/'isolation.json',{'runtime_isolation':ISOLATION,'own_write_guard':True,'harness_byte_identical':file_hash(HERE/'quicktest3_isolated.py')==file_hash(BASE/'harness/quicktest3_isolated.py')})
