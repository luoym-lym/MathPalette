from tools34 import *
from make34 import SPECS
for qid in sys.argv[1:]:
    folder=UNIT/qid/SPECS[qid]['variant_id']
    for path in sorted(folder.glob('tests/*/run_*_response.json')):
        data=read(path)
        print(json.dumps({'question_id':qid,'raw_response':str(path),'sha256':sha(path),'finish_reason':data['choices'][0]['finish_reason'],'model':data['model']},ensure_ascii=False))
        print(data['choices'][0]['message']['content'])
