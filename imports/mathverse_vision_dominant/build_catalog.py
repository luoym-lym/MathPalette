"""Register every retained MathVerse redraw and publish its separate QA findings.

Run only after the branch generators have finished. It never changes source GT,
drawings, Base recipes or Special acceptance records.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import platform
import sys

from PIL import Image

IMPORT = Path(__file__).resolve().parent
ROOT = IMPORT.parents[1]
sys.path.insert(0, str(ROOT))
from dataset_tools.geometry_dataset import write_json, read_json
from dataset_tools.geometry_review import read_registry, registration_for


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(path):
    return Path(path).relative_to(ROOT).as_posix()


def jsonl(path, rows):
    Path(path).write_text(''.join(json.dumps(r, ensure_ascii=False, allow_nan=False)+'\n' for r in rows), encoding='utf-8')


def verification_for(assignment):
    qid, branch = assignment['id'], assignment['branch']
    if branch == 'Analytics':
        provenance_path = ROOT/branch/'fine_grained_dataset'/'provenance'/'MathVerse'/f'{qid}.json'
        provenance = read_json(provenance_path)
        av = provenance.get('answer_verification')
        if isinstance(av, str):
            av = {'reasoning': av, 'verified_answer': provenance.get('verified_answer'),
                  'issue': provenance.get('issue'),
                  'status': 'needs_review' if provenance.get('issue') else 'verified'}
        else:
            av = dict(av)
            av.setdefault('verified_answer', provenance.get('verified_answer'))
            av.setdefault('issue', provenance.get('issue'))
        if av.get('issue') == 'None':
            av['issue'] = None
        # Agents may retain an earlier status after resolving a concern.
        # The final, explicit issue field is authoritative for this import.
        av['status'] = 'needs_review' if av.get('issue') else 'verified'
        return av, provenance_path
    scene_path = ROOT/branch/'dataset_generator'/'scenes'/f'{qid}.json'
    return dict(read_json(scene_path)['answer_verification']), scene_path


def main():
    review_registry=read_registry()
    assignments = read_json(IMPORT/'assignments.json')
    manifest = {r['source_key']: r for r in read_json(IMPORT/'source_manifest.json')}
    assert len(assignments) == len(manifest)
    assert len({r['id'] for r in assignments}) == len(assignments)
    overrides = read_json(IMPORT/'root_verification.json') if (IMPORT/'root_verification.json').exists() else {}
    analytics_root = ROOT/'Analytics'/'fine_grained_dataset'
    analytics_rows = [json.loads(line) for line in (analytics_root/'dataset.jsonl').read_text(encoding='utf-8').splitlines() if line]
    assert len(analytics_rows) == 66, 'Complete Analytics registration/Base before catalog build.'
    analytics = {r['id']:r for r in analytics_rows}
    results = []
    for assignment in assignments:
        qid, branch = assignment['id'], assignment['branch']
        user_review=registration_for(branch,qid,review_registry)
        source = manifest[assignment['source_key']]
        av, verification_path = verification_for(assignment)
        av.update(overrides.get(qid, {}))
        assert av.get('reasoning'), f'{qid}: missing independent derivation'
        image_path = (analytics_root if branch=='Analytics' else ROOT/branch)/'image'/f'{qid}.png'
        with Image.open(image_path) as im:
            assert im.size == (768,768), qid
            assert im.convert('RGBA').getchannel('A').getextrema() == (255,255), qid
        original_copy = analytics_root/read_json(verification_path)['preserved_source_copy'] if branch=='Analytics' else ROOT/branch/'originals'/f'{qid}.png'
        assert sha(original_copy) == source['source_image_sha256'], qid
        if branch == 'Analytics':
            assert analytics[qid]['question'] == source['question'], qid
            assert analytics[qid]['answer'] == source['source_answer'], qid
            script_path = analytics_root/'dataset_generator'/'dataset_generator'/f'function_plot{int(qid[3:]):02d}.py'
            recipes = read_json(analytics_root/'base_variant'/qid/'recipes.json')
            assert len(recipes) == 4, qid
            assert len({r['operation'] for r in recipes}) == 4, qid
            report_path = IMPORT/'results'/'analytics'/f'{qid}_redraw_report.json'
            report = {'id':qid,'source_dataset':'MathVerse','source_provenance':source,
                      'question':source['question'],'answer':source['source_answer'],
                      'answer_verification':av,'determinism_and_base_replay_verified':True,
                      'inputs':{relative(p):sha(p) for p in [original_copy,script_path,verification_path,
                               analytics_root/'dataset_generator'/'mathverse_renderer.py']},
                      'output_png':relative(image_path),'output_png_sha256':sha(image_path),
                      'visual_review':{'status':'inspected','reviewer':'GPT-6-Luna and root source/redraw comparison','user_pass':user_review['user_pass']},
                      'user_review':user_review}
            write_json(report_path, report)
        else:
            scene = read_json(verification_path)
            assert scene['query'] == source['question'], qid
            assert scene['answer'] == source['source_answer'], qid
            report_path = ROOT/branch/'dataset_generator'/'reports'/f'{qid}_redraw_report.json'
            report = read_json(report_path)
            assert report['determinism_verified'] and report['all_constraints_passed'], qid
            assert report['output_png_sha256'] == sha(image_path), qid
            assert report['visual_review']['status'] == 'inspected', qid
            for fingerprint in report['inputs'].values():
                assert sha(ROOT/fingerprint['path']) == fingerprint['sha256'], f'{qid}: stale input'
            user_review=registration_for(branch,qid,review_registry)
            report['user_review']=user_review
            report['visual_review']['user_pass']=user_review['user_pass']
            write_json(report_path,report)
            result_path=IMPORT/'results'/('plane' if branch=='PlaneGeometry' else 'solid')/f"{source['source_key']}.json"
            prepared=read_json(result_path)
            prepared.update(user_review=user_review,user_pass=user_review['user_pass'],
                            registration_status=user_review['status'],visual_review=report['visual_review'])
            write_json(result_path,prepared)
            script_path = ROOT/branch/'dataset_generator'/f"{'plane' if branch=='PlaneGeometry' else 'solid'}_plot{int(qid[5:]):02d}.py"
        status = 'needs_review' if av.get('status') != 'verified' or av.get('issue') else 'verified'
        result = {**assignment,'source_dataset':'MathVerse','question':source['question'],
                  'answer':source['source_answer'],'source_answer':source['source_answer'],
                  'image':relative(image_path),'original_image':relative(original_copy),
                  'script':relative(script_path),'verification':relative(verification_path),
                  'report':relative(report_path),'image_sha256':sha(image_path),
                  'status':status,'answer_verification':av,'retained':True,
                  'user_pass':user_review['user_pass'],'registration_status':user_review['status'],
                  'user_review':user_review}
        results.append(result)
    for branch in ('PlaneGeometry','SolidGeometry'):
        branch_rows=[r for r in results if r['branch']==branch]
        def dataset_row(r):
            return {'id':r['id'],'question':r['question'],'answer':r['answer'],'image':f"image/{r['id']}.png"}
        jsonl(ROOT/branch/'dataset.jsonl',[dataset_row(r) for r in branch_rows if r['user_pass']])
        jsonl(ROOT/branch/'pending_dataset.jsonl',[dataset_row(r) for r in branch_rows if not r['user_pass']])
    jsonl(IMPORT/'imported_questions.jsonl', results)
    pending_geometry=[r for r in results if r['branch']!='Analytics' and not r['user_pass']]
    jsonl(IMPORT/'pending_geometry_questions.jsonl',pending_geometry)
    legacy=[]
    for row in analytics_rows[:20]:
        review=registration_for('Analytics',row['id'],review_registry)
        legacy.append({**row,'source_dataset':'DynaMath','branch':'Analytics',
                       'image':'Analytics/fine_grained_dataset/'+row['image'],
                       'retained':True,'user_review':review,'user_pass':review['user_pass'],
                       'registration_status':review['status']})
    candidates=legacy+results
    catalog=[r for r in candidates if r['registration_status']=='registered']
    jsonl(ROOT/'question_bank.jsonl', catalog)
    jsonl(ROOT/'question_candidates.jsonl',candidates)
    jsonl(ROOT/'pending_questions.jsonl',[r for r in candidates if not r['user_pass']])
    analytics_registration={r['id']:r['user_pass'] for r in candidates if r['branch']=='Analytics'}
    # The legacy Analytics dataset is a frozen input to Base/Special generation.
    # Preserve its bytes; publish a separate user-approved list for formal use.
    jsonl(analytics_root/'approved_dataset.jsonl',[r for r in analytics_rows if analytics_registration[r['id']]])
    jsonl(analytics_root/'pending_dataset.jsonl',[r for r in analytics_rows if not analytics_registration[r['id']]])
    registered_geometry=[r for r in results if r['branch']!='Analytics' and r['user_pass']]
    progress={'policy':'explicit_user_approval','registered_geometry_count':len(registered_geometry),
              'registered_geometry_ids':[r['id'] for r in registered_geometry],
              'pending_geometry_count':len(pending_geometry),'pending_geometry_ids':[r['id'] for r in pending_geometry],
              'question_bank_count':len(catalog),'all_candidates_retained':True}
    write_json(IMPORT/'geometry_review_progress.json',progress)
    write_json(IMPORT/'question_review_progress.json',{
        'policy':'explicit_user_approval','candidate_count':len(candidates),
        'registered_count':len(catalog),'registered_ids':[r['id'] for r in catalog],
        'pending_count':len(candidates)-len(catalog),
        'pending_ids':[r['id'] for r in candidates if not r['user_pass']],
        'registered_by_branch':dict(Counter(r['branch'] for r in catalog)),
        'pending_by_branch':dict(Counter(r['branch'] for r in candidates if not r['user_pass'])),
        'all_candidates_retained':True})
    issues = [r for r in results if r['status']=='needs_review']
    write_json(IMPORT/'issues.json', issues)
    counts = Counter(r['branch'] for r in results)
    snapshot = read_json(IMPORT/'existing_analytics_snapshot.json')
    unchanged, changed = [], []
    allowed = {'Analytics/fine_grained_dataset/dataset.jsonl','Analytics/fine_grained_dataset/base_variant/generated_index.jsonl'}
    for path, digest in snapshot.items():
        if path in allowed:
            continue
        (unchanged if sha(ROOT/path)==digest else changed).append(path)
    assert not changed, f'Existing frozen files changed: {changed}'
    old_prefix = b''.join((analytics_root/'dataset.jsonl').read_bytes().splitlines(keepends=True)[:20])
    normalized_prefix = old_prefix.replace(b'\r\n',b'\n')
    prefix_hashes = {hashlib.sha256(b).hexdigest() for b in (normalized_prefix,normalized_prefix.replace(b'\n',b'\r\n'))}
    assert snapshot['Analytics/fine_grained_dataset/dataset.jsonl'] in prefix_hashes, 'Old twenty records changed'
    for name in ('base_support.py','generate_base_variants.py'):
        assert sha(analytics_root/'dataset_generator'/name) == sha(IMPORT/'pipeline_before'/name), name
    deleted_dir=IMPORT/'archive'/'deleted_questions'
    deleted=[read_json(p/'deletion_record.json') for p in sorted(deleted_dir.iterdir())
             if (p/'deletion_record.json').exists()] if deleted_dir.exists() else []
    summary = {'source_dataset':'MathVerse','source_html':'wrong_review_vision_dominant.html',
               'source_count':len(results)+len(deleted),'imported_count':len(results),'branch_counts':dict(counts),
               'registered_geometry_count':len(registered_geometry),'pending_geometry_count':len(pending_geometry),
               'question_bank_count':len(catalog),
               'needs_review_count':len(issues),'verified_count':len(results)-len(issues),
               'needs_review_by_branch':dict(Counter(r['branch'] for r in issues)),
               'all_retained_source_answers_preserved':True,'deleted_questions':[d['id'] for d in deleted],
               'new_analytics_base_images':184,'new_analytics_special_pending':46,
               'existing_frozen_files_checked':len(unchanged),'existing_frozen_files_changed':changed,
               'old_base_pipeline_unchanged':True,'generated_at_utc':datetime.now(timezone.utc).isoformat(),
               'old_source_line_endings_restoration':'line_endings_restoration.json',
               'reviewers':['GPT-6-Luna x3','root independent comparison'],
               'python':platform.python_version()}
    write_json(IMPORT/'import_report.json',summary)
    lines = ['# MathVerse 重绘题核验疑点','',
             f'MathVerse source has {summary["source_count"]} questions; {len(results)} retained and {len(deleted)} deleted. {len(issues)} retained candidates have QA concerns.',
             '', '原图、重绘图、完整题干和逐题推导可在 [对照页](redraw_review.html) 查看。`needs_review` 不表示已经证明题目错误。','']
    for row in issues:
        av = row['answer_verification']
        lines += [f"## {row['id']}（{row['source_key']}）",'',
                  f"- 来源答案：{row['source_answer']}",
                  f"- 核验候选：{av.get('verified_answer') or '现有条件未能确定'}",
                  f"- 疑点：{av.get('issue_zh') or av.get('issue') or av.get('reasoning')}",
                  f"- 推导：{av['reasoning']}", '']
    (IMPORT/'issues.md').write_text('\n'.join(lines),encoding='utf-8')
    build_html(results,summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))


def build_html(rows, summary):
    cards = []
    branch_counts=Counter(row['branch'] for row in rows)
    for row in rows:
        av = row['answer_verification']
        escape = lambda v: html.escape(str(v if v is not None else '未确定'))
        badge = '需复核' if row['status']=='needs_review' else '核验一致'
        registration=row['registration_status']
        registration_text=('用户已通过 · 正式入库' if row['user_pass'] else
                           '图示已修改 · 等待重新审核' if registration=='needs_reapproval' else '等待用户逐题审核')
        source = '../../'+row['original_image']
        redraw = '../../'+row['image']
        cards.append(f'''<article id="{row['id']}" data-status="{row['status']}" data-branch="{row['branch']}" data-registration="{registration}">
<h2>{row['id']} <span>{row['source_key']} · {row['branch']}</span><b class="{row['status']}">{badge}</b></h2>
<p class="registration">{registration_text}</p>
<div class="pair"><figure><a href="{source}" target="_blank"><img loading="lazy" src="{source}" alt="{row['id']} 来源图"></a><figcaption>MathVerse 来源图</figcaption></figure>
<figure><a href="{redraw}" target="_blank"><img loading="lazy" src="{redraw}" alt="{row['id']} 重绘图"></a><figcaption>统一协议重绘图</figcaption></figure></div>
<p class="question">{escape(row['question'])}</p><div class="answers"><p>来源 GT：<strong>{escape(row['answer'])}</strong></p><p>核验候选：<strong>{escape(av.get('verified_answer'))}</strong></p></div>
{('<p class="issue">'+escape(av.get('issue_zh') or av.get('issue'))+'</p>') if av.get('issue') else ''}
<details><summary>查看推导及冻结文件</summary><p>{escape(av['reasoning'])}</p><a href="../../{row['verification']}">场景 / provenance</a> · <a href="../../{row['script']}">绘图脚本</a> · <a href="../../{row['report']}">核对报告</a></details></article>''')
    document = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MathVerse 重绘核验 · MathPalette</title>
<style>body{margin:0;background:#f4f5f7;color:#19212c;font:16px/1.6 system-ui,sans-serif}header{padding:28px max(20px,calc((100vw - 1100px)/2));background:white;border-bottom:1px solid #ddd}h1{margin:0;font-size:27px}header p{margin:8px 0}nav{position:sticky;top:0;background:#fff;padding:12px 20px;display:flex;flex-wrap:wrap;gap:12px;border-bottom:1px solid #ddd;z-index:3;align-items:center}nav select,nav input{font:inherit;padding:6px 10px;border:1px solid #bbb;border-radius:5px}main{max-width:1100px;margin:20px auto;padding:0 15px}article{background:#fff;border:1px solid #ddd;border-radius:8px;padding:20px;margin:20px 0}h2{font-size:21px;margin:0 0 12px;display:flex;gap:15px;align-items:center;flex-wrap:wrap}h2 span{font-size:14px;font-weight:400;color:#586575}h2 b{font-size:14px;padding:3px 9px;border-radius:5px;margin-left:auto}.needs_review{background:#fff1d5;color:#785012}.verified{background:#e6f3e9;color:#285a34}.pair{display:grid;grid-template-columns:1fr 1fr;gap:15px}figure{margin:0;background:#fff;border:1px solid #eee;text-align:center}figure img{width:100%;height:430px;object-fit:contain}figcaption{background:#f8f9fb;padding:5px}.question{white-space:pre-wrap}.answers{display:flex;flex-wrap:wrap;gap:20px;background:#f8f9fb;padding:0 12px;overflow-wrap:anywhere}.issue{background:#fff8e9;padding:12px;overflow-wrap:anywhere}details{margin-top:12px}summary{cursor:pointer}details p{white-space:pre-wrap}a{color:#285cb5}article[hidden]{display:none}#count{margin-left:auto}@media(max-width:700px){.pair{grid-template-columns:1fr}figure img{height:350px}}</style>
<header><h1>MathVerse redraw review</h1><p>{summary['source_count']} source questions: Analytics {branch_counts.get('Analytics',0)}, Plane Geometry {branch_counts.get('PlaneGeometry',0)}, Solid Geometry {branch_counts.get('SolidGeometry',0)}. Deleted questions are excluded from candidates.</p><p>QA candidates flag concerns and do not replace source answers. <a href="issues.md">Issue list</a> ? <a href="import_report.json">Import report</a></p></header>
<nav><label>范围 <select id="status"><option value="all">全部</option><option value="needs_review">仅需复核</option><option value="verified">核验一致</option></select></label><label>题型 <select id="branch"><option value="all">全部题型</option><option>Analytics</option><option>PlaneGeometry</option><option>SolidGeometry</option></select></label><label>入库 <select id="registration"><option value="all">全部</option><option value="registered">已正式入库</option><option value="pending_user_review">待用户审核</option><option value="needs_reapproval">待重新审核</option></select></label><input id="search" placeholder="搜索题号、来源编号或文字" aria-label="搜索"><span id="count"></span></nav><main>'''+''.join(cards)+'''</main>
<script>const cards=[...document.querySelectorAll('article')];function filter(){const status=document.querySelector('#status').value,branch=document.querySelector('#branch').value,registration=document.querySelector('#registration').value,q=document.querySelector('#search').value.trim().toLowerCase();let n=0;cards.forEach(c=>{const visible=(status==='all'||c.dataset.status===status)&&(branch==='all'||c.dataset.branch===branch)&&(registration==='all'||c.dataset.registration===registration)&&(!q||c.textContent.toLowerCase().includes(q));c.hidden=!visible;if(visible)n++});document.querySelector('#count').textContent=`显示 ${n} / ${cards.length} 题`};for(const id of ['status','branch','registration','search'])document.querySelector('#'+id).addEventListener('input',filter);filter();</script></html>'''
    (IMPORT/'redraw_review.html').write_text(document,encoding='utf-8')


if __name__=='__main__':
    main()
