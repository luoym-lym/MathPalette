"""Unit 22 only: read-only formal inspection and existing renderer execution."""
from pathlib import Path
import os, sys
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
BASE = HERE.parent
sys.dont_write_bytecode = True
for key, name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = HERE/name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(HERE/'render_tmp')
def own_guard(event,args):
    def check(p):
        if p is None or isinstance(p,int): return
        if not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):
            raise PermissionError('Unit22 write outside own root blocked: '+str(p))
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'): check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'): check(args[0]);check(args[1])
sys.addaudithook(own_guard)
import json, hashlib, shutil, copy
from datetime import datetime, timezone
def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p): return [json.loads(x) for x in Path(p).read_text(encoding='utf-8-sig').splitlines() if x.strip()] if Path(p).exists() else []
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,value):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f: json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
ASSIGN=read(BASE/'background_22_assignment.json')
IDS=ASSIGN['question_ids']
from dataset_tools.catalog import content,digest
def eligibility(branch,qid):
    assert qid in IDS
    b=PROJECT/branch
    record=next(r for r in rows(b/'dataset.jsonl') if r['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'].get(qid,{})
    payload=content(PROJECT,branch,record)
    accepted=[r for r in rows(b/'special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in rows(b/'special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    special=b/'special_variant'/qid
    formal_plugins=list((special/'plugins').glob('*.json')) if (special/'plugins').exists() else []
    collection=read(special/'collection.json') if (special/'collection.json').exists() else None
    valid=approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(payload)==approval.get('content_sha256')
    eligible=record['source_dataset']=='MathVision' and valid and not accepted and not collected and not formal_plugins and not(collection and collection.get('current'))
    return {'checked_at':now(),'question_id':qid,'branch':branch,'record':record,'question_record_sha256':digest(record),'approval':approval,'current_content_sha256':digest(payload),'approval_current':valid,'accepted_records':accepted,'collected_records':collected,'formal_plugin_files':[str(p.relative_to(PROJECT)) for p in formal_plugins],'collection':collection,'eligible':eligible,'frozen_content':payload}
def frozen_files(branch,record):
    b=PROJECT/branch
    files={str((b/p).relative_to(PROJECT)).replace('\\','/'):sha(b/p) for p in content(PROJECT,branch,record)['files']}
    for p in ['MATHPALETTE_PROTOCOL.md','dataset_tools/mathvision_workbench.py',branch+'/REDRAW_PROTOCOL.md']:
        files[p]=sha(PROJECT/p)
    for p in (b/'workbench').glob('*.py'): files[str(p.relative_to(PROJECT)).replace('\\','/')]=sha(p)
    for name in ['plugin.schema.json','config.json']: files[f'{branch}/workbench/{name}']=sha(b/'workbench'/name)
    return files
def setup(branch):
    sys.path.insert(0,str(PROJECT/branch/'workbench'))
    from workbench_io import load_config
    config=load_config();config['runtime_dir']=str(HERE/'state');config['output_dir']=str(HERE/'output')
    if branch=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
    else:
        from delivery_bridge_adapter import RendererAdapter
        from render_plugins import PluginRenderer
    return RendererAdapter(config),PluginRenderer,config
def inspect(branch):
    from PIL import Image
    adapter,_,_=setup(branch)
    from partial_style import object_paths
    from dataset_tools.mathvision_workbench import png_bytes
    for qid in IDS:
        if qid.startswith('Plane') != (branch=='PlaneGeometry'): continue
        directory=HERE/qid;directory.mkdir(exist_ok=False)
        elig=eligibility(branch,qid);write(directory/'eligibility_initial.json',elig)
        if not elig['eligible']: print(qid,'ineligible',flush=True);continue
        record=elig['record'];write(directory/'source_hashes_initial.json',frozen_files(branch,record))
        write(directory/'formal_record.json',record)
        metadata=adapter.inspect_question(qid);write(directory/'context.json',metadata)
        scene=adapter.scene(qid)
        try:
            data=png_bytes(scene)
            (directory/'baseline.png').write_bytes(data)
            with Image.open(PROJECT/branch/record['image']) as a, Image.open(directory/'baseline.png') as b:
                assert a.size==b.size==(768,768) and a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
            scene.fig.canvas.draw()
            paths={}
            for obj in metadata['objects']:
                if obj.get('styleable'):
                    paths[obj['id']]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,obj['id'])]
            write(directory/'exact_paths.json',paths)
        finally: scene.close()
        shutil.copyfile(PROJECT/branch/record['image'],directory/'original.png')
        if record.get('original_image'): shutil.copyfile(PROJECT/branch/record['original_image'],directory/('source'+Path(record['original_image']).suffix))
        write(directory/'baseline_check.json',{'question_id':qid,'no_op_pixel_equal':True,'png_sha256':sha(directory/'baseline.png'),'formal_png_sha256':sha(directory/'original.png'),'viewed_by_primary':'pending manual image review','isolation':ISOLATION})
        print(qid,'eligible, baseline exact, objects',len(metadata['objects']),flush=True)
def render(branch,spec_path):
    adapter,Renderer,config=setup(branch)
    specs=read(spec_path)
    from workbench_io import environment_versions
    for spec in specs:
        qid=spec['question_id'];assert qid in IDS
        directory=HERE/qid/spec['name'];directory.mkdir(exist_ok=False)
        elig=eligibility(branch,qid);write(directory/'eligibility_before_render.json',elig);assert elig['eligible']
        before=frozen_files(branch,elig['record']);metadata=adapter.inspect_question(qid)
        renderer=Renderer(config,adapter,{qid:metadata})
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':spec['description'],'intent':spec['hypothesis'],'params':{'actions':spec['actions']}}
        normalized,data,pixels=renderer.render(plugin)
        normalized2,data2,pixels2=renderer.render(normalized,frozen=True)
        assert normalized==normalized2 and data==data2 and pixels==pixels2
        assert frozen_files(branch,elig['record'])==before
        (directory/'candidate.png').write_bytes(data)
        write(directory/'plugin.json',normalized)
        write(directory/'context.json',metadata)
        design={k:v for k,v in spec.items() if k!='actions'}
        design.update(created_at=now(),branch=branch,plugin_sha256=sha(directory/'plugin.json'),image_sha256=sha(directory/'candidate.png'),pixel_sha256=pixels,approval_status='PRIMARY ONLY; no independent second review, no Pass/Collect')
        write(directory/'design.json',design)
        write(directory/'render_check.json',{'baseline_matches_formal':True,'actual_schema_default_normalization':True,'frozen_plugin_replay_byte_identical':True,'png_sha256':sha(directory/'candidate.png'),'pixel_sha256':pixels,'frozen_inputs':before,'environment':environment_versions(),'isolation':ISOLATION})
        print(qid,spec['name'],sha(directory/'candidate.png'),flush=True)
def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('mode');p.add_argument('branch');p.add_argument('--spec');a=p.parse_args()
    if a.mode=='inspect':inspect(a.branch)
    elif a.mode=='render':render(a.branch,a.spec)
if __name__=='__main__':main()
