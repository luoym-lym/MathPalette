from bootstrap import *
import hashlib,json,runpy
qid='Solid234';source=HERE/qid/'r57_maximum_generator_to_cut_trace'
gate=json.loads((HERE/'prelaunch_gate.json').read_text(encoding='utf-8-sig'))
assert gate['all_gates_passed'] and gate['actual_prior_API_calls']==0
assert hashlib.sha256((source/'candidate.png').read_bytes()).hexdigest()==gate['image_sha256']
assert hashlib.sha256((source/'design.json').read_bytes()).hexdigest()==gate['design_sha256']
assert not list(source.rglob('*_started.json')) and not list(source.rglob('summary.json'))
script=HERE/'harness'/'quicktest3_isolated.py'
sys.argv=[str(script),'--branch','SolidGeometry','--question',qid,'--image',str(source/'candidate.png'),'--design',str(source/'design.json'),'--output',str(source/'tests'),'--runs','2']
runpy.run_path(str(script),run_name='__main__')
