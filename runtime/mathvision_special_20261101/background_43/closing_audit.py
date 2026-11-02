import env
from env import OWN,PROJECT,SHARED
from prepare import read,dump,sha,IDS
from datetime import datetime,timezone
import json

if __name__=='__main__':
    found=[];malformed=[]
    for pattern in ['binding.json','design.json']:
        for p in SHARED.rglob(pattern):
            if p.is_relative_to(OWN):continue
            raw=p.read_bytes()
            if not any(q.encode() in raw for q in IDS):continue
            try:d=json.loads(raw.decode('utf-8-sig'))
            except (UnicodeError,json.JSONDecodeError) as e:
                malformed.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'error':str(e),'immutable_bytes_preserved':True,'not_a_no_call_claim':True});continue
            if d.get('question_id',d.get('id')) in IDS:
                found.append({'path':str(p),'sha256':sha(p),'question_id':d.get('question_id',d.get('id')),'type':pattern,'expected_wrong_answer':d.get('expected_wrong_answer'),'image_sha256':d.get('image_sha256',d.get('png_sha256'))})
    same_raw=[]
    for q in ['Plane402','Plane409']:
        for mp in (SHARED/'background_17'/q).rglob('manual_final_review.json'):
            d=read(mp)
            for r in d['manual_reviews']:
                raw=read(r['raw_response']);actual=raw['choices'][0]['message']['content']
                same=actual==r['complete_final'];assert same
                same_raw.append({'question_id':q,'raw_path':r['raw_response'],'sha256':sha(r['raw_response']),'full_raw_content_equals_complete_text_manually_read':same,'old_final':r['manual_final'],'old_target_hit':r['manual_hit']})
    dump(OWN/'history_discovery_completion.json',{'all_shared_binding_and_design_scan':found,'relevant_malformed':malformed,'old_raw_text_equivalence':same_raw,'bytes_not_repaired_or_modified':True,'additional_own_question_api_calls_found_beyond_reviewed_history':False})
    errors=[{'phase':'precall_native_QA','question_id':'Plane407','event':'First native_audit.py invocation stopped at assertion of original black centre pixels.','resolution':'Untested draft preserved HOLD, same new hypothesis repaired before any API. All original centre pixels black in tested draft.','API_call_impact':0},{'phase':'postcall_report_writer','event':'Initial finalize.py exited ModuleNotFoundError: workbench_io before reading/test processing.','resolution':'Own report writer sys.path corrected, then completed. No request retried and no frozen solver evidence altered.','API_call_impact':0}]
    dump(OWN/'local_tooling_errors.json',errors)
    cp=read(OWN/'checkpoint.json');cp['counts']['postcall_bookkeeping_errors_fixed_without_API']=1;cp['local_non_API_failures']=errors
    cp['history_discovery_completion']=str(OWN/'history_discovery_completion.json')
    cp['no_live_own_API_processes']=True
    cp['own_API_process_exit_records']=[{'path':str(p),'record':read(p),'sha256':sha(p)} for p in OWN.glob('Plane*/r43_*/api_process_finished.json')]
    assert len(cp['own_API_process_exit_records'])==4
    cp['closed_at_utc']=datetime.now(timezone.utc).isoformat()
    dump(OWN/'checkpoint.json',cp)
    # Record all final evidence artifacts, excluding volatile caches and this index itself.
    files={}
    for p in OWN.rglob('*'):
        if p.is_file() and not any(x in p.parts for x in ['cache','mplcache','tmp','render_tmp','mpl_cache']):
            if p.name!='evidence_manifest.json':files[str(p.relative_to(OWN))]={'sha256':sha(p),'bytes':p.stat().st_size}
    dump(OWN/'evidence_manifest.json',{'created_at_utc':datetime.now(timezone.utc).isoformat(),'files':files,'frozen_source_and_prior_evidence_preserved':True})
    print(json.dumps({'historical_bindings_designs':found,'malformed':len(malformed),'raw_texts_verified':len(same_raw),'evidence_files':len(files),'own_API_exit_records':len(cp['own_API_process_exit_records'])},ensure_ascii=False))
