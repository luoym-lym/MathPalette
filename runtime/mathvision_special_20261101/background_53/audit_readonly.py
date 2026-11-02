from research import *
import base64
from prepare_designs import PROOFS,SKIPS

def main():
    history=read(OWN/'history_inventory.json')
    files={}
    parsed=[];bad=[];raw=[];requests=[]
    for qid,entries in history['histories'].items():
        for e in entries:
            p=Path(e['path']);data=p.read_bytes();assert sha(p)==e['sha256']
            files[str(p)]=sha(p)
            if p.suffix!='.json':continue
            try:value=json.loads(data.decode('utf-8-sig'))
            except (UnicodeDecodeError,json.JSONDecodeError) as error:
                bad.append({'path':str(p),'bytes':len(data),'sha256':sha(p),'error':str(error),'preserved_without_repair':True})
                continue
            parsed.append({'path':str(p),'sha256':sha(p),'bytes':len(data)})
            if p.name.endswith('_response.json'):
                raw.append({'question_id':qid,'path':str(p),'sha256':sha(p),'response':value})
            if p.name=='request.json':
                binding=read(p.parent/'binding.json')
                actual_image=base64.b64decode(value['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
                requests.append({'question_id':qid,'path':str(p),'sha256':sha(p),'matches_binding_request':sha(p)==binding['request_body_sha256'],'embedded_image_matches_binding':hashlib.sha256(actual_image).hexdigest()==binding['image_sha256'],'only_formal_question':value['messages'][1]['content'][0]['text']==binding['question'],'keys':list(value),'preset':binding['expected_wrong_answer']})
    semantics=[]
    for entry in history['semantic_rejects']:
        p=Path(entry['path']);data=p.read_bytes();value=json.loads(data.decode('utf-8-sig'))
        assert sha(p)==entry['sha256'];files[str(p)]=sha(p)
        # Preserve full parsed document in our own read-through, with no repair or rewrite of its source.
        semantics.append({'source':str(p),'sha256':sha(p),'bytes_fully_read':len(data),'report':value})
    helpers=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json','SolidGeometry/workbench/config.json','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/renderer_adapter.py','SolidGeometry/workbench/workbench_io.py','SolidGeometry/workbench/quick_test.py','dataset_tools/mathvision_workbench.py','dataset_tools/catalog.py','runtime/mathvision_special_20261101/runtime_isolation.py','runtime/mathvision_special_20261101/delivery_bridge_adapter.py','runtime/mathvision_special_20261101/harness/quicktest3_isolated.py','runtime/mathvision_special_20261101/background_53_brief.txt','runtime/mathvision_special_20261101/background_53_assignment.json','runtime/mathvision_special_20261101/continuation_brief.txt','runtime/mathvision_special_20261101/annotation_semantics_lessons_20261102.json','runtime/mathvision_special_20261101/annotation_semantics_lesson_plane242_r24_20261102.json']
    for rel in helpers:files[str(PROJECT/rel)]=sha(PROJECT/rel)
    references=[]
    for n in range(1,15):
        p=SHARED/f'batch_{n:02d}'/'manifest.json';manifest=read(p);files[str(p)]=sha(p)
        references.append({'batch':n,'manifest_sha256':sha(p),'mechanisms':[{k:c.get(k) for k in ['question_id','mechanism','expected_wrong_answer','original_control_answers','quality_review']} for c in manifest['candidates']]})
    for qid in IDS:
        elig=eligibility(qid)
        for rel,digest in elig['formal_input_binding']['files'].items():
            files[str((BRANCH/rel).resolve())]=digest
        record=elig['record']
        # Read the complete exact native item documents and canonical formal scene; snapshot only inside own root.
        docs=[]
        for rel in [record['scene'],record['script'],*[r for r in record['runtime_dependencies'] if '/items/' in r]]:
            p=BRANCH/rel;text=p.read_text(encoding='utf-8-sig')
            docs.append({'path':str(p),'sha256':sha(p),'full_text':text})
        dump(OWN/qid/'complete_frozen_source_documents_read.json',docs)
    dump(OWN/'old_full_raw_and_request_readthrough.json',{'raw_responses':raw,'request_checks':requests,'invalid_historical_json':bad,'all_history_json_full_read':parsed,'old_manual_final_disposition':{'Solid238':'First completed final1040 missed448; second aborted, no valid pair. Never retry this image.','Solid241':'Old assessment no design/no API, mathematical mapping concern retained.','Solid242':'96pi+120 twice missed96pi.','Solid243':'45 twice for each of two separate60-preset designs; both MISS.','Solid244':'120 twice missed60.','Solid245':'256pi twice missed228pi.','Solid246':'3pi/4 twice missed3pi/2.','Solid248':'5 twice missed20.'},'existing_original_controls_in_this_history':[]})
    dump(OWN/'complete_independent_reject_readthrough.json',semantics)
    dump(OWN/'reference_mechanisms.json',references)
    dump(OWN/'readonly_snapshot_before_calls.json',{'at':now(),'files':files,'scope':'All8 question input files and assigned historical evidence; relevant shared renderer/harness/protocol files and exact independent rejects. Mutable global progress is diagnostic, not a frozen original.'})
    dump(OWN/'source_native_read_receipts.json',{'at':now(),'source_and_formal_images_actually_viewed':[str(BRANCH/s/qid)+ext for qid in IDS for s,ext in [('originals','.jpg'),('image','.png')]],'old_images_actually_viewed':[e['path'] for es in history['histories'].values() for e in es if e['path'].endswith('candidate.png')],'canonical_scenes_completely_read':IDS,'formal_full_wording_read':IDS,'old_designs_presets_and_full_raw_responses_manually_read':True,'all_old_files_parsed_and_hashed_in_full':True,'independent_reject_files_fully_parsed':history['semantic_rejects'],'lessons_applied':'A reasonable transported physical-ink reading with no valid option is a blocking ambiguity, not cured by an author-only annotation assertion. These numerical problems are examined individually; no blanket color ban or new equality/coplananarity is inferred.','mathematical_primary_proofs':PROOFS,'skip_reasons':SKIPS})
    print(json.dumps({'old_full_raw_response_count':len(raw),'historical_bad_json_count':len(bad),'old_request_count':len(requests),'protected_readonly_files':len(files),'all_request_checks_pass':all(x['matches_binding_request'] and x['embedded_image_matches_binding'] and x['only_formal_question'] for x in requests)},ensure_ascii=False))

if __name__=='__main__':main()
