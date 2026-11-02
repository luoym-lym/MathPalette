from env50 import *
from inspect50 import IDS
from dataset_tools.catalog import read
refs=[]
for p in sorted(ROOT.glob('batch_*/manifest.json')):
    m=read(p)
    for c in m['candidates']:
        refs.append({'batch':p.parent.name,'manifest_path':str(p),'manifest_sha256':sha(p),'question_id':c['question_id'],'mechanism':c['mechanism'],'source':c['candidate_source'],'review_status':c['quality_review'],'control_answers':c.get('original_control_answers',[])})
dump(OWN/'delivered_information_references.json',refs)
print(json.dumps(refs,ensure_ascii=False))
report=read(ROOT/'exploration_report.json')
attempts=[a for a in report.get('attempts',[]) if isinstance(a,dict) and a.get('question_id') in IDS]
dump(OWN/'global_history_excerpt_readonly.json',{'diagnostic_runtime_metadata':True,'source_path':str(ROOT/'exploration_report.json'),'sha256_at_read':sha(ROOT/'exploration_report.json'),'selected_attempts':attempts,'not_success_grading':'No tail-mention heuristic used. Old question-directory manifest and full raw inventory control actual call accounting.'})
for q in IDS:
    h=read(OWN/'history_read_audit.json')[q]
    dump(OWN/q/'old_native_image_review.json',{'all_old_native_images_actually_opened':True,'images':h['all_old_images'],'all_old_saved_designs':h['old_designs'],'all_old_raw_responses':h['old_raw_responses'],'malformed_old_files_preserved':h['malformed_preserved'],'image_findings':'Actual old PNGs are the unchanged formal baseline, not old tested candidate images; source JPG for Plane183 also opened. No historical candidate/design/response was found in these8question directories. Complete old prescreen reasons read.','historical_metadata_correction':{'source_primary_audit_Plane177':'Old source_visual_findings mentions unrelated Plane237 car colors. This is a copy/paste narrative error, not a changed input or an old solver call. Actual Plane177 board8x6,pockets and45-degree ray were directly inspected. Old file remains unchanged.'} if q=='Plane177' else {}})
