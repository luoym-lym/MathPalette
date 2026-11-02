"""Finalize two runtime-only research deliveries and the finite 24-question outcome."""
import base64
from datetime import datetime, timezone
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
now=datetime.now(timezone.utc).isoformat()
read=lambda f:json.loads(Path(f).read_text(encoding='utf-8-sig'))
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()

def dump(path,value):
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def uri(path):
    return 'data:image/png;base64,'+base64.b64encode(Path(path).read_bytes()).decode('ascii')

class Images(HTMLParser):
    def __init__(self):
        super().__init__();self.images=[]
    def handle_starttag(self,tag,attrs):
        if tag=='img':self.images.append(dict(attrs))

review_path=HERE/'independent_review/Plane321_a01_pivot_legs_vs_true_bases_r1/independent_review.json'
review=read(review_path)
batch=HERE/'batch_02';archive=HERE/'batch_02.zip';verification=HERE/'batch_02_verification'
integrity=read(verification/'archive_integrity.json')
assert sha(archive)==integrity['archive_sha256']
assert sha(batch/'Plane321/candidate.png')==sha(verification/'reproduced/Plane321.png')==review['candidate_png_sha256']
assert sha(batch/'Plane321/independent_review.json')==sha(review_path)
markup=(batch/'review.html').read_text(encoding='utf-8');parser=Images();parser.feed(markup)
assert len(parser.images)==1
for attribute,name in [('src','candidate.png'),('data-variant','candidate.png'),('data-original','original.png')]:
    assert hashlib.sha256(base64.b64decode(parser.images[0][attribute].split(',',1)[1])).hexdigest()==sha(batch/'Plane321'/name)
assert '变体' in markup and '贴近模仿' in markup
source_manifest=read(HERE/'readonly_source_sha256.json')
changes=[name for name,expected in source_manifest.items() if sha(ROOT/name)!=expected]
assert changes==[],changes
dump(verification/'final_delivery_verification.json',{
    'checked_at_utc':now,'candidate_sha256':review['candidate_png_sha256'],
    'replay_from_fresh_unpacked_archive_bytes_equal':True,'archive_sha256':sha(archive),
    'archive_members':integrity['archive_members'],'archive_CRC_and_exact_members_checked':True,
    'HTML_embedded_candidate_and_original_bytes_checked':True,
    'protected_source_checks':len(source_manifest),'protected_source_differences':[],
    'packaged_report_sha256':sha(review_path),'solver_calls':0,'foreground_replay_exit_code':0,
    'background_processes_started':0,'formal_edits':0,'Pass_Collect_actions':0,
    'imitation_fidelity':'close imitation',
})
prepared=read(HERE/'delivery_batch_02_prepared.json')
prepared.update({'status':'READY_FOR_RESEARCH_DELIVERY_NO_PASS_COLLECT','verified_at_utc':now,
                 'verification':'batch_02_verification/final_delivery_verification.json'})
dump(HERE/'delivery_batch_02_prepared.json',prepared)
outcomes=read(HERE/'independent_review_outcomes.json')
outcomes['updated_at_utc']=now
outcomes['reviews']['Plane321']={
    'question_id':'Plane321','variant_id':review['variant_id'],'decision':'recommended',
    'completed_and_consumed':True,'report':str(review_path.relative_to(HERE)).replace('\\','/'),
    'report_sha256':sha(review_path),'method_fidelity':'close imitation',
    'original_unique_answer':'E = 300°','observed_two_complete_finals':['B = 120°','B = 120°'],
    'eligible_for_delivery':True,'delivery_batch':'batch_02','replacement_or_new_test_scheduled':False,
}
dump(HERE/'independent_review_outcomes.json',outcomes)
progress=read(HERE/'latest_progress.json')
progress.update({'updated_at_utc':now,'known_pending_independent_reviews':[],
 'independent_review_dispatch_status':'All three NEW independent reviews consumed: two recommended, one rejected',
 'completed_independent_review_decisions':{'Plane461':'reject','Solid166':'recommended','Plane321':'recommended'},
 'qualified_delivered_this_task':2,'unqualified_for_delivery_count':22,
 'new_research_tasks_scheduled':0,'exploration_after_latest_user_steering':'No further exploration or solver calls; finite delivery complete',
 'delivery_index':'delivery_index.html'})
progress['delivery_batches']=[{'batch':'batch_02','questions':['Plane321'],'imitation_fidelity':'close imitation','zip':'batch_02.zip','PNG':'batch_02/Plane321/candidate.png'},
                            {'batch':'batch_01','questions':['Solid166'],'imitation_fidelity':'extension','zip':'batch_01.zip','PNG':'batch_01/Solid166/candidate.png'}]
dump(HERE/'latest_progress.json',progress)
unit_outcomes=read(HERE/'unit_outcomes.json')
unit_outcomes['updated_at_utc']=now
for row in unit_outcomes['question_outcomes']:
    if row['question_id']=='Plane321':
        row.update({'status':'INDEPENDENT_SECOND_REVIEW_RECOMMENDED_PACKAGED_RUNTIME_ONLY',
                    'qualified_delivered':True,'imitation_fidelity':'close imitation',
                    'independent_review':str(review_path.relative_to(HERE)).replace('\\','/'),'delivery_batch':'batch_02'})
assert sum(row['qualified_delivered'] for row in unit_outcomes['question_outcomes'])==2
unit_outcomes['units']['u04_angles']['status']='COMPLETED_ONE_QUALIFIED_OTHER_UNQUALIFIED'
unit_outcomes['units']['u04_angles']['independent_review_decisions']={'Plane321':'recommended'}
unit_outcomes['qualification_note']='Three PRIMARY candidates independently reviewed: Plane321 close imitation recommended; Solid166 extension recommended; Plane461 rejected. Exactly two runtime research deliveries; other22 have no qualified delivery. No further exploration. The already-requested u11 cancellation terminal reconciliation remains separately recorded, not a pending independent review.'
dump(HERE/'unit_outcomes.json',unit_outcomes)

entries=[];cards=[]
for qid,batch_name,reference,correct,wrong,fidelity,description in [
    ('Plane321','batch_02','Plane427','E = 300°','B = 120°','贴近模仿','沿用原边的两类角色配色：绕 A 的三条边为蓝色，两条对应对边为红色。仅修改原有五条边的颜色和线宽；与参考图交换了两类颜色。'),
    ('Solid166','batch_01','Solid203','5','4','扩展模仿','红色比较 x 与边 4，另三组颜色追踪真实接缝。共八条原边、四组颜色，比用户原例更丰富；没有新增点、线或切分。'),
]:
    directory=HERE/batch_name/qid
    assert sha(HERE/(batch_name+'.zip'))==read(HERE/(batch_name+'_verification/final_delivery_verification.json'))['archive_sha256']
    entry={'question_id':qid,'reference':reference,'correct_answer':correct,'frozen_wrong_preset':wrong,
           'two_complete_finals':[wrong,wrong],'method_fidelity':fidelity,'description':description,
           'candidate_PNG':batch_name+'/'+qid+'/candidate.png','plugin':batch_name+'/'+qid+'/plugin.json',
           'zip':batch_name+'.zip','review_page':batch_name+'/review.html',
           'independent_review':batch_name+'/'+qid+'/independent_review.json',
           'candidate_sha256':sha(directory/'candidate.png'),'zip_sha256':sha(HERE/(batch_name+'.zip')),
           'user_approval_Pass_Collect':False}
    entries.append(entry)
    cards.append(f'''<article><h2>{qid} <span>{fidelity}</span></h2><p>{html.escape(description)}</p>
<p class="facts">正确：<strong>{html.escape(correct)}</strong>　预设错误：<strong>{html.escape(wrong)}</strong>　两次完整终答：<strong>{html.escape(wrong)} / {html.escape(wrong)}</strong></p>
<div class="images"><figure><figcaption>你的当前标注参考 · {reference}</figcaption><img src="{uri(HERE/'references'/reference/'C01.png')}" alt="用户当前{reference}标注"></figure>
<figure><figcaption>本轮变体 · {qid}</figcaption><img src="{uri(directory/'candidate.png')}" alt="{qid}已双测并二审的冻结变体"></figure></div>
<p><a href="{entry['zip']}">完整交付包</a> · <a href="{entry['candidate_PNG']}">PNG</a> · <a href="{entry['plugin']}">插件 JSON</a> · <a href="{entry['review_page']}">原图对照与完整响应</a> · <a href="{entry['independent_review']}">独立二审报告</a></p></article>''')
document='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MathVision 本轮模仿设计 · 2份</title><style>body{font-family:system-ui,sans-serif;max-width:1180px;margin:24px auto;padding:0 18px;color:#202938;background:#fff}h1{font-size:26px}p{line-height:1.65}article{border:1px solid #d6dde4;border-radius:12px;padding:18px;margin:22px 0}h2{margin:0 0 12px}h2 span{font-size:14px;font-weight:normal;margin-left:12px;color:#526071}.images{display:grid;grid-template-columns:1fr 1fr;gap:14px}figure{margin:0}figcaption{font-size:14px;margin:6px 0}img{display:block;width:100%;height:auto}.facts{background:#f4f7fa;padding:10px;border-radius:6px}a{color:#155cb0}footer{font-size:13px;color:#526071}@media(max-width:700px){.images{grid-template-columns:1fr}}</style></head><body><h1>MathVision 本轮模仿设计 · 2份</h1><p>24道目标题中，2份满足“两次完整终答均命中事前冻结错误答案＋新独立二审推荐”的研究交付门槛。其余22题没有合格交付；其中 Plane461 虽双中，但因信息对应与模仿程度不足被二审淘汰。本轮不再追加探索。</p>'''+''.join(cards)+'''<footer><p>两次命中仅代表这两条记录，不证明总体成功率、具体内部机制、因果增益或每条标记的必要性。Solid166 源 JPG 的统一灰底在当前正式 PNG 中已缺失，变体没有改变填充，此差异已记入独立报告。所有内容仍仅在 runtime；没有用户审批、Pass、Collect 或正式库改动。</p><p><a href="unit_outcomes.json">24题状态</a> · <a href="independent_review_outcomes.json">3份候选二审结论</a> · <a href="qualified_delivery_index.json">交付索引与哈希</a></p></footer></body></html>'''
(HERE/'delivery_index.html').write_text(document,encoding='utf-8')
index={'created_at_utc':now,'scope_count':24,'qualified_count':2,'not_qualified_count':22,
       'qualification':'Two complete predeclared-preset hits on identical PNG and NEW independent second-review recommendation',
       'candidates':entries,'extra_exploration':False,'formal_edits':0,'Pass_Collect_actions':0,
       'scope_limit':'Known consumed evidence only. Prior u11 cancellation reconciliation is preserved separately; no claim of absent unrecorded activity.'}
dump(HERE/'qualified_delivery_index.json',index)
parser=Images();parser.feed(document)
assert len(parser.images)==4
expected=[HERE/'references/Plane427/C01.png',HERE/'batch_02/Plane321/candidate.png',HERE/'references/Solid203/C01.png',HERE/'batch_01/Solid166/candidate.png']
for img,path in zip(parser.images,expected):
    assert hashlib.sha256(base64.b64decode(img['src'].split(',',1)[1])).hexdigest()==sha(path)
dump(HERE/'delivery_index_verification.json',{'checked_at_utc':now,'embedded_image_count':4,'embedded_reference_candidate_bytes_exact':True,'index_sha256':sha(HERE/'delivery_index.html'),'qualified_delivery_count':2,'new_solver_calls':0,'protected_sources_unchanged':len(source_manifest)})
with (HERE/'continuation.txt').open('a',encoding='utf-8') as stream:
    stream.write('\n'+now+' Consumed NEW Plane321 independent review after reading completed thread: recommended close imitation, E300 unique, frozen B120/B120. Packaged batch_02.zip and fresh offline exact replay from unpacked ZIP passed. Two research deliveries total: Plane321 and Solid166; Plane461 reject; 22/24 without qualified delivery. delivery_index.html shows actual current reference beside exact candidate. All376 protected inputs unchanged, no new solver calls or formal writes/Pass/Collect. All three independent reviews completed; no extra exploration. Prior u11 cancellation reconciliation remains separately noted, not polled.\n')
print(json.dumps({'qualified':2,'not_qualified':22,'new_delivery':'Plane321','index':str(HERE/'delivery_index.html'),
                  'Plane321_zip':str(archive),'zip_MiB':round(archive.stat().st_size/1048576,2),
                  'extra_solver_calls':0,'protected_sources_unchanged':len(source_manifest)},ensure_ascii=False))
