import json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
FINALS={
 ('Plane166','v01'):['B','C'],
 ('Plane171','v01'):['A','B'],
 ('Plane175','v01'):['B','C'],('Plane175','v02'):['D','A'],('Plane175','v03'):['C','none_of_the_choices'],
 ('Plane175','v04'):['A','C'],('Plane175','v05'):['B','B'],('Plane175','v06'):['A','B'],
 ('Plane179','v01'):['4'],('Plane189','v01'):['B','E'],
 ('Plane192','v01'):['A','D'],('Plane192','v02'):['D','A'],('Plane192','v03'):['A','A'],
 ('Plane196','v01'):['B','B'],
 ('Plane236','v01'):['D','D'],('Plane236','v02'):['E','D'],('Plane236','v03'):['E','E'],('Plane236','v04'):['D','E'],
 ('Plane253','v01'):['B','B'],('Plane261','v01'):['C','C'],
 ('Plane421','v01'):['0','C'],('Plane421','v02'):['1/5','C'],('Plane444','v01'):['E','E'],
 ('Plane452','v01'):['E','D'],('Plane458','v01'):['B','D'],
 ('Plane459','v01'):['5','6'],('Plane459','v02'):['6','3'],('Plane462','v01'):['E','E'],
 ('Plane463','v01'):['18','24'],('Plane472','v01'):['B','B'],
 ('Plane478','v01'):['6','7'],('Plane478','v02'):['4','4'],('Plane478','v03'):['13','24'],
 ('Plane483','v01'):['8','6.5'],('Plane488','v01'):['45.625','32'],('Plane434','v01'):['B','B'],
 ('Plane434','v02'):['27','B'],('Plane440','v01'):['D','D_with_inconsistent_expression'],
}
records=[]
for design_path in sorted(HERE.glob('Plane*/v*/design.json')):
    design=json.loads(design_path.read_text(encoding='utf8'))
    qid,vid=design['question_id'],design['variant_id']
    summaries=list(design_path.parent.glob('tests/*/summary.json'))
    answers=FINALS.get((qid,vid),[])
    record={**design,'manually_read_final_answers':answers,
            'evidence_summaries':[str(p) for p in summaries],
            'current_design_file_sha256':hashlib.sha256(design_path.read_bytes()).hexdigest(),
            'two_predeclared_hits':len(answers)==2 and all(a==design['predicted_wrong_answer'] for a in answers),
            'user_pass':False,'user_collect':False,'strict_quality_status':'not_qualified_by_two_tests'}
    if record['two_predeclared_hits']:
        record['strict_quality_status']='pending_independent_review'
    if qid=='Plane192' and vid=='v03':
        record['original_control_final_answers']=['A','A']
        record['strict_quality_status']='not_recommended_original_same_wrong_answer_and_option_highlight_only'
    if qid=='Plane179':
        record['run_2_transport_failure']=True
    if not answers:
        record['strict_quality_status']='not_tested_draft'
    if qid=='Plane440':
        record['answer_note']='Run 1 derived sqrt(2)+1/2 (choice D); run 2 chose D but its final numeric expression contradicts that letter. Neither matched preset B.'
    records.append(record)
(HERE/'analysis_results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
summary={'variant_count':len(records),'fully_manually_read_tests':sum(len(r['manually_read_final_answers'])==2 for r in records),
         'two_predeclared_hit_candidates':[r['question_id']+'/'+r['variant_id'] for r in records if r['two_predeclared_hits']],
         'strictly_recommended_variants':[],
         'note':'All candidates are unapproved. New designs require two matching predeclared answers, unchanged evidence hashes, and independent strict-quality review.'}
(HERE/'exploration_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=False))
