from tools_local import *
d=json.loads((BASE/'exploration_report.json').read_text(encoding='utf-8-sig'))
for row in d['attempts']:
    if row['question_id'] in ['Plane282','Plane293']:print(json.dumps(row,ensure_ascii=False,indent=2))
