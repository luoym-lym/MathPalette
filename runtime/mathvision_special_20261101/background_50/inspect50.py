from env50 import *
from datetime import datetime,timezone
from dataset_tools.catalog import rows,read,content,digest
IDS=['Plane170','Plane176','Plane177','Plane180','Plane181','Plane182','Plane183','Plane197']
BRANCH=PROJECT/'PlaneGeometry'
def eligibility(qid):
    rec=next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    source=content(PROJECT,'PlaneGeometry',rec)
    indices={};local={}
    for n in ['accepted_index.jsonl','collected_index.jsonl']:
        p=BRANCH/'special_variant'/n
        indices[n]={'sha256':sha(p) if p.exists() else None,'matching_records':[r for r in rows(p) if qid in json.dumps(r)] if p.exists() else []}
    for n in ['recipes.json','collection.json']:
        p=BRANCH/'special_variant'/qid/n
        if p.exists():local[n]={'sha256':sha(p),'content':read(p)}
    matches=approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(source)==approval['content_sha256']
    return {'checked_at':datetime.now(timezone.utc).isoformat(),'question_id':qid,'record':rec,'approval':approval,'current_content_sha256':digest(source),'approval_matches_current':matches,'source_content':source,'indices':indices,'local_special_files':local,'eligible':rec['source_dataset']=='MathVision' and matches and not local and not any(i['matching_records'] for i in indices.values())}
def main():
    sys.path.insert(0,str(BRANCH/'workbench'))
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    config=load_config();config['runtime_dir']=str(OWN/'unused_state');config['output_dir']=str(OWN/'unused_output')
    adapter=RendererAdapter(config)
    before={}
    allfiles=[p for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(OWN)]
    for q in IDS:
        d=OWN/q;d.mkdir(exist_ok=True)
        e=eligibility(q);dump(d/'eligibility_start.json',e)
        assert e['eligible'],q
        c=adapter.inspect_question(q);dump(d/'context.json',c)
        dump(d/'formal_record.json',e['record'])
        dump(d/'formal_scene_snapshot.json',read(BRANCH/e['record']['scene']))
        s=adapter.scene(q)
        try:
            b=png_bytes(s);(d/'no_op.png').write_bytes(b)
            arts={}
            for oid,aa in s.artists.items():
                arts[oid]=[]
                for a in aa:
                    obj={'type':type(a).__name__}
                    for attr in ['get_xy','get_xdata','get_ydata','get_text','get_position','get_facecolor','get_edgecolor','get_linewidth','get_linestyle','get_offsets','get_sizes']:
                        if hasattr(a,attr):
                            try:
                                v=getattr(a,attr)();obj[attr]=v.tolist() if hasattr(v,'tolist') else v
                            except Exception as x:obj[attr]=str(x)
                    arts[oid].append(obj)
            dump(d/'native_artists.json',arts)
            dump(d/'baseline_check.json',{'formal_pixel_equal':pixel_hash(b)==pixel_hash(BRANCH/e['record']['image']),'no_op_sha256':sha(d/'no_op.png'),'formal_sha256':sha(BRANCH/e['record']['image'])})
        finally:s.close()
        old=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in allfiles if q in p.parts or q in p.name]
        dump(d/'old_file_manifest.json',old)
        for rel,h in e['source_content']['files'].items():before[str((BRANCH/rel).resolve())]=h
        print(json.dumps({'id':q,'eligible':e['eligible'],'objects':len(c['objects']),'old_files':len(old),'question':e['record']['question']},ensure_ascii=False),flush=True)
    for p in [PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',BRANCH/'dataset.jsonl',BRANCH/'workbench/mathvision_adapter.py',BRANCH/'workbench/mathvision_plugins.py',ROOT/'harness/quicktest3_isolated.py']:
        before[str(p)]=sha(p)
    dump(OWN/'source_hashes_before.json',before)
    dump(OWN/'isolation.json',{'strict_guard_before_project_import':True,'shared_isolation':ISOLATION,'pid':os.getpid()})
if __name__=='__main__':main()
