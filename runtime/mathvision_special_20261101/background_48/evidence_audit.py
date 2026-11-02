import task_env
from task_env import OWN,PROJECT
from prepare import read,write,hashfile,eligibility
from workbench_io import pixel_hash,canonical_hash
from quick_test import SYSTEM_PROMPT,TEST_PROFILES
from datetime import datetime,timezone
import json,hashlib,base64
from pathlib import Path

def sha(b):return hashlib.sha256(b).hexdigest()
def audit(d):
    design=read(d/'design.json');q=design['question_id'];tests=list((d/'tests').glob('quicktest3_*'))
    assert len(tests)==1
    t=tests[0];binding=read(t/'binding.json');rawreq=(t/'request.json').read_bytes();req=json.loads(rawreq);snap=(t/'design_snapshot.json').read_bytes();img=(d/'candidate.png').read_bytes()
    formal=eligibility(q);r=formal['formal_record']
    expected={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':[{'type':'text','text':r['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(img).decode('ascii')}}]}]}
    checks={'exact_request_only_formal_question_and_candidate_PNG':req==expected,'same_design_snapshot_bytes':snap==(d/'design.json').read_bytes(),'request_body_hash':sha(rawreq)==binding['request_body_sha256'],'image_hash':sha(img)==binding['image_sha256']==design['png_sha256'],'pixel_hash':pixel_hash(img)==binding['pixel_sha256']==design['pixel_sha256'],'design_hash':sha(snap)==binding['design_sha256'],'current_formal_record_hash':canonical_hash(r)==binding['question_record_sha256'],'preset_unchanged_and_wrong':binding['expected_wrong_answer']==design['expected_wrong_answer'] and str(design['expected_wrong_answer'])!=str(r['answer']),'reference_quick_test_unchanged':hashfile(PROJECT/'PlaneGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256'],'exactly_two_starts':len(list(t.glob('run_*_started.json')))==2,'exactly_two_raw_responses':len(list(t.glob('run_*_response.json')))==2,'requested_runs_two':binding['requested_runs']==2,'candidate_two_offline_renders_same_bytes':img==(d/'replay_2.png').read_bytes(),'native_primary_completed_before_call':(d/'primary_review.json').stat().st_mtime<=(t/'run_01_started.json').stat().st_mtime,'difference_audit_before_call':(d/'design_difference_audit.json').stat().st_mtime<=(t/'run_01_started.json').stat().st_mtime,'current_original_approval_and_eligibility':formal['eligible'],'all_marks_actual_visible':read(d/'marker_chroma_audit.json')['all_visible'],'all_paths_exact':read(d/'marker_chroma_audit.json')['all_path_bindings_exact']}
    runs=[]
    for i in (1,2):
        raw=t/f'run_{i:02d}_response.json';payload=json.loads(raw.read_bytes());job=read(t/f'run_{i:02d}.json');started=read(t/f'run_{i:02d}_started.json');choice=payload['choices'][0]
        rc={'http200':job['http_status']==200,'completed':job['status']=='completed','finish_stop':choice['finish_reason']=='stop','not_truncated':not job['truncated'],'full_content_exactly_retained':job['answer']==choice['message']['content'],'raw_response_sha256':hashfile(raw)==job['response_sha256'],'same_image_design_request':all(job[k]==binding[k] and started[k]==binding[k] for k in ('image_sha256','design_sha256','request_body_sha256')),'no_reasoning_tokens':payload['usage']['completion_tokens_details']['reasoning_tokens']==0}
        runs.append({'run_index':i,'checks':rc,'raw_response_path':str(raw),'raw_response_sha256':hashfile(raw),'full_answer_text':choice['message']['content'],'started_at':started['started_at'],'finished_at':job['finished_at']})
    assert all(checks.values()),checks
    assert all(all(x['checks'].values()) for x in runs)
    result={'question_id':q,'variant_id':design['variant_id'],'checked_at_utc':datetime.now(timezone.utc).isoformat(),'all_checks_passed':True,'checks':checks,'binding':binding,'exact_artifact_paths':{name:str(d/name) for name in ('design.json','plugin.json','candidate.png','context.json','path_fingerprints.json','math_proof.json','primary_review.json','marker_chroma_audit.json','design_difference_audit.json')},'request_path':str(t/'request.json'),'summary_path':str(t/'summary.json'),'runs':runs,'limits':'Exact local frozen evidence audit. No provider-side exhaustive ledger or causal/statistical result claimed.'}
    write(d/'frozen_evidence_audit.json',result);return result

if __name__=='__main__':
    results=[]
    for f in OWN.glob('Plane*/r48_*/design.json'):
        d=f.parent
        if list((d/'tests').glob('quicktest3_*/summary.json')):
            a=audit(d);results.append({'question_id':a['question_id'],'variant_id':a['variant_id'],'all_checks_passed':a['all_checks_passed'],'audit_path':str(d/'frozen_evidence_audit.json')});print(a['question_id'],'bindings verified',flush=True)
    write(OWN/'evidence_binding_audit.json',{'candidates':results})
