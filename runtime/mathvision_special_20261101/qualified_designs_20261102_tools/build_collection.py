"""Consolidate existing reviewed deliveries. No rendering, solver calls or formal writes."""
from pathlib import Path
import base64
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import json
import os
import shutil
import sys
import zipfile

sys.dont_write_bytecode = True
TOOLS = Path(__file__).resolve().parent
BASE = TOOLS.parent
ROOT = BASE.parents[1]
OUT = BASE / 'qualified_designs_20261102'
ARCHIVE = BASE / 'qualified_designs_20261102.zip'
assert not ARCHIVE.exists(), 'Never overwrite an existing delivery archive.'
assert not OUT.exists() or (OUT.is_dir() and not any(OUT.iterdir())), 'Never overwrite an existing delivery.'
OUT.mkdir(exist_ok=True)


def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OUT):
        raise PermissionError('Consolidation writes only into its new runtime delivery: ' + str(resolved))


def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        if Path(os.fsdecode(args[0])).resolve() != ARCHIVE:
            check_write(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check_write(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check_write(args[0])
        check_write(args[1])


sys.addaudithook(guard)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(BASE))
from publish_batch import verify_evidence
from dataset_tools import catalog


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(262144), b''):
            digest.update(block)
    return digest.hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def tree_hashes(directory):
    return {p.relative_to(directory).as_posix(): sha(p) for p in sorted(directory.rglob('*')) if p.is_file()}


def digest_record(record):
    return hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


def esc(value):
    return html.escape(str(value), quote=True)


def uri(path):
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def pretty_answer(value, record):
    choices = record.get('choices', {})
    text = choices.get(str(value)) if isinstance(choices, dict) else None
    return str(value) + (' · ' + str(text) if text is not None else '')


def main():
    manifests = sorted(BASE.glob('batch_[0-9][0-9]/manifest.json'))
    assert len(manifests) == 14
    expected_ids = {'Solid176', 'Plane308', 'Solid203', 'Plane217', 'Plane234', 'Solid142',
                    'Plane259', 'Solid167', 'Plane324', 'Plane391', 'Plane404', 'Solid197',
                    'Solid128', 'Plane192', 'Plane233', 'Solid126', 'Solid230', 'Plane427'}
    approvals = read(ROOT / 'provenance/approvals.json')['approvals']
    entries, audit, source_snapshots = [], [], {}
    formal_files = {}
    for manifest_path in manifests:
        batch = manifest_path.parent.name
        batch_dir = manifest_path.parent
        old_zip = BASE / (batch + '.zip')
        source_snapshots[batch] = {'files_sha256': tree_hashes(batch_dir), 'zip_sha256': sha(old_zip)}
        with zipfile.ZipFile(old_zip) as zipped:
            assert zipped.testzip() is None, batch
            for name in zipped.namelist():
                relative = Path(name)
                assert not relative.is_absolute() and '..' not in relative.parts
                assert relative.parts[0] == batch
                assert hashlib.sha256(zipped.read(name)).hexdigest() == sha(BASE / relative), name
        selection = read(BASE / (batch + '_selection.json'))
        for item in read(manifest_path)['candidates']:
            q = item['question_id']
            source = batch_dir / q
            original_source = BASE / item['candidate_source']
            summary, record, summary_path = verify_evidence(source)
            evidence = summary_path.parent
            chosen = next(x for x in selection if (BASE / x['candidate']).resolve() == original_source.resolve())
            review_path = source / 'independent_review.json'
            report = read(review_path)
            preset = str(item['expected_wrong_answer'])
            assert report['decision'] == 'recommended'
            assert sha(review_path) == sha(BASE / chosen['independent_review'])
            assert sha(source / 'design.json') == sha(evidence / 'design_snapshot.json')
            assert sha(source / 'design.json') == sha(original_source / 'design.json')
            assert sha(source / 'candidate.png') == item['candidate_sha256'] == sha(original_source / 'candidate.png')
            assert sha(source / 'plugin.json') == item['plugin_sha256'] == sha(original_source / 'plugin.json')
            assert sha(batch_dir / 'reproduced' / (q + '.png')) == item['candidate_sha256']
            assert summary['requested_runs'] == len(summary['results']) == 2
            assert summary['two_completed'] is True
            assert item['tested_final_answers'] == [item['expected_wrong_answer']] * 2
            assert str(summary['expected_wrong_answer']) == preset != str(record['answer'])
            assert str(record['answer']) == str(item['correct_answer'])
            assert record['question'] == item['question'] == summary['question']
            assert record['source_dataset'] == 'MathVision'
            assert digest_record(record) == item['record_sha256'] == summary['question_record_sha256']
            assert sha(evidence / 'request.json') == summary['request_body_sha256']
            assert summary['profile'] == 'quicktest3'
            assert summary['settings']['model'] == 'mimo-v2.6-flash'
            assert summary['settings']['thinking'] == {'type': 'disabled'}
            binding = read(evidence / 'binding.json')
            assert all(binding[key] == summary[key] for key in binding)
            request = read(evidence / 'request.json')
            assert set(request) == {'model', 'stream', 'thinking', 'messages'}
            assert request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type': 'disabled'}
            raw_endings = []
            for index, result in enumerate(summary['results'], 1):
                raw = read(evidence / f'run_{index:02d}_response.json')
                assert raw['choices'][0]['message']['content'] == result['answer']
                assert raw['choices'][0]['finish_reason'] == 'stop'
                assert result['request_body_sha256'] == summary['request_body_sha256']
                raw_endings.append(result['answer'][-700:])
            branch = item['branch']
            fingerprint = catalog.digest(catalog.content(ROOT, branch, record))
            approval = approvals[q]
            assert approval['reviewer'] == 'user' and approval['instruction']
            assert fingerprint == approval['content_sha256']
            assert sha(source / 'original.png') == sha(ROOT / branch / record['image'])
            for special_index in ['accepted_index.jsonl', 'collected_index.jsonl']:
                index_path = ROOT / branch / 'special_variant' / special_index
                matching = [r for r in catalog.rows(index_path) if r.get('question_id', r.get('id')) == q]
                assert not matching, (q, special_index, 'Special state changed')
                formal_files[index_path.relative_to(ROOT).as_posix()] = sha(index_path)
            assert not (ROOT / branch / 'special_variant' / q / 'recipes.json').exists()
            assert not (ROOT / branch / 'special_variant' / q / 'collection.json').exists()
            for relative, expected in item['input_files'].items():
                assert sha(ROOT / relative) == expected, relative
                formal_files[relative] = expected
            for supplement in item.get('supplemental_evidence', []):
                for relative, expected in supplement['files_sha256'].items():
                    assert sha(batch_dir / supplement['packaged_path'] / relative) == expected
            for relative in [branch + '/dataset.jsonl', 'provenance/approvals.json']:
                formal_files[relative] = sha(ROOT / relative)
            rel_candidate = f'batches/{batch}/{q}'
            entries.append({
                **item,
                'variant_id': read(source / 'design.json').get('variant_id') or original_source.name,
                'source_batch': batch,
                'correct_answer_display': pretty_answer(record['answer'], record),
                'expected_wrong_answer_display': pretty_answer(item['expected_wrong_answer'], record),
                'limitation': chosen.get('limitation', ''),
                'independent_review_sha256': sha(review_path),
                'current_original_approval_content_sha256': fingerprint,
                'packaged_directory': rel_candidate,
                'packaged_evidence_summary': f'{rel_candidate}/{summary_path.relative_to(source).as_posix()}',
                'easy_access_candidate_png': f'candidate_pngs/{q}.png',
                'easy_access_plugin_json': f'plugins/{q}.json',
                'test_full_answers': [r['answer'] for r in summary['results']],
            })
            audit.append({'question_id': q, 'source_batch': batch, 'qualified': True,
                          'same_frozen_image_two_complete_responses': True,
                          'predeclared_preset_matches_existing_independent_manual_final_review': True,
                          'raw_response_and_request_bindings_exact': True,
                          'independent_review_recommended_and_byte_identical': True,
                          'existing_reproduced_png_exact': True,
                          'current_formal_record_approval_and_original_image_match': True,
                          'current_special_pass_collect_absent': True,
                          'original_full_answer_endings': raw_endings})
            print('VERIFIED', q, preset + '/' + preset, 'correct', record['answer'], flush=True)
    assert {e['question_id'] for e in entries} == expected_ids and len(entries) == 18
    entries.sort(key=lambda e: (0 if e['branch'] == 'PlaneGeometry' else 1,
                                int(''.join(c for c in e['question_id'] if c.isdigit()))))
    counts = Counter(e['branch'] for e in entries)
    assert counts == {'PlaneGeometry': 10, 'SolidGeometry': 8}
    (OUT / 'batches').mkdir()
    (OUT / 'candidate_pngs').mkdir()
    (OUT / 'plugins').mkdir()
    for manifest_path in manifests:
        source = manifest_path.parent
        target = OUT / 'batches' / source.name
        shutil.copytree(source, target)
        assert tree_hashes(target) == source_snapshots[source.name]['files_sha256']
    for entry in entries:
        source = OUT / entry['packaged_directory']
        shutil.copyfile(source / 'candidate.png', OUT / entry['easy_access_candidate_png'])
        shutil.copyfile(source / 'plugin.json', OUT / entry['easy_access_plugin_json'])
    manifest = {
        'title': 'MathVision Special 合格设计汇总',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'count': 18, 'branch_counts': dict(counts),
        'qualification': '同一冻结 PNG 的两次完整 quicktest3 终答命中事前预设错误答案；已有独立二审 recommended，已核验数学唯一性、标记信息性、简洁性和原生可读性。',
        'approval_status': '全部仍待用户 Special Pass / Collect；研究推荐不代替用户审批。',
        'exploration_status': '按用户要求保持暂停；本次整理没有新增模型调用或探索。',
        'evidence_scope': '仅重核并复制既有 14 个交付批次；没有重新推断模型机制，没有改写原图、冻结设计、预设答案、旧证据或正式数据。',
        'statistical_scope': '两次观察命中不估计总体命中率、不证明因果增益；逐题原图对照及机制限制见 limitation 和原始独立二审。',
        'candidates': entries,
    }
    dump(OUT / 'manifest.json', manifest)
    dump(OUT / 'verification.json', {
        'created_at': manifest['created_at'], 'count': len(entries), 'checks': audit,
        'source_batches_before_sha256': source_snapshots,
        'relevant_formal_files_before_sha256': formal_files,
        'no_new_solver_calls': True,
    })
    write_readme(manifest)
    write_html(manifest)
    # Verify all links and exact bytes after consolidation, without executing copied helpers.
    for entry in entries:
        for relative in [entry['packaged_directory'] + '/original.png',
                         entry['packaged_directory'] + '/candidate.png',
                         entry['packaged_directory'] + '/independent_review.json',
                         entry['packaged_evidence_summary'], entry['easy_access_candidate_png'],
                         entry['easy_access_plugin_json']]:
            assert (OUT / relative).is_file(), relative
        assert sha(OUT / entry['easy_access_candidate_png']) == entry['candidate_sha256']
        assert sha(OUT / entry['easy_access_plugin_json']) == entry['plugin_sha256']
    for name, before in source_snapshots.items():
        assert tree_hashes(BASE / name) == before['files_sha256']
        assert sha(BASE / (name + '.zip')) == before['zip_sha256']
    assert all(sha(ROOT / relative) == expected for relative, expected in formal_files.items())
    dump(OUT / 'source_preservation.json', {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'all_14_original_batch_trees_and_archives_unchanged': True,
        'all_18_candidate_copies_and_supplements_byte_identical': True,
        'relevant_formal_files_unchanged_during_consolidation': True,
        'source_batch_file_count': sum(len(x['files_sha256']) for x in source_snapshots.values()),
        'relevant_formal_file_count': len(formal_files),
        'scope': '仅上述明确跟踪文件；不宣称整个工作区未变化。',
    })
    dump(OUT / 'checksums.json', tree_hashes(OUT))
    with zipfile.ZipFile(ARCHIVE, 'x', zipfile.ZIP_DEFLATED) as zipped:
        for path in sorted(OUT.rglob('*')):
            if path.is_file():
                zipped.write(path, OUT.name + '/' + path.relative_to(OUT).as_posix())
    with zipfile.ZipFile(ARCHIVE) as zipped:
        assert zipped.testzip() is None
        for name in zipped.namelist():
            relative = Path(name)
            assert not relative.is_absolute() and '..' not in relative.parts
            assert hashlib.sha256(zipped.read(name)).hexdigest() == sha(BASE / relative)
    print(json.dumps({'count': 18, 'branch_counts': dict(counts), 'index': str(OUT / 'index.html'),
                      'archive': str(ARCHIVE), 'archive_sha256': sha(ARCHIVE),
                      'archive_bytes': ARCHIVE.stat().st_size, 'new_API_calls': 0}, ensure_ascii=False))


def write_readme(manifest):
    lines = [
        'MathVision Special 合格设计汇总（2026-11-02）',
        '', '共18份：平面10份、立体8份。',
        '打开 index.html 查看原图/变体、正式题干、诱导设计、预设错答、两次完整模型回答与二审链接。无需联网。',
        'candidate_pngs/：按正式题号命名的18张最终候选PNG。',
        'plugins/：与最终候选精确对应的18份插件JSON。',
        'batches/：14个原交付批次的逐字节副本，含冻结设计、原图、原始请求/响应、独立二审及现有重放结果。',
        'manifest.json：统一结构化清单，保留逐题限制与证据路径。',
        'verification.json / source_preservation.json / checksums.json：本次只读核验、来源保全与逐文件哈希。',
        '', '判定范围：两次完整quicktest3终答命中调用前冻结的错误预设；独立二审推荐，原题唯一正确答案和人类可读性保持。',
        '研究推荐不代表用户Pass/Collect。原图对照与实际推理限制均保留，不据此声称总体成功率或因果增益。',
        'Solid230虽获独立二审推荐，原主审hold保留；两次实际均把6点读成5点，未证实原预设的值合并机制。',
        '探索继续暂停；本次仅整理既有交付，无新模型调用，不修改正式库或旧证据。',
        '', '题号 | 正确答案 | 冻结错答 | 两次终答 | 原图对照',
    ]
    for e in manifest['candidates']:
        controls = ' / '.join(map(str, e['original_control_answers'])) or '未测'
        lines.append(f"{e['question_id']} | {e['correct_answer_display']} | {e['expected_wrong_answer_display']} | "
                     + ' / '.join(map(str, e['tested_final_answers'])) + ' | ' + controls)
    for e in manifest['candidates']:
        lines.extend(['', e['question_id'] + ' · ' + e['variant_id'],
                      '设计：' + e['mechanism'], '限制：' + e['limitation'],
                      '证据：' + e['packaged_directory'] + '/'])
    (OUT / 'README.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_html(manifest):
    rows, cards = [], []
    for e in manifest['candidates']:
        q = e['question_id']
        branch = 'plane' if e['branch'] == 'PlaneGeometry' else 'solid'
        label = '平面' if branch == 'plane' else '立体'
        target = e['packaged_directory']
        controls = ' / '.join(map(str, e['original_control_answers'])) or '未测'
        finals = ' / '.join(map(str, e['tested_final_answers']))
        rows.append(f'<tr data-kind="{branch}" data-q="{q.lower()}"><td><a href="#{q}">{q}</a></td>'
                    f'<td>{label}</td><td>{esc(e["correct_answer_display"])}</td>'
                    f'<td>{esc(e["expected_wrong_answer_display"])}</td><td>{esc(finals)}</td><td>{esc(controls)}</td></tr>')
        answers = ''.join('<details><summary>第' + str(i) + '次完整 quicktest3 回答</summary><pre>'
                          + esc(answer) + '</pre></details>' for i, answer in enumerate(e['test_full_answers'], 1))
        images = ''.join(f'<figure><figcaption>{title}</figcaption><a href="{target}/{name}" target="_blank" rel="noopener">'
                         f'<img src="{uri(OUT / target / name)}" alt="{q} {title}" width="768" height="768" loading="lazy"></a></figure>'
                         for title, name in [('原图', 'original.png'), ('变体 · 实际测试图', 'candidate.png')])
        special = '<p class="special">原主审 HOLD 保留。二审推荐的是双次预设数值命中；实际错误为 6→5，未证实预设机制。</p>' if q == 'Solid230' else ''
        cards.append(f'''<article id="{q}" data-kind="{branch}" data-q="{q.lower()}">
<header><h2>{q}</h2><span class="badge">{label} · 双次命中 · 独立二审推荐</span><a class="back" href="#top">回到清单 ↑</a></header>
<p class="mechanism">{esc(e['mechanism'])}</p>
<dl><div><dt>正确答案</dt><dd>{esc(e['correct_answer_display'])}</dd></div><div><dt>冻结错答</dt><dd>{esc(e['expected_wrong_answer_display'])}</dd></div><div><dt>两次终答</dt><dd>{esc(finals)}</dd></div><div><dt>原图对照</dt><dd>{esc(controls)}</dd></div></dl>
{special}<p class="limitation"><strong>复核备注：</strong>{esc(e['limitation'])}</p>
<div class="images">{images}</div>
<p class="links"><a href="{e['easy_access_candidate_png']}" download>候选 PNG</a><a href="{e['easy_access_plugin_json']}" download>插件 JSON</a><a href="{target}/independent_review.json">独立二审</a><a href="{e['packaged_evidence_summary']}">双测证据</a><a href="batches/{e['source_batch']}/review.html">原批次审阅页</a></p>
<details><summary>正式题干与选项</summary><pre>{esc(e['question'])}</pre></details>{answers}
<details><summary>设计标识与文件指纹</summary><pre>{esc(e['variant_id'])}\nPNG SHA-256: {e['candidate_sha256']}\n插件 SHA-256: {e['plugin_sha256']}\n二审 SHA-256: {e['independent_review_sha256']}</pre></details>
</article>''')
    style = '''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:16px}body{margin:0;background:#f4f6f8;color:#172638;font-family:"Microsoft YaHei",system-ui,sans-serif;line-height:1.65}main{max-width:1160px;margin:auto;padding:36px 24px 70px}.intro,article,.listing{background:white;border:1px solid #dce3e9;border-radius:12px;padding:24px;margin-bottom:22px}h1{font-size:28px;margin:0 0 10px}h2{font-size:23px;margin:0}p{margin:10px 0}a{color:#245caf;text-underline-offset:3px}.meta{color:#536576;font-size:14px}.counts{display:flex;gap:12px;margin:18px 0;flex-wrap:wrap}.counts span{background:#edf4fa;padding:8px 15px;border-radius:8px}.controls{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:12px 0}input,select{font:inherit;border:1px solid #bdcbd8;border-radius:6px;padding:9px 12px;background:#fff}input{min-width:230px}table{width:100%;border-collapse:collapse;font-size:14px}th,td{padding:10px 12px;border-bottom:1px solid #e5eaf0;text-align:left}th{background:#f3f6f9;font-weight:600}.table-wrap{overflow-x:auto}article header{display:flex;gap:16px;align-items:center;flex-wrap:wrap}.badge{font-size:12px;background:#edf6ef;color:#235c3a;border-radius:5px;padding:4px 9px}.back{margin-left:auto;font-size:13px}.mechanism{font-size:16px;margin-top:18px}dl{display:flex;gap:24px;flex-wrap:wrap;margin:18px 0;padding:14px 16px;background:#f3f6f9;border-radius:8px}dt{font-size:12px;color:#5b6c7b}dd{margin:2px 0;font-weight:600}.limitation{font-size:14px;color:#526474;border-left:3px solid #becbd6;padding-left:12px}.special{background:#fff3dd;border-radius:6px;padding:10px 12px;font-size:14px;color:#754b0c}.images{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:18px 0}figure{margin:0;border:1px solid #e1e6eb;background:white;border-radius:8px;overflow:hidden}figcaption{text-align:center;font-size:13px;background:#f5f7fa;padding:7px}img{width:100%;height:auto;display:block}.links{display:flex;gap:17px;flex-wrap:wrap;font-size:14px}details{border-top:1px solid #e4e9ee;padding:11px 0}summary{cursor:pointer;font-size:14px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px;line-height:1.65;background:#f8fafc;padding:14px;border-radius:6px;margin:10px 0;font-family:Consolas,"Microsoft YaHei",monospace}.hidden{display:none!important}footer{color:#586979;font-size:13px;padding:8px 4px}@media(max-width:700px){main{padding:16px 10px}.intro,article,.listing{padding:16px}.images{grid-template-columns:1fr}h1{font-size:23px}.back{margin-left:0}th,td{padding:9px 8px}dl{gap:15px}}@media print{body{background:white}main{padding:0}.controls,.back{display:none}article{break-inside:avoid}.intro,article,.listing{border-color:#bbb}a{color:inherit}}'''
    markup = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MathVision Special · 18 份合格设计</title><style>{style}</style></head><body><main id="top">
<section class="intro"><p class="meta">MathVision · Special 设计汇总 · 2026-11-02</p><h1>18 份合格设计</h1>
<div class="counts"><span>平面 10 份</span><span>立体 8 份</span><span>全部双次命中 + 独立二审推荐</span></div>
<p>每份均在同一冻结图上完成两次 quicktest3，完整终答命中测试前预设的错误答案；独立二审核验了唯一正确答案、标记用途、简洁性与原生可读性。</p>
<p class="meta">均待用户 Pass / Collect。两次观察不代表总体成功率；原图对照与实际推理限制逐题保留。探索保持暂停，本次整理没有新增模型调用。</p>
<p class="links"><a href="README.txt">文字清单</a><a href="manifest.json">统一数据清单</a><a href="verification.json">核验记录</a><a href="source_preservation.json">来源保全</a></p></section>
<section class="listing"><div class="controls"><input id="search" type="search" placeholder="搜索题号，例如 Plane217" aria-label="搜索题号"><select id="branch" aria-label="题目分支"><option value="all">全部题目</option><option value="plane">平面</option><option value="solid">立体</option></select><span id="visible-count" class="meta">显示 18 / 18 份</span></div>
<div class="table-wrap"><table><thead><tr><th>题号</th><th>分支</th><th>正确答案</th><th>冻结错答</th><th>两次终答</th><th>原图对照</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>
{''.join(cards)}<footer>图像以原始 768×768 PNG 嵌入，点击可查看原尺寸。所有旧批次、测试响应与二审报告按字节保留。未执行 Pass、Collect 或正式数据变更。</footer></main>
<script>function filter(){{const text=document.getElementById('search').value.trim().toLowerCase(),kind=document.getElementById('branch').value;let count=0;document.querySelectorAll('article[data-q]').forEach(a=>{{const visible=a.dataset.q.includes(text)&&(kind==='all'||a.dataset.kind===kind);a.classList.toggle('hidden',!visible);if(visible)count++}});document.querySelectorAll('tr[data-q]').forEach(a=>a.classList.toggle('hidden',!(a.dataset.q.includes(text)&&(kind==='all'||a.dataset.kind===kind))));document.getElementById('visible-count').textContent='显示 '+count+' / 18 份'}}document.getElementById('search').addEventListener('input',filter);document.getElementById('branch').addEventListener('change',filter);</script></body></html>'''
    (OUT / 'index.html').write_text(markup, encoding='utf-8')


if __name__ == '__main__':
    main()
