import own_runtime as rt
import sys
from pathlib import Path
import json
import hashlib
import os

BRANCH = rt.PROJECT/'PlaneGeometry'
sys.path.insert(0,str(BRANCH/'workbench'))
from dataset_tools import catalog
from workbench_io import load_config, environment_versions, pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from render_plugins import check_schema

def eligibility(qid):
    assignment=rt.read(rt.OWN/'assignment.json')
    expected=next(q for q in assignment['questions'] if q['question_id']==qid)
    row=next(r for r in catalog.rows(BRANCH/'dataset.jsonl') if r['id']==qid)
    approval=rt.read(rt.PROJECT/'provenance/approvals.json')['approvals'].get(qid)
    fingerprint=catalog.digest(catalog.content(rt.PROJECT,'PlaneGeometry',row))
    reasons=[]
    if row!=expected['formal_record']: reasons.append('formal_record_changed')
    if row['source_dataset']!='MathVision': reasons.append('wrong_source')
    if not approval or fingerprint != approval['content_sha256']: reasons.append('approval_content_mismatch')
    if fingerprint != expected['current_content_sha256']: reasons.append('assignment_content_mismatch')
    source=[]
    for rel,digest in expected['frozen_source_files_sha256'].items():
        actual=rt.sha(rt.PROJECT/rel)
        source.append({'path':rel,'expected':digest,'actual':actual})
        if actual!=digest: reasons.append('source_drift:'+rel)
    state={}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        p=BRANCH/'special_variant'/name
        matches=[r for r in catalog.rows(p) if r.get('question_id',r.get('id'))==qid] if p.exists() else []
        state[name]={'sha256':rt.sha(p) if p.exists() else None,'matches':matches}
        if matches: reasons.append(name+'_has_entry')
    d=BRANCH/'special_variant'/qid
    for name in ('recipes.json','collection.json'):
        p=d/name
        value=rt.read(p) if p.exists() else None
        state[name]={'sha256':rt.sha(p) if p.exists() else None,'value':value}
        if value: reasons.append(name+'_exists_nonempty')
    return {'question_id':qid,'checked_at':rt.now(),'eligible':not reasons,'reasons':reasons,
        'formal_record':row,'approval':approval,'current_content_sha256':fingerprint,
        'frozen_source_checks':source,'special_state':state,
        'dataset_sha256':rt.sha(BRANCH/'dataset.jsonl'),'approvals_sha256':rt.sha(rt.PROJECT/'provenance/approvals.json')}

def adapter():
    cfg=load_config()
    cfg['runtime_dir']=str(rt.OWN/'ownruntime'/'workbench')
    cfg['output_dir']=str(rt.OWN/'ownruntime'/'outputs')
    return cfg,RendererAdapter(cfg)

def capture():
    cfg,ad=adapter()
    for qid in rt.read(rt.OWN/'assignment.json')['question_ids']:
        d=rt.OWN/qid
        e=eligibility(qid);rt.save(d/'eligibility_initial.json',e)
        if not e['eligible']:
            print(qid,'HOLD',e['reasons']);continue
        meta=ad.inspect_question(qid)
        rt.save(d/'context.json',meta)
        rt.save(d/'manifest.json',ad.manifest)
        rt.save(d/'environment.json',{'versions':environment_versions(),'variables':{n:os.environ[n] for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},'isolation':rt.ISOLATION})
        scene=ad.scene(qid)
        try:
            data=png_bytes(scene)
            assert pixel_hash(data)==meta['original_pixel_sha256']
            (d/'native_noop.png').write_bytes(data)
            rt.save(d/'noop.json',{'same_pixels_as_formal':True,'native_sha256':hashlib.sha256(data).hexdigest(),'formal_sha256':rt.sha(ad.original_paths[qid])})
        finally:scene.close()
        print(qid,'objects',len(meta['objects']),'snap',len(meta['snap_points']))
        for ob in meta['objects']:
            geom=ob.get('geometry',{})
            print(ob['id'],ob.get('kind'),json.dumps(geom,ensure_ascii=False)[:800])
    return cfg,ad

if __name__=='__main__':capture()
