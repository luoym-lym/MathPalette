from bootstrap import install,OWN
install()
from research import load,save,sha
import sys,json
qid=sys.argv[1]
folder=next((OWN/qid).glob('r52_*'))
for summary in (folder/'tests').glob('*/summary.json'):
    s=load(summary)
    print(json.dumps({'summary':str(summary),'binding':{k:s[k] for k in ['question_id','expected_wrong_answer','question','image_path','image_sha256','design_path','design_sha256','request_body_sha256','two_completed']}}))
    for p in sorted(summary.parent.glob('run_*_response.json')):
        raw=load(p)
        print(json.dumps({'path':str(p),'sha256':sha(p),'full_raw_response':raw},ensure_ascii=False))
