from bootstrap import *
sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))
from workbench_io import load_config, canonical_hash, pixel_hash, environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.catalog import content, digest

IDS = ['Plane295', 'Plane342']
OLD = {'Plane295':'inner_ear_shoulder_correspondence', 'Plane342':'quarterturn_wedge_edge_binding'}
BASE = ROOT.parent
BRANCH = PROJECT / 'PlaneGeometry'

def rows(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []

def eligibility(qid):
    assert qid in IDS
    record = next(r for r in rows(BRANCH / 'dataset.jsonl') if r['id'] == qid)
    approvals = read(PROJECT / 'provenance/approvals.json')['approvals']
    approval = approvals.get(qid, {})
    fingerprint = digest(content(PROJECT, 'PlaneGeometry', record))
    reasons = []
    if record['source_dataset'] != 'MathVision': reasons.append('not formal MathVision')
    if approval.get('reviewer') != 'user' or not approval.get('instruction') or approval.get('content_sha256') != fingerprint:
        reasons.append('missing or mismatched original user approval')
    state = {}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p = BRANCH / 'special_variant' / name
        matches = [r for r in rows(p) if r.get('question_id') == qid]
        state[name] = {'sha256':sha(p) if p.exists() else None, 'matching_records':matches}
        if matches: reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p = BRANCH / 'special_variant' / qid / name
        value = read(p) if p.exists() else None
        state[name] = {'sha256':sha(p) if p.exists() else None, 'value':value}
        if value:
            if name == 'collection.json':
                c = value.get('current',{})
                if c.get('status') == 'collected' or c.get('collected_at') or c.get('special_case'): reasons.append(name)
            else:
                entries = value if isinstance(value,list) else value.get('recipes',value.get('variants',[]))
                if isinstance(entries,dict): entries=list(entries.values())
                if any(x.get('status')=='passed' or x.get('reviewed_at') for x in entries if isinstance(x,dict)): reasons.append(name)
    delivered = []
    for p in BASE.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'): delivered.append(str(p.relative_to(PROJECT)))
    if delivered: reasons.append('already delivered')
    return {'question_id':qid,'checked_at':now(),'eligible':not reasons,'reasons':reasons,
            'formal_record':record,'formal_record_sha256':canonical_hash(record),
            'current_content_sha256':fingerprint,'original_approval':approval,
            'state':state,'delivered_matches':delivered,
            'authoritative_hashes':{str(p.relative_to(PROJECT)):sha(p) for p in [BRANCH/'dataset.jsonl',PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json']},
            'mutable_progress_diagnostic_only':{str(p.relative_to(PROJECT)):sha(p) for p in [BASE/'exploration_report.json',BASE/'remaining_questions.jsonl']}}

def input_manifest(ad,qid):
    r=ad.records[qid]
    paths = [BRANCH/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths += list(ad.input_files.values())
    paths += [PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',BRANCH/'dataset.jsonl',PROJECT/'MATHPALETTE_PROTOCOL.md',BRANCH/'REDRAW_PROTOCOL.md']
    paths += list((BRANCH/'workbench').glob('*.py')) + [BRANCH/'workbench/plugin.schema.json',BRANCH/'workbench/config.json']
    return {'record_sha256':canonical_hash(r),'files':{str(p.relative_to(PROJECT)):sha(p) for p in sorted(set(paths))},'environment':environment_versions()}

def make_adapter():
    cfg=load_config()
    cfg['runtime_dir']=str(ROOT/'render_state')
    cfg['output_dir']=str(ROOT/'render_output')
    return cfg,RendererAdapter(cfg)

def initialize():
    cfg,ad = make_adapter()
    oldhashes = {}
    for qid in IDS:
        qroot=ROOT/qid
        e=eligibility(qid)
        if not (qroot/'eligibility_start.json').exists(): save(qroot/'eligibility_start.json',e)
        assert e['eligible'], e['reasons']
        manifest=input_manifest(ad,qid)
        meta=ad.inspect_question(qid)
        for leaf,value in [('context.json',meta),('input_manifest_start.json',manifest),('formal_record.json',ad.records[qid]),('formal_scene_snapshot.json',read(BRANCH/ad.records[qid]['scene']))]:
            if not (qroot/leaf).exists(): save(qroot/leaf,value)
        (qroot/'formal.png').write_bytes(ad.original_paths[qid].read_bytes())
        (qroot/'source.jpg').write_bytes((BRANCH/ad.records[qid]['original_image']).read_bytes())
        scene=ad.scene(qid)
        try:
            from dataset_tools.mathvision_workbench import png_bytes
            data=png_bytes(scene)
            assert pixel_hash(data)==meta['original_pixel_sha256']
            (qroot/'no_op.png').write_bytes(data)
            paths={obj['id']:object_paths(scene,obj['id']) for obj in meta['objects'] if obj.get('styleable',True)}
            paths=json.loads(json.dumps(paths,default=lambda x:x.tolist() if hasattr(x,'tolist') else str(x)))
            save(qroot/'frozen_paths_complete.json',paths)
        finally: scene.close()
        assert manifest==input_manifest(ad,qid)
        oldroot=BASE/'background_19'/qid
        for p in oldroot.rglob('*'):
            if p.is_file(): oldhashes[str(p.relative_to(PROJECT))]=sha(p)
        rev=BASE/'independent_review'/f'{qid}_{OLD[qid]}'
        for p in rev.rglob('*'):
            if p.is_file(): oldhashes[str(p.relative_to(PROJECT))]=sha(p)
        print(json.dumps({'qid':qid,'eligible':True,'approval_matches':True,'no_op_equals_formal':True,'objects':len(meta['objects'])}))
    for p in [BASE/'background_19/checkpoint.json',BASE/'background_18/checkpoint.json',BASE/'background_19/second_review_queue.json']:
        oldhashes[str(p.relative_to(PROJECT))]=sha(p)
    save(ROOT/'old_evidence_hashes_start.json',oldhashes)
    save(ROOT/'isolation.json',{'created_at':now(),'strict_own_root_guard':True,'shared_runtime_isolation':ISOLATION,'no_nested_agents':True,'environment':{k:os.environ.get(k) for k in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONPYCACHEPREFIX']}})

if __name__ == '__main__':
    initialize()
