"""Package the already reviewed close imitation; no new design or solver call."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import zipfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def check_write(path):
    if isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(HERE):
        raise PermissionError('Packing write outside own runtime case: '+str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if (isinstance(mode,str) and any(x in mode for x in 'wax+')) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC)):
            check_write(path)
    elif event in ('os.mkdir','os.rmdir','os.remove','os.chmod','os.utime'):
        check_write(args[0])
    elif event in ('os.rename','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0,str(ROOT))
from dataset_tools import catalog

review_path = HERE/'independent_review/Plane321_a01_pivot_legs_vs_true_bases_r1/independent_review.json'
review = read(review_path)
source = Path(review['candidate_directory'])
assert source.is_relative_to(HERE)
assert review['decision'] == 'recommended' and review['blocking_objections'] == []
assert review['method_fidelity']['classification'] == 'close imitation'
for filename, field in [('candidate.png','candidate_png_sha256'),('plugin.json','plugin_sha256'),('design.json','design_sha256')]:
    assert sha(source/filename) == review[field]
assert sha(Path(review['summary_path'])) == review['summary_sha256']
record = next(r for r in catalog.rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']=='Plane321')
approval = read(ROOT/'provenance/approvals.json')['approvals']['Plane321']
fingerprint = catalog.digest(catalog.content(ROOT,'PlaneGeometry',record))
assert fingerprint == approval['content_sha256'] == review['current_eligibility']['current_content_sha256']
special = ROOT/'PlaneGeometry/special_variant'
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    file = special/name
    assert not file.exists() or not any(r.get('id',r.get('question_id'))=='Plane321' for r in catalog.rows(file))
assert not (special/'Plane321/recipes.json').exists()
assert not (special/'Plane321/collection.json').exists()

support = HERE/'delivery_support/Plane321/review_audit'
support.mkdir(parents=True,exist_ok=False)
for name in ['independent_math_proof.json','exact_replay.json','frozen_binding_audit.json',
             'archive_history_audit.json','current_eligibility.json','scoped_preservation_final.json',
             'scoped_sources_before.json','old_history_read.json','process_closure_os.json',
             'final_validation.json','request_history_scan.json','supporting_integrity_audit.json']:
    original = review_path.parent/name
    shutil.copyfile(original,support/name)
    assert sha(original)==sha(support/name)
for original in review_path.parent.glob('offline_error_*.json'):
    shutil.copyfile(original,support/original.name)

selection = [{
    'candidate':str(source.relative_to(HERE)).replace('\\','/'),
    'independent_review':str(review_path.relative_to(HERE)).replace('\\','/'),
    'final_answers':['B = 120°','B = 120°'],
    'control_answers':[],
    'mechanism':'贴近模仿 Plane427 的原边角色配色：绕 A 的边 AB、AC、AD 为蓝色，对应的对边 BC、CD 为红色，仅对原有五条边着色并适度加粗。',
    'limitation':'正确答案 E = 300°；事前冻结错误预设 B = 120°，两次完整终答均为 B = 120°。两份推理错误不同，仅报告这两次命中，不证明具体机制、因果增益或每条标记的必要性。现行参考图为红色两腰、蓝色底边，本图保留同一角色分组并交换配色。',
    'supplemental_evidence':[
        {'source':'references/Plane427','destination':'reference_current_user_Plane427'},
        {'source':'units/u04_angles/Plane321','destination':'preserved_current_question_history'},
        {'source':'delivery_support/Plane321/review_audit','destination':'independent_review_support'},
    ],
}]
selection_path = HERE/'selection_batch_02.json'
dump(selection_path,selection)
spec = importlib.util.spec_from_file_location('readonly_packager',HERE/'publish_batch.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
summary, current_record, evidence_path = helper.verify_evidence(source)
assert current_record == record
assert summary['requested_runs'] == len(summary['results']) == 2
assert summary['design_sha256'] == sha(source/'design.json')
assert sha(source/'design.json') == sha(evidence_path.parent/'design_snapshot.json')
for result, final in zip(summary['results'],review['complete_final_readings']):
    assert result['answer'] == final['raw_content']
    assert final['final_letter']=='B' and final['final_value_degrees']=='120' and final['matches_frozen_preset']
helper.build(selection_path,'batch_02')
batch=HERE/'batch_02';archive=HERE/'batch_02.zip';verification=HERE/'batch_02_verification'
verification.mkdir(exist_ok=False)
extract_root=verification/'unpacked';extract_root.mkdir()
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    archive_files=set()
    for item in bundle.infolist():
        target=(extract_root/item.filename).resolve()
        assert target.is_relative_to(extract_root.resolve()) and not item.is_dir()
        local=HERE/item.filename
        assert local.is_relative_to(batch) and bundle.read(item)==local.read_bytes()
        archive_files.add(item.filename)
    assert archive_files=={str(f.relative_to(HERE)).replace('\\','/') for f in batch.rglob('*') if f.is_file()}
    bundle.extractall(extract_root)
dump(verification/'archive_integrity.json',{
    'checked_at_utc':datetime.now(timezone.utc).isoformat(),'archive_sha256':sha(archive),
    'archive_members':len(archive_files),'all_member_bytes_equal_staged_batch':True,'CRC_passed':True,
    'extraction_root':str(extract_root),'new_solver_calls':0,'approval_content_sha256_recomputed':fingerprint,
    'research_recommendation_only_no_Pass_Collect':True,
})
replay_source=(HERE/'replay_batch01_unpacked.py').read_text(encoding='utf-8-sig')
assert 'Solid166' in replay_source and 'batch_01' in replay_source
(HERE/'replay_batch02_unpacked.py').write_text(replay_source.replace('batch_01','batch_02').replace('Solid166','Plane321'),encoding='utf-8')
dump(HERE/'delivery_batch_02_prepared.json',{
    'created_at_utc':datetime.now(timezone.utc).isoformat(),'question_id':'Plane321','batch':str(batch),
    'zip':str(archive),'PNG':str(batch/'Plane321/candidate.png'),'review':str(batch/'review.html'),
    'status':'PACKAGED_PENDING_FRESH_UNPACKED_OFFLINE_REPLAY','imitation_fidelity':'close imitation',
    'formal_edits':0,'solver_calls':0,
})
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'members':len(archive_files),
                  'next':'Fresh offline replay from unpacked ZIP, no solver call.'},ensure_ascii=False))
