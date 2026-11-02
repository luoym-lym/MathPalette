"""Run the path-localized original harness. Audit hook adds read-only eligibility
checks immediately before each urllib network opening; it never changes payload.
"""
from worker_env import *
import runpy
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('question',choices=['Solid186','Solid226'])
parser.add_argument('variant',nargs='?')
args=parser.parse_args()
qid=args.question
variant={'Solid186':'r05_three_patch_changed_area_binding','Solid226':'r05_removed_roof_to_new_cut_faces'}[qid]
if args.variant:
    allowed={'Solid186':['r05_face_scale_comparison'],'Solid226':['r05_front_plane_loss']}
    assert args.variant in allowed[qid]
    variant=args.variant
folder=OWN/qid/variant
assert not list((folder/'tests').glob('*/run_*_started.json')),'No retry/recovery of previous started requests'
for f in ('fresh_process_replay.json','primary_review_before_calls.json'):
    assert (folder/f).is_file()
design=load(folder/'design.json')
hpath=OWN/'harness/quicktest3_isolated.py'
assert sha(hpath)==load(OWN/'harness/localization_audit.json')['localized_sha256']
count=0
def before_network(event, eventargs):
    global count
    if event!='urllib.Request': return
    count+=1
    assert count<=2
    url,data=eventargs[:2]
    assert url.endswith('/chat/completions')
    current=eligibility(qid)
    assert current['eligible'],current['checks']
    assert sha(folder/'candidate.png')==design['image_sha256']
    assert sha(folder/'plugin.json')==design['plugin_sha256']
    assert sha(folder/'design.json')==load(folder/'render_gates.json')['design_sha256']
    for p,h in load(folder/'input_manifest.json')['source_manifest'].items(): assert sha(PROJECT/p)==h
    payload=json.loads(data)
    assert payload['messages'][1]['content'][0]['text']==current['record']['question']
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    save(folder/f'eligibility_immediately_before_call_{count:02d}.json',current,True)
    save(folder/f'network_guard_{count:02d}.json',{'at':now(),'pid':os.getpid(),'call_index':count,
      'request_body_sha256':hashlib.sha256(data).hexdigest(),'unmodified_original_payload':True,
      'current_eligibility_pass':True,'source_hashes_unchanged':True},True)
    cp=load(OWN/'checkpoint.json')
    cp.update(at=now(),status='original_quicktest3_running',calls_started=len(list(OWN.glob('Solid*/r05_*/tests/*/run_*_started.json'))))
    cp['questions'][qid]={'status':'testing','variant':variant,'current_call':count}
    save(OWN/'checkpoint.json',cp)
sys.addaudithook(before_network)
save(folder/'process_launch.json',{'at':now(),'pid':os.getpid(),'command':sys.argv,'python':sys.executable,
    'harness':str(hpath),'harness_sha256':sha(hpath),'runs':2,'no_automatic_retry':True},True)
sys.argv=[str(hpath),'--branch','SolidGeometry','--question',qid,'--image',str(folder/'candidate.png'),
          '--design',str(folder/'design.json'),'--output',str(folder/'tests'),'--runs','2']
returned=False
try:
    runpy.run_path(str(hpath),run_name='__main__')
    returned=True
finally:
    save(folder/'process_completed.json',{'at':now(),'pid':os.getpid(),'observed_urllib_openings':count,
         'harness_main_returned':returned,'no_background_API_process_created':True},True)
