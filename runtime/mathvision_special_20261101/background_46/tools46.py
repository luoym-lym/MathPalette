from bootstrap46 import *
from datetime import datetime, timezone
import copy
from runtime_isolation import install
ISOLATION=install(OWN/'render_tmp')
sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from renderer_adapter import scene_png
from workbench_io import load_config,pixel_hash,file_hash,canonical_hash,environment_versions
from partial_style import object_paths
CONFIG=load_config();CONFIG['runtime_dir']=str(OWN/'state');CONFIG['output_dir']=str(OWN/'output')
AD=RendererAdapter(CONFIG)
ASSIGN=read(TASK/'background_46_assignment.json');IDS=ASSIGN['question_ids']
def now(): return datetime.now(timezone.utc).isoformat()
def jl(p): return [json.loads(x) for x in Path(p).read_text(encoding='utf-8-sig').splitlines() if x.strip()] if Path(p).is_file() else []
def eligibility(q):
    assert q in IDS
    from dataset_tools.catalog import content,digest
    r=AD.records[q];a=read(PROJECT/'provenance/approvals.json')['approvals'].get(q,{})
    fp=digest(content(PROJECT,'SolidGeometry',r)); reasons=[];special={}
    if r.get('source_dataset')!='MathVision':reasons.append('not MathVision')
    if a.get('reviewer')!='user' or not a.get('instruction') or fp!=a.get('content_sha256'):reasons.append('current original approval mismatch')
    for n in ['accepted_index.jsonl','collected_index.jsonl']:
        p=PROJECT/'SolidGeometry/special_variant'/n
        special[n]=[x for x in jl(p) if x.get('question_id')==q]
        if special[n]:reasons.append(n+' contains question')
    for n in ['recipes.json','collection.json']:
        p=PROJECT/'SolidGeometry/special_variant'/q/n
        if p.exists():
            x=read(p);special[n]=x
            if n=='recipes.json':
                entries=x if isinstance(x,list) else x.get('recipes',x.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries): reasons.append('passed recipe')
            else:
                c=x.get('current',{})
                if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collected/special completion')
    delivered=[]
    for p in TASK.glob('batch_*/manifest.json'):
        if q in p.read_text(encoding='utf-8-sig'):delivered.append(str(p))
    if delivered:reasons.append('previously delivered')
    return {'question_id':q,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'MathVision':r.get('source_dataset')=='MathVision','approval':a,'approval_content_actual':fp,'approval_matches_current':fp==a.get('content_sha256'),'authoritative_special_records':special,'delivery_manifests':delivered,'ledger_readonly_diagnostic_only':True}
def inputs(q):
    r=AD.records[q];rel=[r[k] for k in ['image','scene','script','original_image'] if r.get(k)]+r.get('runtime_dependencies',[])
    files={str(AD.branch/p):sha(AD.branch/p) for p in rel}
    for p in ['provenance/approvals.json','SolidGeometry/dataset.jsonl','SolidGeometry/workbench/config.json','SolidGeometry/workbench/quick_test.py','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/plugin.schema.json','dataset_tools/mathvision_workbench.py','dataset_tools/catalog.py']:
        files[str(PROJECT/p)]=sha(PROJECT/p)
    for p in ['runtime_isolation.py','delivery_bridge_adapter.py','harness/quicktest3_isolated.py']:files[str(TASK/p)]=sha(TASK/p)
    return files
def artist_snapshot(s):
    return {'fills':[{'path':p.get_path().vertices.tolist(),'codes':None if p.get_path().codes is None else p.get_path().codes.tolist(),'color':list(p.get_facecolor()),'transform':p.get_transform().get_matrix().tolist()} for p in s.ax.patches if p.get_fill()],
        'texts':[{'text':t.get_text(),'position':list(t.get_position()),'font':t.get_fontsize(),'transform':t.get_transform().get_matrix().tolist()} for t in s.ax.texts],
        'view':[list(s.ax.get_xlim()),list(s.ax.get_ylim()),s.ax.get_aspect(),s.fig.get_size_inches().tolist()]}
def paths(q,targets):
    s=AD.scene(q)
    try:
        s.fig.canvas.draw()
        return {t:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(s,t)] for t in targets}
    finally:s.close()
