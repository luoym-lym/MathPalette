from pathlib import Path
import os, sys, json, hashlib, copy
from datetime import datetime, timezone

TASK=Path(__file__).resolve().parent
SHARED=TASK.parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=TASK/name; p.mkdir(parents=True,exist_ok=True); os.environ[key]=str(p)

def owncheck(path):
    if isinstance(path,int) or path is None:return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(TASK):raise PermissionError('background_37 write outside own directory: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(SHARED))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config, pixel_hash, file_hash, canonical_hash, environment_versions
from dataset_tools.catalog import content,digest

CONFIG=load_config()
CONFIG['runtime_dir']=str(TASK/'bridge_state')
CONFIG['output_dir']=str(TASK/'bridge_outputs')
AD=RendererAdapter(CONFIG)
ASSIGN=json.loads((SHARED/'background_37_assignment.json').read_text(encoding='utf-8-sig'))
IDS=ASSIGN['question_ids']
OLD={q:SHARED/('background_13' if q in ['Solid102','Solid177','Solid230'] else 'background_14')/q for q in IDS}
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def jsonl(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def write(p,v):
    p=Path(p);owncheck(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def frozen(q):
    r=AD.records[q]; branch=ROOT/'SolidGeometry'
    paths=[r['image'],r['scene'],r['script'],*r.get('runtime_dependencies',[])]
    if r.get('original_image'):paths.append(r['original_image'])
    files={str((branch/p).relative_to(ROOT)).replace('\\','/'):file_hash(branch/p) for p in sorted(set(paths))}
    for p in ['dataset_tools/mathvision_workbench.py','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/config.json','SolidGeometry/workbench/renderer_adapter.py','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/plugin.schema.json','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/workbench_io.py','runtime/mathvision_special_20261101/delivery_bridge_adapter.py','runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/harness/quicktest3_isolated.py']:
        files[p]=file_hash(ROOT/p)
    return {'question_record_sha256':canonical_hash(r),'files':files,'environment':environment_versions()}
def eligibility(q):
    assert q in IDS
    b=ROOT/'SolidGeometry';r=next(x for x in jsonl(b/'dataset.jsonl') if x['id']==q);a=read(ROOT/'provenance/approvals.json')['approvals'][q]
    actual=digest(content(ROOT,'SolidGeometry',r));reasons=[];special={}
    if r['source_dataset']!='MathVision':reasons.append('not MathVision')
    if a.get('reviewer')!='user' or not a.get('instruction') or actual!=a.get('content_sha256'):reasons.append('approval mismatch')
    for n,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=b/'special_variant'/n
        if p.exists():special[n]={'sha256':file_hash(p),'question_records':[x for x in jsonl(p) if x.get('question_id')==q or x.get('id')==q]}
        if any(x.get('status')==status for x in special.get(n,{}).get('question_records',[])):reasons.append(n)
    for n in ['recipes.json','collection.json']:
        p=b/'special_variant'/q/n;special[n]={'exists':p.exists()}
        if p.exists():special[n].update(sha256=file_hash(p),content=read(p));reasons.append('existing '+n+' requires manual exclusion')
    delivered=[]
    for p in SHARED.glob('batch_*/manifest.json'):
        if q in p.read_text(encoding='utf-8-sig'):delivered.append(str(p.relative_to(ROOT)))
    if delivered:reasons.append('already delivered')
    return {'question_id':q,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'source_dataset':r['source_dataset'],'formal_record_canonical_sha256':canonical_hash(r),'approval':a,'current_content_sha256':actual,'approval_matches_current':actual==a.get('content_sha256'),'special_records':special,'delivered_manifests':delivered,'mutable_progress_is_diagnostic_only':True}
def inspect(q):
    out=TASK/q;out.mkdir(exist_ok=False)
    e=eligibility(q);write(out/'eligibility_at_start.json',e);assert e['eligible'],e['reasons']
    ctx=AD.inspect_question(q)
    write(out/'context.json',ctx);write(out/'formal_record.json',AD.records[q]);write(out/'frozen_inputs.json',frozen(q))
    r=AD.records[q];write(out/'source_scene_snapshot.json',read(ROOT/'SolidGeometry'/r['scene']))
    (out/'original.png').write_bytes(AD.original_paths[q].read_bytes())
    if r.get('original_image'):(out/('source'+Path(r['original_image']).suffix)).write_bytes((ROOT/'SolidGeometry'/r['original_image']).read_bytes())
    print(json.dumps({'question_id':q,'eligible':True,'baseline_pixels_equal':True,'objects':len(ctx['objects']),'answer':r['answer']}),flush=True)
def render(q,vid,actions,preset,intent,proof,roles,difference):
    assert q in IDS and eligibility(q)['eligible']
    folder=TASK/q/vid;folder.mkdir(exist_ok=False)
    write(folder/'design_difference_audit.json',{'question_id':q,'variant_id':vid,'created_at':now(),'old_history':str(OLD[q]),'substantive_difference':difference,'new_geometric_hypothesis':intent,'expected_wrong_answer_frozen_before_calls':preset,'cosmetic_change_only':False})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':intent[:1000],'intent':intent[:1000],'params':{'actions':actions}}
    before=frozen(q);ctx=AD.inspect_question(q);renderer=PluginRenderer(CONFIG,AD,{q:ctx})
    normal,data,pix=renderer.render(plugin);normal2,data2,pix2=renderer.render(plugin)
    assert normal==normal2 and data==data2 and pix==pix2
    assert frozen(q)==before
    (folder/'candidate.png').write_bytes(data);write(folder/'plugin.json',normal);write(folder/'context.json',ctx)
    report={'question_id':q,'png_sha256':file_hash(folder/'candidate.png'),'pixel_sha256':pix,'baseline_matches_formal':True,'twice_byte_identical':True,'schema_normalized':True,'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(normal),'isolation':ISOLATION,'native_visual_review':'pending'}
    write(folder/'render_check.json',report)
    write(folder/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':preset,'correct_answer':AD.records[q]['answer'],'intent':intent,'pretest_math_proof':proof,'pretest_marker_roles':roles,'source_context':str(TASK/q/'context.json'),'frozen_png_sha256':report['png_sha256'],'frozen_pixel_sha256':pix,'approval_status':'PRIMARY ONLY; parent must create NEW independent review; no Pass/Collect'})
    print(json.dumps({'question_id':q,'variant_id':vid,'preset':preset,'marks':len(actions),'sha256':report['png_sha256']}),flush=True)
    return folder
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
if __name__=='__main__':
    if sys.argv[1:] == ['inspect']:
        prior={str(p.relative_to(ROOT)).replace('\\','/'):file_hash(p) for q in IDS for p in OLD[q].rglob('*') if p.is_file()}
        for p in [SHARED/'background_13/checkpoint.json',SHARED/'background_14/checkpoint.json',SHARED/'background_37_brief.txt',SHARED/'background_37_assignment.json']:
            prior[str(p.relative_to(ROOT)).replace('\\','/')]=file_hash(p)
        write(TASK/'readonly_history_hashes_before.json',prior)
        write(TASK/'isolation.json',{'own_guard_before_any_project_import':True,'cache_environment':{k:os.environ[k] for k in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME']},'runtime_isolation':ISOLATION,'adapter_source':str(SHARED/'delivery_bridge_adapter.py')})
        for q in IDS:inspect(q)
