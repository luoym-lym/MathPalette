"""Package only independently recommended candidates; never writes the library."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import shutil
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path,data):
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def data_uri(path):
    return 'data:image/png;base64,'+base64.b64encode(Path(path).read_bytes()).decode('ascii')

def verify_evidence(source):
    design=read(source/'design.json')
    expected=design.get('expected_wrong_answer',design.get('predicted_wrong_answer'))
    candidates=[]
    for path in (source/'tests').glob('*/summary.json'):
        data=read(path)
        if data.get('two_completed') and str(data['expected_wrong_answer'])==str(expected):
            candidates.append((path,data))
    if len(candidates)!=1:
        raise ValueError('Expected exactly one frozen complete pair: '+str(source))
    summary_path,summary=candidates[0]
    evidence=summary_path.parent
    image_hash=sha(source/'candidate.png')
    if summary['image_sha256']!=image_hash:
        raise ValueError('Tested candidate PNG differs')
    if summary['design_sha256']!=sha(evidence/'design_snapshot.json'):
        raise ValueError('Frozen design differs')
    frozen_design=read(evidence/'design_snapshot.json')
    if str(frozen_design.get('expected_wrong_answer',frozen_design.get('predicted_wrong_answer')))!=str(expected):
        raise ValueError('Prediction changed')
    request=read(evidence/'request.json')
    user=request['messages'][1]['content']
    if [item['type'] for item in user]!=['text','image_url']:
        raise ValueError('Unexpected solver input')
    encoded=user[1]['image_url']['url'].split(',',1)[1]
    if hashlib.sha256(base64.b64decode(encoded)).hexdigest()!=image_hash:
        raise ValueError('Request image differs')
    branch=summary['branch']
    records=[json.loads(s) for s in (ROOT/branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    record=next(r for r in records if r['id']==summary['question_id'])
    if user[0]['text']!=record['question']:
        raise ValueError('Solver question differs from formal question')
    for index,result in enumerate(summary['results'],1):
        if result.get('status')!='completed' or result.get('truncated') or result.get('http_status')!=200:
            raise ValueError('Incomplete or truncated solver response')
        if result['response_sha256']!=sha(evidence/f'run_{index:02d}_response.json'):
            raise ValueError('Raw response differs')
        if result['image_sha256']!=image_hash or result['design_sha256']!=summary['design_sha256']:
            raise ValueError('Run binding differs')
    return summary,record,summary_path

def build(selection_path, batch_name):
    selection=read(selection_path)
    destination=HERE/batch_name
    if destination.exists():
        raise ValueError('Batch is immutable; choose a new name')
    staged=[]
    for item in selection:
        source=(HERE/item['candidate']).resolve()
        review=(HERE/item['independent_review']).resolve()
        if not source.is_relative_to(HERE) or not review.is_relative_to(HERE):
            raise ValueError('Unsafe candidate/review path')
        report=read(review)
        decision=report.get('decision',report.get('verdict',report.get('status')))
        if decision!='recommended':
            raise ValueError('Independent review does not recommend '+str(source))
        for supplement in item.get('supplemental_evidence',[]):
            additional=(HERE/supplement['source']).resolve()
            relative=Path(supplement['destination'])
            if not additional.is_relative_to(HERE) or not additional.is_dir():
                raise ValueError('Unsafe or missing supplemental evidence')
            if relative.is_absolute() or '..' in relative.parts:
                raise ValueError('Unsafe supplemental destination')
        summary,record,evidence=verify_evidence(source)
        staged.append((item,source,review,report,summary,record,evidence))
    destination.mkdir()
    cards=[]
    entries=[]
    for item,source,review,report,summary,record,evidence in staged:
        qid=record['id']
        target=destination/qid
        shutil.copytree(source,target)
        shutil.copyfile(review,target/'independent_review.json')
        shutil.copyfile(ROOT/summary['branch']/record['image'],target/'original.png')
        shutil.copyfile(ROOT/summary['branch']/record['scene'],target/'frozen_scene_reference.json')
        supplemental=[]
        for supplement in item.get('supplemental_evidence',[]):
            additional=(HERE/supplement['source']).resolve()
            copied=(target/supplement['destination']).resolve()
            if not copied.is_relative_to(target.resolve()):
                raise ValueError('Supplemental evidence would escape candidate folder')
            shutil.copytree(additional,copied)
            hashes={str(p.relative_to(additional)).replace('\\','/'):sha(p) for p in additional.rglob('*') if p.is_file()}
            if any(sha(copied/relative)!=expected for relative,expected in hashes.items()):
                raise ValueError('Supplemental evidence copy changed bytes')
            supplemental.append({'original_source':supplement['source'],'packaged_path':qid+'/'+supplement['destination'],'files_sha256':hashes})
        dependencies={record['scene'],record['script'],record['image'],*record.get('runtime_dependencies',[])}
        if record.get('original_image'):
            dependencies.add(record['original_image'])
        inputs={str((ROOT/summary['branch']/name).relative_to(ROOT)).replace('\\','/'):sha(ROOT/summary['branch']/name) for name in dependencies}
        for name in ['dataset_tools/mathvision_workbench.py',summary['branch']+'/workbench/plugin.schema.json',summary['branch']+'/workbench/render_plugins.py',summary['branch']+'/workbench/renderer_adapter.py']:
            inputs[name]=sha(ROOT/name)
        entry={'question_id':qid,'branch':summary['branch'],'source_dataset':'MathVision','correct_answer':record['answer'],'expected_wrong_answer':summary['expected_wrong_answer'],'tested_final_answers':item['final_answers'],'original_control_answers':item.get('control_answers',[]),'mechanism':item['mechanism'],'quality_review':'recommended','user_approval_status':'UNREVIEWED; no Pass/Collect','candidate_source':str(source.relative_to(HERE)).replace('\\','/'),'evidence_path':str(evidence.relative_to(source)).replace('\\','/'),'candidate_sha256':summary['image_sha256'],'plugin_sha256':sha(target/'plugin.json'),'question':record['question'],'input_files':inputs,'record_sha256':summary['question_record_sha256']}
        if supplemental:
            entry['supplemental_evidence']=supplemental
        entries.append(entry)
        choices=html.escape(str(record['answer']))
        wrong=html.escape(str(summary['expected_wrong_answer']))
        answers=' / '.join(html.escape(str(x)) for x in item['final_answers'])
        controls=' / '.join(html.escape(str(x)) for x in item.get('control_answers',[])) or '未测'
        original=data_uri(target/'original.png'); variant=data_uri(target/'candidate.png')
        responses=''.join('<details><summary>Quick Test 3 · 第'+str(i)+'次完整回答</summary><pre>'+html.escape(r['answer'])+'</pre></details>' for i,r in enumerate(summary['results'],1))
        cards.append(f'''<article><div class="row"><strong>{qid}</strong><span class="badge">双测命中 · 独立复核推荐</span></div><p>{html.escape(item['mechanism'])}</p><div class="facts"><span>正确：<b>{choices}</b></span><span>预设错答：<b>{wrong}</b></span><span>两次回答：<b>{answers}</b></span><span>原图对照：{controls}</span></div><p class="muted">{html.escape(item.get('limitation',''))}</p><div class="switches"><button onclick="swap(this,'variant')" class="selected">变体</button><button onclick="swap(this,'original')">原图</button></div><img class="drawing" src="{variant}" data-variant="{variant}" data-original="{original}" alt="{qid} 原图和变体切换"><details><summary>正式题干</summary><pre>{html.escape(record['question'])}</pre></details>{responses}<details><summary>独立复核记录</summary><pre>{html.escape(json.dumps(report,ensure_ascii=False,indent=2))}</pre></details><p class="muted">文件：{qid}/candidate.png · plugin.json · tests/ · independent_review.json</p></article>''')
    dump(destination/'manifest.json',{'batch':batch_name,'created_at':datetime.now(timezone.utc).isoformat(),'approval_status':'All candidates remain user-unreviewed; no formal files changed','candidates':entries})
    markup='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>MathVision Special 审阅</title><style>:root{font-family:var(--font-sans,system-ui);color:var(--foreground,#202938)}body{margin:0}p{line-height:1.6}article{background:var(--card,#f7f8fa);border:1px solid var(--border,#d7dce3);border-radius:var(--radius,12px);padding:16px;margin:0 0 16px}.row{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.row strong{font-size:22px}.badge{font-size:12px;color:var(--success,#187e50)}.facts{display:flex;gap:12px;flex-wrap:wrap;font-size:14px}.muted{font-size:13px;color:var(--muted-foreground,#6b7280)}.switches{display:flex;gap:8px;margin-top:12px}button{font:inherit;padding:6px 16px;border-radius:8px;border:1px solid var(--border,#c8ced7);background:var(--secondary,#eceff3);color:var(--foreground,#202938);cursor:pointer}button.selected{background:var(--primary,#354f9e);color:var(--primary-foreground,white)}.drawing{display:block;width:100%;max-width:768px;margin:12px auto;background:white;border-radius:8px}details{border-top:1px solid var(--border,#d7dce3);padding:10px 0}summary{cursor:pointer;font-size:14px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-family:var(--font-mono,monospace);font-size:13px;line-height:1.55}footer{font-size:12px;color:var(--muted-foreground,#6b7280);line-height:1.7}</style></head><body>'''+''.join(cards)+'''<footer>所有变体均待用户审核。模型测试与独立复核均不代表用户 Pass / Collect。仅发送正式题干与候选 PNG；预设错误答案在两次测试前冻结。两次命中仅表示这两次记录，不推断总体成功率。</footer><script>function swap(b,key){const a=b.closest('article');a.querySelector('.drawing').src=a.querySelector('.drawing').dataset[key];a.querySelectorAll('button').forEach(x=>x.classList.remove('selected'));b.classList.add('selected')}</script></body></html>'''
    (destination/'review.html').write_text(markup,encoding='utf-8')
    shutil.copyfile(HERE/'replay_candidate.py',destination/'replay_candidate.py')
    shutil.copyfile(HERE/'runtime_isolation.py',destination/'runtime_isolation.py')
    shutil.copyfile(HERE/'delivery_bridge_adapter.py',destination/'delivery_bridge_adapter.py')
    archive=HERE/(batch_name+'.zip')
    with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED) as bundle:
        for path in destination.rglob('*'):
            if path.is_file():
                bundle.write(path,str(path.relative_to(HERE)))
    print(json.dumps({'batch':str(destination),'review':str(destination/'review.html'),'zip':str(archive),'candidates':[e['question_id'] for e in entries]},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--selection',required=True);p.add_argument('--batch',required=True)
    a=p.parse_args();build(a.selection,a.batch)
