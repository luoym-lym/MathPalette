import review_bootstrap as r
import base64
import json
import traceback

def main():
    q=next(x for x in r.read(r.TASK/'history_index.json')['questions'] if x['question_id']=='Plane461')
    current_hash=r.sha(r.CAND/'candidate.png')
    old=[]; tracked={}
    for d in q['designs']:
        root=r.PROJECT/d['directory']
        design=r.read(root/'design.json')
        item={'directory':str(root),'preset':design['expected_wrong_answer'],
              'image_sha256':r.sha(root/'candidate.png'),'same_as_assigned_image':r.sha(root/'candidate.png')==current_hash,
              'mechanism':design['mechanism'],'full_raw_responses':[]}
        for p in sorted(root.rglob('*')):
            if p.is_file(): tracked[str(p.relative_to(r.PROJECT)).replace('\\','/')]=r.sha(p)
        for t in sorted((root/'tests').glob('quicktest3_*')):
            item['request_sha256']=r.sha(t/'request.json')
            for p in sorted(t.glob('run_??_response.json')):
                raw=r.read(p)
                item['full_raw_responses'].append({'path':str(p),'sha256':r.sha(p),'content':raw['choices'][0]['message']['content'],'finish_reason':raw['choices'][0]['finish_reason']})
        item['independent_manual_final_letters']=['B','B'] if 'background_26' in str(root) else ['C','D']
        item['independent_preset_hits']=[v==item['preset'] for v in item['independent_manual_final_letters']]
        item['history_interpretation']='Preserve explicit letters. Earlier D preset B/B is a miss despite run1 central-cluster prose. Earlier C preset C/D is partial hit, never paired success.'
        old.append(item)
    r.save(r.OWN/'additional_old_sources_before.json',tracked)
    # Inventory the retained request evidence across both runtime roots, including
    # copies, without inferring zero calls from candidate-local folders alone.
    matches=[]; errors=[]; examined=0; candidate_starts={}; request_copies=[]
    question=r.read(r.CAND/'reference_transfer.json')['independent_formal_stem']
    test=next((r.CAND/'tests').iterdir())
    request_hash=r.sha(test/'request.json')
    for root in (r.PROJECT/'runtime',r.PROJECT/'.runtime'):
        for p in root.rglob('request.json'):
            if p.is_relative_to(r.OWN): continue
            examined+=1
            try:
                req=r.read(p)
                texts=[]; images=[]
                for msg in req.get('messages',[]):
                    content=msg.get('content')
                    if isinstance(content,str) and msg.get('role')=='user': texts.append(content)
                    if isinstance(content,list):
                        for block in content:
                            if block.get('type')=='text': texts.append(block.get('text'))
                            if block.get('type')=='image_url':
                                url=block.get('image_url',{}).get('url','')
                                if url.startswith('data:image/png;base64,'):
                                    images.append(r.hashlib.sha256(base64.b64decode(url.split(',',1)[1],validate=True)).hexdigest())
                same_q=question in texts
                same_image=current_hash in images
                if same_q or same_image:
                    rec={'request_path':str(p),'request_sha256':r.sha(p),'same_question':same_q,'same_assigned_PNG':same_image,'embedded_image_hashes':images,'starts':[],'errors_or_aborts':[]}
                    for start_path in sorted(p.parent.glob('run_??_started.json')):
                        start=r.read(start_path); rec['starts'].append(start)
                        if same_image and same_q:
                            candidate_starts.setdefault(start['run_id'],[]).append(str(start_path))
                    for ep in sorted(p.parent.glob('*')):
                        if ep.is_file() and any(w in ep.name.lower() for w in ('error','abort','incomplete')):
                            rec['errors_or_aborts'].append({'path':str(ep),'sha256':r.sha(ep)})
                    matches.append(rec)
                if r.sha(p)==request_hash: request_copies.append(str(p))
            except Exception as exc:
                errors.append({'path':str(p),'error_type':type(exc).__name__,'error':str(exc)})
    orphan_image_starts=[]; all_started_examined=0
    for root in (r.PROJECT/'runtime',r.PROJECT/'.runtime'):
        for p in root.rglob('run_*_started.json'):
            if p.is_relative_to(r.OWN): continue
            all_started_examined+=1
            try:
                start=r.read(p)
                if start.get('image_sha256')==current_hash:
                    if not (p.parent/'request.json').is_file(): orphan_image_starts.append(str(p))
                    aliases=candidate_starts.setdefault(start['run_id'],[])
                    if str(p) not in aliases: aliases.append(str(p))
            except Exception as exc:
                errors.append({'path':str(p),'error_type':type(exc).__name__,'error':str(exc)})
    out={'at':r.now(),'history_index_sha256':r.sha(r.TASK/'history_index.json'),
        'old_designs_and_complete_raw_readings':old,'retained_request_files_examined':examined,
        'same_question_or_same_image_request_matches':matches,'assigned_exact_request_copies':request_copies,
        'assigned_question_and_PNG_unique_started_run_ids':candidate_starts,
        'assigned_question_and_PNG_exactly_two_unique_started_runs':len(candidate_starts)==2,
        'all_started_files_examined':all_started_examined,
        'same_image_starts_without_request':orphan_image_starts,
        'parse_errors_preserved_not_repaired':errors,
        'scope_limit':'Filesystem evidence inventory, not a claim about unrecorded external calls. Current task old-history index and retained request files across runtime/ and .runtime/ inspected. No rerun, retry, cleanup, network or original-file mutation.',
        'cross_ID_transfer':'Plane461 reference is current Plane217 C01 authorized in task.json. Reference image and candidate image are different. No transposed final-answer evidence; same-image/different-question requests would be identified separately.'}
    r.save(r.OWN/'history_audit.json',out)
    print(json.dumps({'examined':examined,'matches':[{'path':x['request_path'],'same_assigned_PNG':x['same_assigned_PNG'],'starts':len(x['starts'])} for x in matches],'current_unique_starts':len(candidate_starts),'parse_errors':errors,'old_presets_and_finals':[(x['preset'],x['independent_manual_final_letters']) for x in old]},ensure_ascii=False))

if __name__=='__main__':
    try: main()
    except BaseException as exc:
        r.save(r.OWN/('offline_error_'+r.now().replace(':','_')+'.json'),{'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()})
        raise
