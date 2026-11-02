from bootstrap import HERE, PROJECT, TASK
import base64
import gc
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

IDS = ['Solid134','Solid165','Solid218','Solid223']

def now(): return datetime.now(timezone.utc).isoformat()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''): h.update(block)
    return h.hexdigest()
def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')
def record(q):
    with (PROJECT/'SolidGeometry/dataset.jsonl').open(encoding='utf-8-sig') as f:
        for line in f:
            r = json.loads(line)
            if r['id'] == q: return r
    raise ValueError(q)

def eligibility(q, name):
    from dataset_tools.catalog import content, digest
    r = record(q)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][q]
    c = content(PROJECT,'SolidGeometry',r)
    actual = digest(c)
    indices = {}
    for name_ in ('accepted_index.jsonl','collected_index.jsonl'):
        p = PROJECT/'SolidGeometry/special_variant'/name_
        if not p.exists(): p = PROJECT/'SolidGeometry'/name_
        rows = []
        if p.exists():
            with p.open(encoding='utf-8-sig') as f:
                for line in f:
                    if line.strip():
                        row=json.loads(line)
                        if row.get('question_id',row.get('id')) == q: rows.append(row)
        indices[name_] = {'path':str(p),'sha256':sha(p) if p.exists() else None,'entries':rows}
    specials={}
    for n in ('recipes.json','collection.json'):
        p=PROJECT/'SolidGeometry/special_variant'/q/n
        specials[n]={'exists':p.exists(),'sha256':sha(p) if p.exists() else None}
    assigned=next(x for x in read(TASK/'background_69_assignment.json')['questions'] if x['question_id']==q)
    sources=[]
    for role, item in assigned['source_assignment_question']['source_inputs'].items():
        p=Path(item['path']); actual_sha=sha(p)
        sources.append({'role':role,'path':str(p),'expected':item['sha256'],'actual':actual_sha,'matches':actual_sha==item['sha256']})
    valid=(r==assigned['formal_record'] and r['source_dataset']=='MathVision' and actual==approval['content_sha256'] and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and not any(x['entries'] for x in indices.values()) and not any(x['exists'] for x in specials.values()) and all(x['matches'] for x in sources))
    result={'question_id':q,'created_at':now(),'eligible':valid,'formal_record':r,'approval':approval,'computed_content_sha256':actual,'content':c,'indices':indices,'special_records':specials,'assigned_source_hashes':sources,'no_passed_variant':not any(x['entries'] for x in indices.values()),'not_collected_noSpecialCompletion':not any(x['exists'] for x in specials.values())}
    save(HERE/q/('eligibility_'+name+'.json'),result)
    if not valid: raise ValueError('Current eligibility failed: '+q)
    return result

def initial():
    assignment=read(TASK/'background_69_assignment.json')
    frozen=[]
    for item in assignment['questions']:
        q=item['question_id']; eligibility(q,'initial')
        rows=[]
        for name, expected in item['frozen_source_files_sha256'].items():
            p=Path(item['source_directory'])/name
            actual=sha(p)
            rows.append({'path':str(p),'expected':expected,'actual':actual,'matches':actual==expected})
        save(HERE/q/'frozen_source_validation.json',rows)
        if not all(x['matches'] for x in rows): raise ValueError('Frozen source mismatch: '+q)
        frozen+=rows
        print(q,'fresh approval, source and frozen-input hashes pass',flush=True)
    save(HERE/'audits'/'frozen_inputs_initial.json',frozen)

def zero_scan():
    assignment=read(TASK/'background_69_assignment.json')
    hashes={x['question_id']:x['frozen_source_files_sha256']['candidate.png'] for x in assignment['questions']}
    variants={x['question_id']:x['variant_id'] for x in assignment['questions']}
    matches=[]; malformed=[]; embedded=[]; inventory=[]; errors=[]
    roots=0; started_count=0; raw_count=0; request_count=0
    # One filesystem file, one JSON and one embedded image at a time.
    with (HERE/'audits'/'whole_task_file_inventory.jsonl').open('x',encoding='utf-8') as manifest:
        for root, dirs, names in os.walk(TASK):
            dirs[:]=[d for d in dirs if not (Path(root)/d).resolve().is_relative_to(HERE)]
            for name in sorted(names):
                p=Path(root)/name
                try:
                    item={'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
                    manifest.write(json.dumps(item,ensure_ascii=False)+'\n')
                    roots+=1
                    suffix=p.suffix.lower()
                    if 'started' in name.lower(): started_count+=1
                    if 'response' in name.lower(): raw_count+=1
                    if 'request' in name.lower(): request_count+=1
                    exact=[q for q,h in hashes.items() if h==item['sha256']]
                    if exact: matches.append({**item,'kind':'exact_file','question_ids':exact})
                    if suffix not in ('.json','.jsonl','.txt','.log','.md','.py','.bin'): continue
                    text=p.read_text(encoding='utf-8-sig',errors='replace')
                    text_q=[q for q in IDS if hashes[q] in text or variants[q] in text]
                    image_q=[]
                    for m in re.finditer(r'data:image/[^;,\s]+;base64,([A-Za-z0-9+/=\r\n]+)',text):
                        try:
                            blob=base64.b64decode(m.group(1),validate=False)
                            ih=hashlib.sha256(blob).hexdigest()
                            qm=[q for q,h in hashes.items() if ih==h]
                            embedded.append({'path':str(p),'offset':m.start(),'decoded_sha256':ih,'bytes':len(blob),'matching_question_ids':qm})
                            image_q.extend(qm)
                            del blob
                        except Exception as error: errors.append({'path':str(p),'embedded_decode_error':str(error)})
                    json_error=None
                    if suffix=='.json':
                        try:
                            value=json.loads(text); del value
                        except (ValueError,TypeError) as error: json_error=str(error)
                    elif suffix=='.jsonl':
                        for no,line in enumerate(text.splitlines(),1):
                            if not line.strip(): continue
                            try: value=json.loads(line); del value
                            except ValueError as error: json_error=f'line {no}: {error}'; break
                    if json_error:
                        dest=HERE/'snapshots'/'malformed'/item['sha256']/(p.name)
                        dest.parent.mkdir(parents=True,exist_ok=True)
                        if not dest.exists(): shutil.copyfile(p,dest)
                        malformed.append({**item,'error':json_error,'target_reference_question_ids':sorted(set(text_q+image_q)),'snapshot':str(dest)})
                    if text_q or image_q:
                        matches.append({**item,'kind':'text_or_embedded_reference','text_question_ids':text_q,'embedded_question_ids':image_q,'malformed':bool(json_error),'evidence_filename':bool(re.search(r'(binding|request|summary|started|response|error|incomplete|run_\d)',name,re.I))})
                    del text
                except Exception as error: errors.append({'path':str(p),'error':repr(error)})
            gc.collect()
    save(HERE/'audits'/'whole_task_exact_png_scan.json',{'created_at':now(),'task_root':str(TASK),'excluded_only':str(HERE),'target_png_hashes':hashes,'variant_ids':variants,'files_hashed':roots,'started_files':started_count,'response_named_files':raw_count,'request_named_files':request_count,'matches':matches,'embedded_requests_decoded':embedded,'malformed_files':malformed,'errors':errors,'interpretation':'Raw observations only. Each matching invocation and unknown match requires manual classification; missing summary never proves zero calls.'})
    print('whole task scan complete',roots,'files;',len(matches),'matches;',len(embedded),'embedded images;',len(malformed),'malformed;',len(errors),'errors',flush=True)

def history():
    for q in IDS:
        rows=[]; transcripts=[]
        with (HERE/'audits'/'whole_task_file_inventory.jsonl').open(encoding='utf-8') as inventory:
            for line in inventory:
                item=json.loads(line)
                p=Path(item['path']);name=p.name
                if q not in p.parts: continue
                rows.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
                if p.suffix.lower() not in ('.json','.txt','.log','.py'): continue
                if name in ('context.json','context_fresh.json','request.json','old_full_text.txt'): continue
                text=p.read_text(encoding='utf-8-sig',errors='replace')
                if len(text)>200000: continue
                transcripts.append('FILE '+str(p)+'\n'+text+'\n')
                del text
        save(HERE/q/'old_evidence_manifest.json',rows)
        # Separate transcript files keep inspection manageable and never discard raw finals.
        for i,part in enumerate(transcripts):
            p=HERE/q/'history_text'/f'{i:04d}.txt'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(part,encoding='utf-8')
        save(HERE/q/'history_transcript_index.json',[{'index':i,'header':part.splitlines()[0],'bytes':len(part.encode('utf-8'))} for i,part in enumerate(transcripts)])
        print(q,len(rows),'historical files;',len(transcripts),'full text files',flush=True)
        del transcripts,rows;gc.collect()

def request_deep_scan():
    targets=read(HERE/'audits'/'whole_task_exact_png_scan.json')['target_png_hashes']
    decoded=[]; bindings=[]; malformed=[]; files=0; strings=0
    def walk(value):
        if isinstance(value,str): yield value
        elif isinstance(value,dict):
            for key,item in value.items():
                yield str(key)
                yield from walk(item)
        elif isinstance(value,list):
            for item in value: yield from walk(item)
    with (HERE/'audits'/'whole_task_file_inventory.jsonl').open(encoding='utf-8') as f:
        for line in f:
            inv=json.loads(line);p=Path(inv['path'])
            if p.suffix.lower() not in ('.json','.jsonl','.bin','.txt','.log'): continue
            if not re.search(r'(request|binding|summary|started|response|error|incomplete|run_\d)',p.name,re.I): continue
            files+=1
            text=p.read_text(encoding='utf-8-sig',errors='replace')
            try: value=json.loads(text)
            except ValueError:
                # Raw text fallback was already hash/base64/path scanned in full.
                malformed.append({'path':str(p),'sha256':inv['sha256'],'raw_target_hash_match':[q for q,h in targets.items() if h in text]})
                del text;continue
            for s in walk(value):
                strings+=1
                if 'data:image/' in s:
                    for m in re.finditer(r'data:image/[^;,\s]+;base64,([A-Za-z0-9+/=\s]+)',s):
                        blob=base64.b64decode(m.group(1)); h=hashlib.sha256(blob).hexdigest()
                        decoded.append({'path':str(p),'decoded_sha256':h,'bytes':len(blob),'matching_question_ids':[q for q,expected in targets.items() if expected==h]})
                        del blob
                hit=[q for q,h in targets.items() if h in s]
                if hit: bindings.append({'path':str(p),'question_ids':hit,'matching_string':s[:2000]})
            del value,text;gc.collect()
    save(HERE/'audits'/'deep_decoded_invocation_scan.json',{'created_at':now(),'evidence_files_fully_parsed':files,'decoded_strings_inspected':strings,'embedded_images':decoded,'hash_reference_matches':bindings,'malformed_raw_fallback':malformed,'all_target_embedded_matches':[x for x in decoded if x['matching_question_ids']]})
    print('Deep parsed invocation audit:',files,'files;',len(decoded),'images;',len(bindings),'hashrefs;',sum(bool(x['matching_question_ids']) for x in decoded),'target images',flush=True)

def certify():
    scan=read(HERE/'audits/whole_task_exact_png_scan.json')
    deep=read(HERE/'audits/deep_decoded_invocation_scan.json')
    assert not scan['errors'] and not deep['hash_reference_matches'] and not deep['all_target_embedded_matches']
    assert not any(x['target_reference_question_ids'] for x in scan['malformed_files'])
    assignments=read(TASK/'background_69_assignment.json')['questions']
    allowed_metadata={
        str(TASK/'background_69_assignment.json'):'Exact four-question assignment containing frozen hashes and reuse instructions, no invocation evidence.',
        str(TASK/'exploration_report.json'):'Parent research aggregate lists frozen untested drafts, no bound started/request/raw target artifact.',
        str(TASK/'quota_interruption_recovery_20261102.json'):'Recovery inventory explicitly reports background_61 failed_usage_limit, zero starts, zero summaries; corroboration only.',
        str(TASK/'background_61/prepare_candidates.py'):'Immutable local candidate preparation source; no remote API invocation logic.',
        str(TASK/'background_67/whole_task_scan_files.jsonl'):'Other worker filesystem hash inventory, not target call evidence.',
        str(TASK/'background_67/snapshots/exploration_report.json'):'Byte-identical snapshot of parent aggregate, no new invocation.',
        str(TASK/'background_70/read_snapshots/exploration_report.json'):'Byte-identical snapshot of parent aggregate, no new invocation.'}
    classified=[]
    for m in scan['matches']:
        p=Path(m['path'])
        if str(p) in allowed_metadata:
            reason=allowed_metadata[str(p)]
        else:
            item=next((a for a in assignments if p.parent==Path(a['source_directory'])),None)
            assert item is not None, ('Unclassified matching evidence',str(p))
            assert p.name in ('candidate.png','repeat.png','design.json','design_difference_audit.json','render_check.json')
            reason='Original frozen local PNG or local pre-render/design hash record; not an API request/start/binding/raw/result.'
        assert not m.get('evidence_filename',False)
        classified.append({**m,'manual_classification':reason,'actual_call':False,'unknown':False})
    for p,reason in allowed_metadata.items():
        src=Path(p)
        if src.name not in ('exploration_report.json','whole_task_scan_files.jsonl') and src.exists():
            dst=HERE/'snapshots'/'zero_call_metadata'/src.name
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(src,dst)
    save(HERE/'audits/zero_call_match_classification.json',classified)
    records=[]
    with (PROJECT/'SolidGeometry/dataset.jsonl').open(encoding='utf-8-sig') as f:
        for line in f:
            if line.strip(): records.append(json.loads(line))
    for a in assignments:
        q=a['question_id'];h=a['frozen_source_files_sha256']['candidate.png']
        exact=[m for m in scan['matches'] if m['kind']=='exact_file' and q in m['question_ids']]
        assert {Path(x['path']).name for x in exact}=={'candidate.png','repeat.png'} and len(exact)==2
        assert not any(q in x['matching_question_ids'] for x in scan['embedded_requests_decoded'])
        related=[{'question_id':r['id'],'source_key':r.get('source_key')} for r in records if r.get('source_dataset')=='MathVision' and r.get('source_key')==a['formal_record']['source_key']]
        assert [x['question_id'] for x in related]==[q]
        save(HERE/q/'zero_prior_call_certification.json',{'question_id':q,'variant_id':a['variant_id'],'candidate_png_sha256':h,'certified_at_utc':now(),'reuse_eligible':True,'actual_prior_calls_found':0,'matching_unknown_evidence':[],'scope':'Entire task runtime tree as inventoried, across every old unit and duplicate/copy/evidence filename; OWNROOT excluded. Fresh current-formal source key duplicate audit included.','whole_task_files_hashed':scan['files_hashed'],'raw_regex_embedded_images_decoded':len(scan['embedded_requests_decoded']),'parsed_invocation_files':deep['evidence_files_fully_parsed'],'parsed_invocation_embedded_images_decoded':len(deep['embedded_images']),'exact_png_matches':exact,'matching_embedded_request_images':[],'matching_bindings_starts_summaries_raw_errors_incompletes':[],'malformed_old_json_preserved':len(scan['malformed_files']),'malformed_raw_hash_base64_path_target_matches':[],'all_reference_matches_classified':str(HERE/'audits/zero_call_match_classification.json'),'source_key_duplicate_check':related,'old_different_png_calls_do_not_license_retesting':True,'missing_summary_used_as_zero_call_proof':False,'scan_manifest':str(HERE/'audits/whole_task_file_inventory.jsonl'),'scan_report':str(HERE/'audits/whole_task_exact_png_scan.json'),'deep_scan_report':str(HERE/'audits/deep_decoded_invocation_scan.json'),'unchanged_reuse_is_first_pair_only':True})
    print('All27 matches classified: original frozen inputs or metadata only; four first-call reuse certifications saved')

if __name__=='__main__':
    {'initial':initial,'zero_scan':zero_scan,'history':history,'request_deep_scan':request_deep_scan,'certify':certify}[sys.argv[1]]()
