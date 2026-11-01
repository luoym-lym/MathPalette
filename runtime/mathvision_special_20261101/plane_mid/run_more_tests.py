import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE.parent/'harness'))
from quicktest3_isolated import run_tests
records=json.loads((HERE/'more_designs.json').read_text(encoding='utf-8'))
for r in records:
    print('START',r['question_id'],r['variant_id'],flush=True)
    result=run_tests('PlaneGeometry',r['question_id'],r['image_path'],Path(r['image_path']).with_name('design.json'),Path(r['image_path']).parent/'tests',2)
    print('ANSWER_TAIL',r['question_id'],json.dumps([x.get('answer','')[-260:] for x in result['results']],ensure_ascii=False),flush=True)
    if not all(x['status']=='completed' for x in result['results']):
        print('API_ERROR_STOP',flush=True)
        break
