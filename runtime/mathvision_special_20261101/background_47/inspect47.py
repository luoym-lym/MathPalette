from env47 import *
import json
import hashlib
from datetime import datetime, timezone
from dataset_tools.catalog import rows, read, content, digest

IDS = ['Plane452','Plane456','Plane457','Plane458','Plane460','Plane462','Plane463','Plane465']
BRANCH = PROJECT / 'PlaneGeometry'

def eligibility(qid):
    record = next(r for r in rows(BRANCH / 'dataset.jsonl') if r['id'] == qid)
    approval = read(PROJECT / 'provenance/approvals.json')['approvals'][qid]
    current_content = content(PROJECT, 'PlaneGeometry', record)
    special = BRANCH / 'special_variant'
    indices = {}
    matching = {}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p = special / name
        indices[name] = {'path':str(p), 'sha256':sha(p) if p.exists() else None}
        matching[name] = [r for r in rows(p) if qid in json.dumps(r, ensure_ascii=False)] if p.exists() else []
    local = {}
    for name in ['collection.json','recipes.json']:
        p = special / qid / name
        if p.exists():
            local[name] = {'path':str(p),'sha256':sha(p),'content':read(p)}
    evidence = {'checked_at':datetime.now(timezone.utc).isoformat(),'record':record,'approval':approval,
                'current_content_sha256':digest(current_content),
                'approval_matches':approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(current_content)==approval['content_sha256'],
                'source_content':current_content,'special_indices':indices,'matching_special_records':matching,'special_local_files':local}
    evidence['eligible'] = record['source_dataset']=='MathVision' and evidence['approval_matches'] and not any(matching.values()) and not local
    return evidence

def main():
    sys.path.insert(0, str(BRANCH / 'workbench'))
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    config = load_config()
    config['runtime_dir'] = str(OWN / 'workbench_runtime_unused')
    config['output_dir'] = str(OWN / 'workbench_output_unused')
    adapter = RendererAdapter(config)
    source_hashes = {}
    for qid in IDS:
        root = OWN / qid
        audit = eligibility(qid)
        dump(root / 'eligibility_start.json', audit)
        assert audit['eligible'], qid
        metadata = adapter.inspect_question(qid)
        dump(root / 'context.json', metadata)
        dump(root / 'formal_record.json', audit['record'])
        rec = audit['record']
        formal_scene = read(BRANCH / rec['scene'])
        dump(root / 'formal_scene_snapshot.json', formal_scene)
        with_scene = adapter.scene(qid)
        try:
            (root / 'noop.png').write_bytes(png_bytes(with_scene))
            artists = {}
            for oid, objs in with_scene.artists.items():
                artists[oid] = []
                for obj in objs:
                    a = {'type':type(obj).__name__}
                    for attr in ['get_xy','get_xdata','get_ydata','get_text','get_position','get_facecolor','get_edgecolor','get_linewidth','get_linestyle','get_offsets','get_sizes']:
                        if hasattr(obj,attr):
                            try:
                                v=getattr(obj,attr)()
                                a[attr]=v.tolist() if hasattr(v,'tolist') else v
                            except Exception as e:
                                a[attr] = str(e)
                    artists[oid].append(a)
            dump(root/'native_artists.json',artists)
        finally:
            with_scene.close()
        for rel,h in audit['source_content']['files'].items():
            source_hashes[str((BRANCH/rel).resolve())] = h
        source_hashes[str(PROJECT/'provenance/approvals.json')] = sha(PROJECT/'provenance/approvals.json')
        source_hashes[str(PROJECT/'provenance/source_notes.json')] = sha(PROJECT/'provenance/source_notes.json')
        # Read-only inventory of ALL existing qid-directory files and related global excerpts.
        old=[]
        for p in ROOT.rglob('*'):
            if not p.is_file() or p.is_relative_to(OWN):
                continue
            if qid in p.parts or qid in p.name:
                old.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
        dump(root/'old_file_manifest.json',old)
        print(json.dumps({'qid':qid,'eligible':audit['eligible'],'approval':audit['current_content_sha256'],'objects':len(metadata['objects']),
                          'old_files':len(old),'formal_scene':formal_scene},ensure_ascii=False),flush=True)
    dump(OWN/'source_hashes_before.json',source_hashes)
    dump(OWN/'isolation.json',{'ownroot':str(OWN),'isolation':ISOLATION,'strict_guard_before_project_imports':True,'pid':os.getpid()})

if __name__=='__main__':
    main()
