"""Package an existing independently recommended design; no solver calls."""
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
        if (isinstance(mode, str) and any(x in mode for x in 'wax+')) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC)):
            check_write(path)
    elif event in ('os.mkdir','os.rmdir','os.remove','os.chmod','os.utime'):
        check_write(args[0])
    elif event in ('os.rename','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(ROOT))
from dataset_tools import catalog

review_path = HERE/'independent_review/Solid166_r12_full_seam_context_x_four_r1/independent_review.json'
review = read(review_path)
source = Path(review['candidate_directory'])
assert source.is_relative_to(HERE)
assert review['decision'] == 'recommended' and review['unresolved_blocking_objections'] == []
assert review['method_fidelity']['classification'] == 'extension'
for filename, field in [('candidate.png','image_sha256'),('plugin.json','plugin_sha256'),('design.json','design_sha256')]:
    assert sha(source/filename) == review[field]
assert sha(Path(review['summary_path'])) == review['summary_sha256']

record = next(r for r in catalog.rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id'] == 'Solid166')
approval = read(ROOT/'provenance/approvals.json')['approvals']['Solid166']
fingerprint = catalog.digest(catalog.content(ROOT, 'SolidGeometry', record))
assert fingerprint == approval['content_sha256'] == review['current_eligibility']['final_recomputed_content_sha256']
assert record == review['current_eligibility']['formal_record']
special = ROOT/'SolidGeometry/special_variant'
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    file = special/name
    assert not file.exists() or not any(r.get('id',r.get('question_id')) == 'Solid166' for r in catalog.rows(file))
assert not (special/'Solid166/recipes.json').exists()
assert not (special/'Solid166/collection.json').exists()

support = HERE/'delivery_support/Solid166/review_audit'
support.mkdir(parents=True, exist_ok=False)
for name in ['independent_math.json','exact_replay.json','candidate_transport_audit.json',
             'all_twelve_trial_transport_audit.json','world_projection_visibility.json',
             'current_eligibility.json','scoped_preservation_final.json','old_evidence_preservation.json',
             'process_closure.json','old_history_index_Solid166.json']:
    original = review_path.parent/name
    shutil.copyfile(original, support/name)
    assert sha(original) == sha(support/name)
for original in review_path.parent.glob('offline_error_*.json'):
    shutil.copyfile(original, support/original.name)

selection = [{
    'candidate':str(source.relative_to(HERE)).replace('\\','/'),
    'independent_review':str(review_path.relative_to(HERE)).replace('\\','/'),
    'final_answers':['4','4'],
    'control_answers':[],
    'mechanism':'扩展模仿 Solid203 的原边同色对应：红色比较 x 与 4，另三组颜色追踪真实接缝，形成具体的边对应参照。',
    'limitation':'扩展型模仿：8 条原边、4 组颜色，比用户原例更丰富。正确答案为 5，冻结错误预设为 4，两次完整终答均为 4；仅报告这两次命中，不证明因果增益或每条标记的必要性。源 JPG 的统一灰底在现有正式 PNG 中已为白色，本变体未改变填充。',
    'supplemental_evidence':[
        {'source':'references/Solid203','destination':'reference_current_user_Solid203'},
        {'source':'units/u09_octa_nets/Solid166','destination':'preserved_current_question_history'},
        {'source':'delivery_support/Solid166/review_audit','destination':'independent_review_support'},
    ],
}]
selection_path = HERE/'selection_batch_01.json'
dump(selection_path, selection)
spec = importlib.util.spec_from_file_location('readonly_packager', HERE/'publish_batch.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
summary, _, _ = helper.verify_evidence(source)
assert summary['requested_runs'] == len(summary['results']) == 2
assert summary['design_sha256'] == sha(source/'design.json')
for result, final in zip(summary['results'], review['actual_complete_final_readings']):
    assert result['answer'] == final['complete_answer']
    assert final['final_value'] == '4' and final['exact_frozen_preset_match']

helper.build(selection_path, 'batch_01')
batch = HERE/'batch_01'
archive = HERE/'batch_01.zip'
verification = HERE/'batch_01_verification'
verification.mkdir(exist_ok=False)
extract_root = verification/'unpacked'
extract_root.mkdir()
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    archive_files = set()
    for item in bundle.infolist():
        target = (extract_root/item.filename).resolve()
        assert target.is_relative_to(extract_root.resolve()) and not item.is_dir()
        local = HERE/item.filename
        assert local.is_relative_to(batch) and bundle.read(item) == local.read_bytes()
        archive_files.add(item.filename)
    local_files = {str(f.relative_to(HERE)).replace('\\','/') for f in batch.rglob('*') if f.is_file()}
    assert archive_files == local_files
    bundle.extractall(extract_root)
dump(verification/'archive_integrity.json', {
    'checked_at_utc':datetime.now(timezone.utc).isoformat(), 'archive_sha256':sha(archive),
    'archive_members':len(archive_files), 'all_member_bytes_equal_staged_batch':True,
    'CRC_passed':True, 'extraction_root':str(extract_root), 'new_solver_calls':0,
    'approval_content_sha256_recomputed':fingerprint,
    'research_recommendation_only_no_Pass_Collect':True,
})
dump(HERE/'delivery_batch_01_prepared.json', {
    'created_at_utc':datetime.now(timezone.utc).isoformat(), 'question_id':'Solid166',
    'batch':str(batch), 'zip':str(archive), 'PNG':str(batch/'Solid166/candidate.png'),
    'review':str(batch/'review.html'), 'status':'PACKAGED_PENDING_FRESH_UNPACKED_OFFLINE_REPLAY',
    'imitation_fidelity':'extension', 'formal_edits':0, 'solver_calls':0,
})
print(json.dumps({'archive':str(archive), 'bytes':archive.stat().st_size,
                  'members':len(archive_files), 'next':'Fresh offline replay from unpacked ZIP, no solver call.'},ensure_ascii=False))
